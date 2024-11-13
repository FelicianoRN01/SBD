from conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()

libreriaBD = cliente["libreria"]
librosColeccion = libreriaBD["libros"]

#Busca libros que tienen 1072 paginas
miquery = { "paginas": 1072 }

libros = librosColeccion.find(miquery)

print("Libros con 1072 páginas:")
for libro in libros:
    print(libro)
    print("\n")

# Busca libros con precio mayor o igual a 5 y cuyo título empiece con '1'
libros = librosColeccion.find({
    "$and": [
        { "titulo": { "$regex": "^1" } },  
        { "precio": { "$gte": 5 } }         
    ]
})

print("Libros con cuyo título empiece con '1' y el precio sea mayor que uno")
for libro in libros:
    print(libro)
    print("\n")


#libros que no tengan mas de 600 paginas y no cuesten mas de 30 euros
libros = librosColeccion.find({
    "paginas": { "$lte": 600 },
    "precio": { "$lte": 30 }
})

print("Libros que no tengan más de 600 páginas y precio menor a 30 euros:")
for libro in libros:
    print(libro)
    print("\n")

print("Listado de libros ordenados por titulo descendente")

librosOrdenadosPortituloDescendente = librosColeccion.find().sort("titulo",-1)
for d in librosOrdenadosPortituloDescendente:
    print(d)
    print("\n")


miqueryel = { "titulo": "Cien Años de Soledad" }

resultado = librosColeccion.delete_one(miqueryel)

print(resultado.deleted_count, " documento eliminado.")

miqueryact = { "titulo": "1984" }
nuevosValores = { "$set": { "precio": "1,99" } }

resultado1 = librosColeccion.update_many(miqueryact, nuevosValores)
