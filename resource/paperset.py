# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paperset.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(600, 400))
        Form.setMaximumSize(QtCore.QSize(600, 400))
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(120, 50, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 100, 161, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 50, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 54, 12))
        self.label_2.setObjectName("label_2")
        self.lineEdit_num_1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_num_1.setGeometry(QtCore.QRect(359, 40, 50, 20))
        self.lineEdit_num_1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_num_1.setObjectName("lineEdit_num_1")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(317, 44, 54, 12))
        self.label_3.setObjectName("label_3")
        self.lineEdit_num_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_num_2.setGeometry(QtCore.QRect(360, 86, 50, 20))
        self.lineEdit_num_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_num_2.setObjectName("lineEdit_num_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(318, 90, 54, 12))
        self.label_4.setObjectName("label_4")
        self.lineEdit_num_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_num_3.setGeometry(QtCore.QRect(361, 136, 50, 20))
        self.lineEdit_num_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_num_3.setObjectName("lineEdit_num_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(319, 140, 54, 12))
        self.label_5.setObjectName("label_5")
        self.lineEdit_num_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_num_4.setGeometry(QtCore.QRect(361, 186, 50, 20))
        self.lineEdit_num_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_num_4.setObjectName("lineEdit_num_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(319, 190, 54, 12))
        self.label_6.setObjectName("label_6")
        self.lineEdit_num_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_num_5.setGeometry(QtCore.QRect(362, 226, 50, 20))
        self.lineEdit_num_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_num_5.setObjectName("lineEdit_num_5")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(320, 230, 54, 12))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(380, 350, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 350, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_danxuan = QtWidgets.QLabel(Form)
        self.label_danxuan.setGeometry(QtCore.QRect(415, 42, 54, 12))
        self.label_danxuan.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_danxuan.setObjectName("label_danxuan")
        self.label_duoxuan = QtWidgets.QLabel(Form)
        self.label_duoxuan.setGeometry(QtCore.QRect(415, 90, 54, 12))
        self.label_duoxuan.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_duoxuan.setObjectName("label_duoxuan")
        self.label_panduan = QtWidgets.QLabel(Form)
        self.label_panduan.setGeometry(QtCore.QRect(415, 140, 54, 12))
        self.label_panduan.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_panduan.setObjectName("label_panduan")
        self.label_tiankong = QtWidgets.QLabel(Form)
        self.label_tiankong.setGeometry(QtCore.QRect(415, 190, 54, 12))
        self.label_tiankong.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_tiankong.setObjectName("label_tiankong")
        self.label_wenda = QtWidgets.QLabel(Form)
        self.label_wenda.setGeometry(QtCore.QRect(415, 230, 54, 12))
        self.label_wenda.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_wenda.setObjectName("label_wenda")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(40, 170, 54, 12))
        self.label_8.setObjectName("label_8")
        self.lineEdit_testname = QtWidgets.QLineEdit(Form)
        self.lineEdit_testname.setGeometry(QtCore.QRect(120, 166, 161, 20))
        self.lineEdit_testname.setObjectName("lineEdit_testname")
        self.lineEdit_testtime = QtWidgets.QLineEdit(Form)
        self.lineEdit_testtime.setGeometry(QtCore.QRect(121, 216, 121, 20))
        self.lineEdit_testtime.setObjectName("lineEdit_testtime")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(40, 220, 54, 12))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(250, 217, 31, 16))
        self.label_10.setObjectName("label_10")
        self.label_panduan_2 = QtWidgets.QLabel(Form)
        self.label_panduan_2.setGeometry(QtCore.QRect(460, 140, 54, 12))
        self.label_panduan_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_panduan_2.setObjectName("label_panduan_2")
        self.label_duoxuan_2 = QtWidgets.QLabel(Form)
        self.label_duoxuan_2.setGeometry(QtCore.QRect(460, 90, 54, 12))
        self.label_duoxuan_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_duoxuan_2.setObjectName("label_duoxuan_2")
        self.label_wenda_2 = QtWidgets.QLabel(Form)
        self.label_wenda_2.setGeometry(QtCore.QRect(460, 230, 54, 12))
        self.label_wenda_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_wenda_2.setObjectName("label_wenda_2")
        self.label_danxuan_2 = QtWidgets.QLabel(Form)
        self.label_danxuan_2.setGeometry(QtCore.QRect(460, 42, 54, 12))
        self.label_danxuan_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_danxuan_2.setObjectName("label_danxuan_2")
        self.label_tiankong_2 = QtWidgets.QLabel(Form)
        self.label_tiankong_2.setGeometry(QtCore.QRect(460, 190, 54, 12))
        self.label_tiankong_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_tiankong_2.setObjectName("label_tiankong_2")
        self.lineEdit_val_1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_val_1.setGeometry(QtCore.QRect(487, 40, 50, 20))
        self.lineEdit_val_1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_val_1.setObjectName("lineEdit_val_1")
        self.lineEdit_val_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_val_2.setGeometry(QtCore.QRect(488, 86, 50, 20))
        self.lineEdit_val_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_val_2.setObjectName("lineEdit_val_2")
        self.lineEdit_val_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_val_3.setGeometry(QtCore.QRect(489, 136, 50, 20))
        self.lineEdit_val_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_val_3.setObjectName("lineEdit_val_3")
        self.lineEdit_val_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_val_4.setGeometry(QtCore.QRect(489, 186, 50, 20))
        self.lineEdit_val_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_val_4.setObjectName("lineEdit_val_4")
        self.lineEdit_val_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_val_5.setGeometry(QtCore.QRect(490, 226, 50, 20))
        self.lineEdit_val_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_val_5.setObjectName("lineEdit_val_5")
        self.label_summary = QtWidgets.QLabel(Form)
        self.label_summary.setGeometry(QtCore.QRect(40, 270, 500, 12))
        self.label_summary.setMinimumSize(QtCore.QSize(500, 0))
        self.label_summary.setObjectName("label_summary")
        self.label.setBuddy(self.comboBox)
        self.label_2.setBuddy(self.comboBox_2)
        self.label_8.setBuddy(self.lineEdit_testname)
        self.label_9.setBuddy(self.lineEdit_testtime)

        self.retranslateUi(Form)
        self.comboBox.currentTextChanged['QString'].connect(Form.shiyongFW_changed)
        self.pushButton.clicked.connect(Form.on_clicked)
        self.pushButton_2.clicked.connect(Form.close)
        self.comboBox_2.currentTextChanged['QString'].connect(Form.zhuanye_changed)
        self.lineEdit_testname.textChanged['QString'].connect(Form.testname_changed)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.comboBox, self.comboBox_2)
        Form.setTabOrder(self.comboBox_2, self.lineEdit_testname)
        Form.setTabOrder(self.lineEdit_testname, self.lineEdit_testtime)
        Form.setTabOrder(self.lineEdit_testtime, self.lineEdit_num_1)
        Form.setTabOrder(self.lineEdit_num_1, self.lineEdit_val_1)
        Form.setTabOrder(self.lineEdit_val_1, self.lineEdit_num_2)
        Form.setTabOrder(self.lineEdit_num_2, self.lineEdit_val_2)
        Form.setTabOrder(self.lineEdit_val_2, self.lineEdit_num_3)
        Form.setTabOrder(self.lineEdit_num_3, self.lineEdit_val_3)
        Form.setTabOrder(self.lineEdit_val_3, self.lineEdit_num_4)
        Form.setTabOrder(self.lineEdit_num_4, self.lineEdit_val_4)
        Form.setTabOrder(self.lineEdit_val_4, self.pushButton)
        Form.setTabOrder(self.pushButton, self.lineEdit_val_5)
        Form.setTabOrder(self.lineEdit_val_5, self.lineEdit_num_5)
        Form.setTabOrder(self.lineEdit_num_5, self.pushButton_2)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "试卷设置"))
        self.label.setText(_translate("Form", "适用范围"))
        self.label_2.setText(_translate("Form", "专业选择"))
        self.lineEdit_num_1.setText(_translate("Form", "0"))
        self.label_3.setText(_translate("Form", "单选题"))
        self.lineEdit_num_2.setText(_translate("Form", "0"))
        self.label_4.setText(_translate("Form", "多选题"))
        self.lineEdit_num_3.setText(_translate("Form", "0"))
        self.label_5.setText(_translate("Form", "判断题"))
        self.lineEdit_num_4.setText(_translate("Form", "0"))
        self.label_6.setText(_translate("Form", "填空题"))
        self.lineEdit_num_5.setText(_translate("Form", "0"))
        self.label_7.setText(_translate("Form", "问答题"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_2.setText(_translate("Form", "退出"))
        self.label_danxuan.setText(_translate("Form", "0"))
        self.label_duoxuan.setText(_translate("Form", "0"))
        self.label_panduan.setText(_translate("Form", "0"))
        self.label_tiankong.setText(_translate("Form", "0"))
        self.label_wenda.setText(_translate("Form", "0"))
        self.label_8.setText(_translate("Form", "考试名称"))
        self.lineEdit_testtime.setText(_translate("Form", "30"))
        self.label_9.setText(_translate("Form", "考试时长"))
        self.label_10.setText(_translate("Form", "分钟"))
        self.label_panduan_2.setText(_translate("Form", "分值"))
        self.label_duoxuan_2.setText(_translate("Form", "分值"))
        self.label_wenda_2.setText(_translate("Form", "分值"))
        self.label_danxuan_2.setText(_translate("Form", "分值"))
        self.label_tiankong_2.setText(_translate("Form", "分值"))
        self.lineEdit_val_1.setText(_translate("Form", "1"))
        self.lineEdit_val_2.setText(_translate("Form", "1"))
        self.lineEdit_val_3.setText(_translate("Form", "1"))
        self.lineEdit_val_4.setText(_translate("Form", "1"))
        self.lineEdit_val_5.setText(_translate("Form", "1"))
        self.label_summary.setText(_translate("Form", "【概要】"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())