from PyQt5.QtSql import QSqlDatabase

def db_connect():
    server = 'localhost'
    database = 'Cinema-2'
    driver = 'QODBC3'

    
    db = QSqlDatabase.addDatabase(driver)

   
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    db.setDatabaseName(connection_string)

    if db.open():
        print("Connection successful")
        return db
    else:
        print("Connection Error: ", db.lastError().text())
        return None

def db_disconnect(main_window, db):
    import GUI.mainGUI as mainGUI
    mainGUI.clear(main_window)
    mainGUI.home(main_window)
    db.close()
    print("Connection closed")

db = None