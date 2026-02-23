def line_up(name, number):
    n_str = str(number)
    
    if n_str[-2:] in ["11", "12", "13"]:
        suffix = "th"
    else:

        suffix = { "1": "st", "2": "nd", "3": "rd" }.get(n_str[-1], "th")
        
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"