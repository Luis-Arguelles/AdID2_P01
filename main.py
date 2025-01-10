print("1.- Suma de n cantidad de números (positivos y negativos")
option = input("Seleccione una opción: ")

inputNumber = ""
sum = 0

match(option):
    case "1":
        while inputNumber != 0:
            inputNumber = int(input("Número a sumar (0 para finalizar): "))
            sum += inputNumber
        print(f"La suma es {sum}")



