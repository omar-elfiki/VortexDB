from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI.mainGUI import home
from PyQt5.QtGui import QIcon

def main():
    app = QApplication([])
    main_window = QMainWindow()

    home(main_window)
    main_window.setWindowTitle("Vortex Cinemas Database System")
    main_window.setWindowIcon(QIcon("assets/icon.ico"))

    main_window.show()

    app.exec_()

if __name__ == "__main__":
    main()

