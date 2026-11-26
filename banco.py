import mysql.connector
import pandas as pandas

# Construir a conexão com o servidor MySQL
def conectar():
        conexao = mysql.connector.connect(
            host='localhost', # onde está mysql
            user='app_hortifruti', # user do app
            password='App@Horti2026', # senha do app
            database='hortifruti' # banco de dados do app
        )
        return conexao

def cadastrar(nome, categoria, preco):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
                "INSERT INTO produto(nome, categoria, preco) values (%s, %s, %s)",
                (nome, categoria, preco)
        )
        conexao.commit()
        cursor.close() 
        conexao.close()