
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Frame, Scrollbar, Tk, Canvas, Entry, Text, Button, ttk , PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


mybookswindow = Tk()
class Aplicattion():
    def __init__(self):
        self.mybookswindow=mybookswindow
        self.interface()
        self.Frame_Table()
        self.MyBooks_list()
        self.mybookswindow.resizable(True, True)
        self.mybookswindow.mainloop()

    def interface(self):
        self.mybookswindow.geometry("1300x700")
        self.mybookswindow.configure(bg = "#2C0A59")
        self.mybookswindow.maxsize(width=1300, height=700)#configura as dmensoes maximas da tela
        self.mybookswindow.minsize(width=400, height=170)


        self.canvas = Canvas(
            mybookswindow,
            mybookswindow.title("Mybooks"),
            bg = "#2C0A59",
            height = 700,
            width = 1297,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        self.button_image_home = PhotoImage(
            file=relative_to_assets("button_home.png"))

        self.button_home = Button(
            image=self.button_image_home,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_home clicked"),
            bg = "#2C0A59",
            activebackground="#2C0A59",
            bd=0,
            relief="sunken",
            cursor="hand2",
        )

        self.button_home.place(
            x=1191.0,
            y=21.0
        )

        self.image_image_MyBooks = PhotoImage(
            file=relative_to_assets("MyBooks.png"))
        image_1 = self.canvas.create_image(
            248.861328125,
            68.0,
            image=self.image_image_MyBooks
        )
        
    def Frame_Table(self): 
        self.frame_MyBooksTable= Frame(self.mybookswindow,bd=5,bg="#2C0A59",highlightbackground="purple",highlightthickness=3)
        self.frame_MyBooksTable.place(relx=0.05,rely=0.34 ,relwidth=0.90,relheight=0.65)
    def MyBooks_list(self):

        self.Books_list= ttk.Treeview(self.frame_MyBooksTable,height=5,columns=("Title","Type","Author","Publisher","Publication date","Start of Reading","End of Reading","Status"))#"Status"

        self.Books_list.heading("#0",text="ID")
        self.Books_list.heading("#1",text="Title")
        self.Books_list.heading("#2",text="Type")
        self.Books_list.heading("#3",text="Author")
        self.Books_list.heading("#4",text="Publisher")
        self.Books_list.heading("#5",text="Publication date")
        self.Books_list.heading("#6",text="Start of Reading")
        self.Books_list.heading("#7",text="End of Reading" )
        self.Books_list.heading("#8",text="Status" )

        self.Books_list.column("#0", width=150)
        self.Books_list.column("#1", width=150)
        self.Books_list.column("#2", width=150)
        self.Books_list.column("#3", width=150)
        self.Books_list.column("#4", width=150)
        self.Books_list.column("#5", width=150)
        self.Books_list.column("#6", width=150)
        self.Books_list.column("#7", width=150)
        self.Books_list.column("#8", width=150)

        self.Books_list.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.98)

        self.scroolList = Scrollbar(self.frame_MyBooksTable, orient='vertical')
        self.Books_list.configure(yscroll=self.scroolList.set)

        self.xscroolList = Scrollbar(self.frame_MyBooksTable, orient='horizontal')
        # self.Books_list.configure(yscroll=self.xscroolList.set)

        self.scroolList.place(relx=0.98, rely=0.01, relwidth=0.01, relheight=0.98)

        # self.xscroolList.place(relx=0.01, rely=0.99, relwidth=0.99, relheight=0.1)        
Aplicattion()  