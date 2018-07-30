import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore

# dl = Dial
# sl = Slider

class Form(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self, flags=QtCore.Qt.Widget)
        self.dl = QtWidgets.QDial()
        self.sd = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Signal Slot")
        form_lbx = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)
        
        self.dl.valueChanged.connect(self.sd.setValue)
        self.sd.valueChanged.connect(self.dl.setValue)

        form_lbx.addWidget(self.dl)
        form_lbx.addWidget(self.sd)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
