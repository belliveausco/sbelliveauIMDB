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

        self.title = 'Most Popular TV Shows By RankUpDowns'
        self.left = 0
        self.top = 0
        self.width = 1250
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
        self.tableWidget.setRowCount(100)  # rows
        self.tableWidget.setColumnCount(9)  # Columns
        self.tableWidget.setHorizontalHeaderLabels(["pop_tv_id", "rank", "rankUpDown", "title", "fullTitle", "year",
                                                    "crew", "imDbRating", "imDbRatingCount"])
        conn = sql.connect('imDb.db')
        cursor = conn.cursor()
        query = "SELECT * FROM most_popular_tv_shows ORDER BY rankUpDown DESC;"

        table_row = 0
        for row in cursor.execute(query):
            self.tableWidget.setItem(table_row, 0, QTableWidgetItem(row[0]))
            self.tableWidget.setItem(table_row, 1, QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(table_row, 2, QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(table_row, 3, QTableWidgetItem(row[3]))
            self.tableWidget.setItem(table_row, 4, QTableWidgetItem(row[4]))
            self.tableWidget.setItem(table_row, 5, QTableWidgetItem(row[5]))
            self.tableWidget.setItem(table_row, 6, QTableWidgetItem(row[6]))
            self.tableWidget.setItem(table_row, 7, QTableWidgetItem(row[7]))
            self.tableWidget.setItem(table_row, 8, QTableWidgetItem(row[8]))
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