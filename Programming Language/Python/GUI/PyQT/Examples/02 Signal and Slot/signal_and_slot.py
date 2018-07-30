# coding: utf-8

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("02.ui", self)
        self.ui.show()

    @QtCore.pyqtSlot()
    def slot_1st(self):
        self.ui.label.setText("1")

    @QtCore.pyqtSlot()
    def slot_2nd(self):
        self.ui.label.setText("2")

    @QtCore.pyqtSlot()
    def slot_3rd(self):
        self.ui.label.setText("3")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())


'''
Signal과 Slot은 위젯끼리 통신을 하는 용도로 사용할 수 있습니다.
어떠한 이벤트가 일어났을때 그것을 다른 오브젝트에게 알려주고 값을 전달하거나 받을 수 있도록 해줍니다.
콜백 함수등을 이용하는 다른 GUI 프레임웍과 비교되는 통신 방법으로 Qt의 강점이라 할 수 있습니다.

QObject 를 상속받은 모든 위젯은 Signal과 Slot을 가질 수 있습니다.
'''