# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '07.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def __init__(self):
        self.cnt = 0
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 202)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(str(self.cnt))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.button = QtWidgets.QPushButton("Click")
        self.button.setObjectName("button")
        self.verticalLayout.addWidget(self.button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "테스트입니다"))
        self.label.setText(_translate("Dialog", "ㅎㅇ"))
        self.button.setText(_translate("Dialog", "눌러"))
        self.button.clicked.connect(self.count)

    @QtCore.pyqtSlot()
    def count(self):
        # pyqtSlot 데코레이터를 이용, 메소드를 Qt Slot으로 명시해야함.
        self.cnt = self.cnt + 1
        self.label.setText(str(self.cnt))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

