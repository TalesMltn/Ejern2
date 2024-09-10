class X:
    def z(self, x, y):
        if y == 0:
            raise ValueError("No se puede dividir por cero.")
        return x * y if y != 0 else x / y


def main():
    try:
        x = float(input("Ingresa el valor de x: "))
        y = float(input("Ingresa el valor de y: "))

        operacion = X()
        resultado = operacion.z(x, y)

        print(f"El resultado de la operación es: {resultado}")

    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: División por cero no permitida.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


if __name__ == "__main__":
    main()
