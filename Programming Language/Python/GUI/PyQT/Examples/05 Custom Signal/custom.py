import sys
import time

from PyQt5 import QtWidgets
from PyQt5 import QtCore

class TicGenerator(QtCore.QThread):
    # Custom Signal
    # Call Tic Signal

    tic = QtCore.pyqtSignal(name="Tic")

    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            t = int(time.time())
            if not t % 5 == 0:  # 5초마다 tic 발생
                self.usleep(1)  # micro second?
                continue
            self.Tic.emit()
            self.msleep(1000)  # called process is sleeping. cannot interrupt.

class Form(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self, flags=QtCore.Qt.Widget)
        self.text = QtWidgets.QTextEdit()
        self.tic_gen = TicGenerator()
        self.init_widget()
        self.tic_gen.start()

    def init_widget(self):  # 위젯 초기 설정
        self.setWindowTitle("Custom Signal")
        form_lbx = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.TopToBottom, parent=self)  # 레이아웃 상하 정렬
        self.setLayout(form_lbx)

        self.tic_gen.Tic.connect(lambda: self.text.insertPlainText(time.strftime("[%H:%M:%S] Tic!\n")))  # Print Plain Text

        form_lbx.addWidget(self.text)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
