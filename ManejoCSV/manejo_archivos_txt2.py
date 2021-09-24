data = ["Linea 1", "Linea 2", "Linea 3", "Linea 4", "Linea 5"]

# Tenemos dos formas de escribir un archivo TXT

# De linea a linea
fic = open("text.txt", "w")
# for line in data:
#     fic.write(line)
#     fic.write("\n")
# fic.close()

# Podemos simplificar esto con la funcion print
for line in data:
    print(line, file=fic)
fic.close()

# Escribir el archivo de una vez
fic = open("text2.txt", "w")
fic.writelines("%s\n" % s for s in data)
fic.close()

# LEER ARCHIVOS TXT

# Tenemos dos formas de leer un archivo TXT

# Leer el archivo de una vez
fic = open("text.txt", "r")
lines = fic.readlines()
fic.close()
print(lines)

# De linea a linea 
# Podemos hacer un ciclo for y luego podemos guardar en una lista los valores iterados.
fic = open("text.txt", "r")
lines = []

for line in fic:
    lines.append(line)
fic.close()
print(lines)


# ELIMINAR SALTOS DE LINEA
# Podemos hacerlo con el metodo rstrip
line1= [s.rstrip("\n") for s in lines]
print(line1)

# Esto es solo un poco de lo que podemos hacer con los archivos de texto y Python
# Te recomiendo que leas la documentacion de Python para que profundices lo aprendido

