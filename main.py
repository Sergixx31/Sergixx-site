import funciones
import os


funciones.conexionbase()
salir = False
opcion = 0

while not salir:

    print("1. Mostrar datos")
    print("2. Opcion 2")
    print("3. Opcion 3")
    print("4. Salir")

    print("Elige una opcion")

    opcion = funciones.pedirNumeroEntero()

    if opcion == 1:
        funciones.conexionbase()
        mycursor = funciones.dataBase.cursor()

        mycursor.execute("SELECT * FROM users")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
        os.system("clear")
    elif opcion == 2:
        print("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        os.system("clear")
        salir = True

    else:
        print("Introduce un numero entre 1 y 3")


print("Fin")