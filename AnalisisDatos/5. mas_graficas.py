import matplotlib.pyplot as plt
import pandas as pd

# Import data and create dataframe
liquido_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
liquido_column_headers = ['Alcohol', 'Acido Malico', 'Cenizas', 'Alcalinidad de las cenizas', 'Magnesio', 'Fenoles totales', 'Flavonoides',
                          'Fenoles no flavonoloides', 'Proantocianinas', 'Intensidad de color', 'Matiz', 'OD280/OD315 de sustancia diluida', 'Prolina']
liquido_df = pd.read_csv(liquido_url, names=liquido_column_headers)

# Figure
fig, ax1 = plt.subplots()
fig.set_size_inches(13, 10)

# Labels data
ax1.set_xlabel("Alcohol")
ax1.set_ylabel("Intensidad de Color")
ax1.set_title(
    "Relacion entre la intensidad de color y la cantidad de alcoho en el liquido")

# r sequence
c = liquido_df["Intensidad de color"]

# Plot
plt.scatter(liquido_df["Alcohol"], liquido_df["Intensidad de color"],
            c=c, cmap='RdPu', s=liquido_df["Prolina"]*.5, alpha=.5)
cbar = plt.colorbar()
cbar.set_label("Intensidad de color")
plt.show()
