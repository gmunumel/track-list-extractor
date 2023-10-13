# pylint: disable=missing-function-docstring
# pylint: disable=import-error
# pylint: disable=line-too-long
from main import get_tracks_info


def test_ok():
    result = get_tracks_info(
        "https://www.1001tracklists.com/tracklist/1f00ch3k/sebastien-leger-the-moment-presents-exceptional-trips-gocek-turkey-mixmag-2021-07-04.html")
    print(result)
    assert result == "Sébastien Léger @ The Moment Presents: Exceptional Trips, Göcek, Turkey (Mixmag) 2021-07-04\n===========================================================================================\n01. Budakid - Astray In Woodland\n02. [00:05:00] Sébastien Léger - Son Of Sun [ALL DAY I DREAM]\n03. [00:11:45] Shai T - One Night In Paris [LOST MIRACLE]\n04. [00:17:30] Simone Vitullo & Tanit - Priroda (Greg Ochman Remix) [GO DEEVA]\n05. [00:23:00] Sébastien Léger - Regina Blue [ALL DAY I DREAM]\n06. [00:29:00] Sébastien Léger - Lava [ALL DAY I DREAM]\n07. [00:35:00] Sébastien Léger - Feel [ALL DAY I DREAM]\n08. [00:42:00] Eli Nissan - Lyla [LOST MIRACLE]\n09. [00:48:00] Raw Main - Sacré Coeur [LOST MIRACLE]\n10. [00:54:00] Cypherpunx ft. Sian Evans - Alien (Sébastien Léger Remix) [RENAISSANCE]\n11. [01:02:00] Eli Nissan - Casablanca [LOST MIRACLE]\n12. [01:08:00] Roy Rosenfeld - Force Major [LOST & FOUND]\n13. [01:14:00] Roy Rosenfeld - Tuti [LOST MIRACLE]\n14. [01:19:30] Ólafur Arnalds - Saman (Sébastien Léger Remix)\n\nSource: https://www.1001tracklists.com/tracklist/1f00ch3k/sebastien-leger-the-moment-presents-exceptional-trips-gocek-turkey-mixmag-2021-07-04.html"
