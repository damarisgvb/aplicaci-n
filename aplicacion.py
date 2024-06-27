def menu (): #definiendo menu
    print("1-Suma")
    print("2-resta")
    print("3-multiplicacion")
    print("4-division")
    
def suma (num1, num2): #definiendo suma
    res = num1+num2
    print(res)
    
    
def resta (num1, num2): #definicion resta
    res = num1-num2
    print(res)
    
def multiplicacion (num1, num2): #definiendo multiplicacion
    res = num1*num2
    print(res)
    
def division (num1, num2): #definiendo division
    res = num1/num2
    print(res)
    
resultado = ("suma", "resta", "multiplicacion", "division")

while True: #repiticion es verdadera e elegir una opcion para sumar, restar, multiplicar o dividir

    opcion = int(input("Ingrese la opcion para 1=sumar, 2=restar 2=multiplicar 4=dividir: ")) #elige opcion
    if opcion == 1:
        num1 = float(input("ingrese un numero: "))
        num2 = float(input("ingrese un numero: "))
        suma(num1, num2)
        

    elif opcion == 2:
        num1 = float(input("ingrese un numero: "))
        num2 = float(input("ingrese un numero: "))
        resta(num1, num2)
        
    elif opcion == 3:
        num1 = float(input("ingrese un numero: "))
        num2 = float(input("ingrese un numero: "))
        multiplicacion(num1, num2)
        
    elif opcion == 4:
        num1 = float(input("ingrese un numero: "))
        num2 = float(input("ingrese un numero: "))
        division(num1, num2)
    else:
        print("error, vuelve a elegir un opcion de 1 a 4")
    