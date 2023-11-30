
import streamlit as st
from livro import Livro

# Título da página
st.title("Biblioteca")

# Menu de opções
menu = ["Adicionar livro", "Visualizar livros", "Atualizar livro", "Deletar livro"]
choice = st.sidebar.selectbox("Selecione uma opção", menu)

if choice == "Adicionar livro":
    # Formulário para adicionar livro
    st.subheader("Adicionar livro")
    id = st.number_input("ID")
    titulo = st.text_input("Título")
    autor = st.text_input("Autor")
    genero = st.text_input("Gênero")
    ano = st.number_input("Ano", min_value=0, max_value=9999)

    if st.button("Adicionar"):
        # Crie uma instância da classe Livro e adicione ao banco de dados
        livro = Livro(id, titulo, autor, genero, ano)
        livro.adicionar_livro()
        st.success(f"Livro '{titulo}' adicionado com sucesso!")

elif choice == "Visualizar livros":
    # Visualizar todos os livros
    st.subheader("Visualizar livros")
    livros = Livro.visualizar_todos_livros()
    for livro in livros:
        st.write(livro)

elif choice == "Atualizar livro":
    # Formulário para atualizar livro
    st.subheader("Atualizar livro")
    id = st.number_input("ID do livro a ser atualizado")
    titulo = st.text_input("Novo título")
    autor = st.text_input("Novo autor")
    genero = st.text_input("Novo gênero")
    ano = st.number_input("Novo ano", min_value=0, max_value=9999)

    if st.button("Atualizar"):
        # Crie uma instância da classe Livro e atualize no banco de dados
        livro = Livro(id, titulo, autor, genero, ano)
        livro.atualizar_livro()
        st.success(f"Livro com ID '{id}' atualizado com sucesso!")

elif choice == "Deletar livro":
    # Formulário para deletar livro
    st.subheader("Deletar livro")
    id = st.number_input("ID do livro a ser deletado")

    if st.button("Deletar"):
        # Crie uma instância da classe Livro e delete do banco de dados
        livro = Livro(id, None, None, None, None)
        livro.deletar_livro()
        st.success(f"Livro com ID '{id}' deletado com sucesso!")
