# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        Form.setMinimumSize(QtCore.QSize(500, 500))
        Form.setMaximumSize(QtCore.QSize(500, 500))
        Form.setStyleSheet("QWidget#Form1{\n"
"    border-image: url(:/register/images/register_backgroud.PNG);\n"
"}\n"
"QWidget#Form{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(90, 30, 311, 451))
        self.widget.setObjectName("widget")
        self.register_btn = QtWidgets.QPushButton(self.widget)
        self.register_btn.setEnabled(False)
        self.register_btn.setGeometry(QtCore.QRect(10, 346, 281, 40))
        self.register_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.register_btn.setStyleSheet("QPushButton{    \n"
"    background-color:rgb(0, 0, 0);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:15px\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color:rgb(30, 30, 30);\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background-color:rgb(60, 60, 60);\n"
"}\n"
"QPushButton:disabled{\n"
"    \n"
"    background-color:rgb(100, 100, 100);\n"
"}")
        self.register_btn.setObjectName("register_btn")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 158, 64, 33))
        self.label.setStyleSheet("font: 10pt \"宋体\";")
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.password_le = QtWidgets.QLineEdit(self.widget)
        self.password_le.setGeometry(QtCore.QRect(83, 200, 195, 33))
        self.password_le.setMinimumSize(QtCore.QSize(0, 30))
        self.password_le.setStyleSheet("background-color:transparent;\n"
"color:rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid lightgrey;\n"
"font-size:13px")
        self.password_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_le.setObjectName("password_le")
        self.acount_le = QtWidgets.QLineEdit(self.widget)
        self.acount_le.setGeometry(QtCore.QRect(82, 158, 195, 33))
        self.acount_le.setMinimumSize(QtCore.QSize(0, 30))
        self.acount_le.setStyleSheet("background-color:transparent;\n"
"color:rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid lightgrey;\n"
"font-size:13")
        self.acount_le.setObjectName("acount_le")
        self.confirm_pwd_le = QtWidgets.QLineEdit(self.widget)
        self.confirm_pwd_le.setGeometry(QtCore.QRect(83, 246, 195, 33))
        self.confirm_pwd_le.setMinimumSize(QtCore.QSize(0, 30))
        self.confirm_pwd_le.setStyleSheet("background-color:transparent;\n"
"color:rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid lightgrey;\n"
"font-size:13")
        self.confirm_pwd_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_pwd_le.setObjectName("confirm_pwd_le")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 202, 64, 33))
        self.label_2.setStyleSheet("font: 10pt \"宋体\";")
        self.label_2.setIndent(-1)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 247, 62, 33))
        self.label_3.setStyleSheet("font: 10pt \"宋体\";")
        self.label_3.setIndent(-1)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 292, 62, 33))
        self.label_4.setStyleSheet("font: 10pt \"宋体\";")
        self.label_4.setIndent(-1)
        self.label_4.setObjectName("label_4")
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_name.setGeometry(QtCore.QRect(83, 289, 91, 33))
        self.lineEdit_name.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_name.setStyleSheet("background-color:transparent;\n"
"color:rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid lightgrey;\n"
"font-size:13px")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setGeometry(QtCore.QRect(240, 300, 35, 16))
        self.checkBox_2.setAutoExclusive(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 62, 33))
        self.label_5.setStyleSheet("font: 10pt \"宋体\";")
        self.label_5.setIndent(-1)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 59, 62, 33))
        self.label_6.setStyleSheet("font: 10pt \"宋体\";")
        self.label_6.setIndent(-1)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(9, 111, 62, 33))
        self.label_7.setStyleSheet("font: 10pt \"宋体\";")
        self.label_7.setIndent(-1)
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(80, 7, 191, 30))
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox.setEditable(True)
        self.comboBox.setMaxVisibleItems(3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 59, 191, 30))
        self.comboBox_2.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setMaxVisibleItems(3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setGeometry(QtCore.QRect(79, 111, 191, 30))
        self.comboBox_3.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setMaxVisibleItems(3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(190, 300, 35, 16))
        self.checkBox.setAutoExclusive(True)
        self.checkBox.setObjectName("checkBox")
        self.register_btn_2 = QtWidgets.QPushButton(self.widget)
        self.register_btn_2.setEnabled(True)
        self.register_btn_2.setGeometry(QtCore.QRect(10, 400, 281, 40))
        self.register_btn_2.setMinimumSize(QtCore.QSize(0, 30))
        self.register_btn_2.setStyleSheet("QPushButton{    \n"
"    background-color:rgb(0, 0, 0);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:15px\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color:rgb(30, 30, 30);\n"
"}\n"
"\n"
"QPushButton:pressed{    \n"
"    background-color:rgb(60, 60, 60);\n"
"}\n"
"QPushButton:disabled{\n"
"    \n"
"    background-color:rgb(100, 100, 100);\n"
"}")
        self.register_btn_2.setObjectName("register_btn_2")
        self.label.setBuddy(self.acount_le)
        self.label_2.setBuddy(self.password_le)
        self.label_3.setBuddy(self.confirm_pwd_le)
        self.label_4.setBuddy(self.lineEdit_name)
        self.label_5.setBuddy(self.comboBox)
        self.label_6.setBuddy(self.comboBox_2)
        self.label_7.setBuddy(self.comboBox_3)

        self.retranslateUi(Form)
        self.register_btn.clicked.connect(Form.register_clicked)
        self.acount_le.textChanged['QString'].connect(Form.input_changed)
        self.password_le.textChanged['QString'].connect(Form.input_changed)
        self.confirm_pwd_le.textChanged['QString'].connect(Form.input_changed)
        self.checkBox.clicked.connect(Form.sex_changed)
        self.checkBox_2.clicked.connect(Form.sex_changed)
        self.comboBox.currentTextChanged['QString'].connect(Form.dan1_changed)
        self.comboBox_2.currentTextChanged['QString'].connect(Form.dan2_changed)
        self.lineEdit_name.textChanged['QString'].connect(Form.input_changed)
        self.acount_le.textChanged['QString'].connect(Form.input_changed)
        self.register_btn_2.clicked.connect(Form.exit_clicked)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.comboBox, self.comboBox_2)
        Form.setTabOrder(self.comboBox_2, self.comboBox_3)
        Form.setTabOrder(self.comboBox_3, self.acount_le)
        Form.setTabOrder(self.acount_le, self.password_le)
        Form.setTabOrder(self.password_le, self.confirm_pwd_le)
        Form.setTabOrder(self.confirm_pwd_le, self.lineEdit_name)
        Form.setTabOrder(self.lineEdit_name, self.checkBox)
        Form.setTabOrder(self.checkBox, self.checkBox_2)
        Form.setTabOrder(self.checkBox_2, self.register_btn)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.register_btn.setText(_translate("Form", "注  册"))
        self.label.setText(_translate("Form", "账    号"))
        self.password_le.setPlaceholderText(_translate("Form", "请输入密码"))
        self.acount_le.setPlaceholderText(_translate("Form", "请输入账户名"))
        self.confirm_pwd_le.setPlaceholderText(_translate("Form", "请确认密码"))
        self.label_2.setText(_translate("Form", "密    码"))
        self.label_3.setText(_translate("Form", "确认密码"))
        self.label_4.setText(_translate("Form", "姓　　名"))
        self.lineEdit_name.setPlaceholderText(_translate("Form", "请输入姓名"))
        self.checkBox_2.setText(_translate("Form", "女"))
        self.label_5.setText(_translate("Form", "一级单位"))
        self.label_6.setText(_translate("Form", "二级单位"))
        self.label_7.setText(_translate("Form", "三级单位"))
        self.checkBox.setText(_translate("Form", "男"))
        self.register_btn_2.setText(_translate("Form", "取  消"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
