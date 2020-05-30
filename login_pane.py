# encoding: utf-8
# @author: w4dll
# @file: login_pane.py
# @time: 2020/4/19 14:12

from PyQt5.Qt import*
from resource.login import Ui_Form
from mytool import readjson


class LoginPane(QWidget, Ui_Form):

    # # 用户自定义信号
    show_register_signal = pyqtSignal()
    login_signal = pyqtSignal(str, str)

    def __init__(self, parent = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.setWindowTitle("登录")

        # 设置动画背景
        movie = QMovie(":/login/images/login_background1.gif")
        self.label_login_background.setMovie(movie)
        movie.setScaledSize(QSize(500, 180))
        movie.setSpeed(6)
        movie.start()


        # 设置下拉框信息,添加用户图标
        usr_info = readjson("data/userinfo.json")
        if len(usr_info) == 0:
            usr_info = {}
        self.comboBox.addItems(list(usr_info.keys()))
        for i in range(len(usr_info)):
            self.comboBox.setItemIcon(i, QIcon(":/login/images/login3.png"))
        self.comboBox.setMaxVisibleItems(5)

        # 初始化登录相关信息
        login_info = readjson("data/autologin.json")
        if len(login_info) > 0: # 如果存在
            self.comboBox.setCurrentText(login_info[0])
            if login_info[3] == True:  # 记住密码
                self.lineEdit.setText(login_info[1])
                self.checkBox_2.setChecked(login_info[3])
            if login_info[2] == True:  # 自动登录
                self.checkBox.setChecked(login_info[2])

                # 延迟3秒后自动登录
                # todo 等待3秒后，如果用户没有操作，自动登录,由于这里初始化未绑定槽，所以直接调用不行
                self.time = QTimer(self)
                self.time.setInterval(5000)
                self.time.timeout.connect(self.auto_click)
                self.time.start()


    def auto_click(self):
        self.time.stop()
        self.pushButton_3.click()

    # comboBox下拉框内容变化时，清空密码框内容
    def clean_pwd(self):
        self.lineEdit.clear()

    # 点击注册按钮时，发送注册信号
    def register_clicked(self):
        self.show_register_signal.emit()

    # 如果用户名和密码均不为空，设置登录按钮可用，否则不可用
    def enable_login_btn(self):
        account = self.comboBox.currentText()
        password = self.lineEdit.text()
        if len(account) > 0 and len(password) > 0:
            self.pushButton_3.setEnabled(True)
        else:
            self.pushButton_3.setEnabled(False)

    # 点击登录按钮时，触发登录信号
    def check_login(self):
        # 登录信号触发
        account = self.comboBox.currentText()
        password = self.lineEdit.text()
        self.login_signal.emit(account, password)

    # 自动登录复窗框槽函数，如果勾选，则记住密码复选框也勾选
    def auto_login(self, checked):
        if checked:
            self.checkBox_2.setChecked(True)

            # 如果勾选，下次自动登录
        else:
            # 如果不勾选，下次不自动登录
            pass

    # 记住密码复选框，如果不勾选，则自动登录也不勾选
    def remenber_pwd(self, checked):
        if not checked:
            self.checkBox.setChecked(False)
        else:
            # 如果勾选，则下次记住密码，但不自动登录
            pass

    # 登录错误，登录框震动动画
    def show_error_animation(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.widget_3)
        animation.setPropertyName(b"pos")
        animation.setKeyValueAt(0, self.widget_3.pos())
        animation.setKeyValueAt(0.2, self.widget_3.pos() + QPoint(15, 0))
        animation.setKeyValueAt(0.5, self.widget_3.pos())
        animation.setKeyValueAt(0.7, self.widget_3.pos() + QPoint(-15, 0))
        animation.setKeyValueAt(1, self.widget_3.pos())
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.setLoopCount(3)
        animation.setDuration(100)
        animation.start(QAbstractAnimation.DeleteWhenStopped)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = LoginPane()
    window.show()
    sys.exit(app.exec_())