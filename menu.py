from validaciones import validadEntero, validarMenu, herramienta_valida, nombre_valido, persona_valida, validar_contraseñaadm
from gestionHerramientas import guarda_herramientas, actualizar_herramienta, eliminar_herramienta, listar_herramientas, existe_herramienta
from gestionPersona import guardar_persona, eliminar_persona, listar_persona, actualizar_persona, existe_persona
from gestionPrestamos import guardar_prestamo, listar_prestamos, eliminar_prestamo, existe_prestamo,actualizar_prestamo1, devolver_prestamo
from historial import *

def menu_principal():
    while True:
        op1=validarMenu('''
                        1. administrador
                        2. usuario
                        3. salir
                        ''',1,3)
        while op1==None:
                op1=validarMenu('error, intente nuevamente',1,3)
        match op1:
             case 1:
                  contraseña_adm()
             case 2:
                  menu_usuario()
             case 3:
                  print('gracias por utilizar nuestra aplicacion')
             case _:
                  print('error, opcion no encontrada')
        if op1==3:
            break                                                

def menu_administrador_2():
     while True:
        op=validarMenu('''
                        1. herramientas
                        2. personas
                        3. prestamos
                        5. historial
                        4. salir
                        ''',1,4)
        while op==None:
                op=validarMenu('error, intente nuevamente',1,4)
        match op:
             case 1:
                  menu_herramientas()
             case 2:
                  menu_persona()
             case 3:
                  menu_prestamos()
             case 4:
                  print('gracias por utilizar nuestra aplicacion')
             case 5:
                  historial()
             case _:
                  print('error, opcion no encontrada')
        if op==4:
            break                               

def menu_herramientas():
     while True:
          op2=validarMenu('''
                         1. crear herramientas
                         2. actualizar herramientas
                         3. listar herramientas
                         4. eliminar herramientas
                         5. salir
                         ''',1,5)
          while op2==None:
               op2=validarMenu('error, intentelo nuevamente',1,5)
          match op2:
               case 1:
                  guarda_herramientas()
               case 2:
                  actualizar_herramienta()
               case 3:
                  listar_herramientas()
               case 4:
                  eliminar_herramienta()       
               case 5:
                  print('gracias por utilizar nuestro sistema')
               case _:
                  print('error, opcion no encontrada')
          if op2==5:
               break             

def menu_prestamos():
     while True:
          op2=validarMenu('''
                         1. actualizar prestamo
                         2. listar prestamo
                         3. eliminar prestamo
                         4. salir
                         5. historial
                         ''',1,4)
          while op2==None:
               op2=validarMenu('error, intentelo nuevamente',1,4)
          match op2:
               case 1:
                  actualizar_prestamo1()
               case 2:
                  listar_prestamos()
               case 3:
                  eliminar_prestamo()     
               case 4:
                  print('gracias por utilizar nuestro sistema')
               case 5:
                    historial()
               case _:
                  print('error, opcion no encontrada')
          if op2==4:
               break             

def menu_usuario():
    while True:
        op2=validarMenu('''
                        1. quiero pedir una herramienta 
                        2. quiero devolver una herramienta
                        3. salir
                        ''',1,3)
        while op2==None:
                op2=validarMenu('error, intente nuevamente',1,3)
        match op2:
             case 1:
                    print("guardar solicitud")
             case 2:
                  devolver_prestamo()
             case 3:
                  print('gracias por utilizar nuestro sistema')
             case _:
                  print('error, opcion no encontrada')
        if op2==3:
            break
        
def menu_persona():
    while True:
        op1=validarMenu('''
                         1. crear usuario
                         2. actualizar usuario
                         3. listar usuario
                         4. eliminar usuario
                         5. salir
                        ''',1,5)
        while op1==None:
                op1=validarMenu('error, intente nuevamente',1,3)
        match op1:
             case 1:
                  guardar_persona()
             case 2:
                  actualizar_persona()
             case 3:
                  listar_persona()
             case 4:
                  eliminar_persona()
             case 5:
                  print('gracias por utilizar nuestra aplicacion')
             case _:
                  print('error, opcion no encontrada')
        if op1==5:
            break          

def contraseña_adm():
     while not validar_contraseñaadm('ingrese la contraseña'):
          contraseña = input('Ingrese la contraseña correcta')

     print('********BIENVENIDO AL SISTEMA********')        
     menu_administrador_2()


                     



                                                                       
