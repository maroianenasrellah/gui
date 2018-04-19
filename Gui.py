from tkinter import *

class Gui:

    def __init__(self, root):
        tframe = Frame(root)
        tframe.pack(side='top')
        bframe = Frame(root)
        bframe.pack(side='bottom')
        self.txt = Text(tframe)
        self.txt.insert('0.0', 'Totally foobar')
        self.txt.pack()
        self.btn = Button(bframe, text='OK')
        self.btn.pack()


    def get_big_text(self, callback, title='', text=''):
        popup = Toplevel(height=160, width=180)
        popup.title(title)
        txtframe = Frame(popup)
        txtframe.pack()
        big_text = Text(txtframe)
        big_text.insert('0.0',text)
        big_text.pack()
        btnframe = Frame(popup)
        btnframe.pack()
        grab_text = Button(btnframe)
        grab_text.config(text="Done", command=lambda:callback(big_text.get('0.0', 'end')))
        grab_text.pack()

root=Tk()
root.title('Example')
foo = Gui(root)
foo.get_big_text(lambda x:print(x))
root.mainloop()
