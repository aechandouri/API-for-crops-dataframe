
import tkinter as tnk
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Describable:
    def __init__(self):
        #Main window
        win_main = tnk()
        win_main.title("Food crops dataset")
        win_main.configure()
      
        #set window size
        widthwin = win_main.winfo_screenwidth()
        heightwin = win_main.winfo_screenheight()

       
        API_title = Label(win_main, text="FoodCorps API")
        API_title.pack()

        win_main.mainloop()


    def describe(self) -> str:
        pass


if __name__ == "__main__":
    Describable()
