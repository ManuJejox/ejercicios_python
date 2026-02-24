"""
Module to handle customer queuing and ordinal greetings.

This script provides tools to format customer positions correctly in English
using standard ordinal suffixes (st, nd, rd, th).
"""

# Global configuration - Using uppercase for constants (PEP 8)
ORDINAL_SUFFIXES = {1: "st", 2: "nd", 3: "rd"}
DEFAULT_SUFFIX = "th"


def line_up(name: str, number: int) -> str:
    """
    Generate a greeting message with the customer's position in ordinal format.

    Args:
        name (str): The customer's name.
        number (int): The customer's position in the queue.

    Returns:
        str: A formatted message including the correct ordinal suffix.
    """
    # Logic to handle English ordinal exceptions (11th, 12th, 13th)
    last_two_digits = number % 100
    last_digit = number % 10

    if 11 <= last_two_digits <= 13:
        suffix = DEFAULT_SUFFIX
    else:
        suffix = ORDINAL_SUFFIXES.get(last_digit, DEFAULT_SUFFIX)

    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"