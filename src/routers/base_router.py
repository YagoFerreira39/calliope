from fastapi import FastAPI

from src.routers.upload_files_routers.files_router import FilesRouter


class BaseRouter:
    app_v1 = FastAPI(
        title="Calliope",
        version="0.0.1"
    )

    @classmethod
    def _initialize_routes(cls) -> FastAPI:
        files_router = FilesRouter.get_routes()
        BaseRouter.app_v1.include_router(router=files_router, prefix="/file")

        return BaseRouter.app_v1

    @classmethod
    def initialize_routes(cls) -> FastAPI:
        cls._initialize_routes()

        return cls.app_v1
