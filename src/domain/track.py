"""
This module defines the Track dataclass which represents a music track with various attributes.
"""

from dataclasses import dataclass, fields
from typing import List, Any


@dataclass
class Track:
    """
    A class used to represent a music track.

    Attributes
    ----------
    id : str
        The unique identifier of the track.
    number : str
        The track number in the album.
    time : str
        The duration of the track.
    name : str
        The name of the track.
    label : str
        The label associated with the track.
    """

    id: str
    number: str
    time: str
    name: str
    label: str

    def __post_init__(self) -> None:
        self._init()

    def _init(self) -> None:
        self._strip_fields()
        self._time_formatted()

    def _strip_fields(self) -> None:
        self.id = self.id.strip()
        self.number = self.number.strip()
        self.time = self.time.strip()
        self.name = self.name.strip()
        self.label = self.label.strip()

    def _time_formatted(self) -> None:
        if self.time == "":
            return
        result = "["
        times = self.time.split(":")
        if len(times) == 2:
            result += "00:"
        for one_t in times:
            if len(one_t) == 1:
                result += "0" + one_t
            else:
                result += one_t

            result += ":"

        result = result[:-1]
        self.time = result + "]"

    def print_id(self) -> str:
        """
        Generates a formatted string representing the track's ID.
        The string includes the track number (if available), the track time (if available),
        and a placeholder "ID - ID".
        Returns:
            str: The formatted track ID string.
        """
        result = "\n"
        if len(self.number) > 0:
            result += self.number + ". "

        if len(self.time) > 0:
            result += self.time + " "

        result += "ID - ID"

        return result

    def print_track(self) -> str:
        """
        Constructs and returns a formatted string representation of the track.
        The string includes the track number, time, name, and label if they are present.
        The format is as follows:
        - Track number followed by a period and a space (e.g., "1. ")
        - Track time followed by a space (e.g., "03:45 ")
        - Track name (e.g., "Song Title")
        - Track label enclosed in square brackets (e.g., " [Label]")
        Returns:
            str: A formatted string representation of the track, or an empty string
            if no track information is available.
        """
        result = ""
        if len(self.number) > 0:
            result += self.number + ". "

        if len(self.time) > 0:
            result += self.time + " "

        if len(self.name) > 0:
            result += self.name

        if len(self.label) > 0:
            result += f" [{self.label}]"

        if len(result) > 0:
            return "\n" + result

        return result

    def to_json(self):
        """
        Returns the track as a JSON object.
        """
        track_json = {}
        for attribute in Track.get_attributes():
            track_json.update(self._get_value(attribute))
        return track_json

    def _get_value(self, attribute: str) -> dict[str, Any]:
        value = getattr(self, attribute, None)
        if value is None or value == "":
            return {}
        return {attribute: value}

    def get_pretty_print(self) -> str:
        """
        Generates a pretty-printed string representation of the track.
        The string includes the track number, time, name, and label if they are present.
        Returns:
            str: The pretty-printed string representation of the track.
        """
        if len(self.name) > 0:
            return self.print_track()
        return self.print_id()

    @staticmethod
    def get_attributes() -> List[str]:
        """
        Retrieve a list of attribute names for the Track class.

        Returns:
            List[str]: A list containing the names of all fields in the Track class.
        """
        return [field.name for field in fields(Track)]

    def __repr__(self) -> str:
        return f"<Track {self.id!r} {self.number!r} {self.time!r} {self.name!r} {self.label!r}>"
