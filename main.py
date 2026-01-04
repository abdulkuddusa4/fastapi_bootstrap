from contextlib import asynccontextmanager
from dotenv import load_dotenv

from fastapi import FastAPI

from customer.router import customer_router

from db import create_db_and_tables, run_auto_migrations

import redis
from config import init_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("app startaup..")
    await run_auto_migrations()

    # app.redis_client = redis.from_url("redis://localhost")

    init_settings({
        "REDIS_CLIENT": redis.from_url("redis://localhost")
    })


    # asyncio.create_task(agent_message_handler(
    #     app.redis_client, app.AGENT_PHONE_ID
    # ))

    yield


booking_app = FastAPI(
    lifespan=lifespan
)


booking_app.include_router(customer_router, prefix="/customer")
