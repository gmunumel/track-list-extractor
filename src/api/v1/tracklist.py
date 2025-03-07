import urllib.request

from flask import request

from src.services.extractor import TRACKLISTS_URL, Extractor
from src.services.webdriver import WebDriver
from src.log import log_info
from . import api


@api.route("/tracklist", methods=["POST"])
def tracklist():
    url = request.json.get("url", None)
    log_info(f"URL received: {url}")
    log_info(urllib.request.urlopen("https://google.com").getcode())
    log_info(urllib.request.urlopen(TRACKLISTS_URL).getcode())
    extractor = Extractor(WebDriver())
    session = extractor.extract(url)
    log_info("Extraction successful")
    return session, 200
