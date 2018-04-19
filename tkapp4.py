import tkinter as tk

class CustomDialog(object):
    def __init__(self, parent, title="Enter a paragraph", default_text=""):
        self.parent = parent
        self.title = title
        self.default = default_text

    def show(self):
        self.popup = tk.Toplevel(self.parent)
        self.popup.title(self.title)
        txtframe = tk.Frame(self.popup)
        txtframe.pack()
        self.big_text = tk.Text(txtframe)
        self.big_text.insert('1.0',self.default)
        self.big_text.pack()
        btnframe = tk.Frame(self.popup)
        btnframe.pack()
        grab_text = tk.Button(btnframe)
        grab_text.config(text="Done", command=self.done)
        grab_text.pack()

        # make sure our "done" method gets called even if the
        # user destroys the window
        self.popup.wm_protocol("WM_DELETE_WINDOW", self.done)

        # wait for the window to be destroyed
        root.wait_window(self.popup)
        return self.data

    def done(self, *args):
        # get the data from the window, then destroy
        # the window and return to the caller
        self.data = self.big_text.get("1.0", "end-1c")
        self.popup.destroy()

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        b = tk.Button(self, text="Get Input", command=self.go)
        b.pack()

    def go(self):
        dialog = CustomDialog(self, default_text="totally foobar")
        result = dialog.show()
        print ("result:", result)


if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
