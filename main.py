execute = True

while execute:
    print("1.- Suma de n cantidad de números (positivos y negativos")
    print("4.- Calcular el factorial (!n) de un número")
    print("7.- Promedio de una serie de números")

    option = input("Seleccione una opción: ")

    match option:
        case "1":
            repeat = True
            while repeat:
                inputNumber = ""
                sum = 0

                while inputNumber != 0:
                    inputNumber = int(input("Número a sumar (0 para finalizar): "))
                    sum += inputNumber
                print(f"La suma es {sum}")
                repeat = input("¿Desea realizar otra suma? (s/n): ") == "s"
        case "4":
            repeat = True
            while repeat:
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
                repeat = input("¿Desea calcular el factorial de otro número? (s/n): ") == "s"
        case "7":
            repeat = True
            while repeat:
                dividend = 0
                divisor = 0
                print("Introduce números para calcular el promedio. Ingresa -1 para terminar")
                while True:
                    number = float(input("Número: "))
                    if number == 1:
                        break
                    dividend += number
                    divisor += 1
                if divisor > 0:
                    average = dividend / divisor
                    print("El promedio es: ", average)
                else:
                    print("No se ingresaron números válidos para calcular el promedio")
                repeat = input("¿Deseas calcular el promedio de otra serie? (s/n): ") == "s"
    execute = input("¿Desea elegir alguna otra opción del menú? (s/n): ") == "s"




