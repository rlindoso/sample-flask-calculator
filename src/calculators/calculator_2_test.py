from typing import Dict

from src.drivers.numpy_handler import NumpyHandler
from .calculator_2 import Calculator2

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest(body={ "numbers": [2.12, 4.62, 1.32] })

    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)
    calc = calculator_2.calculate(mock_request)

    assert isinstance(calc, dict)
    assert calc == {'data': {'calculator': 2, 'result': 0.08}}
