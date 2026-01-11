from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from datetime import datetime, timezone
from typing import TypedDict

from fastapi import Depends, HTTPException, status
import jwt, os
from jwt import PyJWTError

from dotenv import load_dotenv

load_dotenv()

security = HTTPBearer()
SECRET_KEY = os.environ['SECRET_KEY']

def authenticate(creds: HTTPAuthorizationCredentials = Depends(security)):

        token = creds.credentials

        try:
            payload = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=["HS256"],
            )

            exp = payload.get("exp")
            if exp is not None:
                if datetime.fromtimestamp(exp, tz=timezone.utc) < datetime.now(tz=timezone.utc):
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Token expired",
                        headers={"WWW-Authenticate": "Bearer"},
                    )

            return payload  # type: ignore[return-value]

        except PyJWTError as e:
            raise e
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token",
                headers={"WWW-Authenticate": "Bearer"},
            )


def authenticate_customer(claim = Depends(authenticate)):
    if claim.get('user_type') != 'CUSTOMER':
        raise HTTPException(
            detail={"error": "customer account required"},
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    return claim

def authenticate_ROLE_A(claim = Depends(authenticate)):
    if claim.get('user_type') != 'ROLE_A':
        raise HTTPException(
            detail={"error": "customer account required"},
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    return claim


def authenticate_ROLE_B(claim = Depends(authenticate)):
    if claim.get('user_type') != 'ROLE_B':
        raise HTTPException(
            detail={"error": "driver account required"},
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    return claim


def authenticate_ROLE_X_DEPENDS_B(claim = Depends(authenticate_ROLE_B)):
    if claim.get('user_type') != 'HELPER':
        raise HTTPException(
            {"error": "helper account required"},
            status.HTTP_401_UNAUTHORIZED
        )
    return claim

