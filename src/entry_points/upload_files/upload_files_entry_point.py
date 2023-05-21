import json
from http import HTTPStatus
from typing import Callable

from fastapi import Response

from src.domain.exceptions.exceptions import FileExtensionException
from src.domain.responses.http_response_body import HttpResponseBody


class UploadFilesEntryPoint:
    @staticmethod
    async def __process_callback(
        callback: Callable, params: any = None
    ):
        response = await callback(params)
        return response

    @staticmethod
    async def process_request(
        callback: Callable, params: any = None
    ) -> Response:
        response_body = None

        try:
            response = await UploadFilesEntryPoint.__process_callback(callback=callback, params=params)

            response_body = HttpResponseBody(
                status_code=response.get("status_code"),
                message=response.get("message"),
                result=response.get("result")
            )

        except FileExtensionException:
            response_body = HttpResponseBody(
                status_code=HTTPStatus.BAD_REQUEST,
                message="File extension not allowed.",
            )

        except Exception as exception:
            response_body = HttpResponseBody(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                message="An unexpected error occurred.",
            )

        finally:
            return response_body.build_http_response()
