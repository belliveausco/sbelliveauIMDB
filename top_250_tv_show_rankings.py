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

        self.title = 'Top 250 TV Show Ratings'
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
        self.tableWidget.setRowCount(5)  # rows
        self.tableWidget.setColumnCount(24)  # Columns
        self.tableWidget.setHorizontalHeaderLabels(["ranking", "pop_movie_id", "totalRating", "totalRatingVotes",
                                                    "rating10percent", "rating10Votes", "rating9percent",
                                                    "rating9Votes", "rating8percent", "rating8Votes",
                                                    "rating7percent",
                                                    "rating7Votes", "rating6percent", "rating6Votes", "rating5percent",
                                                    "rating5Votes", "rating4percent", "rating4Votes",
                                                    "rating3percent", "rating3Votes", "rating2percent", "rating2Votes",
                                                    "rating1percent", "rating1Votes"])
        conn = sql.connect('imDb.db')
        cursor = conn.cursor()
        query = "SELECT * FROM user_ratings ORDER BY ranking;"

        table_row = 0
        for row in cursor.execute(query):
            self.tableWidget.setItem(table_row, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(table_row, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(table_row, 2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(table_row, 3, QTableWidgetItem(row[3]))
            self.tableWidget.setItem(table_row, 4, QTableWidgetItem(row[4]))
            self.tableWidget.setItem(table_row, 5, QTableWidgetItem(row[5]))
            self.tableWidget.setItem(table_row, 6, QTableWidgetItem(row[6]))
            self.tableWidget.setItem(table_row, 7, QTableWidgetItem(row[7]))
            self.tableWidget.setItem(table_row, 8, QTableWidgetItem(row[8]))
            self.tableWidget.setItem(table_row, 9, QTableWidgetItem(row[9]))
            self.tableWidget.setItem(table_row, 10, QTableWidgetItem(row[10]))
            self.tableWidget.setItem(table_row, 11, QTableWidgetItem(row[11]))
            self.tableWidget.setItem(table_row, 12, QTableWidgetItem(row[12]))
            self.tableWidget.setItem(table_row, 13, QTableWidgetItem(row[13]))
            self.tableWidget.setItem(table_row, 14, QTableWidgetItem(row[14]))
            self.tableWidget.setItem(table_row, 15, QTableWidgetItem(row[15]))
            self.tableWidget.setItem(table_row, 16, QTableWidgetItem(row[16]))
            self.tableWidget.setItem(table_row, 17, QTableWidgetItem(row[17]))
            self.tableWidget.setItem(table_row, 18, QTableWidgetItem(row[18]))
            self.tableWidget.setItem(table_row, 19, QTableWidgetItem(row[19]))
            self.tableWidget.setItem(table_row, 20, QTableWidgetItem(row[20]))
            self.tableWidget.setItem(table_row, 21, QTableWidgetItem(row[21]))
            self.tableWidget.setItem(table_row, 22, QTableWidgetItem(row[22]))
            self.tableWidget.setItem(table_row, 23, QTableWidgetItem(row[23]))
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
