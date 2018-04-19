#!/usr/bin/python3
import tkinter as tk
import os
fields = 'Last Name', 'First Name', 'Club', 'datemax'

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        self.label = tk.Label(self.frame, text="Enter un secteur:").pack()
        self.entry= tk.Entry(self.frame,bd=4)
        self.entry.pack()
        self.entry.focus()
        
##        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
##        self.button1.pack()

        self.button = tk.Button(self.frame, text = 'Cliquez ici', width = 10, command = self.new_reading,fg="red")
        self.button.pack(side="left")#,fill="both", expand=True
        
        self.frame.pack()
        self.master.geometry('800x480')
    
        self.exitButton  = tk.Button(self.frame, text = 'Exit', width = 6, command = self.exitProgram)
        self.exitButton.pack(side="right")#, fill="both", expand=True
        self.frame.pack()
        
    def exitProgram(self):
        print("Exit Button pressed")
        self.master.destroy()
        
    def new_writing(self):
        print("Writing..." )
     
    def new_reading(self):
        self.destroy()
 
        def setText(text):
            first_entry.delete(0,END)
            first_entry.insert(0,text)
            return
           
            
        print("Secteur: %s" % (self.entry.get()))
        
        self.label = tk.Label(self.frame, text=self.entry.get(),fg = "light green",bg = "red",font = "Helvetica 16 bold italic").pack()

        #group = tk.LabelFrame(self.master, text="Customer Details", pady=20)
        #group.pack(padx=10, pady=10)
    
        first_label = tk.LabelFrame(self.master, text="First Name")
        first_label.pack(padx=10, pady=10)
        
        first_entry = tk.Entry(first_label)
        first_entry .insert(0, 'First Name')
        first_entry.pack()

        
        second_label = tk.LabelFrame(self.master, text="Last Name")
        second_label.pack(padx=10, pady=10)
        
        second_entry = tk.Entry(second_label)
        second_entry.insert(0, 'Last Name')
        second_entry.pack()

        Third_label = tk.LabelFrame(self.master, text="Club")
        Third_label.pack(padx=10, pady=10)
        
        Third_entry = tk.Entry(Third_label)
        Third_entry.insert(0, 'club')
        Third_entry.pack()

        #v = StringVar(self.master, value='default text')
        #e = tk.Entry(self.master, textvariable=v)
        l= tk.LabelFrame(self.master, text="date")
        l.pack(padx=10, pady=10)
       # e = tk.Entry(self.master)
        e = tk.Entry(l)
        e.insert(0, '20180422')
        e.pack()

        self.button = tk.Button(self.master, text = 'Valider', width = 10, command = self.new_writing,fg="green")
        self.button.pack()

##        self.text=tk.Text(self.frame)
##        self.text.pack(side=tk.TOP,fill=tk.BOTH,expand=1)
##        #self.text.pack()
##        self.text.height=10

 
        
##    def new_window(self):
##        self.newWindow = tk.Toplevel(self.master)
##        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
        self.master.geometry('800x480')
   
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
