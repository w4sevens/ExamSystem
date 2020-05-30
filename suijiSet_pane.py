# encoding: utf-8
# @author: w4dll
# @file: suijiSet_pane.py
# @time: 2020/5/24 0:40

from PyQt5.Qt import*
from resource.suiji_set import Ui_Form
from mytool import writejson, readjson

class suijiSetPane(QWidget, Ui_Form):
    def __init__(self, parent = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

        data = readjson("data/suiji_set.json")
        if len(data) == 0:
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
        else:
            self.lineEdit_num_1.setText(str(data[0][0]))
            self.lineEdit_num_2.setText(str(data[0][1]))
            self.lineEdit_num_3.setText(str(data[0][2]))
            self.lineEdit_num_4.setText(str(data[0][3]))
            self.lineEdit_num_5.setText(str(data[0][4]))
            self.lineEdit_val_1.setText(str(data[1][0]))
            self.lineEdit_val_2.setText(str(data[1][1]))
            self.lineEdit_val_3.setText(str(data[1][2]))
            self.lineEdit_val_4.setText(str(data[1][3]))
            self.lineEdit_val_5.setText(str(data[1][4]))

    def on_clicked(self):
        list_num = [self.lineEdit_num_1, self.lineEdit_num_2, self.lineEdit_num_3, self.lineEdit_num_4, self.lineEdit_num_5]
        list_val = [self.lineEdit_val_1, self.lineEdit_val_2, self.lineEdit_val_3, self.lineEdit_val_4, self.lineEdit_val_5]
        l1, l2 = [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]
        for i in range(5):
            try:
                l1[i] = int(list_num[i].text())
            except:
                list_num[i].clear()
                list_num[i].setPlaceholderText("Error")
                list_num[i].setFocus()
                return
            try:
                l2[i] = int(list_val[i].text())
            except:
                list_val[i].clear()
                list_val[i].setPlaceholderText("Error")
                list_val[i].setFocus()
                return

        writejson("data/suiji_set.json", [l1, l2])
        QMessageBox.about(self, "提示", "随机设置成功！")
        self.close()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = suijiSetPane()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = suijiSetPane()
    win.show()
    sys.exit(app.exec_())