
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from interface.screens import MyBooksWindow


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ConfirmDeleteWindow:
    def __init__(self, table):
        self.Books_list = table
        self.ConfirmDeleteWindow= Toplevel()
        icon = PhotoImage(file=relative_to_assets("Logo.png"))
        self.ConfirmDeleteWindow.iconphoto(False, icon)
        self.ConfirmDeleteWindow.geometry("500x300")
        self.ConfirmDeleteWindow.configure(bg = "#2C0A59")
        self.ConfirmDeleteWindow.title("Delete Confirm")

    def deleteBook(self):
        from controller.database import remove_database
        books = self.Books_list.selection()
        for book in books:
            isbn = self.Books_list.item(book)["text"]
            remove_database(isbn)
            self.Books_list.delete(book)
        self.ConfirmDeleteWindow.destroy()

    def generate_ConfirmDelete_window(self):

        canvas = Canvas(
            self.ConfirmDeleteWindow,
            bg = "#2C0A59",
            height = 300,
            width = 500,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)

        ConfirmDeleteWindowimage_image_borda = PhotoImage(
            file=relative_to_assets("image_borda.png"))
        ConfirmDeleteWindowimage_borda = canvas.create_image(
            250.0,
            150.0,
            image=ConfirmDeleteWindowimage_image_borda
        )

        image_image_deleteBook = PhotoImage(
            file=relative_to_assets("image_deleteBook.png"))
        image_deleteBook = canvas.create_image(
            249.0,
            55.0,
            image=image_image_deleteBook
        )

        image_image_confirmDelete = PhotoImage(
            file=relative_to_assets("image_confirmDelete.png"))
        image_confirmDelete = canvas.create_image(
            250.0,
            134.0,
            image=image_image_confirmDelete
        )

        self.ConfirmDeleteWindow.btn_cancelinactive = PhotoImage(file=relative_to_assets("button_cancel.png"))
        self.ConfirmDeleteWindow.btn_cancelactive = PhotoImage(file=relative_to_assets("button_cancelActive.png"))

        button_image_cancel = PhotoImage(
            file=relative_to_assets("button_cancel.png"))

        button_cancel = Button(
            self.ConfirmDeleteWindow,
            image=button_image_cancel,
            borderwidth=0,
            highlightthickness=0,
            bg="#2C0A59",
            bd=0,
            relief="sunken",
            cursor="hand2",
            activebackground="#2C0A59",
            command=lambda: self.ConfirmDeleteWindow.destroy() #print("button_cancel clicked") #
        )

        button_cancel.place(
            x=72.0,
            y=220.0,

        )
        
        button_cancel.bind("<Enter>", lambda e: button_cancel.config(image=self.ConfirmDeleteWindow.btn_cancelactive))
        button_cancel.bind("<Leave>", lambda e: button_cancel.config(image=self.ConfirmDeleteWindow.btn_cancelinactive))

        self.ConfirmDeleteWindow.btn_delete2inactive= PhotoImage(file=relative_to_assets("button_delete2.png"))
        self.ConfirmDeleteWindow.btn_delete2active = PhotoImage(file=relative_to_assets("button_deleteActive2.png"))

        button_image_delete2 = PhotoImage(
            file=relative_to_assets("button_delete2.png"))

        button_delete2 = Button(
            self.ConfirmDeleteWindow,
            image=button_image_delete2,
            borderwidth=0,
            highlightthickness=0,
            bg="#2C0A59",
            bd=0,
            relief="sunken",
            cursor="hand2",
            activebackground="#2C0A59",
            command=self.deleteBook
        )
        button_delete2.place(
            x=260.0,
            y=220.0,
        )

        button_delete2.bind("<Enter>", lambda e: button_delete2.config(image=self.ConfirmDeleteWindow.btn_delete2active))
        button_delete2.bind("<Leave>", lambda e: button_delete2.config(image=self.ConfirmDeleteWindow.btn_delete2inactive))

        self.ConfirmDeleteWindow.resizable(False, False)
        self.ConfirmDeleteWindow.mainloop()