from typing import Dict, List

from pytest import raises

from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.drivers.numpy_handler import NumpyHandler
from .calculator_3 import Calculator3

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler(DriverHandlerInterface):
    def standard_deviation(self, numbers: List[float]) -> float: pass
    
    def variation(self, numbers: List[float]) -> float:
        return 3


def test_calculate_with_variation_error():
    mock_request = MockRequest(body={ "numbers": [1, 2, 3, 4, 5] })

    driver = MockDriverHandler()
    calculator_3 = Calculator3(driver)
    
    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(excinfo.value) == 'Process failure: Variation smaller than multiplication'

def test_calculate_with_variation_error():
    mock_request = MockRequest(body={ "numbers": [1, 1, 1, 1, 3] })

    driver = MockDriverHandler()
    calculator_3 = Calculator3(driver)
    
    calc = calculator_3.calculate(mock_request)

    assert isinstance(calc, dict)
    assert calc == {'data': {'calculator': 3, 'result': 3, 'success': True}}
