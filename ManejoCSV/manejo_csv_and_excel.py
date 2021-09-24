import pandas as pd

# Manejo de archivos CSV

# Estas son básicamente archivos de texto en los que cada línea contiene 
# una fila de datos con múltiples registros delimitados por un separador (Comunmente una coma ",").

data = {
    "first_name": ["Sigrid", "Joe", "Theodoric", "Kennedy", "Beatrix", "Olimpia", "Grange", "Salle"],
    "last_name": ["Mannock", "Hinners", "Rivers", "Donnell", "Parlett", "Guenther", "Douce", "Johnstone"],
    "age": [27,31,36,53,48,36,40,34],
    "amount_1": [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
    "amount_2": [8.06, "?", 5.90, "?", "?", 7.48, 4.37, "?"]
}

data_DataFrame = pd.DataFrame(data)
# print(data_DataFrame)

# Acaba la implentacion
# Podemos cambiar el delimitador con el argumento "sep":
data_DataFrame.to_csv("example.csv")


# LECTURA DE ARCHIVOS CSV
df = pd.read_csv("example.csv",
                 # Omitimos la fila que se crea por defecto
                 skiprows=1,
                 names = ["UID", "First Name", "Last Name", "Age", "Sales #1", "Sales #2"],
                 # Reemplazamos los "?" por NaN
                 na_values=["?"],
                 # Le podemos añadir indices a los datos (Hasta mas de 1)
                 index_col=["First Name", "Last Name"]
                 )
print()
# print(df)


# MANEJO DE ARCHIVOS EXCEL

# Antes del guardar un archivo, debemos tener antes un DataFrame

df = pd.DataFrame(data, columns = ["first_name", "last_name", "age", "amount_1", "amount_2"])

# Ahora para exportar el archivo utilizamos el metodo to_excel
# Y con el atributo sheet_name especificamos la hoja en la que van a estar los datos:
df.to_excel("example.xlsx", sheet_name="example")


# LECTURA DE ARCHIVOS EXCEL

# Leemos archivos excel con el metodo read_excel.
# Si el archivo tiene mas de una hoja, podemos especificarla
df = pd.read_excel("example.xlsx", sheet_name="example")
print(df)

# Podemos omitir la cabecera con el metodo header
# Y con el atributo skiprows podemos ignorar filas
# Ademas, podemos cambiar el nombre de las filas con el atributo Names
df = pd.read_excel("example.xlsx", header=None, skiprows=1,
                   names=["UID", "First Name", "Last Name", "Age", "Sales #1", "Sales #2"]
                   )
print()
print(df)

# Como siempre, investiga un poco más...

