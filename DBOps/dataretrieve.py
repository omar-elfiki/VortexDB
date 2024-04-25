from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox
from DBOps.dbconnect import db_connect

def getbranches(list):
    conn = db_connect()
    if conn is not None:
        query = QSqlQuery(conn)
        select_query = "SELECT Branch_name FROM Cinema_Branch"
        query.prepare(select_query)
        if query.exec_():
            while query.next():
                list.append(query.value(0))
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Failed to fetch data from database")
            msg.exec_()
    return list

def getemployee(list):
    conn = db_connect()
    if conn is not None:
        query = QSqlQuery(conn)
        select_query = "SELECT Name FROM Employee"
        query.prepare(select_query)
        if query.exec_():
            while query.next():
                list.append(query.value(0))
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Failed to fetch data from database")
            msg.exec_()
    return list

def getbranchid(selected_option):
    conn = db_connect()
    if conn is not None:
        query = QSqlQuery(conn)
        select_query = "SELECT Branch_id FROM Cinema_Branch WHERE Branch_name = ?"
        query.prepare(select_query)
        query.addBindValue(selected_option)
        if query.exec_():
            query.next()
            return query.value(0)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Failed to fetch data from database")
            msg.exec_()

def getEmployeeid(selected_option):
    conn = db_connect()
    if conn is not None:
        query = QSqlQuery(conn)
        select_query = "SELECT Employee_ID FROM Employee WHERE Name = ?"
        query.prepare(select_query)
        query.addBindValue(selected_option)
        if query.exec_():
            query.next()
            return query.value(0)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Failed to fetch data from database")
            msg.exec_()

def getscreens(list,branch):
    import DBOps.dbconnect as dbconnect
    if branch == "Select Branch":
        return list
    else:
        id = getbranchid(branch)
        cursor = dbconnect.conn.cursor()
        cursor.execute(f"SELECT Screen_ID FROM Screen WHERE Branch_ID = '{id}'")
        for screen in cursor.fetchall():
            list.append(screen[0])
        return list

def getMovies(list):
    conn = db_connect()
    if conn is not None:
        query = QSqlQuery(conn)
        selectquery = ("SELECT Title FROM Movie")
        query.prepare(selectquery)
        if query.exec_():
            while query.next():
                list.append(query.value(0))
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Failed to fetch data from database")
            msg.exec_()
    return list