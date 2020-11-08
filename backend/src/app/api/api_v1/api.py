from fastapi import APIRouter

from app.api.api_v1.endpoints import users, login, ping, bins, user_bins_data

api_router = APIRouter()
api_router.include_router(ping.router, tags=["Test"])
api_router.include_router(login.router, tags=["Login"])  
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(bins.router, prefix="/bins", tags=["Bins"])
api_router.include_router(user_bins_data.router, prefix="/users_bins_data", tags=["Bins user data"])
