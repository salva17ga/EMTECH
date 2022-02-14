
from lifestore_file import lifestore_products # registros que maneja la tienda
from lifestore_file import lifestore_sales # registros compras
from lifestore_file import lifestore_searches # registros busquedas

# PROBLEMA: 
# acumulación de inventario 
# reduccion en las búsquedas de un grupo importante de productos ; disminucion de ventas ultimo trimestre

### Login de usuario: 
usuario = input ("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese la contraseña secreta: ")
desbloqueo = False

if contraseña == "emtech":
    print(f"Bienvenido {usuario}, preparando análisis de ventas:")
    global desbloqueo
    desbloqueo = True 
else: 
    print("No has ingresado la contraseña correcta")


### Productos más vendidos y productos rezagados a partir del análisis de las categorías con menores ventas y categorias 
# con menores búsquedas

# 5 productos con mayores ventas: 
# lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]

x = [] # lista vacía, para rellenarse con el id_product
x = [i[1] for i in lifestore_sales] # lista de unicamente el segundo indice de lifestore_sales

def contar(datos): # definir función para crear un diccionario de cuantas veces aparece cada dato
    result = {}
    for dato in datos: 
        if dato not in result: 
            result[dato] = 0 # meter contador 0 
        result[dato] += 1 # incrementar el contador de ese dato
    return result 

dicc = contar(x) # almacenamos el diccionario
respuesta = sorted(dicc.items(), key = lambda x: x[1], reverse = True) # lo ordenamos en función del valor con ayuda de una función lambda
print(f"Los cinco productos con mayores ventas, ordenados por (id, número de ventas), son: {respuesta[0:4]}") # con un slicing seleccionamos el top 5


# 10 productos con mayores búsquedas
# lifestore_searches = [id_search, id product]
busquedas = [] # creo lista vacia para rellenarla con el id de producto
for i in lifestore_searches: # se rellena la lista busquedas con todos los id producto 
     busquedas.append(i[1])

aux = contar(busquedas) ; print(aux) # hago un diccionario sobre el número de veces que aparece cada producto
respuesta_2 = sorted(aux.items(), key = lambda x: x[1], reverse = True ) 
respuesta_2 = respuesta_2[0:9]
print (f"Los 10 productos con mayores búsquedas, ordenados por (id_search, id_product), son: {respuesta_2}")

# por categoria, uno con los 5 productos con menores ventas y uno con los 10 productos con menores búsquedas
# listado de los 5 productos con menores ventas: 
respuesta_3 = sorted(dicc.items(), key = lambda x: x[1], reverse = False)
respuesta_3 = respuesta_3[0:15] 
print(f"los productos que sólo se han vendido una vez, ordenados por (id, numero de ventas), son: {respuesta_3}")

# listado de los 10 productos con menores búsquedas: 
respuesta_4 = sorted(aux.items(), key = lambda x: x[1], reverse = False) 
respuesta_4 = respuesta_4[0:9] ; print(respuesta_4)
print (f"Los productos que sólo fueron buscados una vez, ordenados por (id_search, id_product), son: {respuesta_4}")



### total de ingresos y ventas promedio mensuales, total anual y meses con más ventas al año (# de ventas, total de ingresos)
# total de ventas por mes y al año: 
# lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
import pandas as pd 
import datetime as dt 
id_sales=[] # creo una lista vacia por cada valor importante de la lista original
id_product=[]
score=[]
date=[]
refund=[]

for i in lifestore_sales: # cada lista se rellena con un ciclo for 
    id_sales.append(i[0]) 

for i in lifestore_sales: 
    id_product.append(i[1]) 

for i in lifestore_sales: 
    score.append(i[2]) 

for i in lifestore_sales: 
    date.append(i[3]) 

for i in lifestore_sales: 
    refund.append(i[4]) 

id_sales= pd.Series(id_sales) #convierto cada lista en series 
id_product=pd.Series(id_product)
score=pd.Series(score)
date=pd.Series(date)
refund=pd.Series(refund)

# concateno las series para analizarlas como un data frame: 
df = pd.concat([id_sales, id_product, score, date, refund], axis = 1)
rename = { # creo diccionario para renombrar el DF
    0:"id_sales", 
    1:"id_product", 
    2:"score", 
    3:"date", 
    4:"refund"
}

df = df.rename(columns=rename)
df["date"] = pd.to_datetime(df["date"])
print("Las ventas agrupadas por fecha a lo largo del año son:")
df.groupby(["date"])[["id_product", "date"]].value_counts() #df agrupando las ventas por fecha

# subset de data frames por mes: 

enero = (df["date"] >= "2020-01-01") & (df["date"] < "2020-02-01")
print(enero)
df_enero = df.loc[enero]

febrero = (df["date"] >= "2020-02-01") & (df["date"] < "2020-03-01")
df_febrero = df.loc[febrero]

marzo = (df["date"] >= "2020-03-01") & (df["date"] < "2020-04-01")
df_marzo = df.loc[marzo]

abril = (df["date"] >= "2020-04-01") & (df["date"] < "2020-05-01")
df_abril = df.loc[abril]

mayo = (df["date"] >= "2020-05-01") & (df["date"] < "2020-06-01")
df_mayo = df.loc[mayo]

junio = (df["date"] >= "2020-06-01") & (df["date"] < "2020-07-01")
df_junio = df.loc[junio]

julio = (df["date"] >= "2020-07-01") & (df["date"] < "2020-08-01")
df_julio = df.loc[julio]

agosto = (df["date"] >= "2020-08-01") & (df["date"] < "2020-09-01")
df_agosto = df.loc[agosto]

septiembre = (df["date"] >= "2020-09-01") & (df["date"] < "2020-10-01")
df_septiembre = df.loc[septiembre]

octubre = (df["date"] >= "2020-10-01") & (df["date"] < "2020-11-01")
df_octubre = df.loc[octubre]

noviembre = (df["date"] >= "2020-11-01") & (df["date"] < "2020-12-01")
df_noviembre = df.loc[noviembre] 

diciembre = (df["date"] >= "2020-12-01") & (df["date"] < "2020-12-31")
df_diciembre = df.loc[diciembre] 


print(f"En el año 2020, se realizaron {len(df)} ventas, de las cuales {len(df_enero)} fueron en enero, \
{len(df_febrero)} en febrero, {len(df_marzo)} en marzo, {len(df_abril)} en abril, {len(df_mayo)} en mayo, \
{len(df_junio)} en junio, {len(df_julio)} en julio, {len(df_agosto)} en agosto, {len(df_septiembre)} en septiembre, \
{len(df_octubre)} en octubre, {len(df_noviembre)} en noviembre y {len(df_diciembre)} en diciembre")

meses = pd.Series([len(df_enero), len(df_febrero), len(df_marzo), len(df_abril), len(df_mayo), 
                  len(df_junio), len(df_julio), len(df_agosto), len(df_septiembre), len(df_octubre), 
                  len(df_noviembre), len(df_diciembre)], index = ["Enero", "Febrero", "Marzo", "Abril", 
                  "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])
meses = meses.sort_values(ascending=False) 

print("Los meses ordenados de mayor a menor por número de ventas son:")
print(meses)

## total de ingresos mensuales: 
productos_id = [] 
productos_nombre = [] 
productos_precio = [] 

for i in lifestore_products: # cada lista se rellena con un ciclo for 
    productos_id.append(i[0]) 

for i in lifestore_products:
    productos_nombre.append(i[1]) 

for i in lifestore_products:
    productos_precio.append(i[2]) 

productos_id = pd.Series(productos_id) 
productos_nombre = pd.Series(productos_nombre)
productos_precio = pd.Series(productos_precio)

productos = pd.concat([productos_id, productos_nombre, productos_precio], axis = 1)
print(productos)

nombres_productos = {
    0 : "id_product", 
    1 : "product_name", 
    2 : "price"
}

productos = productos.rename(columns = nombres_productos)

# enero 
print("Detalle de productos vendidos en enero:")
ingresos_enero = pd.merge(df_enero, productos, left_on= "id_product", right_index=True)
print(ingresos_enero)
ventas_enero = sum(ingresos_enero["price"])
print(f"En enero, se registró un ingreso de {ventas_enero} pesos")

# febrero 
print("Detalle de productos vendidos en febrero:")
ingresos_febrero = pd.merge(df_febrero, productos, left_on= "id_product", right_index=True)
print(ingresos_febrero)
ventas_febrero= sum(ingresos_febrero["price"])
print(f"En febrero, se registró un ingreso de {ventas_febrero} pesos")

# marzo 
print("Detalle de productos vendidos en marzo:")
ingresos_marzo = pd.merge(df_marzo, productos, left_on= "id_product", right_index=True)
print(ingresos_marzo)
ventas_marzo = sum(ingresos_marzo["price"])
print(f"En marzo, se registró un ingreso de {ventas_marzo} pesos")

# abril 
print("Detalle de productos vendidos en abril:")
ingresos_abril = pd.merge(df_abril, productos, left_on= "id_product", right_index=True)
print(ingresos_abril)
ventas_abril= sum(ingresos_abril["price"])
print(f"En abril, se registró un ingreso de {ventas_abril} pesos")

# mayo 
print("Detalle de productos vendidos en mayo:")
ingresos_mayo = pd.merge(df_mayo, productos, left_on= "id_product", right_index=True)
print(ingresos_mayo)
ventas_mayo= sum(ingresos_mayo["price"])
print(f"En mayo, se registró un ingreso de {ventas_mayo} pesos")

# junio 
print("Detalle de productos vendidos en junio:")
ingresos_junio = pd.merge(df_junio, productos, left_on= "id_product", right_index=True)
print(ingresos_junio)
ventas_junio= sum(ingresos_junio["price"])
print(f"En junio, se registró un ingreso de {ventas_junio} pesos")

# julio 
print("Detalle de productos vendidos en julio:")
ingresos_julio = pd.merge(df_julio, productos, left_on= "id_product", right_index=True)
print(ingresos_julio)
ventas_julio= sum(ingresos_julio["price"])
print(f"En julio, se registró un ingreso de {ventas_julio} pesos")

# agosto 
print("Detalle de productos vendidos en agosto:")
ingresos_agosto = pd.merge(df_agosto, productos, left_on= "id_product", right_index=True)
print(ingresos_agosto)
ventas_agosto= sum(ingresos_agosto["price"])
print(f"En agosto, se registró un ingreso de {ventas_agosto} pesos")

# septiembre 
print("Detalle de productos vendidos en septiembre:")
ingresos_septiembre = pd.merge(df_septiembre, productos, left_on= "id_product", right_index=True)
print(ingresos_septiembre)
ventas_septiembre= sum(ingresos_septiembre["price"])
print(f"En septiembre, se registró un ingreso de {ventas_septiembre} pesos")

# octubre 
print("Detalle de productos vendidos en octubre:")
ingresos_octubre= pd.merge(df_octubre, productos, left_on= "id_product", right_index=True)
print(ingresos_octubre)
ventas_octubre= sum(ingresos_octubre["price"])
print(f"En octubre, se registró un ingreso de {ventas_octubre} pesos")

# noviembre 
print("Detalle de productos vendidos en noviembre:")
ingresos_noviembre = pd.merge(df_noviembre, productos, left_on= "id_product", right_index=True)
print(ingresos_noviembre)
ventas_noviembre= sum(ingresos_noviembre["price"])
print(f"En noviembre, se registró un ingreso de {ventas_noviembre} pesos")

# diciembre 
print("Detalle de productos vendidos en diciembre:")
ingresos_diciembre = pd.merge(df_diciembre, productos, left_on= "id_product", right_index=True)
print(ingresos_diciembre)
ventas_diciembre= sum(ingresos_diciembre["price"])
print(f"En diciembre, se registró un ingreso de {ventas_diciembre} pesos")

