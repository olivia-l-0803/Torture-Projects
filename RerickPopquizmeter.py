from tkinter import *
import pygame
import time




class Meterbar:
    def __init__(self, Amount = 100, Background):
        self.Amount = Amount
        self.Background = Background 
        
        


Window = Tk()
Window.title("Mr. Rerick Pop Quiz Meter")
Window.geometry("800x400")

Title = Label(Window, text= "Mr. Rerick's Pop Quiz Meter", font=("Courier New", 30), fg="Black")
Title.pack()









Window.mainloop()