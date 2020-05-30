# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_login_background = QtWidgets.QLabel(self.widget)
        self.label_login_background.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_login_background.setText("")
        self.label_login_background.setObjectName("label_login_background")
        self.horizontalLayout_2.addWidget(self.label_login_background)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(5, 0, 5, 10)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setContentsMargins(10, 0, 10, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox.setMinimumSize(QtCore.QSize(0, 40))
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_2.setMinimumSize(QtCore.QSize(0, 40))
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 2, 1, 1, 1, QtCore.Qt.AlignTop)
        self.comboBox = QtWidgets.QComboBox(self.widget_3)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border:none;\n"
"    font-size:13px;\n"
"    border-bottom:1px solid lightgrey;\n"
"    background-color:transparent;\n"
"}\n"
"QComboBox:hover {\n"
"    border-bottom:1px solid gray;\n"
"}\n"
"QComboBox:focus {\n"
"    border-bottom:1px solid rgb(0, 255, 255);\n"
"}\n"
"QComboBox:drop-down {\n"
"    background-color:transparent;\n"
"    width:30px;\n"
"    height:40px;\n"
"}\n"
"QComboBox:down-arrow {    \n"
"    image: url(:/login/images/arrow_down.png);\n"
"    width:60px;\n"
"    height:28px;\n"
"}\n"
"QComboBox QAbstractItemView {    \n"
"    min-height:100px;\n"
"}\n"
"QComboBox QAbstractItemView:item {    \n"
"    color:rgb(255, 255, 0);\n"
"}")
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_3.setStyleSheet("QPushButton{    \n"
"    background-color:rgb(0, 0, 0);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:15px;\n"
"    spacing:20px\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color:rgb(60, 60, 60);\n"
"}\n"
"QPushButton:disabled{\n"
"    \n"
"    background-color:rgb(100, 100, 100);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/login/images/safe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border:none;\n"
"    font-size:13px;\n"
"    border-bottom:1px solid lightgrey;\n"
"    background-color:transparent;\n"
"}\n"
"QLineEdit:hover {\n"
"    border-bottom:1px solid gray;\n"
"}\n"
"QLineEdit:focus {\n"
"    border-bottom:1px solid rgb(0, 255, 255);\n"
"}")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)
        self.gridLayout.setRowMinimumHeight(0, 1)
        self.gridLayout.setRowMinimumHeight(1, 1)
        self.gridLayout.setRowMinimumHeight(2, 1)
        self.gridLayout.setRowMinimumHeight(3, 1)
        self.horizontalLayout.addWidget(self.widget_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_2.setMaximumSize(QtCore.QSize(80, 80))
        self.pushButton_2.setStyleSheet("border-image: url(:/login/images/wechat.jpg);")
        self.pushButton_2.setText("")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 3)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.register_clicked)
        self.comboBox.editTextChanged['QString'].connect(Form.enable_login_btn)
        self.lineEdit.textChanged['QString'].connect(Form.enable_login_btn)
        self.pushButton_3.clicked.connect(Form.check_login)
        self.checkBox.clicked['bool'].connect(Form.auto_login)
        self.checkBox_2.clicked['bool'].connect(Form.remenber_pwd)
        self.comboBox.currentTextChanged['QString'].connect(Form.clean_pwd)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "注册账号"))
        self.checkBox.setText(_translate("Form", "自动登陆"))
        self.checkBox_2.setText(_translate("Form", "记住密码"))
        self.pushButton_3.setText(_translate("Form", "安全登陆"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
