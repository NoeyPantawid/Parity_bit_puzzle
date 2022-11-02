from ui import Ui_MainWindow
from random import randint
from PyQt5 import QtWidgets
import sys

class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        self.ui.random_btn.pressed.connect(self.random_func)
        self.ui.answer_btn.pressed.connect(self.answer_func)

        self.ui.random_btn_2.pressed.connect(self.random_func_2)
        self.ui.answer_btn_2.pressed.connect(self.answer_func_2)

        self.ans = ["Odd", 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.reveal = []
        self.unknown = 0
        self.unknown_2 = 0

    def random_func(self):
        p = randint(0, 1) #0 = odd, 1 = even
        b1 = randint(0, 1)
        b2 = randint(0, 1)
        b3 = randint(0, 1)
        b4 = randint(0, 1)
        b5 = randint(0, 1)
        b6 = randint(0, 1)
        b7 = randint(0, 1)
        b8 = randint(0, 1)
        s = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8
        self.unknown = randint(0, 9)

        if p == 0:
            parity = "Odd"
        else:
            parity = "Even"
        
        b9 = self.checkParity(p, s)

        self.ans = [parity, b1, b2, b3, b4, b5, b6, b7, b8, b9]
        self.reveal = self.ans.copy()
        self.reveal[self.unknown] = "?"

        #reset color
        for i in range(0, 10):
            eval(f'self.ui.bit_{i}.setStyleSheet("color: white")')

        #red color
        eval(f'self.ui.bit_{self.unknown}.setStyleSheet("color: red")')

        for i in range(0, 10):
            eval(f'self.ui.bit_{i}.setText(f"{self.reveal[i]}")')
    
    def answer_func(self):
        eval(f'self.ui.bit_{self.unknown}.setStyleSheet("color: green")')
        for i in range(0, 10):
            eval(f'self.ui.bit_{i}.setText(f"{self.ans[i]}")')

    def random_func_2(self):
        p = randint(0, 1)
        b1 = randint(0, 1)
        b2 = randint(0, 1)
        b3 = randint(0, 1)
        b4 = randint(0, 1)
        b5 = randint(0, 1)

        s1 = b1 + b3 + b5
        s2 = b1 + b2 + b4
        s3 = b2 + b3
        s4 = b4 + b5

        self.unknown = randint(0, 9)
        self.unknown_2 = randint(0, 9)

        if p == 0:
            parity = "Odd"
        else:
            parity = "Even"
        
        b6 = self.checkParity(p, s1)
        b7 = self.checkParity(p, s2)
        b8 = self.checkParity(p, s3)
        b9 = self.checkParity(p, s4)

        self.ans = [parity, b1, b2, b3, b4, b5, b6, b7, b8, b9]
        self.reveal = self.ans.copy()
        self.reveal[self.unknown] = "?"
        self.reveal[self.unknown_2] = "?"

        #reset color
        for i in range(0, 10):
            eval(f'self.ui.bit_1{i}.setStyleSheet("color: white")')
        
        #red color
        eval(f'self.ui.bit_1{self.unknown}.setStyleSheet("color: red")')
        eval(f'self.ui.bit_1{self.unknown_2}.setStyleSheet("color: red")')

        for i in range(0, 10):
            eval(f'self.ui.bit_1{i}.setText(f"{self.reveal[i]}")')
    
    def answer_func_2(self):
        eval(f'self.ui.bit_1{self.unknown}.setStyleSheet("color: green")')
        eval(f'self.ui.bit_1{self.unknown_2}.setStyleSheet("color: green")')
        for i in range(0, 10):
            eval(f'self.ui.bit_1{i}.setText(f"{self.ans[i]}")')
        

    def checkParity(self, p, s):
        if p == 0:
            if s % 2 == 0:
                return 1
            else:
                return 0
        else:
            if s % 2 == 1:
                return 1
            else:
                return 0

app = QtWidgets.QApplication(sys.argv)
AppCode = App()
AppCode.show()
app.exec_()