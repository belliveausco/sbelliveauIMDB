import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import sqlite3 as sql


class App(QWidget):

    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()
        # Database tools
        self.cursor = curs
        self.connection = conn

        self.title = 'Top 250 TV Shows'
        self.left = 0
        self.top = 0
        self.width = 1000
        self.height = 800

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self):
        # Create table
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(250)  # rows
        self.tableWidget.setColumnCount(7)  # Columns
        self.tableWidget.setHorizontalHeaderLabels(["id", "title", "fullTitle", "year",
                                                    "crew", "imDbRating", "imDbRatingCount"])
        conn = sql.connect('imDb.db')
        cursor = conn.cursor()
        query = "SELECT * FROM top250_tv_shows;"

        table_row = 0
        for row in cursor.execute(query):
            self.tableWidget.setItem(table_row, 0, QTableWidgetItem(row[0]))
            self.tableWidget.setItem(table_row, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(table_row, 2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(table_row, 3, QTableWidgetItem(row[3]))
            self.tableWidget.setItem(table_row, 4, QTableWidgetItem(row[4]))
            self.tableWidget.setItem(table_row, 5, QTableWidgetItem(row[5]))
            self.tableWidget.setItem(table_row, 6, QTableWidgetItem(row[6]))
            table_row += 1

        # Show widget
        self.show()


def main():
    conn = sql.connect('imDb.db')
    cursor = conn.cursor()
    app = QApplication(sys.argv)
    ex = App(conn, cursor)
    ex.isHidden()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
