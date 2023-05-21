from typing import TypedDict


class ResponseBody(TypedDict):
    status_code: int
    message: str
    result: dict | list[dict]
