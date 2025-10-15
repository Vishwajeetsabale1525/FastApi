from decorators import log_operation
from exceptions import DivisionByZeroError, InvalidOperationError

class Calculator:

    @log_operation
    def add(self, *args):
        return sum(args)

    @log_operation
    def subtract(self, *args):
        if not args:
            raise InvalidOperationError("No numbers provided for subtraction.")
        result = args[0]
        for num in args[1:]:
            result -= num
        return result

    @log_operation
    def multiply(self, *args):
        if not args:
            raise InvalidOperationError("No numbers provided for multiplication.")
        result = 1
        for num in args:
            result *= num
        return result

    @log_operation
    def divide(self, *args):
        if not args:
            raise InvalidOperationError("No numbers provided for division.")
        result = args[0]
        for num in args[1:]:
            if num == 0:
                raise DivisionByZeroError("Cannot divide by zero.")
            result /= num
        return result

    def stream_operations(self, operation, numbers):
        """
        Generator to process a stream of numbers lazily.
        operation: 'add', 'subtract', 'multiply', 'divide'
        numbers: iterable of numbers
        """
        if not numbers:
            raise InvalidOperationError("No numbers provided for streaming.")
        if operation not in ('add', 'subtract', 'multiply', 'divide'):
            raise InvalidOperationError(f"Invalid operation: {operation}")
        for i in range(1, len(numbers)+1):
            yield getattr(self, operation)(*numbers[:i])
