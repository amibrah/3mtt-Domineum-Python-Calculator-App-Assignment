class Calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def divide(self):
        return self.a / self.b

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

calc = Calculator(a, b)

print(f'Subtraction of {a} and {b} is {calc.subtract()}')
print(f'Sum of {a} and {b} is {calc.sum()}')
print(f'Multiplication of {a} and {b} is {calc.multiply()}')
print(f'Division of {a} and {b} is {calc.divide()}')