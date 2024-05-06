from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
pages_router = APIRouter()


@pages_router.get("/")
async def home(request: Request):
	return templates.TemplateResponse("dashboard.html",{"request":request})
