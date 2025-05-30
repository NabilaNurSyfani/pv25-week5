# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'week5.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import re
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(520, 457) 
        MainWindow.setWindowTitle("Form Validation")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 20, 440, 350))

        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(10)

        # Name
        self.label = QtWidgets.QLabel("Name:")
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setFixedSize(200, 25)
        self.formLayout.addRow(self.label, self.lineEdit)

        # Email
        self.label_2 = QtWidgets.QLabel("Email:")
        self.lineEdit_2 = QtWidgets.QLineEdit()
        self.lineEdit_2.setFixedSize(200, 25)
        self.formLayout.addRow(self.label_2, self.lineEdit_2)

        # Age
        self.label_3 = QtWidgets.QLabel("Age:")
        self.lineEdit_3 = QtWidgets.QLineEdit()
        self.lineEdit_3.setFixedSize(200, 25)
        self.formLayout.addRow(self.label_3, self.lineEdit_3)

        # Phone
        self.label_4 = QtWidgets.QLabel("Phone Number:")
        self.lineEdit_4 = QtWidgets.QLineEdit()
        self.lineEdit_4.setText("+62 ")
        self.lineEdit_4.setFixedSize(200, 25)
        self.formLayout.addRow(self.label_4, self.lineEdit_4)

        # Address
        self.label_5 = QtWidgets.QLabel("Address:")
        self.textEdit = QtWidgets.QTextEdit()
        self.textEdit.setFixedSize(300, 120)
        self.formLayout.addRow(self.label_5, self.textEdit)

        # Gender
        self.label_6 = QtWidgets.QLabel("Gender:")
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItems(["", "Male", "Female"])
        self.comboBox.setFixedSize(100, 25)
        self.formLayout.addRow(self.label_6, self.comboBox)

        self.label8 = QtWidgets.QLabel("Nabila Nur Syfani (F1D022082)", self.centralwidget)
        self.label8.setGeometry(QtCore.QRect(170, 438, 300, 20))
        self.label8.setStyleSheet("font-size: 7pt;")

        # Education
        self.label_7 = QtWidgets.QLabel("Education:")
        self.comboBox_2 = QtWidgets.QComboBox()
        self.comboBox_2.addItems(["", "Elementary School","Junior High School", "Senior High School", "Diploma", "Bachelor's Degree", "Master's Degree", "Doctoral Degree"])
        self.comboBox_2.setFixedSize(150, 25)
        self.formLayout.addRow(self.label_7, self.comboBox_2)

        # Tombol button untuk save dan clear
        self.pushButton = QtWidgets.QPushButton("Save", self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(125, 390, 100, 30))

        self.pushButton_2 = QtWidgets.QPushButton("Clear", self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(275, 390, 100, 30))

        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.saveData)
        self.pushButton_2.clicked.connect(self.clearForm)
        self.lineEdit_4.textChanged.connect(self.formatPhoneNumber)

        # Shortcut Q
        quit_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Q"), MainWindow)
        quit_shortcut.activated.connect(MainWindow.close)

    def formatPhoneNumber(self, text):
        if not text.startswith("+62"):
            self.lineEdit_4.setText("+62 ")
            return

        cursor_pos = self.lineEdit_4.cursorPosition()

        raw_number = re.sub(r"[^\d]", "", text.replace("+62", "", 1))
        raw_number = raw_number[:11] 
        before_format = text

        if len(raw_number) >= 3:
            formatted = f"+62 {raw_number[:3]}"
            if len(raw_number) >= 7:
                formatted += f" {raw_number[3:7]}"
                if len(raw_number) > 7:
                    formatted += f" {raw_number[7:]}"
            else:
                formatted += f" {raw_number[3:]}"
        else:
            formatted = f"+62 {raw_number}"

        diff = len(formatted) - len(before_format)

        self.lineEdit_4.blockSignals(True)
        self.lineEdit_4.setText(formatted)
        self.lineEdit_4.blockSignals(False)

        new_pos = max(0, cursor_pos + diff)
        self.lineEdit_4.setCursorPosition(new_pos)

    def saveData(self):
        name = self.lineEdit.text()
        email = self.lineEdit_2.text()
        age = self.lineEdit_3.text()
        phone = self.lineEdit_4.text()
        address = self.textEdit.toPlainText()
        gender = self.comboBox.currentText()
        education = self.comboBox_2.currentText()

        # Validasi kosong
        if name == "" or email == "" or age == "" or phone.strip() == "+62" or address == "" or gender == "" or education == "":
            QtWidgets.QMessageBox.warning(None, "Error", "All fields are required.")
            return
        
        # Validasi nama 
        if any(char.isdigit() for char in name):
            QtWidgets.QMessageBox.warning(None, "Error", "Please enter a valid name (name cannot contain numbers).")
            return
        
        # Validasi email
        if not email.endswith("@gmail.com"):
            QtWidgets.QMessageBox.warning(None, "Error", "Please enter a valid email address (@gmail.com).")
            return
        
        # Validasi age 
        if not age.isdigit():
            QtWidgets.QMessageBox.warning(None, "Error", "Please enter a valid age (integer value).")
            return

        # Validasi phone number
        digits_only = re.sub(r"[^\d]", "", phone.replace("+62", "", 1))
        if len(digits_only) < 11:
            QtWidgets.QMessageBox.warning(None, "Error", "Please enter a valid 13 digit Phone number.")
            return

        # Validasi semua valid
        QtWidgets.QMessageBox.information(None, "Success", "Profile saved succesfully")
        self.clearForm()

    def clearForm(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.setText("+62 ")
        self.textEdit.clear()
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
