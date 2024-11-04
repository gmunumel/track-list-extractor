# Track List Extractor

This is a small project to extrach track information from https://www.1001tracklists.com/. You only need to provide the url.

## Install Dependencies

Create a virtual environment to store project-related libraries. Run the following command in root folder:

    mkdir .venv

Then run the virtual environment library script with:

    python3 -m venv .venv

Activate the virtual environment:

If you are in Windows:

    .\.venv\Scripts\activate

If you are in Linux:

    source .venv/bin/activate

Then install the libraries:

    pip install -r requirements.txt

Verify that you are running Python pipenv from VScode main.py file.

## Result

For example for the url:

```
https://www.1001tracklists.com/tracklist/1f00ch3k/sebastien-leger-the-moment-presents-exceptional-trips-gocek-turkey-mixmag-2021-07-04.html
```

With the curl as:

```
curl -X POST -H "Content-Type: application/json" \
 -d '{"url": "https://www.1001tracklists.com/tracklist/1f00ch3k/sebastien-leger-the-moment-presents-exceptional-trips-gocek-turkey-mixmag-2021-07-04.html"}' \
  http://localhost:5000/tracklist 
```


Produces the output similar to this:

```
{
        "name": "Sébastien Léger @ The Moment Presents: Exceptional Trips, Göcek, Turkey (Mixmag) 2021-07-04",
        "pretty_print": "Sébastien Léger @ The Moment Presents: Exceptional Trips, Göcek, Turkey (Mixmag) 2021-07-04\n===========================================================================================\n01. Budakid - Astray In Woodland\n02. [00:05:00] Sébastien Léger - Son Of Sun [ALL DAY I DREAM]\n03. [00:11:45] Shai T - One Night In Paris [LOST MIRACLE]\n04. [00:17:30] Simone Vitullo & Tanit - Priroda (Greg Ochman Remix) [GO DEEVA]\n05. [00:23:00] Sébastien Léger - Regina Blue [ALL DAY I DREAM]\n06. [00:29:00] Sébastien Léger - Lava [ALL DAY I DREAM]\n07. [00:35:00] Sébastien Léger - Feel [ALL DAY I DREAM]\n08. [00:42:00] Eli Nissan - Lyla [LOST MIRACLE]\n09. [00:48:00] Raw Main - Sacré Coeur [LOST MIRACLE]\n10. [00:54:00] Cypherpunx ft. Sian Evans - Alien (Sébastien Léger Remix) [RENAISSANCE]\n11. [01:02:00] Eli Nissan - Casablanca [LOST MIRACLE]\n12. [01:08:00] Roy Rosenfeld - Force Major [LOST & FOUND]\n13. [01:14:00] Roy Rosenfeld - Tuti [LOST MIRACLE]\n14. [01:19:30] Ólafur Arnalds - Saman (Sébastien Léger Remix)\n\n Source: https://www.1001tracklists.com/tracklist/1f00ch3k/sebastien-leger-the-moment-presents-exceptional-trips-gocek-turkey-mixmag-2021-07-04.html",
        "source": "https://www.1001tracklists.com/tracklist/1f00ch3k/sebastien-leger-the-moment-presents-exceptional-trips-gocek-turkey-mixmag-2021-07-04.html",
        "total_tracks": "14",
        "tracks": [
            {
                "id": "tlp0_labeldata",
                "name": "Budakid - Astray In Woodland",
                "number": "01",
            },
            {
                "id": "tlp1_labeldata",
                "label": "ALL DAY I DREAM",
                "name": "Sébastien Léger - Son Of Sun",
                "number": "02",
                "time": "[00:05:00]",
            },
            {
                "id": "tlp2_labeldata",
                "label": "LOST MIRACLE",
                "name": "Shai T - One Night In Paris",
                "number": "03",
                "time": "[00:11:45]",
            },
            {
                "id": "tlp3_labeldata",
                "label": "GO DEEVA",
                "name": "Simone Vitullo & Tanit - Priroda (Greg Ochman Remix)",
                "number": "04",
                "time": "[00:17:30]",
            },
            {
                "id": "tlp4_labeldata",
                "label": "ALL DAY I DREAM",
                "name": "Sébastien Léger - Regina Blue",
                "number": "05",
                "time": "[00:23:00]",
            },
            {
                "id": "tlp5_labeldata",
                "label": "ALL DAY I DREAM",
                "name": "Sébastien Léger - Lava",
                "number": "06",
                "time": "[00:29:00]",
            },
            {
                "id": "tlp6_labeldata",
                "label": "ALL DAY I DREAM",
                "name": "Sébastien Léger - Feel",
                "number": "07",
                "time": "[00:35:00]",
            },
            {
                "id": "tlp7_labeldata",
                "label": "LOST MIRACLE",
                "name": "Eli Nissan - Lyla",
                "number": "08",
                "time": "[00:42:00]",
            },
            {
                "id": "tlp8_labeldata",
                "label": "LOST MIRACLE",
                "name": "Raw Main - Sacré Coeur",
                "number": "09",
                "time": "[00:48:00]",
            },
            {
                "id": "tlp9_labeldata",
                "label": "RENAISSANCE",
                "name": "Cypherpunx ft. Sian Evans - Alien (Sébastien Léger Remix)",
                "number": "10",
                "time": "[00:54:00]",
            },
            {
                "id": "tlp10_labeldata",
                "label": "LOST MIRACLE",
                "name": "Eli Nissan - Casablanca",
                "number": "11",
                "time": "[01:02:00]",
            },
            {
                "id": "tlp11_labeldata",
                "label": "LOST & FOUND",
                "name": "Roy Rosenfeld - Force Major",
                "number": "12",
                "time": "[01:08:00]",
            },
            {
                "id": "tlp12_labeldata",
                "label": "LOST MIRACLE",
                "name": "Roy Rosenfeld - Tuti",
                "number": "13",
                "time": "[01:14:00]",
            },
            {
                "id": "tlp13_labeldata",
                "name": "Ólafur Arnalds - Saman (Sébastien Léger Remix)",
                "number": "14",
                "time": "[01:19:30]",
            },
        ],
    }
```

## Test

To run all tests

```
pytest -v
```