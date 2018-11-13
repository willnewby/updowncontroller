"""Utility functions for updown check."""
import updown


def check_exists(url):
    """Check if a check for url exists, and if it does, return it."""
    try:
        return True, updown.checks()[url]
    except KeyError:
        return False, None
