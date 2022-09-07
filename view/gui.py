from sqlite3 import Cursor

from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtWidgets import QLabel, QLineEdit, QSpinBox, QComboBox, QTreeWidget, QTreeWidgetItem
from PySide2.QtWidgets import QPushButton, QVBoxLayout

from view.checkup import Ui_Janela
from controller.Banco import Banco

from model.Objetos import Objeto

class Campo(QLabel, QLineEdit, QComboBox):

    def __init__(self, titulo: str):
        super().__init__()
        self.titulo = titulo
        self.label = QLabel(titulo)
    
    def texto(self, tamanho: int, exemplo: str, mascara: str):
        self.campo = QLineEdit()
        self.tipo = 'texto'
        self.campo.setMaxLength(tamanho)
        self.campo.setPlaceholderText(exemplo)
        self.campo.setInputMask(mascara)

        return self

    def senha(self):
        self.campo = QLineEdit()
        self.campo.setEchoMode(QLineEdit.Password)
        self.tipo = 'texto'
        return self

    def numeroInt(self, tamanho: int):
        self.campo = QLineEdit()
        self.tipo = 'inteiro'
        self.campo.setMaxLength(tamanho)

        return self

    def numeroFloat(self, tamanho: int):
        self.campo = QLineEdit()
        self.tipo = 'float'
        self.campo.setMaxLength(tamanho)

        return self
        
    def comboBoxBanco(self, banco: Banco, nome_tabela: str, coluna: str):
        self.cbbanco = []
        self.cbbanco.append(banco) 
        self.cbbanco.append(nome_tabela)
        self.cbbanco.append(coluna)
        self.campo = QComboBox()
        self.tipo = 'combo'
        self.campo.addItems(self.cbbanco[0].verColuna(self.cbbanco[1], self.cbbanco[2]))
        return self

    def spin(self, max, min):
        self.campo = QSpinBox()
        self.tipo = 'spin'
        self.campo.setMaximum(max)
        self.campo.setMinimum(min)
        return self

    def getValor(self):
        if self.tipo == 'inteiro':
            return int(self.campo.text())
        elif self.tipo == 'float':
            return float(self.campo.text())
        elif self.tipo == 'combo':
            return self.campo.currentIndex() + 1
        elif self.tipo == 'spin':
            return self.campo.value()
        elif self.tipo == 'texto':
            return self.campo.text()
        else:
            return str(self.campo.text())   

    def setValor(self, valor):
        if self.tipo == 'inteiro':
            if not(valor is None):
                self.campo.setText(str(valor))
            else:
                self.campo.setText(str(''))
        elif self.tipo == 'float':
            if not(valor is None):
                self.campo.setText(str(valor))
            else:
                self.campo.setText(str(''))
        elif self.tipo == 'combo':
            if not(valor is None):
                self.cbbanco[0].cursor.connection.commit()
                lista = Objeto.listaEmLista(True, self.cbbanco[0].verColuna(self.cbbanco[1], self.cbbanco[2]))
                
                self.campo.clear()

                self.campo.addItems(lista)
                self.campo.setCurrentIndex(valor - 1)
            else:
                self.cbbanco[0].cursor.connection.commit()
                lista = Objeto.listaEmLista(True, self.cbbanco[0].verColuna(self.cbbanco[1], self.cbbanco[2]))
                
                self.campo.clear()

                self.campo.addItems(lista)
                        
        elif self.tipo == 'spin':
            if not(valor is None):
                self.campo.setValue(int(valor))
            else:
                self.campo.setValue(0)
        elif self.tipo == 'texto':
            if not(valor is None):
                self.campo.setText(str(valor))
            else:
                self.campo.setText(str(''))
        else:
            if not(valor is None):
                self.campo.setText(str(valor))
            else:
                self.campo.setText(str(''))

class Cadastro(QWidget):
    def __init__(self, titulo, banco: Banco, atualizar, simples: Objeto, campos: Campo = []):
        super().__init__()
        self.setWindowTitle('Cadastro de ' + titulo)
        self.setFixedWidth(500)
        self.banco = banco
        self.simples = simples
        self.campos = campos
        self.atualizar = atualizar
        
        layouCadastro = QVBoxLayout()
        for campo in self.campos:
            layouCadastro.addWidget(campo.label)
            layouCadastro.addWidget(campo.campo)
            campo.setValor(None)              

        botao = QPushButton('Cadastrar')
        botao.clicked.connect(lambda: self.cadastrar())
        layouCadastro.addWidget(botao)

        self.setLayout(layouCadastro)

    def cadastrar(self):

        if len(self.simples.valores) == len(self.campos):
            for cont in range(0, len(self.simples.valores)):
                self.simples.valores[cont] = self.campos[cont].getValor()
                self.campos[cont].setValor(None)
                
        print(self.simples.valores)
        self.simples.add(self.banco.cursor, True)
        self.atualizar()
        self.close()

class Editar(QWidget):
    def __init__(self, titulo, banco: Banco, index: int, atualizar, simples: Objeto, campos: Campo = []):
        super().__init__()
        self.setWindowTitle('Editar de ' + titulo)
        self.setFixedWidth(500)
        self.banco = banco
        self.simples = simples
        self.campos = campos
        self.atualizar = atualizar
        
        layouEditar = QVBoxLayout()

        self.simples.id_valor = index
        self.simples.valores = banco.verObjeto(index, simples)

        for cont in range(0, len(self.simples.valores)):
            self.campos[cont].setValor(self.simples.valores[cont])  

        for campo in self.campos:
            layouEditar.addWidget(campo.label)
            layouEditar.addWidget(campo.campo)      

        botao = QPushButton('Editar')
        botao.clicked.connect(lambda: self.editar())
        layouEditar.addWidget(botao)

        self.setLayout(layouEditar)

    def editar(self):
        
        if len(self.simples.valores) == len(self.campos):
            for cont in range(0, len(self.simples.valores)):
                self.simples.valores[cont] = self.campos[cont].getValor()
                print(self.campos[cont].getValor())
                self.campos[cont].setValor(None)

        self.simples.set(self.banco.cursor)
        self.atualizar()
        self.close()

class Tabela:

    def __init__(self, janela: Ui_Janela, pagina: QWidget, tabela: QTreeWidget, objetoPesquisa: Objeto, simples: Objeto, condicao: str, colunasExternas = [], tabelasExternas = [], titulos = [], metodos: QPushButton = [], campos: Campo = []):
        self.janela = janela
        self.pagina = pagina
        self.tabela = tabela
        self.objetoPesquisa = objetoPesquisa
        self.colunasExternas= colunasExternas
        self.tabelasExternas= tabelasExternas
        self.simples = simples
        self.condicao = condicao
        self.exemplo = simples
        self.titulos = titulos
        self.metodos = metodos
        self.campos = campos
        self.ativoCadastro = False
        self.ativoEdita = False
        
        for campo in self.campos:
            campo.setValor(None)

        self.colunas = (self.objetoPesquisa.colunas + self.colunasExternas)
        self.tabelas = self.tabelasExternas
        self.tabelas.insert(0, self.objetoPesquisa.nome_tabela)

        self.cadastro = QWidget()
        self.editar = QWidget()

    def load(self):
        self.tabela.setColumnCount(len(self.titulos))
        self.tabela.setHeaderLabels(self.titulos)

        self.janela.paginas.setCurrentWidget(self.pagina)
        self.metodos[0].clicked.connect(lambda: self.addItem())
        self.metodos[1].clicked.connect(lambda: self.setItem())
        self.metodos[2].clicked.connect(lambda: self.delItem())
        self.metodos[3].clicked.connect(lambda: self.refresh())
    
    def refresh(self):
        self.tabela.clear()
        
        self.indexs, self.saidas = self.janela.banco.listarPesquisa(self.simples.id_nome, self.condicao, self.colunas,  self.tabelas)
        
        print(str.upper(self.simples.nome_tabela) + ': ')
        
        for item in self.saidas:
            print(item)
            QTreeWidgetItem(self.tabela, Objeto.listaEmString(item))

        self.janela.banco.cursor.connection.commit()

    def addItem(self):
        
        if not(self.cadastro.isVisible()) and not(self.editar.isVisible()):
            for campo in self.campos:
                campo.setValor(None)
            self.cadastro = Cadastro(self.simples.nome_tabela, self.janela.banco, self.refresh, self.simples, self.campos)
            self.cadastro.show()
        

    def setItem(self):
        if not(self.editar.isVisible()) and not(self.cadastro.isVisible()):
            id = self.tabela.currentIndex().row()
            if id != -1:
                self.editar = Editar(self.simples.nome_tabela, self.janela.banco, self.indexs[id], self.refresh, self.simples, self.campos)
                self.editar.show()
            else:
                self.msg = QMessageBox()
                self.msg.setWindowTitle('Alerta')
                self.msg.setText('selecione um item')
                self.msg.show()

    def delItem(self):
        id = self.tabela.currentIndex().row()
        
        if id != -1:
            self.simples.id_valor = self.indexs[id]
            self.simples.remove(self.janela.banco.cursor)
            self.refresh()
        else:
            print('selecione um item')
