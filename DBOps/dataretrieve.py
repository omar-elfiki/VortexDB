from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox
from datetime import time
from PyQt5.QtCore import QTime
from DBOps.dbconnect import db_connect

def execute_query(query_text, params):
    conn = db_connect()
    query = QSqlQuery(conn)
    query.prepare(query_text)
    for param in params:
        query.addBindValue(param)
    if not query.exec_():
        print(query.lastError().text())
        return None
    if query.next():
        return query.value(0)
    return None

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

def getemployee(list, branch):
    if branch == "":
        return list.append("Select Branch to view employees")
    else:
        conn = db_connect()
        if conn is not None:
            id = getbranchid(branch)
            query = QSqlQuery(conn)
            select_query = (f"SELECT Name FROM Employee WHERE Branch_ID = '{id}'")
            query.prepare(select_query)
            if query.exec_():
                while query.next():
                    list.append(query.value(0))
                if list == []:
                    list.append("No Employees Found")                
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
        select_query = "SELECT Branch_ID FROM Cinema_Branch WHERE Branch_name = ?"
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
    if branch == "":
        return list.append("Select Branch to view screens")
    else:
        conn = db_connect()
        if conn is not None:
            id = getbranchid(branch)
            query = QSqlQuery(conn)
            select_query = (f"SELECT Screen_ID FROM Screen WHERE Branch_ID = '{id}'")
            query.prepare(select_query)
            if query.exec_():
                while query.next():
                    list.append(f"Screen {str(query.value(0))}")
        
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Failed to fetch data from database")
            msg.exec_()
        return list

def getScreenID(screen):
    screen_number = int(screen.split(' ')[1])
    return screen_number

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

def getshowingIDs(list, branch):
    conn = db_connect()
    if conn is not None:
        id = getbranchid(branch)
        query = QSqlQuery(conn)
        select_query = (f"SELECT Showing_ID FROM Movie_Showing WHERE Branch_ID = '{id}'")
        query.prepare(select_query)
        if query.exec_():
            while query.next():
                list.append(str(query.value(0)))
            if list == []:
                list.append("No Showings Found")
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to fetch data from database")
        msg.exec_()
    return list

def getshowinginfo(branch, showingID):
    if branch == "" or showingID == "":
        return "Select Showing to view details"
    else:
        conn = db_connect()
        if conn is not None:
            id = getbranchid(branch)
            date_query = "SELECT Date FROM Movie_Showing WHERE Branch_ID = ? and Showing_ID = ?"
            date = execute_query(date_query, [id, showingID])
            if date == None:
                return "No Showings found"
            date_string = date.toString('yyyy-MM-dd')

            # time_query = "SELECT Time FROM Movie_Showing WHERE Branch_ID = ? and Showing_ID = ?"
            # time_str = execute_query(time_query, [branch, showingID])
            # time = QTime.fromString(time_str, 'hh:mm:ss')

            movie_id_query = "SELECT Movie_ID FROM Movie_Showing WHERE Showing_ID = ?"
            movie_id = execute_query(movie_id_query, [showingID])

            title_query = "SELECT Title FROM Movie WHERE Movie_ID = ?"
            title = execute_query(title_query, [movie_id])

            if date and title:
                return f"Showing of {title} on {date_string}"
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Failed to fetch data from database")
                msg.exec_()


def getCustomerinfo(phone):
    conn = db_connect()
    if conn is not None:
        query = QSqlQuery(conn)
        select_query = "SELECT Customer_ID, Name FROM Customer WHERE Phone_number = ?"
        query.prepare(select_query)
        query.addBindValue(phone)
        if query.exec_():
            query.next()
            return f"{query.value(0)} , {query.value(1)}"
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to fetch data from database")
        msg.exec_()

def getcustID(phone):
    conn = db_connect()
    if conn is not None:
        query = QSqlQuery(conn)
        select_query = "SELECT Customer_ID FROM Customer WHERE Phone_number = ?"
        query.prepare(select_query)
        query.addBindValue(phone)
        if query.exec_():
            query.next()
            return query.value(0)
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to fetch data from database")
        msg.exec_()

def getshowingscreen(branch, screeningID):
    conn = db_connect()
    if conn is not None:
        id = getbranchid(branch)
        query = QSqlQuery(conn)
        select_query = (f"SELECT Screen_ID FROM Movie_Showing WHERE Branch_ID = '{id}' AND Showing_ID = '{screeningID}'")
        query.prepare(select_query)
        if query.exec_():
            query.next()
            return str(query.value(0))
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to fetch data from database")
        msg.exec_()

def getscreenvalidity(branch, screenID):
    conn = db_connect()
    if conn is not None:
        if screenID == "":
            return "Invalid, Screen ID cannot be empty"
        else:
            id = getbranchid(branch)
            sid = int(screenID)
            query = QSqlQuery(conn)
            select_query = (f"SELECT Screen_ID FROM Screen WHERE Branch_ID = '{id}'")
            query.prepare(select_query)
            if query.exec_():
                while query.next():
                    if query.value(0) == sid:
                        return "Invalid, Screen already exists"
            return "Valid"
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to fetch data from database")
        msg.exec_()

def getmovieid(title):
    conn = db_connect()
    if conn is not None:
        query = QSqlQuery(conn)
        select_query = "SELECT Movie_ID FROM Movie WHERE Title = ?"
        query.prepare(select_query)
        query.addBindValue(title)
        if query.exec_():
            query.next()
            return query.value(0)
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to fetch data from database")
        msg.exec_()