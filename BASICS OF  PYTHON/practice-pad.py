class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, number):
        self.result += number
        return self.result

    def subtract(self, number):
        self.result -= number
        return self.result

    def multiply(self, number):
        self.result *= number
        return self.result

    def divide(self, number):
        if number == 0:
            raise ValueError("Division by zero is not allowed.")
        self.result /= number
        return self.result

    def clear(self):
        self.result = 0

# usage
calc = Calculator()

print(calc.add(5))
print(calc.subtract(10))
print(calc.multiply(3))
print(calc.divide(2))

calc.clear()
print(calc.result)