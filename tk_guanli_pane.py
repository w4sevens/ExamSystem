# encoding: utf-8
# @author: w4dll
# @file: usermanage_pane.py
# @time: 2020/5/6 22:01

from PyQt5.Qt import*
from resource.tk_guanli import Ui_Form
from mytool import readjson, writejson

class tkGuanli(QWidget, Ui_Form):
    tk_guanli_complete = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    # 初始化界面
    def initUi(self):

        self.tiku = readjson("data/tiku.json")
        if len(self.tiku) == 0:
            self.tiku = {}
            QMessageBox.about(self, "提示", "请先导入题库！")
            self.pushButton_2.setEnabled(False)

        # 题库信息整理，长度统一
        length_row = 0
        sheet_list = []
        for x in self.tiku:
            length_row = max(length_row, len(self.tiku[x]))
            sheet_list.append(self.tiku[x])

        # 将题库补全，长度统一
        for i in range(len(sheet_list)):
            if len(sheet_list[i]) < length_row:
                sheet_len = len(sheet_list[i])
                for j in range(length_row - sheet_len):
                    sheet_list[i].insert(len(sheet_list[i])-2, "")

        # 插入表头信息
        first_row = ["适用人员", "适用单位", "题目", "题型"]
        i = 1
        for m in range(4, length_row - 2):
            first_row.append("选项" + str(i))
            i += 1
        first_row.append("答案")
        first_row.append("备注")

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(first_row)

        # 添加数据
        for item in sheet_list:
            li = []
            for v in item:
                q1 = QStandardItem(str(v))
                q1.setTextAlignment(Qt.AlignCenter)  # 设置单元格居中显示
                li.append(q1)
            self.model.appendRow(li)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置表格的选取方式是行选取

    # 选中行
    def row_selected(self, x):
        self.pushButton.setEnabled(True)

    # 删除行
    def delete_row(self):
        for index in self.tableView.selectedIndexes():
            self.model.removeRow(index.row())
        self.pushButton.setEnabled(False)

    # 确定按钮
    def on_ok(self):
        if QMessageBox.No == QMessageBox.question(self, "提示", "是否保存更改？"):
            return

        rowcount = self.model.rowCount()
        colcount = self.model.columnCount()
        ls1 = {}
        for i in range(rowcount):
            ls = []
            for j in range(colcount):
                index = self.model.index(i,j)
                s = self.model.data(index)
                if s != "" or j == colcount-1:
                    ls.append(s)
            ls1[str(i)] = ls
        # print(ls1)
        writejson("data/tiku.json", ls1)
        self.tk_guanli_complete.emit()
        self.close()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = tkGuanli()
    win.show()
    sys.exit(app.exec_())