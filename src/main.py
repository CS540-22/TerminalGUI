import tkinter as tk
from tkinter import ttk
import subprocess
from tkinter import *
import functools

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


        self.texts = []       # all the texts
        self.entries = []     # all the command entires to type in



    def enterCallback(self, event, arg):
        print(event, arg)
        out = ""
        ent = self.entries[arg]
        text = self.texts[arg]
        try :
            out = subprocess.check_output(ent.get(), stderr=subprocess.STDOUT, shell=True).decode("utf-8")
        except:
            pass

       
        if (out == ""): out = "Command \"{}\" is not found".format(ent.get())
        text.config(text = out)


        if arg == len(self.texts) - 1: self.newCommand()

        self.tab.update()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        self.canvas.yview_scroll(3000, "units")



    def bound_to_mousewheel(self, event):
        fp = functools.partial
        self.canvas.bind_all("<Button-5>", fp(self.on_mousewheel, scroll=1))
        self.canvas.bind_all("<Button-4>", fp(self.on_mousewheel, scroll=-1))
       

    def unbound_to_mousewheel(self, event):
        self.canvas.unbind_all("<Button-4>")
        self.canvas.unbind_all("<Button-5>")

    def on_mousewheel(self, scroll):
        self.canvas.yview_scroll(int(scroll), "units")


    def on_configure(self, event):
        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))


    def render(self):



        canvas = tk.Canvas(self.tab, width = 770,height = 550, scrollregion = (0, 0, 300, 1000))
        canvas.pack(side=tk.LEFT)

        scrollbar = tk.Scrollbar(self.tab, command=canvas.yview)
        scrollbar.pack(side=tk.LEFT, fill='y', expand=True)

        canvas.configure(yscrollcommand = scrollbar.set)

        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        canvas.bind('<Configure>', self.on_configure)
        
        # canvas.bind_all("<MouseWheel>", lambda event, canvas=canvas : on_mousewheel(event, canvas))

        # --- put frame in canvas ---
        self.frame = tk.Frame(canvas)

        canvas.bind('<Enter>', self.bound_to_mousewheel)
        canvas.bind('<Leave>', self.unbound_to_mousewheel)
        canvas.create_window((600, 0), window=self.frame)
        canvas.pack()
        self.canvas = canvas
        self.newCommand()
        

    def newCommand(self):

        # get row number
        command_id = len(self.texts)
        row=command_id * 2

        # create the new command prompt and new empty text.

        pwd = subprocess.check_output("pwd", shell=True).decode("utf-8")[:-1] + ": "
        tk.Label(master=self.frame, text=pwd, fg="red").grid(column = 0, row = row, padx=5)
        ent = tk.Entry(master=self.frame, width=55)
        ent.grid(column = 1, row = row)
        ent.bind('<Return>', lambda event, command_id=command_id : self.enterCallback(event,command_id))
        text = tk.Label(master=self.frame, text="", justify="left", wraplength=500)
        text.grid(column=0, columnspan=100, row=row + 1, sticky="w", padx=5)

        self.entries.append(ent)
        self.texts.append(text)
        

def main():
    window = tk.Tk()
    window.title("Terminal GUI")
    window.geometry("800x500")

    # window.resizable(width=False, height=False)

    style = ttk.Style(window)
    style.theme_use('classic')
    # ttk.Style(window).configure("TLABEL", foreground="red", background="white")

  
    

    tab_control = TabControl(window)
    tab_control.addTab("Terminal")
    tab_control.addTab("User Commands")
    tab_control.addTab("Pipe")
    tab_control.pack(expand=True, fill ="both")

    
    tab1 = tab_control.getTabByName("Terminal")
    tab2 = tab_control.getTabByName("User Commands")
    tab3 = tab_control.getTabByName("Pipe")
    # tab1.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
      
    
    terminal = Terminal(window, tab1)
    terminal.render()
    ttk.Label(tab2,
              text ="Lets dive into the\
              world of computers").grid(column = 0,
                                        row = 0, 
                                        padx = 30,
                                        pady = 30)

    ttk.Label(tab3,
              text ="Implement pipe here").pack()
  
    window.mainloop()





if __name__ == "__main__":
    main()
