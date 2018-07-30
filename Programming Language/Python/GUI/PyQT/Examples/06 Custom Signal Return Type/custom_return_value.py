# -*- coding: utf-8 -*-

import sys
import string
import time
import random

from PyQt5 import QtWidgets
from PyQt5 import QtCore


# OTP (One-Time Password)를 생성해준다.

class OTPGenerator(QtCore.QThread):
    value_changed = QtCore.pyqtSignal(str, name="ValueChanged")
    expires_in = QtCore.pyqtSignal(int, name="ExpiresIn")

    EXPIRE_TIME = 5

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.characters = list(string.ascii_uppercase)
        self.token = self.generate()

    def __del__(self):
        self.wait()

    def generate(self):
        random.shuffle(self.characters)
        return ''.join(self.characters[0:5])

    def run(self):
        self.value_changed.emit(self.token)  # 시작 후 첫 OTP 전달
        while True:  # emit = 전송
            t = int(time.time()) % self.EXPIRE_TIME
            self.expires_in.emit(self.EXPIRE_TIME - t)  # 남은 시간 전달
            if t != 0:
                self.usleep(1)
                continue
            # 변경된 토큰 값 전달
            self.token = self.generate()
            self.value_changed.emit(self.token)
            self.msleep(1000)


class Form(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self, flags=QtCore.Qt.Widget)
        self.lb_token = QtWidgets.QLabel()
        self.lb_expire_time = QtWidgets.QLabel()
        self.otp_gen = OTPGenerator()
        self.init_widget()
        self.otp_gen.start()  # 생성자 실행 후 OTP 생성 시작

    def init_widget(self):  # 위젯 초기화
        self.setWindowTitle("Custom Signal return type")
        form_lbx = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.TopToBottom, parent=self)  # 상하 정렬
        self.setLayout(form_lbx)

        # Connect Signal and Slot
        self.otp_gen.ValueChanged.connect(self.lb_token.setText)
        self.otp_gen.ExpiresIn.connect(lambda v: self.lb_expire_time.setText(str(v)))

        form_lbx.addWidget(self.lb_token)
        form_lbx.addWidget(self.lb_expire_time)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
