import numpy as np
import pandas as pd 

# Metodo value_counts
# Este método devuelve una estructura conteniendo los valores 
# presentes en la serie y el número de ocurrencias de
# cada uno. Estos valores se muestran en orden decreciente

# Como puede apreciarse, por defecto no se incluyen los valores nulos. 
# Este comportamiento puede modificarse haciendo uso del parámetro dropna
s = pd.Series([3,1,2,1,1,4,1,2, np.nan])
print(s.value_counts(dropna = False))

# Tambien podemos agruparlos en bins
print()
print(s.value_counts(bins=2))