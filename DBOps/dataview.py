import GUI.viewpage as viewpage
import DBOps.dbconnect as dbconnect

def view_branches():
    cursor = dbconnect.conn.cursor()
    cursor.execute("SELECT * FROM Cinema_Branch")
    columns = [column[0] for column in cursor.description]
    viewpage.view_treeview.delete(*viewpage.view_treeview.get_children())
    viewpage.view_treeview["columns"] = columns
    for col in columns:
        viewpage.view_treeview.heading(col, text=col)
        viewpage.view_treeview.column(col, width=200)

    viewpage.view_treeview['show'] = 'headings'

    rows = cursor.fetchall()
    for row in rows:
        row = tuple(str(x) for x in row)
        viewpage.view_treeview.insert("", "end", values=row)
    viewpage.close_button.pack()
    viewpage.view_treeview.pack(pady=200)
    viewpage.close_button.config(command=viewpage.close_table)

def view_customers():
    cursor = dbconnect.conn.cursor()
    cursor.execute("SELECT * FROM Customer")
    columns = [column[0] for column in cursor.description]
    viewpage.view_treeview.delete(*viewpage.view_treeview.get_children())
    viewpage.view_treeview["columns"] = columns
    for col in columns:
        viewpage.view_treeview.heading(col, text=col)
        viewpage.view_treeview.column(col, width=200)

    viewpage.view_treeview['show'] = 'headings'

    rows = cursor.fetchall()
    for row in rows:
        row = tuple(str(x) for x in row)
        viewpage.view_treeview.insert("", "end", values=row)
    viewpage.close_button.pack()
    viewpage.view_treeview.pack(pady=200)
    viewpage.close_button.config(command=viewpage.close_table)

def view_employees():
    cursor = dbconnect.conn.cursor()
    cursor.execute("SELECT * FROM Employee")
    columns = [column[0] for column in cursor.description]
    viewpage.view_treeview.delete(*viewpage.view_treeview.get_children())
    viewpage.view_treeview["columns"] = columns
    for col in columns:
        viewpage.view_treeview.heading(col, text=col)
        viewpage.view_treeview.column(col, width=200)

    viewpage.view_treeview['show'] = 'headings'

    rows = cursor.fetchall()
    for row in rows:
        row = tuple(str(x) for x in row)
        viewpage.view_treeview.insert("", "end", values=row)
    viewpage.close_button.pack()
    viewpage.view_treeview.pack(pady=200)
    viewpage.close_button.config(command=viewpage.close_table)

def view_screenings():
    cursor = dbconnect.conn.cursor()
    cursor.execute("SELECT * FROM Movie_Showing")
    columns = [column[0] for column in cursor.description]
    viewpage.view_treeview.delete(*viewpage.view_treeview.get_children())
    viewpage.view_treeview["columns"] = columns
    for col in columns:
        viewpage.view_treeview.heading(col, text=col)
        viewpage.view_treeview.column(col, width=200)

    viewpage.view_treeview['show'] = 'headings'

    rows = cursor.fetchall()
    for row in rows:
        row = tuple(str(x) for x in row)
        viewpage.view_treeview.insert("", "end", values=row)
    viewpage.close_button.pack()
    viewpage.view_treeview.pack(pady=200)
    viewpage.close_button.config(command=viewpage.close_table)

def view_screens():
    cursor = dbconnect.conn.cursor()
    cursor.execute("SELECT * FROM Screen")
    columns = [column[0] for column in cursor.description]
    viewpage.view_treeview.delete(*viewpage.view_treeview.get_children())
    viewpage.view_treeview["columns"] = columns
    for col in columns:
        viewpage.view_treeview.heading(col, text=col)
        viewpage.view_treeview.column(col, width=200)

    viewpage.view_treeview['show'] = 'headings'

    rows = cursor.fetchall()
    for row in rows:
        row = tuple(str(x) for x in row)
        viewpage.view_treeview.insert("", "end", values=row)
    viewpage.close_button.pack()
    viewpage.view_treeview.pack(pady=200)
    viewpage.close_button.config(command=viewpage.close_table)

def view_movies():
    cursor = dbconnect.conn.cursor()
    cursor.execute("SELECT * FROM Movie")
    columns = [column[0] for column in cursor.description]
    viewpage.view_treeview.delete(*viewpage.view_treeview.get_children())
    viewpage.view_treeview["columns"] = columns
    for col in columns:
        viewpage.view_treeview.heading(col, text=col)
        viewpage.view_treeview.column(col, width=200)

    viewpage.view_treeview['show'] = 'headings'

    rows = cursor.fetchall()
    for row in rows:
        row = tuple(str(x) for x in row)
        viewpage.view_treeview.insert("", "end", values=row)
    viewpage.close_button.pack()
    viewpage.view_treeview.pack(pady=200)
    viewpage.close_button.config(command=viewpage.close_table)

def view_tickets():
    cursor = dbconnect.conn.cursor()
    cursor.execute("SELECT * FROM Ticket")
    columns = [column[0] for column in cursor.description]
    viewpage.view_treeview.delete(*viewpage.view_treeview.get_children())
    viewpage.view_treeview["columns"] = columns
    for col in columns:
        viewpage.view_treeview.heading(col, text=col)
        viewpage.view_treeview.column(col, width=200)

    viewpage.view_treeview['show'] = 'headings'

    rows = cursor.fetchall()
    for row in rows:
        row = tuple(str(x) for x in row)
        viewpage.view_treeview.insert("", "end", values=row)
    viewpage.close_button.pack()
    viewpage.view_treeview.pack(pady=200)
    viewpage.close_button.config(command=viewpage.close_table)

def view_showingmanagement():
    cursor = dbconnect.conn.cursor()
    cursor.execute("SELECT * FROM Showing_Management")
    columns = [column[0] for column in cursor.description]
    viewpage.view_treeview.delete(*viewpage.view_treeview.get_children())
    viewpage.view_treeview["columns"] = columns
    for col in columns:
        viewpage.view_treeview.heading(col, text=col)
        viewpage.view_treeview.column(col, width=200)

    viewpage.view_treeview['show'] = 'headings'

    rows = cursor.fetchall()
    for row in rows:
        row = tuple(str(x) for x in row)
        viewpage.view_treeview.insert("", "end", values=row)
    viewpage.close_button.pack()
    viewpage.view_treeview.pack(pady=200)
    viewpage.close_button.config(command=viewpage.close_table) 