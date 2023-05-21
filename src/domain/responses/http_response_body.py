import json

from fastapi import Response


class HttpResponseBody:
    def __init__(
            self,
            status_code: int,
            message: str = None,
            result: dict = None
    ):
        self.__status_code = status_code
        self.__message = message
        self.__result = result

    def __build_http_encoded_content(self) -> str:
        response = {
            "status_code": self.__status_code,
            "message": self.__message,
            "result": self.__result
        }

        return json.dumps(response)

    def build_http_response(self) -> Response:
        print(f"INTTTT: {self.__status_code}")
        return Response(
            content=self.__build_http_encoded_content(),
            status_code=self.__status_code,
            media_type="application/json"
        )
