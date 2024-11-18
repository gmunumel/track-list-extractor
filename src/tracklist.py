from services.extractor import Extractor, TRACKLISTS_URL
from services.webdriver import WebDriver


def handler(event=None, context=None):
    session = None
    try:
        url = event.get("url", None)
        extractor = Extractor(WebDriver())
        session = extractor.extract(url)
    except Exception as e:
        return {"error": str(e)}
    return {"session": session}


if __name__ == "__main__":
    event = {
        "url": f"{TRACKLISTS_URL}/tracklist/1f00ch3k/sebastien-leger-the-moment-presents-exceptional-trips-gocek-turkey-mixmag-2021-07-04.html"
    }
    print(handler(event))
