# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'checkup.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Janela(object):
    def setupUi(self, Janela):
        if not Janela.objectName():
            Janela.setObjectName(u"Janela")
        Janela.resize(817, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Janela.sizePolicy().hasHeightForWidth())
        Janela.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"config/img/icone.png", QSize(), QIcon.Normal, QIcon.Off)
        Janela.setWindowIcon(icon)
        self.actionProcurar = QAction(Janela)
        self.actionProcurar.setObjectName(u"actionProcurar")
        self.actionCategorias = QAction(Janela)
        self.actionCategorias.setObjectName(u"actionCategorias")
        self.actionProcurar_2 = QAction(Janela)
        self.actionProcurar_2.setObjectName(u"actionProcurar_2")
        self.actionCategorias_2 = QAction(Janela)
        self.actionCategorias_2.setObjectName(u"actionCategorias_2")
        self.actionProcurarReserva = QAction(Janela)
        self.actionProcurarReserva.setObjectName(u"actionProcurarReserva")
        self.actionServicos = QAction(Janela)
        self.actionServicos.setObjectName(u"actionServicos")
        self.actionMultas = QAction(Janela)
        self.actionMultas.setObjectName(u"actionMultas")
        self.actionHospede = QAction(Janela)
        self.actionHospede.setObjectName(u"actionHospede")
        self.actionConsumo = QAction(Janela)
        self.actionConsumo.setObjectName(u"actionConsumo")
        self.actionNfe = QAction(Janela)
        self.actionNfe.setObjectName(u"actionNfe")
        self.actionProcurarQuartos = QAction(Janela)
        self.actionProcurarQuartos.setObjectName(u"actionProcurarQuartos")
        self.actionCategoriasQuartos = QAction(Janela)
        self.actionCategoriasQuartos.setObjectName(u"actionCategoriasQuartos")
        self.actionItens = QAction(Janela)
        self.actionItens.setObjectName(u"actionItens")
        self.actionProcurarFuncionarios = QAction(Janela)
        self.actionProcurarFuncionarios.setObjectName(u"actionProcurarFuncionarios")
        self.actionFuncoes = QAction(Janela)
        self.actionFuncoes.setObjectName(u"actionFuncoes")
        self.actionAdministrador = QAction(Janela)
        self.actionAdministrador.setObjectName(u"actionAdministrador")
        self.actionContas = QAction(Janela)
        self.actionContas.setObjectName(u"actionContas")
        self.actionInfo = QAction(Janela)
        self.actionInfo.setObjectName(u"actionInfo")
        self.actionDefinicoes = QAction(Janela)
        self.actionDefinicoes.setObjectName(u"actionDefinicoes")
        self.actionContato = QAction(Janela)
        self.actionContato.setObjectName(u"actionContato")
        self.actionConvidados = QAction(Janela)
        self.actionConvidados.setObjectName(u"actionConvidados")
        self.centralwidget = QWidget(Janela)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.paginas = QStackedWidget(self.centralwidget)
        self.paginas.setObjectName(u"paginas")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.paginas.sizePolicy().hasHeightForWidth())
        self.paginas.setSizePolicy(sizePolicy1)
        self.pg_reserva = QWidget()
        self.pg_reserva.setObjectName(u"pg_reserva")
        self.verticalLayout_3 = QVBoxLayout(self.pg_reserva)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.vl_titulo = QVBoxLayout()
        self.vl_titulo.setObjectName(u"vl_titulo")
        self.labelTitulo = QLabel(self.pg_reserva)
        self.labelTitulo.setObjectName(u"labelTitulo")
        font = QFont()
        font.setFamily(u"Bebas Neue")
        font.setPointSize(26)
        self.labelTitulo.setFont(font)

        self.vl_titulo.addWidget(self.labelTitulo)

        self.line = QFrame(self.pg_reserva)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.vl_titulo.addWidget(self.line)


        self.verticalLayout_3.addLayout(self.vl_titulo)

        self.tabelaReserva = QTreeWidget(self.pg_reserva)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.tabelaReserva.setHeaderItem(__qtreewidgetitem)
        self.tabelaReserva.setObjectName(u"tabelaReserva")

        self.verticalLayout_3.addWidget(self.tabelaReserva)

        self.hl_botoes = QHBoxLayout()
        self.hl_botoes.setObjectName(u"hl_botoes")
        self.adicionarReserva = QPushButton(self.pg_reserva)
        self.adicionarReserva.setObjectName(u"adicionarReserva")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.adicionarReserva.sizePolicy().hasHeightForWidth())
        self.adicionarReserva.setSizePolicy(sizePolicy2)
        self.adicionarReserva.setMinimumSize(QSize(80, 0))
        font1 = QFont()
        font1.setFamily(u"Bebas Neue")
        font1.setPointSize(16)
        self.adicionarReserva.setFont(font1)
        self.adicionarReserva.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);\n"
"border-color: transparent;")

        self.hl_botoes.addWidget(self.adicionarReserva)

        self.editarReserva = QPushButton(self.pg_reserva)
        self.editarReserva.setObjectName(u"editarReserva")
        sizePolicy2.setHeightForWidth(self.editarReserva.sizePolicy().hasHeightForWidth())
        self.editarReserva.setSizePolicy(sizePolicy2)
        self.editarReserva.setMinimumSize(QSize(80, 0))
        self.editarReserva.setFont(font1)
        self.editarReserva.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 217, 0);\n"
"border-color: transparent;")

        self.hl_botoes.addWidget(self.editarReserva)

        self.deletarReserva = QPushButton(self.pg_reserva)
        self.deletarReserva.setObjectName(u"deletarReserva")
        sizePolicy2.setHeightForWidth(self.deletarReserva.sizePolicy().hasHeightForWidth())
        self.deletarReserva.setSizePolicy(sizePolicy2)
        self.deletarReserva.setMinimumSize(QSize(80, 0))
        self.deletarReserva.setFont(font1)
        self.deletarReserva.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-color: transparent;")
        self.deletarReserva.setFlat(False)

        self.hl_botoes.addWidget(self.deletarReserva)

        self.espH = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_botoes.addItem(self.espH)

        self.atualizarReservas = QPushButton(self.pg_reserva)
        self.atualizarReservas.setObjectName(u"atualizarReservas")
        sizePolicy2.setHeightForWidth(self.atualizarReservas.sizePolicy().hasHeightForWidth())
        self.atualizarReservas.setSizePolicy(sizePolicy2)
        self.atualizarReservas.setMinimumSize(QSize(80, 0))
        self.atualizarReservas.setFont(font1)
        self.atualizarReservas.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-color: transparent;")

        self.hl_botoes.addWidget(self.atualizarReservas)


        self.verticalLayout_3.addLayout(self.hl_botoes)

        self.paginas.addWidget(self.pg_reserva)
        self.pg_funcoes = QWidget()
        self.pg_funcoes.setObjectName(u"pg_funcoes")
        self.verticalLayout_2 = QVBoxLayout(self.pg_funcoes)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.vl_titulo_3 = QVBoxLayout()
        self.vl_titulo_3.setObjectName(u"vl_titulo_3")
        self.labelTitulo_3 = QLabel(self.pg_funcoes)
        self.labelTitulo_3.setObjectName(u"labelTitulo_3")
        self.labelTitulo_3.setFont(font)

        self.vl_titulo_3.addWidget(self.labelTitulo_3)

        self.line_3 = QFrame(self.pg_funcoes)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.vl_titulo_3.addWidget(self.line_3)


        self.verticalLayout_2.addLayout(self.vl_titulo_3)

        self.tabelaFuncao = QTreeWidget(self.pg_funcoes)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.tabelaFuncao.setHeaderItem(__qtreewidgetitem1)
        self.tabelaFuncao.setObjectName(u"tabelaFuncao")

        self.verticalLayout_2.addWidget(self.tabelaFuncao)

        self.hl_botoes_2 = QHBoxLayout()
        self.hl_botoes_2.setObjectName(u"hl_botoes_2")
        self.adicionarFuncao = QPushButton(self.pg_funcoes)
        self.adicionarFuncao.setObjectName(u"adicionarFuncao")
        sizePolicy2.setHeightForWidth(self.adicionarFuncao.sizePolicy().hasHeightForWidth())
        self.adicionarFuncao.setSizePolicy(sizePolicy2)
        self.adicionarFuncao.setMinimumSize(QSize(80, 0))
        self.adicionarFuncao.setFont(font1)
        self.adicionarFuncao.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);\n"
"border-color: transparent;")

        self.hl_botoes_2.addWidget(self.adicionarFuncao)

        self.editarFuncao = QPushButton(self.pg_funcoes)
        self.editarFuncao.setObjectName(u"editarFuncao")
        sizePolicy2.setHeightForWidth(self.editarFuncao.sizePolicy().hasHeightForWidth())
        self.editarFuncao.setSizePolicy(sizePolicy2)
        self.editarFuncao.setMinimumSize(QSize(80, 0))
        self.editarFuncao.setFont(font1)
        self.editarFuncao.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 217, 0);\n"
"border-color: transparent;")

        self.hl_botoes_2.addWidget(self.editarFuncao)

        self.deletarFuncao = QPushButton(self.pg_funcoes)
        self.deletarFuncao.setObjectName(u"deletarFuncao")
        sizePolicy2.setHeightForWidth(self.deletarFuncao.sizePolicy().hasHeightForWidth())
        self.deletarFuncao.setSizePolicy(sizePolicy2)
        self.deletarFuncao.setMinimumSize(QSize(80, 0))
        self.deletarFuncao.setFont(font1)
        self.deletarFuncao.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-color: transparent;")
        self.deletarFuncao.setFlat(False)

        self.hl_botoes_2.addWidget(self.deletarFuncao)

        self.espH_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_botoes_2.addItem(self.espH_2)

        self.atualizarFuncoes = QPushButton(self.pg_funcoes)
        self.atualizarFuncoes.setObjectName(u"atualizarFuncoes")
        sizePolicy2.setHeightForWidth(self.atualizarFuncoes.sizePolicy().hasHeightForWidth())
        self.atualizarFuncoes.setSizePolicy(sizePolicy2)
        self.atualizarFuncoes.setMinimumSize(QSize(80, 0))
        self.atualizarFuncoes.setFont(font1)
        self.atualizarFuncoes.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-color: transparent;")

        self.hl_botoes_2.addWidget(self.atualizarFuncoes)


        self.verticalLayout_2.addLayout(self.hl_botoes_2)

        self.paginas.addWidget(self.pg_funcoes)
        self.pg_hospede = QWidget()
        self.pg_hospede.setObjectName(u"pg_hospede")
        self.verticalLayout_4 = QVBoxLayout(self.pg_hospede)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.vl_titulo_4 = QVBoxLayout()
        self.vl_titulo_4.setObjectName(u"vl_titulo_4")
        self.labelTitulo_4 = QLabel(self.pg_hospede)
        self.labelTitulo_4.setObjectName(u"labelTitulo_4")
        self.labelTitulo_4.setFont(font)

        self.vl_titulo_4.addWidget(self.labelTitulo_4)

        self.line_4 = QFrame(self.pg_hospede)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.vl_titulo_4.addWidget(self.line_4)


        self.verticalLayout_4.addLayout(self.vl_titulo_4)

        self.tabelaHospede = QTreeWidget(self.pg_hospede)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setText(0, u"1");
        self.tabelaHospede.setHeaderItem(__qtreewidgetitem2)
        self.tabelaHospede.setObjectName(u"tabelaHospede")

        self.verticalLayout_4.addWidget(self.tabelaHospede)

        self.hl_botoes_3 = QHBoxLayout()
        self.hl_botoes_3.setObjectName(u"hl_botoes_3")
        self.adicionarHospede = QPushButton(self.pg_hospede)
        self.adicionarHospede.setObjectName(u"adicionarHospede")
        sizePolicy2.setHeightForWidth(self.adicionarHospede.sizePolicy().hasHeightForWidth())
        self.adicionarHospede.setSizePolicy(sizePolicy2)
        self.adicionarHospede.setMinimumSize(QSize(80, 0))
        self.adicionarHospede.setFont(font1)
        self.adicionarHospede.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);\n"
"border-color: transparent;")

        self.hl_botoes_3.addWidget(self.adicionarHospede)

        self.editarHospede = QPushButton(self.pg_hospede)
        self.editarHospede.setObjectName(u"editarHospede")
        sizePolicy2.setHeightForWidth(self.editarHospede.sizePolicy().hasHeightForWidth())
        self.editarHospede.setSizePolicy(sizePolicy2)
        self.editarHospede.setMinimumSize(QSize(80, 0))
        self.editarHospede.setFont(font1)
        self.editarHospede.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 217, 0);\n"
"border-color: transparent;")

        self.hl_botoes_3.addWidget(self.editarHospede)

        self.deletarHospede = QPushButton(self.pg_hospede)
        self.deletarHospede.setObjectName(u"deletarHospede")
        sizePolicy2.setHeightForWidth(self.deletarHospede.sizePolicy().hasHeightForWidth())
        self.deletarHospede.setSizePolicy(sizePolicy2)
        self.deletarHospede.setMinimumSize(QSize(80, 0))
        self.deletarHospede.setFont(font1)
        self.deletarHospede.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-color: transparent;")
        self.deletarHospede.setFlat(False)

        self.hl_botoes_3.addWidget(self.deletarHospede)

        self.espH_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_botoes_3.addItem(self.espH_3)

        self.atualizarHospedes = QPushButton(self.pg_hospede)
        self.atualizarHospedes.setObjectName(u"atualizarHospedes")
        sizePolicy2.setHeightForWidth(self.atualizarHospedes.sizePolicy().hasHeightForWidth())
        self.atualizarHospedes.setSizePolicy(sizePolicy2)
        self.atualizarHospedes.setMinimumSize(QSize(80, 0))
        self.atualizarHospedes.setFont(font1)
        self.atualizarHospedes.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-color: transparent;")

        self.hl_botoes_3.addWidget(self.atualizarHospedes)


        self.verticalLayout_4.addLayout(self.hl_botoes_3)

        self.paginas.addWidget(self.pg_hospede)
        self.pg_categoriaQuarto = QWidget()
        self.pg_categoriaQuarto.setObjectName(u"pg_categoriaQuarto")
        self.verticalLayout_5 = QVBoxLayout(self.pg_categoriaQuarto)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.vl_titulo_5 = QVBoxLayout()
        self.vl_titulo_5.setObjectName(u"vl_titulo_5")
        self.labelTitulo_5 = QLabel(self.pg_categoriaQuarto)
        self.labelTitulo_5.setObjectName(u"labelTitulo_5")
        self.labelTitulo_5.setFont(font)

        self.vl_titulo_5.addWidget(self.labelTitulo_5)

        self.line_5 = QFrame(self.pg_categoriaQuarto)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.vl_titulo_5.addWidget(self.line_5)


        self.verticalLayout_5.addLayout(self.vl_titulo_5)

        self.tabelaCategoriaQuarto = QTreeWidget(self.pg_categoriaQuarto)
        __qtreewidgetitem3 = QTreeWidgetItem()
        __qtreewidgetitem3.setText(0, u"1");
        self.tabelaCategoriaQuarto.setHeaderItem(__qtreewidgetitem3)
        self.tabelaCategoriaQuarto.setObjectName(u"tabelaCategoriaQuarto")

        self.verticalLayout_5.addWidget(self.tabelaCategoriaQuarto)

        self.hl_botoes_4 = QHBoxLayout()
        self.hl_botoes_4.setObjectName(u"hl_botoes_4")
        self.adicionarCategoriaQuarto = QPushButton(self.pg_categoriaQuarto)
        self.adicionarCategoriaQuarto.setObjectName(u"adicionarCategoriaQuarto")
        sizePolicy2.setHeightForWidth(self.adicionarCategoriaQuarto.sizePolicy().hasHeightForWidth())
        self.adicionarCategoriaQuarto.setSizePolicy(sizePolicy2)
        self.adicionarCategoriaQuarto.setMinimumSize(QSize(80, 0))
        self.adicionarCategoriaQuarto.setFont(font1)
        self.adicionarCategoriaQuarto.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);\n"
"border-color: transparent;")

        self.hl_botoes_4.addWidget(self.adicionarCategoriaQuarto)

        self.editarCategoriaQuarto = QPushButton(self.pg_categoriaQuarto)
        self.editarCategoriaQuarto.setObjectName(u"editarCategoriaQuarto")
        sizePolicy2.setHeightForWidth(self.editarCategoriaQuarto.sizePolicy().hasHeightForWidth())
        self.editarCategoriaQuarto.setSizePolicy(sizePolicy2)
        self.editarCategoriaQuarto.setMinimumSize(QSize(80, 0))
        self.editarCategoriaQuarto.setFont(font1)
        self.editarCategoriaQuarto.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 217, 0);\n"
"border-color: transparent;")

        self.hl_botoes_4.addWidget(self.editarCategoriaQuarto)

        self.deletarCategoriaQuarto = QPushButton(self.pg_categoriaQuarto)
        self.deletarCategoriaQuarto.setObjectName(u"deletarCategoriaQuarto")
        sizePolicy2.setHeightForWidth(self.deletarCategoriaQuarto.sizePolicy().hasHeightForWidth())
        self.deletarCategoriaQuarto.setSizePolicy(sizePolicy2)
        self.deletarCategoriaQuarto.setMinimumSize(QSize(80, 0))
        self.deletarCategoriaQuarto.setFont(font1)
        self.deletarCategoriaQuarto.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-color: transparent;")
        self.deletarCategoriaQuarto.setFlat(False)

        self.hl_botoes_4.addWidget(self.deletarCategoriaQuarto)

        self.espH_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_botoes_4.addItem(self.espH_4)

        self.atualizarCategoriaQuartos = QPushButton(self.pg_categoriaQuarto)
        self.atualizarCategoriaQuartos.setObjectName(u"atualizarCategoriaQuartos")
        sizePolicy2.setHeightForWidth(self.atualizarCategoriaQuartos.sizePolicy().hasHeightForWidth())
        self.atualizarCategoriaQuartos.setSizePolicy(sizePolicy2)
        self.atualizarCategoriaQuartos.setMinimumSize(QSize(80, 0))
        self.atualizarCategoriaQuartos.setFont(font1)
        self.atualizarCategoriaQuartos.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-color: transparent;")

        self.hl_botoes_4.addWidget(self.atualizarCategoriaQuartos)


        self.verticalLayout_5.addLayout(self.hl_botoes_4)

        self.paginas.addWidget(self.pg_categoriaQuarto)
        self.pg_quarto = QWidget()
        self.pg_quarto.setObjectName(u"pg_quarto")
        self.verticalLayout_6 = QVBoxLayout(self.pg_quarto)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.vl_titulo_6 = QVBoxLayout()
        self.vl_titulo_6.setObjectName(u"vl_titulo_6")
        self.labelTitulo_6 = QLabel(self.pg_quarto)
        self.labelTitulo_6.setObjectName(u"labelTitulo_6")
        self.labelTitulo_6.setFont(font)

        self.vl_titulo_6.addWidget(self.labelTitulo_6)

        self.line_6 = QFrame(self.pg_quarto)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.vl_titulo_6.addWidget(self.line_6)


        self.verticalLayout_6.addLayout(self.vl_titulo_6)

        self.tabelaQuarto = QTreeWidget(self.pg_quarto)
        __qtreewidgetitem4 = QTreeWidgetItem()
        __qtreewidgetitem4.setText(0, u"1");
        self.tabelaQuarto.setHeaderItem(__qtreewidgetitem4)
        self.tabelaQuarto.setObjectName(u"tabelaQuarto")
        self.tabelaQuarto.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_6.addWidget(self.tabelaQuarto)

        self.hl_botoes_5 = QHBoxLayout()
        self.hl_botoes_5.setObjectName(u"hl_botoes_5")
        self.adicionarQuarto = QPushButton(self.pg_quarto)
        self.adicionarQuarto.setObjectName(u"adicionarQuarto")
        sizePolicy2.setHeightForWidth(self.adicionarQuarto.sizePolicy().hasHeightForWidth())
        self.adicionarQuarto.setSizePolicy(sizePolicy2)
        self.adicionarQuarto.setMinimumSize(QSize(80, 0))
        self.adicionarQuarto.setFont(font1)
        self.adicionarQuarto.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);\n"
"border-color: transparent;")

        self.hl_botoes_5.addWidget(self.adicionarQuarto)

        self.editarQuarto = QPushButton(self.pg_quarto)
        self.editarQuarto.setObjectName(u"editarQuarto")
        sizePolicy2.setHeightForWidth(self.editarQuarto.sizePolicy().hasHeightForWidth())
        self.editarQuarto.setSizePolicy(sizePolicy2)
        self.editarQuarto.setMinimumSize(QSize(80, 0))
        self.editarQuarto.setFont(font1)
        self.editarQuarto.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 217, 0);\n"
"border-color: transparent;")

        self.hl_botoes_5.addWidget(self.editarQuarto)

        self.deletarQuarto = QPushButton(self.pg_quarto)
        self.deletarQuarto.setObjectName(u"deletarQuarto")
        sizePolicy2.setHeightForWidth(self.deletarQuarto.sizePolicy().hasHeightForWidth())
        self.deletarQuarto.setSizePolicy(sizePolicy2)
        self.deletarQuarto.setMinimumSize(QSize(80, 0))
        self.deletarQuarto.setFont(font1)
        self.deletarQuarto.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-color: transparent;")
        self.deletarQuarto.setFlat(False)

        self.hl_botoes_5.addWidget(self.deletarQuarto)

        self.espH_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_botoes_5.addItem(self.espH_5)

        self.atualizarQuartos = QPushButton(self.pg_quarto)
        self.atualizarQuartos.setObjectName(u"atualizarQuartos")
        sizePolicy2.setHeightForWidth(self.atualizarQuartos.sizePolicy().hasHeightForWidth())
        self.atualizarQuartos.setSizePolicy(sizePolicy2)
        self.atualizarQuartos.setMinimumSize(QSize(80, 0))
        self.atualizarQuartos.setFont(font1)
        self.atualizarQuartos.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-color: transparent;")

        self.hl_botoes_5.addWidget(self.atualizarQuartos)


        self.verticalLayout_6.addLayout(self.hl_botoes_5)

        self.paginas.addWidget(self.pg_quarto)
        self.pg_funcionario = QWidget()
        self.pg_funcionario.setObjectName(u"pg_funcionario")
        self.verticalLayout_12 = QVBoxLayout(self.pg_funcionario)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.vl_titulo_12 = QVBoxLayout()
        self.vl_titulo_12.setObjectName(u"vl_titulo_12")
        self.labelTitulo_12 = QLabel(self.pg_funcionario)
        self.labelTitulo_12.setObjectName(u"labelTitulo_12")
        self.labelTitulo_12.setFont(font)

        self.vl_titulo_12.addWidget(self.labelTitulo_12)

        self.line_12 = QFrame(self.pg_funcionario)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.vl_titulo_12.addWidget(self.line_12)


        self.verticalLayout_12.addLayout(self.vl_titulo_12)

        self.tabelaFuncionario = QTreeWidget(self.pg_funcionario)
        __qtreewidgetitem5 = QTreeWidgetItem()
        __qtreewidgetitem5.setText(0, u"1");
        self.tabelaFuncionario.setHeaderItem(__qtreewidgetitem5)
        self.tabelaFuncionario.setObjectName(u"tabelaFuncionario")
        self.tabelaFuncionario.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_12.addWidget(self.tabelaFuncionario)

        self.hl_botoes_11 = QHBoxLayout()
        self.hl_botoes_11.setObjectName(u"hl_botoes_11")
        self.adicionarFuncionario = QPushButton(self.pg_funcionario)
        self.adicionarFuncionario.setObjectName(u"adicionarFuncionario")
        sizePolicy2.setHeightForWidth(self.adicionarFuncionario.sizePolicy().hasHeightForWidth())
        self.adicionarFuncionario.setSizePolicy(sizePolicy2)
        self.adicionarFuncionario.setMinimumSize(QSize(80, 0))
        self.adicionarFuncionario.setFont(font1)
        self.adicionarFuncionario.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);\n"
"border-color: transparent;")

        self.hl_botoes_11.addWidget(self.adicionarFuncionario)

        self.editarFuncionario = QPushButton(self.pg_funcionario)
        self.editarFuncionario.setObjectName(u"editarFuncionario")
        sizePolicy2.setHeightForWidth(self.editarFuncionario.sizePolicy().hasHeightForWidth())
        self.editarFuncionario.setSizePolicy(sizePolicy2)
        self.editarFuncionario.setMinimumSize(QSize(80, 0))
        self.editarFuncionario.setFont(font1)
        self.editarFuncionario.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 217, 0);\n"
"border-color: transparent;")

        self.hl_botoes_11.addWidget(self.editarFuncionario)

        self.deletarFuncionario = QPushButton(self.pg_funcionario)
        self.deletarFuncionario.setObjectName(u"deletarFuncionario")
        sizePolicy2.setHeightForWidth(self.deletarFuncionario.sizePolicy().hasHeightForWidth())
        self.deletarFuncionario.setSizePolicy(sizePolicy2)
        self.deletarFuncionario.setMinimumSize(QSize(80, 0))
        self.deletarFuncionario.setFont(font1)
        self.deletarFuncionario.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-color: transparent;")
        self.deletarFuncionario.setFlat(False)

        self.hl_botoes_11.addWidget(self.deletarFuncionario)

        self.espH_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_botoes_11.addItem(self.espH_11)

        self.atualizarFuncionarios = QPushButton(self.pg_funcionario)
        self.atualizarFuncionarios.setObjectName(u"atualizarFuncionarios")
        sizePolicy2.setHeightForWidth(self.atualizarFuncionarios.sizePolicy().hasHeightForWidth())
        self.atualizarFuncionarios.setSizePolicy(sizePolicy2)
        self.atualizarFuncionarios.setMinimumSize(QSize(80, 0))
        self.atualizarFuncionarios.setFont(font1)
        self.atualizarFuncionarios.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-color: transparent;")

        self.hl_botoes_11.addWidget(self.atualizarFuncionarios)


        self.verticalLayout_12.addLayout(self.hl_botoes_11)

        self.paginas.addWidget(self.pg_funcionario)
        self.pg_conta = QWidget()
        self.pg_conta.setObjectName(u"pg_conta")
        self.verticalLayout_13 = QVBoxLayout(self.pg_conta)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.vl_titulo_13 = QVBoxLayout()
        self.vl_titulo_13.setObjectName(u"vl_titulo_13")
        self.labelTitulo_13 = QLabel(self.pg_conta)
        self.labelTitulo_13.setObjectName(u"labelTitulo_13")
        self.labelTitulo_13.setFont(font)

        self.vl_titulo_13.addWidget(self.labelTitulo_13)

        self.line_13 = QFrame(self.pg_conta)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.vl_titulo_13.addWidget(self.line_13)


        self.verticalLayout_13.addLayout(self.vl_titulo_13)

        self.tabelaConta = QTreeWidget(self.pg_conta)
        __qtreewidgetitem6 = QTreeWidgetItem()
        __qtreewidgetitem6.setText(0, u"1");
        self.tabelaConta.setHeaderItem(__qtreewidgetitem6)
        self.tabelaConta.setObjectName(u"tabelaConta")

        self.verticalLayout_13.addWidget(self.tabelaConta)

        self.hl_botoes_12 = QHBoxLayout()
        self.hl_botoes_12.setObjectName(u"hl_botoes_12")
        self.adicionarConta = QPushButton(self.pg_conta)
        self.adicionarConta.setObjectName(u"adicionarConta")
        sizePolicy2.setHeightForWidth(self.adicionarConta.sizePolicy().hasHeightForWidth())
        self.adicionarConta.setSizePolicy(sizePolicy2)
        self.adicionarConta.setMinimumSize(QSize(80, 0))
        self.adicionarConta.setFont(font1)
        self.adicionarConta.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);\n"
"border-color: transparent;")

        self.hl_botoes_12.addWidget(self.adicionarConta)

        self.editarConta = QPushButton(self.pg_conta)
        self.editarConta.setObjectName(u"editarConta")
        sizePolicy2.setHeightForWidth(self.editarConta.sizePolicy().hasHeightForWidth())
        self.editarConta.setSizePolicy(sizePolicy2)
        self.editarConta.setMinimumSize(QSize(80, 0))
        self.editarConta.setFont(font1)
        self.editarConta.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 217, 0);\n"
"border-color: transparent;")

        self.hl_botoes_12.addWidget(self.editarConta)

        self.deletarConta = QPushButton(self.pg_conta)
        self.deletarConta.setObjectName(u"deletarConta")
        sizePolicy2.setHeightForWidth(self.deletarConta.sizePolicy().hasHeightForWidth())
        self.deletarConta.setSizePolicy(sizePolicy2)
        self.deletarConta.setMinimumSize(QSize(80, 0))
        self.deletarConta.setFont(font1)
        self.deletarConta.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-color: transparent;")
        self.deletarConta.setFlat(False)

        self.hl_botoes_12.addWidget(self.deletarConta)

        self.espH_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_botoes_12.addItem(self.espH_12)

        self.atualizarContas = QPushButton(self.pg_conta)
        self.atualizarContas.setObjectName(u"atualizarContas")
        sizePolicy2.setHeightForWidth(self.atualizarContas.sizePolicy().hasHeightForWidth())
        self.atualizarContas.setSizePolicy(sizePolicy2)
        self.atualizarContas.setMinimumSize(QSize(80, 0))
        self.atualizarContas.setFont(font1)
        self.atualizarContas.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-color: transparent;")

        self.hl_botoes_12.addWidget(self.atualizarContas)


        self.verticalLayout_13.addLayout(self.hl_botoes_12)

        self.paginas.addWidget(self.pg_conta)
        self.pg_convidado = QWidget()
        self.pg_convidado.setObjectName(u"pg_convidado")
        self.verticalLayout_7 = QVBoxLayout(self.pg_convidado)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.vl_titulo_14 = QVBoxLayout()
        self.vl_titulo_14.setObjectName(u"vl_titulo_14")
        self.labelTitulo_14 = QLabel(self.pg_convidado)
        self.labelTitulo_14.setObjectName(u"labelTitulo_14")
        self.labelTitulo_14.setFont(font)

        self.vl_titulo_14.addWidget(self.labelTitulo_14)

        self.line_14 = QFrame(self.pg_convidado)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.vl_titulo_14.addWidget(self.line_14)


        self.verticalLayout_7.addLayout(self.vl_titulo_14)

        self.tabelaConvidado = QTreeWidget(self.pg_convidado)
        __qtreewidgetitem7 = QTreeWidgetItem()
        __qtreewidgetitem7.setText(0, u"1");
        self.tabelaConvidado.setHeaderItem(__qtreewidgetitem7)
        self.tabelaConvidado.setObjectName(u"tabelaConvidado")

        self.verticalLayout_7.addWidget(self.tabelaConvidado)

        self.hl_botoes_13 = QHBoxLayout()
        self.hl_botoes_13.setObjectName(u"hl_botoes_13")
        self.adicionarConvidado = QPushButton(self.pg_convidado)
        self.adicionarConvidado.setObjectName(u"adicionarConvidado")
        sizePolicy2.setHeightForWidth(self.adicionarConvidado.sizePolicy().hasHeightForWidth())
        self.adicionarConvidado.setSizePolicy(sizePolicy2)
        self.adicionarConvidado.setMinimumSize(QSize(80, 0))
        self.adicionarConvidado.setFont(font1)
        self.adicionarConvidado.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);\n"
"border-color: transparent;")

        self.hl_botoes_13.addWidget(self.adicionarConvidado)

        self.editarConvidado = QPushButton(self.pg_convidado)
        self.editarConvidado.setObjectName(u"editarConvidado")
        sizePolicy2.setHeightForWidth(self.editarConvidado.sizePolicy().hasHeightForWidth())
        self.editarConvidado.setSizePolicy(sizePolicy2)
        self.editarConvidado.setMinimumSize(QSize(80, 0))
        self.editarConvidado.setFont(font1)
        self.editarConvidado.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 217, 0);\n"
"border-color: transparent;")

        self.hl_botoes_13.addWidget(self.editarConvidado)

        self.deletarConvidado = QPushButton(self.pg_convidado)
        self.deletarConvidado.setObjectName(u"deletarConvidado")
        sizePolicy2.setHeightForWidth(self.deletarConvidado.sizePolicy().hasHeightForWidth())
        self.deletarConvidado.setSizePolicy(sizePolicy2)
        self.deletarConvidado.setMinimumSize(QSize(80, 0))
        self.deletarConvidado.setFont(font1)
        self.deletarConvidado.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-color: transparent;")
        self.deletarConvidado.setFlat(False)

        self.hl_botoes_13.addWidget(self.deletarConvidado)

        self.espH_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_botoes_13.addItem(self.espH_13)

        self.atualizarConvidados = QPushButton(self.pg_convidado)
        self.atualizarConvidados.setObjectName(u"atualizarConvidados")
        sizePolicy2.setHeightForWidth(self.atualizarConvidados.sizePolicy().hasHeightForWidth())
        self.atualizarConvidados.setSizePolicy(sizePolicy2)
        self.atualizarConvidados.setMinimumSize(QSize(80, 0))
        self.atualizarConvidados.setFont(font1)
        self.atualizarConvidados.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-color: transparent;")

        self.hl_botoes_13.addWidget(self.atualizarConvidados)


        self.verticalLayout_7.addLayout(self.hl_botoes_13)

        self.paginas.addWidget(self.pg_convidado)
        self.pg_servico = QWidget()
        self.pg_servico.setObjectName(u"pg_servico")
        self.verticalLayout_8 = QVBoxLayout(self.pg_servico)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.vl_titulo_15 = QVBoxLayout()
        self.vl_titulo_15.setObjectName(u"vl_titulo_15")
        self.labelTitulo_15 = QLabel(self.pg_servico)
        self.labelTitulo_15.setObjectName(u"labelTitulo_15")
        self.labelTitulo_15.setFont(font)

        self.vl_titulo_15.addWidget(self.labelTitulo_15)

        self.line_15 = QFrame(self.pg_servico)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.vl_titulo_15.addWidget(self.line_15)


        self.verticalLayout_8.addLayout(self.vl_titulo_15)

        self.tabelaServico = QTreeWidget(self.pg_servico)
        __qtreewidgetitem8 = QTreeWidgetItem()
        __qtreewidgetitem8.setText(0, u"1");
        self.tabelaServico.setHeaderItem(__qtreewidgetitem8)
        self.tabelaServico.setObjectName(u"tabelaServico")

        self.verticalLayout_8.addWidget(self.tabelaServico)

        self.hl_botoes_14 = QHBoxLayout()
        self.hl_botoes_14.setObjectName(u"hl_botoes_14")
        self.adicionarServico = QPushButton(self.pg_servico)
        self.adicionarServico.setObjectName(u"adicionarServico")
        sizePolicy2.setHeightForWidth(self.adicionarServico.sizePolicy().hasHeightForWidth())
        self.adicionarServico.setSizePolicy(sizePolicy2)
        self.adicionarServico.setMinimumSize(QSize(80, 0))
        self.adicionarServico.setFont(font1)
        self.adicionarServico.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);\n"
"border-color: transparent;")

        self.hl_botoes_14.addWidget(self.adicionarServico)

        self.editarServico = QPushButton(self.pg_servico)
        self.editarServico.setObjectName(u"editarServico")
        sizePolicy2.setHeightForWidth(self.editarServico.sizePolicy().hasHeightForWidth())
        self.editarServico.setSizePolicy(sizePolicy2)
        self.editarServico.setMinimumSize(QSize(80, 0))
        self.editarServico.setFont(font1)
        self.editarServico.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 217, 0);\n"
"border-color: transparent;")

        self.hl_botoes_14.addWidget(self.editarServico)

        self.deletarServico = QPushButton(self.pg_servico)
        self.deletarServico.setObjectName(u"deletarServico")
        sizePolicy2.setHeightForWidth(self.deletarServico.sizePolicy().hasHeightForWidth())
        self.deletarServico.setSizePolicy(sizePolicy2)
        self.deletarServico.setMinimumSize(QSize(80, 0))
        self.deletarServico.setFont(font1)
        self.deletarServico.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-color: transparent;")
        self.deletarServico.setFlat(False)

        self.hl_botoes_14.addWidget(self.deletarServico)

        self.espH_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_botoes_14.addItem(self.espH_14)

        self.atualizarServicos = QPushButton(self.pg_servico)
        self.atualizarServicos.setObjectName(u"atualizarServicos")
        sizePolicy2.setHeightForWidth(self.atualizarServicos.sizePolicy().hasHeightForWidth())
        self.atualizarServicos.setSizePolicy(sizePolicy2)
        self.atualizarServicos.setMinimumSize(QSize(80, 0))
        self.atualizarServicos.setFont(font1)
        self.atualizarServicos.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-color: transparent;")

        self.hl_botoes_14.addWidget(self.atualizarServicos)


        self.verticalLayout_8.addLayout(self.hl_botoes_14)

        self.paginas.addWidget(self.pg_servico)
        self.pg_itens = QWidget()
        self.pg_itens.setObjectName(u"pg_itens")
        self.verticalLayout_9 = QVBoxLayout(self.pg_itens)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.vl_titulo_16 = QVBoxLayout()
        self.vl_titulo_16.setObjectName(u"vl_titulo_16")
        self.labelTitulo_16 = QLabel(self.pg_itens)
        self.labelTitulo_16.setObjectName(u"labelTitulo_16")
        self.labelTitulo_16.setFont(font)

        self.vl_titulo_16.addWidget(self.labelTitulo_16)

        self.line_16 = QFrame(self.pg_itens)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.vl_titulo_16.addWidget(self.line_16)


        self.verticalLayout_9.addLayout(self.vl_titulo_16)

        self.tabelaItens = QTreeWidget(self.pg_itens)
        __qtreewidgetitem9 = QTreeWidgetItem()
        __qtreewidgetitem9.setText(0, u"1");
        self.tabelaItens.setHeaderItem(__qtreewidgetitem9)
        self.tabelaItens.setObjectName(u"tabelaItens")

        self.verticalLayout_9.addWidget(self.tabelaItens)

        self.hl_botoes_15 = QHBoxLayout()
        self.hl_botoes_15.setObjectName(u"hl_botoes_15")
        self.adicionarItens = QPushButton(self.pg_itens)
        self.adicionarItens.setObjectName(u"adicionarItens")
        sizePolicy2.setHeightForWidth(self.adicionarItens.sizePolicy().hasHeightForWidth())
        self.adicionarItens.setSizePolicy(sizePolicy2)
        self.adicionarItens.setMinimumSize(QSize(80, 0))
        self.adicionarItens.setFont(font1)
        self.adicionarItens.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);\n"
"border-color: transparent;")

        self.hl_botoes_15.addWidget(self.adicionarItens)

        self.editarItens = QPushButton(self.pg_itens)
        self.editarItens.setObjectName(u"editarItens")
        sizePolicy2.setHeightForWidth(self.editarItens.sizePolicy().hasHeightForWidth())
        self.editarItens.setSizePolicy(sizePolicy2)
        self.editarItens.setMinimumSize(QSize(80, 0))
        self.editarItens.setFont(font1)
        self.editarItens.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 217, 0);\n"
"border-color: transparent;")

        self.hl_botoes_15.addWidget(self.editarItens)

        self.deletarItens = QPushButton(self.pg_itens)
        self.deletarItens.setObjectName(u"deletarItens")
        sizePolicy2.setHeightForWidth(self.deletarItens.sizePolicy().hasHeightForWidth())
        self.deletarItens.setSizePolicy(sizePolicy2)
        self.deletarItens.setMinimumSize(QSize(80, 0))
        self.deletarItens.setFont(font1)
        self.deletarItens.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-color: transparent;")
        self.deletarItens.setFlat(False)

        self.hl_botoes_15.addWidget(self.deletarItens)

        self.espH_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_botoes_15.addItem(self.espH_15)

        self.atualizarItens = QPushButton(self.pg_itens)
        self.atualizarItens.setObjectName(u"atualizarItens")
        sizePolicy2.setHeightForWidth(self.atualizarItens.sizePolicy().hasHeightForWidth())
        self.atualizarItens.setSizePolicy(sizePolicy2)
        self.atualizarItens.setMinimumSize(QSize(80, 0))
        self.atualizarItens.setFont(font1)
        self.atualizarItens.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-color: transparent;")

        self.hl_botoes_15.addWidget(self.atualizarItens)


        self.verticalLayout_9.addLayout(self.hl_botoes_15)

        self.paginas.addWidget(self.pg_itens)
        self.pg_multa = QWidget()
        self.pg_multa.setObjectName(u"pg_multa")
        self.verticalLayout_10 = QVBoxLayout(self.pg_multa)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.vl_titulo_17 = QVBoxLayout()
        self.vl_titulo_17.setObjectName(u"vl_titulo_17")
        self.labelTitulo_17 = QLabel(self.pg_multa)
        self.labelTitulo_17.setObjectName(u"labelTitulo_17")
        self.labelTitulo_17.setFont(font)

        self.vl_titulo_17.addWidget(self.labelTitulo_17)

        self.line_17 = QFrame(self.pg_multa)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.vl_titulo_17.addWidget(self.line_17)


        self.verticalLayout_10.addLayout(self.vl_titulo_17)

        self.tabelaMulta = QTreeWidget(self.pg_multa)
        __qtreewidgetitem10 = QTreeWidgetItem()
        __qtreewidgetitem10.setText(0, u"1");
        self.tabelaMulta.setHeaderItem(__qtreewidgetitem10)
        self.tabelaMulta.setObjectName(u"tabelaMulta")

        self.verticalLayout_10.addWidget(self.tabelaMulta)

        self.hl_botoes_16 = QHBoxLayout()
        self.hl_botoes_16.setObjectName(u"hl_botoes_16")
        self.adicionarMulta = QPushButton(self.pg_multa)
        self.adicionarMulta.setObjectName(u"adicionarMulta")
        sizePolicy2.setHeightForWidth(self.adicionarMulta.sizePolicy().hasHeightForWidth())
        self.adicionarMulta.setSizePolicy(sizePolicy2)
        self.adicionarMulta.setMinimumSize(QSize(80, 0))
        self.adicionarMulta.setFont(font1)
        self.adicionarMulta.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);\n"
"border-color: transparent;")

        self.hl_botoes_16.addWidget(self.adicionarMulta)

        self.editarMulta = QPushButton(self.pg_multa)
        self.editarMulta.setObjectName(u"editarMulta")
        sizePolicy2.setHeightForWidth(self.editarMulta.sizePolicy().hasHeightForWidth())
        self.editarMulta.setSizePolicy(sizePolicy2)
        self.editarMulta.setMinimumSize(QSize(80, 0))
        self.editarMulta.setFont(font1)
        self.editarMulta.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 217, 0);\n"
"border-color: transparent;")

        self.hl_botoes_16.addWidget(self.editarMulta)

        self.deletarMulta = QPushButton(self.pg_multa)
        self.deletarMulta.setObjectName(u"deletarMulta")
        sizePolicy2.setHeightForWidth(self.deletarMulta.sizePolicy().hasHeightForWidth())
        self.deletarMulta.setSizePolicy(sizePolicy2)
        self.deletarMulta.setMinimumSize(QSize(80, 0))
        self.deletarMulta.setFont(font1)
        self.deletarMulta.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-color: transparent;")
        self.deletarMulta.setFlat(False)

        self.hl_botoes_16.addWidget(self.deletarMulta)

        self.espH_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_botoes_16.addItem(self.espH_16)

        self.atualizarMulta = QPushButton(self.pg_multa)
        self.atualizarMulta.setObjectName(u"atualizarMulta")
        sizePolicy2.setHeightForWidth(self.atualizarMulta.sizePolicy().hasHeightForWidth())
        self.atualizarMulta.setSizePolicy(sizePolicy2)
        self.atualizarMulta.setMinimumSize(QSize(80, 0))
        self.atualizarMulta.setFont(font1)
        self.atualizarMulta.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-color: transparent;")

        self.hl_botoes_16.addWidget(self.atualizarMulta)


        self.verticalLayout_10.addLayout(self.hl_botoes_16)

        self.paginas.addWidget(self.pg_multa)
        self.pg_consumo = QWidget()
        self.pg_consumo.setObjectName(u"pg_consumo")
        self.verticalLayout_11 = QVBoxLayout(self.pg_consumo)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.vl_titulo_18 = QVBoxLayout()
        self.vl_titulo_18.setObjectName(u"vl_titulo_18")
        self.labelTitulo_18 = QLabel(self.pg_consumo)
        self.labelTitulo_18.setObjectName(u"labelTitulo_18")
        self.labelTitulo_18.setFont(font)

        self.vl_titulo_18.addWidget(self.labelTitulo_18)

        self.line_18 = QFrame(self.pg_consumo)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.vl_titulo_18.addWidget(self.line_18)


        self.verticalLayout_11.addLayout(self.vl_titulo_18)

        self.tabelaConsumo = QTreeWidget(self.pg_consumo)
        __qtreewidgetitem11 = QTreeWidgetItem()
        __qtreewidgetitem11.setText(0, u"1");
        self.tabelaConsumo.setHeaderItem(__qtreewidgetitem11)
        self.tabelaConsumo.setObjectName(u"tabelaConsumo")

        self.verticalLayout_11.addWidget(self.tabelaConsumo)

        self.hl_botoes_17 = QHBoxLayout()
        self.hl_botoes_17.setObjectName(u"hl_botoes_17")
        self.adicionarConsumo = QPushButton(self.pg_consumo)
        self.adicionarConsumo.setObjectName(u"adicionarConsumo")
        sizePolicy2.setHeightForWidth(self.adicionarConsumo.sizePolicy().hasHeightForWidth())
        self.adicionarConsumo.setSizePolicy(sizePolicy2)
        self.adicionarConsumo.setMinimumSize(QSize(80, 0))
        self.adicionarConsumo.setFont(font1)
        self.adicionarConsumo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);\n"
"border-color: transparent;")

        self.hl_botoes_17.addWidget(self.adicionarConsumo)

        self.editarConsumo = QPushButton(self.pg_consumo)
        self.editarConsumo.setObjectName(u"editarConsumo")
        sizePolicy2.setHeightForWidth(self.editarConsumo.sizePolicy().hasHeightForWidth())
        self.editarConsumo.setSizePolicy(sizePolicy2)
        self.editarConsumo.setMinimumSize(QSize(80, 0))
        self.editarConsumo.setFont(font1)
        self.editarConsumo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 217, 0);\n"
"border-color: transparent;")

        self.hl_botoes_17.addWidget(self.editarConsumo)

        self.deletarConsumo = QPushButton(self.pg_consumo)
        self.deletarConsumo.setObjectName(u"deletarConsumo")
        sizePolicy2.setHeightForWidth(self.deletarConsumo.sizePolicy().hasHeightForWidth())
        self.deletarConsumo.setSizePolicy(sizePolicy2)
        self.deletarConsumo.setMinimumSize(QSize(80, 0))
        self.deletarConsumo.setFont(font1)
        self.deletarConsumo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-color: transparent;")
        self.deletarConsumo.setFlat(False)

        self.hl_botoes_17.addWidget(self.deletarConsumo)

        self.espH_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_botoes_17.addItem(self.espH_17)

        self.atualizarConsumos = QPushButton(self.pg_consumo)
        self.atualizarConsumos.setObjectName(u"atualizarConsumos")
        sizePolicy2.setHeightForWidth(self.atualizarConsumos.sizePolicy().hasHeightForWidth())
        self.atualizarConsumos.setSizePolicy(sizePolicy2)
        self.atualizarConsumos.setMinimumSize(QSize(80, 0))
        self.atualizarConsumos.setFont(font1)
        self.atualizarConsumos.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-color: transparent;")

        self.hl_botoes_17.addWidget(self.atualizarConsumos)


        self.verticalLayout_11.addLayout(self.hl_botoes_17)

        self.paginas.addWidget(self.pg_consumo)
        self.pg_inicio = QWidget()
        self.pg_inicio.setObjectName(u"pg_inicio")
        self.label = QLabel(self.pg_inicio)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 70, 241, 291))
        self.label.setPixmap(QPixmap(u"config/img/icone.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.pg_inicio)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 60, 92, 81))
        font2 = QFont()
        font2.setFamily(u"Bebas Neue")
        font2.setPointSize(20)
        self.label_2.setFont(font2)
        self.label_2.setPixmap(QPixmap(u"config/img/cama.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.btQuartos = QPushButton(self.pg_inicio)
        self.btQuartos.setObjectName(u"btQuartos")
        self.btQuartos.setGeometry(QRect(30, 130, 150, 40))
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btQuartos.sizePolicy().hasHeightForWidth())
        self.btQuartos.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamily(u"Bebas Neue")
        font3.setPointSize(14)
        self.btQuartos.setFont(font3)
        self.btQuartos.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: white;\n"
"border-radius: 15px;")
        self.btQuartos.setIconSize(QSize(80, 80))
        self.btQuartos.setFlat(False)
        self.btReservas = QPushButton(self.pg_inicio)
        self.btReservas.setObjectName(u"btReservas")
        self.btReservas.setGeometry(QRect(30, 300, 150, 40))
        sizePolicy3.setHeightForWidth(self.btReservas.sizePolicy().hasHeightForWidth())
        self.btReservas.setSizePolicy(sizePolicy3)
        self.btReservas.setFont(font3)
        self.btReservas.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: white;\n"
"border-radius: 15px;")
        self.btReservas.setIconSize(QSize(80, 80))
        self.btReservas.setFlat(False)
        self.label_3 = QLabel(self.pg_inicio)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 220, 92, 81))
        self.label_3.setFont(font2)
        self.label_3.setPixmap(QPixmap(u"config/img/key.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.btHospedes = QPushButton(self.pg_inicio)
        self.btHospedes.setObjectName(u"btHospedes")
        self.btHospedes.setGeometry(QRect(30, 470, 150, 40))
        sizePolicy3.setHeightForWidth(self.btHospedes.sizePolicy().hasHeightForWidth())
        self.btHospedes.setSizePolicy(sizePolicy3)
        self.btHospedes.setFont(font3)
        self.btHospedes.setStyleSheet(u"background-color: rgb(0, 200, 0);\n"
"color: white;\n"
"border-radius: 15px;")
        self.btHospedes.setIconSize(QSize(80, 80))
        self.btHospedes.setFlat(False)
        self.label_4 = QLabel(self.pg_inicio)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 390, 92, 81))
        self.label_4.setFont(font2)
        self.label_4.setPixmap(QPixmap(u"config/img/hospedes.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.btAdminstracao = QPushButton(self.pg_inicio)
        self.btAdminstracao.setObjectName(u"btAdminstracao")
        self.btAdminstracao.setGeometry(QRect(630, 130, 150, 40))
        sizePolicy3.setHeightForWidth(self.btAdminstracao.sizePolicy().hasHeightForWidth())
        self.btAdminstracao.setSizePolicy(sizePolicy3)
        self.btAdminstracao.setFont(font3)
        self.btAdminstracao.setStyleSheet(u"background-color: rgb(162, 0, 255);\n"
"color: white;\n"
"border-radius: 15px;")
        self.btAdminstracao.setIconSize(QSize(80, 80))
        self.btAdminstracao.setFlat(False)
        self.label_5 = QLabel(self.pg_inicio)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(660, 50, 92, 81))
        self.label_5.setFont(font2)
        self.label_5.setPixmap(QPixmap(u"config/img/dashboard.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.btFuncionarios = QPushButton(self.pg_inicio)
        self.btFuncionarios.setObjectName(u"btFuncionarios")
        self.btFuncionarios.setGeometry(QRect(630, 300, 150, 40))
        sizePolicy3.setHeightForWidth(self.btFuncionarios.sizePolicy().hasHeightForWidth())
        self.btFuncionarios.setSizePolicy(sizePolicy3)
        self.btFuncionarios.setFont(font3)
        self.btFuncionarios.setStyleSheet(u"background-color: rgb(170, 85, 0);\n"
"color: white;\n"
"border-radius: 15px;")
        self.btFuncionarios.setIconSize(QSize(80, 80))
        self.btFuncionarios.setFlat(False)
        self.label_6 = QLabel(self.pg_inicio)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(660, 220, 92, 81))
        self.label_6.setFont(font2)
        self.label_6.setPixmap(QPixmap(u"config/img/funcionarios.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.pg_inicio)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(660, 370, 92, 81))
        self.label_7.setFont(font2)
        self.label_7.setPixmap(QPixmap(u"config/img/itens.webp"))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.pushButton_6 = QPushButton(self.pg_inicio)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(630, 450, 150, 40))
        sizePolicy3.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy3)
        self.pushButton_6.setFont(font3)
        self.pushButton_6.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: white;\n"
"border-radius: 15px;")
        self.pushButton_6.setIconSize(QSize(80, 80))
        self.pushButton_6.setFlat(False)
        self.line_2 = QFrame(self.pg_inicio)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(200, 20, 20, 521))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_7 = QFrame(self.pg_inicio)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(570, 20, 20, 521))
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.label_8 = QLabel(self.pg_inicio)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(250, 360, 291, 81))
        font4 = QFont()
        font4.setFamily(u"Bebas Neue")
        font4.setPointSize(24)
        self.label_8.setFont(font4)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.pg_inicio)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(270, 410, 251, 41))
        font5 = QFont()
        font5.setFamily(u"Bebas Neue")
        font5.setPointSize(12)
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"color: rgb(96, 96, 96);")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.paginas.addWidget(self.pg_inicio)

        self.verticalLayout.addWidget(self.paginas)

        Janela.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Janela)
        self.statusbar.setObjectName(u"statusbar")
        Janela.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(Janela)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 817, 18))
        self.menuGerenciar = QMenu(self.menubar)
        self.menuGerenciar.setObjectName(u"menuGerenciar")
        self.menuReserva = QMenu(self.menuGerenciar)
        self.menuReserva.setObjectName(u"menuReserva")
        self.menuQuarto = QMenu(self.menuGerenciar)
        self.menuQuarto.setObjectName(u"menuQuarto")
        self.menuFuncionarios = QMenu(self.menuGerenciar)
        self.menuFuncionarios.setObjectName(u"menuFuncionarios")
        self.menuAdministrador = QMenu(self.menubar)
        self.menuAdministrador.setObjectName(u"menuAdministrador")
        Janela.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuGerenciar.menuAction())
        self.menubar.addAction(self.menuAdministrador.menuAction())
        self.menuGerenciar.addAction(self.menuReserva.menuAction())
        self.menuGerenciar.addAction(self.actionHospede)
        self.menuGerenciar.addSeparator()
        self.menuGerenciar.addAction(self.menuQuarto.menuAction())
        self.menuGerenciar.addAction(self.menuFuncionarios.menuAction())
        self.menuReserva.addAction(self.actionProcurarReserva)
        self.menuReserva.addAction(self.actionConvidados)
        self.menuReserva.addAction(self.actionServicos)
        self.menuReserva.addAction(self.actionMultas)
        self.menuReserva.addAction(self.actionConsumo)
        self.menuQuarto.addAction(self.actionProcurarQuartos)
        self.menuQuarto.addAction(self.actionCategoriasQuartos)
        self.menuQuarto.addAction(self.actionItens)
        self.menuFuncionarios.addAction(self.actionProcurarFuncionarios)
        self.menuFuncionarios.addAction(self.actionFuncoes)
        self.menuAdministrador.addAction(self.actionAdministrador)
        self.menuAdministrador.addAction(self.actionContas)

        self.retranslateUi(Janela)

        self.paginas.setCurrentIndex(12)


        QMetaObject.connectSlotsByName(Janela)
    # setupUi

    def retranslateUi(self, Janela):
        Janela.setWindowTitle(QCoreApplication.translate("Janela", u"Checkup: Atlantic Hotel", None))
        self.actionProcurar.setText(QCoreApplication.translate("Janela", u"Procurar", None))
        self.actionCategorias.setText(QCoreApplication.translate("Janela", u"Categorias", None))
        self.actionProcurar_2.setText(QCoreApplication.translate("Janela", u"Procurar", None))
        self.actionCategorias_2.setText(QCoreApplication.translate("Janela", u"Categorias", None))
        self.actionProcurarReserva.setText(QCoreApplication.translate("Janela", u"Procurar", None))
        self.actionServicos.setText(QCoreApplication.translate("Janela", u"Servi\u00e7os", None))
        self.actionMultas.setText(QCoreApplication.translate("Janela", u"Multas", None))
        self.actionHospede.setText(QCoreApplication.translate("Janela", u"Hospede", None))
        self.actionConsumo.setText(QCoreApplication.translate("Janela", u"Consumo", None))
        self.actionNfe.setText(QCoreApplication.translate("Janela", u"NFe", None))
        self.actionProcurarQuartos.setText(QCoreApplication.translate("Janela", u"Procurar", None))
        self.actionCategoriasQuartos.setText(QCoreApplication.translate("Janela", u"Categorias", None))
        self.actionItens.setText(QCoreApplication.translate("Janela", u"Itens", None))
        self.actionProcurarFuncionarios.setText(QCoreApplication.translate("Janela", u"Procurar", None))
        self.actionFuncoes.setText(QCoreApplication.translate("Janela", u"Fun\u00e7\u00f5es", None))
        self.actionAdministrador.setText(QCoreApplication.translate("Janela", u"Perfil", None))
        self.actionContas.setText(QCoreApplication.translate("Janela", u"Contas", None))
        self.actionInfo.setText(QCoreApplication.translate("Janela", u"Info", None))
        self.actionDefinicoes.setText(QCoreApplication.translate("Janela", u"Defini\u00e7\u00f5es de Sistema", None))
        self.actionContato.setText(QCoreApplication.translate("Janela", u"Contato e Suporte", None))
        self.actionConvidados.setText(QCoreApplication.translate("Janela", u"Convidados", None))
        self.labelTitulo.setText(QCoreApplication.translate("Janela", u"Reservas", None))
        self.adicionarReserva.setText(QCoreApplication.translate("Janela", u"Adicionar", None))
        self.editarReserva.setText(QCoreApplication.translate("Janela", u"EDITAR", None))
        self.deletarReserva.setText(QCoreApplication.translate("Janela", u"deletar", None))
        self.atualizarReservas.setText(QCoreApplication.translate("Janela", u"Atualizar", None))
        self.labelTitulo_3.setText(QCoreApplication.translate("Janela", u"Fun\u00e7\u00f5es", None))
        self.adicionarFuncao.setText(QCoreApplication.translate("Janela", u"Adicionar", None))
        self.editarFuncao.setText(QCoreApplication.translate("Janela", u"EDITAR", None))
        self.deletarFuncao.setText(QCoreApplication.translate("Janela", u"deletar", None))
        self.atualizarFuncoes.setText(QCoreApplication.translate("Janela", u"Atualizar", None))
        self.labelTitulo_4.setText(QCoreApplication.translate("Janela", u"Hospedes", None))
        self.adicionarHospede.setText(QCoreApplication.translate("Janela", u"Adicionar", None))
        self.editarHospede.setText(QCoreApplication.translate("Janela", u"EDITAR", None))
        self.deletarHospede.setText(QCoreApplication.translate("Janela", u"deletar", None))
        self.atualizarHospedes.setText(QCoreApplication.translate("Janela", u"Atualizar", None))
        self.labelTitulo_5.setText(QCoreApplication.translate("Janela", u"CATEGORIA DOS QUARTOS", None))
        self.adicionarCategoriaQuarto.setText(QCoreApplication.translate("Janela", u"Adicionar", None))
        self.editarCategoriaQuarto.setText(QCoreApplication.translate("Janela", u"EDITAR", None))
        self.deletarCategoriaQuarto.setText(QCoreApplication.translate("Janela", u"deletar", None))
        self.atualizarCategoriaQuartos.setText(QCoreApplication.translate("Janela", u"Atualizar", None))
        self.labelTitulo_6.setText(QCoreApplication.translate("Janela", u"QUARTOS", None))
        self.adicionarQuarto.setText(QCoreApplication.translate("Janela", u"Adicionar", None))
        self.editarQuarto.setText(QCoreApplication.translate("Janela", u"EDITAR", None))
        self.deletarQuarto.setText(QCoreApplication.translate("Janela", u"deletar", None))
        self.atualizarQuartos.setText(QCoreApplication.translate("Janela", u"Atualizar", None))
        self.labelTitulo_12.setText(QCoreApplication.translate("Janela", u"Funcion\u00e1rios", None))
        self.adicionarFuncionario.setText(QCoreApplication.translate("Janela", u"Adicionar", None))
        self.editarFuncionario.setText(QCoreApplication.translate("Janela", u"EDITAR", None))
        self.deletarFuncionario.setText(QCoreApplication.translate("Janela", u"deletar", None))
        self.atualizarFuncionarios.setText(QCoreApplication.translate("Janela", u"Atualizar", None))
        self.labelTitulo_13.setText(QCoreApplication.translate("Janela", u"Contas", None))
        self.adicionarConta.setText(QCoreApplication.translate("Janela", u"Adicionar", None))
        self.editarConta.setText(QCoreApplication.translate("Janela", u"EDITAR", None))
        self.deletarConta.setText(QCoreApplication.translate("Janela", u"deletar", None))
        self.atualizarContas.setText(QCoreApplication.translate("Janela", u"Atualizar", None))
        self.labelTitulo_14.setText(QCoreApplication.translate("Janela", u"CONVIDADOS", None))
        self.adicionarConvidado.setText(QCoreApplication.translate("Janela", u"Adicionar", None))
        self.editarConvidado.setText(QCoreApplication.translate("Janela", u"EDITAR", None))
        self.deletarConvidado.setText(QCoreApplication.translate("Janela", u"deletar", None))
        self.atualizarConvidados.setText(QCoreApplication.translate("Janela", u"Atualizar", None))
        self.labelTitulo_15.setText(QCoreApplication.translate("Janela", u"Servi\u00e7os", None))
        self.adicionarServico.setText(QCoreApplication.translate("Janela", u"Adicionar", None))
        self.editarServico.setText(QCoreApplication.translate("Janela", u"EDITAR", None))
        self.deletarServico.setText(QCoreApplication.translate("Janela", u"deletar", None))
        self.atualizarServicos.setText(QCoreApplication.translate("Janela", u"Atualizar", None))
        self.labelTitulo_16.setText(QCoreApplication.translate("Janela", u"itens dos quartos", None))
        self.adicionarItens.setText(QCoreApplication.translate("Janela", u"Adicionar", None))
        self.editarItens.setText(QCoreApplication.translate("Janela", u"EDITAR", None))
        self.deletarItens.setText(QCoreApplication.translate("Janela", u"deletar", None))
        self.atualizarItens.setText(QCoreApplication.translate("Janela", u"Atualizar", None))
        self.labelTitulo_17.setText(QCoreApplication.translate("Janela", u"Multas", None))
        self.adicionarMulta.setText(QCoreApplication.translate("Janela", u"Adicionar", None))
        self.editarMulta.setText(QCoreApplication.translate("Janela", u"EDITAR", None))
        self.deletarMulta.setText(QCoreApplication.translate("Janela", u"deletar", None))
        self.atualizarMulta.setText(QCoreApplication.translate("Janela", u"Atualizar", None))
        self.labelTitulo_18.setText(QCoreApplication.translate("Janela", u"COnsumo", None))
        self.adicionarConsumo.setText(QCoreApplication.translate("Janela", u"Adicionar", None))
        self.editarConsumo.setText(QCoreApplication.translate("Janela", u"EDITAR", None))
        self.deletarConsumo.setText(QCoreApplication.translate("Janela", u"deletar", None))
        self.atualizarConsumos.setText(QCoreApplication.translate("Janela", u"Atualizar", None))
        self.label.setText("")
        self.label_2.setText("")
        self.btQuartos.setText(QCoreApplication.translate("Janela", u"quartos", None))
        self.btReservas.setText(QCoreApplication.translate("Janela", u"reservas", None))
        self.label_3.setText("")
        self.btHospedes.setText(QCoreApplication.translate("Janela", u"hospedes", None))
        self.label_4.setText("")
        self.btAdminstracao.setText(QCoreApplication.translate("Janela", u"Adminstra\u00e7ao", None))
        self.label_5.setText("")
        self.btFuncionarios.setText(QCoreApplication.translate("Janela", u"funcion\u00e1rios", None))
        self.label_6.setText("")
        self.label_7.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("Janela", u"itens", None))
        self.label_8.setText(QCoreApplication.translate("Janela", u"checkup", None))
        self.label_9.setText(QCoreApplication.translate("Janela", u"sistema gerenciador de hoteis", None))
        self.menuGerenciar.setTitle(QCoreApplication.translate("Janela", u"Gerenciar", None))
        self.menuReserva.setTitle(QCoreApplication.translate("Janela", u"Reserva", None))
        self.menuQuarto.setTitle(QCoreApplication.translate("Janela", u"Quarto", None))
        self.menuFuncionarios.setTitle(QCoreApplication.translate("Janela", u"Funcion\u00e1rio", None))
        self.menuAdministrador.setTitle(QCoreApplication.translate("Janela", u"Administra\u00e7\u00e3o", None))
    # retranslateUi

