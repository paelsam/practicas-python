import pandas as pd 

# Tambien podemos utilizar booleanos en DataFrames:
df = pd.DataFrame(np.arange(18).reshape([6,3]), 
        index = ["a", "b", "c", "d", "e", "f"],
        columns = ["A", "B", "C"])

mask = [True, False, True, False, False, True]
# Imprimira el numero de filas con valor True
# Si la lista de bool no tiene los valores de index completo
# Dara Error
print(df[mask])


# La verdadera potencia de este estilo de selección se pone de manifiesto cuando la máscara se genera a
# partir de los datos del propio dataframe. Por ejemplo, si queremos seleccionar las filas para las que el valor
# de la columna A sea mayor que 7

print()
print(df[df.A > 7])

