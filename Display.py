import sqlite3
from tkinter import *

def Read_Data():
    window = Tk()
    window.title("Show Passwords")
    i = 1
    try:
        connection = sqlite3.connect("Password_Saver.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * from Password_saver_table")
        records = cursor.fetchall()
        lbl = Label(window, text = "Set For", borderwidth = 2, relief = "ridge", bg = "blue", fg = "white", width = 25, font = ("Times New Roman", 20))
        lbl.grid(row = 0, column = 0)
        lbl = Label(window, text = "Passwords", borderwidth = 2, relief = "ridge", bg = "blue", fg = "white", width = 25, font = ("Times New Roman", 20))
        lbl.grid(row = 0, column = 1)

        for row in records:
            for j in range(len(row)):
                lbl = Label(window, text = row[j], bg = "light blue", fg = "black", borderwidth = 2, relief = "ridge", font = ("Times New Roman", 20), width = 25)
                lbl.grid(row = i, column = j)
            i += 1
        
        window.geometry("600x600")
        window.mainloop()

        cursor.close()
    except sqlite3.Error as error:
        lbl.configure(text = "Failed to read data from the table " + error, bg = "light blue", fg = "black", font = ("Times New Roman", 20), width = 25)

    finally:
        if (connection):
            connection.close()