import sys
import sqlite3 as sql
import gui_window


def main():
    # Main database stuff here
    conn = sql.connect('imDb.db')
    cursor = conn.cursor()
    app = gui_window.QApplication(sys.argv)
    ex = gui_window.Window(conn, cursor)
    ex.isHidden()
    sys.exit(app.exec_())


main()
