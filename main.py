import sys
import validators

from requests_html import HTMLSession


def get_tracks_info(url):
    # url = "https://www.1001tracklists.com/tracklist/1kpbmppt/hernan-cattaneo-incendia-dome-burning-man-multiverse-united-states-2021-09-01.html"
    # url = "https://www.1001tracklists.com/tracklist/gc36679/sebastien-leger-halaszbastya-etterem-budapest-hungary-2022-10-01.html"

    print(f"started for '{url}' ...")
    session = HTMLSession()

    r = session.get(url)

    r.html.render()

    tree = r.html
    print("tree generated ...")

    set_name = tree.xpath("/html/body/meta[1]/@content")
    print(set_name)
    print(set_name[0])
    print("=" * len(set_name[0]))

    number_tracks = tree.xpath('//*[@id="tlTab"]/meta[3]/@content')[0].strip()

    if len(number_tracks) == 0:
        print("Error: number of tracks empty")
        return

    # Get Tracks
    for i in range(int(number_tracks)):
        track_number = tree.xpath('//*[@id="tlp{}_tracknumber_value"]/text()'.format(i))
        if len(track_number) > 0:
            track_number = track_number[0].strip()

        cue_id = tree.xpath('//div[contains(@class, "trRow{}")]/@id'.format(i + 1))
        if len(cue_id) > 0:
            cue_id = cue_id[0].replace("tlp_", "")

        track_time = tree.xpath('//*[@id="cue_{}"]/text()'.format(cue_id))
        if len(track_time) > 0:
            track_time = track_time[0].strip()
            track_time = get_time_formatted(track_time)

        track_name = tree.xpath('//*[@id="tlp{}_content"]/meta[1]/@content'.format(i))
        if len(track_name) > 0:
            track_name = track_name[0].strip()
            print_track(track_time, track_name, track_number)
        else:
            print_id(track_time, track_number)

    source = tree.xpath('//meta[@itemprop="mainEntityOfPage"]/@itemid')
    if len(source) > 0:
        source = source[0].strip()
        print("\n" + "Source: " + source)


def print_track(track_time, track_name, track_number):
    result = ""
    if track_number != "" and len(track_number) > 0:
        result += track_number + ". "

    if track_time != "" and len(track_time) > 0:
        result += track_time + " "

    if track_name != "" and len(track_name) > 0:
        result += track_name

    print(result)


def print_id(track_time, track_number):
    result = ""
    if track_number != "" and len(track_number) > 0:
        result += track_number + ". "

    if track_time != "" and len(track_time) > 0:
        result += track_time + " "

    result += "ID - ID"

    print(result)


def get_time_formatted(time):
    if time == "":
        return ""
    result = "["
    times = time.split(":")
    if len(times) == 2:
        result += "00:"
    for time in times:
        if len(time) == 1:
            result += "0" + time
        else:
            result += time

        result += ":"

    result = result[:-1]
    return result + "]"


def main():
    url = input("Enter a valid url: ")
    if not url.endswith(".html"):
        print("Error: not a html url")
        sys.exit(0)

    if not validators.url(url):
        print("Error: url not valid")
        sys.exit(0)

    get_tracks_info(url)


if __name__ == "__main__":
    main()
