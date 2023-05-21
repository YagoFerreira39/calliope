from src.domain.exceptions.exceptions import FileExtensionException


class FileValidator:
    @staticmethod
    def validate_file_extension(file_extension: str):
        suitable_extensions: list = [
            "csv", "pdf"
        ]

        if (file_extension not in suitable_extensions):
            raise FileExtensionException()
        else:
            pass
