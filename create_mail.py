import mysql.connector

def create_database():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    cursor = con.cursor()

    # Criar o banco de dados se não existir
    database_name = "mailservice"
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    cursor.execute(f"USE {database_name}")

    # Criar tabela se não existir
    cursor.execute('''CREATE TABLE IF NOT EXISTS address
                    (id INT AUTO_INCREMENT PRIMARY KEY,
                    emails VARCHAR(255))''')

    # Inserir alguns emails de exemplo
    emails = ['vinicius.silva405@fatec.sp.gov.br', 'luiz.bedim@fatec.sp.gov.br', 'priscila.raminelli@fatec.sp.gov.br',
              'eva.ananias@fatec.sp.gov.br', 'matheus.bordin01@fatec.sp.gov.br']

    # Inserir emails na tabela
    for email in emails:
        cursor.execute("INSERT INTO address(emails) VALUES (%s)", (email,))

    # Commit e fechar a conexão
    con.commit()
    con.close()

# Criar o banco de dados e inserir dados
create_database()
print("Mail Service was Opened!")