from sqlite3 import Cursor
from PySide2.QtWidgets import QMessageBox

class Objeto:

    def __init__(self, nome_tabela, id_nome, colunas = [], valores = []):
        self.nome_tabela = nome_tabela
        self.id_nome = id_nome
        self.id_valor = 0
        self.colunas = colunas
        self.valores = valores

    def listaEmTexto(ignore: bool, lista = []):
        texto = ''
        tamanho = len(lista)
        for cont in range(0, tamanho):
            if not(ignore):
                if (type(lista[cont]) == int) or (type(lista[cont]) == float):
                    if cont == (tamanho - 1):
                        texto += str(lista[cont])
                    else:
                        texto += str(lista[cont]) + ', '
                else:
                    if cont == (tamanho - 1):
                        texto += str('"' + lista[cont] + '"')
                    else:
                        texto +=  str('"' + lista[cont] + '"') + ', '
            else:
                if cont == (tamanho - 1):
                    texto += lista[cont]
                else:
                    texto += lista[cont] + ', '
        return texto

    def listaEmLista(ignore: bool, lista = []):
        listaAux = []
        tamanho = len(lista)
        for cont in range(0, tamanho):
            if not(ignore):
                if (type(lista[cont]) == int) or (type(lista[cont]) == float):
                    if cont == (tamanho - 1):
                        listaAux.append(str(lista[cont]))
                    else:
                        listaAux.append(str(lista[cont]))
                else:
                    if cont == (tamanho - 1):
                        listaAux.append(str('"' + lista[cont] + '"'))
                    else:
                        listaAux.append(str('"' + lista[cont] + '"'))
            else:
                if cont == (tamanho - 1):
                    listaAux.append(str(lista[cont]))
                else:
                    listaAux.append(str(lista[cont]))
        return listaAux

    def listaEmString(lista):
        laux = []
        for item in lista:
            if (type(item) == int) or (type(item) == float):
                laux.append(str(item))
            else:
                laux.append(item)
        return laux
        
    def add(self, cursor: Cursor, auto_increment: bool):

        if auto_increment:
            self.id_valor = int(cursor.execute('select count(*) from ' + self.nome_tabela + ';').fetchall()[0][0]) + 1

        while True:   
            if len(cursor.execute('select * from ' + self.nome_tabela + ' where ' + self.id_nome + ' = ' + str(self.id_valor) + ';').fetchall()) > 0:
                self.id_valor += 1
            else:
                break          
        
        sql = 'insert into ' + self.nome_tabela + '(' + self.id_nome + ', ' + Objeto.listaEmTexto(True, self.colunas) + ') values(' + str(self.id_valor) + ', ' + Objeto.listaEmTexto(False, self.valores) + ');'
        
        try:
            cursor.execute(sql)
            cursor.connection.commit()
            print(self.nome_tabela + ' adicionado(a)!')

        except:
            self.msg = QMessageBox()
            self.msg.setWindowTitle('Alerta')
            self.msg.setText('Esse item já existe')
            self.msg.show()
            print('Não foi possivel executar a acao: ' + sql)
        
    def set(self, cursor: Cursor):

        juncao = []
        lista = Objeto.listaEmLista(False, self.valores)

        for cont in range(0, len(self.colunas)):
            juncao.append(self.colunas[cont] + ' = ' + lista[cont])

        sql = 'UPDATE ' + self.nome_tabela + ' SET ' + Objeto.listaEmTexto(True, juncao) + ' WHERE ' + self.id_nome + ' = ' + self.id_valor + ';'
       
        try:
            cursor.execute(sql)
            cursor.connection.commit()
            print(self.nome_tabela + ' editado(a)!')
        except:
            print('Não foi possivel executar a acao: ' + sql)

    def remove(self, cursor: Cursor):

        sql = 'DELETE FROM ' + self.nome_tabela + ' WHERE ' + self.id_nome +  ' = ' + str(self.id_valor) + ';'
        
        try:
            cursor.execute(sql)
            cursor.connection.commit()
            print(self.nome_tabela + ' deletado(a)!')
        except:
            print('Não foi possivel executar a acao: ' + sql)

    def getString(self):
        lista = []

        for cont in range(0, len(self.colunas)):
            lista.append(str(self.colunas[cont] + ' = ' + str(self.valores[cont])))
        
        return self.id_valor + '# '+ str.upper(self.nome_tabela) + ': ' + Objeto.listaEmTexto(True, lista)

    def getStatusValor(self):
        if len(self.colunas) == len(self.valores):
            return True
        else:
            return False

    def addValor(self, nova_coluna, valor):
        if self.getStatusValor():
            if not(nova_coluna in self.colunas):
                self.colunas.append(nova_coluna)
                self.valores.append(valor)
            else:
                print('A coluna ' + nova_coluna + ' já exite!')
        else:
            print('Numero de colunas é diferente do numero de valores')

    def getValor(self, coluna: str):
        if self.getStatusValor():
            if coluna in self.colunas:
                return self.valores[self.colunas.index(coluna)]
            else:
                print('A coluna ' + coluna + ' não já exite!')
                return False
        else:
            print('Numero de colunas é diferente do numero de valores')
            return False

    def setValor(self, coluna: str, valor):
        if self.getStatusValor():
            if coluna in self.colunas:
                self.valores[self.colunas.index(coluna)] = valor
            else:
                print('A coluna ' + coluna + ' não já exite!')
        else:
            print('Numero de colunas é diferente do numero de valores')
        
    def delValor(self, coluna: str):
        if self.getStatusValor():
            if coluna in self.colunas:
                self.valores.remove(self.valores[self.colunas.index(coluna)])
                self.colunas.remove(coluna)
            else:
                print('A coluna ' + coluna + ' não já exite!')
            
        else:
            print('Numero de colunas é diferente do numero de valores')

    def setAllValor(self, valores = []):
        if self.getStatusValor():
            self.valores = valores
        else:
            print('Numero de colunas é diferente do numero de valores')

class Hospede(Objeto):
    def __init__(self):
        super().__init__(
            'hospede', 
            'idHospede', 
            ['num_documento', 'nome', 'data_nasc', 'endereco', 'email', 'telefone'], 
            ['', '', '', '', '', '']
        )

class CategoriaQuarto(Objeto):
    def __init__(self):
        super().__init__(
            'categoria_quarto', 
            'idCategoria', 
            ['descricao'], 
            ['']
        )

class Quarto(Objeto):
    def __init__(self) -> None:
        super().__init__(
            'quarto', 
            'idQuarto', 
            ['numero', 'valor', 'categoria_quarto_id'], 
            [0, 0.0, 0]
        )

class Funcao(Objeto):
    
    def __init__(self):
        super().__init__(
            'funcao', 
            'idFuncao', 
            ['descricao'], 
            ['Vazia']
        )

class Funcionario(Objeto):
    
    def __init__(self):
        super().__init__(
            'funcionario', 
            'idFuncionario', 
            ['cpf', 'nome', 'data_nasc', 'funcao_id'], 
            ['', '', '', 0]
        )

class Conta(Objeto):
    
     def __init__(self):
        super().__init__(
            'conta', 
            'idConta', 
            ['usuario', 'senha', 'funcionario_id'], 
            ['', '', 0]
        )

class Reserva(Objeto):
    def __init__(self):
        super().__init__(
            'reserva', 
            'idReserva', 
            ['checkin', 'checkout', 'num_renovacoes', 'total', 'hospede_id', 'quarto_id', 'conta_id'], 
            ['', '', 0, 0.0, 0, 0, 0]
        )

class Convidado(Objeto):
    def __init__(self):
        super().__init__(
            'convidado', 
            'idConvidado', 
            ['reserva_id', 'hospede_id'], 
            [0, 0]
        )

class Servico(Objeto):
    def __init__(self):
        super().__init__(
            'servico', 
            'idServico', 
            ['tipo', 'valor', 'reserva_id', 'funcionario_id'], 
            ['', 0.0, 0, 0]
        )

class Item(Objeto):
    def __init__(self):
        super().__init__(
            'item', 
            'idItem', 
            ['descricao', 'quantidade', 'item_valor', 'frigobar', 'quarto_id'],  
            ['', 0, 0.0, '', 0]
        )

class Multa(Objeto):
    def __init__(self):
        super().__init__(
            'multa', 
            'idMulta', 
            ['multa_inicio', 'multa_fim', 'valor', 'reserva_id'],  
            ['', '', 0.0, 0]
        )

class Consumo(Objeto):
    def __init__(self):
        super().__init__(
            'consumo', 
            'idConsumo', 
            ['reserva_id', 'itens_id'],  
            [0, 0]
        )