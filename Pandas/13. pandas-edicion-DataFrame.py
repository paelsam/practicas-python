import pandas as pd

bd = pd.DataFrame(np.arange(1,13).reshape([4,3]),
        index = ["a", "b", "c", "d"],
        columns = ["A", "B", "C"])
print("Antes:") 
print(bd)

# Podemos editar el valor de una serie o DataFrame a traves del metodo loc/iloc
bd.iloc[1,2] = "UwU"
print()
print("Despues:")
print(bd)

# Tambien podemos modificar los valores de una fila completa:
bd["A"] = [10, 20, 30, 40]
print()
print(bd)

# Podemos cambiar el valor de un volumen de bloques:
bd.loc["a":"b", "A":"B"] = -1
print()
print(bd)

# Podemos tambien hacerlo de esta forma: 
bd.loc["b":"c", "A":"B"] = [[-1,-2], [-3,-4]]
print()
print(bd)

# TE RECOMIENDO QUE INVESTIGUES MAS SOBRE ESTO...