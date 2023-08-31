import re

import bookm
import mysql.connector
import database
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5 import Qt,QtCore
# import MySQLdb
from PyQt5.uic import loadUiType


ui,_=loadUiType('main.ui')
MainUI,_=loadUiType('login.ui')


######### login #################
class Main(QMainWindow,MainUI):
    def __init__(self,paren=None):
        super(Main,self).__init__(paren)
        QMainWindow.__init__(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Handel_Login)
        self.exit.clicked.connect(lambda: MainApp.exit())
    def Handel_Login(self):
        db = mysql.connector.connect(
            user='root',
            passwd='',
            host='localhost',
            database='library'
        )
        self.cursor = db.cursor()
        self.cursor.execute('SELECT * FROM users')
        result = self.cursor.fetchall()
        username = self.user.text()
        password = self.password.text()
        for row in result:
            if username == row[1] and password == row[3]:
                print('user match')
                self.window2 = MainApp()
                self.close()
                self.window2.show()

            else:
                self.label_2.setText('البيانات غير صحيحه')
                self.user.setText("")
                self.password.setText("")




 ######### main #################
class MainApp(QMainWindow , ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.but()
    def Handel_UI_Changes(self):
        self.tabWidget.tabBar().setVisible(False)

######### mathod button #################
    def but(self):
        self. showTableWegidBook()
        self.showTableWegidUser()
        ######### move from window to window #################
        self.mov1.clicked.connect(self.Open_Day_To_Day_Tab)
        self.mov3.clicked.connect(self.Open_CLients_Tab)
        self.mov4.clicked.connect(self.Open_Users_Tab)
            ##### Books #####
        self.tableWidget_5.clicked.connect(self.returnWegidBook)
        self.tableWidget_4.clicked.connect(self.returnWegidUser)
        self.uppdet.clicked.connect(self. uppdatBook)
        self.remov.clicked.connect(self.removBook)
        self.butSarchB.clicked.connect(self.search)
        self.search_User.clicked.connect(self.searchUser)
        self.AddUser.clicked.connect(self.addUsers)
        self.removUser.clicked.connect(self.RemovUser)
        self.pushButton_5.clicked.connect(self.Add_Books_info)
        self.pushButton_10.clicked.connect(self.unloading)
        self.uppdetUserButton.clicked.connect(self.uppdatUser)
        sarch = self.sarchBook.text()
######### mathod set to button #################
    def Open_Day_To_Day_Tab(self):
        self.tabWidget.setCurrentIndex(0)
    def Open_CLients_Tab(self):
        self.tabWidget.setCurrentIndex(1)
    def Open_Users_Tab(self):
        self.tabWidget.setCurrentIndex(2)

######### mathod Books  #################
     ### get premery key from table wiged  ###
    def returnWegidBook(self):
        row = self.tableWidget_5.currentRow()
        global index
        index= self.tableWidget_5.item(row, 0).text()
        item = self.tableWidget_5.item(row, 1).text()
        item2=self.tableWidget_5.item(row, 2).text()
        item3 = self.tableWidget_5.item(row, 3).text()
        item4 = self.tableWidget_5.item(row, 4).text()
        item5 = self.tableWidget_5.item(row, 5).text()
            ######### get text addet ################
        self.lineEdit_8.setText(item)
        self.lineEdit_10.setText(item2)
        self.lineEdit_11.setText(item3)
        self.lineEdit_9.setText(item4)
        self.lineEdit_6.setText(item5)
    def returnWegidUser(self):
        row = self.tableWidget_4.currentRow()
        global index1
        index1 = self.tableWidget_4.item(row, 0).text()
        item = self.tableWidget_4.item(row, 1).text()
        item2 = self.tableWidget_4.item(row, 2).text()
        item3 = self.tableWidget_4.item(row, 3).text()
        ######### get text addet ################
        self.T_name_4.setText(item)
        self.T_name_3.setText(item2)
        self.T_name_2.setText(item3)

     #### show table wiged  ####

    def showTableWegidBook(self):
        sql = "SELECT * FROM books"
        cont = database.dbcon()
        res = cont.queryResult(sql)
        self.tableWidget_5.setRowCount(len(res))
        self.tableWidget.setRowCount(len(res))
        column = 0
        for data in res:
            for col in range(0, 6):
                self.tableWidget_5.setItem(column, col, QTableWidgetItem(str(data[col])))
                self.tableWidget.setItem(column, col, QTableWidgetItem(str(data[col])))
            column += 1

    def showTableWegidUser(self):
        sql = "SELECT * FROM users"
        cont = database.dbcon()
        res = cont.queryResult(sql)
        self.tableWidget_4.setRowCount(len(res))
        column = 0
        for data in res:
            for col in range(0, 4):
                self.tableWidget_4.setItem(column, col, QTableWidgetItem(str(data[col])))
            column += 1
    #### remov item books ###
    def removBook(self):
        name=self.lineEdit_8.text()
        if name=="":
            QMessageBox.warning(self, 'تنبيه', "رجاء حدد عنصر للحذف")
        else:
            warning = QMessageBox.warning(self, 'حذف عنصر', "هل انت متاكد من حذف العنصر",QMessageBox.Yes | QMessageBox.No)
            if warning == QMessageBox.Yes:
                sql = "DELETE FROM books WHERE `id_Book`='"+index+"'"
                cont = database.dbcon()
                cont.queryExecute(sql)
                self.showTableWegidBook()
                self.lineEdit_6.setText("")
                self.lineEdit_9.setText("")
                self.lineEdit_11.setText("")
                self.lineEdit_10.setText("")
                self.lineEdit_8.setText("")
            else:
                pass

    #### uppdat item books ##
    def uppdatBook(self):
       item1=self.lineEdit_8.text()
       item2=self.lineEdit_10.text()
       item3=self.lineEdit_11.text()
       item4=self.lineEdit_9.text()
       item5=self.lineEdit_6.text()

       if (item1 and item2 and item3 and item4 and item5) == "":
           QMessageBox.warning(self, 'تنبيه', "رجاء دخل قيمه ")
       else:
           print(index)
           warning = QMessageBox.warning(self, 'تحديث عنصر', "هل انت متاكد من تحديث العنصر",QMessageBox.Yes | QMessageBox.No)
           if warning == QMessageBox.Yes:
                sql = "UPDATE `books` SET `Name_Book`='"+item1+"',`Author_Name`='"+item2+"',`Release_Date`='"+item3+"',`Purchasing_price`='"+item4+"',`selling_price`='"+item5+"' WHERE `id_Book`='"+index+"'"
                cont = database.dbcon()
                cont.queryExecute(sql)
                self.lineEdit_6.setText("")
                self.lineEdit_9.setText("")
                self.lineEdit_11.setText("")
                self.lineEdit_10.setText("")
                self.lineEdit_8.setText("")
                self.showTableWegidBook()
           else:
                pass

    ### search item books ##
    def search(self):
         sarch=self.sarchBook.text()
         ser = sarch.strip()
         if sarch != "":
             sql = " SELECT * FROM books WHERE Name_Book LIKE '%"+ser+"%'"
             cont = database.dbcon()
             res = cont.queryResult(sql)
             print(res)
             self.tableWidget.setRowCount(len(res))
             column = 0
             for data in res:
                 for col in range(0, 6):
                     self.tableWidget.setItem(column, col, QTableWidgetItem(str(data[col])))
                 column += 1
         else:
             self.showTableWegidBook()
    def searchUser(self):
         sarch=self.sarchUser.text()
         if sarch != "":
             ser=sarch.strip()
             sql = " SELECT * FROM users WHERE user_name LIKE '%"+ser+"%'"
             cont = database.dbcon()
             res = cont.queryResult(sql)
             self.tableWidget_4.setRowCount(len(res))
             column = 0
             for data in res:
                 for col in range(0, 4):
                     self.tableWidget_4.setItem(column, col, QTableWidgetItem(str(data[col])))
                 column += 1
         else:
             self.showTableWegidUser()
    ### defult ##

    def addUsers(self):
        User=self.T_name_4.text()
        email =self.T_name_3.text()
        password = self.T_name_2.text()
        if (User and email and password) == "":
            QMessageBox.warning(self, 'تنبيه', "رجاء دخل قيمه ")
        else:
            Em = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if re.fullmatch(Em, email):
                sql = "INSERT INTO `users`(`user_name`, `user_email`, `user_password`) VALUES ('" + User + "','" + email + "','" + password + "')"
                cont = database.dbcon()
                cont.queryExecute(sql)
                self.T_name_2.setText("")
                self.T_name_4.setText("")
                self.T_name_3.setText("")
                self.statusBar().showMessage('تم اضافه المستخدم بنجاح')
                self.showTableWegidUser()
            else:
                QMessageBox.warning(self, 'تنبيه', "رجاء دخل الايميل بشكل صحيح ")

    def RemovUser(self):
        User = self.T_name_4.text()
        email = self.T_name_3.text()
        password = self.T_name_2.text()
        if (User and email and password) == "":
            QMessageBox.warning(self, 'تنبيه', "الرجاء اختيار عنصر للحذف")
        else:
            warning = QMessageBox.warning(self, 'حذف عنصر', "هل انت متاكد من حذف العنصر", QMessageBox.Yes | QMessageBox.No)
            if warning == QMessageBox.Yes:
                sql = "DELETE FROM users WHERE idusers ='" + index1 + "'"
                cont = database.dbcon()
                cont.queryExecute(sql)
                self.T_name_2.setText("")
                self.T_name_4.setText("")
                self.T_name_3.setText("")
                self.statusBar().showMessage('تم حذف المستخدم بنجاح')
                self.showTableWegidUser()
            else:
                pass

    def uppdatUser(self):
        User = self.T_name_4.text()
        email = self.T_name_3.text()
        password = self.T_name_2.text()
        if (User and email and password) == "":
            QMessageBox.warning(self, 'تنبيه', "رجاء دخل قيمه ")
        else:
            # Em = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            # if re.fullmatch(Em, email):
                sql = "UPDATE `users` SET `user_name`='"+User+"',`user_email`='"+email+"',`user_password`='"+password+"' WHERE `idusers`='"+index1+"'"
                cont = database.dbcon()
                cont.queryExecute(sql)
                self.T_name_2.setText("")
                self.T_name_4.setText("")
                self.T_name_3.setText("")
                self.showTableWegidUser()
            # else:
            #     QMessageBox.warning(self, 'تنبيه', "رجاء دخل الايميل بشكل صحيح ")

    def Add_Books_info(self):
        Book_Name = self.lineEdit.text()
        Author_Name = self.lineEdit_2.text()
        Release_Date = self.dateEdit.date().toPyDate().strftime('%Y-%m-%d').replace('-', '/').replace('/', '-')
        Purchasing_price = self.lineEdit_4.text()
        selling_price = self.lineEdit_5.text()

        if (Book_Name and Author_Name and Release_Date and Purchasing_price and selling_price) == "":
            QMessageBox.warning(self, 'تنبيه', " رجاء ادخل القيم ")
        else:
            try:
                float(Purchasing_price)
                float(selling_price)
            except:
                QMessageBox.warning(self, 'تنبيه', "رجاء ادخل القيم بشكل صحيح", QMessageBox.Ok)

            else:
                sql = "INSERT INTO `books`(`Name_Book`, `Author_Name`, `Release_Date`, `Purchasing_price`, `selling_price`) VALUES ('" + Book_Name + "','" + Author_Name + "','" + Release_Date + "','" + Purchasing_price + "','" + selling_price + "')"
                cont = database.dbcon()
                cont.queryExecute(sql)
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_4.setText("")
                self.lineEdit_5.setText("")
                self.statusBar().showMessage('تم اضافه الكتاب بنجاح', 2000)
                self.showTableWegidBook()


    def unloading(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.statusBar().showMessage('تم تفريغ الحقول بنجاح', 5000)

######### main stert #################
def main():
    app=QApplication(sys.argv)
    window= Main()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()