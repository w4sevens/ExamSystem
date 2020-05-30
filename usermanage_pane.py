# encoding: utf-8
# @author: w4dll
# @file: usermanage_pane.py
# @time: 2020/5/6 22:01

from PyQt5.Qt import*
from resource.usermanagement import Ui_Form
from mytool import readjson, writejson
from adduser_pane import AddUser

class userManegePane(QWidget, Ui_Form):

    user_changed_singal = pyqtSignal()

    def __init__(self, username):
        super().__init__()
        self.setupUi(self)
        self.currentusername = username
        self.initUi()


    # 初始化界面
    def initUi(self):

        # 设置当前用户显示
        self.label_2.setText("当前用户："+self.currentusername)

        # 获取试卷信息,添加到listWidget
        self.users = readjson("data/userinfo.json")
        if len(self.users) == 0:
            self.users = {}

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["用户名", "姓名", "性别", "一级单位", "二级单位", "三级单位", "注册时间", "用户权限"])

        # 添加数据
        for user in self.users:
            li = []
            q1 = QStandardItem(user)
            q1.setTextAlignment(Qt.AlignCenter)  # 设置单元格居中显示
            li.append(q1)
            for i in range(7):
                x = self.users[user][i+1]
                m = QStandardItem(x)
                m.setTextAlignment(Qt.AlignCenter)  # 设置单元格居中显示
                li.append(m)
            self.model.appendRow(li)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置表格的选取方式是行选取

    # 提升权限
    def updatepriority(self):
        indexs = self.tableView.selectionModel().selection().indexes()  # 将所有单元格按顺序存储
        prio = ["一般用户", "管理员", "超级管理员"]
        current_priority = self.users[self.currentusername][-1]
        for i in range(int(len(indexs)/8)):
            d = indexs[8 * i + 7].data()
            if d in prio[:-1] and current_priority in prio[1:]:
                if prio.index(d) < prio.index(current_priority):
                    s = prio[1+prio.index(d)]
                    self.model.setData(indexs[8 * i + 7], s)
                    self.users[indexs[8 * i].data()][-1] = s
                    QMessageBox.about(self, "提示", "操作成功！")
                else:
                    QMessageBox.about(self, "提示", "你没有操作权限！")
            else:
                QMessageBox.about(self, "提示", "你没有操作权限！")
        self.tableView.setCurrentIndex(QModelIndex())
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)

        # 存储用户权限
        writejson("data/userinfo.json", self.users)

    # 删除用户
    def deleteuser(self):
        if self.tableView.currentIndex().row()>-1:
            indexs = self.tableView.selectionModel().selection().indexes()  # 将所有单元格按顺序存储
            if QMessageBox.Yes == QMessageBox.question(self, "提示", "确实删除用户吗？删除后不可恢复!"):
                prio = ["一般用户", "管理员", "超级管理员"]
                ls_row_num = []
                for i in range(0, len(indexs), 8):
                    account = indexs[i].data()  # 用户名
                    if self.currentusername == account:
                        QMessageBox.about(self, "提示", "不能删除本人！")
                        continue
                    d = indexs[i+7].data()  # 用户权限
                    current_priority = self.users[self.currentusername][-1]
                    if prio.index(d) < prio.index(current_priority):
                        ls_row_num.append(indexs[i])
                        # self.model.removeRows(indexs[x].row(), 1)   # 由于这里删除一行，前面自动没有了，所以每次都从0行开始
                        self.users.pop(account)
                    else:
                        QMessageBox.about(self, "提示", "你没有操作权限！不能删除用户【"+account+"】")
                # 删除表中显示
                ls_row_num.reverse()
                for index in ls_row_num:
                    self.model.removeRow(index.row())
                writejson("data/userinfo.json", self.users)
                self.user_changed_singal.emit()

        self.tableView.setCurrentIndex(QModelIndex())  # 设置当前索引行为空
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)

    # 添加用户
    def adduser(self):
        self.win = AddUser()
        self.win.register_singal.connect(self.addusertotable)
        self.win.setWindowModality(Qt.ApplicationModal)
        self.win.show()

    def addusertotable(self, list_user):
        # list_user=['name', 'p', '丁莉莉', '男', '1', '22', '333', '202005161734']
        users = readjson("data/userinfo.json")
        if len(users) == 0:
            users = {}
        if list_user[0] in users:
            QMessageBox.about(self, "提示", "用户已存在！")
        else:
            users[list_user[0]] = list_user[1:] + ["一般用户"]
        writejson("data/userinfo.json", users)
        self.user_changed_singal.emit()

        self.initUi()

    # 选中行
    def row_selected(self, x):
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = userManegePane("dll")
    win.show()
    sys.exit(app.exec_())