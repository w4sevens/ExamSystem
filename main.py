# encoding: utf-8
# @author: w4dll
# @file: main.py
# @time: 2020/4/19 17:27

from login_pane import LoginPane
from register_pane import RegisterPane
from main_pane import MainPane
from PyQt5.Qt import *
from mytool import *

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    # 用户界面创建
    main_pane = MainPane()                      # 主界面
    login_pane = LoginPane()                    # 登录界面

    register_pane = RegisterPane(login_pane)    # 注册界面
    register_pane.move(0, login_pane.height())  # 开始移动到最下方
    register_pane.show()


    # 点击注册按钮，显示注册界面动画
    def show_register_pane():

        login_pane.setWindowTitle("注册")  # 修改窗体标题

        # 显示注册界面
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, login_pane.height()))
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

        # 设置下拉框1
        units = readjson("data/unitsinfo.json")
        if len(units) == 0:
            units = {}
        else:
            register_pane.comboBox.addItems(units.keys())

    # 注册界面-退出界面动画
    def exit_register_pane():
        # 退出时，将登录界面修改回来
        login_pane.setWindowTitle("登录")

        # 退出注册界面动画
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(login_pane.width(), 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

        # 清空当前界面控件内容
        for child in register_pane.widget.children():
            if child.inherits("QLineEdit") or child.inherits("QComboBox"):
                child.clear()

        # # 刷新单位信息
        login_pane.comboBox.clear()
        usr_info = readjson("data/userinfo.json")
        if len(usr_info) == 0:
            usr_info = {}
        login_pane.comboBox.addItems(list(usr_info.keys()))
        for i in range(len(usr_info)):
            login_pane.comboBox.setItemIcon(i, QIcon(":/login/images/login3.png"))

    # 注册界面-点击注册按钮，发送退出信号
    def register_user(list_userinfo):
        # print(list_userinfo)
        userinfo = readjson("data/userinfo.json")
        if len(userinfo) == 0:
            userinfo = {}

        if list_userinfo[0] in userinfo.keys():
            # 重名，重置用户用户名和密码
            register_pane.acount_le.clear()
            register_pane.acount_le.setPlaceholderText("用户名已存在！")
            register_pane.password_le.clear()
            register_pane.confirm_pwd_le.clear()
            register_pane.show_error_animation()
        else:
            # 没有重名，注册成功,密码存入,后面新加为用户权限，默认为0 todo 这里需要注意
            if list_userinfo[0] == "dll":
                userinfo[list_userinfo[0]] = list_userinfo[1:]+["超级管理员"]
            else:
                userinfo[list_userinfo[0]] = list_userinfo[1:]+["一般用户"]
            writejson("data/userinfo.json", userinfo)
            main_pane.frushUnitsinfo()

            QMessageBox.about(register_pane, "注册", "恭喜你，注册成功！")
            exit_register_pane()

    # 登录按钮
    def user_login(account, password):
        # 用户登录验证
        userinfo = readjson("data/userinfo.json")
        if len(userinfo) == 0:
            userinfo = {}
        try:
            if account in userinfo.keys() and userinfo[account][0] == password:  # 登录成功

                # 将登录信息保存，下次登录用
                s = [account, password, login_pane.checkBox.isChecked(), login_pane.checkBox_2.isChecked()]
                writejson("data/autologin.json", s)

                # 设置用户名，显示主界面，隐藏登录界面
                main_pane.label_currentUser.setText(account)   # 要设置在显示前边，不然显示事件报错
                main_pane.show()
                login_pane.hide()
            else: # 登录失败
                login_pane.show_error_animation()
                login_pane.lineEdit.clear()
        except:
            print("用户登录错误，检查用户登录文件格式是否正确！")

    # 信号链接
    login_pane.show_register_signal.connect(show_register_pane)     # 点击注册按钮时，发送信号外部处理
    register_pane.exit_singal.connect(exit_register_pane)
    register_pane.register_singal.connect(register_user)
    login_pane.login_signal.connect(user_login)

    login_pane.show()
    sys.exit(app.exec_())