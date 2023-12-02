import pandas as pd

def Limpiar_datos(archivo):
    # GENERAR DATAFRAME
    df = pd.read_csv(archivo)

    # IMPRIMIR EL PORCENTAJE DE VALORES NULOS DE LA COLUMNA EDAD
    por_nul_edad = df["Age"].isnull().mean() * 100
    print("\n----------------PORCENTAJE NULOS EN EDAD-------------")
    print(f"El porcentaje de los valores nulos en la columna Edad es: {por_nul_edad:.2f}%")

    # ELIMINAR PASAJEROS CON EDAD DESCONOCIDA
    df = df.dropna(subset=["Age"])

    #PORCENTAJE DE VALORES NULOS EN LA COLUMNA CABIN
    por_nul_cabin = df["Cabin"].isnull().mean() * 100
    print("\n----------------PORCENTAJE NULOS EN CABIN-------------")
    print(f"El porcentaje de valores nulos en Cabin es: {por_nul_cabin:.2f}%")

    # SUSTITUIR CABIN POR SIN ESPECIFICAR
    df["Cabin"] = df["Cabin"].fillna("Sin especificar")

    print("\n----------------DATAFRAME RETORNADO-------------")
    return df

archivo = "datasets/titanic.csv"

df_limpio = Limpiar_datos(archivo)
print(df_limpio)