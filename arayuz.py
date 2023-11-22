import sys 
from PyQt5 import QtWidgets,QtGui,QtTest
import os
def encode():
    os.popen('/usr/bin/bash otp_encode.sh')
def decode():
    os.popen('/usr/bin/bash otp_decode.sh')
def generate():
    os.popen('/usr/bin/bash generate_randoms.sh')
    
app=QtWidgets.QApplication(sys.argv)
win=QtWidgets.QWidget()
win.setWindowTitle("arayüz")

button1=QtWidgets.QPushButton(win)
button2=QtWidgets.QPushButton(win)
button3=QtWidgets.QPushButton(win)

button1.setText("mesaj oluştur")
button2.setText("mesaj çöz")
button3.setText("anahtar yarat")
        
button1.clicked.connect(encode)
button2.clicked.connect(decode)
button3.clicked.connect(generate)
	
button1.setGeometry(80,60, 320, 100) 
button2.setGeometry(80,220, 320, 100) 
button3.setGeometry(80,380, 320, 100) 

win.setGeometry(0, 60, 480, 540)
win.show()

sys.exit(app.exec_()) 
