import os
import errno

# Definimos el nombre del archivo y el contenido que queremos escribir en él
filename = "/foo/bar/baz.txt"
file_content = "Ejercicio 1"

# Comprobamos si la carpeta donde se encuentra el archivo existe. Si no existe, la creamos.
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

# Abrimos el archivo en modo escritura y escleacribimos el contenido en él
with open(filename, "w") as f:
    f.write("file_content")

# Mostramos por pantalla el mensaje "He acabado el ejercicio 1"
print("He acabado el ejercicio 1")  


    