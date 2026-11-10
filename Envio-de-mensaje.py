ruta_arch = "C:\\Users\\USUARIO\\Desktop\\Campus\\Python\\lectura-de-archivos.py\\mbox.txt"
ruta_dest= "C:\\Users\\USUARIO\\Desktop\\Campus\\Python\\lectura-de-archivos.py\\destinatarios.txt"


with open(ruta_arch, "r", encoding="utf-8") as arch, \
    open(ruta_dest, "w", encoding="utf-8") as dest:
    emails = []
    
    for linea in arch:
        if linea.startswith("From: "):
            correo = linea.split(" ")[1].strip()
            if correo not in emails:
                emails.append(correo)

    for correo in reversed(emails):
        mensaje = f"{correo} enviado [ok]"
        print(mensaje)
        dest.write(mensaje + "\n") 
