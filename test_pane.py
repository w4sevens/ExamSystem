# encoding: utf-8
# @author: w4dll
# @file: test_pane.py
# @time: 2020/4/29 19:39

from resource.testUI import Ui_Form
from PyQt5.Qt import *
from PyQt5 import sip
from functools import partial
from mytool import *
import re, time

class testPane(QWidget, Ui_Form):

    test_finished_signal = pyqtSignal(list)  # 考试结束信号

    def __init__(self, data, username, parent = None, *args, **kwargs):
        super(testPane, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)

        self.currentuser = username                      # 当前登录用户
        self.name = list(data.keys())[0]
        self.tkdata = data[self.name][3]                 # 考题
        self.test_time = int(data[self.name][0])         # 考试时长
        self.test_vals = data[self.name][2]              # 各题分值
        self.test_nums = data[self.name][1]
        self.test_time2 = data[self.name][0]             # 存储时间，传递用

        self.forward_btnNum = 0          # 这个要放在initUi前面
        self.suiji = "顺序考试"            # 后续添加的随机考试类别，这种方法不科学， 少用

        # 初始化界面题号
        self.initUi()
        self.btn_pressed(0)  # 调用一下第一个按钮，显示初始题目状态

        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    # 根据用户传入的题库信息dict_tiku初始化考试界面
    def initUi(self):
        self.scrollAreaWidgetContents.setMinimumSize(1000, 50+int(26*len(self.tkdata)/25))
        # todo 初始化按钮界面
        if len(self.tkdata) > 0 :
            self.win_width = self.scrollAreaWidgetContents.width()  # 这个值是变化的，所以这里存储便于后面使用
            for i in range(0, len(self.tkdata)):  # 根据题目数量，建立相应的题号按钮
                btn = QPushButton(self.scrollAreaWidgetContents)
                btn.resize(35, 20)  # 设置按钮的高度和宽度
                btn.setText(str(i + 1))
                btn.setFocusPolicy(Qt.NoFocus)

                x = 10 + (i % int(self.win_width/40)) * 38                  # 按钮宽度+间隔=38，高度+间隔=28
                y = 10 + int(i / int(self.win_width/40)) * 26
                btn.move(x, y)

                btn.clicked.connect(partial(self.btn_pressed, i))           # 这个函数可以实现参数传递
                self.tkdata[list(self.tkdata.keys())[i]].append("")         # 将用户选择答案赋在题库后面

        else:
            print("题库信息为空")
            self.close()

        # todo 初始化倒计时器
        self.time = QTimer(self)
        self.time.setInterval(60000)
        self.time.start()                       # 参数表示多久后触发，即延时时间
        self.label_timecount.setText("离考试结束还有【"+str(self.test_time) + "】分钟")
        self.time.timeout.connect(self.Refresh)

    # 上下左右键操作
    def keyReleaseEvent(self, evt) -> None:
        super(testPane, self).keyReleaseEvent(evt)
        if evt.key() == 16777234: # 左
            self.prev_clicked()
        elif evt.key() == 16777236: # 右
            self.next_clicked()
        elif evt.key() == 16777235: # 上
            a = self.forward_btnNum - 25
            if  a < 0:
                a += len(self.tkdata) - len(self.tkdata) % 25 + 25
                if a > len(self.tkdata)-1:
                    a = a - 25
            self.btn_pressed(a)
        elif evt.key() == 16777237: # 下
            a = self.forward_btnNum + 25
            if a > len(self.tkdata)-1:
                a = a % 25
            self.btn_pressed(a)
        else:
            pass

        # QKeyEvent()

    # 刷新计时器
    def Refresh(self):
        self.test_time -= 1
        self.label_timecount.setText("离考试结束还有【"+str(self.test_time) + "】分钟")
        if self.test_time == 0:
            self.time.stop()
            # 考试结束，提交试卷
            QMessageBox.about(self, "提示", "考试结束！")
            self.submit_test()

    # 题号按钮点击槽函数
    def btn_pressed(self, n):  # n->表示题目索引号，从0开始

        tk_keys = list(self.tkdata.keys())

        # 恢复前一个按钮颜色
        x = 10 + (self.forward_btnNum % int(self.win_width / 40)) * 38  # 按钮宽度+间隔=40，高度+间隔=30
        y = 10 + int(self.forward_btnNum / int(self.win_width / 40)) * 26
        if len(self.tkdata[tk_keys[self.forward_btnNum]][-1]) > 0: # 题目已经有答案，按钮蓝色
            self.scrollAreaWidgetContents.childAt(x, y).setStyleSheet("background-color:cyan;")
        else: # 题目没有选择答案，恢复原样
            self.scrollAreaWidgetContents.childAt(x, y).setStyleSheet("")
        self.forward_btnNum = n   # 存储当前按钮号，下次使用

        # 设置当前按钮颜色
        x = 10 + (n % int(self.win_width/40)) * 38  # 按钮宽度+间隔=40，高度+间隔=30
        y = 10 + int(n / int(self.win_width/40)) * 26
        self.scrollAreaWidgetContents.childAt(x, y).setStyleSheet("background-color:rgb(255, 255, 0);")

        # 清空题目、选项、答案框内容
        if len(self.scrollAreaWidgetContents_2.children()) > 0 :
            for child in self.scrollAreaWidgetContents_2.children(): # 逐个删除题目
                sip.delete(child)
        if len(self.scrollAreaWidgetContents_3.children()) > 0 :
            for child in self.scrollAreaWidgetContents_3.children(): # 逐个删除选项
                sip.delete(child)
        if len(self.scrollAreaWidgetContents_4.children()) > 0 :
            for child in self.scrollAreaWidgetContents_4.children(): # 逐个删除答案
                sip.delete(child)

        # 设置题目显示信息
        label_timu = QLabel(self.tkdata[list(self.tkdata.keys())[n]][2], self.scrollAreaWidgetContents_2)
        label_timu.move(10, 10)
        label_timu.show()

        # 设置选项显示信息
        key = list(self.tkdata.keys())[n]
        type_str = self.tkdata[key][3]
        if type_str == "单选题":
            if len(self.tkdata[key][4:-3]) > 0 :
                i = 0
                s = ""
                for itme in self.tkdata[key][4:-3]:
                    s = s + chr(i + 65) + ". " + str(itme) + "\n"
                    radio = QRadioButton(chr(i + 65), self.scrollAreaWidgetContents_4)
                    radio.move(10 + 50 * i, 10)  # 选项之间的距离50
                    radio.show()
                    radio.setFocusPolicy(Qt.NoFocus)
                    radio.clicked.connect(partial(self.radio_slot, n))  # 把题号索引传递过去

                    # 已经有答案，将按钮设置为选中状态
                    if len(self.tkdata[key][-1]) == 1: # 单选
                        if ord(self.tkdata[key][-1])-65 == i:
                            radio.setChecked(True)

                    # 指示器+1,新建下一个选项
                    i += 1

                # 显示题目
                label_timu = QLabel(s, self.scrollAreaWidgetContents_3)
                label_timu.move(10, 10)
                label_timu.show()
        elif type_str == "多选题":
            if len(self.tkdata[key][4:-3]) > 0:
                i = 0
                s = ""
                li = [ord(x) - 65 for x in self.tkdata[key][-1]]
                for itme in self.tkdata[list(self.tkdata.keys())[n]][4:-3]:
                    s = s + chr(i + 65) + ". " + str(itme) + "\n"
                    chk = QCheckBox(chr(i + 65), self.scrollAreaWidgetContents_4)
                    chk.move(10 + 50 * i, 10)  # 选项之间的距离50
                    chk.show()
                    chk.setFocusPolicy(Qt.NoFocus)
                    chk.clicked.connect(partial(self.check_slot, n))  # 把题号索引传递过去

                    # 已经有答案，将按钮设置为选中状态
                    if len(self.tkdata[key][-1]) > 0:  # 多选
                        if i in li:
                            chk.setChecked(True)

                    # 指示器+1,新建下一个选项
                    i += 1

                # 显示题目
                label_timu = QLabel(s, self.scrollAreaWidgetContents_3)
                label_timu.move(10, 10)
                label_timu.show()
        elif type_str == "判断题":
            if len(self.tkdata[key][4:-3]) > 0 :
                i = 0
                s = ""
                for itme in self.tkdata[key][4:-3]:
                    s = s + chr(i + 65) + ". " + str(itme) + "\n"
                    radio = QRadioButton(chr(i + 65), self.scrollAreaWidgetContents_4)
                    radio.move(10 + 50 * i, 10)  # 选项之间的距离50
                    radio.show()
                    radio.setFocusPolicy(Qt.NoFocus)
                    radio.clicked.connect(partial(self.radio_slot, n))  # 这个和单选题可以共用

                    # 已经有答案，将按钮设置为选中状态
                    if len(self.tkdata[key][-1]) == 1: # 单选
                        if ord(self.tkdata[key][-1])-65 == i:
                            radio.setChecked(True)

                    # 指示器+1,新建下一个选项
                    i += 1

                # 显示题目
                label_timu = QLabel(s, self.scrollAreaWidgetContents_3)
                label_timu.move(10, 10)
                label_timu.show()
        elif type_str == "填空题":
            let = QLineEdit(self.scrollAreaWidgetContents_4)
            let.resize(self.scrollAreaWidgetContents_4.width(), self.scrollAreaWidgetContents_4.height())
            let.textChanged.connect(partial(self.text_changed, n))
            let.show()
            if self.tkdata[list(self.tkdata.keys())[n]][-1] == "":
                let.setPlaceholderText("请输入答案，并用分号（；）隔开")
            else:
                let.setText(self.tkdata[key][-1])
            let.setFocus()
        elif type_str == "问答题":
            let = QTextEdit(self.scrollAreaWidgetContents_4)
            let.resize(self.scrollAreaWidgetContents_4.width(), self.scrollAreaWidgetContents_4.height())
            let.textChanged.connect(partial(self.text_changed1, n))
            let.show()
            if self.tkdata[key][-1] == "":
                let.setPlaceholderText("请输入你的答案！")
            else:
                let.setText(self.tkdata[key][-1])
                # let.toPlainText()
            let.setFocus()
        else: # 其他情况不操作
            pass

    # 填空题槽函数
    def text_changed(self, n):
        text = self.scrollAreaWidgetContents_4.children()[0].text()
        self.tkdata[list(self.tkdata.keys())[n]][-1] = text  # 存入答案

    # 填空题槽函数
    def text_changed1(self, n):
        text = self.scrollAreaWidgetContents_4.children()[0].toPlainText()
        self.tkdata[list(self.tkdata.keys())[n]][-1] = text  # 存入答案

    # 多选选项槽函数
    def check_slot(self, n):
        self.tkdata[list(self.tkdata.keys())[n]][-1] = ""
        for chk in self.scrollAreaWidgetContents_4.children():
            if chk.isChecked():
                s = chr(self.scrollAreaWidgetContents_4.children().index(chk) + 65)
                self.tkdata[list(self.tkdata.keys())[n]][-1] += s  # 存入答案

    # 单选选项槽函数，判断题共用
    def radio_slot(self, n):
        for radio in self.scrollAreaWidgetContents_4.children():
            s = ""
            if radio.isChecked():
                s = s + chr(self.scrollAreaWidgetContents_4.children().index(radio) + 65)
                self.tkdata[list(self.tkdata.keys())[n]][-1] = s  # 存入答案

    # 提交考试槽函数
    def submit_test(self):

        # 计算考生成绩
        score = 0
        ls1 = ["单选题", "多选题", "判断题", "填空题", "问答题"]
        for key in self.tkdata:
            if self.tkdata[key][3] in ["单选题", "判断题"]: # 单选、判断
                if self.tkdata[key][-1] == self.tkdata[key][-3]:
                    score += self.test_vals[ls1.index(self.tkdata[key][3])]
            elif self.tkdata[key][3] == "多选题": # 多选
                k1 = list(self.tkdata[key][-1])
                k1.sort()
                k2 = list(self.tkdata[key][-3])
                k2.sort()
                if k1 == k2:
                    score += self.test_vals[ls1.index(self.tkdata[key][3])]
            elif self.tkdata[key][3] == "填空题": # 填空
                # todo 这里可以对填空题得分进行优化处理
                k1 = re.split('[;；,，。 ]', str(self.tkdata[key][-1]))
                k2 = re.split('[;；,，。 ]', str(self.tkdata[key][-3]))
                if k1 == k2:
                    score += self.test_vals[ls1.index(self.tkdata[key][3])]
            elif self.tkdata[key][3] == "问答题": # 问答
                if self.tkdata[key][-1] == self.tkdata[key][-3]:
                    score += self.test_vals[ls1.index(self.tkdata[key][3])]
            else:
                pass

        # 显示考试相关信息
        tmp3 = str(int(self.test_time2)-self.test_time)

        s1 = "本次考试结束：\n" \
             "      试卷名称：" + str(self.name) + "\n" \
             "      考试时长：" + str(self.test_time2) + "分钟\n" \
             "      考试用时：" + tmp3 + "分钟\n" \
             "      得　　分：" + str(score)
        QMessageBox.about(self, "考试结束", s1)

        # todo 考试结束,处理后续问题,这里没有存储用户信息
        # 1.试卷的存储，用户信息，考试信息，结果
        test_resualt_all = readjson("data/test_resualt_all.json")
        if len(test_resualt_all) == 0:
            test_resualt_all = {}

        # 重新命名，存储考试信息
        t = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        a, b = str(self.name).split("-")
        new_name = str(t) + '-' + b

        test_resualt_all[new_name] = [self.currentuser, self.test_time2, tmp3, score, self.test_nums, self.test_vals, self.tkdata, self.suiji]
        writejson("data/test_resualt_all.json", test_resualt_all)


        # 发送一个考试结束的信号，传递相关信息，在外部进行后续处理
        sums = sum(self.test_nums)
        sumscore = 0
        for i in range(5):
            sumscore += self.test_vals[i] * self.test_nums[i]
        self.test_finished_signal.emit([t, b, sums, sumscore, score])

        self.close()


    # 上一题按钮槽函数
    def prev_clicked(self):
        if self.forward_btnNum == 0:
            self.btn_pressed(len(self.tkdata) - 1)
        else:
            self.btn_pressed(self.forward_btnNum-1)

    # 下一题按钮槽函数
    def next_clicked(self):
        if self.forward_btnNum == len(self.tkdata)-1:
            self.btn_pressed(0)
        else:
            self.btn_pressed(self.forward_btnNum+1)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    data = readjson("data/defaulttest.json")
    win = testPane(data, "dll")
    win.show()
    sys.exit(app.exec_())
