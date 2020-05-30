# encoding: utf-8
# @author: w4dll
# @file: paperset_pane.py
# @time: 2020/4/24 20:30

from PyQt5.Qt import*
from resource.paperset import Ui_Form
from mytool import *
from functools import partial

import time

class PapersetPane(QDialog, Ui_Form):

    add_test_signal = pyqtSignal()

    def __init__(self, parent = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.initUi()

        self.nums, self.vals = [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]

    # 根据题库信息初始化下拉框
    def initUi(self):
        # 信号与槽函数
        self.lineEdit_testname.editingFinished.connect(self.nameEdited)
        self.lineEdit_testtime.editingFinished.connect(self.timeEdited)
        self.lineEdit_num_1.editingFinished.connect(partial(self.setSummary, "nums", 0))
        self.lineEdit_num_2.editingFinished.connect(partial(self.setSummary, "nums", 1))
        self.lineEdit_num_3.editingFinished.connect(partial(self.setSummary, "nums", 2))
        self.lineEdit_num_4.editingFinished.connect(partial(self.setSummary, "nums", 3))
        self.lineEdit_num_5.editingFinished.connect(partial(self.setSummary, "nums", 4))
        self.lineEdit_val_1.editingFinished.connect(partial(self.setSummary, "vals", 0))
        self.lineEdit_val_2.editingFinished.connect(partial(self.setSummary, "vals", 1))
        self.lineEdit_val_3.editingFinished.connect(partial(self.setSummary, "vals", 2))
        self.lineEdit_val_4.editingFinished.connect(partial(self.setSummary, "vals", 3))
        self.lineEdit_val_5.editingFinished.connect(partial(self.setSummary, "vals", 4))

        self.lineEdit_testtime.setEnabled(False)

        # 初始化界面信息
        self.data = readjson("data/tkinfo.json")  # 题库信息
        if len(self.data) > 0:
            for x in self.data:
                self.comboBox.addItem(x)
        else:
            self.label_summary.setText("概要：题库为空，请先导入题库文件！")

    # 数字输入框槽函数
    def setSummary(self,type, index):
        s = "【概要】"
        self_vals = [self.lineEdit_val_1, self.lineEdit_val_2, self.lineEdit_val_3, self.lineEdit_val_4, self.lineEdit_val_5]
        self_nums = [self.lineEdit_num_1, self.lineEdit_num_2, self.lineEdit_num_3, self.lineEdit_num_4, self.lineEdit_num_5]
        self_label = [self.label_danxuan.text(), self.label_duoxuan.text(), self.label_panduan.text(),
                      self.label_tiankong.text(), self.label_wenda.text()]
        # 检测用户输入合法性，并存储
        if type == "nums":
            try:
                # 如果输入数字超过总数，取最大值
                if int(self_nums[index].text()) > int(self_label[index]):
                    self.nums[index] = int(self_label[index])
                    self_nums[index].setText(self_label[index])
                else:
                    self.nums[index] = int(self_nums[index].text())
            except:
                self_nums[index].clear()
                self_nums[index].setPlaceholderText("Error")
                s += "请输入正确的数值！"
                self.label_summary.setText(s)
                self_nums[index].setFocus()
                return
        else:
            try:
                self.vals[index] = int(self_vals[index].text())
            except:
                self_vals[index].clear()
                self_vals[index].setPlaceholderText("Error")
                s += "请输入正确的数值！"
                self.label_summary.setText(s)
                self_vals[index].setFocus()
                return

        # 计算，形成概要字符串
        total_nums, total_score = 0, 0
        for i in range(5):
            total_nums += self.nums[i]
            total_score += self.nums[i] * self.vals[i]
        if self.lineEdit_testname.text() != "":
            s += self.lineEdit_testname.text() + ", "
        if self.lineEdit_testtime.text() != "":
            s += "时长" + self.lineEdit_testtime.text() + "分钟， "
        s += "共" + str(total_nums) + "题, 总分：" + str(total_score) + "分。"
        self.label_summary.setText(s)

    # 考试名称编辑框编辑完成时，修改概要信息,修改时间共用
    def nameEdited(self):
        s = "【概要】"
        # 计算，形成概要字符串
        total_nums, total_score = 0, 0
        for i in range(5):
            total_nums += self.nums[i]
            total_score += self.nums[i] * self.vals[i]
        if self.lineEdit_testname.text() != "":
            s += self.lineEdit_testname.text() + ", "
        else:
            self.lineEdit_testname.setPlaceholderText("Error")
            self.lineEdit_testname.setFocus()
        s += "时长" + self.lineEdit_testtime.text() + "分钟， "
        s += "共" + str(total_nums) + "题, 总分：" + str(total_score) + "分。"
        self.label_summary.setText(s)

    def timeEdited(self):
        s = "【概要】"
        # 计算，形成概要字符串
        total_nums, total_score = 0, 0
        for i in range(5):
            total_nums += self.nums[i]
            total_score += self.nums[i] * self.vals[i]
        if self.lineEdit_testname.text() != "":
            s += self.lineEdit_testname.text() + ", "

        if self.lineEdit_testtime.text() != "":
            s += "时长" + self.lineEdit_testtime.text() + "分钟， "
            try:
                t = int(self.lineEdit_testtime.text())
            except:
                self.lineEdit_testtime.setPlaceholderText("Error")
                self.lineEdit_testtime.setFocus()
                return
        else:
            self.lineEdit_testtime.setPlaceholderText("Error")
            self.lineEdit_testtime.setFocus()
        s += "共" + str(total_nums) + "题, 总分：" + str(total_score) + "分。"
        self.label_summary.setText(s)

    # 考试名称LineEdit内容改变，且不为空时，设置确定按钮可用
    def testname_changed(self, text):
        if text != "":
            self.pushButton.setEnabled(True)
            self.lineEdit_testtime.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)
            self.lineEdit_testtime.setEnabled(False)

    # 专业下拉框变动槽函数
    def zhuanye_changed(self):
        # 清空用户设置
        self.lineEdit_num_1.setText("0")
        self.lineEdit_num_2.setText("0")
        self.lineEdit_num_3.setText("0")
        self.lineEdit_num_4.setText("0")
        self.lineEdit_num_5.setText("0")
        self.lineEdit_val_1.setText("1")
        self.lineEdit_val_2.setText("1")
        self.lineEdit_val_3.setText("1")
        self.lineEdit_val_4.setText("1")
        self.lineEdit_val_5.setText("1")

        # 根据下拉框变动统计题库中各型题目数量并显示在标签上
        tiku = readjson("data/tiku.json")
        num_tiku = [0, 0, 0, 0, 0]  # 存储单选、多选、判断、填空、问答、其他数量
        ls = ["单选题", "多选题", "判断题", "填空题", "问答题"]
        if len(tiku) > 0:
            for m in tiku:
                if tiku[m][0] == self.comboBox.currentText() and tiku[m][1] == self.comboBox_2.currentText():
                    if tiku[m][3] in ls:
                        num_tiku[ls.index(tiku[m][3])] += 1  # 将数字取出来转换后变成下标
        else:
            print("题库中无信息")

        # 显示label信息
        self.label_danxuan.setText(str(num_tiku[0]))
        self.label_duoxuan.setText(str(num_tiku[1]))
        self.label_panduan.setText(str(num_tiku[2]))
        self.label_tiankong.setText(str(num_tiku[3]))
        self.label_wenda.setText(str(num_tiku[4]))

    # 范围下拉框变动
    def shiyongFW_changed(self, str_fw):
        self.comboBox_2.clear()
        if self.comboBox.currentText() != "":
            for x in self.data[self.comboBox.currentText()]:
                self.comboBox_2.addItem(x)

    # 确定按钮槽函数
    def on_clicked(self):
        self_label = [self.label_danxuan.text(), self.label_duoxuan.text(), self.label_panduan.text(),
                      self.label_tiankong.text(), self.label_wenda.text()]

        # 获取当前范围-单位情况下所有类型题目的题号
        tiku = readjson("data/tiku.json")
        if len(tiku) > 0:
            mytk = [[],[],[],[],[]]                 # 存储各型题目的题号
            ls = ["单选题", "多选题", "判断题", "填空题", "问答题"]
            for x in tiku:
                if tiku[x][0] == self.comboBox.currentText() and tiku[x][1] == self.comboBox_2.currentText():
                    mytk[ls.index(tiku[x][3])].append(x)

            # 随机选择指定数量题目，如果题库中少于指定数，取全部
            get_tiku = []
            for i in range(5):
                li = get_random(self.nums[i], int(self_label[i]))   # 随机取用户输入个数
                for j in li:
                    get_tiku.append(mytk[i][j])

            # 存储试卷文件
            all_shijuan = readjson("data/shijuan_all.json")
            if all_shijuan == "":  # 如果为空
                all_shijuan = {}
            t = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
            testname = str(t) + "-" + self.lineEdit_testname.text()

            # 取出题号对应的题目信息存入d1，写入文件
            d1 = {}
            for x in get_tiku:
                d1[x] = tiku[x]
            all_shijuan[testname] = [self.lineEdit_testtime.text(), self.nums, self.vals, d1]
            writejson("data/shijuan_all.json", all_shijuan)
            QMessageBox.about(self, "添加", "添加试卷成功，可以开始考试了！")
            self.close()
            self.add_test_signal.emit()
        else:
            print("题库中没有题目，不操作")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = PapersetPane()
    window.show()
    sys.exit(app.exec_())