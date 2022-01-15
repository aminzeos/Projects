# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os
from PyQt5 import QtCore, QtGui, QtWidgets
from googletrans import Translator
from gtts import gTTS
import playsound

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(756, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_out = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_out.setGeometry(QtCore.QRect(390, 70, 351, 241))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit_out.setFont(font)
        self.textEdit_out.setObjectName('textEdit_out')
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 320, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_paste = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_paste.setGeometry(QtCore.QRect(10, 315, 75, 23))
        self.pushButton_paste.setObjectName('pushButton_paste')
        self.pushButton_copy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_copy.setGeometry(QtCore.QRect(670, 315, 75, 23))
        self.pushButton_copy.setObjectName('pushButton_copy')
        self.pushButton_clear_in = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear_in.setObjectName('pushButton_clear_in')
        self.pushButton_clear_in.setGeometry(QtCore.QRect(80, 315, 75, 23))
        self.pushButton_aloud_in = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_aloud_in.setGeometry(QtCore.QRect(150, 315, 75, 23))
        self.pushButton_aloud_in.setObjectName('pushButton_aloud_in')
        self.pushButton_clear_out = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear_out.setObjectName('pushButton_clear_out')
        self.pushButton_clear_out.setGeometry(QtCore.QRect(600, 315, 75, 23))
        self.pushButton_aloud_out = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_aloud_out.setGeometry(QtCore.QRect(530, 315, 75, 23))
        self.pushButton_aloud_out.setObjectName('pushButton_aloud_out')
        self.pushButton_change = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_change.setGeometry(QtCore.QRect(340, 10, 75, 23))
        self.pushButton_change.setObjectName('pushButton_change')
        self.comboBox_out = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_out.setGeometry(QtCore.QRect(390, 40, 351, 22))
        self.comboBox_out.setObjectName("comboBox_out")
        self.comboBox_out.addItem("")
        self.comboBox_out.addItem("")
        self.comboBox_out.addItem("")
        self.comboBox_out.addItem("")
        self.comboBox_out.addItem("")
        self.comboBox_out.addItem("")
        self.comboBox_out.addItem("")
        self.comboBox_out.addItem("")
        self.comboBox_out.addItem("")
        self.comboBox_out.addItem("")
        self.comboBox_out.addItem("")
        self.comboBox_out.addItem("")
        self.comboBox_out.addItem("")
        self.comboBox_out.addItem("")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_out.setFont(font)
        self.textEdit_in = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_in.setGeometry(QtCore.QRect(10, 69, 351, 241))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_in.setFont(font)
        self.textEdit_in.setObjectName('textEdit_in')
        self.comboBox_in = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_in.setGeometry(QtCore.QRect(10, 40, 351, 22))
        self.comboBox_in.setObjectName("comboBox_in")
        self.comboBox_in.addItem("")
        self.comboBox_in.addItem("")
        self.comboBox_in.addItem("")
        self.comboBox_in.addItem("")
        self.comboBox_in.addItem("")
        self.comboBox_in.addItem("")
        self.comboBox_in.addItem("")
        self.comboBox_in.addItem("")
        self.comboBox_in.addItem("")
        self.comboBox_in.addItem("")
        self.comboBox_in.addItem("")
        self.comboBox_in.addItem("")
        self.comboBox_in.addItem("")
        self.comboBox_in.addItem("")
        self.comboBox_in.addItem("")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_in.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 756, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.translate)
        self.pushButton_copy.clicked.connect(self.copy)
        self.pushButton_paste.clicked.connect(self.paste)
        self.pushButton_clear_in.clicked.connect(self.clear_in)
        self.pushButton_clear_out.clicked.connect(self.clear_out)
        self.pushButton_aloud_in.clicked.connect(self.aloud_in)
        self.pushButton_aloud_out.clicked.connect(self.aloud_out)
        self.pushButton_change.clicked.connect(self.change)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Translator"))
        try:
            MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        except:
            pass
        self.pushButton.setText(_translate("MainWindow", "Translate"))
        self.pushButton_paste.setText(_translate('MainWindow', 'Paste'))
        self.pushButton_copy.setText(_translate('MainWindow', 'Copy'))
        self.pushButton_clear_in.setText(_translate('MainWindow', 'Clear'))
        self.pushButton_clear_out.setText(_translate('MainWindow', 'Clear'))
        self.pushButton_aloud_in.setText(_translate('MainWindow', 'Aloud'))
        self.pushButton_aloud_out.setText(_translate('MainWindow', 'Aloud'))
        self.pushButton_change.setText(_translate('MainWindow', 'Change'))
        self.comboBox_out.setItemText(0, _translate("MainWindow", "Africans"))
        self.comboBox_out.setItemText(1, _translate("MainWindow", "Arabic"))
        self.comboBox_out.setItemText(2, _translate("MainWindow", "Dutch"))
        self.comboBox_out.setItemText(3, _translate("MainWindow", "English"))
        self.comboBox_out.setItemText(4, _translate("MainWindow", "French"))
        self.comboBox_out.setItemText(5, _translate("MainWindow", "German"))
        self.comboBox_out.setItemText(6, _translate("MainWindow", "Hindi"))
        self.comboBox_out.setItemText(7, _translate("MainWindow", "Irish"))
        self.comboBox_out.setItemText(8, _translate("MainWindow", "Italian"))
        self.comboBox_out.setItemText(9, _translate("MainWindow", "Japanese"))
        self.comboBox_out.setItemText(10, _translate("MainWindow", "Persian"))
        self.comboBox_out.setItemText(11, _translate("MainWindow", "Russian"))
        self.comboBox_out.setItemText(12, _translate("MainWindow", "Spanish"))
        self.comboBox_out.setItemText(13, _translate("MainWindow", "Turkish"))
        self.comboBox_in.setItemText(0, _translate("MainWindow", "Detect Language"))
        self.comboBox_in.setItemText(1, _translate("MainWindow", "Africans"))
        self.comboBox_in.setItemText(2, _translate("MainWindow", "Arabic"))
        self.comboBox_in.setItemText(3, _translate("MainWindow", "Dutch"))
        self.comboBox_in.setItemText(4, _translate("MainWindow", "English"))
        self.comboBox_in.setItemText(5, _translate("MainWindow", "French"))
        self.comboBox_in.setItemText(6, _translate("MainWindow", "German"))
        self.comboBox_in.setItemText(7, _translate("MainWindow", "Hindi"))
        self.comboBox_in.setItemText(8, _translate("MainWindow", "Irish"))
        self.comboBox_in.setItemText(9, _translate("MainWindow", "Italian"))
        self.comboBox_in.setItemText(10, _translate("MainWindow", "Japanese"))
        self.comboBox_in.setItemText(11, _translate("MainWindow", "Persian"))
        self.comboBox_in.setItemText(12, _translate("MainWindow", "Russian"))
        self.comboBox_in.setItemText(13, _translate("MainWindow", "Spanish"))
        self.comboBox_in.setItemText(14, _translate("MainWindow", "Turkish"))
    
    def aloud_in(self):
        _in, _out = self.check_for_selected()
        text = self.textEdit_in.toPlainText()
        if self.in_lang == 'en':
            tts = gTTS(text=text)
            tts.save('tts.mp3')
            playsound.playsound('tts.mp3')
            os.remove('tts.mp3')
        elif self.in_lang == '':
            tts = gTTS(text=text)
            tts.save('tts.mp3')
            playsound.playsound('tts.mp3')
            os.remove('tts.mp3')
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Import Error')
            msg.setText('Only English language supported')
            x = msg.exec_()

    def aloud_out(self):
        _in, _out = self.check_for_selected()
        text = self.textEdit_out.toPlainText()
        if self.out_lang == 'en':
            tts = gTTS(text=text)
            tts.save('tts.mp3')
            playsound.playsound('tts.mp3')
            os.remove('tts.mp3')
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Import Error')
            msg.setText('Only English language supported')
            x = msg.exec_()

    def clear_in(self):
        self.textEdit_in.setText('')
    
    def clear_out(self):
        self.textEdit_out.setText('')

    def translate(self):
        _in, _out = self.check_for_selected()
        trans = Translator()
        text = self.textEdit_in.toPlainText()
        self.in_lang = _in
        if _in != '' :
            out = trans.translate(text, src=_in, dest=_out)
            self.out_lang = _out
        else:
            out = trans.translate(text, dest=_out)
            self.out_lang = _out
        self.textEdit_out.setText(out.text)
    
    def change(self):
        _in = self.comboBox_in.currentIndex()
        _out = self.comboBox_out.currentIndex()
        if _in != 0:
            out = _in - 1
            inn = _out + 1
            self.comboBox_in.setCurrentIndex(inn)
            self.comboBox_out.setCurrentIndex(out)
            text_in = self.textEdit_in.toPlainText()
            text_out = self.textEdit_out.toPlainText()
            self.textEdit_in.setText(text_out)
            self.textEdit_out.setText(text_in)
            __in , __out = self.check_for_selected()
            self.in_lang = __in
            self.out_lang = __out


    def copy(self):
        self.textEdit_out.selectAll()
        self.textEdit_out.copy()

    def paste(self):
        self.textEdit_in.paste()

    def check_for_selected(self):
        combo_in = self.comboBox_in.currentIndex()
        combo_out = self.comboBox_out.currentIndex()
        combo_in_final = ''
        combo_out_final = 'en'
        if combo_in == 1:
            combo_in_final = 'af'
        elif combo_in == 2:
            combo_in_final = 'ar'
        elif combo_in == 3:
            combo_in_final = 'nl'
        elif combo_in == 4:
            combo_in_final = 'en'
        elif combo_in == 5:
            combo_in_final = 'fr'
        elif combo_in == 6:
            combo_in_final = 'de'
        elif combo_in == 7:
            combo_in_final = 'hi'
        elif combo_in == 8:
            combo_in_final = 'ga'
        elif combo_in == 9:
            combo_in_final = 'it'
        elif combo_in == 10:
            combo_in_final = 'ja'
        elif combo_in == 11:
            combo_in_final = 'fa'
        elif combo_in == 12:
            combo_in_final = 'ru'
        elif combo_in == 13:
            combo_in_final = 'es'
        elif combo_in == 14:
            combo_in_final = 'tr'
        

        if combo_out == 0:
            combo_out_final = 'af'
        elif combo_out == 1:
            combo_out_final = 'ar'
        elif combo_out == 2:
            combo_out_final = 'nl'
        elif combo_out == 3:
            combo_out_final = 'en'
        elif combo_out == 4:
            combo_out_final = 'fr'
        elif combo_out == 5:
            combo_out_final = 'de'
        elif combo_out == 6:
            combo_out_final = 'hi'
        elif combo_out == 7:
            combo_out_final = 'ga'
        elif combo_out == 8:
            combo_out_final = 'it'
        elif combo_out == 9:
            combo_out_final = 'ja'
        elif combo_out == 10:
            combo_out_final = 'fa'
        elif combo_out == 11:
            combo_out_final = 'ru'
        elif combo_out == 12:
            combo_out_final = 'es'
        elif combo_out == 13:
            combo_out_final = 'tr'
        
        self._in, self._out = combo_in_final, combo_out_final
        return combo_in_final, combo_out_final
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())