# encoding: utf-8
# @author: w4dll
# @file: register_pane.py
# @time: 2020/4/18 23:31

from PyQt5.Qt import*
from resource.scoreUi import Ui_Form
from mytool import readjson
from openpyxl import load_workbook, workbook

class scoreTongji(QWidget, Ui_Form):

    def __init__(self, parent = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

        self.initUi()

    def initUi(self):
        # 初始化tableview
        self.list_model = QStandardItemModel()
        self.list_model.setHorizontalHeaderLabels(["用户名","姓名", "一级单位", "二级单位", "三级单位",
                                                    "试卷名称", "考试时间", "考试时长", "用时", "题目数量",
                                                    "总分", "得分", "考试类别"])
        data = readjson("data/test_resualt_all.json")

        if len(data) > 0:
            # 添加数据
            for key in data:
                a, b = key.split("-")
                li = []
                account = data[key][0]
                li.append(account)
                d_temp = readjson("data/userinfo.json")
                if account in d_temp:
                    li += [d_temp[account][1]] + d_temp[account][3:6]
                else:
                    li += ["", "", "", ""]
                li += [b, a] + data[key][1:3]
                tmp1, tmp2 = data[key][4:6]
                nums, vals = 0, 0
                for i in range(5):
                    nums += tmp1[i]
                    vals += tmp1[i] * tmp2[i]
                li += [nums, vals] + [data[key][3]] + [data[key][-1]]

                ls_q = []
                for x in li:
                    q1 = QStandardItem(str(x))
                    q1.setTextAlignment(Qt.AlignCenter)  # 设置单元格居中显示
                    ls_q.append(q1)

                self.list_model.appendRow(ls_q)
            self.tableView.setModel(self.list_model)
            self.tableView.horizontalHeader().setStretchLastSection(True)
            # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置表格

    def save_excel(self):
        # QModelIndex()
        # for i in range(self.list_model.rowCount()):
        #     print(self.list_model.item(, i).data())

        self.tableView.selectAll()
        indexs = self.tableView.selectionModel().selection().indexes()
        if len(indexs) > 0:
            ls0 = []
            for i in range(0, len(indexs), 13):
                ls = []
                for j in range(13):
                    ls.append(indexs[i+j].data())
                ls0.append(ls)

            wb = workbook.Workbook()
            s = ["用户名","姓名", "一级单位", "二级单位", "三级单位",
                 "试卷名称", "考试时间", "考试时长", "用时", "题目数量", "总分", "得分", "考试类别"]
            ls0.insert(0, s)
            for x in ls0:
                wb.worksheets[0].append(x)

            filepath, _ = QFileDialog.getSaveFileName(self, "导出题库到Excel文件", "./", "excel(*.xlsx)")
            if len(filepath) > 0:
                wb.save(filepath)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = scoreTongji()

    window.show()
    sys.exit(app.exec_())