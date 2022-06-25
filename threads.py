import time
from PySide2 import QtCore, QtWidgets


class MyApp(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()

    def initUi(self):
        self.lineEdirStart = QtWidgets.QLineEdit()
        self.lineEdirStart.setPlaceholderText('Введите количество секунд.')

        self.pushButtonStart = QtWidgets.QPushButton()
        self.pushButtonStart.setText('Start')
        self.pushButtonStop = QtWidgets.QPushButton()
        self.pushButtonStop.setText('Stop')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lineEdirStart)
        layout.addWidget(self.pushButtonStart)
        layout.addWidget(self.pushButtonStop)
        self.setLayout(layout)



if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = MyApp()
    win.show()

    app.exec_()
