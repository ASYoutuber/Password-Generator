from tkinter import *
import random
import Display
import Insert

window = Tk()

title = Label(window, text = "Password Generator", bg = "blue", fg = "white", font = ("Times New Roman", 40), width = 45, justify = "center")
num_chrac = Label(window, text = "Number of chracters", bg = "light blue", fg = "black", font = ("Times New Roman", 20), width = 25)
result = Label(window)
text = "Which website you want the password to be saved for?"
lbl = Label(window, text = text, bg = "light blue", fg = "black", font = ("Times New Roman", 20), width = len(text) + 5)
user_for = Entry(window, width = 25, font = ("Futura", 20))

v = IntVar()
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()

scale = Scale(window, variable = v, from_ = 8, to = 15, orient = HORIZONTAL)

num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
lower = list(map(chr, range(97, 123)))
upper = list(map(chr, range(65, 91)))
symbols = ["%", "@", "#", "$", "&"]
password = ""

def Selection():
    global password

    password_l = []
    password = ""

    if (v1.get() == 1):
        password_l.append(num)
         
    if (v2.get() == 1):
        password_l.append(lower)
         
    if (v3.get() == 1):
        password_l.append(upper)
    
    if (v4.get() == 1):
        password_l.append(symbols)
    
    if (len(password_l) > 0):
    
        for i in range(v.get()):
            password = password + random.choice(random.choice(password_l))
    
    result.configure(text = "Your generated password is " + password, bg = "blue", fg = "white", font = ("Times New Roman", 20), width = len(password) + 30)

def Add_Data():
    global password
    if (len(user_for.get()) > 0):
        Insert.add(user_for.get(), password)

def Save_Passwords():
    lbl.grid(row = 12, column = 2)
    user_for.grid(row = 13, column = 2)
    btn2.grid(row = 14, column = 2)

def Show_Password():
    Display.Read_Data()

c = Checkbutton(window, text = "Include Numbers", variable = v1, onvalue = 1, offvalue = 0, bg = "blue", fg = "white", font = ("Times New Roman", 20), width = 25)
c2 = Checkbutton(window, text = "Lowercase Letters", variable = v2, onvalue = 1, offvalue = 0, bg = "light blue", fg = "black", font = ("Times New Roman", 20), width = 25)
c3 = Checkbutton(window, text = "Uppercase Letters", variable = v3, onvalue = 1, offvalue = 0, bg = "blue", fg = "white", font = ("Times New Roman", 20), width = 25)
c4 = Checkbutton(window, text = "Symbols", variable = v4, onvalue = 1, offvalue = 0, bg = "light blue", fg = "black", font = ("Times New Roman", 20), width = 25)

btn = Button(window, text = "Generate password", bg = "blue", fg = "white", font = ("Times New Roman", 20), width = 25, command = Selection)
btn2 = Button(window, text = "Add password", bg = "blue", fg = "white", font = ("Times New Roman", 20), width = 25, command = Add_Data)
btn3 = Button(window, text = "Save password", bg = "blue", fg = "white", font = ("Times New Roman", 20), width = 25, command = Save_Passwords)
btn4 = Button(window, text = "Show passwords", bg = "blue", fg = "white", font = ("Times New Roman", 20), width = 25, command = Show_Password)

title.grid(row = 0, column = 2)
num_chrac.grid(row = 1, column = 2)
scale.grid(row = 2, column = 2)
c.grid(row = 3, column = 2)
c3.grid(row = 5, column = 2)
c2.grid(row = 4, column = 2)
c4.grid(row = 6, column = 2)
btn.grid(row = 7, column = 2)
btn4.grid(row = 8, column = 2)
btn3.grid(row = 10, column = 2)
result.grid(row = 11, column = 2)

window.geometry("900x600")
window.title("Password Generator")
window.mainloop()