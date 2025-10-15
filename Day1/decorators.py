from functools import wraps
from context_manager import LogManager

def log_operation(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
            log_message = f"Operation: {func.__name__}, Arguments: {args}, Result: {result}\n"
        except Exception as e:
            log_message = f"Operation: {func.__name__}, Arguments: {args}, Error: {e}\n"
            raise
        # Use context manager to write logs
        with LogManager("logs/calculator.log") as log_file:
            log_file.write(log_message)
        return result
    return wrapper
