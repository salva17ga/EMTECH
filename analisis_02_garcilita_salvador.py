from operator import index
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/emtechinstitute/data-science-proyecto2/master/synergy_logistics_database.csv")

df.head() 
df.shape
df["direction"].describe()
df.columns

## 1) Rutas de importación y exportación 
# ¿cuales son las 10 rutas más demandadas? 
df["origin"].value_counts()
df["destination"].value_counts() # Rusia se repite

# vamos a homogeneizar: Russia con Rusia
df["destination"] = df["destination"].str.replace("Rusia", "Russia")

origenes = df["origin"].value_counts().head(10)
destinos = df["destination"].value_counts().head(10) # Rusia se repite

paises = pd.concat([origenes, destinos])
paises.describe
paises.unique
paises = paises.to_frame()
paises["pais"] = paises.index
paises.shape
paises.head()
paises_resumen = paises.groupby("pais").sum()
paises_resumen[0].sort_values(ascending=False).head(10) # respuesta 1 



## 2) medio transporte utilizado 
# ¿cuales son los 3 medios de transporte más importantes considerando el valor de las importaciones y exportaciones? 
# ¿cual es el medio de transporte que podrian reducir? 

df.head()
df["transport_mode"].value_counts()
df.groupby("transport_mode")["total_value"].sum().sort_values(ascending=False) # respuesta 2 

## 3) valor total de importaciones y exportaciones 
# ¿qué grupo de paises le generan el 80% del valor de las exportaciones e importaciones? 
df.head() 
df["direction"]=="Exports"

exportaciones = df[df["direction"] == "Exports"]
exportaciones.groupby("origin")[["origin", "total_value"]].sum().sort_values(by = "total_value",ascending=False).head(10)

importaciones = df[df["direction"] == "Imports"]
importaciones.groupby("destination")[["destination", "total_value"]].sum().sort_values(by = "total_value",ascending=False).head(10)