from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys 
import os
import subprocess
import time
from PyQt5.uic import loadUi
from gui import Ui_MainWindow
from qqqdialog import *


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
    
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.label = QLabel(self)
        self.ui.setupUi(self)
        self.ui.button1.clicked.connect(self.button1clicked)
        self.ui.progressBar.setValue(0)
            
    def button1clicked(self):
        time.sleep(1.10)
        self.ui.progressBar.setValue(10)
        subprocess.run(["adb", "root"])
        self.ui.progressBar.setValue(20)
        subprocess.run(["adb", "shell", "sudo", "dd", "if=/dev/zero", "bs=1MiB", "of=/userdata/system.img", "conv=notrunc", "oflag=append", "count=6000"])
        self.ui.progressBar.setValue(30)
        subprocess.run(["adb", "shell", "sudo", "losetup", "-c", "/dev/loop0"])
        self.ui.progressBar.setValue(40)
        subprocess.run(["adb", "reboot", "recovery"])
        self.ui.progressBar.setValue(50)
        time.sleep(10.0)
        self.ui.progressBar.setValue(60)
        subprocess.run(["adb", "root"])
        self.ui.progressBar.setValue(70)
        subprocess.run(["adb", "shell", "losetup", "/dev/block/loop0", "/data/system.img"])
        self.ui.progressBar.setValue(80)
        subprocess.run(["adb", "shell", "e2fsck", "-f", "/dev/block/loop0"])
        self.ui.progressBar.setValue(90)
        subprocess.run(["adb", "shell", "resize2fs", "-f", "/dev/block/loop0"])
        self.ui.progressBar.setValue(100)
        
        self.window=QtWidgets.QDialog()
        self.ui=Ui_window2()
        self.ui.setup(self.window)
        self.window.show()
        self.ui.buttonBox.accepted.connect(self.buttonboxacc)
        self.ui.buttonBox.rejected.connect(self.buttonboxrej)
    
    def buttonboxacc(self):
        subprocess.run(["adb", "shell", "reboot"])
        sys.exit()
        
    def buttonboxrej(self):
        sys.exit()
        
        
        
        
        
    
    
    
    
        
        
        


app = QtWidgets.QApplication([])

application = mywindow()

application.show()

sys.exit(app.exec())