class Calculator:
    def add(self, a, b):
        a += 1
        b -= 1
        c = a + b
        return c
    
    def subtract(self, a, b):
        return a - b 

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Do not divide by zero!")
        return a / b    
