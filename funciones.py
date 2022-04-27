import mysql.connector
import os

dataBase = mysql.connector.connect(
    host="localhost",
    user="sergi",
    passwd="1234",
    database="gfg"
)

def conexionbase():
    import mysql.connector
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


