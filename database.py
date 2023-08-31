import mysql.connector


class dbcon:
    def __init__(self):
        pass
    def queryResult(self,f):
        con = mysql.connector.connect(user='root',passwd='',host='localhost',database='library')
        conn = con.cursor()
        conn.execute(f)
        result = conn.fetchall()
        con.close()
        return result
    def queryExecute(self,f):
        cont = mysql.connector.connect(user='root', passwd='', host='localhost', database='library')
        cons = cont.cursor()
        cons.execute(f)
        cont.commit()
        cont.close()