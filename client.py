import socket #import socket module
import os
import subprocess
import random
import sys
import thread
from PyQt4.QtGui import *

class Client :
    socket1 = socket.socket() #create a socket object
    def createWindow(self):
    	self.a = QApplication(sys.argv)# The QWidget widget is the base class of all user interface objects in PyQt4.
        self.w = QWidget()# Set window size.
        self.textbox = QLineEdit(self.w)
        self.btn = QPushButton('Start',self.w)
        self.send = QPushButton('Send',self.w)
        self.send.hide()
        self.textfield = QLabel(self.w)
        self.textfield.resize(300,200)
        self.textfield.hide()
        self.w.resize(1000,500)# Set window title
        self.w.setWindowTitle("Chatting")
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        self.btn.setToolTip('Click to quit!')
        self.btn.clicked.connect(self.onStart)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 80)
        self.w.show()
        self.a.exec_()# Show window
        #done
    def onStart(self):
	    self.createConnection(self.textbox.text())
	    self.ShowmessageBar()
	    thread.start_new_thread(self.Recieve,("RecieveMessage",0))
	    self.a.processEvents()
    #done
    def createConnection(self,name):
        host   = socket.gethostname() 
        port   = 14000
        self.socket1.connect((host,port))
        mess=self.socket1.recv(1024)
        self.socket1.send(name)	
        print(mess)

    #done
    def Recieve(self,name,s):
    	while 1:
    		self.textfield.setText(self.socket1.recv(1024))
    		# message =(self.socket1.recv(1024))
    		# print (message+"here")
    		# newText = "hahahaha"+self.textfield.text()+message
    		# print(newText)
    		


		#done 
    def ShowmessageBar(self):
    	self.textbox.move(100,100)
        self.textbox.resize(300,200)
        self.textfield.show()
        self.btn.hide()   
        self.textfield.move(100,300)
        self.textfield.resize(300,200)
        self.textbox.setText("")
        self.send.show()
        self.send.clicked.connect(self.sendMessage)
        self.send.move(400, 400)
        self.send.setText("Send")
        self.a.processEvents()
        
   
        #done
    def sendMessage(self):
    	# if self.textbox.text()!=None :
    	self.socket1.send(self.textbox.text())
        self.textbox.setText("")
	



    	


        
    
 
if __name__ == '__main__':
    client = Client()
    client.createWindow()
    
