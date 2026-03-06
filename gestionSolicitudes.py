from gestionarJson import registrar, guardar, generar_id
from validaciones import validadEntero,validarMenu,persona_valida
from gestionHerramientas import listar_herramientas, guarda_herramientas,eliminar_herramienta,actualizar_herramienta, existe_herramienta, ARCHIVO1
from gestionPersona import listar_persona, guardar_persona, eliminar_persona, actualizar_persona
from datetime import date, datetime, timedelta
from log import *
ARCHIVO= "solicitudes.json"



def listar_solicitudes():
    herramientas=registrar(ARCHIVO1)
    solicitudes=registrar("solicitudes.json") 
    print('********BIENVENIDO AL SISTEMA**********')   
    if not solicitudes:
        print('no hay solicitudes')
        return
    for elementos in solicitudes:
        print(f'ID: {elementos["id"]} -> {elementos ["nombre"]} -> {elementos["Herramienta"]} -> {elementos ["Cantidad"]} -> {elementos ["Fecha_inicio"]} -> {elementos ["Fecha_final"]}-> {elementos ["estado"]}')
    print()

def actualizar_estado(solicitudes):
    solicitudes=registrar("solicitudes.json")
    listar_solicitudes()
    id_solicitud=validadEntero("escoja el id del prestamo a actualizar")
    while(id_solicitud==None):
                id_solicitud=validadEntero('error, escoja el id del prestamo a actualizar')
                log("el usuario quiere colocar un numero que no es entero")
    contador = 0               
    for elemento in solicitudes: 
        if id_solicitud== elemento["id"]: 
            while True:
                    estado_prestamo = int(input("1. Pendiente, 2. Aprobado: "))
        if estado_prestamo==1:
            nuevo_estado="Pendiente"
            elemento["estado"] = nuevo_estado
            solicitudes[contador]["estado"]
            break
        elif estado_prestamo==2:
            nuevo_estado="aprobado"
            elemento["estado"] = nuevo_estado
            solicitudes[contador]["estado"]
            guardar("solicitudes.json", solicitudes)
            return solicitudes[contador]
        else: 
            estado_prestamo=int(input("Ingrese nuevamente la opcion: "))  
        contador+= 1

    guardar("solicitudes.json", solicitudes)
    return solicitudes[contador]