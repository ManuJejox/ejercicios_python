def rebase(input_base: int, digits: list, output_base: int) -> list:
    """Convert a sequence of digits in one base, representing a number, into a sequence of digits in another base, representing the same number."""
    
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")
        
    if not any(digits):
        return [0]
    
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
        
    new_digits = []
    digits_base10 = 0

    for num, index in zip(digits, range(len(digits)-1, -1, -1)):
            digits_base10 += num * (input_base ** index)
        
    while digits_base10 > 0:
            
        new_digits.append(digits_base10 % output_base)
        digits_base10 = digits_base10 // output_base
            
    new_digits = new_digits[::-1]
    return new_digits