# Se plantea la función para calcular el promedio
def calcular_promedio(temperaturas):
    promedios = {}  # Se crea un diccionario
    # En este bloque se itera sobre cada ciudad y las semanas, además de hacer sumas, conteo de días y calculo del promedio
    for ciudad, semanas in temperaturas.items():
        suma_total = sum(temp for semana in semanas for temp in semana)
        cantidad_dias = sum(len(semana) for semana in semanas)
        promedios[ciudad] = suma_total / cantidad_dias

    return promedios


# Datos de temperaturas basadas en el código anterior
temperaturas = {
    "Chernóbil": [
        [-5, -4, -3, -2, -1, 0, 1],
        [5, 6, 7, 8, 9, 10, 11],
        [20, 21, 22, 23, 24, 25, 26],
        [10, 11, 12, 13, 14, 15, 16]
    ],
    "Hiroshima": [
        [5, 6, 7, 8, 9, 10, 11],
        [15, 16, 17, 18, 19, 20, 21],
        [28, 29, 30, 31, 32, 33, 34],
        [20, 21, 22, 23, 24, 25, 26]
    ],
    "Nagasaki": [
        [8, 9, 10, 11, 12, 13, 14],
        [16, 17, 18, 19, 20, 21, 22],
        [29, 30, 31, 32, 33, 34, 35],
        [22, 23, 24, 25, 26, 27, 28]
    ]
}

# Se calcula el prmedio
promedios_ciudades = calcular_promedio(temperaturas)

print("Estas ciudades, marcadas por eventos históricos, tienen temperaturas que varían según la estación del año.\n")

# En este bloque se imprime una pregunta sobre la ciudad de la que se desea saber la temperatura.
print("Elige una ciudad para ver sus promedios de temperatura:")
print("1. Chernóbil")
print("2. Hiroshima")
print("3. Nagasaki")
opcion = input("Ingresa el número de la ciudad (1, 2 o 3): ")

# Se presentan las condiciones ante la elección del usuario
if opcion == "1":
    ciudad_elegida = "Chernóbil"
elif opcion == "2":
    ciudad_elegida = "Hiroshima"
elif opcion == "3":
    ciudad_elegida = "Nagasaki"
else:
    print("Opción no válida. Por favor, ejecuta el programa nuevamente.")
    exit()

# Se imprime el promedio de la ciudad elegida
print(f"\nLa temperatura promedio en la ciudad de {ciudad_elegida} es: {promedios_ciudades[ciudad_elegida]:.2f}°C")