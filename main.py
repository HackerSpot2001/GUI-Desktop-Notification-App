#!/usr/bin/python3
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QComboBox, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QPushButton, QVBoxLayout, QWidget
import sys
import notify2
import time

class Desktop_Notifier(QWidget):
    def __init__(self):
        super().__init__()
        
        self.urgency_level = ['Low','Normal','Critical']
        top = 80
        left = 350
        width = 600
        height = 500
        self.setWindowTitle("Desktop Notifier App | Python3 PyQt5")
        self.setMaximumSize(width,height)
        self.setWindowIcon(QIcon("notification.png"))
        self.setMinimumSize(width,height)
        self.setGeometry(left,top,width,height)
        self.vbox = QVBoxLayout()
        self.setWidgets()
        self.setLayout(self.vbox)

    def setWidgets(self):
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        # self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()

        # Set Lables
        self.note_name  = QLabel("Notification Name:- ")
        self.note_name.setAlignment(Qt.AlignCenter)
        self.note_name.setStyleSheet("color:white;font-size:17px;font-weight:bold;width:80px;height:5px;border:2px solid white;border-radius:10px;margin:0px 10px;")
        
        self.note_title = QLabel("Notification Title:- ")
        self.note_title.setAlignment(Qt.AlignCenter)
        self.note_title.setStyleSheet("color:white;font-size:17px;font-weight:bold;width:80px;height:5px;border:2px solid white;border-radius:10px;margin:0px 10px;")
        
        self.note_message = QLabel("Notification Message:- ")
        self.note_message.setAlignment(Qt.AlignCenter)
        self.note_message.setStyleSheet("color:white;font-size:17px;font-weight:bold;width:80px;height:5px;border:2px solid white;border-radius:10px;margin:0px 10px;")
        
        # self.note_time_interval = QLabel("Notification Duration:- ")
        # self.note_time_interval.setAlignment(Qt.AlignCenter)
        # self.note_time_interval.setStyleSheet("color:white;font-size:17px;font-weight:bold;width:80px;height:5px;border:2px solid white;border-radius:10px;margin:0px 10px;")
        
        self.note_urgency = QLabel("Notification Urgency:- ")
        self.note_urgency.setAlignment(Qt.AlignCenter)
        self.note_urgency.setStyleSheet("color:white;font-size:17px;font-weight:bold;width:80px;height:5px;border:2px solid white;border-radius:10px;margin:0px 10px;")

        #set LineEdits and comboBox
        self.note_name_inp = QLineEdit()
        self.note_name_inp.setText('')
        self.note_name_inp.setPlaceholderText("Only String Valid")
        self.note_name_inp.setStyleSheet("width:100px;height:30px;border:2px solid white;border-radius:10px;padding:0px 10px;margin:0px 30px;font-size:12px;font-weight:bold;")
        
        self.note_title_inp = QLineEdit()
        self.note_title_inp.setPlaceholderText("Only String Valid")
        self.note_title_inp.setText('')
        self.note_title_inp.setStyleSheet("width:100px;height:30px;border:2px solid white;border-radius:10px;padding:0px 10px;margin:0px 40px;font-size:12px;font-weight:bold;")
        
        self.note_message_inp = QLineEdit()
        self.note_message_inp.setText('')
        self.note_message_inp.setPlaceholderText("Only String Valid")
        self.note_message_inp.setStyleSheet("width:100px;height:30px;border:2px solid white;border-radius:10px;padding:0px 10px;margin:0px 20px;font-size:12px;font-weight:bold;")
        
        # self.note_time_inp = QLineEdit()
        # self.note_time_inp.setText('')
        # self.note_time_inp.setPlaceholderText("Only Intigers Valid")
        # self.note_time_inp.setStyleSheet("width:100px;height:30px;border:2px solid white;border-radius:10px;padding:0px 10px;margin:0px 20px;font-size:12px;font-weight:bold;")
        
        self.note_urgency_inp = QComboBox()
        self.note_urgency_inp.setStyleSheet("height:30px;margin:0px 20px;font-size:18px;font-weight:bold;")
        for i in self.urgency_level:
            self.note_urgency_inp.addItem(i)

        # Add Widgets in Vbox layout
        self.hbox1.addWidget(self.note_name)
        self.hbox1.addWidget(self.note_name_inp)
        self.hbox2.addWidget(self.note_title)
        self.hbox2.addWidget(self.note_title_inp)
        self.hbox3.addWidget(self.note_message)
        self.hbox3.addWidget(self.note_message_inp)
        # self.hbox4.addWidget(self.note_time_interval)
        # self.hbox4.addWidget(self.note_time_inp)
        self.hbox5.addWidget(self.note_urgency)
        self.hbox5.addWidget(self.note_urgency_inp)
        self.set_note = QPushButton()
        self.set_note.setStyleSheet("background-color:purple;color:white;font-size:18px;font-weight:bold;")
        self.set_note.setText("Set Notification")
        self.set_note.clicked.connect(self.setNotification)

        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        # self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addWidget(self.set_note)

    def setNotification(self):
        inp1 = self.note_name_inp.text()
        inp2 = self.note_title_inp.text()
        inp3 = self.note_message_inp.text()
        # inp4 = self.note_time_inp.text()
        inp5 = self.note_urgency_inp.currentText()
        if (inp1 == '' ) or (inp2 == '' ) or (inp3 == '' ) :
            QMessageBox.question(self,"Data Warning...","Please Fill all Input Fields",QMessageBox.Ok)
        
        else:
            try:
                notify2.init(inp1)
                notification_object = notify2.Notification(None,icon="notification.png")
                if inp5 == "Low":
                    notification_object.set_urgency(notify2.URGENCY_LOW)
                    notification_object.update(inp2,inp3)
                    notification_object.show()
                    time.sleep(5)  
                    notification_object.close()

                elif inp5 == "Normal":
                    notification_object.set_urgency(notify2.URGENCY_NORMAL)
                    notification_object.update(inp2,inp3)
                    notification_object.show()
                    time.sleep(5)  
                    notification_object.close()

                elif inp5 == "Critical":
                    notification_object.set_urgency(notify2.URGENCY_CRITICAL)
                    notification_object.update(inp2,inp3)
                    notification_object.show()
                    time.sleep(5)  
                    notification_object.close()

                self.note_name_inp.setText('')
                self.note_title_inp.setText('')
                self.note_message_inp.setText('')
                # self.note_time_inp.setText('')

            except Exception as e:
                QMessageBox.question(self,"Data Error",str(e),QMessageBox.Ok)
        

            

       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Desktop_Notifier()
    window.show()
    sys.exit(app.exec_())
