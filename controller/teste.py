import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit, QSpinBox, QSlider, QDial, QVBoxLayout, QWidget, QDialog, QMessageBox
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QPixmap, QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("CheckUp - Gerenciador de Hotel")
        self.setFixedSize(QSize(1920, 1080))
        self.setWindowIcon(QIcon(QPixmap("img/icone.png")))
        
        #LABEL

        self.label = QLabel("Aula 05, Bem-vindo")
        fonte = self.label.font()
        fonte.setPointSize(20)
        fonte.setFamily("Bebas Neue")
        
        self.label.setFont(fonte)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        #BOTAO

        self.botao = QPushButton("Click")
        self.botao.clicked.connect(self.alert)

        #IMAGEM

        self.imagem = QLabel("Pixmap")
        self.imagem.setScaledContents(True)
        self.imagem.setPixmap(QPixmap("img/icone.png"))
        
        #CHECKBOX

        self.check = QCheckBox("Marque a aqui")
        self.check.setCheckState(Qt.Checked)
        self.check.stateChanged.connect(self.status)

        #COMBOBOX

        self.combo = QComboBox()
        self.combo.addItems(['item 1', 'item 2', 'item 3'])

        self.combo.currentIndexChanged.connect(self.show_index)
        self.combo.currentTextChanged.connect(self.show_text)

        #LISTWIDGET

        self.lista = QListWidget()
        self.lista.addItems(['item 1', 'item 2', 'item 3'])

        self.lista.currentTextChanged.connect(self.show_text)

        #LINEEDIT
        self.campo = QLineEdit()
        self.campo.setMaxLength(10)
        self.campo.setPlaceholderText('Coloque seu nome')

        self.campo.returnPressed.connect(self.return_text)
        self.campo.setInputMask('000.000.000-00;_')

        #SINBOX
        self.spin = QSpinBox()
        self.spin.setMinimum(1)
        self.spin.setMaximum(100)
        self.spin.setSuffix(' un')

        self.slider = QSlider()
        self.slider.setMinimum(-10)
        self.slider.setMaximum(10)

        self.slider.setSingleStep(2)

        self.slider.valueChanged.connect(self.value_changed)
        self.slider.sliderMoved.connect(self.slider_position)
        self.slider.sliderPressed.connect(self.slider_pressed)
        self.slider.sliderReleased.connect(self.slider_released)

        #DIAL

        self.dial = QDial()
        self.dial.setRange(-10, 100)
        self.dial.setSingleStep(0.5)

        self.dial.valueChanged.connect(self.value_changed)
        self.dial.sliderMoved.connect(self.slider_position)
        self.dial.sliderPressed.connect(self.slider_pressed)
        self.dial.sliderReleased.connect(self.slider_released)

        #self.setCentralWidget(self.label)
        #self.setCentralWidget(self.botao)
        #self.setCentralWidget(self.imagem)
        #self.setCentralWidget(self.check)
        #self.setCentralWidget(self.combo)
        #self.setCentralWidget(self.lista)
        #self.setCentralWidget(self.campo)
        #self.setCentralWidget(self.spin)
        #self.setCentralWidget(self.slider)
        #self.setCentralWidget(self.dial)

        #LAYOUT

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.botao)
        self.layout.addWidget(self.imagem)
        self.layout.addWidget(self.check)
        self.layout.addWidget(self.combo)
        self.layout.addWidget(self.lista)
        self.layout.addWidget(self.campo)
        self.layout.addWidget(self.spin)
        self.layout.addWidget(self.slider)
        self.layout.addWidget(self.dial)

        self.teste = QWidget()
        self.teste.setLayout(self.layout)

        self.setCentralWidget(self.teste)
    
    def alert(self):

        msg = QMessageBox(self)
        msg.setWindowTitle("MSG")
        msg.setText("Ok")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = msg.exec_()

        if result == QMessageBox.Yes:
            print('Botão pressionado!!')
            self.botao.setEnabled(False)
            d = QDialog(self)
            d.setWindowTitle("Hello")
            d.exec_()

    def status(self, s):
        print(s == Qt.Checked)
        print(s)

    def show_index(self, i):
        print(i)

    def show_text(self, s):
        print(s)

    def return_text(self):
        print("Enter pressionado")
        self.centralWidget().setText(f"Olá { self.campo.text() } ")

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print('position', p)

    def slider_pressed(self):
        print('pressed')

    def slider_released(self):
        print('released')



app = QApplication(sys.argv)
janela = MainWindow()

janela.show()
app.exec_()