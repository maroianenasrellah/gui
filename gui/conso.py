import tkinter as tk

def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, self.parent)
        
        self.vscroll = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.hscroll = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.console = tk.Text(self, wrap='none', width=60)
        
        self.console.config(yscrollcommand = self.vscroll.set)
        self.console.config(xscrollcommand = self.hscroll.set)
        self.vscroll.config(command = self.console.yview)
        self.hscroll.config(command = self.console.xview)
        
        self.console.grid(column=0,row=0, sticky=(tk.W, tk.N, tk.S, tk.E))
        self.vscroll.grid(column=1, row=0, sticky=(tk.E,tk.N,tk.S))
        self.hscroll.grid(column=0,row=1, sticky=(tk.E,tk.W,tk.S))
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.console.insert(tk.END, 'Started PIEFACE GUI\n*************************\n')
        self.console.config(state=tk.DISABLED) 
