
import sqlite3

class Livro:
    def __init__(self, id, titulo, autor, genero, ano):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano = ano

    def adicionar_livro(self):
        conn = sqlite3.connect('biblioteca.db')
        c = conn.cursor()
        c.execute("INSERT INTO livros VALUES (:id, :titulo, :autor, :genero, :ano)",
                  {'id': self.id, 'titulo': self.titulo, 'autor': self.autor,
                   'genero': self.genero, 'ano': self.ano})
        conn.commit()
        conn.close()

    @staticmethod
    def visualizar_todos_livros():
        conn = sqlite3.connect('biblioteca.db')
        c = conn.cursor()
        c.execute("SELECT * FROM livros")
        livros = c.fetchall()
        conn.close()
        return livros

    def atualizar_livro(self):
        conn = sqlite3.connect('biblioteca.db')
        c = conn.cursor()
        c.execute("""UPDATE livros SET titulo = :titulo,
                  autor = :autor, genero = :genero,
                  ano = :ano WHERE id = :id""",
                  {'id': self.id, 'titulo': self.titulo,
                   'autor': self.autor, 'genero': self.genero,
                   'ano': self.ano})
        conn.commit()
        conn.close()

    def deletar_livro(self):
        conn = sqlite3.connect('biblioteca.db')
        c = conn.cursor()
        c.execute("DELETE from livros WHERE id = :id",
                  {'id': self.id})
        conn.commit()
        conn.close()
