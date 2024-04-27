import PyQt5.QtSql as QtSql
from PyQt5.QtWidgets import QMessageBox

def sum_all_ticks(date, conn):
    model = QtSql.QSqlQueryModel()
    model.setQuery(f"""
        SELECT COUNT(*) AS Total_Tickets_Sold
        FROM Ticket T
        INNER JOIN Movie_Showing MS ON T.Showing_ID = MS.Showing_ID AND T.Screen_ID = MS.Screen_ID AND T.Branch_ID = MS.Branch_ID
        WHERE MS.Date = '{date}';
    """, conn)
    return model

def ticks_sold_by_branch(date, conn):
    model = QtSql.QSqlQueryModel()
    model.setQuery(f"""
        SELECT 
            CB.Branch_name, 
            COUNT(*) AS Tickets_Sold
        FROM 
            Ticket T
        INNER JOIN 
            Movie_Showing MS ON T.Showing_ID = MS.Showing_ID AND T.Screen_ID = MS.Screen_ID AND T.Branch_ID = MS.Branch_ID
        INNER JOIN
            Cinema_Branch CB ON T.Branch_ID = CB.Branch_ID
        WHERE 
            MS.Date = '{date}'
        GROUP BY 
            CB.Branch_name;
    """, conn)
    return model

def average_tickets_sold(conn):
    model = QtSql.QSqlQueryModel()
    model.setQuery("""
        SELECT AVG(DailySales) AS "Average Daily Sales"
        FROM (
            SELECT COUNT(Ticket_ID) as DailySales
            FROM Ticket
            JOIN Movie_Showing ON Ticket.Showing_ID = Movie_Showing.Showing_ID
            GROUP BY Movie_Showing.Date
        ) as DailyTicketSales""", conn)
    return model