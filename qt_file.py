from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from directory_script import directory_script
from PIL import Image
# import _pickle

class Ui_Import_data(object):
    def browse_data1(self):
        data_path=QtWidgets.QFileDialog.getExistingDirectory(None,'Select a folder',r"D:\Programming")
        
        if data_path != '':
        
            directory_script(data_path)
        
    def setupUi(self, Import_data):
        Import_data.setWindowIcon(QtGui.QIcon('flagofCuba_6551.png'))
        
        
        Import_data.setObjectName("Import_data")
        Import_data.resize(640, 640)
        self.pushButton = QtWidgets.QPushButton(Import_data)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 640, 640))
        
        self.pushButton.setMask(QtGui.QRegion(self.pushButton.rect(), QtGui.QRegion.Ellipse))
        
        self.pushButton.setStyleSheet('''border-image: url("upload-1118929_1280.webp");''')
        
        self.retranslateUi(Import_data)

        self.pushButton.clicked.connect(self.browse_data1)
        
        QtCore.QMetaObject.connectSlotsByName(Import_data)

    def retranslateUi(self, Import_data):
        _translate = QtCore.QCoreApplication.translate
        Import_data.setWindowTitle(_translate("Import_data", "Image Converter"))
        self.pushButton.setText(_translate("Import_data", ""))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Import_data = QtWidgets.QDialog()
    ui = Ui_Import_data()
    ui.setupUi(Import_data)
    Import_data.show()
    sys.exit(app.exec_())
