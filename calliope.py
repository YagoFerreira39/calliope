import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.routers.base_router import BaseRouter

calliope_app_v1 = BaseRouter.initialize_routes()

calliope_app: FastAPI = FastAPI(
    version="0.0.1"
)

calliope_app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

calliope_app.mount("/api/v1", calliope_app_v1)

if __name__ == '__main__':
    port = 4002
    uvicorn.run(calliope_app, port=port, host="0.0.0.0")

