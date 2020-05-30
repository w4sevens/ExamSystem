# encoding: utf-8
# @author: w4dll
# @file: test_pane.py
# @time: 2020/4/29 19:39

from resource.moniUI import Ui_Form
from PyQt5.Qt import *
from PyQt5 import sip
from functools import partial
from mytool import *

class moniPane(QWidget, Ui_Form):

    test_finished_signal = pyqtSignal(list)  # 考试结束信号

    def __init__(self, data, name, parent = None, *args, **kwargs):
        super(moniPane, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)

        self.name = name
        self.tkdata = data              # 考题
        self.forward_btnNum = 0         # 这个要放在initUi前面

        # 初始化界面题号
        self.initUi()
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)


    # 根据用户传入的题库信息dict_tiku初始化考试界面
    def initUi(self):
        self.scrollAreaWidgetContents.setMinimumSize(1000, 50 + int(26 * len(self.tkdata) / 25))

        # todo 初始化按钮界面
        if len(self.tkdata) > 0 :
            i = 0
            for item in self.tkdata:  # 根据题目数量，建立相应的题号按钮
                btn = QPushButton(self.scrollAreaWidgetContents)
                btn.resize(35, 20)  # 设置按钮的高度和宽度
                btn.setText(str(i + 1))
                btn.setFocusPolicy(Qt.NoFocus)

                self.win_width = self.scrollAreaWidgetContents.width()      # 这个值是变化的，所以这里存储便于后面使用

                x = 10 + (i % int(self.win_width/40)) * 38                  # 按钮宽度+间隔=40，高度+间隔=30
                y = 10 + int(i / int(self.win_width/40)) * 26
                btn.move(x, y)

                btn.clicked.connect(partial(self.btn_pressed, i))           # 这个函数可以实现参数传递
                self.tkdata[item].append("")         # 将用户选择答案赋在题库后面
                i += 1
            self.btn_pressed(0)  # 调用一下第一个按钮，显示初始题目状态
        else:
            print("题库信息为空")
            self.close()

    # 题号按钮点击槽函数
    def btn_pressed(self, n):  # n->表示题目索引号，从0开始

        key = list(self.tkdata.keys())[n]
        # 如果做过题目，显示答案
        ans1 = self.tkdata[key]
        if len(ans1[-1]) > 0: # 题目已经有答案，按钮蓝色
            self.label_ans.setText("正确答案："+ ans1[-3])
        else:
            self.label_ans.setText("正确答案：")

        # 恢复前一个按钮颜色
        x = 10 + (self.forward_btnNum % int(self.win_width / 40)) * 38  # 按钮宽度+间隔=40，高度+间隔=30
        y = 10 + int(self.forward_btnNum / int(self.win_width / 40)) * 26
        ans = self.tkdata[list(self.tkdata.keys())[self.forward_btnNum]]
        if len(ans[-1]) > 0: # 题目已经有答案，按钮蓝色
            if ans[-1] == ans[-3]:
                self.scrollAreaWidgetContents.childAt(x, y).setStyleSheet("background-color:cyan;")
            else:
                self.scrollAreaWidgetContents.childAt(x, y).setStyleSheet("background-color:red;")
        else: # 题目没有选择答案，恢复原样
            self.scrollAreaWidgetContents.childAt(x, y).setStyleSheet("")
        self.forward_btnNum = n   # 存储当前按钮号，下次使用

        # 设置当前按钮颜色
        x = 10 + (n % int(self.win_width/40)) * 38  # 按钮宽度+间隔=40，高度+间隔=30
        y = 10 + int(n / int(self.win_width/40)) * 26
        self.scrollAreaWidgetContents.childAt(x, y).setStyleSheet("background-color: rgb(255, 255, 0);")

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
        s1 = str(self.tkdata[key][2])
        label_timu = QLabel(s1, self.scrollAreaWidgetContents_2)
        label_timu.move(10, 10)
        label_timu.show()

        # 设置选项显示信息
        if self.tkdata[key][3] == "单选题":
            if len(self.tkdata[key][4:-3]) > 0 :  # 选项存在
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
        elif self.tkdata[key][3] == "多选题":
            if len(self.tkdata[key][4:-3]) > 0:
                i = 0
                s = ""
                li = [ord(x) - 65 for x in self.tkdata[key][-1]]
                for itme in self.tkdata[key][4:-3]:
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
        elif self.tkdata[key][3] == "判断题":
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
                    if len(self.tkdata[key][-1]) == 1: # 判断
                        if ord(self.tkdata[key][-1])-65 == i:
                            radio.setChecked(True)

                    # 指示器+1,新建下一个选项
                    i += 1

                # 显示题目
                label_timu = QLabel(s, self.scrollAreaWidgetContents_3)
                label_timu.move(10, 10)
                label_timu.show()
        elif self.tkdata[key][3] == "填空题":
            let = QLineEdit(self.scrollAreaWidgetContents_4)
            let.resize(self.scrollAreaWidgetContents_4.width(), self.scrollAreaWidgetContents_4.height())
            let.textChanged.connect(partial(self.text_changed, n))
            let.show()
            if self.tkdata[key][-1] == "":
                let.setPlaceholderText("请输入答案，并用分号（；）隔开")
            else:
                let.setText(self.tkdata[key][-1])
            let.setFocus()
        elif self.tkdata[key][3] == "问答题":
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

        # 写入模拟考试的信息
        # 用户错题信息
        if QMessageBox.Yes == QMessageBox.question(self, "提示", "是否存储错题？"):
            self.wrong, self.right= {}, {}
            for key in self.tkdata:
                if self.tkdata[key][-1] != "":
                    if self.tkdata[key][-1] != self.tkdata[key][-3]:
                        self.wrong[key] = self.tkdata[key]
                        self.wrong[key].pop()
                    else:
                        self.right[key] = self.tkdata[key]
                        self.right[key].pop()

            # 如果错题集存在，存入，如果做对了，剔除错题
            dd = readjson("data/wrong_tiku.json")
            if len(dd) == 0:
                dd = {}
            if self.name in dd:
                for item in self.right: # 去掉对的
                    if self.right[item] in dd[self.name].values():
                        dd[self.name].pop(item)
                for item in self.wrong: # 添加错题
                    if self.wrong[item] not in dd[self.name].values():
                        dd[self.name][item] = self.wrong[item]
            else:
                dd[self.name] = self.wrong
            writejson("data/wrong_tiku.json", dd)
            QMessageBox.about(self, "提示", "错题存储成功！")

        self.close()

    def keyReleaseEvent(self, evt) -> None:
        super(moniPane, self).keyReleaseEvent(evt)
        if evt.key() == 16777234:
            self.prev_clicked()
        elif evt.key() == 16777235:
            a = self.forward_btnNum - 25
            if a < 0:
                a += len(self.tkdata) - len(self.tkdata) % 25 + 25
                if a > len(self.tkdata)-1:
                    a = a - 25
            self.btn_pressed(a)
        elif evt.key() == 16777236:
            self.next_clicked()
        elif evt.key() == 16777237:
            a = self.forward_btnNum + 25
            if a > len(self.tkdata)-1:
                a = a % 25
            self.btn_pressed(a)
        else:
            pass

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
    win = moniPane(data[list(data.keys())[0]][3], "dll")
    win.show()
    sys.exit(app.exec_())
