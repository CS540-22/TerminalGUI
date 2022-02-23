import tkinter as tk
from tkinter import ttk
import subprocess


# name conversion
#Label   lbl lbl_name
#Button  btn btn_submit
#Entry   ent ent_age
#Text    txt txt_notes
#Frame   frm frm_address


# Tab control class that allows you to add tabs and retrive tabs
class TabControl:
    def __init__(self, window):
        self.window = window
        self.tabs = {}
        self.tab_control = ttk.Notebook(window)

    def addTab(self, name):
        tab = ttk.Frame(self.tab_control)
        self.tab_control.add(tab, text=name, sticky="nw")
        self.tabs[name] = tab

    def getTabByName(self, name):
        return self.tabs[name]

    def pack(self, **options):
        self.tab_control.pack(options)

class Terminal:
    def __init__(self, window, tab):
        self.tab = tab
        self.window = window




    def enterCallback(self, event):
        out = ""
        try :
            out = subprocess.check_output(self.ent.get(), stderr=subprocess.STDOUT, shell=True).decode("utf-8")
        except:
            pass

        if (out == ""): out = "Command \"{}\" is not found".format(self.ent.get())
        self.text.config(text = out)


    def render(self):

        self.frame = tk.Frame(master=self.tab)

        pwd = subprocess.check_output("pwd", shell=True).decode("utf-8")[:-1] + ": "
        tk.Label(master=self.frame, text=pwd, fg="red").grid(column = 0, row = 0, padx=5)  
        self.ent = tk.Entry(master=self.frame, width=55)
        self.ent.grid(column = 1, row = 0)
        self.ent.bind('<Return>', self.enterCallback)
        self.text = tk.Label(master=self.frame, text="", justify="left")
        self.text.grid(column=0, row=1, sticky="w", padx=5)
        self.frame.pack(expand = True, fill="x", side="left")


def main():
    window = tk.Tk()
    window.title("Terminal GUI")
    window.geometry("800x500")

    style = ttk.Style(window)
    style.theme_use('classic')
    # ttk.Style(window).configure("TLABEL", foreground="red", background="white")

  
    

    tab_control = TabControl(window)
    tab_control.addTab("Terminal")
    tab_control.addTab("User Commands")
    tab_control.pack(expand=True, fill ="both")
    
    tab1 = tab_control.getTabByName("Terminal")
    tab2 = tab_control.getTabByName("User Commands")
      
    
    terminal = Terminal(window, tab1)
    terminal.render()
    ttk.Label(tab2,
              text ="Lets dive into the\
              world of computers").grid(column = 0,
                                        row = 0, 
                                        padx = 30,
                                        pady = 30)
  
    window.mainloop()











if __name__ == "__main__":
    main()
