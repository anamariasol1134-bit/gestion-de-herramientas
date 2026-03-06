from gestionarJson import *


def historial():
    prestamos=registrar("prestamos.json")
    nombre = input("Ingrese el nombre del usuario: ").strip()

    encontrado=False

    print(f"historial de prestamos de {nombre}:")

    for elemento in prestamos:
        if elemento["nombre"].lower() == nombre.lower():
            encontrado= True
            print("****************************************")
            print(f"""
                Id:               {elemento["id"]}
                Herramienta:      {elemento["Herramienta"]}
                Cantidad:         {elemento["Cantidad"]}
                Fecha inicio:     {elemento["Fecha_inicio"]}
                Fecha fin:        {elemento["Fecha_final"]}
                Estado:           {elemento["estado"]}
""")
    if not encontrado:
        print("El usuario no tiene prestamos registrados")
