from gestionarJson import registrar, guardar, generar_id
from validaciones import validadEntero, validarMenu, herramienta_valida, precio_valido
from log import *

ARCHIVO1= "heramientas.json"

def menu_categoria():
            while True:
                categoria_op=validarMenu('''
                        1. carpinteria
                        2. jardineria
                        3. de casa
                        ''',1,3)
                match categoria_op:
                    case 1:
                        return ("carpinteria")
                    case 2:
                        return ("jardineria")
                    case 3:
                        return ("de casa")
                    case _:
                        categoria_op=int(input("error, opcion no valida"))


def guarda_herramientas():
    herramientas=registrar(ARCHIVO1)
    categoria=menu_categoria()
    while herramienta_valida(categoria)==False:
        categoria=input('ingrese la categoria')
        log("el usuario coloco un nombre vacio")
    
    nombre_herramienta=input('ingrese el nombre de la herramienta')
    while herramienta_valida(nombre_herramienta)==False:
        nombre_herramienta=input('ingrese el nombre de la herramienta valido')
        log("el usuario coloco un nombre vacio")
    
    cantidad=(input('ingrese la cantidad que tiene'))
    while herramienta_valida(cantidad)==False:
        cantidad=input('ingrese una cantidad valida')
        log("el usuario coloco un nombre vacio")
    
    precio=float(input('ingrese el precio de la herramienta'))
    while precio_valido(precio)==False:
          precio=float(input('ingrese un precio valido')) 
          log("el usuario quizo colocar un numero negativo")
    
    estado=(input('ingrese el estado de la herramienta'))
    while herramienta_valida(estado)==False:
          estado=(input('ingrese el estado de la herramienta'))
          log("el usuario coloco un nombre vacio")
       
           
    nueva_herramienta={
            "id": generar_id(herramientas),
            "nombre": nombre_herramienta,
            "categoria": categoria,
            "cantidad":cantidad,
            "valor": str(precio),
            "estado": estado.lower()
    }    
    herramientas.append(nueva_herramienta)
    guardar(ARCHIVO1,herramientas)
    print('herramienta guardada')

def listar_herramientas():
    herramientas=registrar(ARCHIVO1)
    if not herramientas:
        print("no hay herramientas")
        return
    for elemento in herramientas:
        print(f'ID:{elemento["id"]} -> {elemento["nombre"]} -> {elemento["categoria"]} -> {elemento["cantidad"]} -> {elemento["valor"]} -> {elemento["estado"]}')
    print()

def existe_herramienta(nombre):
    herramientas=registrar(ARCHIVO1)
    for elemento in herramientas:
        if nombre.lower()==elemento["nombre"].lower():
            return True
    return False

def actualizar_herramienta():
    herramientas=registrar(ARCHIVO1)
    listar_herramientas()
    id_herramienta=validadEntero("escoja el id a actualizar")
    while(id_herramienta==None):
        id_herramienta=validadEntero('error, escoja el id a actualizar')
        log("el usuario quiere colocar un numero que no es entero")

    for elemento in herramientas:
        if id_herramienta==elemento["id"]:
            nombre=input('ingrese el nombre de la herramienta')
            while herramienta_valida(nombre)==False:
                nombre=input('ingrese el nombre de la herramienta')
                log("el usuario coloco un nombre vacio")

            elemento["nombre"]=nombre
            guardar(ARCHIVO1, herramientas)
            print('herramienta actualizada')
            return
    print("la herramienta no existe")

def eliminar_herramienta():
    contador_aux=0
    herramientas=registrar(ARCHIVO1)
    listar_herramientas()
    id_herramienta=validadEntero("escoja el id a eliminar")
    while(id_herramienta==None):
        id_herramienta=validadEntero("escoja el id a eliminar")
        log("el usuario quiere colocar un numero que no es entero")

    for elemento in herramientas:
        if id_herramienta==elemento["id"]:
            herramientas.pop(contador_aux)
            guardar(ARCHIVO1, herramientas)
            print('herramienta eliminada')
            return       
        contador_aux+=1
    print("la profesion no existe")    
    
    
    
    
     
        
