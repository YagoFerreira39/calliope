from http import HTTPStatus

from fastapi import UploadFile

from src.domain.messages.response_message import ResponseMessage
from src.domain.responses.response_body import ResponseBody
from src.domain.validators.file_validator import FileValidator
from src.services.template_methods.upload_files_template_methods import \
    UploadFilesTemplateMethods


class FileController:
    @staticmethod
    async def upload_file(file: UploadFile) -> ResponseBody:
        file_extension: str = file.filename.split(".")[-1]

        FileValidator.validate_file_extension(file_extension)

        template_method = UploadFilesTemplateMethods.get_template_method(
            file_extension)

        result = await template_method(file=file)

        response: ResponseBody = {
            "result": result,
            "status_code": HTTPStatus.OK,
            "message": ResponseMessage.OK_MESSAGE
        }

        return response
