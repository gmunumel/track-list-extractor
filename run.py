from src.tracklist1001 import handler
from src.services.extractor import TRACKLISTS_URL

if __name__ == "__main__":
    event = {
        "url": f"{TRACKLISTS_URL}/tracklist/1f00ch3k/sebastien-leger-the-moment-presents-exceptional-trips-gocek-turkey-mixmag-2021-07-04.html"
    }
    print(handler(event))
