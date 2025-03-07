import logging

from flask import Flask, Blueprint


def create_app():
    app = Flask(__name__)
    init(app)
    configure_logging(app)
    app.logger.info("Flask application track-list-extractor has started.")
    return app


def init(app):
    app.register_error_handler(404, resource_not_found)
    app.register_error_handler(405, method_not_allowed)

    api = Blueprint("api", __name__)

    from .api.v1 import api as api_v1

    api.register_blueprint(api_v1, url_prefix="/api/v1")

    app.register_blueprint(api)


def configure_logging(app):
    # Remove all handlers associated with the root logger object
    for handler in app.logger.handlers[:]:
        app.logger.removeHandler(handler)

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)


def resource_not_found(_):
    return {"error": "Resource not found"}, 404


def method_not_allowed(_):
    return {"error": "Method not allowed"}, 405
