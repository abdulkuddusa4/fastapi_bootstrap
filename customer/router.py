from fastapi import APIRouter, Depends

from db import SessionDep
from .models import Job

from sqlmodel import select

from auth.utils import authenticate, authenticate_driver, authenticate_customer

from .schemas.request import CreateJobRequest
from . import services

customer_router = APIRouter()


@customer_router.get("/check")
async def helo(db: SessionDep, claim = Depends(authenticate_customer)):

	job = Job(
		customer_id=32,
		start_lat=2,
		start_lng=23.3,
		end_lat=2,
		end_lng=23.3
	)
	a = db.add(job)
	await db.commit()
	return job

@customer_router.post("/create-job")
async def create_job(
	db: SessionDep,
	claim = Depends(authenticate_customer),
	payload: CreateJobRequest=None
)->Job:
	return await services.create_job(db, payload)