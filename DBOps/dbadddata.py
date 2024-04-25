import DBOps.dbconnect as dbconnect
import PyQt5.QtSql as QtSql
from PyQt5.QtWidgets import QMessageBox

def add_new_customer(name, email, phone_number, birth_date):
    conn = dbconnect.db_connect()
    if conn is not None:
        query = QtSql.QSqlQuery(conn)
        insert_query = "INSERT INTO Customer (Name, Email, Phone_number, Birth_date) VALUES (?, ?, ?, ?)"
        query.prepare(insert_query)
        query.addBindValue(name)
        query.addBindValue(email)
        query.addBindValue(phone_number)
        query.addBindValue(birth_date)
        if query.exec_():
            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("New customer added")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Failed to insert data into SQL table: " + query.lastError().text())
            msg.exec_()
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to connect to database")
        msg.exec_()

def add_new_screen(branch_id, seat_type, numberofseats, dateofinspection):
    conn = dbconnect.db_connect()
    if conn is not None:
        query = QtSql.QSqlQuery(conn)
        insert_query = "INSERT INTO Screen (Branch_ID, Seat_Type, Number_of_seats, Date_of_inspection) VALUES (?, ?, ?, ?)"
        query.prepare(insert_query)
        query.addBindValue(branch_id)
        query.addBindValue(seat_type)
        query.addBindValue(numberofseats)
        query.addBindValue(dateofinspection)
        if query.exec_():
            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("New Screen added")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Failed to insert data into SQL table: " + query.lastError().text())
            msg.exec_()

def add_new_movie(title, language, subtitle, start_date, end_date, age_rating):
    conn = dbconnect.db_connect()
    if conn is not None:
        query = QtSql.QSqlQuery(conn)
        insert_query = "INSERT INTO Movie (Title, Language, Subtitles, Start_Date, End_Date, Age_rating) VALUES (?, ?, ?, ?, ?, ?)"
        query.prepare(insert_query)
        query.addBindValue(title)
        query.addBindValue(language)
        query.addBindValue(subtitle)
        query.addBindValue(start_date)
        query.addBindValue(end_date)
        query.addBindValue(age_rating)
        if query.exec_():
            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("New Movie added")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Failed to insert data into SQL table: " + query.lastError().text())
            msg.exec_()

def add_new_ticket(customer_id, showing_id, screen_id, branch_id, seat_number, price):
    conn = dbconnect.db_connect()
    if conn is not None:
        query = QtSql.QSqlQuery(conn)
        insert_query = "INSERT INTO Ticket (Customer_ID, Showing_ID, Screen_ID, Branch_ID, Seat_number, Price) VALUES (?, ?, ?, ?, ?, ?)"
        query.prepare(insert_query)
        query.addBindValue(customer_id)
        query.addBindValue(showing_id)
        query.addBindValue(screen_id)
        query.addBindValue(branch_id)
        query.addBindValue(seat_number)
        query.addBindValue(price)
        if query.exec_():
            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("New Ticket added")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Failed to insert data into SQL table: " + query.lastError().text())
            msg.exec_()

def add_new_showing(screen_id, branch_id, movie_id, date, time):
    conn = dbconnect.db_connect()
    if conn is not None:
        query = QtSql.QSqlQuery(conn)
        insert_query = "INSERT INTO Showing (Screen_ID, Branch_ID, Movie_ID, Date, Time) VALUES (?, ?, ?, ?, ?)"
        query.prepare(insert_query)
        query.addBindValue(screen_id)
        query.addBindValue(branch_id)
        query.addBindValue(movie_id)
        query.addBindValue(date)
        query.addBindValue(time)
        if query.exec_():
            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("New Showing added")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Failed to insert data into SQL table: " + query.lastError().text())
            msg.exec_()

def add_new_employee(Name, Email, Phone_number, Branch_ID):
    conn = dbconnect.db_connect()
    if conn is not None:
        query = QtSql.QSqlQuery(conn)
        insert_query = "INSERT INTO Employee (Name, Email, Phone_number, Branch_ID) VALUES (?, ?, ?, ?)"
        query.prepare(insert_query)
        query.addBindValue(Name)
        query.addBindValue(Email)
        query.addBindValue(Phone_number)
        query.addBindValue(Branch_ID)
        if query.exec_():
            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("New Employee added")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Failed to insert data into SQL table: " + query.lastError().text())
            msg.exec_()

def assign_management(Employee_ID, Showing_ID, Screen_ID, Branch_ID):
    conn = dbconnect.db_connect()
    if conn is not None:
        query = QtSql.QSqlQuery(conn)
        insert_query = "INSERT INTO Showing_Management (Employee_ID, Showing_ID, Screen_ID, Branch_ID) VALUES (?, ?, ?, ?)"
        query.prepare(insert_query)
        query.addBindValue(Employee_ID)
        query.addBindValue(Showing_ID)
        query.addBindValue(Screen_ID)
        query.addBindValue(Branch_ID)
        if query.exec_():
            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("New Showing Management added")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Failed to insert data into SQL table: " + query.lastError().text())
            msg.exec_()
