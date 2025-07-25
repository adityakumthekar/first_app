from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from datetime import datetime
import httpx
import json

# Initialize FastAPI app
app = FastAPI(
    title="Mandi Rate API",
    description="API to fetch agricultural commodity rates from government mandi data",
    version="1.0.0"
)

# Pydantic Models
class MandiFilters(BaseModel):
    """Filters for mandi rate queries"""
    state: Optional[str] = Field(None, description="State name to filter by")
    district: Optional[str] = Field(None, description="District name to filter by")
    market: Optional[str] = Field(None, description="Market name to filter by")
    commodity: Optional[str] = Field(None, description="Commodity name to filter by")
    variety: Optional[str] = Field(None, description="Variety of commodity to filter by")
    grade: Optional[str] = Field(None, description="Grade of commodity to filter by")

class PaginationParams(BaseModel):
    """Pagination parameters"""
    offset: int = Field(0, ge=0, description="Number of records to skip")
    limit: int = Field(100, ge=1, le=1000, description="Maximum number of records to return")

class MandiRateRecord(BaseModel):
    """Single mandi rate record"""
    state: Optional[str] = None
    district: Optional[str] = None
    market: Optional[str] = None
    commodity: Optional[str] = None
    variety: Optional[str] = None
    grade: Optional[str] = None
    arrival_date: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    modal_price: Optional[float] = None

class MandiRateResponse(BaseModel):
    """Response model for mandi rate API"""
    success: bool = Field(description="Whether the request was successful")
    message: str = Field(description="Response message")
    total_records: int = Field(description="Total number of records available")
    returned_records: int = Field(description="Number of records in current response")
    offset: int = Field(description="Current offset")
    limit: int = Field(description="Current limit")
    data: List[MandiRateRecord] = Field(description="List of mandi rate records")

class ErrorResponse(BaseModel):
    """Error response model"""
    success: bool = False
    message: str
    error_code: Optional[str] = None

# Configuration
GOVT_API_BASE_URL = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
GOVT_API_KEY = "579b464db66ec23bdd000001bff534fa3e234b7b6057fa492bea6325"

@app.get("/", response_model=dict)
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Mandi Rate API",
        "version": "1.0.0",
        "endpoints": {
            "rates": "/api/v1/mandi-rates",
            "health": "/health",
            "docs": "/docs"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now()}

@app.get("/api/v1/mandi-rates", 
         response_model=MandiRateResponse,
         responses={
             400: {"model": ErrorResponse},
             500: {"model": ErrorResponse}
         })
async def get_mandi_rates(
    # Pagination parameters
    offset: int = Query(0, ge=0, description="Number of records to skip for pagination"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of records to return"),
    
    # Output format
    format: Literal["json", "xml", "csv"] = Query("json", description="Output format"),
    
    # Filter parameters
    state: Optional[str] = Query(None, description="Filter by state name"),
    district: Optional[str] = Query(None, description="Filter by district name"),
    market: Optional[str] = Query(None, description="Filter by market name"),
    commodity: Optional[str] = Query(None, description="Filter by commodity name"),
    variety: Optional[str] = Query(None, description="Filter by variety name"),
    grade: Optional[str] = Query(None, description="Filter by grade")
):
    """
    Fetch mandi rates from government API with filtering and pagination
    
    Returns agricultural commodity rates from various mandis across India
    """
    try:
        # Build query parameters for government API
        params = {
            "api-key": GOVT_API_KEY,
            "format": format,
            "offset": offset,
            "limit": limit
        }
        
        # Add filters if provided
        if state:
            params["filters[state.keyword]"] = state
        if district:
            params["filters[district]"] = district
        if market:
            params["filters[market]"] = market
        if commodity:
            params["filters[commodity]"] = commodity
        if variety:
            params["filters[variety]"] = variety
        if grade:
            params["filters[grade]"] = grade
        
        # Make request to government API
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(GOVT_API_BASE_URL, params=params)
            response.raise_for_status()
            
            if format == "json":
                data = response.json()
                
                # Extract records from government API response
                records = []
                if "records" in data:
                    for record in data["records"]:
                        records.append(MandiRateRecord(
                            state=record.get("state"),
                            district=record.get("district"),
                            market=record.get("market"),
                            commodity=record.get("commodity"),
                            variety=record.get("variety"),
                            grade=record.get("grade"),
                            arrival_date=record.get("arrival_date"),
                            min_price=float(record.get("min_price", 0)) if record.get("min_price") else None,
                            max_price=float(record.get("max_price", 0)) if record.get("max_price") else None,
                            modal_price=float(record.get("modal_price", 0)) if record.get("modal_price") else None
                        ))
                
                return MandiRateResponse(
                    success=True,
                    message="Data fetched successfully",
                    total_records=data.get("total", len(records)),
                    returned_records=len(records),
                    offset=offset,
                    limit=limit,
                    data=records
                )
            else:
                # For non-JSON formats, return raw response
                return response.text
                
    except httpx.TimeoutException:
        raise HTTPException(
            status_code=500,
            detail="Request timeout while fetching data from government API"
        )
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Government API error: {e.response.text}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

@app.get("/api/v1/filters/states", response_model=List[str])
async def get_available_states():
    """Get list of available states for filtering"""
    # This would typically fetch from database or cache
    # For now, returning common states
    return [
        "Andhra Pradesh", "Bihar", "Gujarat", "Haryana", "Karnataka", 
        "Madhya Pradesh", "Maharashtra", "Punjab", "Rajasthan", "Tamil Nadu",
        "Telangana", "Uttar Pradesh", "West Bengal"
    ]

@app.get("/api/v1/filters/commodities", response_model=List[str])
async def get_available_commodities():
    """Get list of available commodities for filtering"""
    return [
        "Rice", "Wheat", "Bajra", "Jowar", "Maize", "Barley",
        "Arhar", "Moong", "Urad", "Gram", "Masoor",
        "Cotton", "Sugarcane", "Jute", "Groundnut", "Mustard",
        "Sunflower", "Soybean", "Sesamum", "Castor"
    ]

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return ErrorResponse(
        success=False,
        message=exc.detail,
        error_code=str(exc.status_code)
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)