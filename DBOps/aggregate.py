import DBOps.dbconnect as dbconnect

conn = dbconnect.db_connect()

def sum_all_ticks(date):
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT COUNT(*) AS Total_Tickets_Sold
        FROM Ticket T
        INNER JOIN Movie_Showing MS ON T.Showing_ID = MS.Showing_ID AND T.Screen_ID = MS.Screen_ID AND T.Branch_ID = MS.Branch_ID
        WHERE MS.Date = '{date}';
    """)
    for row in cursor:
        print(row)
        return row

def ticks_sold_by_branch(date):
    cursor = conn.cursor()
    cursor.execute(f"""
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
    """)
    for row in cursor:
        print(row)
        return row

def average_tickets_permovie(movieid):
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT 
            MS.Showing_ID, 
            MS.Screen_ID, 
            MS.Branch_ID, 
            AVG(CAST(COUNT(*) AS FLOAT)) OVER () AS Average_Tickets_Sold_Per_Showing
        FROM 
            Ticket T
        INNER JOIN 
            Movie_Showing MS ON T.Showing_ID = MS.Showing_ID AND T.Screen_ID = MS.Screen_ID AND T.Branch_ID = MS.Branch_ID
        WHERE 
            MS.Movie_ID = '{movieid}'
        GROUP BY 
            MS.Showing_ID, 
            MS.Screen_ID, 
            MS.Branch_ID;
    """)
    for row in cursor:
        print(row)
        return row