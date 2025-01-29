from typing import Dict, List
from flask import request as FlaskRequest

from drivers.interfaces.driver_handler_interface import DriverHandlerInterface

from errors.http_unprocessable_entity import HttpUnprocessableEntity


class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        media = self.__calculate_media(input_data)
        formated_response = self.__format_response(media)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntity("body mal formatado!")

        input_date = body["numbers"]
        return input_date

    def __calculate_media(self, numbers: List[float]) -> float:
        soma = sum(numbers)
        quantidade = len(numbers)
        media = soma / quantidade
        return media

    def __format_response(self, media: float) -> Dict:
        return {"data": {"Calculator": 4, "value": media, "Sucess": True}}
