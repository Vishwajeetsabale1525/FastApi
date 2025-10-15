class CalculatorError(Exception):
    """Base class for calculator exceptions"""
    pass

class DivisionByZeroError(CalculatorError):
    """Exception raised when dividing by zero"""
    pass

class InvalidOperationError(CalculatorError):
    """Exception raised for invalid operations"""
    pass
