import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType(
    "/Users/jwoh/WorkSpace/PyQt5forBeginner/02.02 PushButton/ui/Following.ui")[0]

form_class2 = uic.loadUiType(
    "/Users/jwoh/WorkSpace/PyQt5forBeginner/02.02 PushButton/ui/mainScreen.ui")[0]
# 화면을 띄우는데 사용되는 Class 선언


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # test

        self.btn_1.clicked.connect(self.button1Function)
        # setting image to the button
        self.btn_1.setStyleSheet(
            "background-image : url(/Users/jwoh/WorkSpace/PyQt5forBeginner/02.02 PushButton/man4.png);")

    def button1Function(self):
        print("btn_1 Clicked (Following_Btn Clicked!)")
        self.window2()

    def window2(self):
        self.w = WindowClass2()
        self.w.show()
        self.hide()


class WindowClass2(QMainWindow, form_class2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
