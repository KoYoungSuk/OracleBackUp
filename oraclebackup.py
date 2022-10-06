import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import os 
from tkinter import filedialog

UI_class = uic.loadUiType("oraclebackup_gui.ui")[0]


class MyWindow(QMainWindow, UI_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.backupbtn.clicked.connect(self.backupmethod)
        self.closebtn.clicked.connect(self.closemethod)
      
        self.pwlineedit.returnPressed.connect(self.backupmethod)
    def backupmethod(self):
        id = self.idlineedit.text()
        password = self.pwlineedit.text()
        

        filename = filedialog.asksaveasfilename(title="Save file", filetypes=(("DMP FILES(*.DMP)", "*.DMP"), ("ALL FILES(*.*)", "*.*")))

        
        command = "exp userid= " + str(id) + "/" + str(password) + " file= '" + str(filename) + "' full=y"

        print(command)
        os.system(command)
    def closemethod(self):
        sys.exit()

app = QApplication(sys.argv)

Window = MyWindow()

Window.show()

app.exec_()