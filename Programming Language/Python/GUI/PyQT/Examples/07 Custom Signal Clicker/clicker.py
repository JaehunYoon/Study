import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore

class Form(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self, flags=QtCore.Qt.Widget)
        self.cnt = 0
        self.lb = QtWidgets.QLabel(str(self.cnt))
        self.btn = QtWidgets.QPushButton("Click!")

        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Python Clicker")
        form_lbx = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)

        # Signal Slot connect
        self.btn.clicked.connect(self.count)

        form_lbx.addWidget(self.lb)
        form_lbx.addWidget(self.btn)

    @QtCore.pyqtSlot()
    def count(self):
        # pyqtSlot 데코레이터를 이용, 메소드를 Qt Slot으로 명시해야함.
        self.cnt = self.cnt + 1
        self.lb.setText(str(self.cnt))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
