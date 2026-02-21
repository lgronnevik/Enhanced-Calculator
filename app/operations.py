class Operation:
    """Base class for all calculator operations."""
    def execute(self, a, b):
        raise NotImplementedError("Subclasses must implement this method.")

class Add(Operation):
    def execute(self, a, b):
        return a + b

class Subtract(Operation):
    def execute(self, a, b):
        return a - b

class Multiply(Operation):
    def execute(self, a, b):
        return a * b

class Divide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

class Power(Operation):
    def execute(self, a, b):
        return a ** b

class Root(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot take root with degree 0.")
        return a ** (1 / b)

class OperationFactory:
    """Factory to create operations by name."""
    @staticmethod
    def create_operation(op_type):
        ops = {
            "add": Add,
            "subtract": Subtract,
            "multiply": Multiply,
            "divide": Divide,
            "power": Power,
            "root": Root
        }
        if op_type.lower() in ops:
            return ops[op_type.lower()]()
        else:
            raise ValueError(f"Unknown operation: {op_type}")