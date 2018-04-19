from tkinter import *
import Tkinter
import tkinter.font as tkFont
#import RPi.GPIO as GPIO

win = Tk()

myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')

def start():
    print("LED button pressed")
    ledButton["text"] ="Scanning..."

def exitProgram():
    print("Exit Button pressed")
    win.quit()	


win.title("First GUI")

win.geometry('800x480')

exitButton  = Button(win, text = "Exit", font = myFont, command = exitProgram, height =2 , width = 6) 

exitButton.pack(side = BOTTOM)


ledButton = Button(win, text = "Start The Program", font = myFont, command = start, height = 2, width =16 )
ledButton.pack()

mainloop()
