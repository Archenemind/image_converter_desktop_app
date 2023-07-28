import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Folder import FilesPath


class Ui_Import_data():
    """GUI class"""

    def browse_data(self):
        data_path = QtWidgets.QFileDialog.getExistingDirectory(
            None, 'Select a folder', r"D:\Programming")

        if data_path != '':

            folder = FilesPath(data_path)
            folder.create_folders()
            folder.create_images()
            del folder

    def setupUi(self, Import_data):
        """Window function"""
        Import_data.setWindowIcon(QtGui.QIcon('flagofCuba_6551.png'))
        Import_data.setStyleSheet('''background-color: grey;''')

        Import_data.setObjectName("Import_data")
        Import_data.resize(640, 640)
        self.pushButton = QtWidgets.QPushButton(Import_data)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 640, 640))

        self.pushButton.setStyleSheet(
            '''border-image: url("upload-1118929_1280.webp");''')

        self.retranslateUi(Import_data)

        self.pushButton.clicked.connect(self.browse_data)

    def retranslateUi(self, Import_data):
        """Changes the window name"""
        _translate = QtCore.QCoreApplication.translate
        Import_data.setWindowTitle(_translate(
            "Import_data", "Image Converter"))
        self.pushButton.setText(_translate("Import_data", ""))


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Import_data = QtWidgets.QDialog()
    ui = Ui_Import_data()
    ui.setupUi(Import_data)
    Import_data.show()
    sys.exit(app.exec_())
