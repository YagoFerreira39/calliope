import codecs
import csv

from fastapi import UploadFile


class CsvService:
    __csv_reader = csv.DictReader

    @staticmethod
    async def get_csv_file_content(file: UploadFile):
        csv_file = CsvService.__csv_reader(
            codecs.iterdecode(file.file, 'utf-8'))

        content = {}

        for rows in csv_file:
            primary_key = list(rows)[0]
            key = rows[primary_key]
            content[key] = rows

        file.file.close()
        return content
