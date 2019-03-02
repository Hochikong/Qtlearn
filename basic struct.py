import sys
from PyQt5.QtWidgets import QApplication, QWidget

# create app
app = QApplication(sys.argv)

# create window
win = QWidget()

# set properties
win.setWindowTitle('Basic')

# show
win.show()

# catch exceptions and run
sys.exit(app.exec_())
