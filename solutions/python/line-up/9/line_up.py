"""
Module to handle customer queuing and ordinal greetings.

This script provides tools to format customer positions correctly in English
using standard ordinal suffixes (st, nd, rd, th).
"""

# Global configuration - Using uppercase for constants (PEP 8)
ORDINAL_SUFFIXES = {1: "st", 2: "nd", 3: "rd"}
DEFAULT_SUFFIX = "th"
CENTURY_MODULUS = 100
DECADE_MODULUS = 10
TEEN_LOWER_BOUND = 11
TEEN_UPPER_BOUND = 13


def line_up(name: str, number: int) -> str:
    """
    Generate a greeting message with the customer's position in ordinal format.

    Args:
        name (str): The customer's name.
        number (int): The customer's position in the queue.

    Returns:
        str: A formatted message including the correct ordinal suffix.
    """
    if number < 1:
        raise ValueError("The number must be a positive integer.")
    
    # Logic to handle English ordinal exceptions (11th, 12th, 13th)
    last_two_digits = number % CENTURY_MODULUS
    last_digit = number % DECADE_MODULUS

    if TEEN_LOWER_BOUND <= last_two_digits <= TEEN_UPPER_BOUND:
        suffix = DEFAULT_SUFFIX
    else:
        suffix = ORDINAL_SUFFIXES.get(last_digit, DEFAULT_SUFFIX)

    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"