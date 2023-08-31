from PyQt5.QtWidgets import QTableWidgetItem
import database

def returnCuWegid(self):
    row = self.tableWidget_5.currentRow()
    item = self.tableWidget_5.item(row, 0).text()
    return item

    ######### show tamble wiged  #################

def showTableWegid(self):
    sql = "SELECT * FROM books"
    cont = database.dbcon()
    res = cont.queryResult(sql)
    self.tableWidget_5.setRowCount(len(res))
    column = 0
    for data in res:
        for col in range(0, 6):
            self.tableWidget_5.setItem(column, col, QTableWidgetItem(str(data[col])))
        column += 1