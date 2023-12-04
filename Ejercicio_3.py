"""Examen unidad 2 y 3
Grupo 951
Navarrete Anguiano Roxana Aurora
Torres Celedon David Antonio
Gallardo del Rosario Christian Pablo
Rico Ruiz Brandon Israel"""


import pandas as pd
"""Crear un programa que contenga las siguientes funciones:
a. 	Crear una función que retorne un DataFrame indexado, con la siguiente Información: (5%)
"""
def create_dataframe():
    data = {"Calorias": [420,380,390,490,300],
            "Tiempo": [60,40,75,55,45]}
    d_index = ["L", "M", "X", "J", "V"]
    df = pd.DataFrame(data, index = d_index)
    return df


"""Crear una función que reciba como parámetro el Data Frame anterior, y retorne la media, mediana y desviación estándar de ambas columnas. (5%)
"""
def estadisca(df):
    columnas = ["Calorias", "Tiempo"]
    media =df[columnas].mean()
    mediana = df[columnas].median()
    desv_est =  df[columnas].std()
    return media,mediana,desv_est

"""Desarrollar una función que agregue otra columna al Data Frame para ver si se ha cumplido el reto de quemar más de 400 calorías por hora (Calorías/Tiempo > 400/60). El Data Frame resultante debe ser el siguiente: (5%) 
"""
def nueva_columna(df):
    df_nuevo= df
    df_nuevo["Reto"] = df_nuevo["Calorias"] / df_nuevo["Tiempo"] > 400/60
    return df_nuevo

"""Crear una función que retorne el porcentaje de días que se ha conseguido el reto y los que no. (10%)
"""
def porcentaje_cumplimiento_reto(df):
    total_dias = len(df)
    cumplidos = 0
    no_cumplidos = 0

    for indice, fila in df.iterrows():
        if fila["Reto"]:
            cumplidos += 1
        else:
            no_cumplidos += 1

    porcentaje_cumplidos = (cumplidos / total_dias) * 100
    porcentaje_no_cumplidos = (no_cumplidos / total_dias) * 100

    return porcentaje_cumplidos, porcentaje_no_cumplidos

#ejecutar e imprimir 
df= create_dataframe()
est= estadisca(df)
reto= nueva_columna(df)
porcentaje =porcentaje_cumplimiento_reto(reto)

print(f"dataframe\n{df}\n estadisticas\n {est}\n Reto cumplido \n{reto}\n cumplimiento \n{porcentaje} ")