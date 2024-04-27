import DBOps.operations as ops
import mainGUI as GUI
from PyQt5.QtWidgets import QMessageBox, QComboBox, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QWidget, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from DBOps.dbconnect import db_connect
import DBOps.dataretrieve as dataretrieve

def view_schedule(main_window, branch, screen):
    conn = db_connect()
    if conn is not None:
        schedule = ops.get_screen_schedule(conn,screen,branch)
        if schedule.rowCount() == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Empty Schedule")
            msg.setText("No showings found for this screen")
            msg.exec_()
        else:
            GUI.clear(main_window)
            GUI.displaytable(main_window, schedule)

    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to connect to database")
        msg.exec_()

def view_upcoming_movies(main_window, title_input):
    conn = db_connect()
    if conn is not None:
        title = title_input.currentText()
        upcoming_movies = ops.get_upcoming_movie_screenings(conn, title)
        if upcoming_movies.rowCount() == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Empty Schedule")
            msg.setText("No upcoming showings found for this movie")
            msg.exec_()
        else:
            GUI.clear(main_window)
            GUI.displaytable(main_window, upcoming_movies)
        
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to connect to database")
        msg.exec_()

def screenschedule(main_window):
    conn = db_connect()
    branches = dataretrieve.getbranches([])

    if conn is not None:
        GUI.clear(main_window)
        layout = QVBoxLayout()

        inputs_widget = QWidget()
        inputs_layout = QVBoxLayout(inputs_widget)
        label = QLabel("Screen Schedule", main_window)
        label.setFixedSize(485,50)
        font = QFont("Helvetica", 20)
        label.setFont(font)
        layout.addWidget(label)

        branch_label = QLabel("Branch", main_window)
        inputs_layout.addWidget(branch_label)
        branch_input = QComboBox(main_window)
        branch_input.addItems(branches)
        inputs_layout.addWidget(branch_input)

        screen_label = QLabel("Screen", main_window)
        inputs_layout.addWidget(screen_label)
        screen_input = QComboBox(main_window)
        inputs_layout.addWidget(screen_input)

        def update_screens(index):
            branch = branch_input.itemText(index)
            screens = dataretrieve.getscreens([], branch)
            screen_input.clear()
            screen_input.addItems(screens)

        branch_input.currentIndexChanged.connect(update_screens)

        buttons = QHBoxLayout()
        view_button = QPushButton("View", main_window)
        view_button.setFixedSize(200, 50)
        view_button.clicked.connect(lambda: view_schedule(main_window, dataretrieve.getbranchid(branch_input.currentText()), dataretrieve.getScreenID(screen_input.currentText())))
        buttons.addWidget(view_button)
        back_button = QPushButton("Back", main_window)
        back_button.setFixedSize(200, 50)
        back_button.clicked.connect(lambda: GUI.operations(main_window))
        buttons.addWidget(back_button)

        inputs_widget.setFixedSize(800,400)
        layout.addWidget(inputs_widget)
        layout.addLayout(buttons)

        widget = QWidget()
        widget.setLayout(layout)
        main_window.setCentralWidget(widget)

    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to connect to database")
        msg.exec_()

def customertickets(main_window):
    conn = db_connect()
    if conn is not None:
        GUI.clear(main_window)
        layout = QVBoxLayout()
        inputs_widget = QWidget()
        inputs_layout = QVBoxLayout(inputs_widget)

        label = QLabel("Customer Tickets", main_window)
        label.setFixedSize(485, 50)
        font = QFont("Helvetica", 20)
        label.setFont(font)
        inputs_layout.addWidget(label)

        customer_label = QLabel("Customer Phone", main_window)
        inputs_layout.addWidget(customer_label)
        customer_input = QLineEdit(main_window)
        inputs_layout.addWidget(customer_input)

        buttons = QHBoxLayout()
        view_button = QPushButton("View", main_window)
        view_button.setFixedSize(200, 50)
        view_button.clicked.connect(lambda: GUI.displaytable(main_window, ops.get_customer_tickets(conn, customer_input.text())))
        buttons.addWidget(view_button)
        back_button = QPushButton("Back", main_window)
        back_button.setFixedSize(200, 50)
        back_button.clicked.connect(lambda: GUI.operations(main_window))
        buttons.addWidget(back_button)

        inputs_widget.setFixedSize(800, 400)
        layout.addWidget(inputs_widget)
        layout.addLayout(buttons)

        widget = QWidget()
        widget.setLayout(layout)
        main_window.setCentralWidget(widget)

def emptyshowings(main_window):
    conn = db_connect()
    if conn is not None:
        empty_showings = ops.find_empty_showings(conn)
        if empty_showings.rowCount() == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("No empty showings found")
            msg.exec_()
        else:
            GUI.clear(main_window)
            GUI.displaytable(main_window, empty_showings)
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to connect to database")
        msg.exec_()

def sell_tickets(main_window):
    conn = db_connect()
    if conn is not None:
        GUI.clear(main_window)
        layout = QVBoxLayout()
        inputs_widget = QWidget()
        inputs_layout = QVBoxLayout(inputs_widget)

        label = QLabel("Sell Tickets", main_window)
        label.setFixedSize(485, 50)
        font = QFont("Helvetica", 20)
        label.setFont(font)
        inputs_layout.addWidget(label)

        customer_label = QLabel("Customer Phone", main_window)
        inputs_layout.addWidget(customer_label)
        customer_input = QLineEdit(main_window)
        inputs_layout.addWidget(customer_input)

        customer_id_label = QLabel("Customer Details", main_window)
        inputs_layout.addWidget(customer_id_label)
        customer_id_input = QLineEdit(main_window)
        customer_id_input.setReadOnly(True)
        inputs_layout.addWidget(customer_id_input)

        def update_customerid():
            customer_id_input.setText(dataretrieve.getCustomerinfo(customer_input.text()))
        
        customer_input.textChanged.connect(update_customerid)

        branch_label = QLabel("Branch", main_window)
        inputs_layout.addWidget(branch_label)
        branch_input = QComboBox(main_window)
        branches = dataretrieve.getbranches([])
        branch_input.addItems(branches)
        inputs_layout.addWidget(branch_input)

        screening_label = QLabel("Screening", main_window)
        inputs_layout.addWidget(screening_label)
        screening_input = QComboBox(main_window)
        inputs_layout.addWidget(screening_input)
        details_input = QLineEdit(main_window)
        details_input.setReadOnly(True)
        inputs_layout.addWidget(details_input)


        def update_details():
            branch = branch_input.currentText()
            screening = screening_input.currentText()
            details_input.setText(dataretrieve.getshowinginfo(branch, screening))

        def update_screenings(index):
            branch = branch_input.itemText(index)
            screenings = dataretrieve.getshowingIDs([], branch)
            screening_input.clear()
            screening_input.addItems(screenings)
            

        branch_input.currentIndexChanged.connect(update_screenings)
        screening_input.currentIndexChanged.connect(update_details)
        

        seat_label = QLabel("Seat Number", main_window)
        inputs_layout.addWidget(seat_label)
        seat_input = QLineEdit(main_window)
        inputs_layout.addWidget(seat_input)

        price_label = QLabel("Price", main_window)
        inputs_layout.addWidget(price_label)
        price_input = QLineEdit(main_window)
        inputs_layout.addWidget(price_input)

        buttons = QHBoxLayout()
        sell_button = QPushButton("Sell", main_window)
        sell_button.setFixedSize(200, 50)
        sell_button.clicked.connect(lambda: ops.sell_ticket(customer_input, branch_input, screening_input, seat_input, price_input))
        buttons.addWidget(sell_button)
        back_button = QPushButton("Back", main_window)
        back_button.setFixedSize(200, 50)
        back_button.clicked.connect(lambda: GUI.operations(main_window))
        buttons.addWidget(back_button)

        inputs_widget.setFixedSize(800, 400)
        layout.addWidget(inputs_widget)
        layout.addLayout(buttons)

        widget = QWidget()
        widget.setLayout(layout)
        main_window.setCentralWidget(widget)

    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to connect to database")
        msg.exec_()


def upcomingmovies(main_window):
    conn = db_connect()
    movies = dataretrieve.getMovies([])
    if conn is not None:
        GUI.clear(main_window)
        layout = QVBoxLayout()
        inputs_widget = QWidget()
        inputs_layout = QVBoxLayout(inputs_widget)

        label = QLabel("Upcoming Movie Screenings", main_window)
        label.setFixedSize(485, 50)
        font = QFont("Helvetica", 20)
        label.setFont(font)
        inputs_layout.addWidget(label)
        title_label = QLabel("Movie", main_window)
        inputs_layout.addWidget(title_label)

        title_input = QComboBox(main_window)
        title_input.addItems(movies)
        inputs_layout.addWidget(title_input)

        buttons = QHBoxLayout()
        view_button = QPushButton("View", main_window)
        view_button.setFixedSize(200, 50)
        view_button.clicked.connect(lambda: view_upcoming_movies(main_window, title_input))
        buttons.addWidget(view_button)
        back_button = QPushButton("Back", main_window)
        back_button.setFixedSize(200, 50)
        back_button.clicked.connect(lambda: GUI.operations(main_window))
        buttons.addWidget(back_button)

        inputs_widget.setFixedSize(800, 400)
        layout.addWidget(inputs_widget)
        layout.addLayout(buttons)
        
        widget = QWidget()
        widget.setLayout(layout)
        main_window.setCentralWidget(widget)

    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to connect to database")
        msg.exec_()