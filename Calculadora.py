# Lectura del valor de 2 variables enteras por consola:
print("Ingrese el número 1")
numero1 = int(input())
print("Ingrese el número 2")
numero2 = int(input())
print("Ingrese la operación (+, -, *, /)")
operacion = input()

match operacion:
    case '+':
        # Operación suma:
        suma = numero1 + numero2
        print("La suma es " + str(suma))
    case '-':
        # Operación resta:
        resta = numero1 - numero2
        print("La resta es " + str(resta))
    case '*':
        # Operación multiplicación:
        multiplicacion = numero1 * numero2
        print("La multiplicación es " + str(multiplicacion))
    case '/':
        # Operación división:
        division = numero1 / numero2
        print("La división es " + str(division))
    case '%' :
    #Operación residuo
            Residuo = numero1 % numero2
            print("El residuo es " + str(Residuo))
    case '^':
            #Operacion Potencia
            Potencia = numero1 ** numero2
            print("la potencia del primer numero es " + str(Potencia))
    case _ :
        print("Operación inválida")
