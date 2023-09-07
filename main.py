# pylint: disable=missing-function-docstring
# import os
# import subprocess
import sys
import traceback
import validators
import pyperclip

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC


def get_driver():
    options = Options()
    options.add_argument("--window-size=1920,1200")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    return driver


def print_track(track_time, track_name, track_number):
    result = ""
    if track_number != "" and len(track_number) > 0:
        result += track_number + ". "

    if track_time != "" and len(track_time) > 0:
        result += track_time + " "

    if track_name != "" and len(track_name) > 0:
        result += track_name

    if len(result) > 0:
        return "\n" + result

    return result


def print_id(track_time, track_number):
    result = "\n"
    if track_number != "" and len(track_number) > 0:
        result += track_number + ". "

    if track_time != "" and len(track_time) > 0:
        result += track_time + " "

    result += "ID - ID"

    return result


def get_time_formatted(ttime):
    if ttime == "":
        return ""
    result = "["
    times = ttime.split(":")
    if len(times) == 2:
        result += "00:"
    for one_t in times:
        if len(one_t) == 1:
            result += "0" + one_t
        else:
            result += one_t

        result += ":"

    result = result[:-1]
    return result + "]"


def process(driver):
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "/html/body/meta")))

    print("tree generated ...")

    set_name = driver.find_elements(
        By.XPATH, "/html/body/meta")[0].get_attribute("content")

    result = f"{set_name}\n"
    result += "=" * len(set_name)

    number_tracks = driver.find_elements(
        By.XPATH, "//*[@id='tlTab']/meta")[2].get_attribute("content")

    if len(number_tracks) == 0:
        print("Error: number of tracks empty")
        return

    # Get Tracks
    for i in range(int(number_tracks)):
        track_number = driver.find_element(
            By.XPATH, '//*[@id="tlp{}_tracknumber_value"]'.format(i)).text
        if len(track_number) > 0:
            track_number = track_number.strip()

        cue_id = driver.find_elements(
            By.XPATH, '//div[contains(@class, "trRow{}")]'.format(i + 1))[0].get_attribute("id")
        if len(cue_id) > 0:
            cue_id = cue_id.replace("tlp_", "")

        track_time = driver.find_element(
            By.XPATH, '//*[@id="cue_{}"]'.format(cue_id)).text
        if len(track_time) > 0:
            track_time = track_time.strip()
            track_time = get_time_formatted(track_time)

        track_name = driver.find_elements(
            By.XPATH, '//*[@id="tlp{}_content"]/meta'.format(i))
        if len(track_name) > 0:
            track_name = track_name[0].get_attribute("content").strip()
            result += print_track(track_time, track_name, track_number)
        else:
            result += print_id(track_time, track_number)

    source = driver.find_elements(
        By.XPATH, '//meta[@itemprop="mainEntityOfPage"]')[0].get_attribute("itemid")
    if len(source) > 0:
        source = source.strip()
        result += "\n\n" + "Source: " + source

    print(result)
    print("\nCopying to clipboard...")

    pyperclip.copy(result)

    print("Copy done! ;)")


def get_tracks_info(url):
    print(f"started for '{url}' ...")

    driver = get_driver()

    try:
        driver.get(url)

        process(driver)
    except Exception:
        traceback.print_exc(file=sys.stdout)
    finally:
        driver.quit()


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
