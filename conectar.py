from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

usuario= os.getenv("USUARIO_MONGODB")
password = os.getenv("PASSWORD_MONGODB")
cluster= os.getenv("CLUSTER_MONGODB")

client = MongoClient('mongodb+srv://'+usuario+':'+password+'@'+cluster+'.i1bc4.mongodb.net/?retryWrites=true&w=majority&appName='+cluster)

try:
   client.admin.command('ping')
   print("NOS CONECTAMOS CORRECTAMENTE")
except Exception as e:
   print(e)