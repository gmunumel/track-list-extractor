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

For the url:

```
https://www.1001tracklists.com/tracklist/1f00ch3k/sebastien-leger-the-moment-presents-exceptional-trips-gocek-turkey-mixmag-2021-07-04.html
```

the output is similar to this:

```
Sébastien Léger @ The Moment Presents: Exceptional Trips, Göcek, Turkey (Mixmag) 2021-07-04
===========================================================================================
01. Budakid - Astray In Woodland
02. [00:05:00] Sébastien Léger - Son Of Sun
03. [00:11:45] Shai T - One Night in Paris
04. [00:17:30] Simone Vitullo & Tanit - Priroda (Greg Ochman Remix)
05. [00:23:00] Sébastien Léger - ID
06. [00:29:00] Sébastien Léger - Lava
07. [00:35:00] Sébastien Léger - Feel
08. [00:42:00] Eli Nissan - Lyla
09. [00:48:00] Raw Main - ID
10. [00:54:00] Cypherpunx ft. Sian Evans - Alien (Sébastien Léger Remix)
11. [01:02:00] Eli Nissan - Casablanca
12. [01:08:00] Roy Rosenfeld - ID
13. [01:14:00] Roy Rosenfeld - ID
14. [01:19:30] Ólafur Arnalds - Saman (Sébastien Léger Remix)


Source: https://www.1001tracklists.com/tracklist/1f00ch3k/sebastien-leger-the-moment-presents-exceptional-trips-gocek-turkey-mixmag-2021-07-04.html
```