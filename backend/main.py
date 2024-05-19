from fastapi import FastAPI
from router import pages_router
from fastapi.middleware.cors import CORSMiddleware


def include_router(app):
    app.include_router(pages_router)


def create_app():
    app = FastAPI(title="invoiceManager", version=0.1)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    include_router(app)
    return app


if __name__ == '__main__':
    import uvicorn
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8080)
