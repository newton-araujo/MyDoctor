import firebase_admin
from firebase_admin import credentials, db
from firebase_admin.exceptions import FirebaseError


def initialize_firebase():
    try:
      
        if not firebase_admin._apps:
           
            cred = credentials.Certificate("credencial/mydoctor.json")
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://mydoctor-28643-default-rtdb.firebaseio.com/'
            })
            print("Conexão com o Firebase estabelecida com sucesso.")
        else:
            print("Firebase já foi inicializado.")
    except FileNotFoundError as e:
        print(f"Erro: Arquivo de credenciais não encontrado. Detalhes: {e}")
    except FirebaseError as e:
        print(f"Erro ao conectar-se ao Firebase. Detalhes: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


initialize_firebase()

user_r = db.reference("users")

def buscando_id(id):
    
    user = user_r.child(id).get()
    
    print(user)
    if user:
        return True
    else:
        return False


buscando_id("12345678900")