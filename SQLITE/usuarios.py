from banco import conectar


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def cadastrar_usuario(nome):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome) VALUES (?)', (nome,))
    conn.commit()
    conn.close()
    print(f"Usuário '{nome}' cadastrado com sucesso!")


def listar_nomes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    cursor.close()

    if usuarios:
        print(f"\n=== LISTA DE USUARIOS CADASTRADOS ===")
        for usuario in usuarios:
            print(f"ID: {usuario[0]} | Nome:{usuario[1]}")
        else:
            print(f"\nNenhum usuario encontrado.")
