from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Literal
from datetime import datetime, date
import random

# Initialize FastAPI app
app = FastAPI(
    title="Vegetable Mandi Rates API",
    description="Dummy API for testing React integration with vegetable mandi rates catalog",
    version="1.0.0"
)

# Add CORS middleware for React integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your React app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic Models
class VegetableRate(BaseModel):
    id: int
    state: str
    district: str
    market: str
    commodity: str
    variety: str
    grade: str
    arrival_date: str
    min_price: float
    max_price: float
    modal_price: float
    created_at: str

class AddRateRequest(BaseModel):
    state: str
    district: str
    market: str
    commodity: str
    variety: str
    grade: str
    min_price: float
    max_price: float
    modal_price: float

class ApiResponse(BaseModel):
    success: bool
    message: str
    data: List[VegetableRate]
    total_records: int

# Dummy Data
dummy_vegetables = [
    "Tomato", "Onion", "Potato", "Carrot", "Cabbage", "Cauliflower", 
    "Brinjal", "Okra", "Green Chili", "Capsicum", "Cucumber", "Radish",
    "Spinach", "Coriander", "Mint", "Ginger", "Garlic", "Beetroot"
]

dummy_states = [
    "Punjab", "Haryana", "Uttar Pradesh", "Madhya Pradesh", "Gujarat", 
    "Maharashtra", "Karnataka", "Tamil Nadu", "Andhra Pradesh", "Rajasthan"
]

dummy_districts = {
    "Punjab": ["Ludhiana", "Amritsar", "Jalandhar", "Patiala"],
    "Haryana": ["Gurugram", "Faridabad", "Hisar", "Karnal"],
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Agra", "Varanasi"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot"]
}

dummy_markets = ["Central Market", "Vegetable Market", "Wholesale Market", "Farmers Market"]
dummy_varieties = ["Grade A", "Grade B", "Premium", "Regular", "Organic"]
dummy_grades = ["A", "B", "C"]

# In-memory storage (for demonstration)
vegetable_rates = []

def generate_dummy_data():
    """Generate dummy vegetable rates data"""
    data = []
    for i in range(100):
        state = random.choice(dummy_states)
        districts = dummy_districts.get(state, ["District A", "District B"])
        district = random.choice(districts)
        commodity = random.choice(dummy_vegetables)
        min_price = round(random.uniform(10, 50), 2)
        max_price = round(min_price + random.uniform(5, 20), 2)
        modal_price = round((min_price + max_price) / 2, 2)
        
        rate = VegetableRate(
            id=i + 1,
            state=state,
            district=district,
            market=random.choice(dummy_markets),
            commodity=commodity,
            variety=random.choice(dummy_varieties),
            grade=random.choice(dummy_grades),
            arrival_date=datetime.now().strftime("%Y-%m-%d"),
            min_price=min_price,
            max_price=max_price,
            modal_price=modal_price,
            created_at=datetime.now().isoformat()
        )
        data.append(rate)
    return data

# Initialize dummy data
vegetable_rates = generate_dummy_data()

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Vegetable Mandi Rates API",
        "version": "1.0.0",
        "description": "Dummy API for testing React integration",
        "endpoints": {
            "get_rates": "GET /api/v1/vegetable-rates",
            "add_rate": "POST /api/v1/vegetable-rates",
            "filters": "GET /api/v1/filters"
        },
        "total_records": len(vegetable_rates)
    }

@app.get("/api/v1/vegetable-rates", response_model=ApiResponse)
async def get_vegetable_rates(
    state: Optional[str] = Query(None, description="Filter by state"),
    district: Optional[str] = Query(None, description="Filter by district"),
    market: Optional[str] = Query(None, description="Filter by market"),
    commodity: Optional[str] = Query(None, description="Filter by vegetable/commodity"),
    variety: Optional[str] = Query(None, description="Filter by variety"),
    grade: Optional[str] = Query(None, description="Filter by grade"),
    limit: int = Query(50, ge=1, le=500, description="Maximum records to return"),
    offset: int = Query(0, ge=0, description="Records to skip")
):
    """
    GET method: Fetch vegetable rates with optional filters
    Perfect for testing React developers' GET request integration
    """
    try:
        # Filter data based on query parameters
        filtered_data = vegetable_rates.copy()
        
        if state:
            filtered_data = [r for r in filtered_data if state.lower() in r.state.lower()]
        if district:
            filtered_data = [r for r in filtered_data if district.lower() in r.district.lower()]
        if market:
            filtered_data = [r for r in filtered_data if market.lower() in r.market.lower()]
        if commodity:
            filtered_data = [r for r in filtered_data if commodity.lower() in r.commodity.lower()]
        if variety:
            filtered_data = [r for r in filtered_data if variety.lower() in r.variety.lower()]
        if grade:
            filtered_data = [r for r in filtered_data if grade.lower() in r.grade.lower()]
        
        # Apply pagination
        total = len(filtered_data)
        paginated_data = filtered_data[offset:offset + limit]
        
        return ApiResponse(
            success=True,
            message=f"Successfully retrieved {len(paginated_data)} vegetable rates",
            data=paginated_data,
            total_records=total
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/vegetable-rates", response_model=dict)
async def add_vegetable_rate(rate_data: AddRateRequest):
    """
    POST method: Add new vegetable rate entry
    Perfect for testing React developers' POST request integration with form handling
    """
    try:
        # Validate price logic
        if rate_data.min_price > rate_data.max_price:
            raise HTTPException(status_code=400, detail="Minimum price cannot be greater than maximum price")
        
        if not (rate_data.min_price <= rate_data.modal_price <= rate_data.max_price):
            raise HTTPException(status_code=400, detail="Modal price must be between minimum and maximum price")
        
        # Create new rate entry
        new_rate = VegetableRate(
            id=len(vegetable_rates) + 1,
            state=rate_data.state,
            district=rate_data.district,
            market=rate_data.market,
            commodity=rate_data.commodity,
            variety=rate_data.variety,
            grade=rate_data.grade,
            arrival_date=datetime.now().strftime("%Y-%m-%d"),
            min_price=rate_data.min_price,
            max_price=rate_data.max_price,
            modal_price=rate_data.modal_price,
            created_at=datetime.now().isoformat()
        )
        
        # Add to our in-memory storage
        vegetable_rates.append(new_rate)
        
        return {
            "success": True,
            "message": "Vegetable rate added successfully",
            "data": new_rate,
            "total_records": len(vegetable_rates)
        }
        
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/filters")
async def get_filter_options():
    """
    Get available filter options for React developers to build dynamic dropdowns
    """
    return {
        "states": list(set([rate.state for rate in vegetable_rates])),
        "districts": list(set([rate.district for rate in vegetable_rates])),
        "markets": list(set([rate.market for rate in vegetable_rates])),
        "commodities": list(set([rate.commodity for rate in vegetable_rates])),
        "varieties": list(set([rate.variety for rate in vegetable_rates])),
        "grades": list(set([rate.grade for rate in vegetable_rates]))
    }

@app.get("/api/v1/stats")
async def get_statistics():
    """
    Get basic statistics for dashboard creation
    """
    if not vegetable_rates:
        return {"message": "No data available"}
    
    prices = [rate.modal_price for rate in vegetable_rates]
    commodities_count = {}
    states_count = {}
    
    for rate in vegetable_rates:
        commodities_count[rate.commodity] = commodities_count.get(rate.commodity, 0) + 1
        states_count[rate.state] = states_count.get(rate.state, 0) + 1
    
    return {
        "total_records": len(vegetable_rates),
        "average_price": round(sum(prices) / len(prices), 2),
        "min_price": min(prices),
        "max_price": max(prices),
        "top_commodities": sorted(commodities_count.items(), key=lambda x: x[1], reverse=True)[:5],
        "top_states": sorted(states_count.items(), key=lambda x: x[1], reverse=True)[:5]
    }

@app.delete("/api/v1/vegetable-rates/{rate_id}")
async def delete_vegetable_rate(rate_id: int):
    """
    DELETE method: Remove a vegetable rate entry
    """
    global vegetable_rates
    
    # Find and remove the rate
    rate_to_remove = None
    for i, rate in enumerate(vegetable_rates):
        if rate.id == rate_id:
            rate_to_remove = vegetable_rates.pop(i)
            break
    
    if not rate_to_remove:
        raise HTTPException(status_code=404, detail="Rate not found")
    
    return {
        "success": True,
        "message": f"Vegetable rate with ID {rate_id} deleted successfully",
        "deleted_rate": rate_to_remove
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)