import tkinter as tk
from tkinter import ttk
import webbrowser

root = tk.Tk()
root.title('RFID READER')

label1 = ttk.Label(root, text='ENTRER UN SECTEUR')
label1.grid(row=0, column=0)
entry1 = ttk.Entry(root, width=50)
entry1.grid(row=0, column=1)
b1 =ttk.Button(root, text="QUIT", fg="red",command=quit)
