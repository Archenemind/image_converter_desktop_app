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
        
    def show_image(self):
        im=QtWidgets.QFileDialog.getOpenFileName(None,'Select a file',r"D:\Programming")
        
        image_path = str(im[0])
        
        if image_path.endswith (('.jpg','.png','.avif','.webp')):
        
            im = Image.open(rf'{image_path}')
            im.show()
            
        else:
            self.message = QMessageBox()
            self.message.setIcon(QMessageBox.Icon.Warning)
            self.message.setText('This is not an image')          
            self.message.show()
            
        # with open('data_path.pickle', 'wb') as handle:
        #     _pickle.dump(data_path,handle,protocol=_pickle.HIGHEST_PROTOCOL)

    def setupUi(self, Import_data):
        Import_data.setWindowIcon(QtGui.QIcon('flagofCuba_6551.png'))
        
        
        Import_data.setObjectName("Import_data")
        Import_data.resize(704, 131)
        self.pushButton = QtWidgets.QPushButton(Import_data)
        self.pushButton.setGeometry(QtCore.QRect(600, 20, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Import_data)
        self.label.setGeometry(QtCore.QRect(10, 50, 100, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Import_data)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Import_data)
        self.lineEdit.setGeometry(QtCore.QRect(140, 20, 441, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Import_data)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 50, 441, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(Import_data)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 50, 81, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Import_data)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 100, 81, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.retranslateUi(Import_data)

        self.pushButton.clicked.connect(self.browse_data1)
        self.pushButton_2.clicked.connect(self.show_image)
        QtCore.QMetaObject.connectSlotsByName(Import_data)

    def retranslateUi(self, Import_data):
        _translate = QtCore.QCoreApplication.translate
        Import_data.setWindowTitle(_translate("Import_data", "Image Converter"))
        self.pushButton.setText(_translate("Import_data", "Browse"))
        self.label.setText(_translate("Import_data", "Display Image"))
        self.label_2.setText(_translate("Import_data", "Browse the folder"))
        self.pushButton_2.setText(_translate("Import_data", "Show"))
        self.pushButton_3.setText(_translate("Import_data", "OK"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Import_data = QtWidgets.QDialog()
    ui = Ui_Import_data()
    ui.setupUi(Import_data)
    Import_data.show()
    sys.exit(app.exec_())
