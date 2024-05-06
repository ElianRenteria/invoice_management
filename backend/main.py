from fastapi import FastAPI
#from core.config import settings
from router import pages_router
from fastapi.middleware.cors import CORSMiddleware


def include_router(app):
	app.include_router(pages_router)


def start_application():
	app = FastAPI(title="invoiceManager",version=0.1)
	app.add_middleware(CORSMiddleware, allow_origins=["*"],allow_credentials=True, allow_methods=["*"],allow_headers=["*"])
	include_router(app)
	return app 


app = start_application()