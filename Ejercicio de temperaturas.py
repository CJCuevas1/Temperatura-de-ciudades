# Se presentan las 3 matrices 3D de la siguiente manera: ciudades -> semanas -> días
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

# Se imprime un texto en base a las ciudades que se escogieron y su razón.
print("Estas ciudades, marcadas por eventos históricos, tienen temperaturas que varían según la estación del año.\n")

# Bloque que imprime una pregunta sobre la ciudad de la que se desea saber la temperatura.
print("Elige una ciudad para ver sus promedios de temperatura:")
print("1. Chernóbil")
print("2. Hiroshima")
print("3. Nagasaki")
opcion = input("Ingresa el número de la ciudad (1, 2 o 3): ")

# Se valida las opciones que indicó el usuario.
if opcion == "1":
    ciudad_elegida = "Chernóbil"
elif opcion == "2":
    ciudad_elegida = "Hiroshima"
elif opcion == "3":
    ciudad_elegida = "Nagasaki"
else:
    print("Opción no válida. Por favor, ejecuta el programa nuevamente.")
    exit()

# Se muestran los resultados requeridos
print(f"\nPromedios de temperatura para {ciudad_elegida}:\n")
semanas = temperaturas[ciudad_elegida]
for semana_num, semana in enumerate(semanas, start=1):
    promedio = sum(semana) / len(semana)  # Se calcula el promedio de las temperaturas
    print(f"Semana {semana_num}: {promedio:.2f}°C")