import csv,sys
import pymysql
import re
from typing import *
import hashlib, os
from PyQt5.QtCore import Qt, QAbstractTableModel, QVariant
from PyQt5.QtWidgets import (QWidget, QPushButton,QMainWindow,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit, QComboBox,
    QTableWidget, QCheckBox, QMessageBox, QRadioButton, QListWidget,
    QPlainTextEdit, QListWidgetItem)
from PyQt5.QtGui import (QFont)
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QFrame,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QListView,
    QAbstractItemView,
    QMessageBox,
    QLineEdit,
    QTableView, QDialog, qApp, QGroupBox, QFormLayout, QDialogButtonBox)
from PyQt5.QtGui import (
    QStandardItemModel,
    QStandardItem,
    QPixmap)
from datetime import datetime,date

from PyQt5.uic.properties import QtWidgets

loggedInUser="Unknown"
connection = ""
loggedInEmailaddress = "Unknown"

class MainWindow(QMainWindow):
    def __init__(self, parent=None):

        # global connection
        # try:
        #     connection = pymysql.connect(host="localhost",
        #                                  user="root",
        #                                  password="",
        #                                  db="beltline",
        #                                  charset='utf8mb4',
        #                                  cursorclass=pymysql.cursors.DictCursor)
        # except Exception as e:
        #     print(f"Couldn't log in to MySQL server")
        #     print(e)
        #     sys.exit()

        self.UserLogin= UserLogin()
        #self.RegisterNavigation = screen3.Screen3Window()
        self.startUserLogin()

    def startUserLogin(self):
        self.UserLogin.__init__()
        self.UserLogin.show()
#        self.UserLogin.login_btn.clicked.connect(self.startRegisterNavigation)

#    def startRegisterNavigation(self):
#        print('PyQt5 button click')

        #self.RegisterNavigation.__init__()
        #self.RegisterNavigation.show()

class UserLogin(QWidget): #Screen 1
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label1 = QLabel("Username:", self)
        self.label2 = QLabel("Password:", self)

        self.textbox1 = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.textbox2.setEchoMode(QLineEdit.Password)

        self.login_btn = QPushButton("Login")
        self.register_btn = QPushButton("Register")

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()

        hbox1.addWidget(self.label1)
        hbox1.addWidget(self.textbox1)
        hbox2.addWidget(self.label2)
        hbox2.addWidget(self.textbox2)
        hbox3.addWidget(self.login_btn)
        hbox3.addWidget(self.register_btn)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Atlanta Movie Login')

        self.register_btn.clicked.connect(self.startRegisterNavigation)
        self.login_btn.clicked.connect(self.startLogin)

    def startRegisterNavigation(self):
        self.w = RegisterNavigation()
        self.w.show()

        self.hide()

    def startLogin(self):
        # self.main = UserFunctionality()
        # self.main.show()
        # self.hide()
        self.main = VisitorFunctionality()
        self.main.show()
        self.hide()
    #     #
    #     # global loggedInUser
    #     # global connection
    #     #
    #     # hashPassword = hashedPassword(self.textbox2.text())
    #     # #print(hashPassword)
    #     #
    #     # userNametoSaveTyping = self.textbox1.text() # + 'jsmith@gatech.edu'
    #     # userRole = roleCheck(userNametoSaveTyping)

    #     # with connection.cursor() as cursor:
    #     #     # Read a single record
    #     #     sql = "  select u.username, count(*) as 'rows' from User u, UserEmail e where u.username = e.username and \
    #     #     e.Email = '" + userNametoSaveTyping + "'  and u.Password = '" + hashPassword + "' and \
    #     #     status = 'Approved' group by u.username ;"
    #     #     cursor.execute(sql)
    #     #     usrDetail = cursor.fetchall()
    #     #
    #     # kount=0
    #     # for row in usrDetail :
    #     #     kount = list(row.values())[1]
    #     #     userName = list(row.values())[0]
    #     #
    #     #     loggedInUser = userName

    #     if True:
    #         #print("Successfull Login")
    #         #print(userName)
    #         if userRole == "Administrator-Only":
    #             self.main = AdminOnlyFunctionality()
    #         elif userRole == "Adminstrator-Visitor":
    #             self.main = AdminstratorVisitorFunctionality()
    #         elif userRole == "Manager-Only":
    #             self.main = ManagerOnlyFunctionality()
    #         elif userRole == "Manager-Visitor":
    #             self.main = ManagerVisitorFunctionality()
    #         elif userRole == "Staff-Only":
    #             self.main = StaffFunctionality()
    #         elif userRole == "Staff-Visitor":
    #             self.main = StaffVisitorFunctionality()
    #         elif userRole == "Visitor":
    #             self.main = VisitorFunctionality()
    #         elif userRole == "User":
    #             self.main = UserFunctionality()
    #         else:
    #             buttonReply = QMessageBox.information(self, 'Strange', "Strange: This should never be displayed", QMessageBox.Ok)

    #         self.main.show()
    #         self.hide()
    #     else:
    #         buttonReply = QMessageBox.information(self, 'Login', "Invalid Login Credentials", QMessageBox.Ok)

class Window2(QWidget):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Invalid Login")

class RegisterNavigation(QWidget): #Screen 2
    def __init__(self):
        super (RegisterNavigation, self).__init__()
        self.setWindowTitle("Register Navigation")

        left, top, width, height = 550, 50, 250, 400
        self.setGeometry(left, top, width, height)

        self.userOnly_btn = QPushButton("User Only")
        self.visitorOnly_btn = QPushButton("Customer Only")
        self.employeeOnly_btn = QPushButton("Manager Only")
        self.employeeVisitor_btn = QPushButton("Manager-Customer")
        self.back_btn = QPushButton("Back")

        vbox = QVBoxLayout()
        vbox.addWidget(self.userOnly_btn)
        vbox.addWidget(self.visitorOnly_btn)
        vbox.addWidget(self.employeeOnly_btn)
        vbox.addWidget(self.employeeVisitor_btn)
        vbox.addWidget(self.back_btn)
        self.setLayout(vbox)

        self.userOnly_btn.clicked.connect(self.startUserOnlyRegistration)
        self.visitorOnly_btn.clicked.connect(self.startVisitorOnlyRegistration)
        self.employeeOnly_btn.clicked.connect(self.startEmployeeOnlyRegistration)
        self.employeeVisitor_btn.clicked.connect(self.startEmployeeVisitorRegistration)
        self.back_btn.clicked.connect(self.startBack)

    def startUserOnlyRegistration(self):
        self.w = RegisterUserOnly()
        self.w.show()
        self.hide()

    def startVisitorOnlyRegistration(self):
        self.w = RegisterVistorOnly()
        self.w.show()
        self.hide()

    def startEmployeeOnlyRegistration(self):
        self.w = RegisterEmployeeOnly()
        self.w.show()
        self.hide()

    def startEmployeeVisitorRegistration(self):
        self.w = RegisterEmployeeVisitor()
        self.w.show()
        self.hide()

    def startBack(self):
        self.w = UserLogin()
        self.w.show()
        self.hide()

class RegisterUserOnly(QWidget): #Screen 3
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label1 = QLabel("First Name:", self)
        self.label2 = QLabel("Username:", self)
        self.label3 = QLabel("Password:", self)
        self.label4 = QLabel("Last Name:", self)
        self.label5 = QLabel("Confirm Password:", self)


        self.textbox1 = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.textbox3 = QLineEdit(self)
        self.textbox4 = QLineEdit(self)
        self.textbox4.setEchoMode(QLineEdit.Password)
        self.textbox5 = QLineEdit(self)
        self.textbox5.setEchoMode(QLineEdit.Password)
        self.emailbox1 = QLineEdit(self)
        self.emailbox2 = QLineEdit(self)
        self.emailbox3 = QLineEdit(self)
        self.emailbox4 = QLineEdit(self)

        self.back_btn = QPushButton("Back")
        self.register_btn = QPushButton("Register")

        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox41 = QHBoxLayout()
        self.hbox42 = QHBoxLayout()
        self.hbox43 = QHBoxLayout()
        self.hbox44 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()

        self.hbox1.addWidget(self.label1)
        self.hbox1.addWidget(self.textbox1)
        self.hbox1.addWidget(self.label4)
        self.hbox1.addWidget(self.textbox2)
        self.hbox2.addWidget(self.label2)
        self.hbox2.addWidget(self.textbox3)
        self.hbox3.addWidget(self.label3)
        self.hbox3.addWidget(self.textbox4)
        self.hbox3.addWidget(self.label5)
        self.hbox3.addWidget(self.textbox5)

        self.hbox5.addWidget(self.back_btn)
        self.hbox5.addWidget(self.register_btn)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox5)
        self.setLayout(self.vbox)

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('User Registration')
        self.show()

        self.back_btn.clicked.connect(self.startBack)
        self.register_btn.clicked.connect(self.registerUser)

    def startBack(self):
        self.w = RegisterNavigation()
        self.w.show()
        self.hide()

    def registerUser(self):
        # if fieldvalidation(self,self.emailbox1.text(),self.textbox1.text(),self.textbox2.text(),self.textbox3.text(),self.textbox4.text(),self.textbox5.text(),self.emailbox2.text(),self.emailbox3.text(),self.emailbox4.text(), '','','','','','') == True :
        #
        #     hashPassword = hashedPassword(self.textbox4.text())
        #
        #     global connection
        #
        #
        #     cursor = connection.cursor()
        #     cursor.execute("""
        #         INSERT INTO User
        #             (Username, Password, Status,Firstname,Lastname)
        #         VALUES
        #             (%s, %s, %s, %s, %s)
        #         ON DUPLICATE KEY UPDATE
        #                                           -- no need to update the PK
        #             Username  = VALUES(Username) ;
        #                    """, (self.textbox3.text(), hashPassword, "Pending",self.textbox1.text(),self.textbox2.text())     # python variables
        #                   )

            for x in range(0, 3):
                email = self.emailbox1.text()
                if  x==0 and self.lblEmail4.isHidden() != True:
                    email = self.emailbox4.text()
                if  x==1 and self.lblEmail3.isHidden() != True:
                    email = self.emailbox3.text()
                if  x==0 and self.lblEmail2.isHidden() != True:
                    email = self.emailbox2.text()

            #     cursor.execute("""
            #         INSERT INTO Useremail
            #             (Username, Email)
            #         VALUES
            #             (%s, %s)
            #         ON DUPLICATE KEY UPDATE
            #                                           -- no need to update the PK
            #             Username  = VALUES(Username),
            #             Email  = VALUES(Email) ;
            #                    """, (self.textbox3.text(), email)     # python variables
            #                   )
            # connection.commit()
            self.textbox1.setEnabled(False)
            self.textbox2.setEnabled(False)
            self.textbox3.setEnabled(False)
            self.textbox4.setEnabled(False)
            self.textbox5.setEnabled(False)
            self.emailbox1.setEnabled(False)
            self.register_btn.setText("Saved")

class RegisterVistorOnly(QWidget): #Screen 4
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.label1 = QLabel("First Name:", self)
        self.label2 = QLabel("Username:", self)
        self.label3 = QLabel("Password:", self)
        self.label4 = QLabel("Last Name:", self)
        self.label5 = QLabel("Confirm Password:", self)
        self.lblEmail1 = QLabel("Credit Card Number:", self)
        self.lblEmail2 = QLabel("Credit Card Number:", self)
        self.lblEmail3 = QLabel("Credit Card Number:", self)
        self.lblEmail4 = QLabel("Credit Card Number:", self)
        self.lblEmail5 = QLabel("Credit Card Number:", self)

        self.textbox1 = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.textbox3 = QLineEdit(self)
        self.textbox4 = QLineEdit(self)
        self.textbox4.setEchoMode(QLineEdit.Password)
        self.textbox5 = QLineEdit(self)
        self.textbox5.setEchoMode(QLineEdit.Password)
        self.emailbox1 = QLineEdit(self)
        self.emailbox2 = QLineEdit(self)
        self.emailbox3 = QLineEdit(self)
        self.emailbox4 = QLineEdit(self)
        self.emailbox5 = QLineEdit(self)

        self.add_btn = QPushButton("Add")
        self.remove_btn1 = QPushButton("Remove")
        self.remove_btn2 = QPushButton("Remove")
        self.remove_btn3 = QPushButton("Remove")
        self.remove_btn4 = QPushButton("Remove")
        self.back_btn = QPushButton("Back")
        self.register_btn = QPushButton("Register")

        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox41 = QHBoxLayout()
        self.hbox42 = QHBoxLayout()
        self.hbox43 = QHBoxLayout()
        self.hbox44 = QHBoxLayout()
        self.hbox45 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()

        self.hbox1.addWidget(self.label1)
        self.hbox1.addWidget(self.textbox1)
        self.hbox1.addWidget(self.label4)
        self.hbox1.addWidget(self.textbox2)

        self.hbox2.addWidget(self.label2)
        self.hbox2.addWidget(self.textbox3)

        self.hbox3.addWidget(self.label3)
        self.hbox3.addWidget(self.textbox4)
        self.hbox3.addWidget(self.label5)
        self.hbox3.addWidget(self.textbox5)

        self.hbox41.addWidget(self.lblEmail1)
        self.hbox41.addWidget(self.emailbox1)
        self.hbox41.addWidget(self.add_btn)

        self.hbox42.addWidget(self.lblEmail2)
        self.hbox42.addWidget(self.emailbox2)
        self.hbox42.addWidget(self.remove_btn1)

        self.hbox43.addWidget(self.lblEmail3)
        self.hbox43.addWidget(self.emailbox3)
        self.hbox43.addWidget(self.remove_btn2)

        self.hbox44.addWidget(self.lblEmail4)
        self.hbox44.addWidget(self.emailbox4)
        self.hbox44.addWidget(self.remove_btn3)

        self.hbox45.addWidget(self.lblEmail5)
        self.hbox45.addWidget(self.emailbox5)
        self.hbox45.addWidget(self.remove_btn4)

        self.hbox5.addWidget(self.back_btn)
        self.hbox5.addWidget(self.register_btn)


        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox41)
        self.vbox.addLayout(self.hbox42)
        self.vbox.addLayout(self.hbox43)
        self.vbox.addLayout(self.hbox44)
        self.vbox.addLayout(self.hbox45)
        self.vbox.addLayout(self.hbox5)

        self.lblEmail2.setHidden(True)
        self.emailbox2.setHidden(True)
        self.remove_btn1.setHidden(True)

        self.lblEmail3.setHidden(True)
        self.emailbox3.setHidden(True)
        self.remove_btn2.setHidden(True)

        self.lblEmail4.setHidden(True)
        self.emailbox4.setHidden(True)
        self.remove_btn3.setHidden(True)

        self.lblEmail5.setHidden(True)
        self.emailbox5.setHidden(True)
        self.remove_btn4.setHidden(True)

        self.setLayout(self.vbox)

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Customer Registration')
        self.show()

        self.back_btn.clicked.connect(self.startBack)
        self.register_btn.clicked.connect(self.registerUser)
        self.add_btn.clicked.connect(self.addWidget)
        self.remove_btn1.clicked.connect(self.removeWidget1)
        self.remove_btn2.clicked.connect(self.removeWidget2)
        self.remove_btn3.clicked.connect(self.removeWidget3)
        self.remove_btn3.clicked.connect(self.removeWidget4)

    def addWidget(self):
        if  self.lblEmail2.isHidden():
            self.lblEmail2.setHidden(False)
            self.emailbox2.setHidden(False)
            self.remove_btn1.setHidden(False)
        elif self.lblEmail3.isHidden():
            self.lblEmail3.setHidden(False)
            self.emailbox3.setHidden(False)
            self.remove_btn2.setHidden(False)
        elif self.lblEmail4.isHidden():
            self.lblEmail4.setHidden(False)
            self.emailbox4.setHidden(False)
            self.remove_btn3.setHidden(False)
        elif self.lblEmail5.isHidden():
            self.lblEmail5.setHidden(False)
            self.emailbox5.setHidden(False)
            self.remove_btn4.setHidden(False)

    def removeWidget1(self):
        self.lblEmail2.setHidden(True)
        self.emailbox2.setHidden(True)
        self.remove_btn1.setHidden(True)

    def removeWidget2(self):
        self.lblEmail3.setHidden(True)
        self.emailbox3.setHidden(True)
        self.remove_btn2.setHidden(True)

    def removeWidget3(self):
        self.lblEmail4.setHidden(True)
        self.emailbox4.setHidden(True)
        self.remove_btn3.setHidden(True)


    def removeWidget4(self):
        self.lblEmail5.setHidden(True)
        self.emailbox5.setHidden(True)
        self.remove_btn4.setHidden(True)

    def startBack(self):
        self.w = RegisterNavigation()
        self.w.show()
        self.hide()

    def registerUser(self):
        # if fieldvalidation(self,self.emailbox1.text(),self.textbox1.text(),self.textbox2.text(),self.textbox3.text(),self.textbox4.text(),self.textbox5.text(),self.emailbox2.text(),self.emailbox3.text(),self.emailbox4.text(),'','','','','','') == True :
        #
        #     hashPassword = hashedPassword(self.textbox4.text())
        #
        #     global connection


            #cursor = connection.cursor()
            # cursor.execute("""
            #     INSERT INTO User
            #         (Username, Password, Status,Firstname,Lastname)
            #     VALUES
            #         (%s, %s, %s, %s, %s)
            #     ON DUPLICATE KEY UPDATE
            #                                       -- no need to update the PK
            #         Username  = VALUES(Username) ;
            #                """, (self.textbox3.text(), hashPassword, "Pending",self.textbox1.text(),self.textbox2.text())     # python variables
            #               )


            #cursor = connection.cursor()
            # cursor.execute("""
            #     INSERT INTO Visitor
            #         (Username)
            #     VALUES
            #         (%s)
            #     ON DUPLICATE KEY UPDATE
            #                                       -- no need to update the PK
            #         Username  = VALUES(Username) ;
            #                """, (self.textbox3.text())     # python variables
            #               )


            for x in range(0, 3):
                email = self.emailbox1.text()
                if  x==0 and self.lblEmail4.isHidden() != True:
                    email = self.emailbox4.text()
                if  x==1 and self.lblEmail3.isHidden() != True:
                    email = self.emailbox3.text()
                if  x==0 and self.lblEmail2.isHidden() != True:
                    email = self.emailbox2.text()

            #     cursor.execute("""
            #         INSERT INTO Useremail
            #             (Username, Email)
            #         VALUES
            #             (%s, %s)
            #         ON DUPLICATE KEY UPDATE
            #                                           -- no need to update the PK
            #             Username  = VALUES(Username),
            #             Email  = VALUES(Email) ;
            #                    """, (self.textbox3.text(), email)     # python variables
            #                   )
            # connection.commit()
            self.textbox1.setEnabled(False)
            self.textbox2.setEnabled(False)
            self.textbox3.setEnabled(False)
            self.textbox4.setEnabled(False)
            self.textbox5.setEnabled(False)
            self.emailbox1.setEnabled(False)
            self.register_btn.setText("Saved")

class RegisterEmployeeOnly(QWidget): #Screen 5
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel("First Name:", self)
        self.label2 = QLabel("Username:", self)
        self.label3 = QLabel("Password:", self)
        self.label5 = QLabel("Last Name:", self)
        self.label6 = QLabel("Company:", self)
        self.label7 = QLabel("Confirm Password:", self)
        self.label8 = QLabel("Street Address:", self)
        self.label9 = QLabel("City:", self)
        self.label10 = QLabel("State:", self)
        self.label11 = QLabel("Zipcode:", self)


        self.textbox1 = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.textbox3 = QLineEdit(self)
        self.textbox5 = QLineEdit(self)
        self.textbox5.setEchoMode(QLineEdit.Password)
        self.textbox6 = QLineEdit(self)
        self.textbox6.setEchoMode(QLineEdit.Password)
        #self.textbox7 = QLineEdit(self)
        self.textbox8 = QLineEdit(self)
        self.textbox9 = QLineEdit(self)
        self.textbox11 = QLineEdit(self)


        self.add_btn = QPushButton("Add")
        self.remove_btn1 = QPushButton("Remove")
        self.remove_btn2 = QPushButton("Remove")
        self.remove_btn3 = QPushButton("Remove")
        self.back_btn = QPushButton("Back")
        self.register_btn = QPushButton("Register")

        self.combo1 = QComboBox(self)
        self.combo1.addItem("")
        self.combo1.addItem("EZ Theater Company")
        self.combo1.addItem("4400 Theater Company")
        self.combo1.addItem("Awesome Theater Company")
        self.combo1.addItem("AI Theater Company")

        self.combo2 = QComboBox(self)
        self.combo2.addItem("")
        self.combo2.addItem("AK")
        self.combo2.addItem("AZ")
        self.combo2.addItem("AR")
        self.combo2.addItem("CA")
        self.combo2.addItem("CO")
        self.combo2.addItem("CT")
        self.combo2.addItem("DL")
        self.combo2.addItem("FL")
        self.combo2.addItem("GA")
        self.combo2.addItem("HI")
        self.combo2.addItem("ID")
        self.combo2.addItem("IL")
        self.combo2.addItem("IN")
        self.combo2.addItem("IA")
        self.combo2.addItem("KS")
        self.combo2.addItem("KY")
        self.combo2.addItem("LA")
        self.combo2.addItem("ME")
        self.combo2.addItem("MD")
        self.combo2.addItem("MA")
        self.combo2.addItem("MI")
        self.combo2.addItem("MN")
        self.combo2.addItem("MS")
        self.combo2.addItem("MO")
        self.combo2.addItem("MT")
        self.combo2.addItem("NE")
        self.combo2.addItem("NV")
        self.combo2.addItem("NH")
        self.combo2.addItem("NJ")
        self.combo2.addItem("NL")
        self.combo2.addItem("NY")
        self.combo2.addItem("NC")
        self.combo2.addItem("ND")
        self.combo2.addItem("OH")
        self.combo2.addItem("OK")
        self.combo2.addItem("OR")
        self.combo2.addItem("PA")
        self.combo2.addItem("RI")
        self.combo2.addItem("SC")
        self.combo2.addItem("SD")
        self.combo2.addItem("TN")
        self.combo2.addItem("TX")
        self.combo2.addItem("UT")
        self.combo2.addItem("VT")
        self.combo2.addItem("VA")
        self.combo2.addItem("WA")
        self.combo2.addItem("WV")
        self.combo2.addItem("WI")
        self.combo2.addItem("WY")

        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        self.hbox41 = QHBoxLayout()
        self.hbox42 = QHBoxLayout()
        self.hbox43 = QHBoxLayout()
        self.hbox44 = QHBoxLayout()
        self.hbox7 = QHBoxLayout()

        self.hbox1.addWidget(self.label)
        self.hbox1.addWidget(self.textbox1)
        self.hbox1.addWidget(self.label5)
        self.hbox1.addWidget(self.textbox2)
        self.hbox2.addWidget(self.label2)
        self.hbox2.addWidget(self.textbox3)
        self.hbox2.addWidget(self.label6)
        self.hbox2.addWidget(self.combo1)
        self.hbox3.addWidget(self.label3)
        self.hbox3.addWidget(self.textbox5)
        self.hbox3.addWidget(self.label7)
        self.hbox3.addWidget(self.textbox6)

        #self.hbox4.addWidget(self.textbox7)
        self.hbox4.addWidget(self.label8)
        self.hbox4.addWidget(self.textbox8)
        self.hbox5.addWidget(self.label9)
        self.hbox5.addWidget(self.textbox9)
        self.hbox5.addWidget(self.label10)
        self.hbox5.addWidget(self.combo2)
        self.hbox5.addWidget(self.label11)
        self.hbox5.addWidget(self.textbox11)

        self.hbox7.addWidget(self.back_btn)
        self.hbox7.addWidget(self.register_btn)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addLayout(self.hbox7)


        self.setLayout(self.vbox)

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Register Employee Only')
        self.show()

        self.back_btn.clicked.connect(self.startBack)
        self.register_btn.clicked.connect(self.registerUser)



    def startBack(self):
        self.w = RegisterNavigation()
        self.w.show()
        self.hide()

    def registerUser(self):
        if self.combo1.currentText() == '':
            buttonReply = QMessageBox.information(self, 'User Type is Required', "User Type is Required.", QMessageBox.Ok)

        # elif fieldvalidation(self,self.emailbox1.text(),self.textbox1.text(),self.textbox2.text(),self.textbox3.text(),self.textbox5.text(),self.textbox6.text(),self.emailbox2.text(),self.emailbox3.text(),self.emailbox4.text(),'EMP',self.textbox7.text(),self.textbox8.text(),self.textbox9.text(),self.combo2.currentText(),self.textbox11.text()) == True :
        #
        #     hashPassword = hashedPassword(self.textbox5.text())
        #     global connection
        #
        #     with connection.cursor() as cursor:
        #         # Read a single record
        #         sql = "  select count(*) + 1 as 'rows' from Employee;"
        #         cursor.execute(sql)
        #         empCount = cursor.fetchall()
        #
        #     uniqueEmpId = 99
        #     for row in empCount :
        #         uniqueEmpId = list(row.values())[0]


            # cursor = connection.cursor()
            # cursor.execute("""
            #     INSERT INTO User
            #         (Username, Password, Status,Firstname,Lastname)
            #     VALUES
            #         (%s, %s, %s, %s, %s)
            #     ON DUPLICATE KEY UPDATE
            #                                       -- no need to update the PK
            #         Username  = VALUES(Username) ;
            #                """, (self.textbox3.text(), hashPassword, "Pending",self.textbox1.text(),self.textbox2.text())     # python variables
            #               )
            #
            # #uniqueEmpId = calendar.timegm(time.strptime('Apr 15, 2019 @ 20:02:58 UTC', '%b %d, %Y @ %H:%M:%S UTC'))
            # phonenum = 0
            # if self.textbox7.text() != '' and self.textbox7.text().isdigit() :
            #     phonenum = self.textbox7.text()
            #
            # zipcodenum = 0
            # if self.textbox11.text() != '' and self.textbox11.text().isdigit() :
            #     zipcodenum = self.textbox11.text()

            # cursor = connection.cursor()
            # cursor.execute("""
            #     INSERT INTO Employee
            #         (Username, EmployeeID, Phone,EmployeeAddress,EmployeeEmployeeCity,EmployeeState,EmplopeeZipcode)
            #     VALUES
            #         (%s, %s, %s, %s, %s, %s, %s)
            #     ON DUPLICATE KEY UPDATE
            #                                       -- no need to update the PK
            #         Username  = VALUES(Username) ;
            #                """, (self.textbox3.text(), uniqueEmpId, phonenum ,self.textbox8.text(),self.textbox9.text(),self.combo2.currentText() ,zipcodenum)     # python variables
            #               )
            #
            # if self.combo1.currentText() == 'Manager':
            #     cursor = connection.cursor()
            #     cursor.execute("""
            #         INSERT INTO Manager
            #             (Username)
            #         VALUES
            #             (%s)
            #         ON DUPLICATE KEY UPDATE
            #                                           -- no need to update the PK
            #             Username  = VALUES(Username) ;
            #                    """, (self.textbox3.text())     # python variables
            #                   )
            #     connection.commit()

            # if self.combo1.currentText() == 'Staff':
            #     cursor = connection.cursor()
            #     cursor.execute("""
            #         INSERT INTO Staff
            #             (Username)
            #         VALUES
            #             (%s)
            #         ON DUPLICATE KEY UPDATE
            #                                           -- no need to update the PK
            #             Username  = VALUES(Username) ;
            #                    """, (self.textbox3.text())     # python variables
            #                   )
            #     connection.commit()

            for x in range(0, 3):
                email = self.emailbox1.text()
                if  x==0 and self.lblEmail4.isHidden() != True:
                    email = self.emailbox4.text()
                if  x==1 and self.lblEmail3.isHidden() != True:
                    email = self.emailbox3.text()
                if  x==0 and self.lblEmail2.isHidden() != True:
                    email = self.emailbox2.text()

            #     cursor.execute("""
            #         INSERT INTO Useremail
            #             (Username, Email)
            #         VALUES
            #             (%s, %s)
            #         ON DUPLICATE KEY UPDATE
            #                                           -- no need to update the PK
            #             Username  = VALUES(Username),
            #             Email  = VALUES(Email) ;
            #                    """, (self.textbox3.text(), email)     # python variables
            #                   )
            # connection.commit()
            self.textbox1.setEnabled(False)
            self.textbox2.setEnabled(False)
            self.textbox3.setEnabled(False)
            self.textbox5.setEnabled(False)
            #self.textbox7.setEnabled(False)
            self.emailbox1.setEnabled(False)
            self.register_btn.setText("Saved")

class RegisterEmployeeVisitor(QWidget): #Screen6
    def __init__(self):
        self.amountOfCreditCards = [0, 0, 0, 0, 0]
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel("First Name:", self)
        self.label2 = QLabel("Username:", self)
        self.label3 = QLabel("Password:", self)
        self.label5 = QLabel("Last Name:", self)
        self.label6 = QLabel("Company:", self)
        self.label7 = QLabel("Confirm Password:", self)
        self.label8 = QLabel("Street Address:", self)
        self.label9 = QLabel("City:", self)
        self.label10 = QLabel("State:", self)
        self.label11 = QLabel("Zipcode:", self)
        self.lblEmail1 = QLabel("Credit Card Number:", self)
        self.lblEmail2 = QLabel("Credit Card Number:", self)
        self.lblEmail3 = QLabel("Credit Card Number:", self)
        self.lblEmail4 = QLabel("Credit Card Number:", self)
        self.lblEmail5 = QLabel("Credit Card Number:", self)
        self.lblEmail6 = QLabel("Credit Card Number:", self)

        self.textbox1 = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.textbox3 = QLineEdit(self)
        self.textbox5 = QLineEdit(self)
        self.textbox5.setEchoMode(QLineEdit.Password)
        self.textbox6 = QLineEdit(self)
        self.textbox6.setEchoMode(QLineEdit.Password)
        self.textbox8 = QLineEdit(self)
        self.textbox9 = QLineEdit(self)
        self.textbox11 = QLineEdit(self)
        self.emailbox1 = QLineEdit(self)
        self.emailbox2 = QLineEdit(self)
        self.emailbox3 = QLineEdit(self)
        self.emailbox4 = QLineEdit(self)
        self.emailbox5 = QLineEdit(self)
        self.emailbox6 = QLineEdit(self)

        self.add_btn = QPushButton("Add")
        self.remove_btn1 = QPushButton("Remove")
        self.remove_btn2 = QPushButton("Remove")
        self.remove_btn3 = QPushButton("Remove")
        self.remove_btn4 = QPushButton("Remove")
        self.remove_btn5 = QPushButton("Remove")
        self.back_btn = QPushButton("Back")
        self.register_btn = QPushButton("Register")

        self.combo1 = QComboBox(self)
        self.combo1.addItem("")
        self.combo1.addItem("EZ Theater Company")
        self.combo1.addItem("4400 Theater Company")
        self.combo1.addItem("Awesome Theater Company")
        self.combo1.addItem("AI Theater Company")

        self.combo2 = QComboBox(self)
        self.combo2.addItem("")
        self.combo2.addItem("AK")
        self.combo2.addItem("AZ")
        self.combo2.addItem("AR")
        self.combo2.addItem("CA")
        self.combo2.addItem("CO")
        self.combo2.addItem("CT")
        self.combo2.addItem("DL")
        self.combo2.addItem("FL")
        self.combo2.addItem("GA")
        self.combo2.addItem("HI")
        self.combo2.addItem("ID")
        self.combo2.addItem("IL")
        self.combo2.addItem("IN")
        self.combo2.addItem("IA")
        self.combo2.addItem("KS")
        self.combo2.addItem("KY")
        self.combo2.addItem("LA")
        self.combo2.addItem("ME")
        self.combo2.addItem("MD")
        self.combo2.addItem("MA")
        self.combo2.addItem("MI")
        self.combo2.addItem("MN")
        self.combo2.addItem("MS")
        self.combo2.addItem("MO")
        self.combo2.addItem("MT")
        self.combo2.addItem("NE")
        self.combo2.addItem("NV")
        self.combo2.addItem("NH")
        self.combo2.addItem("NJ")
        self.combo2.addItem("NL")
        self.combo2.addItem("NY")
        self.combo2.addItem("NC")
        self.combo2.addItem("ND")
        self.combo2.addItem("OH")
        self.combo2.addItem("OK")
        self.combo2.addItem("OR")
        self.combo2.addItem("PA")
        self.combo2.addItem("RI")
        self.combo2.addItem("SC")
        self.combo2.addItem("SD")
        self.combo2.addItem("TN")
        self.combo2.addItem("TX")
        self.combo2.addItem("UT")
        self.combo2.addItem("VT")
        self.combo2.addItem("VA")
        self.combo2.addItem("WA")
        self.combo2.addItem("WV")
        self.combo2.addItem("WI")
        self.combo2.addItem("WY")

        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        self.hbox41 = QHBoxLayout()
        self.hbox42 = QHBoxLayout()
        self.hbox43 = QHBoxLayout()
        self.hbox44 = QHBoxLayout()
        self.hbox45 = QHBoxLayout()
        self.hbox45 = QHBoxLayout()
        self.hbox46 = QHBoxLayout()
        self.hbox7 = QHBoxLayout()
        #
        self.hbox1.addWidget(self.label)
        self.hbox1.addWidget(self.textbox1)
        self.hbox1.addWidget(self.label5)
        self.hbox1.addWidget(self.textbox2)
        self.hbox2.addWidget(self.label2)
        self.hbox2.addWidget(self.textbox3)
        self.hbox2.addWidget(self.label6)
        self.hbox2.addWidget(self.combo1)
        self.hbox3.addWidget(self.label3)
        self.hbox3.addWidget(self.textbox5)
        self.hbox3.addWidget(self.label7)
        self.hbox3.addWidget(self.textbox6)
        # # self.hbox4.addWidget(self.label4)
        # # self.hbox4.addWidget(self.textbox7)
        self.hbox4.addWidget(self.label8)
        self.hbox4.addWidget(self.textbox8)
        self.hbox5.addWidget(self.label9)
        self.hbox5.addWidget(self.textbox9)
        self.hbox5.addWidget(self.label10)
        self.hbox5.addWidget(self.combo2)
        self.hbox5.addWidget(self.label11)
        self.hbox5.addWidget(self.textbox11)
        self.hbox41.addWidget(self.lblEmail1)
        self.hbox41.addWidget(self.emailbox1)
        self.hbox41.addWidget(self.add_btn)
        self.hbox42.addWidget(self.lblEmail2)
        self.hbox42.addWidget(self.emailbox2)
        self.hbox42.addWidget(self.remove_btn1)
        self.hbox43.addWidget(self.lblEmail3)
        self.hbox43.addWidget(self.emailbox3)
        self.hbox43.addWidget(self.remove_btn2)
        self.hbox44.addWidget(self.lblEmail4)
        self.hbox44.addWidget(self.emailbox4)
        self.hbox44.addWidget(self.remove_btn3)
        self.hbox45.addWidget(self.lblEmail5)
        self.hbox45.addWidget(self.emailbox5)
        self.hbox45.addWidget(self.remove_btn4)
        self.hbox46.addWidget(self.lblEmail6)
        self.hbox46.addWidget(self.emailbox6)
        self.hbox46.addWidget(self.remove_btn5)
        self.hbox7.addWidget(self.back_btn)
        self.hbox7.addWidget(self.register_btn)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addLayout(self.hbox41)
        self.cc1 = QWidget()
        self.cc1.setLayout(self.hbox42)
        self.vbox.addWidget(self.cc1)
        self.cc2 = QWidget()
        self.cc2.setLayout(self.hbox43)
        self.vbox.addWidget(self.cc2)
        self.cc3 = QWidget()
        self.cc3.setLayout(self.hbox44)
        self.vbox.addWidget(self.cc3)
        self.cc4 = QWidget()
        self.cc4.setLayout(self.hbox45)
        self.vbox.addWidget(self.cc4)
        self.cc5 = QWidget()
        self.cc5.setLayout(self.hbox46)
        self.vbox.addWidget(self.cc5)
        self.vbox.addLayout(self.hbox7)
        # self.lblEmail2.setHidden(True)
        # self.emailbox2.setHidden(True)
        # self.remove_btn1.setHidden(True)
        # self.lblEmail3.setHidden(True)
        # self.emailbox3.setHidden(True)
        # self.remove_btn2.setHidden(True)
        # self.lblEmail4.setHidden(True)
        # self.emailbox4.setHidden(True)
        # self.remove_btn3.setHidden(True)
        # self.emailbox5.setHidden(True)
        # self.remove_btn5.setHidden(True)

        self.setLayout(self.vbox)

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Register Employee Visitor')
        self.show()

        self.back_btn.clicked.connect(self.startBack)
        self.register_btn.clicked.connect(self.registerUser)
        self.add_btn.clicked.connect(self.addWidget)
        self.remove_btn1.clicked.connect(self.removeWidget1)
        self.remove_btn2.clicked.connect(self.removeWidget2)
        self.remove_btn3.clicked.connect(self.removeWidget3)
        self.remove_btn4.clicked.connect(self.removeWidget4)
        self.remove_btn5.clicked.connect(self.removeWidget5)

    def addWidget(self):
        inx = 0
        for i in range(0, len(self.amountOfCreditCards)):
            if self.amountOfCreditCards[i] == 0:
                self.amountOfCreditCards[i] = 1
                inx = i
                break

        if inx == 0:
            self.emailbox2.setText(self.emailbox1.text())
            self.emailbox2.update()
            self.emailbox1.setText("")
            self.emailbox1.update()
            self.repaint()

        elif inx == 1:
            self.emailbox3.setText(self.emailbox1.text())
            self.emailbox3.update()
            self.emailbox1.setText("")
            self.emailbox1.update()
            self.repaint()

        elif inx == 2:
            self.emailbox4.setText(self.emailbox1.text())
            self.emailbox4.update()
            self.emailbox1.setText("")
            self.emailbox1.update()
            self.repaint()

        elif inx == 3:
            self.emailbox5.setText(self.emailbox1.text())
            self.emailbox5.update()
            self.emailbox1.setText("")
            self.emailbox1.update()
            self.repaint()

        elif inx == 4:
            self.emailbox6.setText(self.emailbox1.text())
            self.emailbox6.update()
            self.emailbox1.setText("")
            self.emailbox1.update()
            self.repaint()


    def removeWidget1(self):
        self.amountOfCreditCards[0] = 0
        self.emailbox2.setText("")
        self.repaint()

    def removeWidget2(self):
        self.amountOfCreditCards[1] = 0
        self.emailbox3.setText("")
        self.repaint()

    def removeWidget3(self):
        self.amountOfCreditCards[2] = 0
        self.emailbox4.setText("")
        self.repaint()

    def removeWidget4(self):
        self.amountOfCreditCards[3] = 0
        self.emailbox5.setText("")
        self.repaint()

    def removeWidget5(self):
        self.amountOfCreditCards[4] = 0
        self.emailbox6.setText("")
        self.repaint()

    def startBack(self):
        self.w = RegisterNavigation()
        self.w.show()
        self.hide()

    def registerUser(self):
        if self.combo1.currentText() == '':
            buttonReply = QMessageBox.information(self, 'User Type is Required', "User Type is Required.", QMessageBox.Ok)

        # elif fieldvalidation(self,self.emailbox1.text(),self.textbox1.text(),self.textbox2.text(),self.textbox3.text(),self.textbox5.text(),self.textbox6.text(),self.emailbox2.text(),self.emailbox3.text(),self.emailbox4.text(),'EMP',self.textbox7.text(),self.textbox8.text(),self.textbox9.text(),self.combo2.currentText(),self.textbox11.text()) == True :
        #
        #     hashPassword = hashedPassword(self.textbox5.text())
        #     global connection
        #
        #     with connection.cursor() as cursor:
        #         # Read a single record
        #         sql = "  select count(*) + 1 as 'rows' from Employee;"
        #         cursor.execute(sql)
        #         empCount = cursor.fetchall()
        #
        #     uniqueEmpId = 99
        #     for row in empCount :
        #         uniqueEmpId = list(row.values())[0]


            # cursor = connection.cursor()
            # cursor.execute("""
            #     INSERT INTO User
            #         (Username, Password, Status,Firstname,Lastname)
            #     VALUES
            #         (%s, %s, %s, %s, %s)
            #     ON DUPLICATE KEY UPDATE
            #                                       -- no need to update the PK
            #         Username  = VALUES(Username) ;
            #                """, (self.textbox3.text(), hashPassword, "Pending",self.textbox1.text(),self.textbox2.text())     # python variables
            #               )
            #
            # #uniqueEmpId = calendar.timegm(time.strptime('Apr 15, 2019 @ 20:02:58 UTC', '%b %d, %Y @ %H:%M:%S UTC'))
            # phonenum = 0
            # if self.textbox7.text() != '' and self.textbox7.text().isdigit() :
            #     phonenum = self.textbox7.text()
            #
            # zipcodenum = 0
            # if self.textbox11.text() != '' and self.textbox11.text().isdigit() :
            #     zipcodenum = self.textbox11.text()
            #
            # cursor = connection.cursor()
            # cursor.execute("""
            #     INSERT INTO Employee
            #         (Username, EmployeeID, Phone,EmployeeAddress,EmployeeEmployeeCity,EmployeeState,EmplopeeZipcode)
            #     VALUES
            #         (%s, %s, %s, %s, %s, %s, %s)
            #     ON DUPLICATE KEY UPDATE
            #                                       -- no need to update the PK
            #         Username  = VALUES(Username) ;
            #                """, (self.textbox3.text(), uniqueEmpId, phonenum ,self.textbox8.text(),self.textbox9.text(),self.combo2.currentText() ,zipcodenum)     # python variables
            #               )
            #
            # if self.combo1.currentText() == 'Manager':
            #     cursor = connection.cursor()
            #     cursor.execute("""
            #         INSERT INTO Manager
            #             (Username)
            #         VALUES
            #             (%s)
            #         ON DUPLICATE KEY UPDATE
            #                                           -- no need to update the PK
            #             Username  = VALUES(Username) ;
            #                    """, (self.textbox3.text())     # python variables
            #                   )
            #     connection.commit()
            #
            # if self.combo1.currentText() == 'Staff':
            #     cursor = connection.cursor()
            #     cursor.execute("""
            #         INSERT INTO Staff
            #             (Username)
            #         VALUES
            #             (%s)
            #         ON DUPLICATE KEY UPDATE
            #                                           -- no need to update the PK
            #             Username  = VALUES(Username) ;
            #                    """, (self.textbox3.text())     # python variables
            #                   )
            #     connection.commit()
            #
            # cursor = connection.cursor()
            # cursor.execute("""
            #     INSERT INTO Visitor
            #         (Username)
            #     VALUES
            #         (%s)
            #     ON DUPLICATE KEY UPDATE
            #                                       -- no need to update the PK
            #         Username  = VALUES(Username) ;
            #                """, (self.textbox3.text())     # python variables
            #               )

            for x in range(0, 3):
                email = self.emailbox1.text()
                if  x==0 and self.lblEmail4.isHidden() != True:
                    email = self.emailbox4.text()
                if  x==1 and self.lblEmail3.isHidden() != True:
                    email = self.emailbox3.text()
                if  x==0 and self.lblEmail2.isHidden() != True:
                    email = self.emailbox2.text()

            #     cursor.execute("""
            #         INSERT INTO Useremail
            #             (Username, Email)
            #         VALUES
            #             (%s, %s)
            #         ON DUPLICATE KEY UPDATE
            #                                           -- no need to update the PK
            #             Username  = VALUES(Username),
            #             Email  = VALUES(Email) ;
            #                    """, (self.textbox3.text(), email)     # python variables
            #                   )
            # connection.commit()
            self.textbox1.setEnabled(False)
            self.textbox2.setEnabled(False)
            self.textbox3.setEnabled(False)
            self.textbox5.setEnabled(False)
            #self.textbox7.setEnabled(False)
            self.emailbox1.setEnabled(False)
            self.register_btn.setText("Saved")

class UserFunctionality(QWidget): #Screen 7
    def __init__(self):
        super (UserFunctionality, self).__init__()
        self.setWindowTitle("User Functionality")

        left, top, width, height = 550, 50, 250, 400
        self.setGeometry(left, top, width, height)

        self.takeTransit_btn = QPushButton("Explore Theater")
        self.viewTransitHistory_btn = QPushButton ("Visit History")
        self.back_btn = QPushButton("Back")

        vbox = QVBoxLayout()
        vbox.addWidget(self.takeTransit_btn)
        vbox.addWidget(self.viewTransitHistory_btn)
        vbox.addWidget(self.back_btn)
        self.setLayout(vbox)

        self.takeTransit_btn.clicked.connect(self.takeTransit)
        self.viewTransitHistory_btn.clicked.connect(self.transitHistory)
        self.back_btn.clicked.connect(self.startBack)

    def startBack(self):
        self.w = UserLogin()
        self.w.show()
        self.hide()

    def transitHistory(self):

        # with connection.cursor() as cursor:
        #     # Read a single record
        #     #sql = "  select Username, Status, FirstName, Lastname from User ;"
        #     sql = " select cast(DATE_FORMAT(c.transitDate, '%Y-%m-%d') as char) as 'Date',  t.transitroute as 'Route', t.transittype as 'Transport Type', cast(t.price as char) " \
        #           " from transit t,taketransit c  where   t.transitType = c.transittype and  t.transitroute = c.transitroute and c.username = '" + loggedInUser + "' ; " \

        #     cursor.execute(sql)
        #     transitDetail = cursor.fetchall()

        self.w = UserTransitHistory(transitDetail)
        self.w.show()
        self.hide()

    def takeTransit(self):
        global connection

        with connection.cursor() as cursor:
            sql = " select t.transitroute as 'Route', t.transittype as 'Transport Type', cast(t.price as char) as 'Price', count(c.sitename) as 'Connected Sites' " \
                  " from transit t left outer join connect c on t.transitType = c.transittype and " \
                  " t.transitroute = c.transitroute group by t.transitroute, t.transittype, t.price ; " \

            cursor.execute(sql)
            transitDetail = cursor.fetchall()

        self.w = UserTakeTransit(transitDetail)
        self.w.show()
        self.hide()
class AdminOnlyFunctionality(QWidget): #screen 8
    def __init__(self):
        super (AdminOnlyFunctionality, self).__init__()

        self.setWindowTitle("Admin-Only Functionality")

        left, top, width, height = 550, 50, 250, 400
        self.setGeometry(left, top, width, height)

        self.manageUser_btn = QPushButton("Manage User")
        self.manageTransit_btn = QPushButton("Explore Theater")
        self.manageSite_btn = QPushButton("Manage Site")

        self.takeTransit_btn = QPushButton("Create Movie")
        self.viewTransit_btn = QPushButton("Visit History")
        self.back_btn = QPushButton("Back")

        vbox = QVBoxLayout()
        vbox.addWidget(self.manageUser_btn)
        vbox.addWidget(self.manageTransit_btn)
        vbox.addWidget(self.manageSite_btn)
        vbox.addWidget(self.takeTransit_btn)
        vbox.addWidget(self.viewTransit_btn)
        vbox.addWidget(self.back_btn)
        self.setLayout(vbox)


        self.manageUser_btn.clicked.connect(self.manageUser)
        self.manageSite_btn.clicked.connect(self.manageSite)
        self.manageTransit_btn.clicked.connect(self.manageTransit)
        self.takeTransit_btn.clicked.connect(self.takeTransit)
        self.viewTransit_btn.clicked.connect(self.transitHistory)
        self.back_btn.clicked.connect(self.startBack)


    def takeTransit(self):
        global connection

        with connection.cursor() as cursor:
            sql = " select t.transitroute as 'Route', t.transittype as 'Transport Type', cast(t.price as char) as 'Price', count(c.sitename) as 'Connected Sites' " \
                  " from transit t left outer join connect c on t.transitType = c.transittype and " \
                  " t.transitroute = c.transitroute group by t.transitroute, t.transittype, t.price ; " \

            cursor.execute(sql)
            transitDetail = cursor.fetchall()

        self.w = UserTakeTransit(transitDetail)
        self.w.show()
        self.hide()

    def transitHistory(self):

        with connection.cursor() as cursor:
            # Read a single record
            #sql = "  select Username, Status, FirstName, Lastname from User ;"
            sql = " select cast(DATE_FORMAT(c.transitDate, '%Y-%m-%d') as char) as 'Date',  t.transitroute as 'Route', t.transittype as 'Transport Type', cast(t.price as char) as 'price' " \
                  " from transit t,taketransit c  where   t.transitType = c.transittype and  t.transitroute = c.transitroute and c.username = '" + loggedInUser + "' ; " \

            cursor.execute(sql)
            transitDetail = cursor.fetchall()

        self.w = UserTransitHistory(transitDetail)
        self.w.show()
        self.hide()



    def manageTransit(self):
        global connection

        with connection.cursor() as cursor:
            sql = "  select * from " \
                  " (select transitroute, transittype, price, count(username) as '# Transit Logged' " \
                  " from transit natural join taketransit group by transitroute, transittype) as table1 " \
                  " natural join " \
                  " (select transitroute, transittype, price, count(sitename) as '# Connected Sites' " \
                  " from transit natural join connect group by transitroute, transittype) as table2; "

            cursor.execute(sql)
            transitDetail = cursor.fetchall()

        #print(usrDetail)
        self.w = AdministratorManageTransit(transitDetail)
        self.w.show()
        self.hide()


    def manageSite(self):
        global connection

        with connection.cursor() as cursor:
            #sql = "  select Sitename as 'Name' , SiteAddress, SiteZipcode, OpenEveryday, ManagerUsername " \
            sql = "  select Sitename as 'Name' , ManagerUsername as 'Manager', (case when OpenEveryday = 0 then 'No' else 'Yes' end) as 'Open Everyday' " \
                  "  from Site ; " #" where  '" + loggedInUser + "';"

            cursor.execute(sql)
            siteDetail = cursor.fetchall()

        #print(usrDetail)
        self.w = AdministratorManageSite(siteDetail)
        self.w.show()
        self.hide()


    # def manageProfile(self):
    #     #buttonReply = QMessageBox.information(self, 'Invlaid Option', "No Screen Defined in Document for Manage Administrator Profile.", QMessageBox.Ok)
    #     #return

    #     global connection

    #     with connection.cursor() as cursor:
    #         # Read a single record
    #         #sql = "  select Username, Status, FirstName, Lastname from User ;"
    #         sql = "  select u.Firstname, u.Lastname, u.Username, '' as Sitename, e.EmployeeID, e.Phone, " \
    #               "  e.EmployeeAddress  from user u, employee e  where u.username = e.username "\
    #               "  and  u.username = '" + loggedInUser + "';"

    #         print(sql)
    #         cursor.execute(sql)
    #         usrDetail = cursor.fetchall()


    #     #print(usrDetail)
    #     self.w = EmployeeManageProfile(usrDetail)
    #     self.w.show()
    #     self.hide()


    def manageUser(self):

        global connection

        with connection.cursor() as cursor:
            # Read a single record
            #sql = "  select Username, Status, FirstName, Lastname from User ;"
            sql = " select u.username, count(ue.username) as 'Email Count', " \
                  " ( case " \
                  " when m.username is not null then 'Manager' " \
                  " when s.username is not null then 'Staff' " \
                  " when v.username is not null then 'Visitor' " \
                  " else 'User' end ) as 'user type' , u.status " \
                  " from Useremail ue , User u " \
                  " left outer join Manager m on u.username = m.username " \
                  " left outer join Staff s ON u.username = s.username " \
                  " left outer join Visitor v ON u.username = v.username " \
                  " where u.username = ue.username group by u.username ; " \


            cursor.execute(sql)
            usrDetail = cursor.fetchall()


        self.w = AdministratorManageUser(usrDetail)
        self.w.show()
        self.hide()

    def startBack(self):
        self.w = UserLogin()
        self.w.show()
        self.hide()
class AdminstratorVisitorFunctionality(QWidget): #screen 9
    def __init__(self):
        super (AdminstratorVisitorFunctionality, self).__init__()
        self.setWindowTitle("Adminstrator-Customer Functionality")

        left, top, width, height = 550, 50, 250, 400
        self.setGeometry(left, top, width, height)

        self.manageUser_btn = QPushButton("Manage User")
        self.manageTransit_btn = QPushButton("Manage Company")
        self.manageSite_btn = QPushButton("Create Movie")

        self.exploreEvent_btn = QPushButton("Explore Theater")

        self.takeransit_btn = QPushButton("Create Movie")
        self.exploreSite_btn = QPushButton("Explore Movie")
        self.viewVisit_btn = QPushButton("Visit History")
        self.back_btn = QPushButton("Back")

        vbox = QVBoxLayout()
        vbox.addWidget(self.manageTransit_btn)
        vbox.addWidget(self.manageSite_btn)
        vbox.addWidget(self.exploreEvent_btn)
        vbox.addWidget(self.manageUser_btn)
        vbox.addWidget(self.takeransit_btn)
        vbox.addWidget(self.exploreSite_btn)
        vbox.addWidget(self.viewVisit_btn)
        vbox.addWidget(self.back_btn)
        self.setLayout(vbox)
        self.back_btn.clicked.connect(self.startBack)

    def startBack(self):
        self.w = UserLogin()
        self.w.show()
        self.hide()
class ManagerOnlyFunctionality(QWidget): #screen 10
    def __init__(self):
        super (ManagerOnlyFunctionality, self).__init__()
        self.setWindowTitle("Manager-Only Functionality")

        left, top, width, height = 550, 50, 250, 400
        self.setGeometry(left, top, width, height)

        self.manageProfile_btn = QPushButton("Theater Overview")
        self.manageEvent_btn = QPushButton("Explore Theater")
        self.viewStaff_btn = QPushButton("Schedule Movie")
        self.viewTransit_btn = QPushButton("View Transit History")
        self.back_btn = QPushButton("Back")

        vbox = QVBoxLayout()
        vbox.addWidget(self.manageProfile_btn)
        vbox.addWidget(self.manageEvent_btn)
        vbox.addWidget(self.viewStaff_btn)
        vbox.addWidget(self.viewTransit_btn)
        vbox.addWidget(self.back_btn)
        self.setLayout(vbox)

        self.manageProfile_btn.clicked.connect(self.manageProfile)
        self.viewStaff_btn.clicked.connect(self.managestaff)
        self.manageEvent_btn.clicked.connect(self.manageEvent)

        self.viewTransit_btn.clicked.connect(self.transitHistory)

        self.back_btn.clicked.connect(self.startBack)

    def startBack(self):
        self.w = UserLogin()
        self.w.show()
        self.hide()


    def takeTransit(self):
        global connection

        with connection.cursor() as cursor:
            sql = " select t.transitroute as 'Route', t.transittype as 'Transport Type', cast(t.price as char) as 'Price', count(c.sitename) as 'Connected Sites' " \
                  " from transit t left outer join connect c on t.transitType = c.transittype and " \
                  " t.transitroute = c.transitroute group by t.transitroute, t.transittype, t.price ; " \

            cursor.execute(sql)
            transitDetail = cursor.fetchall()

        self.w = UserTakeTransit(transitDetail)
        self.w.show()
        self.hide()

    def transitHistory(self):

        with connection.cursor() as cursor:
            # Read a single record
            #sql = "  select Username, Status, FirstName, Lastname from User ;"
            sql = " select cast(DATE_FORMAT(c.transitDate, '%Y-%m-%d') as char) as 'Date',  t.transitroute as 'Route', t.transittype as 'Transport Type', cast(t.price as char) as 'price' " \
                  " from transit t,taketransit c  where   t.transitType = c.transittype and  t.transitroute = c.transitroute and c.username = '" + loggedInUser + "' ; " \

            cursor.execute(sql)
            transitDetail = cursor.fetchall()

        self.w = UserTransitHistory(transitDetail)
        self.w.show()
        self.hide()



    def viewSiteReport(self):

        currentSite = 'orig' #getcurrentManagersite()

        global connection

        with connection.cursor() as cursor:
            sql =  "    select * from (select cast(startdate as char) as startdate, count(eventname) as eventcount " \
                    " from event where sitename = '" + currentSite + "' group by startdate) as table1 " \
                    " natural join  " \
                    " (select cast(startdate as char), count(staffusername) as staffcount  " \
                    " from assignto group by startdate) as table2 " \
                    " natural join  " \
                    " (select cast(startdate as char), count(visitorusername) as total_visits  " \
                    " from visitevent group by startdate) as table3 " \
                    " natural join  " \
                    " (select cast(startdate as char), sum(totalrevenue) as totalrevenue  " \
                    " from (select eventname, sitename, startdate, count(visitorusername) " \
                    " as totalvisits, (eventprice * count(visitorusername)) as totalrevenue from event natural join visitevent " \
                    "  where sitename = '" + currentSite + "' group by eventname, sitename, startdate) as table6 group by startdate)  " \
                    " as table4;"

            cursor.execute(sql)
            shiftreportDetail = cursor.fetchall()

        self.w = SiteReport(shiftreportDetail)
        self.w.show()
        self.hide()

    def manageEvent(self):
        global connection

        with connection.cursor() as cursor:
            sql =  "select e.eventname, datediff(e.enddate, e.startdate) as duration, " \
                    " count(staffusername) as staffcount, (select count(*) from visitevent v " \
                    " where v.eventname = e.eventname) as totalvisits, (select count(*) * e.eventprice from visitevent v " \
                    " where v.eventname = e.eventname) as totalrevenue   " \
                    " from event e left outer join visitevent v on e.eventname = v.eventname " \
                    " left outer join assignto a on e.eventname = a.eventname " \
                    " group by e.eventname, duration, totalvisits,  totalrevenue ;"

            print(sql)
            cursor.execute(sql)
            eventDetail = cursor.fetchall()



        self.w = ManagerManageEvent(eventDetail)
        self.w.show()
        self.hide()



    def managestaff(self):
        global connection

        with connection.cursor() as cursor:
            # Read a single record
            #sql = "  select Username, Status, FirstName, Lastname from User ;"
            sql = "select (select concat(u.firstname, ' ', u.lastname) from user u where u.username = " \
                  " s.username) as 'Staff Name', count(a.staffusername) as '# Event Shifts' from staff s " \
                  " left outer join assignto a on s.username = a.staffusername " \
                  " group by s.username ;"
            cursor.execute(sql)
            staffDetail = cursor.fetchall()



        self.w = ManagerManageStaff(staffDetail)
        self.w.show()
        self.hide()


    def manageProfile(self):

        global connection

        with connection.cursor() as cursor:
            # Read a single record
            #sql = "  select Username, Status, FirstName, Lastname from User ;"
            sql = "  select u.Firstname, u.Lastname, u.Username, s.Sitename, e.EmployeeID, e.Phone, " \
                  "  e.EmployeeAddress  from user u, employee e, site s where u.username = e.username "\
                  "  and e.username = s.ManagerUsername and u.username = '" + loggedInUser + "';"

            cursor.execute(sql)
            usrDetail = cursor.fetchall()

        self.w = EmployeeManageProfile(usrDetail)
        self.w.show()
        self.hide()
class ManagerVisitorFunctionality(QWidget): #screen 11
    def __init__(self):
        super (ManagerVisitorFunctionality, self).__init__()
        self.setWindowTitle("Manager-Visitor Functionality")

        left, top, width, height = 550, 50, 250, 400
        self.setGeometry(left, top, width, height)

        self.manageProfile_btn = QPushButton("Manage Profile")
        self.manageEvent_btn = QPushButton("Manage Event")
        self.viewStaff_btn = QPushButton("View Staff")
        self.viewSiteReport_btn = QPushButton("View Site Report")
        self.exploreSite_btn = QPushButton("Explore Site")
        self.exploreEvent_btn = QPushButton("Explore Event")
        self.takeTransit_btn = QPushButton("Take Transit")
        self.viewTransit_btn = QPushButton("View Transit History")
        self.viewVisit_btn = QPushButton("View Visit History")
        self.back_btn = QPushButton("Back")

        vbox = QVBoxLayout()
        vbox.addWidget(self.manageProfile_btn)
        vbox.addWidget(self.manageEvent_btn)
        vbox.addWidget(self.viewStaff_btn)
        vbox.addWidget(self.viewSiteReport_btn)
        vbox.addWidget(self.exploreSite_btn)
        vbox.addWidget(self.exploreEvent_btn)
        vbox.addWidget(self.takeTransit_btn)
        vbox.addWidget(self.viewTransit_btn)
        vbox.addWidget(self.viewVisit_btn)
        vbox.addWidget(self.back_btn)
        self.setLayout(vbox)

        self.viewStaff_btn.clicked.connect(self.managestaff)
        self.manageProfile_btn.clicked.connect(self.manageProfile)
        self.manageEvent_btn.clicked.connect(self.manageEvent)
        self.viewSiteReport_btn.clicked.connect(self.viewSiteReport)
        self.exploreSite_btn.clicked.connect(self.exploreSite)
        self.exploreEvent_btn.clicked.connect(self.exploreEvent)
        self.takeTransit_btn.clicked.connect(self.takeTransit)
        self.viewTransit_btn.clicked.connect(self.transitHistory)

        self.viewVisit_btn.clicked.connect(self.viewVisitHistory)
        self.back_btn.clicked.connect(self.startBack)

    def startBack(self):
        self.w = UserLogin()
        self.w.show()
        self.hide()

    def viewVisitHistory(self):
        global connection

        with connection.cursor() as cursor:
            sql = " select cast(v.VisitEventDate as char), v.Eventname, v.sitename, cast(sum(e.eventprice) as char) " \
                " from visitevent v, event e where v.eventname = e.eventname and v.visitorusername = '" + loggedInUser + "' " \
                " group by  v.VisitEventDate , v.Eventname, v.sitename " \
                " union " \
                " select cast(visitSiteDate as char), '', sitename, cast(0 as char)  from visitsite s where s.visitorusername =  '" + loggedInUser + "'; "
            #print(sql)
            cursor.execute(sql)
            viewVisitorHistory = cursor.fetchall()

        self.w = VisitorVisitHistory(viewVisitorHistory)
        self.w.show()
        self.hide()


    def takeTransit(self):
        global connection

        with connection.cursor() as cursor:
            sql = " select t.transitroute as 'Route', t.transittype as 'Transport Type', cast(t.price as char) as 'Price', count(c.sitename) as 'Connected Sites' " \
                  " from transit t left outer join connect c on t.transitType = c.transittype and " \
                  " t.transitroute = c.transitroute group by t.transitroute, t.transittype, t.price ; " \

            cursor.execute(sql)
            transitDetail = cursor.fetchall()

        self.w = UserTakeTransit(transitDetail)
        self.w.show()
        self.hide()

    def transitHistory(self):

        with connection.cursor() as cursor:
            # Read a single record
            #sql = "  select Username, Status, FirstName, Lastname from User ;"
            sql = " select cast(DATE_FORMAT(c.transitDate, '%Y-%m-%d') as char) as 'Date',  t.transitroute as 'Route', t.transittype as 'Transport Type', cast(t.price as char) as 'price' " \
                  " from transit t,taketransit c  where   t.transitType = c.transittype and  t.transitroute = c.transitroute and c.username = '" + loggedInUser + "' ; " \

            cursor.execute(sql)
            transitDetail = cursor.fetchall()

        self.w = UserTransitHistory(transitDetail)
        self.w.show()
        self.hide()

    def exploreEvent(self):
        global connection

        with connection.cursor() as cursor:
            sql = " select e.eventname, e.sitename, e.eventprice, count(visitorusername) as totalvisits,  " \
                " (capacity - count(visitorusername)) as ticketsleft, count(visitorusername) as myvisits  " \
                " from Event e left outer join visitevent v on e.eventname = v.eventname and e.startdate = v.startdate " \
                " group by e.eventname, e.sitename, e.eventprice , capacity ; "

            cursor.execute(sql)
            visitorExploreEvent = cursor.fetchall()

        self.w = VisitorExploreEvent(visitorExploreEvent)
        self.w.show()
        self.hide()

    def exploreSite(self):
        global connection

        with connection.cursor() as cursor:
            sql = " select e.sitename, count(e.eventname), count(visitorusername) as totalvisits, " \
                " (select count(visitorusername) from VisitSite s where s.sitename = e.sitename " \
                " and s.visitorusername = '" + loggedInUser + "') as myvisits " \
                " from Event e left outer join visitsite v on e.sitename = v.sitename  " \
                " group by  e.sitename ;"


            cursor.execute(sql)
            visitorExploreSite = cursor.fetchall()

        self.w = VisitorExploreSite(visitorExploreSite)
        self.w.show()
        self.hide()


    def viewVisitHistory(self):
        global connection

        with connection.cursor() as cursor:
            sql = " select cast(v.VisitEventDate as char), v.Eventname, v.sitename, cast(sum(e.eventprice) as char) " \
                " from visitevent v, event e where v.eventname = e.eventname and v.visitorusername = '" + loggedInUser + "' " \
                " group by  v.VisitEventDate , v.Eventname, v.sitename " \
                " union " \
                " select cast(visitSiteDate as char), '', sitename, cast(0 as char)  from visitsite s where s.visitorusername =  '" + loggedInUser + "'; "
            #print(sql)
            cursor.execute(sql)
            viewVisitorHistory = cursor.fetchall()

        self.w = VisitorVisitHistory(viewVisitorHistory)
        self.w.show()
        self.hide()

    def viewSiteReport(self):

        currentSite = 'orig' #getcurrentManagersite()

        global connection

        with connection.cursor() as cursor:
            sql =  "    select * from (select cast(startdate as char) as startdate, count(eventname) as eventcount " \
                    " from event where sitename = '" + currentSite + "' group by startdate) as table1 " \
                    " natural join  " \
                    " (select cast(startdate as char), count(staffusername) as staffcount  " \
                    " from assignto group by startdate) as table2 " \
                    " natural join  " \
                    " (select cast(startdate as char), count(visitorusername) as total_visits  " \
                    " from visitevent group by startdate) as table3 " \
                    " natural join  " \
                    " (select cast(startdate as char), sum(totalrevenue) as totalrevenue  " \
                    " from (select eventname, sitename, startdate, count(visitorusername) " \
                    " as totalvisits, (eventprice * count(visitorusername)) as totalrevenue from event natural join visitevent " \
                    "  where sitename = '" + currentSite + "' group by eventname, sitename, startdate) as table6 group by startdate)  " \
                    " as table4;"

            cursor.execute(sql)
            shiftreportDetail = cursor.fetchall()

        self.w = SiteReport(shiftreportDetail)
        self.w.show()
        self.hide()

    def manageEvent(self):
        global connection

        with connection.cursor() as cursor:
            sql =  "select e.eventname, datediff(e.enddate, e.startdate) as duration, " \
                    " count(staffusername) as staffcount, (select count(*) from visitevent v " \
                    " where v.eventname = e.eventname) as totalvisits, (select count(*) * e.eventprice from visitevent v " \
                    " where v.eventname = e.eventname) as totalrevenue   " \
                    " from event e left outer join visitevent v on e.eventname = v.eventname " \
                    " left outer join assignto a on e.eventname = a.eventname " \
                    " group by e.eventname, duration, totalvisits,  totalrevenue ;"

            cursor.execute(sql)
            eventDetail = cursor.fetchall()



        self.w = ManagerManageEvent(eventDetail)
        self.w.show()
        self.hide()



    def managestaff(self):
        global connection

        with connection.cursor() as cursor:
            # Read a single record
            #sql = "  select Username, Status, FirstName, Lastname from User ;"
            sql = "select s.username as 'Staff Name', count(a.staffusername) as '# Event Shifts' from staff s " \
                  " left outer join assignto a on s.username = a.staffusername "\
                  " group by s.username ;"

            cursor.execute(sql)
            staffDetail = cursor.fetchall()



        self.w = ManagerManageStaff(staffDetail)
        self.w.show()
        self.hide()

    def manageProfile(self):
        print("managing profile")
        global connection

        with connection.cursor() as cursor:
            # Read a single record
            #sql = "  select Username, Status, FirstName, Lastname from User ;"
            sql = "  select u.Firstname, u.Lastname, u.Username, s.Sitename, e.EmployeeID, e.Phone, " \
                  "  e.EmployeeAddress  from user u, employee e, site s where u.username = e.username "\
                  "  and e.username = s.ManagerUsername and u.username = '" + loggedInUser + "';"

            cursor.execute(sql)
            usrDetail = cursor.fetchall()

        self.w = EmployeeManageProfile(usrDetail)
        self.w.show()
        self.hide()
class VisitorFunctionality(QWidget): #screen 14
    def __init__(self):
        super (VisitorFunctionality, self).__init__()
        self.setWindowTitle("Visitor Functionality")

        left, top, width, height = 550, 50, 250, 400
        self.setGeometry(left, top, width, height)

        self.exploreEvent_btn = QPushButton("Explore Movie")
        self.exploreSite_btn = QPushButton("Explore Theater")
        self.viewVisitHist_btn = QPushButton("Visit History")
        self.viewTransit_btn = QPushButton("View History")
        self.back_btn = QPushButton("Back")

        vbox = QVBoxLayout()
        vbox.addWidget(self.exploreEvent_btn)
        vbox.addWidget(self.exploreSite_btn)
        vbox.addWidget(self.viewVisitHist_btn)
        vbox.addWidget(self.viewTransit_btn)
        vbox.addWidget(self.back_btn)
        self.setLayout(vbox)

        self.viewVisitHist_btn.clicked.connect(self.viewVisitHistory)
        self.exploreSite_btn.clicked.connect(self.exploreSite)
        self.exploreEvent_btn.clicked.connect(self.exploreEvent)
        self.viewTransit_btn.clicked.connect(self.transitHistory)
        self.back_btn.clicked.connect(self.startBack)

    def startBack(self):
        self.w = UserLogin()
        self.w.show()
        self.hide()


    def takeTransit(self):
        global connection

        with connection.cursor() as cursor:
            sql = " select t.transitroute as 'Route', t.transittype as 'Transport Type', cast(t.price as char) as 'Price', count(c.sitename) as 'Connected Sites' " \
                  " from transit t left outer join connect c on t.transitType = c.transittype and " \
                  " t.transitroute = c.transitroute group by t.transitroute, t.transittype, t.price ; " \

            cursor.execute(sql)
            transitDetail = cursor.fetchall()

        self.w = UserTakeTransit(transitDetail)
        self.w.show()
        self.hide()

    def transitHistory(self):

        with connection.cursor() as cursor:
            sql = " select cast(DATE_FORMAT(c.transitDate, '%Y-%m-%d') as char) as 'Date',  t.transitroute as 'Route', t.transittype as 'Transport Type', cast(t.price as char) as 'price' " \
                  " from transit t,taketransit c  where   t.transitType = c.transittype and  t.transitroute = c.transitroute and c.username = '" + loggedInUser + "' ; " \

            cursor.execute(sql)
            transitDetail = cursor.fetchall()

        self.w = UserTransitHistory(transitDetail)
        self.w.show()
        self.hide()

    def exploreEvent(self):
        global connection

        with connection.cursor() as cursor:
            sql = " select e.eventname, e.sitename, e.eventprice, count(visitorusername) as totalvisits,  " \
                " (capacity - count(visitorusername)) as ticketsleft, count(visitorusername) as myvisits  " \
                " from Event e left outer join visitevent v on e.eventname = v.eventname and e.startdate = v.startdate " \
                " group by e.eventname, e.sitename, e.eventprice , capacity ; "
            cursor.execute(sql)
            visitorExploreEvent = cursor.fetchall()

        self.w = VisitorExploreEvent(visitorExploreEvent)
        self.w.show()
        self.hide()

    def exploreSite(self):
        global connection

        with connection.cursor() as cursor:
            sql = " select e.sitename, count(e.eventname), count(visitorusername) as totalvisits, " \
                " (select count(visitorusername) from VisitSite s where s.sitename = e.sitename " \
                " and s.visitorusername = '" + loggedInUser + "') as myvisits " \
                " from Event e left outer join visitsite v on e.sitename = v.sitename  " \
                " group by  e.sitename ;"

            cursor.execute(sql)
            visitorExploreSite = cursor.fetchall()

        self.w = VisitorExploreSite(visitorExploreSite)
        self.w.show()
        self.hide()

    def viewVisitHistory(self):
        global connection

        with connection.cursor() as cursor:
            sql = " select cast(v.VisitEventDate as char), v.Eventname, v.sitename, cast(sum(e.eventprice) as char) " \
                " from visitevent v, event e where v.eventname = e.eventname and v.visitorusername = '" + loggedInUser + "' " \
                " group by  v.VisitEventDate , v.Eventname, v.sitename " \
                " union " \
                " select cast(visitSiteDate as char), '', sitename, cast(0 as char)  from visitsite s where s.visitorusername =  '" + loggedInUser + "'; "
            #print(sql)
            cursor.execute(sql)
            viewVisitorHistory = cursor.fetchall()

        self.w = VisitorVisitHistory(viewVisitorHistory)
        self.w.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = MainWindow()
    sys.exit(app.exec_())
