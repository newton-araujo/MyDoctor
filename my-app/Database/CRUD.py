from Database.connect_firebase import initialize_firebase
from firebase_admin import credentials, db, auth, firestore
from time import sleep

initialize_firebase()


users_ref = db.reference('usuarios')

#Criar usuario
def cadastrar_cliente(nome, email, cpf, senha):
    try:
        
        usuario_r = users_ref.get()
        
        for k, v in usuario_r.items():
            
            if v['cpf'] == cpf:
                return False
        
        
        users_ref.child(nome).set(
            {
                'nome':str(nome),
                'email':str(email),
                'cpf':str(cpf) ,
                'senha':str(senha)
            }
        )    
        
        return True
    
    except Exception as e:
        print(f"Erro ao cadastrar o cliente: {e}")
        return False

#Autenticando Usuários LOGIN
def validar_autenticacao(nome, senha):
    try:
        usuarios_r = users_ref.get()
        acesso = False
        
        for k, v in usuarios_r.items():
            
            if v.get('nome') == nome and v.get('senha') == senha:
                acesso = True
        
        if acesso:
            return True
        else:
            return False 
            
    
    except Exception as e:
        return f"Erro: {e}"

#Buscando dados para reset de senha
def buscar_dados(email,cpf):
    
    try:
        usuario_ref = users_ref.get()
        encontrado = False
        
        for k, v in usuario_ref.items():
            
            if v['email'] == email or v['cpf'] == cpf:
                encontrado = True

        if encontrado:
            return True
        else:
            return False
        
    except Exception as e:
        return f"Erro: {e}"
        

def resetar_senha(cpf, email, nova_senha):
    usuarios = users_ref.get()
    encontrado = False
    try:
        for k, v in usuarios.items():
            if v.get('cpf') == cpf or v.get('email') == email:
                users_ref.child(k).update({'senha': nova_senha})
                encontrado = True
                break  

        if encontrado:
            return 'Senha atualizada com sucesso.'
        else:
            return 'Erro: Usuário não encontrado.'
        
    except Exception as e:
        return f'Erro: {e}'

    
        