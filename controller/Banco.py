import sqlite3
from model.Objetos import Objeto

class Banco:
    
    def __init__(self, nome, tabelas = []):
        self.nome = nome
        self.tabelas = tabelas
        self.conexao = sqlite3.connect('database/' + self.nome + '.db')
        self.cursor = self.conexao.cursor()

    def instalar(self):
        
        if len(self.cursor.execute('SELECT * FROM sqlite_master WHERE type="table";').fetchall()) < 1:

            for tabela in self.tabelas:
                codigo = ''

                arquivo = open('database\\presets\\' + tabela + '.txt')
                for linha in arquivo.readlines():
                    codigo += linha

                arquivo.close()

                self.cursor.execute(codigo)
                print('Tabela ' +  tabela + ' criada!')   
            
            self.cursor.execute('insert into funcao(idFuncao, descricao) values(1,"Administrador");')
            self.cursor.execute('insert into funcionario(idFuncionario, cpf, nome, data_nasc, funcao_id) values(1, "000.000.000-01", "Administrador", "2000/01/01", 1);')
            self.cursor.execute('insert into conta(idConta, usuario, senha, funcionario_id) values(1, "admin", "1234", 1);')
    
    def verColuna(self, nome_tabela: str, coluna: str):
        lista = []
        for item_x in self.cursor.execute('select ' + coluna + ' from ' + nome_tabela + ';').fetchall():
            lista.append(item_x[0])
        return lista

    def verObjeto(self, index: int, objeto: Objeto):
        return list(self.cursor.execute('select ' + Objeto.listaEmTexto(True, objeto.colunas) + ' from ' + objeto.nome_tabela + ' where ' + objeto.id_nome + ' = ' + index +';').fetchall()[0])

    def listarPesquisa(self, id_nome, condicao: str, colunas = [], tabelas = []):

        sql = 'select ' + id_nome + ', ' + Objeto.listaEmTexto(True, colunas) + ' from ' + Objeto.listaEmTexto(True, tabelas) + ' ' + condicao + ';'        
        print(sql)
        ids = []
        valores = []
        for linha in self.cursor.execute(sql).fetchall(): 
            aux = []      
            for cont in range(0, len(linha)):
                if cont == 0:
                    ids.append(linha[cont])
                else:
                    aux.append(linha[cont])
            valores.append(aux)
              
        return Objeto.listaEmLista(True, ids), valores

    def verConta(self, usuario, senha):
        if int(self.cursor.execute('select count(*) from conta where usuario = "' + usuario + '" and senha = "' + senha + '";').fetchall()[0][0]) >= 1:
            return True
        else:
            return False