from distutils.log import info
from email.mime import image
from hashlib import new
from itertools import count
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Scrollbar, font, Label, ttk, LEFT, BOTTOM, RIGHT, TOP, X, Y, StringVar, FLAT
from tkinter.tix import ButtonBox
import tkinter
import webbrowser
import asyncio
from controller.request import request, request_google_books
from PIL import Image, ImageTk
from urllib.request import urlopen
import threading
from tkinter import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class SearchWindow:

    def __init__(self):
        # Assets to LoadingGif
        self.framelist = []      # List to hold all the frames
        self.frame_index = 0 
        self.count = 0
        self.flag = True

        self.search_window = Tk()
        self.thread = threading.Thread(target= self.search_keyword)
        self.var = StringVar()
        icon = PhotoImage(file=relative_to_assets("Logo.png"))
        self.search_window.iconphoto(False, icon)
        self.search_window.title("Search")
        self.search_window.geometry("1300x700")
        self.search_window.configure(bg = "#2C0A59")
    

    def animate_gif(self, count=0):  
        try:
            if self.thread.is_alive() == True:
                if count == 0 and self.flag == True:
                    self.l1 = tkinter.Label(self.search_window, bg="#2C0A59", image='' )
                    self.l1.place(x=650, y=150)
                    self.flag=False

                count += 1
                self.l1.config(image=self.framelist[count])
                    
                if count > self.last_frame - 1:
                    count = 0  
                #recall animate_gif method    
                self.l1.after(50, lambda: self.animate_gif(count=count))
            else:
                self.l1.destroy()
                self.thread = threading.Thread(target=self.search_keyword)
        except:
            self.thread = threading.Thread(target=self.search_keyword)
        
    def back_to_home(self):
        if self.thread.is_alive() == False:
            from interface.screens.HomeWindow import HomeWindow
            self.search_window.destroy()
            self.novaHome = HomeWindow()
            self.novaHome.generate_home_window()

    def open_url(self, url):
        webbrowser.open(url, new=0)
        lambda url=url: self.open_url(url)

    async def renders_infos_book(self, books):
        try:
            for i in range(0, len(self.listFrames)):
                self.listFrames[i].destroy()
        except:
            pass

        self.listFrames = list()
        # self.listSubCanvas = list()
        for i in range(0,len(books)):
            self.listFrames.append(None)
            # self.listSubCanvas.append(None)
        counter = 1
        for book in books:
            if counter == 1:
                self.listFrames[counter-1]=Frame(self.search_window, width=160, height=50)
                self.listFrames[counter-1].place(x=160, y=230)

                xscrollbar = ttk.Scrollbar(self.listFrames[counter-1], orient=HORIZONTAL)          
                xscrollbar.pack(side=BOTTOM,fill=X)#ipadx=76,ipady=76,pady=0,padx=0

                # yscrollbar = ttk.Scrollbar(self.listFrames[counter-1], orient=VERTICAL)          
                # yscrollbar.pack(side=RIGHT,fill=Y)#ipadx=76,ipady=76,pady=0,padx=0
                
                books_box=Listbox(self.listFrames[counter-1], width=18, height=8,bg="#93679A",xscrollcommand=xscrollbar.set,font=("Georgia 10 bold"),fg="#2C0A59",selectbackground="purple", cursor="hand2")#yscrollcommand=yscrollbar.set,
                books_box.pack(in_=self.listFrames[counter-1])

                xscrollbar.config(command=books_box.xview)
                # yscrollbar.config(command=books_box.yview)
                
                try:
                    books_box.insert(END,f"TITLE: {book['title']}")
          
                except:
                    pass
                try:
                    books_box.insert(END,f"SUBTITLE: {book['subtitle']}")
                except:
                    pass
                try:
                    books_box.insert(END,f"AUTHORS: {book['authors']}")
                except:
                    pass
                try:
                    books_box.insert(END,f"PUBLISHER: {book['publisher']}")
                except:
                    pass
                try:
                    books_box.insert(END,f"CATEGORIES: {book['categories']}")#, relief=FLAT, foreground="purple", font=("Georgia 10 bold"))
                except:
                    pass
                try:
                    books_box.insert(END,f"ISBN: {book['isbn']}")#, relief=FLAT, foreground="purple", font=("Georgia 10 bold"))
                   
                except:
                    pass
                try:
                    testebutton=Button(self.listFrames[counter-1],width=15,height=1,text="know more",font=("Georgia 10 bold"),foreground="black",command=lambda url=book['previewLink']: self.open_url(url), bg="purple", cursor="hand2")
                    testebutton.pack(side=BOTTOM,fill='x')
                except:
                    pass         

            elif counter == 5:

                self.listFrames[counter-1]=Frame(self.search_window, width=170, height=170)
                self.listFrames[counter-1].place(x=160, y=450)

                xscrollbar = ttk.Scrollbar(self.listFrames[counter-1], orient=HORIZONTAL)          
                xscrollbar.pack(side=BOTTOM,fill=X)#ipadx=76,ipady=76,pady=0,padx=0
                # yscrollbar = ttk.Scrollbar(self.listFrames[counter-1], orient=VERTICAL)          
                # yscrollbar.pack(side=RIGHT,fill=Y)#ipadx=76,ipady=76,pady=0,padx=0
            
                books_box=Listbox(self.listFrames[counter-1], width=18, height=8,bg="#93679A",xscrollcommand=xscrollbar.set,font=("Georgia 10 bold"),fg="#2C0A59",selectbackground="purple", cursor="hand2")#yscrollcommand=yscrollbar.set,
                books_box.pack(in_=self.listFrames[counter-1])

                xscrollbar.config(command=books_box.xview)
                # yscrollbar.config(command=books_box.yview)
                


                # selfLink, title, subtitle, authors, publisher, categories, isbn
                try:
                    books_box.insert(END,f"TITLE: {book['title']}")
          
                except:
                    pass
                try:
                    books_box.insert(END,f"SUBTITLE: {book['subtitle']}")
                except:
                    pass
                try:
                    books_box.insert(END,f"AUTHORS: {book['authors']}")
                except:
                    pass
                try:
                    books_box.insert(END,f"PUBLISHER: {book['publisher']}")
                except:
                    pass
                try:
                    books_box.insert(END,f"CATEGORIES: {book['categories']}")#, relief=FLAT, foreground="purple", font=("Georgia 10 bold"))
                except:
                    pass
                try:
                    books_box.insert(END,f"ISBN: {book['isbn']}")#, relief=FLAT, foreground="purple", font=("Georgia 10 bold"))
                   
                except:
                    pass
                try:
                    testebutton=Button(self.listFrames[counter-1],width=15,height=1,text="know more",font=("Georgia 10 bold"),foreground="black",command=lambda url=book['previewLink']: self.open_url(url), bg="purple", cursor="hand2")
                    testebutton.pack(side=BOTTOM,fill='x')
                except:
                    pass  

            else:
                if counter > 1 and counter < 5:
                    x = 160 + ((counter-1) * 320)
                    y = 230
                else:
                    x = 160 + ((counter - 5) * 320)
                    y = 450

                #scrollbar in frame

                self.listFrames[counter-1]=Frame(self.search_window, width=170, height=170)
                self.listFrames[counter-1].place(x=x, y=y)

                xscrollbar = ttk.Scrollbar(self.listFrames[counter-1], orient=HORIZONTAL)          
                xscrollbar.pack(side=BOTTOM,fill=X)#ipadx=76,ipady=76,pady=0,padx=0
                # yscrollbar = ttk.Scrollbar(self.listFrames[counter-1], orient=VERTICAL)          
                # yscrollbar.pack(side=RIGHT,fill=Y)#ipadx=76,ipady=76,pady=0,padx=0
                

                books_box=Listbox(self.listFrames[counter-1], width=18, height=8,bg="#93679A",xscrollcommand=xscrollbar.set,font=("Georgia 10 bold"),fg="#2C0A59",selectbackground="purple", cursor="hand2")#,yscrollcommand=yscrollbar.set
                books_box.pack(in_=self.listFrames[counter-1])

                xscrollbar.config(command=books_box.xview)
                # yscrollbar.config(command=books_box.yview)
                

                # selfLink, title, subtitle, authors, publisher, categories, isbn
                try:
                    books_box.insert(END,f"TITLE: {book['title']}")
                except:
                    pass
                try:
                    books_box.insert(END,f"SUBTITLE: {book['subtitle']}")
                except:
                    pass
                try:
                    books_box.insert(END,f"AUTHORS: {book['authors']}")
                except:
                    pass
                try:
                    books_box.insert(END,f"PUBLISHER: {book['publisher']}")
                except:
                    pass
                try:
                    books_box.insert(END,f"CATEGORIES: {book['categories']}")#, relief=FLAT, foreground="purple", font=("Georgia 10 bold"))
                except:
                    pass
                try:
                    books_box.insert(END,f"ISBN: {book['isbn']}")#, relief=FLAT, foreground="purple", font=("Georgia 10 bold"))
                   
                except:
                    pass
                try:
                    testebutton=Button(self.listFrames[counter-1],width=15,height=1,text="know more",font=("Georgia 10 bold"),foreground="black",command=lambda url=book['previewLink']: self.open_url(url), bg="purple", cursor="hand2")
                    testebutton.pack(side=BOTTOM,fill='x')
                except:
                    pass 

            counter += 1 
    async def renders_image_book(self, books):
        try:
            for i in range(0, len(self.listLabels)):
                self.listLabels[i].destroy()
        except:
            pass
        counter = 1

        counter = 1
        self.listLabels = list()
        for i in range(0,len(books)):
            self.listLabels.append(None)
        for book in books:
            if counter == 1:
                try:
                    imageUrl = book["imageLink"]
                    u = urlopen(imageUrl)
                    raw_data = u.read()
                    u.close()
                    self.listLabelImage = list()
                    photo = ImageTk.PhotoImage(data=raw_data)
                    self.listLabels[counter - 1] = Label(image=photo, background="#2C0A59")
                    self.listLabels[counter - 1].image = photo
                    self.listLabels[counter - 1].place(x=30, y=230)
                except:
                    photo = PhotoImage(file=relative_to_assets("noImageAvailable.png"))
                    self.listLabels[counter - 1] = Label(image=photo, background="#2C0A59")
                    self.listLabels[counter -1].image = photo
                    self.listLabels[counter - 1].place(x=30, y=230)
            elif counter == 5:

                try:
                    imageUrl = book["imageLink"]
                    u = urlopen(imageUrl)
                    raw_data = u.read()
                    u.close()

                    photo = ImageTk.PhotoImage(data=raw_data)
                    self.listLabels[counter - 1] = Label(image=photo, background="#2C0A59")
                    self.listLabels[counter - 1].image = photo
                    self.listLabels[counter - 1].place(x=30, y=450)
                except:
                    photo = PhotoImage(file=relative_to_assets("noImageAvailable.png"))
                    self.listLabels[counter - 1] = Label(image=photo, background="#2C0A59")
                    self.listLabels[counter - 1].image = photo
                    self.listLabels[counter - 1].place(x=30, y=450)
            else:

                if counter > 1 and counter < 5:
                    x = 30 + ((counter-1) * 320)
                    y = 230
                else:
                    x = 30 + ((counter - 5) * 320)
                    y = 450
                try:
                    imageUrl = book["imageLink"]
                    u = urlopen(imageUrl)
                    raw_data = u.read()
                    u.close()

                    photo = ImageTk.PhotoImage(data=raw_data)
                    self.listLabels[counter - 1] = Label(image=photo, background="#2C0A59")
                    self.listLabels[counter - 1].image = photo
                    self.listLabels[counter - 1].place(x=x, y=y)
                except:
                    photo = PhotoImage(file=relative_to_assets("noImageAvailable.png"))
                    self.listLabels[counter - 1] = Label(image=photo, background="#2C0A59")
                    self.listLabels[counter -1].image = photo
                    self.listLabels[counter - 1].place(x=x, y=y)
            counter += 1
        self.flag = True

    def search_keyword(self):
        keyword = self.entry_search.get()
        books = asyncio.run(request_google_books(keyword))
        try:
            for i in range(0, len(self.listFrames)):
                self.listFrames[i].destroy()
        except:
            pass
        try: 
            self.label.destroy()
        except:
            pass
        if type(books) != list:
            try:
                for i in range(0, len(self.listLabels)):
                    self.listLabels[i].destroy()
            except:
                pass
            try: 
                self.label.destroy()
            except:
                pass
            finally:
                self.var.set(f"Error: {books}")
                self.label = Label( self.search_window, textvariable=self.var, relief=FLAT, background="#2C0A59", foreground="red", font=("Georgia 14 bold"))
                self.label.pack()
                self.flag = True
        else:
            asyncio.run(self.renders_infos_book(books))
            asyncio.run(self.renders_image_book(books))



    def generate_search_window(self):
        self.canvas = Canvas(
            self.search_window,
            bg = "#2C0A59",
            height = 700,
            width = 1300,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        button_image_icon = PhotoImage(
            file=relative_to_assets("icon.png"))
        button_icon = Button(
            image=button_image_icon,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            bg="#2C0A59",
            bd=0,
            activebackground="#2C0A60",
            command=self.back_to_home,
            cursor="hand2",
        )
        button_icon.place(
            x=1197.0,
            y=19.0,
        )

        image_image_search = PhotoImage(
            file=relative_to_assets("image_search.png"))
        
        self.canvas.create_image(
            312.0,
            59.0,
            image=image_image_search
        )

        image_image_isbn = PhotoImage(
            file=relative_to_assets("keywordSearch.png"))
        
        self.canvas.create_image(
            240.0,
            129.0,
            image=image_image_isbn
        )

        entry_image_search = PhotoImage(
            file=relative_to_assets("entry_search.png"))
        
        self.canvas.create_image(
            235.5,
            180.5,
            image=entry_image_search
        )

        self.entry_search = Entry(
            bd=0,
            bg="#93679A",
            highlightthickness=0,
            justify="center",
            font=('Georgia 20')
        )

        self.entry_search.place(
            x=65.5,
            y=161.5,
            width=350.0,
            height=30.75,
        )

        button_image_search = PhotoImage(
            file=relative_to_assets("button_search.png"))
        self.button_search = Button(
            image=button_image_search,
            borderwidth=0,
            highlightthickness=0,
            command=self.animate_gif,
            relief="sunken",
            cursor="hand2",
            activebackground="#2C0A59",
            bg="#2C0A59",
            bd=0,   
        )
        self.button_search.place(
            x=450.0,
            y=162.0,
            width=40.3193359375,
            height=37.80328369140625
        )
        self.button_search.bind("<Button-1>", lambda e: self.thread.start())
        
        while True:
            try:
                # Read a frame from GIF file
                part = 'gif -index {}'.format(self.frame_index)
                frame = PhotoImage(file=relative_to_assets('loading.gif'), format=part)
            except:
                self.last_frame = self.frame_index - 1    # Save index for last frame
                break               # Will break when GIF index is reached
            self.framelist.append(frame)
            self.frame_index += 1 

        self.search_window.resizable(False, False)

        self.search_window.mainloop()
