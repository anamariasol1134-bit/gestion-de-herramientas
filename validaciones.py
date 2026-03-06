
def validadEntero(mensaje):
    try:
        return int(input(mensaje))
    except:
        return None
    
def validarMenu(mensaje, minimo, maximo):
    try:
        dato=int(input(mensaje))
        if dato<minimo or dato>maximo:
            return None
        else:
            return dato
    except:
        return None 
def herramienta_valida(herramienta):
    if herramienta.strip()=="":
        print("herramienta vacia")
        return False
    return True 
  
def nombre_valido(nombre):
    if nombre.strip()=="":
        print("nombre vacia")
        return False
    return True   
def persona_valida(persona):
    if persona.strip()=="":
        print("persona vacia")
        return False
    return True    
def precio_valido(precio):
    if precio <= 0:
        print("El precio no puede ser negativo")
        return False
    return True
def validar_contraseñaadm(mensaje):
    contrasena = input(mensaje).strip()
    contrasena_correcta = "777"

    if contrasena == "" or contrasena_correcta!=contrasena_correcta:
        print("Contraseña vacia")
        return False
    if contrasena == contrasena_correcta:
        return True
    print("***gracias por utilizar nuestro sistema***")
    

          