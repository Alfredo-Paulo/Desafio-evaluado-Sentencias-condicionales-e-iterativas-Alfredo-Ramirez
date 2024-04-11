from getpass import getpass
#inport getpass

password = getpass("ingrese clave secreta")
while password != "python2024":
    password = getpass("clave incorrecta, Ingrese de nuevo : ")

    print("clave correcta !")