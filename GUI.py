from tkinter import *
from tkinter import font
from turtle import back, color, left, width
root = Tk()

pass_string = StringVar()

def ininitializeGUI():
    root.title('-- Basic Password Generator App _ Python --') # name of program
    root.resizable(height= True, width=True)
    root.minsize(height=300 , width= 650)
    root.configure(background = "LightGoldenrod2")
    

    lb_main = Label(root, text="PASSWORD GENERATOR", bg="gold", fg="black", font="Tahoma 24 bold")
    lb_main.grid(row = 0, column = 1 ,columnspan= 4, rowspan= 1)

    '''Left panel OPTION buttons'''
    optionFrame = Frame(root)
    optionFrame.configure(background="LightGoldenrod2")
    Button(optionFrame,text = "Create Password", font="12 ",border= 5, bg = "misty rose").pack(side=TOP,pady= 10,fill = X)
    Button(optionFrame,text = "Reset", font = "12", border= 5, bg = "misty rose").pack(side = TOP,pady= 10, fill = X)
    Button(optionFrame,text = "Exit", font = "12", border= 5,bg = "orange red").pack(side = TOP,pady= 10, fill = X)
    optionFrame.grid(row = 1 , column = 0 , rowspan = 4)

    Label(root, text = "Length").grid(row = 1 ,column= 1)
    Label(root, text = "Length").grid(row = 2 ,column= 1)

    


# To center frame at the center of current desktop screen
def centerFrame(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height// 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x ,y)) 

ininitializeGUI()
centerFrame(root)
root.mainloop()