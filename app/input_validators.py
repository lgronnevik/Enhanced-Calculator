from app.operations import OperationFactory

class InputValidator:
    """Validates user input for calculator operations."""

    @staticmethod
    def validate_command(parts):
        # expects [op, a, b]
        if len(parts) != 3:
            return False, "Command must be in format: operation a b"
        return True, ""

    @staticmethod
    def validate_numbers(a_str, b_str):
        try:
            a = float(a_str)
            b = float(b_str)
            return True, a, b
        except ValueError:
            return False, None, None

    @staticmethod
    def validate_integer(value):
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"Invalid integer: {value}")

    @staticmethod
    def validate_float(value):
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"Invalid float: {value}")

    @staticmethod
    def validate_operation(op_type):
        try:
            OperationFactory.create_operation(op_type)
            return True, ""
        except ValueError as e:
            return False, f"Invalid operation: {op_type}"