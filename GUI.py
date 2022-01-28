from cgitb import text
from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import font
import tkinter
from turtle import back, color, left, width

from password_generator import generateRandomString


def createPassword():
    length = 0
    try:
        length = int(pass_length.get())
        if length <= 0 or length > 50:
            raise ValueError("Out of bound length")
        pass_string.set(generateRandomString(length))

    except ValueError as e:
         tkinter.messagebox.showinfo("Input Error !" , "Please provide an input for password length as integer in range (0 - 50]")
         print(e)
         pass_length.set("")

def reset():
    pass_length.set("")
    pass_string.set("")

# GLOBAL VARIABLES #  
root = Tk()
pass_string = StringVar()
pass_length = StringVar()


def initializeGUI():
    root.title('-- Basic Password Generator App _ Python --') # name of program
    root.resizable(height= True, width=True)
    root.minsize(height=300 , width= 600)
    root.configure(background = "LightGoldenrod2")
    
    #Top Title Label
    lb_main = Label(root, text="PASSWORD GENERATOR", bg="LightGoldenrod2", fg="black", font="Tahoma 24 bold")
    lb_main.grid(row = 0, column = 0 ,columnspan= 5, rowspan= 1)

    #Left panel OPTION buttons
    optionFrame = Frame(root)
    optionFrame.configure(background="LightGoldenrod2",borderwidth= 10, )
    Button(optionFrame,text = "Create Password", font="12 ",border= 5, bg = "misty rose" , command=createPassword).pack(side=TOP,pady= 10,fill = X)
    Button(optionFrame,text = "Reset", font = "12", border= 5, bg = "misty rose", command = reset).pack(side = TOP,pady= 10, fill = X)
    Button(optionFrame,text = "Exit", font = "12", border= 5,bg = "orange red", command = root.quit).pack(side = TOP,pady= 10, fill = X)
    optionFrame.grid(row = 1 , column = 0 , rowspan = 4)

    # Password Length row
    Label(root, text = "Password Length :", font= 10 , bg="LightGoldenrod2" ).grid(row = 1 ,column= 1)
    Entry(root, width = 30,font= "10" ,textvariable=pass_length).grid(row=1, column=2)

    # Password generation row
    Label(root, text = "Generated Password :", font= 10, bg="LightGoldenrod2" ).grid(row = 2 ,column= 1)
    Entry(root, width = 30,font= "10" ,textvariable=pass_string).grid(row=2, column=2)

# To center frame at the center of current desktop screen
def centerFrame(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height// 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x ,y)) 

initializeGUI()
centerFrame(root)
root.mainloop()