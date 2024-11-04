"""
Module for testing the get_tracklist_v1_url function.
"""

from src.config import get_tracklist_v1_url


def test_get_tracklist_v1_url():
    """Test the get_tracklist_v1_url function."""
    assert get_tracklist_v1_url() == "/api/v1/tracklist"
