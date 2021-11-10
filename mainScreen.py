import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType(
    "/Users/jwoh/WorkSpace/PyQt5forBeginner/02.02 PushButton/ui/mainScreen.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # test
        # self.btn_Nav.clicked.connect(self.Nav_Btn_Function)
        self.Nav_Btn.clicked.connect(self.Nav_Btn_Function)
        # setting image to the button
        self.Nav_Btn.setStyleSheet(

            "background-image : url(/Users/jwoh/WorkSpace/PyQt5forBeginner/02.02 PushButton/img/navigation.png);")

        self.Following_Btn.clicked.connect(self.Following_Btn_Function)
        # setting image to the button
        self.Following_Btn.setStyleSheet(
            "background-image : url(/Users/jwoh/WorkSpace/PyQt5forBeginner/02.02 PushButton/img/followers.png);")

        self.Voice_Btn.clicked.connect(self.Voice_Btn_Function)
        # setting image to the button
        self.Voice_Btn.setStyleSheet(
            "background-image : url(/Users/jwoh/WorkSpace/PyQt5forBeginner/02.02 PushButton/img/mic.png);")

        # QPixmap 객체 생성 후 이미지 파일을 이용하여 QPixmap에 사진 데이터 Load하고, Label을 이용하여 화면에 표시
        self.label = QPixmap(
            '/Users/jwoh/WorkSpace/PyQt5forBeginner/02.02 PushButton/img/navigation.png')
        self.label_2 = QPixmap(
            '/Users/jwoh/WorkSpace/PyQt5forBeginner/02.02 PushButton/img/followers.png')
        self.label_3 = QPixmap(
            '/Users/jwoh/WorkSpace/PyQt5forBeginner/02.02 PushButton/img/mic.png')

    def Nav_Btn_Function(self):
        print("Nav_Btn Clicked (Nav_Btn Clicked!)")

    def Following_Btn_Function(self):
        print("Following_Btn Clicked (Following_Btn Clicked!)")

    def Voice_Btn_Function(self):
        print("Voice_Btn Clicked (Voice_Btn Clicked!)")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
