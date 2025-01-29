from typing import Dict, List
from .calculator_4 import Calculator4
from drivers.numpy_handler import NumpyHandler


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body
        pass


class MockDriverHandler:
    def standard_derivation(self, numbers=List[float]) -> float:
        return


# Integração entre NumpyHandler e Calculator2
# Teste de integração
def test_calculate_integration():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})

    driver = NumpyHandler()
    calculate_2 = Calculator4(driver)
    formated_response = calculate_2.calculate(mock_request)
    print()
    print(formated_response)

    assert isinstance(formated_response, dict)
    assert formated_response == {
        "data": {"Calculator": 4, "Sucess": True, "value": 2.686666666666667}
    }


def test_calculate():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})

    driver = MockDriverHandler()
    calculate_4 = Calculator4(driver)
    formated_response = calculate_4.calculate(mock_request)
    print()
    print(formated_response)

    assert isinstance(formated_response, dict)
    assert formated_response == {
        "data": {"Calculator": 4, "Sucess": True, "value": 2.686666666666667}
    }
