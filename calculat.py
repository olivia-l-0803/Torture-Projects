from tkinter import *
import pygame
import time

pygame.init()
pygame.mixer.init()

app = Tk()
app.title("Calculator App")
app.geometry("400x600")







Screen = Label(app, text = "", font=("Courier New", 40), fg="Black")
Screen.pack(fill= "both", expand= 1)

ButtonFrame = Frame(app, background= "sky blue" )
ButtonFrame.pack(fill= "both", expand=TRUE)



def addnumber(whoclicked):
    x = Screen.cget(key="text")
    x = x + whoclicked.cget("text")
    Screen.config(text= x, fg= "black")
    
    check()

def enter():
    x = Screen.cget(key="text")
    b = str(x)
    b = b.replace("÷", "/")
    b = b.replace("x", "*")
    x = b
    try:
        
        answer=  str(eval(x))
        Screen.config(text= answer)
    except:
        Screen.config(text= "Invalid", fg = "red")

def backspace():
    x = Screen.cget(key="text")

    if x == "Invalid":
        x = ""
        Screen.config(text = x)
    else:
        
        x = x[:-1]
        Screen.config(text= x)

def check():
    x = Screen.cget(key="text")
    if "67" in x:
        calculatorsong1 = pygame.mixer.Sound("what is this diddy blud doing on the calculator (Sped Up).wav")
        fartnoise = pygame.mixer.Sound("67-brain-fart.wav")

        channel1 = pygame.mixer.Channel(0)  
        channel2 = pygame.mixer.Channel(1)
        channel2.set_volume(.3)
        
        
        channel1.play(calculatorsong1)
        channel2.play(fartnoise)
        time.sleep(10) 
        pygame.mixer.stop()
        
        
         




#Number Buttons
#row 1
Button1 = Button(ButtonFrame, text="1", overrelief= "ridge", font=("Courier New", 20), command= lambda: addnumber(Button1))
Button1.grid(column= 0 , row = 0, sticky= NSEW)
Button2 = Button(ButtonFrame, text="2", overrelief= "ridge", font=("Courier New", 20),  command= lambda: addnumber(Button2))
Button2.grid(column= 1  , row = 0, sticky= NSEW)
Button3 = Button(ButtonFrame, text="3", overrelief= "ridge", font=("Courier New", 20), command= lambda: addnumber(Button3))
Button3.grid(column= 2  , row = 0, sticky= NSEW)

#row 2
Button4 = Button(ButtonFrame, text="4", overrelief= "ridge", font=("Courier New", 20), command= lambda: addnumber(Button4))
Button4.grid(column= 0  , row = 1, sticky= NSEW)
Button5 = Button(ButtonFrame, text="5", overrelief= "ridge", font=("Courier New", 20),  command= lambda: addnumber(Button5))
Button5.grid(column= 1  , row = 1, sticky= NSEW)
Button6 = Button(ButtonFrame, text="6", overrelief= "ridge", font=("Courier New", 20), command= lambda: addnumber(Button6) )
Button6.grid(column= 2  , row = 1, sticky= NSEW)

#row 3
Button7 = Button(ButtonFrame, text="7", overrelief= "ridge",font=("Courier New", 20),  command= lambda: addnumber(Button7) )
Button7.grid(column= 0  , row = 2, sticky= NSEW)
Button8 = Button(ButtonFrame, text="8", overrelief= "ridge", font=("Courier New", 20), command= lambda: addnumber(Button8))
Button8.grid(column= 1  , row = 2, sticky= NSEW)
Button9 = Button(ButtonFrame, text="9", overrelief= "ridge", font=("Courier New", 20), command= lambda: addnumber(Button9))
Button9.grid(column= 2  , row = 2, sticky= NSEW)

#row 4
Button0 = Button(ButtonFrame, text="0", overrelief= "ridge", font=("Courier New", 20), command= lambda: addnumber(Button0))
Button0.grid(column= 1  , row = 3, sticky= NSEW)

#Function Buttons
Plusbutton = Button(ButtonFrame, text="+", overrelief= "ridge", font=("Courier New", 20), command= lambda: addnumber(Plusbutton))
Plusbutton.grid(column= 3  , row = 0, sticky= NSEW)
Minusbutton = Button(ButtonFrame, text="-", overrelief= "ridge", font=("Courier New", 20), command= lambda: addnumber(Minusbutton))
Minusbutton.grid(column= 3  , row = 1, sticky= NSEW)
Multiplybutton = Button(ButtonFrame, text="x", overrelief= "ridge", font=("Courier New", 20), command= lambda: addnumber(Multiplybutton))
Multiplybutton.grid(column= 3  , row = 2, sticky= NSEW)
Dividebutton = Button(ButtonFrame, text="÷", overrelief= "ridge", font=("Courier New", 20), command= lambda: addnumber(Dividebutton))
Dividebutton.grid(column= 3  , row = 3, sticky= NSEW)

Equalbutton = Button(ButtonFrame, text= "=", overrelief= "ridge", font=("Courier New", 20), command= enter)
Equalbutton.grid(column=2, row = 3, stick= NSEW)

deletebutton = Button(ButtonFrame, text= "Del", overrelief= "ridge", font=("Courier New", 15), command= backspace)
deletebutton.grid(column=0, row = 3, stick= NSEW)



ButtonFrame.grid_rowconfigure(0, weight=1)
ButtonFrame.grid_rowconfigure(1, weight=1)
ButtonFrame.grid_rowconfigure(2, weight=1)
ButtonFrame.grid_rowconfigure(3, weight=1)
 

ButtonFrame.grid_columnconfigure(0, weight=1)
ButtonFrame.grid_columnconfigure(1, weight=1)
ButtonFrame.grid_columnconfigure(2, weight=1)
ButtonFrame.grid_columnconfigure(3, weight=1)




app.mainloop()