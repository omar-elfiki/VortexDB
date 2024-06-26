from DBOps.dbconnect import db_connect
from DBOps.dataretrieve import getcustID, getbranchid
from PyQt5.QtSql import QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QMessageBox

conn = db_connect()

def get_screen_schedule(conn, screenID, branchID):
    query = QSqlQuery(conn)
    query.prepare("""
        SELECT 
            S.Screen_ID AS Screen, 
            S.Branch_ID AS Branch,
            MS.Showing_ID AS Showing, 
            M.Title, 
            MS.Date, 
            MS.Time
        FROM 
            Screen S
        INNER JOIN 
            Movie_Showing MS ON S.Screen_ID = MS.Screen_ID AND S.Branch_ID = MS.Branch_ID
        INNER JOIN 
            Movie M ON MS.Movie_ID = M.Movie_ID
        WHERE 
            S.Screen_ID = :screenID AND S.Branch_ID = :branchID
        ORDER BY 
            MS.Date
    """)
    query.bindValue(":screenID", screenID)
    query.bindValue(":branchID", branchID)
    query.exec_()
    model = QSqlQueryModel()
    model.setQuery(query)
    return model


def get_customer_tickets(conn, parameter):
    model = QSqlQueryModel()
    query = QSqlQuery(conn)
    if parameter == '':
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Invalid parameter")
        msg.exec_()
        return None

    if len(parameter) == 11:
        query.prepare(f"""
        SELECT 
            C.Customer_ID, 
            T.Ticket_ID, 
            T.Showing_ID, 
            T.Screen_ID, 
            T.Branch_ID, 
            M.Title AS Movie_Name,
            MS.Date, 
            MS.Time
        FROM 
            Customer C
        INNER JOIN 
            Ticket T ON C.Customer_ID = T.Customer_ID
        INNER JOIN 
            Movie_Showing MS ON T.Showing_ID = MS.Showing_ID AND T.Screen_ID = MS.Screen_ID AND T.Branch_ID = MS.Branch_ID
        INNER JOIN
            Movie M ON MS.Movie_ID = M.Movie_ID
        WHERE 
            C.Phone_number = :parameter""")
        query.bindValue(":parameter", parameter)
        query.exec_()
        model.setQuery(query)
        return model
            
    elif "@" in parameter:
        query.prepare(f"""
        SELECT 
            C.Customer_ID, 
            T.Ticket_ID, 
            T.Showing_ID, 
            T.Screen_ID, 
            T.Branch_ID, 
            M.Title AS Movie_Name,
            MS.Date, 
            MS.Time
        FROM 
            Customer C
        INNER JOIN 
            Ticket T ON C.Customer_ID = T.Customer_ID
        INNER JOIN 
            Movie_Showing MS ON T.Showing_ID = MS.Showing_ID AND T.Screen_ID = MS.Screen_ID AND T.Branch_ID = MS.Branch_ID
        INNER JOIN
            Movie M ON MS.Movie_ID = M.Movie_ID
        WHERE 
            C.Email = :parameter""")
        query.bindValue(":parameter", parameter)
        query.exec_()
        model.setQuery(query)
        return model
            
    elif len(parameter) < 11:
        query.prepare(f"""
        SELECT 
            C.Customer_ID, 
            T.Ticket_ID, 
            T.Showing_ID, 
            T.Screen_ID, 
            T.Branch_ID, 
            M.Title AS Movie_Name,
            MS.Date, 
            MS.Time
        FROM 
            Customer C
        INNER JOIN 
            Ticket T ON C.Customer_ID = T.Customer_ID
        INNER JOIN 
            Movie_Showing MS ON T.Showing_ID = MS.Showing_ID AND T.Screen_ID = MS.Screen_ID AND T.Branch_ID = MS.Branch_ID
        INNER JOIN
            Movie M ON MS.Movie_ID = M.Movie_ID
        WHERE 
            C.Customer_ID = :parameter""")
        query.bindValue(":parameter", int(parameter))
        query.exec_()
        model.setQuery(query)
        return model
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Invalid parameter")
        msg.exec_()
        return None


    

def get_upcoming_movie_screenings(conn, title):
    model = QSqlQueryModel()
    query = QSqlQuery(conn)
    query.prepare(f"""SELECT  
                        M.Title AS Title,
                        MS.Showing_ID AS Showing, 
                        MS.Screen_ID AS Screen, 
                        B.Branch_name as Branch,
                        MS.Date, 
                        MS.Time
                    FROM 
                        Movie M
                    INNER JOIN 
                        Movie_Showing MS ON M.Movie_ID = MS.Movie_ID
                    INNER JOIN
                        Cinema_branch B ON MS.Branch_ID = B.Branch_ID
                    WHERE 
                        M.Title = :title""")
    query.bindValue(":title", title)
    query.exec_()
    model.setQuery(query)
    return model

def find_empty_showings(conn):
    model = QSqlQueryModel()
    model.setQuery("""
        SELECT 
            MS.Showing_ID AS Showing, 
            MS.Screen_ID AS Screen, 
			B.Branch_name AS Branch,
			M.Title AS Title,
            MS.Date, 
            MS.Time
        FROM 
            Movie_Showing MS
		INNER JOIN
			Cinema_Branch B ON MS.Branch_ID = B.Branch_ID
		INNER JOIN
			Movie M ON MS.Movie_ID = M.Movie_ID
        WHERE 
            NOT EXISTS (
                SELECT 1
                FROM Ticket T
                WHERE 
                    T.Showing_ID = MS.Showing_ID AND 
                    T.Screen_ID = MS.Screen_ID AND 
                    T.Branch_ID = MS.Branch_ID);
                   """, conn)
    return model

def sell_ticket(phone, branch_input, screening_input, seat_input, price_input):
    conn = db_connect()
    id = getcustID(phone.text())
    branchid = getbranchid(branch_input.currentText())
    screening = int(screening_input.currentText())
    seat = int(seat_input.text())
    price = float(price_input.text())
    if conn is not None:
        query3 = QSqlQuery(conn)
        query4 = QSqlQuery(conn)
        query3.prepare(f"SELECT Screen_ID FROM Movie_Showing WHERE Showing_ID = :screening AND Branch_ID = :id")
        query3.bindValue(":screening", screening)
        query3.bindValue(":id", branchid)
        query3.exec_()
        if query3.next():
            screenid = query3.value(0)
        query4.prepare(f"INSERT INTO Ticket (Customer_ID, Branch_ID, Showing_ID, Screen_ID, Seat_number, Price) VALUES (?, ?, ?, ?, ?, ?)")
        query4.addBindValue(id)
        query4.addBindValue(branchid)
        query4.addBindValue(screening)
        query4.addBindValue(screenid)
        query4.addBindValue(seat)
        query4.addBindValue(price)
        if query4.exec_():
            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("Ticket Sold")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText(f"Failed to sell ticket, {query4.lastError().text()}")
            msg.exec_()

    
    