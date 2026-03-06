from gestionarJson import registrar, guardar, generar_id
from validaciones import validadEntero,validarMenu,persona_valida
from gestionHerramientas import listar_herramientas, guarda_herramientas,eliminar_herramienta,actualizar_herramienta, existe_herramienta, ARCHIVO1
from gestionPersona import listar_persona, guardar_persona, eliminar_persona, actualizar_persona
from gestionSolicitudes import *
from datetime import date, datetime
from log import *
ARCHIVO="prestamos.json"

    
def guardar_prestamo():
        prestamos = registrar(ARCHIVO)
        solicitud_aprobada = actualizar_estado()
        if solicitud_aprobada == None:
             print("no guardo nada")
             return 
        prestamos.append(solicitud_aprobada)
        guardar("prestamos.json", prestamos)
        
        print("Préstamo actualizado")
        return
       
def listar_prestamos():
    herramientas=registrar(ARCHIVO1)
    prestamos=registrar("prestamos.json") 
    print('********BIENVENIDO AL SISTEMA**********')   
    if not prestamos:
        print('no hay prestamos')
        return
    for elementos in prestamos:
        print(f'ID: {elementos["id"]} -> {elementos ["nombre"]} -> {elementos["Herramienta"]} -> {elementos ["Cantidad"]} -> {elementos ["Fecha_inicio"]} -> {elementos ["Fecha_final"]}-> {elementos ["estado"]}')
    print()
    
def existe_prestamo(prestamos):
        id_prestamo=registrar(ARCHIVO)
        for elemento in id_prestamo:
            if id_prestamo==elemento["id"]:
                return False
            return True    

def eliminar_prestamo():
        contador_aux=0
        prestamo=registrar(ARCHIVO)
        listar_prestamos()
        id_prestamo=validadEntero("escoja el prestamo a eliminar")
        while(id_prestamo==None):
            id_prestamo=validadEntero("escoja el id a eliminar")
            log("el usuario quiere colocar un numero que no es entero")

        for elemento in prestamo:
            if id_prestamo==elemento["id"]:
                prestamo.pop(contador_aux)
                guardar(ARCHIVO, prestamo)
                print('prestamo eliminado')
                return       
            contador_aux+=1
        print("el prestamo no existe")
def devolver_prestamo():
    herramientas = registrar(ARCHIVO1)
    prestamos = registrar("prestamos.json") 
    listar_prestamos()
    
    id_prestamo = validadEntero("ingrese el id de su prestamo...")
    
    while(id_prestamo == None):
        id_prestamo = validadEntero('error, escoja el id del prestamo a actualizar')
        log("el usuario quiere colocar un numero que no es entero")

    
    for prestamo in prestamos: 
        if prestamo["id"] == id_prestamo: 
            prestamo["estado"] = "Devuelto"
            for i in herramientas:
                 if i["nombre"]==prestamo["Herramienta"]:
                      i["cantidad"] +str (prestamo["Cantidad"])

            guardar("prestamos.json", prestamos)
            guardar(ARCHIVO1, herramientas) 
            print("Herramienta devuelta exitosamente")
            return       
