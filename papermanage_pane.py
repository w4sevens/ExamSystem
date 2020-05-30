from PyQt5.Qt import*
from resource.papermanagement import Ui_Form
from mytool import readjson,writejson

class paperManagePane(QDialog, Ui_Form):

    # setdefault_signal = pyqtSignal()
    delete_testpaper = pyqtSignal()  # 删除默认题库时发送信号


    def __init__(self, parent = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.flage = 0

        self.init()

    # 初始化本界面
    def init(self):
        # 获取试卷信息,添加到listWidget
        self.shijuan = readjson("data/shijuan_all.json")
        if self.shijuan == "":
            self.shijuan = {}
        names = list(self.shijuan.keys())
        if len(names) == 0:
            QMessageBox.about(self, "提示", "试卷信息为空，请先添加试卷！")
            self.flage = 1
            # self.close()            # todo 注意，由于此时主体功能已经初始化完毕，父程序中调用open函数在close函数后面，所以这里没有效果。
            return

        # 显示默认试卷
        # d = readjson("data/defaulttest.json")
        # if len(d) > 0:
        #     self.label_2.setText("默认试卷：" + str(list(d.keys())[0]))
        # else:
        #     self.label_2.setText("默认试卷：无")

        # 设置数据模型
        if len(self.shijuan[names[0]]) > 0 :
            self.model = QStandardItemModel()
            self.model.setHorizontalHeaderLabels(["序号", "试卷名称", "创建时间", "适用范围", "适用单位", "时长", "题目数", "总分"])
            for i in range(len(self.shijuan)):
                q1 = QStandardItem(str(i+1))
                q1.setTextAlignment(Qt.AlignCenter)  # 设置单元格居中显示

                a, b = str(names[i]).split("-")
                q2, q3 = QStandardItem(b), QStandardItem(a)
                q2.setTextAlignment(Qt.AlignCenter)
                q3.setTextAlignment(Qt.AlignCenter)

                val = self.shijuan[names[i]][3].values()
                if len(val) > 0:
                    c, d = list(val)[0][:2]
                else:
                    c, d = "", ""
                q4, q5 = QStandardItem(c), QStandardItem(d)
                q4.setTextAlignment(Qt.AlignCenter)
                q5.setTextAlignment(Qt.AlignCenter)


                e = self.shijuan[names[i]][0]  # 时长
                q6 = QStandardItem(e)
                q6.setTextAlignment(Qt.AlignCenter)

                f = self.shijuan[names[i]][1]
                g = self.shijuan[names[i]][2]
                nums, scores = 0, 0
                for j in range(5):
                    nums += f[j]
                    scores += f[j] * g[j]
                q7, q8 = QStandardItem(str(nums)), QStandardItem(str(scores))
                q7.setTextAlignment(Qt.AlignCenter)
                q8.setTextAlignment(Qt.AlignCenter)

                self.model.appendRow([q1, q2, q3, q4, q5, q6, q7, q8])

            # 绑定数据模型
            self.tableView.setModel(self.model)

            # 表格显示设置
            self.tableView.setShowGrid(True)  # 显示网格线
            self.tableView.horizontalHeader().setStretchLastSection(True)                   # 水平方向表格拉伸满
            # self.tableView.setColumnWidth(0, 50)                                          # 设置列宽，此处设置拉伸，无效
            self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)     # 水平方向，表格大小拓展到适当的尺寸
            self.tableView.verticalHeader().setVisible(False)                               # 隐藏第一列
            self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)               # 设置表格的选取方式是行选取
            self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)              # 设置选取方式为单个选取
            # self.tableView.setSortingEnabled(True)                                          # 排序功能


    # tableview槽函数，选中行操作
    def row_selected(self, modelIndex):
        if modelIndex.row() > -1:
            self.pushButton_2.setEnabled(True)
        else:
            self.pushButton_2.setEnabled(False)

    # 删除试卷
    def deleterow(self):
        indexs = self.tableView.selectionModel().selection().indexes()

        if len(indexs)>0:
            # 删除试卷，修改试卷文件
            s_name = str(indexs[2].data()) + "-" + str(indexs[1].data())
            if QMessageBox.Yes == QMessageBox.question(self, "删除", "是否删除试卷->" + s_name):
                self.model.removeRows(indexs[0].row(), 1)       # 从指定行索引开始删除指定行数，此处1行
                self.shijuan.pop(s_name)
                writejson("data/shijuan_all.json", self.shijuan)
                self.delete_testpaper.emit()

            # 删除后，设置按钮不可用
            self.tableView.setCurrentIndex(QModelIndex())  # 设置当前不选中行
            self.pushButton_2.setEnabled(False)

    # 设置默认试卷
    def setdefault(self):
        indexs = self.tableView.selectionModel().selection().indexes()
        if len(indexs)>0:
            # 获取当前试卷名称
            s_name = str(indexs[2].data()) + "-" + str(indexs[1].data())

            default = {}
            default[s_name] = self.shijuan[s_name]
            writejson("data/defaulttest.json", default)
            QMessageBox.about(self, "设置默认试卷", "设置成功！")

            # 设置默认后，行不选中，按钮不可用
            self.tableView.setCurrentIndex(QModelIndex())   # 设置当前不选中行
            self.pushButton_2.setEnabled(False)

            # self.label_2.setText("默认试卷："+s_name)
            # self.setdefault_signal.emit()

    # 清空所有试卷
    def clearpaper(self):
        if QMessageBox.question(self, "清空试卷", "确定清空题库吗？清空后不可恢复！") == QMessageBox.Yes:
            # 清空所有试卷
            self.model.removeRows(0, self.model.rowCount())
            # self.label_2.setText("默认试卷：无")
            writejson("data/shijuan_all.json", {})
            writejson("data/defaulttest.json", {})
            self.delete_testpaper.emit()
        else:
            pass

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = paperManagePane()
    win.show()
    sys.exit(app.exec_())