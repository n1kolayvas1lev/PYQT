import time
from PySide2 import QtCore, QtWidgets


class MyApp(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initThreads()

    def initThreads(self):
        self.timerThread = TimerThread()

    def initUi(self):
        # ui
        self.setFixedSize(180, 150)  # Установка фиксированных размеров окна

        self.lineEditStart = QtWidgets.QLineEdit()
        self.lineEditStart.setPlaceholderText('Введите количество секунд.')

        self.pushButtonStart = QtWidgets.QPushButton()
        self.pushButtonStart.setText('Start')

        self.pushButtonStop = QtWidgets.QPushButton()
        self.pushButtonStop.setText('Stop')

        # Изменение политик растяжения кнопок.
        # self.pushButtonStop.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
        #                                    QtWidgets.QSizePolicy.Policy.Expanding)
        # self.pushButtonStart.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
        #                                    QtWidgets.QSizePolicy.Policy.Expanding)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lineEditStart)
        layout.addWidget(self.pushButtonStart)
        layout.addWidget(self.pushButtonStop)
        self.setLayout(layout)
        # Добавление спейсера на форму для занятия всего свободного пространства. 1 - размер в пикс.
        # layout.addSpacerItem(
        #     QtWidgets.QSpacerItem(
        #         1,
        #         1,
        #         QtWidgets.QSizePolicy.Policy.Expanding,
        #         QtWidgets.QSizePolicy.Policy.Expanding
        #     )
        # )

        # widgets signals
        self.pushButtonStart.clicked.connect(self.onPushButtonStartClicked)

    def onPushButtonStartClicked(self):
        self.timerThread.start()

class TimerThread(QtCore.QThread):

    def run(self) -> None:
        for i in range(10, 0, -1):
            print(i)
            time.sleep(1)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = MyApp()
    win.show()

    app.exec_()
