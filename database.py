from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

class Database:
    def __init__(self):
        self.client = None
        self.db = None
        try:
            self.client = MongoClient(os.getenv("MONGO_URI"))
            self.db = self.client[os.getenv("DB_NAME", "sales_management")]
        except Exception as e:
            print("Erro ao criar ou conectar ao banco de dados:", e)

    def get_database(self):
        return self.db

    def close_connection(self):
        if self.client:
            self.client.close()

    def test_connection(self):
        try:
            self.client.admin.command('ping')
            print("Conexão com o MongoDB bem-sucedida!")
        except Exception as e:
            print("Erro ao conectar ao MongoDB:", e)
    

database = Database()
database.test_connection()