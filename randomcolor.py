from PyQt5 import QtWidgets, uic
import sys,random
from PyQt5.QtWidgets import *


class mains(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("randomcolor.ui", self)

        self.window()

    def window(self):

        self.pushButton.clicked.connect(self.colorlabel)
        self.pushButton_2.clicked.connect(self.colorbackg)
        self.pushButton_3.clicked.connect(self.colorbt)
        self.pushButton_4.clicked.connect(self.randoms)
        self.setWindowTitle("Change Colors With ComboBox")


        self.rand = "no"
        self.show()


    def lightthema(self):
        self.pushButton.setStyleSheet("background-color : white")
        self.pushButton_2.setStyleSheet("background-color : white")
        self.pushButton_3.setStyleSheet("background-color : white")
        self.label.setStyleSheet("color : gray")
        self.setStyleSheet("background-color : white")

    def darkthema(self):

        self.pushButton.setStyleSheet("background-color : dimgray")
        self.pushButton_2.setStyleSheet("background-color : dimgray")
        self.pushButton_3.setStyleSheet("background-color : dimgray")
        self.label.setStyleSheet("color : black")
        self.setStyleSheet("background-color : dimgray")
    def colorlabel(self,item3):
        self.texts = self.comboBox.currentText()

        if self.texts == "darkthema":
            print("dark  thema secildi")
            self.darkthema()

        elif self.texts == "lightthema":
            self.lightthema()
        else:
            if self.rand == "yes":
                print("label : yes")
                self.label.setStyleSheet("color : {}".format(item3))
            elif self.rand == "no":
                self.label.setStyleSheet("color : {}".format(self.texts))
                print("label no ")
            self.rand = "no"
    def colorbackg(self,item2):


        if self.rand == "yes":
            print("backgorund : yes")
            self.setStyleSheet("background-color : {}".format(item2))
        elif self.rand == "no":
            self.texts = self.comboBox.currentText()
            print("background no")
            self.setStyleSheet("background-color : {}".format(self.texts))
        self.rand = "no"
    def colorbt(self,item):


        if self.rand == "yes":
            print("buton : yes bloku")
            self.pushButton.setStyleSheet("background-color : {}".format(item))
            self.pushButton_2.setStyleSheet("background-color : {}".format(item))
            self.pushButton_3.setStyleSheet("background-color : {}".format(item))

        elif self.rand == "no":
            self.texts = self.comboBox.currentText()
            self.pushButton.setStyleSheet("background-color : {}".format(self.texts))
            self.pushButton_2.setStyleSheet("background-color : {}".format(self.texts))
            self.pushButton_3.setStyleSheet("background-color : {}".format(self.texts))
        self.rand = "no"

    def randoms(self):
        color = ["red","blue","white","pink","yellow","purple","brown","teal"]
        a = random.randint(0,7)
        b = random.randint(0, 7)
        c = random.randint(0, 7)
        self.item = color[a]
        self.item2 = color[b]
        self.item3 = color[c]

        #self.setStyleSheet("background-color : {}".format(self.item))
        self.rand = "yes"
        self.colorbt(self.item)
        self.rand = "yes"
        self.colorbackg(self.item2)
        self.rand = "yes"
        self.colorlabel(self.item3)

        pass

app=QtWidgets.QApplication(sys.argv)

menu = mains()
sys.exit(app.exec_())

