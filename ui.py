# first mathord #

from PySide6.QtWidgets import QApplication ,QMainWindow,QPushButton
import sys

app=QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("This is a fist windo")

Button = QPushButton()
Button.setText( "push Me")

window.setCentralWidget(Button)

window.show()
app.exec()