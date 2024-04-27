from PyQt5.QtSql import QSqlDatabase

def db_connect():
    server = 'localhost'
    database = 'Cinema-2'
    driver = 'QODBC3'  # QODBC3 is the QSqlDatabase driver for ODBC

    # Create a QSqlDatabase object
    db = QSqlDatabase.addDatabase(driver)

    # Set the connection string
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    db.setDatabaseName(connection_string)

    # Open the connection
    if db.open():
        print("Connection successful")
        return db
    else:
        print("Connection Error: ", db.lastError().text())
        return None

def db_disconnect(main_window, db):
    import mainGUI
    mainGUI.clear(main_window)
    mainGUI.home(main_window)
    db.close()
    print("Connection closed")

db = None