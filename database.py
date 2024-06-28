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
    
    
    def initialize_database(self):
        db= self.db
        # Verificar se a coleção 'counters' existe e criar se não existir
        if 'counters' not in db.list_collection_names():
            db.create_collection('counters')

        # Verificar e inicializar o contador para 'empresa_id'
        if db.counters.find_one({"_id": "empresa_id"}) is None:
            db.counters.insert_one({
            "_id": "empresa_id",
            "seq": 0
        })

        # Verificar e inicializar o contador para 'contato_id'
        if db.counters.find_one({"_id": "contato_id"}) is None:
            db.counters.insert_one({
            "_id": "contato_id",
            "seq": 0
        })

        # Verificar e inicializar o contador para 'proposta_id'
        if db.counters.find_one({"_id": "proposta_id"}) is None:
            db.counters.insert_one({
            "_id": "proposta_id",
            "seq": 0
        })

    # Verificar e inicializar o contador para 'visita_id'
        if db.counters.find_one({"_id": "visita_id"}) is None:
            db.counters.insert_one({
            "_id": "visita_id",
            "seq": 0
        })

    # Verificar e inicializar o contador para 'imagem_id'
        if db.counters.find_one({"_id": "imagem_id"}) is None:
            db.counters.insert_one({
            "_id": "imagem_id",
            "seq": 0
        })

    # Verificar e inicializar o contador para 'revisao_id'
        if db.counters.find_one({"_id": "revisao_id"}) is None:
            db.counters.insert_one({
            "_id": "revisao_id",
            "seq": 0
        })

    # Verificar e inicializar o contador para 'tratativa_id'
        if db.counters.find_one({"_id": "tratativa_id"}) is None:
            db.counters.insert_one({
            "_id": "tratativa_id",
            "seq": 0
        })

    # Inicializar coleções para cada entidade
        collections = ['empresas', 'contatos', 'propostas', 'visitas', 'imagens', 'revisoes', 'tratativas']
        for collection in collections:
            if collection not in db.list_collection_names():
                db.create_collection(collection)    

database = Database()
database.test_connection()
database.initialize_database()