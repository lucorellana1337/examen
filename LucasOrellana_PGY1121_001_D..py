1
import datetime
import os

departamentos_disponibles = [['A', 'B', 'C', 'D'] for _ in range(10)]

departamentos_vendidos = [['' for _ in range(4)] for _ in range(10)]

precios = {'A': 3800, 'B': 3000, 'C': 2800, 'D': 3500}

compradores = {}

def comprar_departamento():
    os.system("cls")
    piso = int(input("Ingrese el número de piso (1-10): "))
    tipo = input("Ingrese el tipo de departamento (A, B, C, D): ").upper()
    
    if departamentos_vendidos[piso-1][ord(tipo)-ord('A')] == '':
        
        departamentos_vendidos[piso-1][ord(tipo)-ord('A')] = 'X'
        print("¡Departamento", tipo + str(piso), "vendido con éxito!")

        
        run = input("Ingrese el RUN del comprador (sin guiones ni puntos): ")
        compradores[tipo + str(piso)] = run

        print("Operación realizada correctamente.")
    else:
        print("El departamento", tipo + str(piso), "ya ha sido vendido.")

    input("Presione Enter para continuar...")

def mostrar_departamentos_disponibles():
    os.system("cls")
    print("Departamentos disponibles:")
    for piso, departamentos in enumerate(departamentos_disponibles, start=1):
        print("Piso", piso)
        for tipo, estado in zip(departamentos, departamentos_vendidos[piso-1]):
            if estado == '':
                print(tipo, end=' ')
            else:
                print('X', end=' ')
        print()

    input("Presione Enter para continuar...")

def ver_listado_compradores():
    os.system("cls")
    print("Listado de compradores:")
    for departamento, run in sorted(compradores.items(), key=lambda x: x[1]):
        print(departamento, "-", run)

    input("Presione Enter para continuar...")

def mostrar_ventas_totales():
    os.system("cls")
    if not compradores:
        print("No hay compradores disponibles.")
    else:
        total_por_tipo = {tipo: 0 for tipo in precios.keys()}
        total_general = 0

        for piso, departamentos in enumerate(departamentos_vendidos, start=1):
            for tipo, estado in zip(departamentos_disponibles[piso-1], departamentos):
                if estado == 'X':
                    total_por_tipo[tipo] += 1
                    total_general += precios[tipo]

        if sum(total_por_tipo.values()) == 0:
            print("No se han realizado ventas.")
        else:
            print("Ventas totales:")
            print("TIPO DEPARTAMENTO - CANTIDAD - TOTAL")
            for tipo, cantidad in total_por_tipo.items():
                total_tipo = precios[tipo] * cantidad
                print(f"{tipo} {precios[tipo]} UF - {cantidad} - {total_tipo} UF")
            print("TOTAL", sum(total_por_tipo.values()), total_general, "UF")

    input("Presione Enter para continuar...")

def salir():
    os.system("cls")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
    print(f"\nGracias por usar el sistema, {nombre} {apellido}.")
    print(f"Fecha de salida: {fecha_actual}")

    input("Presione Enter para salir...")

while True:
    os.system("cls")
    print("\n=== Inmobiliaria Casa Feliz ===")
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles")
    print("3. Ver listado de compradores")
    print("4. Mostrar ventas totales")
    print("5. Salir")

    opcion = input("Ingrese una opción (1-5): ").upper()

    if opcion == '1':
        comprar_departamento()
    elif opcion == '2':
        mostrar_departamentos_disponibles()
    elif opcion == '3':
        ver_listado_compradores()
    elif opcion == '4':
        mostrar_ventas_totales()
    elif opcion == '5':
        salir()
        break
    else:
        print("Opción inválida.")

print("¡Gracias por utilizar el sistema!")