import matplotlib.pyplot as plt
import pandas as pd

# Datos del DataFrame usando un formato de fecha arbitrario (m/d/y)
df = pd.DataFrame({
    'Name': [
        'Jhon', 'Lisa', 'Peter', 'Carl', 'Linda', 'Betty'
    ],
    'Date_of_Birth': [
        '01/21/1998', '03/10/1997', '7/25/1999', '01/22/1977', '09/3/1968', '09/15/1970'
    ]
})

df["Date_of_Birth"] = pd.to_datetime(
    df['Date_of_Birth'], infer_datetime_format=True)
plt.clf()
df['Date_of_Birth'].map(lambda d: d.month).plot(kind='hist')
plt.show()
