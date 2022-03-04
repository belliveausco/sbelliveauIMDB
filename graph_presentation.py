import sqlite3
from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import os
import sqlite3 as sql


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()
        # Database tools
        self.cursor = curs
        self.connection = conn

        self.title = 'Graphical Presentation'
        self.left = 0
        self.top = 0
        self.width = 1450
        self.height = 800

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        conn = sql.connect('imDb.db')
        cursor = conn.cursor()

        query = "SELECT * FROM most_popular_movies WHERE rankUpDown>0 ORDER BY rankUpDown DESC;"
        movies_rankUpDown_positive = list()
        i = 0
        popular_movies_moving_up = list()
        for row in cursor.execute(query):
            movies_rankUpDown_positive.append(int(row[2]))
            i += 1
        popular_movies_moving_up.append(i)

        query = "SELECT * FROM most_popular_movies WHERE rankUpDown<0 ORDER BY rankUpDown DESC;"
        movies_rankUpDown_negative = list()
        j = 0
        popular_movies_moving_down = list()
        for row in cursor.execute(query):
            movies_rankUpDown_negative.append(int(row[2]))
            j += 1
        popular_movies_moving_down.append(j)

        query = "SELECT * FROM most_popular_tv_shows WHERE rankUpDown>0 ORDER BY rankUpDown DESC;"
        tv_rankUpDown_positive = list()
        k = 0
        popular_tv_moving_up = list()
        for row in cursor.execute(query):
            tv_rankUpDown_positive.append(int(row[2]))
            k += 1
        popular_tv_moving_up.append(k)

        query = "SELECT * FROM most_popular_tv_shows WHERE rankUpDown<0 ORDER BY rankUpDown DESC;"
        tv_rankUpDown_negative = list()
        m = 0
        popular_tv_moving_down = list()
        for row in cursor.execute(query):
            tv_rankUpDown_negative.append(int(row[2]))
            m += 1
        popular_tv_moving_down.append(m)

        self.graphWidget.setBackground('w')
        self.graphWidget.setTitle("Graph Showing Trends", color="blue", size="30pt")
        styles = {"font-size": "20px"}
        self.graphWidget.setLabel("left", "Number of Movies/TV Shows", color="blue", **styles)
        self.graphWidget.setLabel("bottom", "Red = popular_movies_moving_up, Blue = popular_movies_moving_down, Green "
                                            "= popular_tv_moving_up, Yellow = popular_tv_moving_down", color="blue",
                                            **styles)
        spot1 = [1]
        spot2 = [2]
        spot3 = [3]
        spot4 = [4]
        self.plot(spot1, popular_movies_moving_up, "red")
        self.plot(spot2, popular_movies_moving_down, "blue")
        self.plot(spot3, popular_tv_moving_up, "green")
        self.plot(spot4, popular_tv_moving_down, "yellow")

    def plot(self, x, y, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, pen=pen, symbol='+', symbolSize=35, symbolBrush=color)


def main():
    conn = sql.connect('imDb.db')
    cursor = conn.cursor()
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow(conn, cursor)
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
