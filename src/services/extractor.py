import validators
import urllib.parse

from typing import Any

from src.services.webdriver import WebDriver
from src.domain.session import Session
from src.domain.track import Track
from src.exceptions import ValidationError

TRACKLISTS_URL = "https://www.1001tracklists.com"


class Extractor:
    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

    def extract(self, request_json) -> dict[str, Any]:
        return self._extract_info(request_json)

    def _extract_info(self, request_json) -> dict[str, Any]:
        url = self._validate_payload(request_json)
        return self._process(url)

    def _validate_payload(self, url):
        url = urllib.parse.unquote(url)
        if not validators.url(url):
            raise ValidationError("Invalid url format")
        if TRACKLISTS_URL not in url:
            raise ValidationError(f"Not a {TRACKLISTS_URL} url")
        return url

    def _process(self, url) -> dict[str, Any]:
        self.web_driver.get(url)
        self._bypass_cookies()
        session = self._process_tracks()
        self.web_driver.quit()
        return session

    def _bypass_cookies(self):
        self.web_driver.frame_to_be_available_and_switch_to_it(
            "//iframe[starts-with(@id, 'sp_message_iframe')]"
        )
        self.web_driver.element_to_be_clickable_and_click_it(
            "//button[@aria-label='Accept']"
        )
        self.web_driver.switch_to_default_content()

    def _process_tracks(self):
        number_tracks = self._get_total_number_tracks()
        set_name = self._get_set_name()
        source = self._get_track_source()
        session = Session(
            name=set_name, total_tracks=number_tracks, source=source, pretty_print=""
        )
        for i in range(int(number_tracks)):
            track_number = self._get_track_number(i)
            track_time = self._get_track_time(i)
            track_id = self._get_track_id(i).replace("_content", "_labeldata")
            track_label = self._get_track_label(track_id)
            track_name = self._get_track_name(i)
            track = Track(
                id=track_id,
                number=track_number,
                time=track_time,
                name=track_name,
                label=track_label,
            )
            session.tracks.append(track)

        return session.to_json()

    def _get_set_name(self):
        return self.web_driver.find_element_by_xpath("/html/body/meta").get_attribute(
            "content"
        )

    def _get_total_number_tracks(self):
        return self.web_driver.find_element_by_xpath("//*[@id='tlTab']").get_attribute(
            "data-count"
        )

    def _get_track_number(self, i):
        return self.web_driver.find_element_by_xpath(
            f'//div[contains(@class, "tlpItem")][{i+1}]//div[contains(@class, "bPlay")][1]/span',
        ).text

    def _get_track_time(self, i):
        return self.web_driver.find_element_by_xpath(
            f'//div[contains(@class, "tlpItem")][{i+1}]//div[contains(@class, "bPlay")][1]/div',
        ).text

    def _get_track_id(self, i):
        return self.web_driver.find_element_by_xpath(
            f'//div[contains(@class, "tlpItem")][{i+1}]//div[contains(@class, "bCont")][1]/div',
        ).get_attribute("id")

    def _get_track_label(self, track_id):
        return (
            self.web_driver.find_element_by_id(track_id).text
            if self.web_driver.find_elements_by_id(track_id)
            else ""
        )

    def _get_track_name(self, i):
        return self.web_driver.find_element_by_xpath(
            f'//div[contains(@class, "tlpItem")][{i+1}]//div[contains(@class, "bCont")][1]/div/span[1]',
        ).text

    def _get_track_source(self):
        return self.web_driver.find_element_by_xpath(
            '//meta[@itemprop="mainEntityOfPage"]'
        ).get_attribute("itemid")
