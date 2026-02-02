# Import modules
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

# main app objects and settings
App = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("This is class 1 UI part")
window.resize(300, 200)



# show and run
window.show()
App.exec_()
