from datetime import *

def log(mensaje):
    fecha=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}] {mensaje}")
    while True:
                    estado_prestamo = int(input("1. Pendiente, 2. Aprobado: "))
            
                    if estado_prestamo==1:
                        nuevo_estado="Pendiente"
                        break
                    elif estado_prestamo==2:
                        nuevo_estado="aprobado"
                        break
                    else: 
                        estado_prestamo=int(input("Ingrese nuevamente la opcion: "))  


    