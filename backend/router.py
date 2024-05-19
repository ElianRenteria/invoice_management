from fastapi import APIRouter
from fastapi import Request

pages_router = APIRouter()


@pages_router.get("/")
async def data(request: Request):
    return {"data": "Success"}
