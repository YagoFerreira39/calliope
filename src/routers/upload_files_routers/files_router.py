import codecs
import csv
from typing import Annotated

import multipart
from fastapi import APIRouter, File, Response, UploadFile

from src.controllers.file_controller import FileController
from src.entry_points.upload_files.upload_files_entry_point import \
    UploadFilesEntryPoint


class FilesRouter:
    __router = APIRouter()
    __tag = ["Files"]

    @classmethod
    def get_routes(cls) -> APIRouter:
        return cls.__router

    @staticmethod
    @__router.post("/file", tags=__tag)
    def upload_file(file: Annotated[bytes, File()]):
        return {"file_size": len(file)}

    @staticmethod
    @__router.post("/upload_file")
    async def upload_file(file: UploadFile) -> Response:
        response = await UploadFilesEntryPoint.process_request(
            callback=FileController.upload_file,
            params=file
        )

        return response
