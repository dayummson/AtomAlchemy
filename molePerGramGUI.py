#importing modules

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from numpy import imag
from table_of_elements import table_of_elements as tb



#class for the entire interface

class MpgCalculatorGUI:

    #class variables
    def __init__(self):
        #description for the interface
        self.root = tk.Tk()
        self.root.title("MPG Calculator")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.config(bg="#f5f5f5")

        #label for the interface
        self.header = tk.Label(self.root, text="Example: C 1 H 2", font=('monospace', 15), bg='#f5f5f5')
        self.header.pack(padx=10, pady=10)

        #description for the textbox
        self.textBox = tk.Text(self.root, height=1, font=('monospace', 15))
        self.textBox.pack(padx=10, pady=10)
        
        #description for the image
        self.image_a = ImageTk.PhotoImage(Image.open(''))
        self.image_b = ImageTk.PhotoImage(Image.open(''))

        #buttons for calcution and clearing the console
        self.calcButton = tk.Button(self.root, text="Calculate", image=self.image_a)
        self.clearButton = tk.Button(self.root, text="Clear", image=self.image_b)
        self.calcButton.place(x=10, y=110, width=240, height=70)
        self.clearButton.place(x=250, y=110, width=240, height=70)

        
        

        self.root.mainloop()
    

mpgCalculatorGui = MpgCalculatorGUI()