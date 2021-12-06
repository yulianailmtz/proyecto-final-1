from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

nombre_usuario = ["Administrador"]
codigo_acceso = ["1307"]

usuario = input("Ingresar usuario: ")
contraseña = input("Ingresar contraseña: ")
if usuario in nombre_usuario and contraseña in codigo_acceso: 
  print("Ingresando...")
else:
  print("Acceso denegado") 

#se utilizan las funciones if y and para agregar un inicio de sesión, que de no proporcionar los datos correctos no permitirá avanzar en el programa
print("")
print("")
print("")

from collections import Counter

print("Productos con mayores ventas:")

lista_productos = []
#con esta función se extraen los datos de los productos vendidos
for product in lifestore_sales:
  lista_productos.append(product[1])

contador = Counter(lista_productos)
#utilizando la funcion de contador se suma cuantas veces se vendió un producto y después con most common se ordenan de la lista anterior el top 5 de los mas vendidos
mas_vendidos = contador.most_common(5)
#posteriormente se toma el top 5 y se convierten los id de los articulos en el nombre para que la información sea más entendible
for id in mas_vendidos:
  for nombre in lifestore_products:
    if nombre[0] == id[0]:
      print(nombre[1])

print("")
print("")

lista_busquedas = []

for product in lifestore_searches:
  lista_busquedas.append(product[1])
#al igual que en el caso anterior se crea una lista de las búsquedas por id, en seguida se cuentan estas busquedas y se extraen las 10  más buscadas
contador = Counter(lista_busquedas)

mas_buscados = contador.most_common(10)
#nuevamente se hace una conversión de id a nombres para reconocer el nombre de los productos
print("Productos con mayor búsquedas: ")
for id in mas_buscados:
  for nombre in lifestore_products:
    if nombre[0] == id[0]:
      print(nombre[1])

print("")
print("")

#lifestore_products = [id_product, name, price, category, stock]

#se hacen listas de listas tomando primero las categorías de los productos para ingresar los 5 con menores ventas y los 10 con menores búsquedas. Todo esto con la finalidad de que al final provee el nombre de los productos 
categorias = []

for product in lifestore_products:
  if product[3] not in categorias:
    categorias.append(product[3])

cat_products = [[] for x in range(len(categorias))]

counter = 0

for categoria in categorias:
  for product in lifestore_products:
    if product[3] == categoria:
      cat_products[counter].append(product)
  counter += 1

for i in range(len(categorias)):

  print("")
  print(categorias[i])
  print("")
  print("Menos comprados: ")
  print("")

  lista_categoria = []

  for prod in cat_products[i]:
    lista_categoria.append(prod[0])

  lista_productos = []

  for product in lifestore_sales:
    if product[1] in lista_categoria:
      lista_productos.append(product[1])

  contador = Counter(lista_productos)

  menos_vendidos = contador.most_common()

  if len(menos_vendidos) < 6:
    for j in range(len(menos_vendidos)):
      for nombre in lifestore_products:
        if nombre[0] == menos_vendidos[-j][0]:
          print(nombre[1])
  else:
    for j in range(1, 6):
      for nombre in lifestore_products:
        if nombre[0] == menos_vendidos[-j][0]:
          print(nombre[1])

  print("")
  print("Menos buscados: ")
  print("")

  lista_busquedas = []

  for product in lifestore_searches:
    if product[1] in lista_categoria:
      lista_busquedas.append(product[1])

  contador = Counter(lista_busquedas)

  menos_buscados = contador.most_common()

  if len(menos_buscados) < 11:
    for j in range(len(menos_buscados)):
      for nombre in lifestore_products:
        if nombre[0] == menos_buscados[-j][0]:
          print(nombre[1])
  else:
    for j in range(1, 11):
      for nombre in lifestore_products:
        if nombre[0] == menos_buscados[-j][0]:
          print(nombre[1])

print("")
print("")


#A continuación se crea un promedio de calificación por producto para posteriormente saber cuales son los 5 productos que recibieron la más alta evaluación y cuales son los 5 que recibieron la menor. 

print("Productos mejor evaluados: ")
reseñas = []
score = []

for product in lifestore_products:
  for sale in lifestore_sales:
    if sale[1] == product[0]:
      score.append(sale[2])
  if len(score) > 0:
    reseñas.append([sum(score) / len(score), product[0], product[1]])
  score = []

reseñas.sort()
for i in range(5):
  print(reseñas[i][2])
print("")
print("Productos peor evaluados: ")

reseñas = []
score = []

for product in lifestore_products:
  for sale in lifestore_sales:
    if sale[1] == product[0]:
      score.append(sale[2])
  if len(score) > 0:
    reseñas.append([sum(score) / len(score), product[0], product[1]])
  score = []

reseñas.sort(reverse=True)
for i in range(1, 6):
  print(reseñas[-i][2])

print("")
print("")

#A continuación se ordenan los meses para extraer las fechas en que se realizaon las ventas y posteriormente sumar cual fue el total de ventas por mes. Al conocer el número de ventas y cuáles son los productos vendidos se puede obtener cuáles fueron los ingresos en cada mes. 

months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

lista_meses =  [[] for x in range(len(months))]

counter = 0

for month in months:
  for sale in lifestore_sales:
    if month == sale[3][3:5]:
      lista_meses[counter].append(sale)
  counter += 1

ventas = []
ingresos = []

ven = 0
ing = 0

for meses in lista_meses:
  for product in lifestore_products:
    for mes in meses:
      if product[0] == mes[1]:
        ven += 1
        ing += product[2]
  ventas.append(ven)
  ingresos.append(ing)
  ven = 0
  ing = 0

print("Ventas por mes: ")
print(ventas)
print("Ingresos por mes: ")
print(ingresos)

print("")


ventas = []

ven = 0
ing = 0
counter = 0
ven_anual = 0
ing_anual = 0

for meses in lista_meses:
  for product in lifestore_products:
    for mes in meses:
      if product[0] == mes[1]:
        ven += 1
        ing += product[2]
  ventas.append([ven, ing, months[counter]])
  counter += 1
  ven_anual += ven
  ing_anual += ing
  ven = 0
  ing = 0

for info in ventas:
  print("El mes {} se vendio {} con {} de ingreso".format(info[2], info[0], info[1]))

#Por último, se suman las ventas para saber los ingresos anuales, al igual que se ordenan dichas ventas de mayor a menor para conocer los meses con más ventas al año. 

print("Las ventas anuales son {} y un ingreso de {}".format(ven_anual, ing_anual))

ventas.sort(reverse=True)

print("")
print("")
print("Los meses ordenados por mas ventas a menos ventas son: ")
for info in ventas:
  print("El mes {} se vendio {} con {} de ingreso".format(info[2], info[0], info[1]))




