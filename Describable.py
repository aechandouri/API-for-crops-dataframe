
#Importation de Tkinter selon les différentes versions
try:
    try :
        import tkinter as Tk
        from tkinter import *
        from tkinter.messagebox import *
        from tkinter.filedialog import *
    except:
        import Tkinter as Tk
        from tKinter import *
        from tKinter.messagebox import *
        from tKinter.filedialog import *
except:
    raise ImportError('Tkinter non disponible')

class Describable:
    def __init__(self):
        #Initailisation de la fenêtre principale
        main = Tk()
        main.title("food crops")
        main.configure(bg = "white")
        #main.resizable(0,0)

        #On récupère la largeur (ws) et la hauteur (hs) de la fenêtre
        ws = main.winfo_screenwidth()
        hs = main.winfo_screenheight()

        #texte
        titre = Label(main, text="Application foodCrop", font =("", 32))
        titre.pack()



        main.mainloop()


    def describe(self) -> str:
        pass


if __name__ == "__main__":
    Describable()
