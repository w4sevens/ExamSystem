# encoding: utf-8
# @author: w4dll
# @file: register_pane.py
# @time: 2020/4/18 23:31

from PyQt5.Qt import*
from resource.adduser import Ui_Form
from mytool import readjson
import time

class AddUser(QWidget, Ui_Form):

    register_singal = pyqtSignal(list)

    def __init__(self, parent = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

        self.sex = "" # 性别
        self.initUi()

    def initUi(self):
        self.units = readjson("data/unitsinfo.json")
        for key in self.units:
            self.comboBox.addItem(str(key))

    # 第一个下拉框变动时触发
    def dan1_changed(self, text):
        if text in self.units.keys():
            units2 = self.units[text].keys()
            if len(units2) > 0 :
                self.comboBox_2.clear()
                self.comboBox_2.addItems(units2)
        else:
            self.comboBox_2.clear()

    def dan2_changed(self, text):
        if len(self.units) > 0:  # 单位信息存在
            if self.comboBox.currentText() in self.units.keys():  # 下拉框1在单位信息中
                units2 = self.units[self.comboBox.currentText()].keys()
                if text in units2: # 下拉框2在单位信息中
                    self.comboBox_3.clear()
                    self.comboBox_3.addItems(self.units[self.comboBox.currentText()][text])
                else:
                    self.comboBox_3.clear()
            else:
                self.comboBox_3.clear()

    # 点击性别框时触发
    def sex_changed(self):
        if self.checkBox.checkState():
            self.sex = "男"
        else:
            self.sex = "女"

    # 退出
    def exit_clicked(self):
        print("点击退出按钮")
        self.close()

    # 添加按钮
    def register_clicked(self):
        if self.password_le.text() != self.confirm_pwd_le.text():
            self.confirm_pwd_le.clear()
            self.confirm_pwd_le.setPlaceholderText("两次密码输入不同！")
        else:
            text_acount = self.acount_le.text()
            text_pwd = self.password_le.text()

            # 这里可以用list类型传递信息
            t = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
            self.register_singal.emit([text_acount, text_pwd, self.lineEdit_name.text(), self.sex,
                                       self.comboBox.currentText(), self.comboBox_2.currentText(),
                                       self.comboBox_3.currentText(), t])
        self.close()

    # 输入变动槽函数
    def input_changed(self, str_input):
        # 当输入框全部有效是，注册按钮可用
        # print("输入变动！", str_input)
        if self.acount_le.text() != "" and self.password_le.text() != "" and self.confirm_pwd_le.text() != "" and self.lineEdit_name.text() != "":
            self.register_btn.setEnabled(True)
        else:
            self.register_btn.setEnabled(False)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = AddUser()
    # window.register_singal.connect(lambda li1: print("接受账户和密码：", li1))
    # window.exit_singal.connect(lambda :print("成功退出!"))

    window.show()
    sys.exit(app.exec_())