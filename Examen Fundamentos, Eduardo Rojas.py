import random, csv, math

trabajadores = [
    {"nombre": "Juan Pérez"},
    {"nombre": "María García"},
    {"nombre": "Carlos López"},
    {"nombre": "Ana Martínez"},
    {"nombre": "Pedro Rodríguez"},
    {"nombre": "Laura Hernández"},
    {"nombre": "Miguel Sánchez"},
    {"nombre": "Isabel Gómez"},
    {"nombre": "Francisco Díaz"},
    {"nombre": "Elena Fernández"}
]

def asignar_sueldos(trabajadores):
    sueldos = []
    for _ in trabajadores:
        sueldos.append(random.randint(300000, 2500000))
    return sueldos

def clasificar_sueldos(trabajadores, sueldos): 
    print("Sueldos menores a $800.000")
    for i in range(len(sueldos)):
        if sueldos[i] < 800000:
            print(f"Nombre empleado: {trabajadores[i]['nombre']} Sueldo: ${sueldos[i]}")
            
    print("\nSueldos entre $800.000 y $2.000.000")
    for i in range(len(sueldos)):
        if 800000 <= sueldos[i] <= 2000000:
            print(f"Nombre empleado: {trabajadores[i]['nombre']} Sueldo: ${sueldos[i]}")
            
    print("\nSueldos superiores a $2.000.000")
    for i in range(len(sueldos)):
        if sueldos[i] > 2000000:
            print(f"Nombre empleado: {trabajadores[i]['nombre']} Sueldo: ${sueldos[i]}")
            
    print("\nTotal Sueldos:", sum(sueldos))
            
def ver_estadisticas(sueldos):
            max_sueldo = max(sueldos)
            min_sueldo = min(sueldos)
            promedio_sueldos = sum(sueldos) / len(sueldos)
            geom_sueldos = math.exp(sum(math.log(s) for s in sueldos) / len(sueldos))
            
            print(f"Sueldo más alto: ${max_sueldo}")
            print(f"Sueldo más bajo: ${min_sueldo}")
            print(f"Promedio de sueldos: ${promedio_sueldos:.2f}")
            print(f"Media geométrica de sueldos: ${geom_sueldos:.2f}")
            
def generar_reporte(trabajadores, sueldos):
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        
        for i in range(len(trabajadores)):
            descuento_salud = sueldos[i] * round (0.07)
            descuento_afp = sueldos[i] * round (0.12)
            sueldo_liquido = sueldos[i] - descuento_salud - descuento_afp
            writer.writerow([trabajadores[i]["nombre"], sueldos[i], descuento_salud, descuento_afp, sueldo_liquido])
            print(f"Nombre empleado: {trabajadores[i]['nombre']}, Sueldo Base: ${sueldos[i]}, Descuento Salud: ${descuento_salud:.2f}, Descuento AFP: ${descuento_afp:.2f}, Sueldo Líquido: ${sueldo_liquido:.2f}")

def menu():
    sueldos = []
    while True:
        print("\nMenú:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Generar reporte de sueldos")
        print("5. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sueldos = asignar_sueldos(trabajadores)
            print("Sueldos asignados aleatoriamente.")
        elif opcion == "2":
            if sueldos:
                clasificar_sueldos(trabajadores, sueldos)
            else:
                print("Primero asigne sueldos.")
        elif opcion == "3":
            if sueldos:
                ver_estadisticas(sueldos)
            else:
                print("Primero asigne sueldos.")
        elif opcion == "4":
            if sueldos:
                generar_reporte(trabajadores, sueldos)
            else:
                print("Primero asigne sueldos.")
        elif opcion == "5":
            print("Finalizando programa…")
            print("Desarrollado por: Eduardo Rojas")
            print("RUT: 21.898.995-0")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()