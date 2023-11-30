import sqlite3

# Conecte-se ao banco de dados SQLite
conn = sqlite3.connect('biblioteca.db')
c = conn.cursor()

# Crie a tabela livros

c.execute("CREATE TABLE IF NOT EXISTS livros (id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, genero TEXT, ano INTEGER)")

# Confirme as alterações e feche a conexão
conn.commit()
conn.close()
