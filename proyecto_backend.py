from datetime import date, datetime
#import PyQt6 | Para la interfaz
# import sqlite3 | Para la base de datos

# Fecha de pruebas, tareas, fecha de hoy. 

# Funciones, código local
def materias(): # Muestra las Materias / Temas que estan viendo / Profesor
    pass

def notas(): # Muestra cada materia con cada nota de cada prueba, su promedio final y si esta aprobado
    pass

def fechas(): # Pruebas, Eventos, Tareas de la semana comparando la fecha actual con datatime, exposiciones, materiales
    entrada = input("Ingresa la fecha (AAAA-MM-DD): ")
    try:
        fecha = datetime.strptime(entrada, "%Y-%m-%d").date()
    except ValueError:
        print("Formato de fecha no válido.")
        return

    fecha_hoy = date.today()
    if fecha < fecha_hoy:
        print("Es anterior")
    elif fecha > fecha_hoy:
        print("Es posterior")
    else:
        print("La fecha es hoy")

def hoy(): # Muestra todo lo que habra en la fecha actual (incluyendo las materias de hoy, de que hora a que hora)
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    fecha_hoy = date.today()
    print("Hoy es", dias[fecha_hoy.weekday()], fecha_hoy.strftime("%d-%m-%Y"))

def menu():
    while True:
        print("\n         TimeLine. Proyecto Cero         ")
        print("1. Comparar una fecha")
        print("2. Ver fecha de hoy")
        print("0. Salir")
        respuesta = input("Elige una opción: ")

        if respuesta == "1":
            fechas()
        elif respuesta == "2":
            hoy()
        elif respuesta == "0":
            break
        else:
            print("Opción no válida.")

# General, código global
menu()