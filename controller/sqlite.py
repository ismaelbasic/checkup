import sqlite3

conexao = sqlite3.connect('database/data_checkup.db')
sql = conexao.cursor()

while True:
    comando = input('SQL: ')
    if comando != 'sair':
        sql.execute(comando)
        for linha in sql.fetchall():
            print(linha)
    else:
        break
