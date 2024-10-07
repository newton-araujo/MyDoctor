import random
import sqlite3 as sq

def consultar_usuario(cpf):
    banco = "my-app/DataBase/mydocutor.db"
    
    try:
        conn = sq.connect(banco)
        cursor = conn.cursor()

        query = """
            SELECT * FROM usuarios WHERE cpf = ?
        """
        
        cursor.execute(query, (cpf,))
        resultado = cursor.fetchone()
        
        cursor.close()
        conn.close()  # Corrigido aqui

        # Se usuário cadastrado
        if resultado:
            return True
        else:
            return "Usuário não cadastrado!"
        
    # Em caso de erro de conexão com o banco
    except sq.Error as error:
        return f"Erro: {error}"

def new_cadastrar_usuario(nome, email, cpf, senha):
    banco = "my-app/DataBase/mydocutor.db"
    
    try:
        conn = sq.connect(banco)
        cursor = conn.cursor()
        
        # Método para verificar se o código já foi adicionado
        def check_cod_user(cod):
            query_id = '''
                SELECT cd_usuario FROM usuarios WHERE cd_usuario = ?
            '''
            cursor.execute(query_id, (cod,))
            result = cursor.fetchone()
            
            return result is not None
        
        # Método para gerar código
        def gerar_cod_usu():
            return random.randint(1, 1000)  # Corrigido aqui

        cod_usu = gerar_cod_usu()

        # Verifica se o código já existe e gera um novo se necessário
        while check_cod_user(cod_usu):
            cod_usu = gerar_cod_usu()
        
        # Query para Insert
        insert_query = '''
            INSERT INTO usuarios (cd_usuario, nome_usuario, email, CPF, senha) VALUES (?, ?, ?, ?, ?)
        '''
        
        dados = (cod_usu, nome, email, cpf, senha)
        
        cursor.execute(insert_query, dados)
        conn.commit()
        
        cursor.close()
        conn.close()  # Corrigido aqui
        
        return "Usuário Cadastrado com Sucesso!"
    
    except sq.Error as error:
        return f"Erro: {error}"

