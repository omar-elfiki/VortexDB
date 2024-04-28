from PyQt5.QtWidgets import QPushButton, QGridLayout, QWidget, QTableView, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlQueryModel
from DBOps.dbconnect import db_connect, db_disconnect
from GUI.guiadd import add_customer, add_employee, add_movie, add_screen, add_movie_showing, add_showing_management
import GUI.guiops as ops
import GUI.guireports as greports
import GUI.guiview as gview

def check_parameters(destination_function, *args):
    for i, arg in enumerate(args, 1):
        if not arg:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText(f"Error: Parameter {i} is empty.")
            msg.exec_()
            return
    return destination_function(*args)

def get_all(conn, table_name):
    model = QSqlQueryModel()
    model.setQuery(f'SELECT * FROM {table_name}', conn)

    return model


def home(main_window):
    pixmap = QPixmap("assets/light.png")
    image = QLabel(main_window)
    image.setPixmap(pixmap)
    image.resize(500,500)
    image.move(150, 0)

    label = QLabel("Vortex Cinemas Database System", main_window)
    label.setFixedSize(485, 50)
    label.move(165, 350)
    font = QFont("Helvetica", 20)
    label.setFont(font)

    connect_button = QPushButton("Connect", main_window)
    connect_button.setFixedSize(200, 50)
    connect_button.move(300, 450)


    main_window.resize(800, 600)

    connect_button.clicked.connect(lambda: actions(main_window))
    connect_button.show()
    image.show()

def actions(main_window):
    conn = db_connect()
    if conn is not None:
        clear(main_window)
        name_list = ['Add Records', 'View Records', 'Operations', 'Reports']
        functionlist = [lambda: add(main_window), lambda: view(main_window), lambda: operations(main_window), lambda: reports(main_window)]
        grid_layout = QGridLayout()
        for i in range(2):
            for j in range(2):
                index = i * 2 + j
                button = QPushButton(f'{name_list[index]}' , main_window)
                button.setFixedSize(200, 50)
                button.clicked.connect(functionlist[index])
                grid_layout.addWidget(button, i, j)

        layout = QVBoxLayout()
        layout.addLayout(grid_layout)

        back_button_layout = QHBoxLayout()
        back_button = QPushButton("Disconnect", main_window)
        back_button.setFixedSize(100, 50)
        back_button.clicked.connect(lambda: db_disconnect(main_window, conn))
        back_button_layout.addStretch(2)
        back_button_layout.addWidget(back_button)
        back_button_layout.addStretch(2)

        layout.addLayout(back_button_layout)

        widget = QWidget()
        widget.setLayout(layout)
        main_window.setCentralWidget(widget)
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to connect to database")
        msg.exec_()

def add(main_window):
    conn = db_connect()
    if conn is not None:
        clear(main_window)
        name_list = ['Customer', 'Employee', 'Movie', 'Screen', 'Movie Showing', 'Showing Management']
        functionlist = [lambda: add_customer(main_window), lambda: add_employee(main_window), 
                        lambda: add_movie(main_window), lambda: add_screen(main_window), lambda: add_movie_showing(main_window), 
                        lambda: add_showing_management(main_window)]

        grid_layout = QGridLayout()
        for i in range(3):
            for j in range(2):
                index = i * 2 + j
                button = QPushButton(f'Add {name_list[index]}' , main_window)
                button.setFixedSize(200, 50)
                button.clicked.connect(functionlist[index])
                grid_layout.addWidget(button, i, j)

        layout = QVBoxLayout()
        layout.addLayout(grid_layout)

        back_button_layout = QHBoxLayout()
        back_button = QPushButton("Back", main_window)
        back_button.setFixedSize(100, 50)
        back_button.clicked.connect(lambda: actions(main_window))
        back_button_layout.addStretch()
        back_button_layout.addWidget(back_button)
        back_button_layout.addStretch()

        layout.addLayout(back_button_layout)

        widget = QWidget()
        widget.setLayout(layout)
        main_window.setCentralWidget(widget)

def operations(main_window):
    conn = db_connect()
    if conn is not None:
        clear(main_window)
        name_list = ['Screen Schedule', 'Sell Tickets', 'Upcoming Movie Screenings', 'Empty Showings']
        functionlist = [lambda: ops.screenschedule(main_window), lambda: ops.sell_tickets(main_window), 
                        lambda: ops.upcomingmovies(main_window), lambda: ops.emptyshowings(main_window)]

        grid_layout = QGridLayout()
        for i in range(2):
            for j in range(2):
                index = i * 2 + j
                button = QPushButton(f'{name_list[index]}' , main_window)
                button.setFixedSize(200, 50)
                button.clicked.connect(functionlist[index])
                grid_layout.addWidget(button, i, j)
        
        layout = QVBoxLayout()
        layout.addLayout(grid_layout)

        customer_button_layout = QHBoxLayout()
        customer_button = QPushButton("Customer Tickets", main_window)
        customer_button.setFixedSize(200, 50)
        customer_button.clicked.connect(lambda: ops.customertickets(main_window))
        customer_button_layout.addStretch(2)
        customer_button_layout.addWidget(customer_button)
        customer_button_layout.addStretch(2)

        layout.addLayout(customer_button_layout)

        back_button_layout = QHBoxLayout()
        back_button = QPushButton("Back", main_window)
        back_button.setFixedSize(100, 50)
        back_button.clicked.connect(lambda: actions(main_window))
        back_button_layout.addStretch()
        back_button_layout.addWidget(back_button)
        back_button_layout.addStretch()

        layout.addLayout(back_button_layout)

        widget = QWidget()
        widget.setLayout(layout)
        main_window.setCentralWidget(widget)

    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to connect to database")
        msg.exec_()

def reports(main_window):
    conn = db_connect()
    if conn is not None:
        clear(main_window)
        name_list = ['Total Tickets Sold', 'Tickets Sold by Branch', 'Average Tickets Per Movie']
        functionlist = [lambda: greports.total_tickets_sold(main_window), lambda: greports.tickets_sold_by_branch(main_window), lambda: greports.average_tickets(main_window)]

        grid_layout = QGridLayout()
        for i in range(3):
            for j in range(1):
                index = i * 1 + j
                button = QPushButton(f'{name_list[index]}' , main_window)
                button.setFixedSize(200, 50)
                button.clicked.connect(functionlist[index])
                grid_layout.addWidget(button, i, j)
        
        layout = QVBoxLayout()
        layout.addLayout(grid_layout)

        back_button_layout = QHBoxLayout()
        back_button = QPushButton("Back", main_window)
        back_button.setFixedSize(100, 50)
        back_button.clicked.connect(lambda: actions(main_window))
        back_button_layout.addStretch()
        back_button_layout.addWidget(back_button)
        back_button_layout.addStretch()

        layout.addLayout(back_button_layout)

        widget = QWidget()
        widget.setLayout(layout)
        main_window.setCentralWidget(widget)

def view(main_window):
    conn = db_connect()
    if conn is not None:
        clear(main_window)
        CBmodel = get_all(conn, "Cinema_Branch")
        Cmodel = get_all(conn, "Customer")
        Emodel = get_all(conn, "Employee")
        Mmodel = get_all(conn, "Movie")
        name_list = ['Branches', 'Customers', 'Employees', 'Movies', 'Screens', 'Showings', 'Tickets', 'Management']
        functionlist = [lambda: displaytable(main_window, CBmodel), lambda: displaytable(main_window, Cmodel), lambda: displaytable(main_window, Emodel), 
                        lambda: displaytable(main_window, Mmodel), lambda: gview.viewscreens(main_window), lambda: gview.viewshowings(main_window), 
                        lambda: gview.viewtickets(main_window), lambda: gview.viewshifts(main_window)]

        grid_layout = QGridLayout()
        for i in range(4):
            for j in range(2):
                index = i * 2 + j
                button = QPushButton(f'View {name_list[index]}' , main_window)
                button.setFixedSize(200, 50)
                button.clicked.connect(functionlist[index])
                grid_layout.addWidget(button, i, j)

        layout = QVBoxLayout()
        layout.addLayout(grid_layout)

        back_button_layout = QHBoxLayout()
        back_button = QPushButton("Back", main_window)
        back_button.setFixedSize(100, 50)
        back_button.clicked.connect(lambda: actions(main_window))
        back_button_layout.addStretch()
        back_button_layout.addWidget(back_button)
        back_button_layout.addStretch()

        layout.addLayout(back_button_layout)

        widget = QWidget()
        widget.setLayout(layout)
        main_window.setCentralWidget(widget)

    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to connect to database")
        msg.exec_()


def displaytable(main_window, model):
    layout = QVBoxLayout()

    table_view = QTableView()
    table_view.setModel(model)
    table_view.resizeColumnsToContents()
    table_view.resizeRowsToContents()
    table_view.horizontalHeader().setStretchLastSection(True)

    layout.addWidget(table_view)

    back_button = QPushButton("Back", main_window)
    back_button.setFixedSize(200, 50)
    back_button.clicked.connect(lambda: actions(main_window))
    layout.addWidget(back_button)


    widget = QWidget()
    widget.setLayout(layout)
    main_window.setCentralWidget(widget)


def clear(main_window):
    for widget in main_window.findChildren(QWidget):
        widget.hide()
