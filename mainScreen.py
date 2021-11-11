import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QFont, QFontDatabase
from PyQt5.QtCore import Qt

# connect the ui file

# main screen design
Main_form_class = uic.loadUiType(
    "/Users/jwoh/WorkSpace/PyQt5forBeginner/02.02 PushButton/ui/mainScreen.ui")[0]

# main screen design
Nav_form_class = uic.loadUiType(
    "/Users/jwoh/WorkSpace/PyQt5forBeginner/02.02 PushButton/ui/Nav.ui")[0]

# following screen design
F_form_class = uic.loadUiType(
    "/Users/jwoh/WorkSpace/PyQt5forBeginner/02.02 PushButton/ui/Following.ui")[0]

# following screen design
Voice_form_class = uic.loadUiType(
    "/Users/jwoh/WorkSpace/PyQt5forBeginner/02.02 PushButton/ui/Voice.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언


class WindowClass(QMainWindow, Main_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Nav_Btn.clicked.connect(self.Nav_Btn_Function)
        self.F_Btn.clicked.connect(self.F_Btn_Function)
        # setting image to the button
        self.Voice_Btn.clicked.connect(self.Voice_Btn_Function)
        # setting image to the button

    def Nav_Btn_Function(self):
        print("Nav_Btn Clicked (Nav_Btn Clicked!)")
        self.Nav_window()

    def F_Btn_Function(self):
        print("Following_Btn Clicked (Following_Btn Clicked!)")
        self.F_window()

    def Voice_Btn_Function(self):
        print("Voice_Btn Clicked (Voice_Btn Clicked!)")
        self.Voice_window()

    def Nav_window(self):
        self.n = Nav_WindowClass()
        self.n.show()
        self.hide()

    def F_window(self):
        self.f = F_WindowClass()
        self.f.show()
        self.hide()

    def Voice_window(self):
        self.v = Voice_WindowClass()
        self.v.show()
        self.hide()


class Nav_WindowClass(QMainWindow, Nav_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Nav_Window_Cancle_Btn.clicked.connect(
            self.Nav_Window_Cancle_Btn_Function)

    def Nav_Window_Cancle_Btn_Function(self):
        print("Nav_Window_Cancle_Btn Clicked (Nav_Window_Cancle_Btn Clicked!)")
        self.M_window()

    def M_window(self):
        self.m = WindowClass()
        self.m.show()
        self.hide()


class F_WindowClass(QMainWindow, F_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Following_Cancle_Btn.clicked.connect(
            self.Following_Cancle_Btn_Function)
        self.Following_Action_Btn.clicked.connect(
            self.Following_Action_Btn_Function)
        self.Following_Action_Btn.setStyleSheet(
            "background-image : url(/Users/jwoh/WorkSpace/PyQt5forBeginner/02.02 PushButton/img/man4.png);"
            "background-position : center;")

    def Following_Cancle_Btn_Function(self):
        self.m = WindowClass()
        self.m.show()
        self.hide()

    def Following_Action_Btn_Function(self):
        pass


class Voice_WindowClass(QMainWindow, Voice_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Voice_Cancle_Btn.clicked.connect(self.Voice_Cancle_Btn_Function)
        self.Voice_Action_Btn.clicked.connect(self.Voice_Action_Btn_Function)
        self.Voice_Action_Btn.setStyleSheet(
            "image : url(/Users/jwoh/WorkSpace/PyQt5forBeginner/02.02 PushButton/img/mic.png);"
            "image-position: center;")

    def Voice_Cancle_Btn_Function(self):
        self.m = WindowClass()
        self.m.show()
        self.hide()

    def Voice_Action_Btn_Function(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
