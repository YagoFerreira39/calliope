from src.domain.enums.file_extensions_enum import FileExtensionsEnum
from src.services.csv.csv_service import CsvService


class UploadFilesTemplateMethods:
    __template_methods = {
        FileExtensionsEnum.CSV.value: CsvService.get_csv_file_content
    }

    @classmethod
    def get_template_method(cls, method: str):
        return cls.__template_methods.get(method)
