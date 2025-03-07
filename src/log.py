from flask import current_app as app


def log_error(message, extra=None):
    app.logger.error(message, extra=extra)


def log_info(message, extra=None):
    app.logger.info(message, extra=extra)


def log_warning(message, extra=None):
    app.logger.warning(message, extra=extra)


def log_debug(message, extra=None):
    app.logger.debug(message, extra=extra)
