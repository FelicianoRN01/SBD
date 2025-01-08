import redis
import json

# Conexión a la base de datos Redis

client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# 1 - Crear registros clave-valor
client.set('nombre', 'Ana')
client.set('apellidos', 'Martínez Pérez')
client.set('edad', 28)
client.set('ciudad', 'Barcelona')
client.set('formacion', 'Licenciada en Economía')
client.set('interes', 'Consultoría financiera')
client.set('experiencia', 'Analista financiera')

# 2 - Obtener y mostrar el número de claves registradas
num_keys = len(client.keys('*'))
print(f'Número de claves registradas: {num_keys}')

# 3 - Obtener y mostrar un registro en base a una clave

