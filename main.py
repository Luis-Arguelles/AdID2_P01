print("1.- Suma de n cantidad de números (positivos y negativos")
print("4.- Calcular el factorial (!n) de un número")
option = input("Seleccione una opción: ")

match option:
    case "1":
        inputNumber = ""
        sum = 0
        while inputNumber != 0:
            inputNumber = int(input("Número a sumar (0 para finalizar): "))
            sum += inputNumber
        print(f"La suma es {sum}")
    case "4":
        inputNumber = int(input("Inserte un número para calcular su factorial: "))
        if inputNumber == 0:
            print(f"El factorial de {inputNumber} es 1")
        elif inputNumber > 0:
            count = inputNumber
            factorial = 1
            while count > 0:
                factorial = factorial * count
                count -= 1
            print(f"El factorial de {inputNumber} es {factorial}")




