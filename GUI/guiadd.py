from PyQt5.QtWidgets import QPushButton, QGridLayout, QWidget, QTableView, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox, QComboBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from DBOps import dbconnect, dbadddata, dataretrieve
import GUI.mainGUI as GUI

def add_customer(main_window):
    conn = dbconnect.db_connect()
    if conn is not None:
        GUI.clear(main_window)
        layout = QVBoxLayout()

        inputs_widget = QWidget()
        inputs_layout = QVBoxLayout(inputs_widget)
        label = QLabel("Add Customer", main_window)
        label.setFixedSize(485, 50)
        font = QFont("Helvetica", 20)
        label.setFont(font)
        inputs_layout.addWidget(label)
        name_label = QLabel("Name", main_window)
        inputs_layout.addWidget(name_label)
        name_input = QLineEdit(main_window)
        inputs_layout.addWidget(name_input)
        email_label = QLabel("Email", main_window)
        inputs_layout.addWidget(email_label)
        email_input = QLineEdit(main_window)
        inputs_layout.addWidget(email_input)
        phone_label = QLabel("Phone Number", main_window)
        inputs_layout.addWidget(phone_label)
        phone_input = QLineEdit(main_window)
        inputs_layout.addWidget(phone_input)
        birth_label = QLabel("Birth Date (YYYY-MM-DD)", main_window)
        inputs_layout.addWidget(birth_label)
        birth_input = QLineEdit(main_window)
        inputs_layout.addWidget(birth_input)

        buttons = QHBoxLayout()
        add_button = QPushButton("Add", main_window)
        add_button.setFixedSize(200, 50)
        add_button.clicked.connect(lambda: GUI.check_parameters(dbadddata.add_new_customer, name_input.text(), email_input.text(), phone_input.text(), birth_input.text()))
        buttons.addWidget(add_button)
        back_button = QPushButton("Back", main_window)
        back_button.setFixedSize(200, 50)
        back_button.clicked.connect(lambda: GUI.add(main_window))
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

def add_employee(main_window):
    conn = dbconnect.db_connect()
    branches = dataretrieve.getbranches([])
    if conn is not None:
        GUI.clear(main_window)
        layout = QVBoxLayout()

        inputs_widget = QWidget()
        inputs_layout = QVBoxLayout(inputs_widget)
        label = QLabel("Add Employee", main_window)
        label.setFixedSize(485, 50)
        font = QFont("Helvetica", 20)
        label.setFont(font)
        inputs_layout.addWidget(label)
        name_label = QLabel("Name", main_window)
        inputs_layout.addWidget(name_label)
        name_input = QLineEdit(main_window)
        inputs_layout.addWidget(name_input)
        email_label = QLabel("Email", main_window)
        inputs_layout.addWidget(email_label)
        email_input = QLineEdit(main_window)
        inputs_layout.addWidget(email_input)
        phone_label = QLabel("Phone Number", main_window)
        inputs_layout.addWidget(phone_label)
        phone_input = QLineEdit(main_window)
        inputs_layout.addWidget(phone_input)
        branch = QLabel("Branch", main_window)
        inputs_layout.addWidget(branch)
        branch_input = QComboBox(main_window)
        branch_input.addItems(branches)
        inputs_layout.addWidget(branch_input)

        buttons = QHBoxLayout()
        add_button = QPushButton("Add", main_window)
        add_button.setFixedSize(200, 50)
        add_button.clicked.connect(lambda: GUI.check_parameters(dbadddata.add_new_employee, name_input.text(), email_input.text(), phone_input.text(), dataretrieve.getbranchid(branch_input.currentText())))
        buttons.addWidget(add_button)
        back_button = QPushButton("Back", main_window)
        back_button.setFixedSize(200, 50)
        back_button.clicked.connect(lambda: GUI.add(main_window))
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

def add_movie(main_window):
    conn = dbconnect.db_connect()
    languages = ['English', 'Arabic']
    ages = [0, 7, 12, 15, 18]
    if conn is not None:
        GUI.clear(main_window)
        layout = QVBoxLayout()
        inputs_widget = QWidget()
        inputs_layout = QVBoxLayout(inputs_widget)

        label = QLabel("Add Movie", main_window)
        label.setFixedSize(485, 50)
        font = QFont("Helvetica", 20)
        label.setFont(font)
        inputs_layout.addWidget(label)

        title_label = QLabel("Title", main_window)
        inputs_layout.addWidget(title_label)
        title_input = QLineEdit(main_window)
        inputs_layout.addWidget(title_input)

        language_label = QLabel("Language", main_window)
        inputs_layout.addWidget(language_label)
        language_input = QComboBox(main_window)
        language_input.addItems(languages)
        inputs_layout.addWidget(language_input)

        subtitles_label = QLabel("Subtitles", main_window)
        inputs_layout.addWidget(subtitles_label)
        subtitles_input = QComboBox(main_window)
        subtitles_input.addItems(languages)
        inputs_layout.addWidget(subtitles_input)

        date_label = QLabel('Start & End Dates, (YYYY-MM-DD)', main_window)
        inputs_layout.addWidget(date_label)
        start_date_input = QLineEdit(main_window)
        inputs_layout.addWidget(start_date_input)
        end_date_input = QLineEdit(main_window)
        inputs_layout.addWidget(end_date_input)

        age_label = QLabel("Age Rating", main_window)
        inputs_layout.addWidget(age_label)
        age_input = QComboBox(main_window)
        age_input.addItems([str(i) for i in ages])
        inputs_layout.addWidget(age_input)

        buttons = QHBoxLayout()
        add_button = QPushButton("Add", main_window)
        add_button.setFixedSize(200, 50)
        add_button.clicked.connect(lambda: GUI.check_parameters(dbadddata.add_new_movie, title_input.text(), language_input.currentText(), subtitles_input.currentText(), start_date_input.text(), end_date_input.text(), age_input.currentText()))
        buttons.addWidget(add_button)
        back_button = QPushButton("Back", main_window)
        back_button.setFixedSize(200, 50)
        back_button.clicked.connect(lambda: GUI.add(main_window))
        buttons.addWidget(back_button)

        inputs_widget.setFixedSize(800,400)
        layout.addWidget(inputs_widget)
        layout.addLayout(buttons)

        widget = QWidget()
        widget.setLayout(layout)
        main_window.setCentralWidget(widget)


def add_screen(main_window):
    conn = dbconnect.db_connect()
    branches = dataretrieve.getbranches([])
    types = ['Standard', 'Deluxe', 'VIP']
    if conn is not None:
        GUI.clear(main_window)
        layout = QVBoxLayout()

        inputs_widget = QWidget()
        inputs_layout = QVBoxLayout(inputs_widget)
        label = QLabel("Add Screen", main_window)
        label.setFixedSize(485, 50)
        font = QFont("Helvetica", 20)
        label.setFont(font)

        inputs_layout.addWidget(label)
        branch_label = QLabel("Branch", main_window)
        inputs_layout.addWidget(branch_label)
        branch_input = QComboBox(main_window)
        branch_input.addItems(branches)
        inputs_layout.addWidget(branch_input)

        screen_label = QLabel("Screen Number", main_window)
        inputs_layout.addWidget(screen_label)
        screen_input = QLineEdit(main_window)
        inputs_layout.addWidget(screen_input)

        validity_input = QLineEdit(main_window)
        validity_input.setReadOnly(True)
        inputs_layout.addWidget(validity_input)

        def update_validity(index):
            branch = branch_input.itemText(index)
            screen = screen_input.text()
            validity = dataretrieve.getscreenvalidity(branch, screen)
            validity_input.setText(validity)

        screen_input.textChanged.connect(lambda: update_validity(branch_input.currentIndex()))

        seat_label = QLabel("Seat Type", main_window)
        inputs_layout.addWidget(seat_label)
        seat_input = QComboBox(main_window)
        seat_input.addItems(types)
        inputs_layout.addWidget(seat_input)

        number_label = QLabel("Number of Seats", main_window)
        inputs_layout.addWidget(number_label)
        number_input = QLineEdit(main_window)
        inputs_layout.addWidget(number_input)

        date_label = QLabel("Date of Inspection (YYYY-MM-DD)", main_window)
        inputs_layout.addWidget(date_label)
        date_input = QLineEdit(main_window)
        inputs_layout.addWidget(date_input)

        buttons = QHBoxLayout()
        add_button = QPushButton("Add", main_window)
        add_button.setFixedSize(200, 50)
        add_button.clicked.connect(lambda: GUI.check_parameters(dbadddata.add_new_screen, screen_input.text(),dataretrieve.getbranchid(branch_input.currentText()), seat_input.currentText(), number_input.text(), date_input.text()))
        buttons.addWidget(add_button)
        back_button = QPushButton("Back", main_window)
        back_button.setFixedSize(200, 50)
        back_button.clicked.connect(lambda: GUI.add(main_window))
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

def add_movie_showing(main_window):
    conn = dbconnect.db_connect()
    branches = dataretrieve.getbranches([])
    movies = dataretrieve.getMovies([])
    if conn is not None:
        GUI.clear(main_window)
        layout = QVBoxLayout()

        inputs_widget = QWidget()
        inputs_layout = QVBoxLayout(inputs_widget)
        label = QLabel("Add Movie Showing", main_window)
        label.setFixedSize(485, 50)
        font = QFont("Helvetica", 20)
        label.setFont(font)
        inputs_layout.addWidget(label)
        movie_label = QLabel("Movie", main_window)
        inputs_layout.addWidget(movie_label)
        movie_input = QComboBox(main_window)
        movie_input.addItems(movies)
        inputs_layout.addWidget(movie_input)
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

        date_label = QLabel("Date (YYYY-MM-DD)", main_window)
        inputs_layout.addWidget(date_label)
        date_input = QLineEdit(main_window)
        inputs_layout.addWidget(date_input)
        time_label = QLabel("Time (HH:MM)", main_window)
        inputs_layout.addWidget(time_label)
        time_input = QLineEdit(main_window)
        inputs_layout.addWidget(time_input)

        buttons = QHBoxLayout()
        add_button = QPushButton("Add", main_window)
        add_button.setFixedSize(200, 50)
        add_button.clicked.connect(lambda: GUI.check_parameters(dbadddata.add_new_showing, screen_input.currentText(), branch_input.currentText(), movie_input.currentText(), date_input.text(), time_input.text()))
        buttons.addWidget(add_button)
        back_button = QPushButton("Back", main_window)
        back_button.setFixedSize(200, 50)
        back_button.clicked.connect(lambda: GUI.add(main_window))
        buttons.addWidget(back_button)

        inputs_widget.setFixedSize(800,400)
        layout.addWidget(inputs_widget)
        layout.addLayout(buttons)

        widget = QWidget()
        widget.setLayout(layout)
        main_window.setCentralWidget(widget)

def add_showing_management(main_window):
    conn = dbconnect.db_connect()
    branches = dataretrieve.getbranches([])
    
    if conn is not None:
        GUI.clear(main_window)
        layout = QVBoxLayout()

        inputs_widget = QWidget()
        inputs_layout = QVBoxLayout(inputs_widget)
        label = QLabel("Assign Shift")
        label.setFixedSize(485, 50)
        font = QFont("Helvetica", 20)
        label.setFont(font)
        inputs_layout.addWidget(label)

        branch_label = QLabel("Branch", main_window)
        inputs_layout.addWidget(branch_label)
        branch_input = QComboBox(main_window)
        branch_input.addItems(branches)
        inputs_layout.addWidget(branch_input)
        

        employee_label = QLabel("Employee", main_window)
        inputs_layout.addWidget(employee_label)
        employee_input = QComboBox(main_window)
        inputs_layout.addWidget(employee_input)

        def update_employees(index):
            branch = branch_input.itemText(index)
            employees = dataretrieve.getemployee([], branch)
            employee_input.clear()
            employee_input.addItems(employees)

        branch_input.currentIndexChanged.connect(update_employees)


        showing_label = QLabel("Showing", main_window)
        inputs_layout.addWidget(showing_label)
        showing_input = QComboBox(main_window)
        inputs_layout.addWidget(showing_input)
        showing_details = QLineEdit(main_window)
        showing_details.setReadOnly(True)
        inputs_layout.addWidget(showing_details)

        def update_showing_details(index):
            branch = branch_input.itemText(index)
            showing = showing_input.itemText(index)
            showingdetails = dataretrieve.getshowinginfo(branch, showing)
            showing_details.setText(showingdetails)

        def update_showings(index):
            branch = branch_input.itemText(index)
            showings = dataretrieve.getshowingIDs([], branch)
            showing_input.clear()
            showing_input.addItems(showings)
    

        branch_input.currentIndexChanged.connect(update_showings)
        showing_input.currentIndexChanged.connect(update_showing_details)
        

        screen_label = QLabel("Screen", main_window)
        inputs_layout.addWidget(screen_label)
        screen_input = QLineEdit(main_window)
        screen_input.setReadOnly(True)
        inputs_layout.addWidget(screen_input)

        def updateScreen(index):
            screening = dataretrieve.getshowingscreen(branch_input.currentText(), showing_input.currentText())
            screen_input.setText(screening)

        showing_input.currentIndexChanged.connect(updateScreen)

        buttons = QHBoxLayout()
        add_button = QPushButton("Assign", main_window)
        add_button.setFixedSize(200, 50)
        add_button.clicked.connect(lambda: GUI.check_parameters(dbadddata.assign_management, dataretrieve.getEmployeeid(employee_input.currentText()), showing_input.currentText(), screen_input.text(), dataretrieve.getbranchid(branch_input.currentText())))
        buttons.addWidget(add_button)
        back_button = QPushButton("Back", main_window)
        back_button.setFixedSize(200, 50)
        back_button.clicked.connect(lambda: GUI.add(main_window))
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

