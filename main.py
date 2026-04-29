from PySide6 import QtWidgets, QtCore, QtGui
from PIL import Image


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #self.resize(800,600)
        self.setMinimumSize(QtCore.QSize(600,400))
        self.setMaximumSize(QtCore.QSize(800,600))
        self.setWindowTitle("MRGS Tuck Shop")
        self.setWindowOpacity(1)
        self.setStyleSheet("background-color: black")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Falcon.png"))
        self.setWindowIcon(icon)


if __name__=="__main__":
    app = QtWidgets.QApplication([])
    app.setApplicationName("Riri's App")
    app.setApplicationVersion("v1")
    app.setApplicationDisplayName(f"{app.applicationName()} - {app.applicationVersion()}")
    ui = MainWindow()
    ui.show()
    app.exec()

