from src.exceptions import ValidationError
from src.log import log_error
from .v1 import api


@api.errorhandler(ValidationError)
def validation_error(e):
    return exception_handler(e.args[0], e.args[1])


@api.errorhandler(Exception)
def handle_exception(e):
    return exception_handler(str(e), 500)


def exception_handler(error, status_code):
    log_error(error)
    return {"error": error}, status_code
