execute = True

while execute:
    print("\n ")
    print("1.- Suma de n cantidad de números (positivos y negativos")
    print("2.- Producto entre 'n' numeros")
    print("4.- Calcular el factorial (!n) de un número")
    print("5.- Impresión en la pantalla de las tablas de multiplicar entre el 1 al 10.")
    print("7.- Promedio de una serie de números")
    print("8.- Buscar valores máximo y mínimo de una serie de números")

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

        case "2":
            repeat = True
            while repeat:
                inputNumber = ""
                mult = 1
                multiplo = 0
                anterior = 0

                while inputNumber != 0:
                    inputNumber = int(input("Número a multiplicar (0 para finalizar), la serie iniciara con un 1: "))
                    valor = inputNumber
                    anterior = mult
                    mult = mult * inputNumber
                    print("La multiplicacion de ", anterior, "multiplicado por:", valor, "da como resultado: ", mult)
                repeat = input("¿Desea realizar otra multiplicacion? (s/n): ") == "s"

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

        case "5":
            repeat = True
            while repeat:
                opcion = int(input("Selecciona la tabla de multiplicar que quieras mostrar, entre el 1 al 10: "))
                if opcion >= 1 and opcion <= 10:
                    contador = int(0)
                    for contador in range(10):
                        contador += 1
                        print("El numero", opcion, "por", contador, "es igual a", (opcion * contador))
                else:
                    print("Opcion equivocada")
                repeat = input("¿Desea ver la tabla de otro número? (s/n): ") == "s"

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

        case "8":
            repeat = True
            while repeat:
                numbers = []
                print("Introduce solamente números enteros (para terminar, escribe 'Fin')")
                while repeat:
                    entry = input("Número: ")
                    if entry == "Fin":
                        break
                    try:
                        number = int(entry)
                        numbers.append(number)
                    except ValueError:
                        print("Favor de ingresar solamente números o escribe 'Fin' para terminar")
                if numbers:
                    maximum = max(numbers)
                    minimum = min(numbers)
                    total = len(numbers)
                    print("Resultados:")
                    print("El valor máximo es: ", maximum)
                    print("El valor mínimo es: ", minimum)
                    print("El total de números ingresados es de: ", total)
                else:
                    print("Ningun número fue ingresado")
                repeat = input("¿Deseas repetir el proceso? (s/n): ") == "s"
    execute = input("¿Desea elegir alguna otra opción del menú? (s/n): ") == "s"




