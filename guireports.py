from PyQt5.QtWidgets import QPushButton, QGridLayout, QWidget, QTableView, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox, QComboBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from DBOps import dbconnect, dbadddata, dataretrieve, aggregate
import mainGUI as GUI

def total_tickets_sold(main_window):
    conn = dbconnect.db_connect()
    if conn is not None:
        GUI.clear(main_window)
        layout = QVBoxLayout()

        inputs_widget = QWidget()
        inputs_layout = QHBoxLayout(inputs_widget)
        label = QLabel("Total Tickets Sold by date", main_window)
        label.setFixedSize(485,50)
        font = QFont('Helvetica', 20)
        label.setFont(font)
        inputs_layout.addWidget(label)
        date_label = QLabel("Date, (YYYY-MM-DD)", main_window)
        inputs_layout.addWidget(date_label)
        date_input = QLineEdit(main_window)
        inputs_layout.addWidget(date_input)

        buttons = QHBoxLayout()
        submit_button = QPushButton("Submit", main_window)
        submit_button.setFixedSize(200, 50)
        submit_button.clicked.connect(lambda: GUI.displaytable(main_window, aggregate.sum_all_ticks(date_input.text(), conn)))
        buttons.addWidget(submit_button)
        back_button = QPushButton("Back", main_window)
        back_button.setFixedSize(200, 50)
        back_button.clicked.connect(lambda: GUI.reports(main_window))
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

    
def tickets_sold_by_branch(main_window):
    conn = dbconnect.db_connect()
    if conn is not None:
        GUI.clear(main_window)
        layout = QVBoxLayout()

        inputs_widget = QWidget()
        inputs_layout = QHBoxLayout(inputs_widget)
        label = QLabel("Tickets Sold by Branch", main_window)
        label.setFixedSize(485,50)
        font = QFont('Helvetica', 20)
        label.setFont(font)
        inputs_layout.addWidget(label)
        date_label = QLabel("Date, (YYYY-MM-DD)", main_window)
        inputs_layout.addWidget(date_label)
        date_input = QLineEdit(main_window)
        inputs_layout.addWidget(date_input)

        buttons = QHBoxLayout()
        submit_button = QPushButton("Submit", main_window)
        submit_button.setFixedSize(200, 50)
        submit_button.clicked.connect(lambda: GUI.displaytable(main_window, aggregate.ticks_sold_by_branch(date_input.text(), conn)))
        buttons.addWidget(submit_button)
        back_button = QPushButton("Back", main_window)
        back_button.setFixedSize(200, 50)
        back_button.clicked.connect(lambda: GUI.reports(main_window))
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

def average_tickets(main_window):
    conn = dbconnect.db_connect()
    if conn is not None:
        average = aggregate.average_tickets_sold(conn)
        if average.rowCount() == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("No tickets sold")
            msg.exec_()
        else:
            GUI.clear(main_window)
            GUI.displaytable(main_window, average)
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Failed to connect to database")
        msg.exec_()