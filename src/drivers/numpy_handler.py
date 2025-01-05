from typing import List
import numpy
from .interfaces.driver_handler_interface import DriverHandlerInterface

class NumpyHandler(DriverHandlerInterface):
    def __init__(self) -> None:
        self.__np = numpy

    def standard_deviation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers)
