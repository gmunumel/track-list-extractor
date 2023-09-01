import sys
import validators

from requests_html import HTMLSession


def getTracksInfo(url):
    # url = "https://www.1001tracklists.com/tracklist/1kpbmppt/hernan-cattaneo-incendia-dome-burning-man-multiverse-united-states-2021-09-01.html"
    # url = "https://www.1001tracklists.com/tracklist/gc36679/sebastien-leger-halaszbastya-etterem-budapest-hungary-2022-10-01.html"

    print(f"started for '{url}' ...")
    session = HTMLSession()

    r = session.get(url)

    r.html.render()

    tree = r.html
    print("tree generated ...")

    setName = tree.xpath('/html/body/meta[1]/@content')
    print(setName)
    print(setName[0])
    print('=' * len(setName[0]))

    numberTracks = tree.xpath('//*[@id="tlTab"]/meta[3]/@content')[0].strip()

    if len(numberTracks) == 0:
        print('Error: number of tracks empty')
        return

    # Get Tracks
    for i in range(int(numberTracks)):

        trackNumber = tree.xpath(
            '//*[@id="tlp{}_tracknumber_value"]/text()'.format(i))
        if len(trackNumber) > 0:
            trackNumber = trackNumber[0].strip()

        cueId = tree.xpath(
            '//div[contains(@class, "trRow{}")]/@id'.format(i + 1))
        if len(cueId) > 0:
            cueId = cueId[0].replace('tlp_', '')

        trackTime = tree.xpath('//*[@id="cue_{}"]/text()'.format(cueId))
        if len(trackTime) > 0:
            trackTime = trackTime[0].strip()
            trackTime = getTimeFormatted(trackTime)

        trackName = tree.xpath(
            '//*[@id="tlp{}_content"]/meta[1]/@content'.format(i))
        if len(trackName) > 0:
            trackName = trackName[0].strip()
            printTrack(trackTime, trackName, trackNumber)
        else:
            printID(trackTime, trackNumber)

    source = tree.xpath('//meta[@itemprop="mainEntityOfPage"]/@itemid')
    if len(source) > 0:
        source = source[0].strip()
        print('\n' + 'Source: ' + source)


def printTrack(trackTime, trackName, trackNumber):
    result = ''
    if trackNumber != '' and len(trackNumber) > 0:
        result += trackNumber + '. '

    if trackTime != '' and len(trackTime) > 0:
        result += trackTime + ' '

    if trackName != '' and len(trackName) > 0:
        result += trackName

    print(result)


def printID(trackTime, trackNumber):
    result = ''
    if trackNumber != '' and len(trackNumber) > 0:
        result += trackNumber + '. '

    if trackTime != '' and len(trackTime) > 0:
        result += trackTime + ' '

    result += 'ID - ID'

    print(result)


def getTimeFormatted(time):
    if time == '':
        return ''
    result = '['
    times = time.split(':')
    if len(times) == 2:
        result += '00:'
    for time in times:
        if len(time) == 1:
            result += '0' + time
        else:
            result += time

        result += ':'

    result = result[:-1]
    return result + ']'


def main():
    url = input('Enter a valid url: ')
    if not url.endswith('.html'):
        print("Error: not a html url")
        sys.exit(0)

    if not validators.url(url):
        print("Error: url not valid")
        sys.exit(0)

    getTracksInfo(url)


if __name__ == "__main__":
    main()
