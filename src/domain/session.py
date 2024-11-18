from dataclasses import dataclass, field, fields
from typing import List, Any

from domain.track import Track

PRETTY_PRINT = "pretty_print"
TRACKS = "tracks"


@dataclass
class Session:
    source: str
    name: str
    total_tracks: str
    pretty_print: str
    tracks: List[Track] = field(default_factory=list)

    def __post_init__(self) -> None:
        self._init()

    def _init(self):
        self._strip_fields()

    def _strip_fields(self) -> None:
        self.source = self.source.strip()
        self.name = self.name.strip()
        self.total_tracks = self.total_tracks.strip()

    def print_name(self) -> str:
        result = f"{self.name}\n"
        result += "=" * len(self.name)
        return result

    def print_source(self) -> str:
        return f"\n\n Source: {self.source}"

    def to_json(self):
        session_json = {}
        for attribute in Session.get_attributes():
            session_json.update(self._get_value(attribute))

        return session_json

    def _get_value(self, attribute: str) -> dict[str, Any]:
        value = getattr(self, attribute)
        if attribute == PRETTY_PRINT:
            value = self.get_pretty_print()
        if attribute == TRACKS:
            value = [track.to_json() for track in self.tracks] if self.tracks else []
        return {attribute: value}

    def get_pretty_print(self) -> str:
        result = [self.print_name()]
        result.extend(track.get_pretty_print() for track in self.tracks)
        result.append(self.print_source())
        return "".join(result)

    @staticmethod
    def get_attributes() -> List[str]:
        return [field.name for field in fields(Session)]

    def __repr__(self) -> str:
        return f"<Session {self.tracks!r} {self.source!r} {self.name!r} {self.total_tracks!r}>"
