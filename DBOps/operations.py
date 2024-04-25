import DBOps.dbconnect as dbconnect

conn = dbconnect.db_connect()

def get_screen_schedule(screenID = "", branchID = "", date = ""):
    cursor = conn.cursor()
    cursor.execute(f"EXEC GetMovieShowings @Screen_ID = '{screenID}', @Branch_ID = '{branchID}', @Date = '{date}';")
    for row in cursor:
        print(row)


def get_customer_tickets(parameter):
    cursor = conn.cursor()
    if parameter[2] == "2" or parameter[2] == "1" or parameter[2] == "0" or parameter[2] == "5":
        cursor.execute(f"EXEC GetCustomerTickets @Phone = '{parameter}';")
    elif "@" in parameter:
        cursor.execute(f"EXEC GetCustomerTickets @Email = '{parameter}';")
    else:
        cursor.execute(f"EXEC GetCustomerTickets @Customer_ID = '{parameter}';")

    for row in cursor:
        print(row)
        return row

def get_upcoming_movie_screenings(title = ""):
    cursor = conn.cursor()
    cursor.execute(f"EXEC GetUpcomingMovieShowings @Movie_Name = '{title}';")
    for row in cursor:
        print(row)
        return row

def find_empty_showings():
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            MS.Showing_ID, 
            MS.Screen_ID, 
            MS.Branch_ID, 
            MS.Movie_ID, 
            MS.Date, 
            MS.Time
        FROM 
            Movie_Showing MS
        WHERE 
            NOT EXISTS (
                SELECT 1
                FROM Ticket T
                WHERE 
                    T.Showing_ID = MS.Showing_ID AND 
                    T.Screen_ID = MS.Screen_ID AND 
                    T.Branch_ID = MS.Branch_ID
            );
                   """)
    for row in cursor:
        print(row)
        return row