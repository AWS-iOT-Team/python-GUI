import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType(
    "/Users/jwoh/WorkSpace/PyQt5forBeginner/02.02 PushButton/Following.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # test

        self.btn_1.clicked.connect(self.button1Function)
        # setting image to the button
        self.btn_1.setStyleSheet(
            "background-image : url(/Users/jwoh/WorkSpace/PyQt5forBeginner/02.02 PushButton/img/man4.png);")
        self.btn_1_flag = False

    def button1Function(self):
        print("btn_1 Clicked (Following_Btn Clicked!)")

        # btn_1_flag
    def flag_btn_1(self, state):
        # 콤보 박스 시에 checked 아님?
        if state == Qt.Checked:
            self.btn_1_flag = True
        else:
            self.btn_1_flag = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
