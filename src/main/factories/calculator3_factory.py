from src.calculators.calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler

def calculator3_factory():
    numpy_handler = NumpyHandler()
    return Calculator3(numpy_handler)