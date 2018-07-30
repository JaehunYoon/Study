import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

class Form(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self, flags=QtCore.Qt.Widget)
        self.lb = QtWidgets.QLabel()
        self.sd = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Signal and Slot with Lambda")
        form_lbx = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)

        # QtWidgets.QLabel.setText() : only get string.
        # 정수형을 주는 QtWidgets.QSlider.valueChange() 를 바로 사용할 수 없다.
        # 해결 방법 : lambda를 이용하여 값을 넘겨주는 방식.

        self.sd.valueChanged.connect(lambda v: self.lb.setText(str(v)))

        form_lbx.addWidget(self.lb)
        form_lbx.addWidget(self.sd)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
