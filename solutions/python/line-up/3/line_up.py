def line_up(name, number):
    SUFFIXES = {1:"st", 2:"nd", 3:"rd"}
    DEFAULT_SUFFIX = "th"

    last_two_digits = number % 100
    last_digit = number % 10

    if 11 <= last_two_digits <= 13:
        suffix = DEFAULT_SUFFIX
    
    else:
        suffix = SUFFIXES.get(last_digit, DEFAULT_SUFFIX)

    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"