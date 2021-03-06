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

        self.title = 'Top 250 TV Shows Also in Most Popular TV Shows'
        self.left = 0
        self.top = 0
        self.width = 1250
        self.height = 300

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
        self.tableWidget.setRowCount(35)  # rows
        self.tableWidget.setColumnCount(7)  # Columns
        self.tableWidget.setHorizontalHeaderLabels(["id", "rank", "rankUpDown", "title", "year", "imDbRating",
                                                    "imDbRatingCount"])
        conn = sql.connect('imDb.db')
        cursor = conn.cursor()
        query = "SELECT top250_tv_shows.id, most_popular_tv_shows.rank, most_popular_tv_shows.rankUpDown, " \
                "most_popular_tv_shows.title, top250_tv_shows.year, top250_tv_shows.imDbRating, " \
                "top250_tv_shows.imDbRatingCount " \
                "FROM " \
                "top250_tv_shows " \
                "INNER JOIN " \
                "most_popular_tv_shows ON top250_tv_shows.id = most_popular_tv_shows.pop_tv_id; "
        table_row = 0
        for row in cursor.execute(query):
            self.tableWidget.setItem(table_row, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(table_row, 1, QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(table_row, 2, QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(table_row, 3, QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(table_row, 4, QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(table_row, 5, QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(table_row, 6, QTableWidgetItem(str(row[6])))
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
