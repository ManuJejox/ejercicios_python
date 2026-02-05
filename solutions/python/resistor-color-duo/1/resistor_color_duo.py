COLOR_MAP = {"black": 0,
"brown": 1,
"red": 2,
"orange": 3,
"yellow": 4,
"green": 5,
"blue": 6,
"violet": 7,
"grey": 8,
"white": 9} 

def value(colors):
    
    val1 = COLOR_MAP[colors[0]]
    val2 = COLOR_MAP[colors[1]]
    
    return (val1 * 10) + val2
