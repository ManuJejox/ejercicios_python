def rebase(input_base: int, digits: list, output_base: int) -> list:
    # 1. Validaciones compactas (Vectorized-style logic)
    if input_base < 2:
        raise ValueError("input base must be >= 2")
        
    if output_base < 2:
        raise ValueError("output base must be >= 2")
        
    if any(not 0 <= d < input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    # 2. Convertir a decimal usando el Método de Horner
    # En ML se prefiere esto porque es O(n). Evitamos el coste de las potencias.
    decimal_value = 0
    for d in digits:
        decimal_value = decimal_value * input_base + d

    # 3. Caso base
    if decimal_value == 0:
        return [0]

    # 4. Convertir a base de salida con optimización de memoria
    # Usamos divmod para reducir ciclos de CPU
    res = []
    while decimal_value:
        decimal_value, remainder = divmod(decimal_value, output_base)
        res.append(remainder)

    # 5. Retornar invertido (Slicing eficiente)
    return res[::-1]