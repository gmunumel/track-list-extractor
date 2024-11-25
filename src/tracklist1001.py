import logging

from src.services.extractor import Extractor
from src.services.webdriver import WebDriver

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] (tracklist1001) %(message)s",
    datefmt="%d %b %Y %H:%M:%S",
)


def handler(event=None, context=None):
    logging.info("Handler function invoked")
    session = None
    try:
        url = event.get("url", None)
        logging.info(f"URL received: {url}")
        extractor = Extractor(WebDriver())
        session = extractor.extract(url)
        logging.info("Extraction successful")
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {"error": str(e)}
    return {"session": session}
