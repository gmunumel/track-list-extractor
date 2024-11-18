"""
Unit tests for the Track class.
"""

from src.domain.track import Track


def test_track_print_id():
    track = Track(id="", number="", time="", name="", label="")
    assert track.print_id() == "\nID - ID"


def test_track_print_id_number():
    track = Track(id="", number="01", time="", name="", label="")
    assert track.print_id() == "\n01. ID - ID"


def test_track_print_id_time():
    track = Track(id="", number="", time="05:00", name="", label="")
    assert track.print_id() == "\n[00:05:00] ID - ID"


def test_track_print_track_empty():
    track = Track(id="", number="", time="", name="", label="")
    assert track.print_track() == ""


def test_track_get_pretty_print_empty():
    track = Track(id="", number="", time="", name="", label="")
    assert track.get_pretty_print() == "\nID - ID"
