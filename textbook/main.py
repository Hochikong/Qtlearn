import sys

from PyQt5 import QtWidgets

# when you run you should delete the . before textb
from textb import Ui_MainWindow
from dialog import Ui_Dialog


class MyApp:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)

        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)

        self.dialog = QtWidgets.QDialog()
        self.dialog_ui = Ui_Dialog()
        self.dialog_ui.setupUi(self.dialog)

        self.ui.textEdit.textChanged.connect(self.auto_save)
        self.ui.actionOpen.triggered.connect(self.on_open_click)
        self.ui.actionSave.triggered.connect(self.on_save_click)
        self.ui.actionNew.triggered.connect(self.on_new_click)

        self.main_window.show()
        sys.exit(self.app.exec_())

    def show_dialog(self):
        self.dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(self.dialog)
        self.dialog.show()

        rsp = self.dialog.exec_()
        if rsp == QtWidgets.QDialog.finished:
            self.on_new_click()

    def change_window_title(self, new_title):
        self.main_window.setWindowTitle(new_title)

    # def alert(self, content):
    #     msg = QtWidgets.QMessageBox()
    #     msg.setIcon(QtWidgets.QMessageBox.Warning)
    #     msg.setWindowTitle('Something wrong')
    #     msg.setText("An error have occured.")
    #     msg.setDetailedText(content)
    #     msg.exec_()

    def dialog_alert(self, content):
        self.dialog_ui.label.setText(content)
        self.dialog_ui.pushButton.clicked.connect(self.dialog.close)

        self.dialog.show()
        self.dialog.exec_()

    @staticmethod
    def write_file(filename, content):
        with open(filename, 'w') as f:
            f.write(content)

    def auto_save(self):
        self.write_file('tmp.txt', self.ui.textEdit.toPlainText())

    def on_open_click(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(parent=None, caption='Open file', directory='D:\\',
                                                      filter="Text files (*.txt);;"
                                                             "Yaml files (*.yaml);;"
                                                             "csv files (*.csv);;"
                                                             "Json files (*.json);;"
                                                             "All files (*)")
        if len(fname[0]) > 1:
            try:
                with open(fname[0], 'r') as f1:
                    self.ui.textEdit.setText(f1.read())
                self.change_window_title(fname[0])
            except Exception as e:
                self.dialog_alert(str(e))
                self.on_new_click()
        else:
            pass

    def on_save_click(self):
        fname = QtWidgets.QFileDialog.getSaveFileName(parent=None, caption='Save file', directory='D:\\',
                                                      filter="Text files (*.txt);;"
                                                             "Yaml files (*.yaml);;"
                                                             "csv files (*.csv);;"
                                                             "Json files (*.json);;"
                                                             "All files (*)")
        if len(fname[0]) > 1:
            self.write_file(fname[0], self.ui.textEdit.toPlainText())
            self.change_window_title(fname[0])
        else:
            pass

    def on_new_click(self):
        self.ui.textEdit.clear()
        self.change_window_title("Empty file")


if __name__ == '__main__':
    MyApp()
