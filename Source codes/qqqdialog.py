# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qqqdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window2(object):
    def setup(self, window2):
        window2.setObjectName("window2")
        window2.resize(400, 278)
        window2.setSizeGripEnabled(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(window2)
        self.buttonBox.setGeometry(QtCore.QRect(50, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.label4 = QtWidgets.QLabel(window2)
        self.label4.setGeometry(QtCore.QRect(90, 10, 221, 31))
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(window2)
        self.label5.setGeometry(QtCore.QRect(50, 50, 321, 111))
        self.label5.setObjectName("label5")

        self.retranslateUi(window2)
        self.buttonBox.accepted.connect(window2.accept)
        self.buttonBox.rejected.connect(window2.reject)
        QtCore.QMetaObject.connectSlotsByName(window2)

    def retranslateUi(self, window2):
        _translate = QtCore.QCoreApplication.translate
        window2.setWindowTitle(_translate("window2", "Dialog"))
        self.label4.setText(_translate("window2", "<html><head/><body><p><span style=\" font-size:16pt;\">Operation completed!</span></p></body></html>"))
        self.label5.setText(_translate("window2", "<html><head/><body><p><span style=\" font-size:12pt;\">If the operation was completed </span></p><p><span style=\" font-size:12pt;\">successfully, your phone should reboot </span></p><p><span style=\" font-size:12pt;\">automatically when you press ok. For </span></p><p><span style=\" font-size:12pt;\">check type in your terminal </span></p><p><span style=\" font-size:12pt;\"></span></p></body>phone &quot;df -h&quot;</html>"))
