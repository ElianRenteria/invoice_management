from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
pages_router = APIRouter()

#GET REQUESTS

@pages_router.get("/home")
async def home(request: Request):
	return templates.TemplateResponse("dashboard.html",{"request":request})

@pages_router.get("/")
async def data(request: Request):
	return {"data": "Success"}

@pages_router.get("/login/")
async def login(request: Request):
	return {"data": "Loggin in"}

@pages_router.get("/signup/")
async def signup(request: Request):
	return {"data": "Sign Up"}

#POST REQUESTS

@pages_router.post("/login")
async def loginData(request: Request):
	print("Logged In")
	print(request)

@pages_router.post("/signup")
async def signUpData(request: Request):
	print("Signed Up")
	print(request)