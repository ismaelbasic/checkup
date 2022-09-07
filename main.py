import os
import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox

from view.checkup import Ui_Janela
from view.login import Ui_Login
from controller.Banco import Banco

from view.gui import *
from model.Objetos import *

class Login(QWidget, Ui_Login):
    def __init__(self, app, banco: Banco):
        super().__init__()
        self.setFixedSize(700, 700)
        self.setupUi(self)
        self.app = app
        self.banco = banco
        self.campoSenha.setEchoMode(QLineEdit.Password)
        self.btEntrar.clicked.connect(lambda: self.abrirJanela())

    def abrirJanela(self):
        if self.banco.verConta(self.campoUsuario.text(), self.campoSenha.text()):
            self.app.janela = Janela(banco)
            self.app.janela.show()
            self.close()
        else:
            self.msg = QMessageBox()
            self.msg.setWindowTitle('Status')
            self.msg.setText('Login e/ou senha incorreto(a)(s)!!')
            self.msg.show()

class Janela(QMainWindow, Ui_Janela):
    def __init__(self, banco):
        super(Janela, self).__init__()
        self.setupUi(self)
        self.setFixedWidth(850)

        self.banco = banco

        self.paginas.setCurrentWidget(self.pg_inicio)
        self.actionAdministrador.triggered.connect(lambda: self.paginas.setCurrentWidget(self.pg_inicio))

        self.btQuartos.clicked.connect(lambda: self.ativarQuarto())
        self.btReservas.clicked.connect(lambda: self.ativarReserva())
        self.btHospedes.clicked.connect(lambda: self.ativarHospede())
        self.btAdminstracao.clicked.connect(lambda: self.ativarAdministracao())
        self.btFuncionarios.clicked.connect(lambda: self.ativarFuncionario())
        self.pushButton_6.clicked.connect(lambda: self.ativarItem())

        self.configHospede()
        self.configCategoriaQuarto()
        self.configQuarto()
        self.configFuncao()
        self.configFuncionario()
        self.configConta()
        self.configReserva()
        self.configConvidado()
        self.configServico()
        self.configItem()
        self.configMulta()
        self.configConsumo()

    def configHospede(self):
        hospede = Hospede()
        self.tabHospede = Tabela(
            self, 
            self.pg_hospede, 
            self.tabelaHospede,
            hospede,
            Hospede(), '', [], [],
            [
                'Nº DO DOCUMENTO', 'NOME', 'DATA DE NASCIMENTO', 'ENDEREÇO', 'EMAIL', 'TELEFONE'
            ],
            [ 
                self.adicionarHospede,
                self.editarHospede,
                self.deletarHospede,
                self.atualizarHospedes
            ],
            [
                Campo('Nº do Documento:').texto(30, '', ''),
                Campo('Nome Completo:').texto(30, '', ''),
                Campo('Data de Nascimento:').texto(30, '', '0000/00/00;_'),
                Campo('Endereço:').texto(50, '', ''),
                Campo('Email:').texto(50, 'exemplo@email.com', ''),
                Campo('Telefone:').texto(15, '', '(00) 00000-0000;_')
            ]
        )
        self.tabHospede.refresh()
        
        self.actionHospede.triggered.connect(lambda: self.tabHospede.load())

    def configCategoriaQuarto(self):
        categoriaQuarto = CategoriaQuarto()
        self.tabCategoriaQuarto = Tabela(
            self, 
            self.pg_categoriaQuarto, 
            self.tabelaCategoriaQuarto, 
            categoriaQuarto,
            CategoriaQuarto(), '', [], [],
            [
                'Descrição'
            ],
            [ 
                self.adicionarCategoriaQuarto,
                self.editarCategoriaQuarto,
                self.deletarCategoriaQuarto,
                self.atualizarCategoriaQuartos
            ],
            [
                Campo('Descriçao:').texto(30, 'Ex: Simples, Duplo ...', '')
            ]
        )

        self.tabCategoriaQuarto.refresh()
        
        self.actionCategoriasQuartos.triggered.connect(lambda: self.tabCategoriaQuarto.load())

    def configQuarto(self):
        quarto = Quarto()
        quarto.delValor('categoria_quarto_id')
        self.tabQuarto = Tabela(
            self, 
            self.pg_quarto, 
            self.tabelaQuarto, 
            quarto,
            Quarto(), 'where categoria_quarto_id = idCategoria', ['categoria_quarto.descricao'], ['categoria_quarto'],
            [
                'Nº', 'VALOR(R$)', 'CATEGORIA'
            ],
            [ 
                self.adicionarQuarto,
                self.editarQuarto,
                self.deletarQuarto,
                self.atualizarQuartos
            ],
            [
                Campo('Nº do Quarto:').spin(100, 0),
                Campo('Valor(R$):').numeroFloat(5),
                Campo('Categoria:').comboBoxBanco(self.banco, CategoriaQuarto().nome_tabela, 'descricao')
            ]
        )

        self.tabQuarto.refresh()
        
        self.actionProcurarQuartos.triggered.connect(lambda: self.tabQuarto.load())

    def configFuncao(self):
        funcao = Funcao()
        self.tabFuncao = Tabela(
            self, 
            self.pg_funcoes, 
            self.tabelaFuncao, 
            funcao,
            Funcao(), '', [], [],
            [
                'Descrição'
            ],
            [ 
                self.adicionarFuncao,
                self.editarFuncao,
                self.deletarFuncao,
                self.atualizarFuncoes
            ],
            [
                Campo('Descriçao:').texto(30, 'Ex: Gerente', '')
            ]
        )

        self.tabFuncao.refresh()
        
        self.actionFuncoes.triggered.connect(lambda: self.tabFuncao.load())

    def configFuncionario(self):
        funcionario = Funcionario()
        funcionario.delValor('funcao_id')
        self.tabFuncionario = Tabela(
            self, 
            self.pg_funcionario, 
            self.tabelaFuncionario, 
            funcionario,
            Funcionario(), 'where funcao_id = funcao.idFuncao', ['funcao.descricao'], ['funcao'],
            [
                'CPF', 'NOME', 'DATA DE NASCIMENTO', 'FUNÇÃO'
            ],
            [ 
                self.adicionarFuncionario,
                self.editarFuncionario,
                self.deletarFuncionario,
                self.atualizarFuncionarios
            ],
            [
                Campo('CPF:').texto(12, '', '000.000.000-00;_'),
                Campo('Nome:').texto(30, '', ''),
                Campo('Data de Nascimento:').texto(30, '', '0000/00/00;_'),
                Campo('Função:').comboBoxBanco(self.banco, Funcao().nome_tabela, 'descricao')
            ]
        )

        self.tabFuncionario.refresh()

        self.actionProcurarFuncionarios.triggered.connect(lambda: self.tabFuncionario.load())
        
    def configConta(self):
        conta = Conta()
        conta.delValor('funcionario_id')
        self.tabConta = Tabela(
            self, 
            self.pg_conta, 
            self.tabelaConta, 
            conta,
            Conta(), 'where funcionario_id = idFuncionario', ['funcionario.nome'], ['funcionario'],
            [
                'USUARIO', 'SENHA', 'FUNCIONÁRIO'
            ],
            [ 
                self.adicionarConta,
                self.editarConta,
                self.deletarConta,
                self.atualizarContas
            ],
            [
                Campo('Usuario:').texto(30,'',''),
                Campo('Senha:').senha(),
                Campo('Funcionário:').comboBoxBanco(self.banco, Funcionario().nome_tabela, 'nome')
            ]
        )

        self.tabConta.refresh()
        
        self.actionContas.triggered.connect(lambda: self.tabConta.load())
    
    def configReserva(self):
        reserva = Reserva()
        reserva.delValor('hospede_id')
        reserva.delValor('quarto_id')
        reserva.delValor('conta_id')
        self.tabReserva = Tabela(
            self, 
            self.pg_reserva, 
            self.tabelaReserva, 
            reserva,
            Reserva(), 'where hospede_id = hospede.idHospede and quarto_id = quarto.idQuarto and conta_id = conta.idConta', 
            ['hospede.nome', 'quarto.numero ','conta.usuario'], 
            ['hospede', 'quarto', 'conta'],
            [
                'CHECKIN', 'CHECKOUT', 'Nº DE RENOVAÇÕES', 'TOTAL(R$)', 'HOSPEDE PAGANTE', 'Nº DO QUARTO', 'CONTA DO FUNCIONÁRIO'
            ],
            [ 
                self.adicionarReserva,
                self.editarReserva,
                self.deletarReserva,
                self.atualizarReservas
            ],
            [
                Campo('Checkin:').texto(20, '', '0000/00/00 00:00;_'),
                Campo('Checkout:').texto(20, '', '0000/00/00 00:00;_'),
                Campo('Nº de Renovações:').spin(100, 1),
                Campo('Total:').numeroFloat(10),
                Campo('Hospede Pagante:').comboBoxBanco(self.banco, Hospede().nome_tabela, 'nome'),
                Campo('Nº do Quarto:').comboBoxBanco(self.banco, Quarto().nome_tabela, 'numero'),
                Campo('Conta:').comboBoxBanco(self.banco, Conta().nome_tabela, 'usuario')
            ]
        )

        self.tabReserva.refresh()

        self.actionProcurarReserva.triggered.connect(lambda: self.tabReserva.load())

    def configConvidado(self):
        convidado = Convidado()
        convidado.delValor('reserva_id')
        convidado.delValor('hospede_id')
        self.tabConvidado = Tabela(
            self, 
            self.pg_convidado, 
            self.tabelaConvidado, 
            convidado,
            Convidado(), 'where reserva_id = reserva.idReserva and convidado.hospede_id = hospede.idHospede ', ['reserva.idReserva', 'nome'], ['reserva', 'hospede'],
            [
                'CODIGO DA RESERVA', 'HOSPEDE CONVIDADO'
            ],
            [ 
                self.adicionarConvidado,
                self.editarConvidado,
                self.deletarConvidado,
                self.atualizarConvidados
            ],
            [
                Campo('Reserva:').comboBoxBanco(self.banco, Reserva().nome_tabela, 'idReserva'),
                Campo('Hospede:').comboBoxBanco(self.banco, Hospede().nome_tabela, 'nome')
            ]
        )

        self.tabConvidado.refresh()

        self.actionConvidados.triggered.connect(lambda: self.tabConvidado.load())

    def configServico(self):
        servico = Servico()
        servico.delValor('reserva_id')
        servico.delValor('funcionario_id')
        self.tabServico = Tabela(
            self, 
            self.pg_servico, 
            self.tabelaServico, 
            servico,
            Servico(), 'where reserva_id = reserva.idReserva and servico.funcionario_id = funcionario.idFuncionario', ['reserva.idReserva', 'nome'], ['reserva', 'funcionario'],
            [
                'DESCRIÇÃO', 'VALOR(R$)', 'CODIGO DA RESERVA', 'FUNCINÁRIO'
            ],
            [ 
                self.adicionarServico,
                self.editarServico,
                self.deletarServico,
                self.atualizarServicos
            ],
            [
                Campo('Descriçao:').texto(30, 'Lavanderia, estacionamento ...',''),
                Campo('Valor(R$):').numeroFloat(5),
                Campo('Reserva:').comboBoxBanco(self.banco, Reserva().nome_tabela, 'idReserva'),
                Campo('Funcionário Atribuido:').comboBoxBanco(self.banco, Funcionario().nome_tabela, 'nome')
            ]
        )

        self.tabServico.refresh()

        self.actionServicos.triggered.connect(lambda: self.tabServico.load())

    def configItem(self):
        item = Item()
        item.delValor('quarto_id')
        self.tabItem = Tabela(
            self, 
            self.pg_itens, 
            self.tabelaItens, 
            item,
            Item(), 'where item.quarto_id = quarto.idQuarto', 
            ['quarto.numero'], 
            ['quarto'],
            [
                'DESCRIÇAO', 'QUANTIDADE', 'VALOR(R$)', 'FRIGOBAR', 'Nº DO QUARTO'
            ],
            [ 
                self.adicionarItens,
                self.editarItens,
                self.deletarItens,
                self.atualizarItens
            ],
            [
                Campo('Descrição:').texto(20, '', ''),
                Campo('Quantidade:').spin(100, 0),
                Campo('Valor(R$):').numeroFloat(10),
                Campo('Frigobar?:').texto(20, 'sim ou não', ''),
                Campo('Nº do Quarto:').comboBoxBanco(self.banco, Quarto().nome_tabela, 'numero')
            ]
        )

        self.tabItem.refresh()

        self.actionItens.triggered.connect(lambda: self.tabItem.load())

    def configMulta(self):
        multa = Multa()
        multa.delValor('reserva_id')
        self.tabMulta = Tabela(
            self, 
            self.pg_multa, 
            self.tabelaMulta, 
            multa,
            Multa(), 'where multa.reserva_id = reserva.idReserva', 
            ['reserva.idReserva'], 
            ['reserva'],
            [
                'MULTA INICIO', 'MULTA FIM', 'VALOR(R$)', 'Nº DO RESERVA'
            ],
            [ 
                self.adicionarMulta,
                self.editarMulta,
                self.deletarMulta,
                self.atualizarMulta
            ],
            [
                Campo('Multa Inicio:').texto(20, '', '0000/00/00 00:00;_'),
                Campo('Multa Fim:').texto(20, '', '0000/00/00 00:00;_'),
                Campo('Valor(R$):').numeroFloat(10),
                Campo('Reserva:').comboBoxBanco(self.banco, Reserva().nome_tabela, 'idReserva')
            ]
        )

        self.tabMulta.refresh()

        self.actionMultas.triggered.connect(lambda: self.tabMulta.load())

    def configConsumo(self):
        consumo = Consumo()
        consumo.delValor('reserva_id')
        consumo.delValor('itens_id')
        self.tabConsumo = Tabela(
            self, 
            self.pg_consumo, 
            self.tabelaConsumo, 
            consumo,
            Consumo(), 'where consumo.reserva_id = reserva.idReserva and consumo.itens_id = item.idItem', 
            ['reserva.idReserva', 'item.idItem'], 
            ['reserva', 'item'],
            [
                'CODIGO RESERVA', 'CODIGO ITEM'
            ],
            [ 
                self.adicionarConsumo,
                self.editarConsumo,
                self.deletarConsumo,
                self.atualizarConsumos
            ],
            [
                Campo('Reserva:').comboBoxBanco(self.banco, Reserva().nome_tabela, 'idReserva'),
                Campo('Item:').comboBoxBanco(self.banco, Item().nome_tabela, 'idItem')
            ]
        )

        self.tabConsumo.refresh()

        self.actionConsumo.triggered.connect(lambda: self.tabConsumo.load())

    def ativarQuarto(self):
        self.tabQuarto.load()
        self.tabQuarto.refresh()
        self.paginas.setCurrentWidget(self.pg_quarto)

    def ativarReserva(self):
        self.tabReserva.load()
        self.paginas.setCurrentWidget(self.pg_reserva)
        self.tabReserva.refresh()

    def ativarHospede(self):
        self.tabHospede.load()
        self.paginas.setCurrentWidget(self.pg_hospede)
        self.tabHospede.refresh()

    def ativarAdministracao(self):
        self.tabConta.load()
        self.tabConta.refresh()
        self.paginas.setCurrentWidget(self.pg_conta)

    def ativarFuncionario(self):
        self.tabFuncionario.load()
        self.paginas.setCurrentWidget(self.pg_funcionario)
        self.tabFuncionario.refresh()

    def ativarItem(self):
        self.tabItem.load()
        self.paginas.setCurrentWidget(self.pg_itens)
        self.tabItem.refresh()

if __name__ == '__main__':
    #os.system('pip install pyside2')

    banco = Banco(
        'data_checkup', 
        [ 
            'hospede', 'categoria_quarto', 'quarto', 'funcao', 
            'funcionario', 'conta', 'reserva', 'convidado', 
            'servico', 'item', 'multa', 'consumo' 
        ]
    )
    
    banco.instalar()

    app = QApplication(sys.argv)
    login = Login(app, banco)
    login.show()   
    
    app.exec_()