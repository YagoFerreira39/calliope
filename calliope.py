import uvicorn
from decouple import config
from fastapi import FastAPI
from pyfiglet import print_figlet
from starlette.middleware.cors import CORSMiddleware

from src.routers.base_router import BaseRouter


def build_calliope() -> FastAPI:
    calliope_app = BaseRouter.initialize_routes()
    calliope_app.add_middleware(
        CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
    )


app = build_calliope()

if __name__ == '__main__':
    port = int(config("PORT"))

    print_figlet(text="Calliope", colors="50;0;39")
    uvicorn.run(app, port=port, host="0.0.0.0")
