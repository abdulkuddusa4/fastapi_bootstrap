from typing import Annotated, Tuple
from enum import Enum

from decimal import Decimal

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class JobStatus(Enum):
    CREATED = 0
    PAID=1
    DRIVER_ACCEPTED = 2
    HELPER_PIKED = 3
    PACKAGE_PIKED = 4
    PACKAGE_DROPED = 5
    END = 6

class CarType(str, Enum):
    LITE = "LITE"
    VAN = "VAN"
    PICKUP = "PICKUP"
    XL = "XL"

class Job(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_user_id: int | None = Field(index=True)
    
    budget: Decimal = Field(default=Decimal(0.0))

    start_lat: float
    start_lng: float
    
    end_lat: float
    end_lng: float

    car_type: CarType
    
    status: JobStatus = Field(default=JobStatus.CREATED)
