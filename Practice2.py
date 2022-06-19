import sys
import time

import PySide2
from PySide2 import QtWidgets, QtCore, QtGui
from ui.Practice_2 import Ui_Form


class Practice2(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUi()

    def initUi(self):
        self.setWindowTitle('Practice_2')

        self.ui.pushButton_left_up.clicked.connect(self.left_up_clicked)
        self.ui.pushButton_left_down.clicked.connect(self.left_down_clicked)
        self.ui.pushButton_center.clicked.connect(self.center_clicked)
        self.ui.pushButton_right_up.clicked.connect(self.right_up_clicked)
        self.ui.pushButton_right_down.clicked.connect(self.right_down_clicked)
        self.ui.pushButton_get_wndw_data.clicked.connect(self.wndw_data_clicked)
        self.ui.dial.valueChanged.connect(self.dial)  #
        self.ui.horizontalSlider.valueChanged.connect(self.dial)

        self.ui.dial.installEventFilter(self)

    def left_up_clicked(self) -> None:
        """
        Нажатие кнопки перемещения окна в левый верхний угол экрана.
        :return: None
        """
        self.move(0, 0)

    def left_down_clicked(self) -> None:
        """
        Нажатие кнопки перемещения окна в левый нижний угол экрана.
        :return: None
        """
        self.move(0,
                  self.y_screen_center() * 2 - self.y_window_center() * 2)

    def center_clicked(self) -> None:
        """
        Нажатие кнопки перемещения окна в центр экрана.
        :return: None
        """
        print(QtWidgets.QApplication.primaryScreen().availableGeometry())
        self.move(self.x_screen_center() - self.x_window_center(),
                  self.y_screen_center() - self.y_window_center())

    def right_up_clicked(self) -> None:
        """
        Нажатие кнопки перемещения окна в правый верхний угол экрана.
        :return: None
        """
        self.move(self.x_screen_center() * 2 - self.x_window_center() * 2,
                  0)

    def right_down_clicked(self) -> None:
        """
        Нажатие кнопки перемещения окна в правый нижний угол экрана.
        :return: None
        """
        self.move(self.x_screen_center() * 2 - self.x_window_center() * 2,
                  self.y_screen_center() * 2 - self.y_window_center() * 2)

    def x_window_center(self) -> int:
        """
        Определение центра окна программы по оси Х.
        :return: int
        """
        window_width = self.size().width()
        x = window_width // 2
        return x

    def x_screen_center(self) -> int:
        """
        Определение центра экрана по оси Х.
        :return: int
        """
        screen = QtWidgets.QApplication.primaryScreen().size().width()
        available_screen = QtWidgets.QApplication.primaryScreen().availableGeometry().width()
        if available_screen < screen:
            taskbar = available_screen - screen
            x = screen // 2 - taskbar
        else:
            x = screen // 2
        return x

    def y_window_center(self) -> int:
        """
        Определение центра окна программы по оси Y.
        :return: int
        """
        window_height = self.size().height()
        y = int(window_height / 2)
        return y

    def y_screen_center(self) -> int:
        """
        Определение центра экрана по оси Y.
        :return: int
        """
        screen = QtWidgets.QApplication.primaryScreen().size().height()
        available_screen = QtWidgets.QApplication.primaryScreen().availableGeometry().height()
        if available_screen < screen:
            taskbar = available_screen - screen
            y = screen // 2 - taskbar
        else:
            y = screen // 2
        return y

    # def x_coordinate(self):
    #     screen_width = QtWidgets.QApplication.primaryScreen().size().width()
    #     window_width = self.size().width()
    #     x = int(screen_width / 2 - window_width / 2)
    #     return x

    # def y_coordinate(self):
    #     screen_height = QtWidgets.QApplication.primaryScreen().size().height()
    #     window_height = self.size().height()
    #     y = int(screen_height / 2 - window_height / 2)
    #     return y

    def wndw_data_clicked(self) -> None:
        """
        Вывод на экран по нажатию кнопки получения данных об окне.
        :return: None
        """
        screen_counter = len(QtWidgets.QApplication.screens())
        primary_screen = QtWidgets.QApplication.primaryScreen().name()
        primary_screen_resolution = f'{QtWidgets.QApplication.primaryScreen().size().width()}' \
                                    f' x {QtWidgets.QApplication.primaryScreen().size().height()}'
        screen_name = QtWidgets.QApplication.screenAt(self.pos()).name()
        window_width = self.size().width()
        window_height = self.size().height()
        # screen_height = QtWidgets.QApplication.primaryScreen().availableGeometry().height()
        window_min_width = self.minimumWidth()
        window_min_height = self.minimumHeight()
        x = self.pos().x()
        y = self.pos().y()
        self.ui.plainTextEdit.appendPlainText(f'Кол-во экранов: {screen_counter}' 
                                              f'Текущее основное окно: {primary_screen}'
                                              f'Разрешение экрана: {primary_screen_resolution}'
                                              f'На каком экране окно находится: {screen_name}'
                                              f'Размеры окна: {window_width} x {window_height}'
                                              f'Минимальные размеры окна: {window_min_height} x {window_min_width}'
                                              f'Текущее положение (координаты) окна: x: {x} y: {y}'
                                              f'Координаты центра приложения: x: {self.pos().x() + self.width()/2} '
                                              f'y: {self.pos().y() + self.height()/2}')

    def changeEvent(self, event: PySide2.QtCore.QEvent) -> None:
        """
        Отслеживание состояния окна программы с выводом информации о текущем состоянии.
        :param event: Qt’s main event loop ( exec() ) fetches native window system events from the event queue,
                translates them into QEvents, and sends the translated events to QObject s.
        :return: None
        """
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.isMinimized():
                self.ui.plainTextEdit.appendPlainText(f'{time.ctime()}: Окно свёрнуто.')
            if self.isMaximized():
                self.ui.plainTextEdit.appendPlainText(f'{time.ctime()}: Окно развёрнуто.')
            if self.isHidden():
                self.ui.plainTextEdit.appendPlainText(f'{time.ctime()}: Окно спрятано.')
            if self.isActiveWindow():
                self.ui.plainTextEdit.appendPlainText(f'{time.ctime()}: Окно активно.')
            if self.isVisible():
                self.ui.plainTextEdit.appendPlainText(f'{time.ctime()}: Окно видимо.')

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        """
        Вывод координат окна в терминал.
        :param event:
        :return:
        """
        print(self.pos())

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """
        Вывод информации о размерах при изменении размера окна.
        :param event:
        :return:
        """
        print(self.size())

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        print(event.text(), event.key())

    def dial(self) -> None:
        """
        Dial вариация Horizontal slider, при изменении занчения горизонтального слайдера меняется,
        в данном случае, значение диала и наоборот. Значение выводится на 'ЛСД' дисплей.
        :return: None
        """
        if self.sender().objectName() == "dial":
            value = self.ui.dial.value()
            self.ui.horizontalSlider.setValue(value)

        elif self.sender().objectName() == "horizontalSlider":
            value = self.ui.horizontalSlider.value()
            self.ui.dial.setValue(value)

        self.ui.lcdNumber.display(value)

    def changeLCDview(self) -> None:
        """
        Смена отображения на дисплее в различных системах счсления.
        :return: None
        """
        a = {"HEX": self.ui.lcdNumber.setHexMode, "BIN": self.ui.lcdNumber.setBinMode,
             "OCT": self.ui.lcdNumber.setOctMode, "DEC": self.ui.lcdNumber.setDecMode}

        a[self.ui.comboBox.currentText()]()
        print(self.ui.lcdNumber.mode())

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        """
        Изменение состояния диала и горизонтального слайдера при нажатии + и -
        :param watched: отслеживание события
        :param event: событие (нажатие + и -)
        :return:
        """
        if watched == self.ui.dial and event.type() == QtCore.QEvent.KeyPress:
            if event.text() == "+":
                self.ui.dial.setValue(self.ui.dial.value()+1)
            if event.text() == "-":
                self.ui.dial.setValue(self.ui.dial.value()-1)

            self.ui.plainTextEdit.appendPlainText(f"dial value {self.ui.dial.value()}")
        return super(Practice2, self).eventFilter(watched, event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создаем  объект приложения
    # app = QtWidgets.QApplication(sys.argv)  # Если PyQt

    myWindow = Practice2()  # Создаём объект окна
    myWindow.show()  # Показываем окно

    sys.exit(app.exec_())  # Если exit, то код дальше не исполняется