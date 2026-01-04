from decimal import Decimal
from pydantic import BaseModel, Field
from enum import Enum

# --- CarType Enum ---
class CarType(str, Enum):
    LITE = "LITE"
    VAN = "VAN"
    PICKUP = "PICKUP"
    XL = "XL"


class CreateJobRequest(BaseModel):
    budget: Decimal = Field(default=Decimal("0.0"))
    
    start_lat: float
    start_lng: float
    
    end_lat: float
    end_lng: float

    car_type: CarType

    class Config:
        schema_extra = {
            "example": {
                "budget": "100.50",
                "start_lat": 12.9716,
                "start_lng": 77.5946,
                "end_lat": 12.2958,
                "end_lng": 76.6394,
                "car_type": "LITE",
            }
        }
