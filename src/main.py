import tkinter as tk
from tkinter import ttk
import subprocess
from tkinter import *


# name conversion
#Label   lbl lbl_name
#Button  btn btn_submit
#Entry   ent ent_age
#Text    txt txt_notes
#Frame   frm frm_address

def on_configure(event, canvas):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    print("ok")
    canvas.configure(scrollregion=canvas.bbox('all'))




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
        self.texts = []
        self.entries = []



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

        # sleep(1)


        if arg == len(self.texts) - 1: self.newCommand()

        self.tab.update()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        self.canvas.yview_scroll(3000, "units")


        # self.canvas.configure(scrollregion=self.canvas.bbox('all'))

        # self.frame = tk.Frame(master=self.tab)

        # pwd = subprocess.check_output("pwd", shell=True).decode("utf-8")[:-1] + ": "
        # tk.Label(master=self.frame, text=pwd, fg="red").grid(column = 0, row =2, padx=5)  
        # self.ent = tk.Entry(master=self.frame, width=55)
        # self.ent.grid(column = 1, row = 2)
        # self.ent.bind('<Return>', lambda event, arg=1 : self.enterCallback(event, arg))
        # self.text = tk.Label(master=self.frame, text="", justify="left")
        # self.text.grid(column=0, row=3, sticky="w", padx=5)
        # self.frame.pack(expand = True, fill="x", side="left")

    def render(self):

        # self.frame = tk.Frame(master=self.tab)
        # self.frame = VerticalScrolledFrame(self.tab)
        # canvas_tab2 = tk.Canvas(self.tab, height=200, scrollregion=(0,0, 200,900))
        # canvas_tab2.create_window(0,0, window=self.tab)

        # scrollbar = ttk.Scrollbar(self.tab, orient=tk.VERTICAL)
        # scrollbar.pack(fill=tk.Y, side=tk.RIGHT)
        # scrollbar.config(command=canvas_tab2.yview)

        # canvas_tab2.config(yscrollcommand=scrollbar.set)
        # canvas_tab2.pack()


        canvas = tk.Canvas(self.tab, width = 770,height = 550, scrollregion = (0, 0, 300, 1000))
        canvas.pack(side=tk.LEFT)

        scrollbar = tk.Scrollbar(self.tab, command=canvas.yview)
        scrollbar.pack(side=tk.LEFT, fill='y', expand=True)

        canvas.configure(yscrollcommand = scrollbar.set)

        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        # canvas.configure(scrollregion=canvas.bbox('all'))
        canvas.bind('<Configure>', lambda event, canvas=canvas : on_configure(event, canvas))

        # --- put frame in canvas ---

        self.frame = tk.Frame(canvas)
        canvas.create_window((600, 0), window=self.frame)
        canvas.pack()
        self.canvas = canvas

        # self.canvas = canvas

        # self.scrollbar = tk.Scrollbar(self.frame, orient="vertical")
        # self.scrollbar.pack(side="right",fill="y")
        # self.scrollbar.config(command=tk.yview)

        self.newCommand()
        # self.newCommand()
        # self.newCommand()
        # self.newCommand()

        # self.newCommand()
        # self.newCommand()
        # self.newCommand()
        # pwd = subprocess.check_output("pwd", shell=True).decode("utf-8")[:-1] + ": "
        # tk.Label(master=self.frame, text=pwd, fg="red").grid(column = 0, row = 0, padx=5)  
        # self.ent = tk.Entry(master=self.frame, width=55)
        # self.ent.grid(column = 1, row = 0)
        # self.ent.bind('<Return>', lambda event, arg=1 : self.enterCallback(event,arg))
        # self.text = tk.Label(master=self.frame, text="", justify="left")
        # self.text.grid(column=0, row=1, sticky="w", padx=5)
        # self.frame.pack(expand = True, side="left")

    def newCommand(self):


        
        command_id = len(self.texts)
        row=command_id * 2


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
    tab_control.pack(expand=True, fill ="both")
    
    tab1 = tab_control.getTabByName("Terminal")
    tab2 = tab_control.getTabByName("User Commands")
    # tab1.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
      
    
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
