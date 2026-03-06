from datetime import *

def logE(mensaje):
    fecha=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}] {mensaje}")
    while True:
                    estado_herramienta = int(input("1. reparada, 2. dañada: "))
            
                    if estado_herramienta==1:
                        nuevo_estadoh="Pendiente"
                        break
                    elif estado_herramienta==2:
                        nuevo_estadoh="aprobado"
                        break
                    else: 
                        estado_herramienta=int(input("Ingrese nuevamente la opcion: "))  
