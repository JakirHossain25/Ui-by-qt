# first mathord #

from PySide6.QtWidgets import QApplication ,QMainWindow,QPushButton
import sys

# app=QApplication(sys.argv)
# window = QMainWindow()
# window.setWindowTitle("This is a fist windo")

# Button = QPushButton()
# Button.setText( "push Me")

# window.setCentralWidget(Button)

# window.show()
# app.exec()

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button hold app")

        button = QPushButton("press Me!")
        self.setCentralWidget(button)
        
app=QApplication(sys.argv)

window= ButtonHolder()
window.show()
app.exec()