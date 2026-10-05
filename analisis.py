import pandas as pd

archivo = "C:\\Users\\12505\\Downloads\\sensores_industriales.csv"

df = pd.read_csv(archivo)

print(df.head())
print(df.shape)
print(df.columns)

print("Total de registros:", len(df))
print("Total de sensores:", df["id_sensor"].nunique())

promedio_planta = df.groupby("planta")["temperatura_c"].mean()

print("\nPromedio de temperatura por planta:")
print(promedio_planta)

indice_max = df["temperatura_c"].idxmax()
registro_max = df.loc[indice_max]

print("\nTemperatura máxima:")
print("Temperatura:", registro_max["temperatura_c"])
print("Sensor:", registro_max["id_sensor"])
print("Fecha y hora:", registro_max["fecha_hora"])

alertas = df[df["temperatura_c"] > 85]

print("\nTotal de alertas:", len(alertas))

alertas_por_planta = alertas.groupby("planta").size()

print("\nAlertas por planta:")
print(alertas_por_planta)

alertas.to_csv("resultados/alertas.csv", index=False)

print("\nArchivo de alertas guardado correctamente.")