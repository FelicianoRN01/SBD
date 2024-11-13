from conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()

libreriaBD = cliente["libreria"]
librosColeccion = libreriaBD["libros"]

# Obtenemos el primer libro que encontremos
libro = librosColeccion.find_one()
print("Primer libro encontrado:")
print(libro)
print("\n")

# Obtenemos varios libros
libros = librosColeccion.find()
print("Listado de todos los libros:")
for l in libros:
    print(l)
    print("\n")

# Obtenemos libros pero sin el campo _id
libros2 = librosColeccion.find({}, { "_id": 0, "titulo": 1, "paginas": 1, "precio": 1, "disponible": 1 })
print("Listado de libros sin campo _id:")
for l in libros2:
    print(l)
    print("\n")

# Obtenemos libros pero sin los campos paginas y precio
libros3 = librosColeccion.find({}, {"paginas": 0, "precio": 0})
print("Listado de libros sin campos paginas y precio:")
for l in libros3:
    print(l)
    print("\n")
