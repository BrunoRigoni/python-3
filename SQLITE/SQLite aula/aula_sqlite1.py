import sqlite3

banco = sqlite3.connect('primeiro_banco.db')


cursor = banco.cursor()

# cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

cursor.execute("INSERT INTO pessoas VALUES('Bruno',24,'bruno@mail.com')")

banco.commit()
