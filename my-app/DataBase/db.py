from pymongo import MongoClient, errors
from urllib.parse import quote_plus

class MeuBanco:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def adicionar_dados(self, collection, documento):
        # Verificar se o CPF já existe
        if collection.find_one({"cpf": documento["cpf"]}):
            print("CPF já existe.")
            return False
        try:
            result = collection.insert_one(documento)
            print(f"Documento adicionado com ID: {result.inserted_id}")
            return True
        except errors.PyMongoError as e:
            print(f"Ocorreu um erro ao adicionar o documento: {e}")
            return False


