import time

continuar = True

jugadores = []
puntuaciones = []

def agregar_jugador():
    print()
    nombre = input("Nombre del jugador: ")
    print()
    puntuacion = float(input("Puntuación del jugador: "))
    print()

    jugadores.append(nombre)
    puntuaciones.append(puntuacion)

def mostrar_jugadores():
    for i in range(len(jugadores)):
        print()
        print(jugadores[i], puntuaciones[i])

def puntuacion_mas_alta():
    maximo = max(puntuaciones)
    posicion = puntuaciones.index(maximo)
    print(jugadores[posicion])

def salir():
    print()
    print("¡Hasta pronto!")
    print()
    time.sleep(1.2)
    global continuar
    continuar = False

while continuar:
    print()
    print("Cargando menú...")
    time.sleep(2.4)
    print()
    print("=== MENÚ ===")
    print()
    print("1. Agregar un jugador con su puntuación.")
    print("2. Ver la lista completa de jugadores y puntuaciones.")
    print("3. Ver quién tiene la puntuación más alta.")
    print("4. Salir.")
    
    print()
    opcion = input("Elija una opción: ")
    time.sleep(1.4)

    if opcion == "1":
        time.sleep(0.8)
        agregar_jugador()
        time.sleep(1)
        print()
        print(jugadores, puntuaciones)
        time.sleep(1.4)

    elif opcion == "2":
        time.sleep(0.7)
        mostrar_jugadores()
        time.sleep(1.4)

    elif opcion == "3":
        time.sleep(0.7)
        print()
        puntuacion_mas_alta()
        time.sleep(1.4)

    elif opcion == "4":
        time.sleep(0.7)
        salir()

    else:
        print()
        print("Opción no válida, intentelo de nuevo.")