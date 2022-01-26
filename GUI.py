from tkinter import *
from turtle import width
root = Tk()

root.title('First App') # name of program
root.resizable(height= True, width=True)
root.minsize(height=300 , width= 400)





# To center frame at the center of current desktop screen
def centerFrame():
    root.updat_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheght() // 2) - (height// 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x ,y)) 

root.mainloop()