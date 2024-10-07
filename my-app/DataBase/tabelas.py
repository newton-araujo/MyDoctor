import sqlite3 as sq


def usuarios():    
    conn = sq.connect("my-app/DataBase/mydocutor.db")
    cursor = conn.cursor()
    
    user = f"""
        CREATE TABLE IF NOT EXISTS usuarios(
            cd_usuario INTEGER PRIMARY KEY,
            nome_usuario TEXT,
            email TEXT,
            CPF TEXT,
            senha TEXT
        )
    """
    
    cursor.execute(user)

    cursor.close()
    conn.close()
        

usuarios()


# conn = sq.connect("my-app/DataBase/mydocutor.db")
# cursor = conn.cursor()
# cursor.close()
# conn.close()