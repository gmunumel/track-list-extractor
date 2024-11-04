"""
This module handles errors for the API.
"""

from src.exceptions import ValidationError
from src.api.v1 import api as api_v1


@api_v1.errorhandler(ValidationError)
def validation_error(error):
    """
    Handle validation errors.
    """
    return exception_handler(error.args[0], error.args[1])


@api_v1.errorhandler(Exception)
def handle_exception(exception):
    """
    Handle general exceptions.
    """
    return exception_handler(str(exception), 500)


def exception_handler(message, status_code):
    """
    Handle exceptions by returning an error message and status code.
    """
    return {"error": message}, status_code
