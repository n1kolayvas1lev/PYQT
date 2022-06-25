import time
import psutil
import requests
from requests.exceptions import MissingSchema
from PySide2 import QtCore, QtWidgets
from practice_form_design import Ui_Form


class QThreadPractice(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initThread()
        self.initUi()

    def initThread(self):
        # init threads
        self.timerThread = TimerThread()
        self.pingThread = PingThread()
        self.system_statusTread = SystemStatusThread()
        self.system_statusTread.start()


        # init timer threads signals
        self.timerThread.timerSignal.connect(self.timerThreadTimerSignal)
        self.timerThread.started.connect(self.timerThreadStarted)
        self.timerThread.finished.connect(self.timerThreadFinished)

        # init ping thread signals
        self.pingThread.pingSignal.connect(self.pingThreadSignal)
        self.pingThread.started.connect(self.pingThreadStarted)
        self.pingThread.finished.connect(self.pingThreadFinished)

        # init system status signals
        self.system_statusTread.sys_status.connect(self.system_check_timeoutSignal)
        self.ui.spinBoxSystemInfoDelay.valueChanged.connect(self.system_check_timeout)


    def initUi(self):
        # ui
        self.ui.pushButtonStopTimer.setEnabled(False)



        # signals
        self.ui.pushButtonStartTimer.clicked.connect(self.onPushButtonStartTimerClicked)
        self.ui.pushButtonStopTimer.clicked.connect(self.onPushButtonStopTimerClicked)

        self.ui.pushButtonUrlCheckStart.clicked.connect(self.onPushButtonUrlCheckStartClicked)
        self.ui.pushButtonUrlCheckStop.clicked.connect(self.onPushButtonUrlCheckStopClicked)

    # timerThread SLOTS
    def onPushButtonStartTimerClicked(self):
        self.timerThread.timerCount = self.ui.spinBoxTimerCount.value()
        self.timerThread.start()

    def onPushButtonStopTimerClicked(self):
        self.timerThread.status = False

    def timerThreadTimerSignal(self, emit_value):
        self.ui.lineEditTimerEnd.setText(emit_value)

    def timerThreadStarted(self):
        self.ui.pushButtonStartTimer.setEnabled(False)
        self.ui.pushButtonStopTimer.setEnabled(True)

    def timerThreadFinished(self):
        self.ui.pushButtonStartTimer.setEnabled(True)
        self.ui.pushButtonStopTimer.setEnabled(False)

    # PingThread slots

    def onPushButtonUrlCheckStartClicked(self):
        try:
            self.pingThread.url = self.ui.lineEditURL.text()
            self.pingThread.check_timer = self.ui.spinBoxUrlCheckTime.value()
            self.pingThread.start()
            print(self.ui.lineEditURL.text())
            print(self.ui.spinBoxUrlCheckTime.value())
        except MissingSchema:
            self.ui.lineEditURL.setText('')
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Поддерживаются только URL вида: "https://pypi.org"')

    def onPushButtonUrlCheckStopClicked(self):
        self.pingThread.status = False

    def pingThreadSignal(self, emit_value):
        self.ui.plainTextEditUrlCheckLog.appendPlainText(emit_value)

    def pingThreadStarted(self):
        self.ui.pushButtonUrlCheckStart.setEnabled(False)
        self.ui.spinBoxUrlCheckTime.setEnabled(False)
        self.ui.lineEditURL.setEnabled(False)
        self.ui.pushButtonUrlCheckStop.setEnabled(True)

    def pingThreadFinished(self):
        self.ui.pushButtonUrlCheckStart.setEnabled(True)
        self.ui.spinBoxUrlCheckTime.setEnabled(True)
        self.ui.lineEditURL.setEnabled(True)
        self.ui.pushButtonUrlCheckStop.setEnabled(True)

    # SystemCheck slots

    def system_check_timeout(self):
        self.system_statusTread.check_timer = self.ui.spinBoxSystemInfoDelay.value()

    def system_check_timeoutSignal(self, system_status):
        self.ui.progressBarCPU.setValue(system_status[0])
        self.ui.labelCPUPercent.setText(str(system_status[0]))
        self.ui.progressBarRAM.setValue(system_status[1])
        self.ui.labelRAMPercent.setText(str(system_status[1]))


class TimerThread(QtCore.QThread):
    timerSignal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.timerCount = None
        self.status = None

    def run(self):
        self.status = True

        if self.timerCount is None:
            self.timerCount = 10

        while self.status:
            if self.timerCount < 1:
                break

            time.sleep(1)
            self.timerCount -= 1
            self.timerSignal.emit(str(self.timerCount))


class PingThread(QtCore.QThread):  # https://pypi.org
    pingSignal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.check_timer = None
        self.status = None
        self.url = None

    def run(self):
        self.status = True
        while self.status:
            try:
                request = requests.get(self.url)
                emission = request.status_code
                self.pingSignal.emit(f'Url: {self.url}, response: {emission}, timeout: {self.check_timer}.')
                time.sleep(self.check_timer)
                # print(request.status_code, self.check_timer, self.url)
            except MissingSchema as err:
                self.pingSignal.emit(f'{err}')
                break


class SystemStatusThread(QtCore.QThread):
    sys_status = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.check_timer = None

    def run(self):
        if self.check_timer is None:
            self.check_timer = 1
        while True:
            cpu_usage = psutil.cpu_percent()
            ram_usage = psutil.virtual_memory()
            self.sys_status.emit([cpu_usage, ram_usage.percent])
            print(cpu_usage, ram_usage, self.check_timer)
            time.sleep(self.check_timer)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = QThreadPractice()
    myapp.show()

    app.exec_()
