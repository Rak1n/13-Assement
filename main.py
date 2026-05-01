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
        self.label.setGeometry(200,100,300,200)


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("Riri's App")
    app.setApplicationVersion("v1")
    app.setApplicationDisplayName(f"{app.applicationName()} - {app.applicationVersion()}")
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec())

