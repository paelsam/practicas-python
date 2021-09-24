# MANEJO DE ARCHIVOS TXT

# Por defecto la conexión se abre en modo lectura, con lo que no es posible escribir en el archivo. Para
# poder escribir es necesario utilizar la opción "w" con la que se eliminará cualquier archivo existente y
# creará uno nuevo. Otra opción que se puede utilizar es "a", con la que se añadirá nuevo contenido al
# archivo existente. Las opciones se pueden ver en el siguiente código.

# Se abre el archivo para escribir y elimina archivos anteriores si existen
file = open("text.txt", "w")

# Abre el archivo para agregar contenido 
file = open("text.txt", "a")

# Abre el archivo en modo lectura
file = open("text.txt", "r")

# Una vez finalizado todo, debemos cerrar todos los procesos
file.close()

# La r indica el modo lectura. Si se intentara utilizar la función write para escribir algo, se lanzaría la
# excepción IOError. A continuación los distintos modos.
# •r – Lectura únicamente.
# •w – Escritura únicamente, reemplazando el contenido actual del archivo o bien creándolo si es
# inexistente.
# •a – Escritura únicamente, manteniendo el contenido actual y añadiendo los datos al final del archivo.
# •w+, r+ o a+ – Lectura y escritura.
# El signo '+' permite realizar ambas operaciones. La diferencia entre w+ y r+ consiste en que la primera
# opción borra el contenido anterior antes de escribir nuevos datos, y crea el archivo en caso de ser
# inexistente. a+ se comporta de manera similar, aunque añade los datos al final del archivo.
# Todas las opciones anteriores pueden combinarse con una 'b' (de binary), que consiste en leer o escribir
# datos binarios. Esta opción es válida únicamente en sistemas Microsoft Windows, que hacen una
# distinción entre archivos de texto y binarios. En el resto de las plataformas, es simplemente ignorada.
# Ejemplos: rb, wb, ab+, rb+, wb+

