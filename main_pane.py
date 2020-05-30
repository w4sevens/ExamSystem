# encoding: utf-8
# @author: w4dll
# @file: main_pane.py
# @time: 2020/4/23 19:41
import os
from PyQt5.Qt import *
from mytool import *
from paperset_pane import PapersetPane
from resource.mainUI import Ui_MainWindow
from resource.tk_add import Ui_Dialog
from moni_pane import moniPane
from test_pane import testPane
from papermanage_pane import paperManagePane
from usermanage_pane import userManegePane
from tk_guanli_pane import tkGuanli
from score_tongji_pane import scoreTongji
from addtestpaper_pane import AddPaperTest
from suijiSet_pane import suijiSetPane
import time

import locale
locale.setlocale(locale.LC_ALL, 'en')

class MainPane(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.initSlot()

    # 初始化信号-槽连接
    def initSlot(self):
        self.action_tianjiashijuan.triggered.connect(self.paperset)         # 试卷添加
        self.action_shijuanguanli.triggered.connect(self.papermanagement)   # 试卷管理
        self.action_daorushijuan.triggered.connect(self.importSJ)           # 导入试卷
        self.actiond_daochushijuan.triggered.connect(self.outputSJ)         # 导出试卷
        self.actiond_qingkongshijuan.triggered.connect(self.clearSJ)        # 清空试卷

        self.action_daorutiku.triggered.connect(self.importTk)              # 导入题库
        self.action_daochutiku.triggered.connect(self.tk_output)            # 导出题库到Excel文件中
        self.action_qingkongtiku.triggered.connect(self.tk_clear)           # 清空题库
        self.action_tikuguanli.triggered.connect(self.tk_guanli)            # 题库管理

        self.action_kaishikaoshi.triggered.connect(self.on_start)           # 开始考试
        self.action_suiji_test.triggered.connect(self.suiji_test)           # 随机考试
        self.action_suiji_set.triggered.connect(self.suiji_set)             # 随机设置


        self.actionuser_guanli.triggered.connect(self.usermanage)           # 用户管理
        self.actionuser_daochu.triggered.connect(self.userOutput)           # 导出用户信息
        self.actionuser_daoru.triggered.connect(self.userImport)            # 导入用户信息

        self.action_chengjitongji.triggered.connect(self.socre_tongji)      # 成绩统计

        self.action_close.triggered.connect(self.close_mainUi)              # 关闭主界面
        self.action_outputdata.triggered.connect(self.output_data)          # 导出数据
        self.action_importdata.triggered.connect(self.import_data)          # 导入数据

        self.action_tiku_moban.triggered.connect(self.get_tiku_moban)       # 生成题库模板

        # 初始化列表
        self.initList()

    def get_tiku_moban(self):
        filepath, _ = QFileDialog.getSaveFileName(self, "请选择模板存储路径", "./", "excel(*.xlsx)")
        if len(filepath) > 0:
            wb = workbook.Workbook()
            first_row = ["题目", "题型", "选项A", "选项B", "选项C", "选项D", "选项E", "选项F", "选项G", "选项H", "选项I", "选项J", "答案", "备注"]
            first_row1 = ["谁是最可爱的人？", "单选题", "解放军叔叔", "车夫", "商贩", "小偷", "", "", "", "", "", "", "A", ""]
            first_row2 = ["谁是最可爱的人们？", "多选题", "解放军叔叔", "车夫", "商贩", "小偷", "学生", "哥哥", "", "", "", "", "AB", ""]
            first_row3 = ["我最可爱的人们？", "判断题", "对", "错", "", "", "", "", "", "", "", "", "A", ""]
            first_row4 = ["我最爱(   )？", "填空题", "", "", "", "", "", "", "", "", "", "", "妈妈", ""]
            first_row5 = ["请简述火箭的发射原理？", "问答题", "", "", "", "", "", "", "", "", "", "", "嘟嘟嘟嘟嘟嘟嘟嘟嘟嘟嘟嘟嘟嘟，嘭！", ""]
            wb.worksheets[0].append(first_row)
            wb.worksheets[0].append(first_row1)
            wb.worksheets[0].append(first_row2)
            wb.worksheets[0].append(first_row3)
            wb.worksheets[0].append(first_row4)
            wb.worksheets[0].append(first_row5)
            wb.save(filepath)

    # 导出数据
    def output_data(self):
        d0 = {}
        d0["a"] = readjson("data/shijuan_all.json")
        d0["b"] = readjson("data/test_resualt_all.json")
        d0["c"] = readjson("data/userinfo.json")

        filepath, _ = QFileDialog.getSaveFileName(self, "导出数据", "./", "json(*.json)")
        if filepath == "":
            return
        writejson(filepath, d0)
        QMessageBox.about(self, "提示", "导出成功！")

    # 导入数据
    def import_data(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "导入数据", "./", "json文件(*.json)")
        if len(filepath) > 0:
            if os.path.isfile(filepath):
                data = readjson(filepath)
                try:
                    shijuan = data["a"]
                    test_resualt = data["b"]
                    userinfo = data["c"]
                except:
                    QMessageBox.about(self, "提示", "导入错误！")
                    return

                # 导入试卷
                old_shijuan = readjson("data/shijuan_all.json")
                for x in shijuan:
                    if x not in old_shijuan:
                        old_shijuan[x] = shijuan[x]
                writejson("data/shijuan_all.json", old_shijuan)

                # 导入考试结果
                old_test_result = readjson("data/test_resualt_all.json")
                for x in test_resualt:
                    if x not in old_test_result:
                        old_test_result[x] = test_resualt[x]
                writejson("data/test_resualt_all.json", old_test_result)

                # 导入用户信息
                old_userinfo = readjson("data/userinfo.json")
                for x in userinfo:
                    if x not in old_userinfo:
                        old_userinfo[x] = userinfo[x]
                writejson("data/userinfo.json", old_userinfo)

        # 刷新用户信息，单位信息
        self.refreshtikusInfo()
        self.frushUnitsinfo()
        self.frushlist4()

    # 关闭主界面
    def close_mainUi(self):
        self.close()
    # 随机设置
    def suiji_set(self):
        self.win_suiji_set = suijiSetPane()
        self.win_suiji_set.setWindowModality(Qt.ApplicationModal)
        self.win_suiji_set.show()

    # 设置用户图标
    def setuserIcon(self):
        # QLabel().setStyleSheet()
        data = readjson("data/userinfo.json")
        if len(data) == 0:
            return
        if self.username in data:
            p = data[self.username][-1]
            if p == "超级管理员":
                self.label_picture.setStyleSheet("border-image:url(:/login/images/超级管理员.png);")
            elif p == "管理员":
                    self.label_picture.setStyleSheet("border-image:url(:/login/images/管理员.png);")
            else:
                self.label_picture.setStyleSheet("border-image:url(:/login/images/一般用户.png);")

    # 生成试卷按钮
    def get_testpaper(self):
        dd = self.get_timuInList3()
        if len(dd) > 0:
            self.win_getpaper = AddPaperTest(dd)
            self.win_getpaper.add_test_signal.connect(self.frushlist4)    # 添加成功，刷新列表
            self.win_getpaper.setWindowModality(Qt.ApplicationModal)
            self.win_getpaper.show()
        else:
            QMessageBox.about(self, "提示", "请先添加题库！")

    # 统计成绩菜单
    def socre_tongji(self):
        self.win_tongji = scoreTongji()
        self.win_tongji.setWindowModality(Qt.ApplicationModal)
        self.win_tongji.show()

    # list4行选中
    def row_select4(self):
        rowindex = self.tableView.selectionModel().selection().indexes()
        s = self.list_model4.data(rowindex[0])
        self.label_14.setText(s)
        self.pushButton_5.setEnabled(True)
        self.pushButton_7.setEnabled(True)

        # 考试信息写入默认试卷
        data = readjson("data/shijuan_all.json")
        if len(data) == 0:
            return
        writejson("data/defaulttest.json", {s: data[s]})

        self.setdefautinfo()

    # 随机考试按钮
    def suiji_test(self):
        data = readjson("data/defaulttest.json")
        if len(data) > 0:
            data_num_val = readjson("data/suiji_set.json")
            list1 = [[], [], [], [], []]
            ls = ["单选题", "多选题", "判断题", "填空题", "问答题"]
            dict_tiku = {}
            if len(data_num_val) > 0:
                nums, vals = data_num_val
                key = list(data.keys())[0]

                # 题库归类存入list1
                tiku = data[key][3]
                for x in tiku:
                    list1[ls.index(tiku[x][3])].append(x)

                # 取最大题量
                for i in range(5):
                    if nums[i] > data[key][1][i]:
                        nums[i] = data[key][1][i]
                    ls_num = get_random(nums[i], len(list1[i]))
                    for j in ls_num:
                        key1 = list1[i][j]
                        dict_tiku[key1] = tiku[key1]
                new_data = {}
                new_data[key] = [data[key][0], nums, vals, dict_tiku]
                self.startTest(new_data, "随机考试")

    # 开始考试按钮
    def start_test4(self):
        self.on_start()

    # 清空题库
    def tk_clear(self):
        if QMessageBox.Yes == QMessageBox.question(self, "提示", "是否清空题库，清空后不可恢复！"):
            writejson("data/tiku.json", {})
            writejson("data/tkinfo.json", {})
            self.initList()

    # 题库管理
    def tk_guanli(self):
        # 显示题库，可以进行修改，删除等操作
        self.win_tk_guanli = tkGuanli()
        self.win_tk_guanli.setWindowModality(Qt.ApplicationModal)
        self.win_tk_guanli.tk_guanli_complete.connect(self.tk_guanli_ok)  # 刷新题库信息
        self.win_tk_guanli.show()

    # 题库管理确定
    def tk_guanli_ok(self):
        self.refreshtikusInfo()
        self.initList()

    # 初始化list
    def initList(self):
        # self.pushButton.setEnabled(False)
        # self.pushButton_2.setEnabled(False)
        # self.pushButton_6.setEnabled(False)

        # 定义model
        self.list_model = QStandardItemModel()

        self.list_model2 = QStandardItemModel()
        self.listView_2.setModel(self.list_model2)

        self.list_model3 = QStandardItemModel()
        self.listView_3.setModel(self.list_model3)
        self.listView_3.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.tkinfo = readjson("data/tkinfo.json")
        if len(self.tkinfo) > 0:
            list_item = []
            for d1 in self.tkinfo:
                list_item.append(QStandardItem(d1))
            self.list_model.appendColumn(list_item)

        self.listView.setModel(self.list_model)
        self.listView.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置表格的选取方式是行选取

        self.frushlist4()

    # 刷新list4
    def frushlist4(self):
        # 初始化tableview
        self.list_model4 = QStandardItemModel()
        self.list_model4.setHorizontalHeaderLabels(["试卷名称", "考试时长", "题目数量", "总分"])
        data = readjson("data/shijuan_all.json")
        if len(data) > 0:
            # 添加数据
            for key in data:
                li = []
                q1 = QStandardItem(str(key))
                q1.setTextAlignment(Qt.AlignCenter)  # 设置单元格居中显示
                li.append(q1)

                q2 = QStandardItem(str(data[key][0]))
                q2.setTextAlignment(Qt.AlignCenter)

                li.append(q2)

                tmp1, tmp2 = data[key][1:3]
                nums, vals = 0, 0
                for i in range(5):
                    nums += tmp1[i]
                    vals += tmp1[i] * tmp2[i]
                q3 = QStandardItem(str(nums))
                q3.setTextAlignment(Qt.AlignCenter)
                li.append(q3)
                q4 = QStandardItem(str(vals))
                q4.setTextAlignment(Qt.AlignCenter)
                li.append(q4)
                self.list_model4.appendRow(li)
        self.tableView.setModel(self.list_model4)
        # self.tableView.horizontalHeader().setStretchLastSection(True)
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)           # 所有列都扩展自适应宽度，填充充满整个屏幕宽度
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)    # 所有列都扩展自适应宽度，填充充满整个屏幕宽度

        # 设置列固定宽度
        self.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.tableView.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.tableView.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
        self.tableView.setColumnWidth(0, 239)
        self.tableView.setColumnWidth(1, 80)
        self.tableView.setColumnWidth(2, 80)
        self.tableView.setColumnWidth(3, 80)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置表格行选中模式

        self.tableView.verticalHeader().hide()

    # 第一个list行选中
    def row_select(self, index):
        self.listView_3.setCurrentIndex(QModelIndex())
        self.pushButton_2.setEnabled(False)
        self.pushButton.setEnabled(False)

        self.list_model2.clear()
        d = index.data()
        if d in self.tkinfo.keys():
            list_item = []
            for d1 in self.tkinfo[d]:
                list_item.append(QStandardItem(d1))
            self.list_model2.appendColumn(list_item)
            self.listView_2.setModel(self.list_model2)
            self.listView_2.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置表格的选取方式是行选取

    # 第二个list行选中
    def row_select1(self):
        self.listView_3.setCurrentIndex(QModelIndex())
        self.pushButton_2.setEnabled(False)

        if self.listView_2.currentIndex().row()>-1:
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)

    # 第三个list行选中
    def row_select2(self):
        if self.listView_3.currentIndex().row() > -1:
            self.pushButton_2.setEnabled(True)
            self.pushButton_6.setEnabled(True)
        else:
            self.pushButton_2.setEnabled(False)
            self.pushButton_6.setEnabled(False)

    # 添加按钮
    def add_tiku(self):
        s = self.listView.currentIndex().data() + "-" + self.listView_2.currentIndex().data()

        # 判断是否在list3里边
        if not any([s == self.list_model3.data(self.list_model3.index(i, 0)) for i in range(self.list_model3.rowCount())]):
            self.list_model3.appendRow(QStandardItem(s))

        self.pushButton.setEnabled(False)

    # 删除按钮
    def delete_tiku(self):
        for index in self.listView_3.selectedIndexes():
            self.list_model3.removeRow(index.row())

        self.pushButton_2.setEnabled(False)

    # 获取题库，从list3中选取所有题目
    def get_timuInList3(self):
        # 获取题库信息
        dict_tk = {}
        data = readjson("data/tiku.json")

        # 获取list3所有数据，拆解
        list_tiku = [self.list_model3.data(self.list_model3.index(i, 0)) for i in range(self.list_model3.rowCount())]

        # 存储（范围，专业），逐个取出每一个元素比对，存入符合条件的
        ls01 = []
        for x in list_tiku:
            a, b = x.split("-")
            ls01.append((a, b))
        for item in data:
            if (data[item][0], data[item][1]) in ls01:
                dict_tk[item] = data[item]
        return dict_tk

    # 模拟考试按钮,根据选择内容，选取所有考试题目
    def start_test(self):

        # 获取题库信息
        dict_tk = self.get_timuInList3()

        # 开始模拟考试
        if len(dict_tk) > 0:
            if QMessageBox.Yes == QMessageBox.question(self, "模拟练习", "是否开始模拟练习？"):
                self.win_kaoshi = moniPane(dict_tk, self.label_currentUser.text())
                self.win_kaoshi.setWindowModality(Qt.ApplicationModal)  # 设置为应用程序级别的模态
                self.win_kaoshi.show()
        else:
            QMessageBox.question(self, "提示", "请先添加题库信息！")

    # 我的错题按钮
    def wrong_test(self):
        data = readjson("data/wrong_tiku.json")
        if len(data) == 0:
            QMessageBox.about(self, "提示", "您当前还没有添加错题！")
            return
        if self.username in data.keys():
            mydata = data[self.username]

            # 开始模拟考试
            if len(mydata) > 0:
                if QMessageBox.Yes == QMessageBox.question(self, "错题练习", "是否开始错题练习？"):
                    self.win_kaoshi = moniPane(mydata, self.label_currentUser.text())
                    self.win_kaoshi.setWindowModality(Qt.ApplicationModal)  # 设置为应用程序级别的模态
                    self.win_kaoshi.show()
            else:
                QMessageBox.question(self, "提示", "错题集中没有您的错题！")
        else:
            QMessageBox.about(self, "提示", "您当前还没有添加错题！")

    # 随机选择框
    def chk_random(self, b):
        pass

    # 顺序选择框
    def chk_seq(self, b):
        pass

    # 错题选择框
    def chk_myfalse(self, b):
        pass

    # 我的收藏选择框
    def chk_myfavor(self, b):
        pass

    # 设置权限-用在show重载最后
    def setPriority(self):
        # todo 如果错误删除用户，导致这里不成立
        data = readjson("data/userinfo.json")
        if self.username in data.keys():
            p = data[self.username][-1]

            if p == "一般用户":
                self.actionuser_guanli.setEnabled(False)
                self.actionuser_daochu.setEnabled(False)
                self.actionuser_daoru.setEnabled(False)

                self.action_shijuanguanli.setEnabled(False)
                self.action_daochutiku.setEnabled(False)
                self.actiond_daochushijuan.setEnabled(False)
                self.actiond_qingkongshijuan.setEnabled(False)
                self.action_qingkongtiku.setEnabled(False)
                self.action_tikuguanli.setEnabled(False)

    # 导出用户
    def userOutput(self):
        filepath, _ = QFileDialog.getSaveFileName(self, "导出用户信息到json文件", "./", "json文件(*.json)")
        if len(filepath) > 0:
            data = readjson("data/userinfo.json")
            writejson(filepath, data)
            QMessageBox.about(self, "提示", "导出成功！")

    # 导入用户
    def userImport(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "导入用户信息", "./", "json文件(*.json)")
        if len(filepath) > 0:
            if os.path.isfile(filepath):
                try:
                    data_import = readjson(filepath)
                    data = readjson("data/userinfo.json")
                    for key in data_import.keys():
                        if key in data.keys():
                            s = "用户" + key + "已存在，是否替换！"
                            if QMessageBox.Yes == QMessageBox.question(self, "提示", s):
                                data.pop(key)
                                data[key] = data_import[key]
                            else:
                                pass
                        else:
                            data[key] = data_import[key]
                    writejson("data/userinfo.json", data)
                    QMessageBox.about(self, "提示", "导入成功！")
                except:
                    QMessageBox.about(self, "提示", "导入失败！")

            else:
                QMessageBox.about(self, "提示", "文件路径错误！")
        self.frushUnitsinfo()

    def frushUnitsinfo(self):
        data = readjson("data/userinfo.json")
        if len(data) == 0:
            return

        units = {}
        for key in data:
            a, b, c = data[key][3:6]
            if a in units:
                if b in units[a]:
                    units[a][str(b)] = [c]
                else:
                    if b != "":
                        units[a][str(b)] = [c]
            else:
                if b == "":
                    units[a] = {}
                else:
                    units[a] = {}  # 需要新建二级字典，才可以赋值，否则报错
                    units[a][b] = [c]
        writejson("data/unitsinfo.json", units)

    # 用户管理菜单
    def usermanage(self):
        self.userpane = userManegePane(self.username)
        self.userpane.setWindowModality(Qt.ApplicationModal)
        self.userpane.user_changed_singal.connect(self.frushUnitsinfo)  # 刷新单位信息
        self.userpane.show()

    # 重载显示事件，获取在父程序中设置用户名信息
    def showEvent(self, evt):
        super(MainPane, self).showEvent(evt)
        self.username = self.label_currentUser.text()  # 这里是父程序设置的！！慎用！！！
        self.setPriority()

        self.setuserIcon()

        # 根据用户信息，设置其他信息
        data = readjson("data/userinfo.json")
        if len(data) > 0:
            _, name, sex, d1, d2, d3, regtime, priority = data[self.username]
            self.label_username.setText(name)
            self.label_units1.setText(d1)
            self.label_units2.setText(d2)
            self.label_units3.setText(d3)

        # 设置时间显示
        # import locale
        # locale.setlocale(locale.LC_ALL, 'zh-cn')
        t = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        self.label_currenttime.setText(t)
        # todo 上面的时间显示报错！！！

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.refrush)

        # 设置试卷信息
        self.setdefautinfo()

    # 显示默认题库槽函数
    def setdefautinfo(self):
        data = readjson("data/defaulttest.json")
        if len(data) > 0 :
            testname = list(data.keys())[0]
            testtime = data[testname][0]
            nums = data[testname][1]
            vals = data[testname][2]
            score = 0
            for i in range(5):
                score += nums[i] * vals[i]
            self.label_default.setText(testname)
            self.label_14.setText(testname)
            self.label_testtime.setText(testtime)
            self.label_nums.setText(str(sum(data[testname][1])))
            self.label_scores.setText(str(score))
            self.label_score.setText("")
            self.label_scoretime.setText("")
        else:
            self.label_default.setText("未设置")
            self.label_14.setText("未设置")

    # 时间刷新
    def refrush(self):

        t = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        self.label_currenttime.setText(t)

    # 试卷管理菜单
    def papermanagement(self):
        self.ma = paperManagePane(self)
        # self.ma.setdefault_signal.connect(self.setdefautinfo)
        self.ma.delete_testpaper.connect(self.signal_delete_test)
        if self.ma.flage == 0:
            self.ma.open()

    def signal_delete_test(self):
        self.setdefautinfo()
        self.frushlist4()

    # 开始考试菜单
    def on_start(self):
        # 获取默认设置的题库
        data = readjson("data/defaulttest.json")
        self.startTest(data)

    # 考试函数
    def startTest(self, data, str_test = "顺序考试"):
        if len(data) > 0:
            question = data[list(data.keys())[0]][3]
            if len(question) > 0:
                a, b = str(list(data.keys())[0]).split("-")
                s = "即将开始【" + b + "】考试，考试时长" + data[list(data.keys())[0]][0] + "分钟，是否开始？"
                if QMessageBox.Yes == QMessageBox.question(self, "开始考试", s):
                    # 初始化界面
                    self.win_kaoshi = testPane(data, self.label_currentUser.text())
                    self.win_kaoshi.setWindowTitle("正在进行【" + b + "】考试")
                    self.win_kaoshi.suiji = str_test
                    self.win_kaoshi.setWindowModality(Qt.ApplicationModal)   # 设置为应用程序级别的模态
                    self.win_kaoshi.show()
                    self.win_kaoshi.test_finished_signal.connect(self.showtestresult)
            else:
                QMessageBox.about(self, "提示", "默认试卷中没有找到题目信息，请先设置！")
        else:
            # 没有设置默认题库，请先设置
            QMessageBox.about(self, "提示", "请先设置默认试卷！")

    # 显示考试结果槽函数
    def showtestresult(self, list_result):
        self.label_score.setText(str(list_result[-1]))
        self.label_scoretime.setText(str(list_result[0]))

    # 导出题库菜单
    def tk_output(self):
        filepath, _ = QFileDialog.getSaveFileName(self, "导出题库到Excel文件", "./", "excel(*.xlsx)")
        if len(filepath) > 0:
            data = readjson("data/tiku.json")
            if len(data) > 0 :
                # 通过返回值判断导入是否成功！
                if writeToExcel(filepath, data):
                    QMessageBox.about(self, "提示", "导出题库成功！")
                else:
                    QMessageBox.about(self, "提示", "导出题库失败！")
            else:
                QMessageBox.about(self, "提示", "题库为空！")

    # 选择导入的文件,导入
    def choosefile(self):
        # 根据用户选择，清空后导入题库，或导入后去重
        flag1 = self.d.checkBox.isChecked()
        flag2 = self.d.checkBox_2.isChecked()
        self.dialog.close()

        file, _ = QFileDialog.getOpenFileName(self, "选择题库", "./", "All(*.*);;excel(*.xlsx)", "excel(*.xlsx)")
        # a, b = re.split('[/ -.]', file)[-3:-1]  # 分离出单位、专业
        if len(file) > 0:  # 文件存在
            # 添加验证信息，判断题库是否为：“单位-专业.xlsx"类型
            my_regex = re.compile(".+-.+\\.xlsx")
            if len(my_regex.findall(file)) == 0:   # 名称合法，进行后续操作
                QMessageBox.about(self, "提示", "导入题库名称不合法！")
                return

            if flag1: # 追加后去重
                old_tiku = readjson("data/tiku.json")
                len1 = len(old_tiku)
                if len1 > 0:
                    new_tiku = importExcelTk(file)

                    # 把题目逐个取出，存入文件
                    for item in new_tiku:
                        if item not in old_tiku.values():
                            # 从1开始递增，直到取到没有的题库，为题库号
                            i = 1
                            while(str(i) in old_tiku.keys()):
                                i += 1
                            old_tiku[str(i)] = item
                else: # 题库文件为空，新建
                    old_tiku = {}
                    new_tiku = importExcelTk(file)
                    ls, i = {}, 1
                    for item in new_tiku:
                        old_tiku[str(i)] = item
                        i += 1

                # 写入题库
                writejson("data/tiku.json", old_tiku)

            if flag2: #清空后添加
                old_tiku = {}
                new_tiku = importExcelTk(file)
                ls, i = {}, 1
                for item in new_tiku:
                    old_tiku[str(i)] = item
                    i += 1

                # 写入题库
                writejson("data/tiku.json", old_tiku)

            # 刷新题库信息,存入文件
            self.refreshtikusInfo()
            self.initList()
        else:
            print("没有选择题库文件，不操作！")

    # 刷新单位信息
    def refreshtikusInfo(self):
        # 刷新题库信息,存入文件
        old_tiku = readjson("data/tiku.json")
        if len(old_tiku) == 0:
            writejson("data/tkinfo.json", {})
            return
        ls = {}
        for val in old_tiku.values():
            a, b = val[0], val[1]
            if a in ls.keys():
                if b not in ls[a]:
                    ls[a].append(b)
            else:
                ls[a] = [b]
        writejson("data/tkinfo.json", ls)

    def enabel_choose(self):
        # 使模对话框选择文件按钮可用
        self.d.pushButton.setEnabled(True)

    # 导入题库菜单
    def importTk(self):
        # 导入题库，构建一个模对话框
        self.dialog = QDialog(self)
        self.d = Ui_Dialog()
        self.dialog.on_clicked = self.choosefile
        self.dialog.on_enable = self.enabel_choose
        self.d.setupUi(self.dialog)
        self.dialog.setWindowTitle("选择题库文件（*.xlsx)")
        self.dialog.open()

    # 添加试卷菜单
    def paperset(self):
        self.papersetUI = PapersetPane(self)
        self.papersetUI.add_test_signal.connect(self.frushlist4)
        self.papersetUI.open()

    # 导入试卷菜单
    def importSJ(self):
        # todo 导入试卷，刷新list1
        filepath, _ = QFileDialog.getOpenFileName(self, "导入试卷", "./", "json(*.json)")
        if filepath == "":
            return

        try:
            add_shijuan = readjson(filepath)

            # 读取本地试卷信息
            data = readjson("data/shijuan_all.json")
            if len(data) == 0:
                data = {}

            # 获取每个试卷，依次检测是否存在，然后导入
            keys = list(add_shijuan.keys())
            for key in keys:
                if key in data.keys():
                    print("试卷%s存在，跳过"%key)
                    # QMessageBox.about(self, "提示", "试卷已存在！")
                else:
                    testdata = add_shijuan[key]
                    # 判断导入题库格式是否合法
                    if isinstance(testdata[0], str) and isinstance(testdata[1], list) and len(testdata[1]) == 5 and len(testdata[2]) == 5 and isinstance(testdata[2], list) and isinstance(testdata[3], dict):
                        data[key] = add_shijuan[key]
                    else:
                        print("试卷%s不合法，跳过" % key)

            # 遍历完毕，写入文件
            writejson("data/shijuan_all.json", data)
            self.frushlist4()
            QMessageBox.about(self, "提示", "导入成功！")
        except:
            QMessageBox.about(self, "提示", "导入的文件无效！")

    # 导出试卷菜单
    def outputSJ(self):
        filepath, _ = QFileDialog.getSaveFileName(self, "导出试卷", "./", "json(*.json)")
        if filepath == "":
            return

        data = readjson("data/shijuan_all.json")
        writejson(filepath, data)
        QMessageBox.about(self, "提示", "导出成功！")

    # 清空试卷菜单
    def clearSJ(self):
        if QMessageBox.Yes == QMessageBox.question(self, "提示", "确定清空所有试卷？清空后不可恢复！"):
            writejson("data/shijuan_all.json", {})
            writejson("data/defaulttest.json", {})
            self.setdefautinfo()
            self.frushlist4()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainPane()
    window.label_currentUser.setText("dll")
    window.show()
    sys.exit(app.exec_())