
from lifestore_file import lifestore_products # registros que maneja la tienda
from lifestore_file import lifestore_sales # registros compras
from lifestore_file import lifestore_searches # registros busquedas

# PROBLEMA: 
# acumulación de inventario 
# reduccion en las búsquedas de un grupo importante de productos ; disminucion de ventas ultimo trimestre

### Login de usuario: 
usuario = input ("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese la contraseña secretísima: ")
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
lifestore_searches[0:3]

# por categoria, uno con los 5 productos con menores ventas y uno con los 10 productos con menores búsquedas


### productos por reseña en el servicio a partir del análisis de categorías con mayores ventas y categorias con mayores búsquedas
# dos listados, top 5 productos con las mejores reseñas y otro con las peores, considerando productos con devolución
# (NO CONSIDERAR PRODUCTOS SIN RESEÑAS)



### sugerir una estrategia de productos a retirar del mercado así como sugerencia de cómo reducir la acumulación de inventario 
# considerando los datos de ingresos y ventas mensuales 
