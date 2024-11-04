"""
This module contains pytest fixtures for testing the application.
"""

import pytest

from src import create_app


@pytest.fixture()
def app():
    """Create and configure a new app instance for testing."""
    my_app = create_app()
    my_app.config.update({"TESTING": True})

    yield my_app


@pytest.fixture()
def client(app):
    """A test client for the app."""
    return app.test_client()
