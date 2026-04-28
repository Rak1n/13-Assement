from PySide6 import QtWidgets, QtCore
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



if __name__=="__main__":
    app = QtWidgets.QApplication([])
    ui = MainWindow()
    ui.show()
    app.exec()
