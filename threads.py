import time
from PySide2 import QtCore, QtWidgets


class MyApp(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initThreads()

    def initThreads(self):
        """
        Метод инициализации потоков.
        :return:
        """
        self.timerThread = TimerThread()

    def initUi(self):
        """
        Метод инициализации пользовательского интерфейса
        :return:
        """
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
        """
        Метод-слот для отработки сигнала clicked виджета self.pbStart
        Запускает поток, в котором будет выполняться бэкенд.
        :return:
        """
        self.timerThread.timerCount = int(self.lineEditStart.text())
        self.timerThread.start()

class TimerThread(QtCore.QThread):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.timerCount = None

    def run(self) -> None:
        if self.timerCount is None:
            self.timerCount = 10

        for i in range(self.timerCount, 0, -1):
            print(i)
            time.sleep(1)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = MyApp()
    win.show()

    app.exec_()
