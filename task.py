from abc import ABC, abstractmethod
import logging


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return f"({self.real} + {self.imaginary}i)"


class Calculator(ABC):
    @abstractmethod
    def calculate(self, num1, num2):
        pass


class ComplexCalculator(Calculator):
    def calculate(self, num1, num2):
        logging.info(f"Performing calculation: {num1} + {num2}")
        result_real = num1.real + num2.real
        result_imaginary = num1.imaginary + num2.imaginary
        return ComplexNumber(result_real, result_imaginary)


class ComplexMultiplier(Calculator):
    def calculate(self, num1, num2):
        logging.info(f"Performing calculation: {num1} * {num2}")
        result_real = (num1.real * num2.real) - (num1.imaginary * num2.imaginary)
        result_imaginary = (num1.real * num2.imaginary) + (num1.imaginary * num2.real)
        return ComplexNumber(result_real, result_imaginary)


class ComplexDivider(Calculator):
    def calculate(self, num1, num2):
        logging.info(f"Performing calculation: {num1} / {num2}")
        denominator = (num2.real ** 2) + (num2.imaginary ** 2)
        result_real = ((num1.real * num2.real) + (num1.imaginary * num2.imaginary)) / denominator
        result_imaginary = ((num1.imaginary * num2.real) - (num1.real * num2.imaginary)) / denominator
        return ComplexNumber(result_real, result_imaginary)


class CalculatorClient:
    def __init__(self):
        self.calculator = None

    def set_calculator(self, calculator):
        self.calculator = calculator

    def perform_calculation(self, num1, num2):
        if self.calculator is None:
            raise ValueError("Calculator not set!")

        return self.calculator.calculate(num1, num2)


if __name__ == "__main__":
    # Пример использования
    logging.basicConfig(level=logging.INFO)

    client = CalculatorClient()

    client.set_calculator(ComplexCalculator())
    result = client.perform_calculation(ComplexNumber(2, 3), ComplexNumber(4, 5))
    print("Сложение:", result)

    client.set_calculator(ComplexMultiplier())
    result = client.perform_calculation(ComplexNumber(2, 3), ComplexNumber(4, 5))
    print("Умножение:", result)

    client.set_calculator(ComplexDivider())
    result = client.perform_calculation(ComplexNumber(2, 3), ComplexNumber(4, 5))
    print("Деление:", result)
