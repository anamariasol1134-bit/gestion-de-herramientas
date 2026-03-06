from gestionarJson import registrar, guardar, generar_id
from validaciones import validadEntero, validarMenu, herramienta_valida, nombre_valido, persona_valida
from log import *

ARCHIVO= "persona.json"

def guardar_persona():
    personas=registrar(ARCHIVO)

    nombre=input('ingrese el nombre de la persona')
    while nombre_valido(nombre)==False:
        nombre=input('ingrese un nombre valido')
        log("el usuario trato de poner el nombre en blanco")
    apellido=input('ingrese el apellido de la persona')
    while nombre_valido(apellido)==False:
        apellido=input('ingrese un apellido valido')
        log("el usuario trato de poner el nombre en blanco")
    telefono=(input('ingrese el numero de telefono'))
    while nombre_valido(telefono)==False:
        telefono=(input('ingrese el telefono'))
        log("el usuario trato de poner el nombre en blanco")
    direccion=(input('ingrese la direccion'))
    while nombre_valido(direccion)==False:
        direccion=(input('ingrese una direccion valida'))
        log("el usuario trato de poner el nombre en blanco")
    nueva_persona={
        "id":generar_id(personas),
        "nombre": nombre,
        "apellido":apellido,
        "telefono":str(telefono),
        "direccion":str(direccion),
    }    
    personas.append(nueva_persona)
    guardar(ARCHIVO, personas)
    print('persona guardada')

def listar_persona():
    personas=registrar(ARCHIVO)
    if not personas:
        print('no hay persona')
        return
    for elementos in personas:
        print(f'ID: {elementos["id"]} -> {elementos ["nombre"]} -> {elementos["apellido"]} -> {elementos ["telefono"]} -> {elementos ["direccion"]}')
    print()

def existe_persona(personas):
    id_persona=registrar(ARCHIVO)
    for elemento in listar_persona:
        if id_persona==elemento["id"]:
            return False
    return True    

def actualizar_persona():
    personas=registrar(ARCHIVO)
    listar_persona()
    id_persona=validadEntero("escoja el id de la persona a actualizar")
    while(id_persona==None):
        id_persona=validadEntero('error, escoja el id a actualizar')
        log("el usuario coloco un numero que no es entero")
    for elemento in personas:
        if id_persona==elemento["id"]:
            nombre=input('ingrese el nombre de la persona')
        while nombre_valido(nombre)==False:
            nombre=input('ingrese el nombre de la persona')
            log("el usuario intento colocar un nombre vacio")
        elemento["nombre"]=nombre
        guardar(ARCHIVO, personas)
        print('persona actualizada')
        return
    print("la persona no existe")

def eliminar_persona():
    contador_aux=0
    persona=registrar(ARCHIVO)
    listar_persona()
    id_persona=validadEntero("escoja el id a eliminar")
    while(id_persona==None):
        id_persona=validadEntero("escoja el id a eliminar")
        log("el usuario intento colocar un numero que no es entero")

    for elemento in persona:
        if id_persona==elemento["id"]:
            persona.pop(contador_aux)
            guardar(ARCHIVO, persona)
            print('persona eliminada')
            return       
        contador_aux+=1
    print("la persona no existe")    