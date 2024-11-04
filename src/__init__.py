from flask import Flask

from src.api.errors_handler import exception_handler
from src.api.v1 import api as api_v1


def create_app():
    app = Flask(__name__)
    init(app)
    return app


def init(app):
    app.register_error_handler(404, resource_not_found_error)
    app.register_error_handler(405, method_not_allowed_error)

    app.register_blueprint(api_v1, url_prefix="/api/v1")


def resource_not_found_error(_):
    return exception_handler("Resource not found", 404)


def method_not_allowed_error(_):
    return exception_handler("Method not allowed", 405)
