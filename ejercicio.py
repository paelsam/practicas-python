import pandas as pd
from pandas.core.algorithms import duplicated, value_counts


def casos(ruta: str) -> list:

    df = pd.read_csv(ruta, index_col=1)

    df.loc[df["Sexo"] == "f", "Sexo"] = "F"
    df.loc[df["Sexo"] == "m", "Sexo"] = "M"

    sex_porcent = df.groupby(["Sexo"]).agg({"Sexo": "count"})
    sex_porcent = sex_porcent["Sexo"]*100
    sex_porcent = sex_porcent / len(df["Sexo"])
    sex_porcent = sex_porcent.round(4)

    departament_mean = df.groupby(
        "Departamento o Distrito").agg({"Edad": "mean"})
    departament_mean = departament_mean.round(4)

    infected = df[df["Tipo"] == "Importado"]
    infected = infected.groupby(["País de procedencia"]).agg(
        {"País de procedencia": "count"})
    infected = infected["País de procedencia"]*100
    infected = infected / len(df[df["Tipo"] == "Importado"].index)
    infected = infected.round(4)

    dict_sex = sex_porcent.to_dict()
    dict_age = departament_mean.to_dict()
    dict_age = departament_mean["Edad"].to_dict()
    dict_infected = infected.to_dict()

    return ([dict_sex, dict_age, dict_infected])


ruta = "docs/Casos_positivos_de_COVID-19_en_ColombiaDiezMil.csv"
print(casos(ruta))
