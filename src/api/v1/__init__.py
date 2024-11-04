"""
This module initializes the API blueprint for version 1.
"""

from flask import Blueprint

api = Blueprint("v1", __name__)

from . import tracklist
