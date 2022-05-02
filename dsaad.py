import mysql.connector
import os

dataBase = mysql.connector.connect(
    host="localhost",
    user="sergi",
    passwd="1234",
    database="gfg"

)
def pedirNumeroEntero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num


salir = False
opcion = 0

while not salir:

    print("1. Mostrar datos")
    print("2. Opcion 2")
    print("3. Opcion 3")
    print("4. Salir")

    print("Elige una opcion")

    opcion = pedirNumeroEntero()

    if opcion == 1:
        mycursor = dataBase.cursor()

        mycursor.execute("SELECT * FROM users")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
    elif opcion == 2:
        print("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:

        salir = True

    else:
        print("Introduce un numero entre 1 y 3")

    os.system("clear")
print("Fin")

dataBase.close()