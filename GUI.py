from tkinter import *
from turtle import left, width
root = Tk()

pass_string = StringVar()

root.title('-- Basic Password App _ Python --') # name of program
root.resizable(height= True, width=True)
root.minsize(height=600 , width= 400)


lb_main = Label(root, text="PASSWORD GENERATOR", bg="orange red", fg="black", font="Tahoma 24 bold")
lb_main.pack(anchor=CENTER, side = TOP)

lb_length = Label(root, text= "Password Length",font="none 16 bold")


lb_main1 = Label(root, text="Password Length", fg="black", font="Arial 12")
lb_main1.pack(anchor= W, side = TOP, pady=20)

Entry(root, width=15).pack(side= TOP, pady= 20)



#lbl2 = Label (root, text="Enter something here:", bg="orange red", fg="white", font="none 12 bold")
#lbl2.config(anchor=CENTER)
#lbl2.pack()


# To center frame at the center of current desktop screen
def centerFrame(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height// 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x ,y)) 

centerFrame(root)
root.mainloop()