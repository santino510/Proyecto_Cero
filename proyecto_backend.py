from datetime import date, datetime
#import PyQt6 | Para la interfaz
# import sqlite3 | Para la base de datos

# Fecha de pruebas, tareas, fecha de hoy. 
materias = ["Matematicas", "Lengua_Y_Literatura", "Biologia", "Ingles", "Programacion_1", "Geografia", "Historia", "Entorno_De_Desarrollo", "Fvt"] # Cantidad de materias que tiene el usuario
matriz_notas = []
Lista_eventos = []
# Funciones, código local

def notas(): # Muestra cada materia con cada nota de cada prueba(Te pide cada una de las notas y pasa por materia), su promedio final y si esta aprobado
    matriz = []
    for i in range(len(materias)):
        print(f"Materia: {materias[i]}")
        cantidad_notas = int(input(f"Ingresa la cantidad de notas para {materias[i]}: "))

        notas_materia = []
        for numero in range(1, cantidad_notas + 1):
            nota = float(input(f"Ingresa la nota {numero} de {materias[i]}: "))
            notas_materia.append(nota)

        matriz.append([materias[i], notas_materia])

    print("\nLista de notas:")
    ver_notas(matriz)
    return matriz


def ver_notas(matriz):
    if not matriz:
        print("Todavía no ingresaste notas.")
        return

    for materia, notas_materia in matriz:
        notas_texto = " | ".join(
            f"Nota {numero}: {nota}"
            for numero, nota in enumerate(notas_materia, start=1)
        )
        if notas_materia:
            promedio = sum(notas_materia) / len(notas_materia)
            estado = "Aprobado" if promedio >= 7 else "Desaprobado"
            print(f"- {materia}: {notas_texto} | Promedio: {promedio:.2f} | {estado}")
        else:
            print(f"- {materia}: Sin notas")
        
        
def agregar_eventos(lista_eventos): # Muestra los eventos de la semana, mes y año
    nombre_evento = input("Ingresa el nombre del evento: ")
    fecha_evento = input("Ingresa la fecha del evento (AAAA-MM-DD): ")
    descripcion_evento = input("Ingresa la descripción del evento: ")
    lista_eventos.append((nombre_evento, fecha_evento, descripcion_evento))
def ver_eventos(eventos):
    if not eventos:
        print("No hay eventos programados.")
        return

    print("Eventos programados:")
    for nombre, fecha, descripcion in eventos:
        print(f"- {nombre} (Fecha: {fecha}) - {descripcion}")

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

def fecha_hoy_weekday():
    return date.today().weekday()

HORARIO = {
    "lunes": [
        ("Arte Musica", "14:15", "16:25"),
        ("Lengua Y Literatura", "16:25", "17:55"),
        ("Educación Física", "11:30", "20:05")
        ],
    "martes": [
        ("Biologia", "14:15", "15:35"),
        ("Lengua Y Literatura", "15:45", "17:15"),
        ("Ingles", "17:15", "18:35"),
        ("Matemática", "18:45", "20:05")
        ],
    "miércoles": [
        ("Programacion 1", "14:15", "15:35"),
        ("Ingles", "15:45", "17:15"),
        ("Biologia", "17:15", "18:35"),
        ("Entorno De Desarrollo", "18:45", "20:05")
        ],
    "jueves": [
        ("Geografia", "14:15", "16:25"),
        ("Historia", "16:25", "18:35"),
        ("Entorno De Desarrollo", "18:45", "20:05")
       ],
    "viernes": [
            ("Fvt", "14:15", "16:25"),
        ("Matemática", "16:25", "17:55"),
        ("Programacion 1", "17:55", "20:05"),
        ],
    "sábado": [],
    "domingo": [],
}



def hoy(): # Muestra todo lo que habra en la fecha actual (incluyendo las materias de hoy, de que hora a que hora)
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    fecha_hoy = date.today()
    print("Hoy es", dias[fecha_hoy.weekday()], fecha_hoy.strftime("%d-%m-%Y"))
    dia = dias[fecha_hoy.weekday()]
    materias_del_dia = HORARIO.get(dia)

    if materias_del_dia is None:
        print(f"El día '{dia}' no es válido.")
        return

    print(f"Materias del {dia}:")
    if materias_del_dia:
        for materia, hora_inicio, hora_fin in materias_del_dia:
            print(f"- {materia}: {hora_inicio} a {hora_fin}")
    else:
        print("No hay materias programadas.")


def materia_actual():
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    ahora = datetime.now()
    dia = dias[ahora.weekday()]
    hora_actual = ahora.time()

    print(f"Ahora es {ahora.strftime('%d-%m-%Y %H:%M')} ({dia}).")

    materias_del_dia = HORARIO.get(dia, [])
    if not materias_del_dia:
        print("Ahora no tienes materias.")
        return

    for materia, hora_inicio, hora_fin in materias_del_dia:
        inicio = datetime.strptime(hora_inicio, "%H:%M").time()
        fin = datetime.strptime(hora_fin, "%H:%M").time()

        if inicio <= hora_actual <= fin:
            print(f"Ahora deberías estar teniendo: {materia}")
            print(f"Horario: {hora_inicio} a {hora_fin}")
            return

    print("Ahora no tienes ninguna materia.")


def menu():
    global matriz_notas
    global Lista_eventos

    while True:
        print("\n         TimeLine. Proyecto Cero         ")
        print("1. Comparar una fecha")
        print("2. Ver fecha de hoy")
        print("3. Ver materia actual")
        print("4. Eventos")
        print("5. Ingresar notas")
        print("6. Ver lista de notas")
        print("0. Salir")
        respuesta = input("Elige una opción: ").strip()

        if respuesta == "1":
            fechas()
        elif respuesta == "2":
            hoy()
        elif respuesta == "3":
            materia_actual()
        elif respuesta == "4":
            print("Le gustaria agregar un evento o ver los eventos existentes? 1/2")
            sub_respuesta = input("Elige una opción: ").strip()
            if sub_respuesta == "1":
                agregar_eventos(Lista_eventos)
            elif sub_respuesta == "2":
                ver_eventos(Lista_eventos)
        elif respuesta == "5":
            matriz_notas = notas()
        elif respuesta == "6":
            ver_notas(matriz_notas)
        elif respuesta == "0":
            break
        else:
            print("Opción no válida.")

# General, cudigo global
if __name__ == "__main__":
    menu()
