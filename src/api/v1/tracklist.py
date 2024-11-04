"""API endpoint for extracting the tracklist from a given URL."""

from flask import request

from src.services.extractor import Extractor
from src.services.webdriver import WebDriver

from . import api


@api.route("/tracklist", methods=["POST"])
def tracklist():
    """
    Extracts the tracklist from the given URL.
    """
    extractor = Extractor(WebDriver())
    session = extractor.extract(request.json)
    return session, 200
