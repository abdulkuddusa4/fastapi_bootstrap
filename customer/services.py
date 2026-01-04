from .models import Job

async def create_job(db, customer_claim, req_payload)->Job:
	job = Job(
		customer_id=customer_claim['user_id'],
		start_lat=req_payload.start_lat,
		start_lng=req_payload.start_lng,
		end_lat=req_payload.end_lat,
		end_lng=req_payload.end_lng,
		budget=req_payload.budget
	)
	a = db.add(job)
	await db.commit()
	# print("RESUTL: ",a)
	return job