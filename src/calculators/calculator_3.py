from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface):
        self.__diver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        variation = self.__calculate_variation(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_results(variation, multiplication)

        return self.__format_response(variation)

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Bad format to body")
        
        input_data = body["numbers"]
        return input_data
    
    def __calculate_variation(self, input_data: List[float]) -> float:
        variation = self.__diver_handler.variation(input_data)
        return variation
    
    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1
        for num in numbers:
            multiplication *= num

        return multiplication
    
    def __verify_results(self, variation: float, multiplication: float) -> None:
        if variation < multiplication:
            raise HttpBadRequestError('Process failure: Variation smaller than multiplication')
    
    def __format_response(self, variation: float) -> Dict:
        return {
            "data": {
                "calculator": 3,
                "result": variation,
                "success": True
            }
        }
