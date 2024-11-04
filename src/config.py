"""
This module provides configuration settings and utility functions for the tracklist extractor.
"""

import posixpath


def get_tracklist_v1_url():
    """
    Returns the URL for the tracklist API version 1.
    """
    return posixpath.join("/", "api", "v1", "tracklist")
