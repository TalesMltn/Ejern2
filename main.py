def test_math_operations():
    math_operations = MathOperations()

    # Prueba de multiplicación
    result = math_operations.multiply_or_divide(10, 2)
    print(f"Test Multiplicación: 10 * 2 = {result}")
    assert result == 20, "Error: La multiplicación no funcionó como se esperaba."

    # Prueba de división
    result = math_operations.multiply_or_divide(10, 5)
    print(f"Test División: 10 / 5 = {result}")
    assert result == 2, "Error: La división no funcionó como se esperaba."

    # Prueba de división por cero
    try:
        result = math_operations.multiply_or_divide(10, 0)
        print(f"Test División por cero: 10 / 0 = {result}")
    except ValueError as e:
        print(f"Test División por cero: {e}")

if __name__ == "__main__":
    test_math_operations()
