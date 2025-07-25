from typing import Optional, Dict, Any
from pydantic import BaseModel, validator


class MandiPricesQuery(BaseModel):
    format: str = "json"
    offset: Optional[int] = None
    limit: int = 10
    filters_state_keyword: Optional[str] = None
    filters_district: Optional[str] = None
    filters_market: Optional[str] = None
    filters_commodity: Optional[str] = None
    filters_variety: Optional[str] = None
    filters_grade: Optional[str] = None

    @validator("format")
    def format_must_be_valid(cls, value):
        if value not in ("json", "xml", "csv"):
            raise ValueError("format must be one of: json, xml, csv")
        return value


class MandiPriceItem(BaseModel):
    """Model for an individual mandi price record."""
    # Define fields based on the expected API response structure
    # Example: state: str, district: str, market: str, commodity: str, arrival_date: str, min_price: float, max_price: float, modal_price: float
    data: Dict[str, Any]