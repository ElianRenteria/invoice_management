from fastapi import FastAPI
#from core.config import settings
from backend.router import pages_router


def include_router(app):
	app.include_router(pages_router)


def start_application():
	app = FastAPI(title="invoiceManager",version=0.1)
	include_router(app)
	return app 


app = start_application()