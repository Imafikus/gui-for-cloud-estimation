
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Button, Style
from tkinter import messagebox
from tkinter import Toplevel
from tkinter import *

from PIL import ImageTk, Image


                                                                        

class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()

        
    def initUI(self):
      
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=True, pady=5)
	
        frames = []
                
        frame1 = Frame(self)
        frame1.pack(fill=X)
            
        lbl_date1 = Label(frame1, text="Start").grid(row=0, column=0, pady=5, padx=5)
        date1 = Entry(frame1, width=10)
        date1.grid(row=0, column=1, padx=2.5)

        lbl_date2 = Label(frame1, text="End").grid(row=0, column=2, padx=5)
        date2 = Entry(frame1, width=10)
        date2.grid(row=0, column=3, padx=2.5)

        settings = Button(frame1, text="Settings", command=self.create_window)
        settings.grid(row=0, column=4, padx=50)
        

        frame2 = Frame(self)
        frame2.pack(fill=X)
        calculate = Button(frame2, text = "Calculate")
        calculate.pack(pady = 30)
        calculate.config(height=15, width = 30)
        

        
    def create_window(self):
        newWindow = Toplevel(self)

        

        newWindow.title("Settings")
        lblCVP = Label(newWindow, text="CVP").grid(row=0, column=0, padx=5)
        entryCVP1 = Entry(newWindow, width=10).grid(row=0, column=1, padx=5)
        entryCVP2 = Entry(newWindow, width=10).grid(row=0, column=2, padx=5)

        lblFOV = Label(newWindow, text="FOV").grid(row=1, column=0, padx=5, pady=5)
        entryFOV1 = Entry(newWindow, width=10).grid(row=1, column=1, padx=5, pady=5)
        entryFOV2 = Entry(newWindow, width=10).grid(row=1, column=2, padx=5, pady=5)
        newWindow.geometry("400x400+200+200")

        lblDIR = Label(newWindow, text="DIR").grid(row=2, column=0, padx=5)
        entryDIR1 = Entry(newWindow, width=10).grid(row=2, column=1, padx=5)
        entryDIR2 = Entry(newWindow, width=10).grid(row=2, column=2, padx=5)
        newWindow.geometry("250x200+200+200")

                
        	      

        
        


def main():
  
    root = Tk()
    root.geometry("400x150+300+50")
    app = Example()
    root.mainloop()  


if __name__ == '__main__':
    main()  
