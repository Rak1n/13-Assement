from tkinter.ttk import tclobjs_to_py

from PySide6 import QtWidgets, QtCore, QtGui
from PIL import Image
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #self.resize(800,600)
        self.setMinimumSize(QtCore.QSize(600,400))
        self.setMaximumSize(QtCore.QSize(800,600))
        self.setWindowTitle("MRGS Tuck Shop")
        self.setWindowOpacity(1)
        self.setStyleSheet("background-color: #cc3628")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Falcon.png"))
        self.setWindowIcon(icon)
        self.label = QtWidgets.QLabel("MRGS Tuck", self)
        self.label.setObjectName("label")
        print(self.label.objectName())
        self.label.setGeometry(QtCore.QRect(270,20,70,50)) #100 from the left ,200 from the top,width 300,height 200
        self.label.setStyleSheet("background-color: blue;""color: black")
        self.label2 = QtWidgets.QLabel("ko", self)
        self.label2.setObjectName("l")
        print(self.label2.objectName())
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("Riri's App")
    app.setApplicationVersion("v1")
    app.setApplicationDisplayName(f"{app.applicationName()} - {app.applicationVersion()}")
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec())

