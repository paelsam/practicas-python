import pandas as pd

# Formas de contruir un DataFrame:

# Con un diccionario:

elementos = {
   "Numero atómico": [1,6,47,88],
   "Masa atómica": [1.008, 12.011, 107.87, 226],
   "Familia": ["No metal", "No metal", "Metal", "Metal"]
}
tabla_periodica = pd.DataFrame(elementos)
# print(tabla_periodica)

# Utilizando diferentes diccionarios:
# Los diccionarios deberán compartir el mismo conjunto de claves que se interpretarán como etiquetas de
# columnas. Si las etiquetas no coinciden, se crearán todas las columnas pero se asignarán NaN a los valores
# desconocidos:

unidades_2015 = {"Ag":2, "Au":5, "Cu":3, "Pt":2}
unidades_2016 = {"Ag":4, "Au":6, "Cu":7, "Pt":2}
unidades_2017 = {"Ag":3, "Au":2, "Cu":4, "Pt":1}

# Ahora le asignamos nombres a los indices de las filas

unidades = pd.DataFrame([unidades_2015,unidades_2016,unidades_2017], 
                        index= [2015,2016,2017])
# print(unidades)

