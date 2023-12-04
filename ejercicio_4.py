import numpy as np
import pandas as pd
import datetime as dt
def a(df_emi):
    columnas = ['ESTACION', 'MAGNITUD', 'ANO', 'MES'] + [f'D{i:02d}' for i in range(1, 32)]
    df_emi = df_emi[columnas]
    melt_emi= pd.melt(df_emi, id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='CONTAMINANTE/DIA')
    melt_emi['FECHA'] = pd.to_datetime(melt_emi['ANO'].astype(str) + '-' + melt_emi['MES'].astype(str) + '-' + melt_emi['DIA'].str[1:], errors='coerce')
    melt_emi = melt_emi[~np.isnat(melt_emi['FECHA'])]
    melt_emi = melt_emi.sort_values(by=['ESTACION', 'MAGNITUD', 'FECHA'])
    return melt_emi
def b(df_emisiones, ESTACION, MAGNITUD, FECHA_INICIO, FECHA_FIN):
    df_emisiones_r = df_emisiones[(df_emisiones['ESTACION'] == ESTACION) & (df_emisiones['MAGNITUD'] == MAGNITUD)]
    df_emisiones_r = df_emisiones_r[(df_emisiones_r['FECHA'] >= FECHA_INICIO) & (df_emisiones_r['FECHA'] <= FECHA_FIN)]
    emisiones = df_emisiones_r[['MAGNITUD', 'FECHA']]
    return emisiones

dfemisiones2017 = pd.read_csv("datasets/emisiones-2017.csv", sep=';')
dfemisiones2018 = pd.read_csv("datasets/emisiones-2018.csv", sep=';')
dfemisiones2019 = pd.read_csv("datasets/emisiones-2019.csv", sep=';')

dfemicon = pd.concat([dfemisiones2017, dfemisiones2018, dfemisiones2019], ignore_index=True)
resultado = a(dfemicon)

print(resultado)

estacionf = 8
magnitudf = 6
fechai = pd.to_datetime('2018-05-01')
fechaf = pd.to_datetime('2018-10-31')

emisiones = b(resultado, estacionf, magnitudf, fechai, fechaf)
print(emisiones)