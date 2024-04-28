from PyQt5.QtWidgets import QPushButton, QGridLayout, QWidget, QTableView, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlQueryModel
import GUI.mainGUI as GUI
from DBOps.dbconnect import db_connect, db_disconnect

def viewscreens(main_window):
    conn = db_connect()
    if conn is not None:
        GUI.clear(main_window)
        model = QSqlQueryModel()
        model.setQuery(""" SELECT Screen.Screen_ID as SID, Screen.Branch_ID as BID, Cinema_Branch.Branch_name AS Branch, Screen.Seat_Type AS Type, Screen.Number_of_seats AS #, Screen.Date_of_inspection AS 'Date of Inspection'
                            FROM Screen 
                            INNER JOIN Cinema_Branch ON Screen.Branch_ID = Cinema_Branch.Branch_ID
                            ORDER BY Screen.Branch_ID ASC;""", conn)
        GUI.displaytable(main_window, model)
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to connect to database")
        msg.exec_()

def viewshowings(main_window):
    conn = db_connect()
    if conn is not None:
        GUI.clear(main_window)
        model = QSqlQueryModel()
        model.setQuery(""" SELECT Movie_Showing.Showing_ID AS Showing, Movie_Showing.Screen_ID AS Screen, Cinema_Branch.Branch_name AS Branch, Movie.Title AS 'Movie Title', Movie_Showing.Date, Movie_Showing.Time
                            FROM Movie_Showing 
                            INNER JOIN Cinema_Branch ON Movie_Showing.Branch_ID = Cinema_Branch.Branch_ID
                            INNER JOIN Movie ON Movie_Showing.Movie_ID = Movie.Movie_ID;""", conn)
        GUI.displaytable(main_window, model)
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to connect to database")
        msg.exec_()

def viewtickets(main_window):
    conn = db_connect()
    if conn is not None:
        GUI.clear(main_window)
        model = QSqlQueryModel()
        model.setQuery("""SELECT Ticket.Ticket_ID AS TID, Customer.Name, Ticket.Showing_ID as Showing, Ticket.Screen_ID as Screen, Cinema_Branch.Branch_name AS Branch, Ticket.Seat_number AS Seat, Ticket.Price
                            FROM Ticket
                            INNER JOIN Customer ON Ticket.Customer_ID = Customer.Customer_ID
                            INNER JOIN Cinema_Branch ON Ticket.Branch_ID = Cinema_Branch.Branch_ID;""", conn)
        GUI.displaytable(main_window, model)
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to connect to database")
        msg.exec_()

def viewshifts(main_window):
    conn = db_connect()
    if conn is not None:
        GUI.clear(main_window)
        model = QSqlQueryModel()
        model.setQuery("""SELECT Showing_Management.Employee_ID as EID, Employee.Name as Name, Showing_Management.Showing_ID as Showing, Movie_Showing.Date, Showing_Management.Screen_ID AS Screen, Cinema_Branch.Branch_name AS Branch
                            FROM Showing_Management
                            INNER JOIN Employee ON Showing_Management.Employee_ID = Employee.Employee_ID
                            INNER JOIN Movie_Showing ON Showing_Management.Showing_ID = Movie_Showing.Showing_ID
                            INNER JOIN Cinema_Branch ON Showing_Management.Branch_ID = Cinema_Branch.Branch_ID;""", conn)
        GUI.displaytable(main_window, model)
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to connect to database")
        msg.exec_()  

