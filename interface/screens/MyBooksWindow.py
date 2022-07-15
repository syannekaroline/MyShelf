from pathlib import Path
from tkinter import BOTTOM, CENTER, RIGHT, W, Y,X, Frame, Scrollbar, Tk, Canvas, Entry, Text, Button, ttk , PhotoImage
from tkinter import StringVar, Label, FLAT

from controller.database import query_database

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Aplicattion():
    def __init__(self):
        self.mybookswindow = Tk()
        icon = PhotoImage(file=relative_to_assets("Logo.png"))
        self.mybookswindow.iconphoto(False, icon)
        self.interface()
        self.Frame_Table()
        self.MyBooks_list()

    def back_to_home(self):
        from interface.screens.HomeWindow import HomeWindow
        self.mybookswindow.destroy()
        self.novaHome = HomeWindow()
        self.novaHome.generate_home_window()

    def go_to_CD_window(self):
        from interface.screens.ConfirmDeleteWindow import ConfirmDeleteWindow
        if self.Books_list.selection() != ():
            try: 
                self.labelError.destroy()
            except:
                pass
            self.ConfirmDeleteWindow = ConfirmDeleteWindow(self.Books_list)
            self.ConfirmDeleteWindow.generate_ConfirmDelete_window()
        else:
            try: 
                self.labelError.destroy()
            except:
                pass
            varError = StringVar()
            self.labelError = Label( self.mybookswindow, textvariable=varError, relief=FLAT, foreground="red", background="#2C0A59", font=("Georgia 14 bold"))
            varError.set(f"Error: select a book")
            self.labelError.pack()  


    def interface(self):
        self.mybookswindow.geometry("1300x700")
        self.mybookswindow.configure(bg = "#2C0A59")
        self.mybookswindow.maxsize(width=1300, height=700)#configura as dmensoes maximas da tela
        self.mybookswindow.minsize(width=400, height=170)

        self.canvas = Canvas(
            self.mybookswindow,
            self.mybookswindow.title("My Books"),
            bg = "#2C0A59",
            height = 700,
            width = 1297,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        #buttons
        self.button_image_icon = PhotoImage(
            file=relative_to_assets("icon.png"))

        self.button_icon = Button(
            image=self.button_image_icon,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            bg="#2C0A59",
            bd=0,
            activebackground="#2C0A60",
            command=self.back_to_home,
            cursor="hand2",
        )

        self.button_icon.place(
            x=1194.0,
            y=19.0,
        )
        self.button_image_search = PhotoImage(
                file=relative_to_assets("button_search.png"))

        self.button_search = Button(
            image=self.button_image_search,
            borderwidth=0,
            highlightthickness=0,
            command=self.searchBook,
            relief="sunken",
            cursor="hand2",
            activebackground="#2C0A59",
            bg="#2C0A59",
            bd=0
        )
        self.button_search.place(
            x=1195.0,
            y=193.0,
            width=40.3193359375,
            height=40.5035400390625
        )

        # #button delete

        self.mybookswindow.btn_inactivedelete = PhotoImage(file=relative_to_assets("button_delete.png"))
        self.mybookswindow.btn_activedelete = PhotoImage(file=relative_to_assets("button_deleteActive.png"))

        self.button_image_delete = PhotoImage(
            file=relative_to_assets("button_delete.png"))
        self.button_delete = Button(
            image=self.button_image_delete,
            borderwidth=0,
            highlightthickness=0,
            command=self.go_to_CD_window,
            bg = "#2C0A59",
            activebackground="#2C0A59",
            relief="sunken",
            cursor="hand2"
            
        )
        self.button_delete.place(
            x=378.0,
            y=207.0,

        )
        self.button_delete.bind("<Enter>", lambda e: self.button_delete.config(image=self.mybookswindow.btn_activedelete))
        self.button_delete.bind("<Leave>", lambda e: self.button_delete.config(image=self.mybookswindow.btn_inactivedelete))

        #button edit status 
        self.mybookswindow.btn_inactiveeditstatus = PhotoImage(file=relative_to_assets("button_editstatus.png"))
        self.mybookswindow.btn_activeeditstatus = PhotoImage(file=relative_to_assets("button_editstatusActive.png"))

        self.button_image_editstatus = PhotoImage(
            file=relative_to_assets("button_editstatus.png"))
        self.button_editstatus = Button(
            image=self.button_image_editstatus,
            borderwidth=0,
            highlightthickness=0,
            command=self.switch_to_read,
            bg = "#2C0A59",
            activebackground="#2C0A59",
            relief="sunken",
            cursor="hand2"

        )
        self.button_editstatus.place(
            x=218.0,
            y=207.0,
        )
        self.button_editstatus.bind("<Enter>", lambda e: self.button_editstatus.config(image=self.mybookswindow.btn_activeeditstatus))
        self.button_editstatus.bind("<Leave>", lambda e: self.button_editstatus.config(image=self.mybookswindow.btn_inactiveeditstatus))

        #button Show All
        self.mybookswindow.btn_inactiveShowAll = PhotoImage(file=relative_to_assets("button_ShowAll.png"))
        self.mybookswindow.btn_activeShowAll = PhotoImage(file=relative_to_assets("button_ShowAllActive.png"))

        self.button_image_ShowAll = PhotoImage(
            file=relative_to_assets("button_ShowAll.png"))

        self.button_ShowAll = Button(
            image=self.button_image_ShowAll,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_all_datas,
            bg = "#2C0A59",
            activebackground="#2C0A59",
            relief="sunken",
            cursor="hand2"
        )
        self.button_ShowAll.place(
            x=60.0,
            y=207.0,
        )

        self.button_ShowAll.bind("<Enter>", lambda e: self.button_ShowAll.config(image=self.mybookswindow.btn_activeShowAll))
        self.button_ShowAll.bind("<Leave>", lambda e: self.button_ShowAll.config(image=self.mybookswindow.btn_inactiveShowAll))

        #images

        self.image_image_MyBooks = PhotoImage(
            file=relative_to_assets("MyBooks.png"))
        self.image_1 = self.canvas.create_image(
            248.861328125,
            68.0,
            image=self.image_image_MyBooks
        )

        self.image_image_search = PhotoImage(
            file=relative_to_assets("image_search_MB.png"))
        self.image_search = self.canvas.create_image(
            1000.0,
            165.0,
            image=self.image_image_search
        )

        #input
        self.entry_image_search = PhotoImage(
            file=relative_to_assets("entry_search_2.png"))
        self.entry_bg_1 = self.canvas.create_image(
            990.5,
            215.5,
            image=self.entry_image_search
        )
        self.entry_search = Entry(
            bd=0,
            bg="#93679A",
            highlightthickness=0,
            justify="center",
            font=('Georgia 14')
        )
        self.entry_search.place(
            x=810.0,
            y=198.5,
            width=365.0,
            height=26.0
        )

        #tabela 
        
    def Frame_Table(self): 
        self.frame_MyBooksTable= Frame(self.mybookswindow,bd=5,bg="#2C0A59",highlightbackground="purple",highlightthickness=3)
        self.frame_MyBooksTable.place(relx=0.05,rely=0.34 ,relwidth=0.90,relheight=0.65)

    def MyBooks_list(self):

        self.Books_list= ttk.Treeview(self.frame_MyBooksTable,height=5,columns=("Title","Type","Author","Publisher","Publication date","Language","Start of Reading","End of Reading","Status"))

        self.Books_list.heading("#0",text="ID")
        self.Books_list.heading("#1",text="Type")
        self.Books_list.heading("#2",text="Title")
        self.Books_list.heading("#3",text="Author")
        self.Books_list.heading("#4",text="Publisher")
        self.Books_list.heading("#5",text="Publication date")
        self.Books_list.heading("#6",text="Language")
        self.Books_list.heading("#7",text="Start of Reading")
        self.Books_list.heading("#8",text="End of Reading" )
        self.Books_list.heading("#9",text="Status" )

        self.Books_list.column("#0", width=150,anchor=CENTER)
        self.Books_list.column("#1", width=100,anchor=CENTER)
        self.Books_list.column("#2", width=450,anchor=W)
        self.Books_list.column("#3", width=350,anchor=W)
        self.Books_list.column("#4", width=200,anchor=W)
        self.Books_list.column("#5", width=200,anchor=CENTER)
        self.Books_list.column("#6", width=200,anchor=W)
        self.Books_list.column("#7", width=200,anchor=CENTER)
        self.Books_list.column("#8", width=200,anchor=CENTER)
        self.Books_list.column("#9", width=260,anchor=CENTER)

        self.Books_list.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.98)

        #scroolbar
        self.yscroolList = Scrollbar(self.Books_list, orient='vertical')
        self.Books_list.configure(yscroll= self.yscroolList.set)
        self.yscroolList.pack(side=RIGHT,fill=Y)
        self.yscroolList.config(command= self.Books_list.yview)

        self.xscroolList = Scrollbar(self.Books_list, orient='horizontal')
        self.Books_list.configure(xscroll=self.xscroolList.set)
        self.xscroolList.pack(side=BOTTOM,fill=X) 
        self.xscroolList.config(command=self.Books_list.xview)
        #style
        self.style=ttk.Style()
        
        #pick a theme
        self.style.theme_use("alt")
        self.style.configure("Treeview", 
            background="#93679A",
            foreground="black",
            rowheight=25,
            fieldbackground= "#93679A"
                        
        )
        self.style.map('Treeview',
            background=[('selected','purple')]
        )

    def insert_datas(self):
        try:
            self.allDatas = query_database()
            for i, metadatas in enumerate(self.allDatas):
                self.Books_list.insert(parent='', index='end', iid=i,text=metadatas[0], values=metadatas[1:])
        except:
            pass 

    def show_all_datas(self):
        try: 
            self.labelError.destroy()
        except:
            pass
        finally:
            for item in self.Books_list.get_children():
                self.Books_list.delete(item)
            self.insert_datas()

    def deleteBook(self):
        from controller.database import remove_database
        books = self.Books_list.selection()
        for book in books:
            isbn = self.Books_list.item(book)["text"]
            remove_database(isbn)
            self.Books_list.delete(book)       

    def searchBook(self):
        from controller.database import search_database

        for item in self.Books_list.get_children():
            self.Books_list.delete(item)

        try: 
            self.labelError.destroy()
        except:
            pass
        
        
        search = self.entry_search.get()
        self.searchDatas = search_database(search)
        for i in range(0, len(self.searchDatas)):
            self.Books_list.insert(parent='', index='end', iid=i,text=self.searchDatas[i][0], values=self.searchDatas[i][1:])
        if self.searchDatas == []:
            var = StringVar()
            self.labelError = Label( self.mybookswindow, textvariable=var, relief=FLAT, foreground="red", background="#2C0A59", font=("Georgia 14 bold"))

            var.set(f"Error: nothing found for {search}")
            self.labelError.pack()  

    def switch_to_read(self):
        from controller.database import change_status
        try: 
            self.labelError.destroy()
        except:
            pass
        books = self.Books_list.selection()
        for book in books:
            isbn = self.Books_list.item(book)["text"]
            if self.Books_list.item(book)["values"][-1] != 'read':
                change_status(isbn)
        for item in self.Books_list.get_children():
            self.Books_list.delete(item)
        self.insert_datas()

    def generate_my_books_window(self):
        self.mybookswindow.resizable(False, False)
        self.mybookswindow.mainloop()