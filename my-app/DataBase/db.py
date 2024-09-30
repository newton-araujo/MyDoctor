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

# # Criação da conexão com o MongoDB
# username = "newtonaraujo6"
# password = "Lorenzo@7045"  
# encoded_password = quote_plus(password)

# data_connection = f"mongodb+srv://{username}:{encoded_password}@systemmydoctor.8cxo4.mongodb.net/?retryWrites=true&w=majority&appName=SystemMyDoctor"
# connection_db = MeuBanco(data_connection, 'SystemMyDoctor') 

# # Exemplo de uso
# dados = {
#     "nome": "Newton de Paula Araujo",
#     "cpf": "00000000000",
#     "email": "teste@teste.com",
#     "seguranca": {
#         "password": "admin"
#     }
# }
# colecao = connection_db.db['sua_colecao']
# resultado = connection_db.adicionar_dados(colecao, dados)

# if not resultado:
#     print("Não foi possível adicionar os dados.")
