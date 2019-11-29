from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from sqlite3 import *
from tkcalendar import DateEntry

class LoginWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("TAPS")
        self.geometry("400x300")

        self.style = Style()

        self.style.configure('Header.TFrame', background = 'white')

        self.header_frame = Frame(self, style = 'Header.TFrame')
        self.header_frame.pack(fill = X)

        self.style.configure('Header.TLabel', background = 'white', foreground = 'red', font = (NONE, 25))

        self.header_label = Label(self.header_frame, text = "GALGOTIA BUS SERVICE", style = 'Header.TLabel')
        self.header_label.pack()


        self.style.configure('Content.TFrame', background='white')

        self.content_frame = Frame(self, style = 'Content.TFrame')
        self.content_frame.pack(fill = BOTH, expand = TRUE)

        self.login_frame = Frame(self.content_frame, style = 'Content.TFrame')
        self.login_frame.place(relx = .5, rely = .5, anchor = CENTER)

        self.style.configure('Login.TLabel', background='white', font=(NONE, 15))

        self.fromcity_label = Label(self.login_frame, text = "FROM CITY: ", style = 'Login.TLabel')
        self.fromcity_label.grid(row = 0, column = 0)
        self.fromcity_combobox=Combobox(self.login_frame,state='readonly',
                                        values=("Galgotia college","Galgotia university",
                                                "pari chowk","Botanical Garden"),font=(NONE,15),width=15)
        self.fromcity_combobox.grid(row=0,column=1,pady=5)
        self.fromcity_combobox.focus()


        self.tocity_label = Label(self.login_frame, text="TO CITY: ", style='Login.TLabel')
        self.tocity_label.grid(row=1, column=0)
        self.tocity_combobox = Combobox(self.login_frame, state='readonly',
                                          values=("Galgotia college", "Galgotia university",
                                                  "pari chowk", "Botanical Garden"), font=(NONE, 15), width=15)
        self.tocity_combobox.grid(row=1, column=1, pady=5)
        self.tocity_combobox.focus()

        self.style.configure('TButton', font = (NONE, 15))

        self.datetime_label=Label(self.login_frame,text="DATE: ",style= 'Login.TLabel')
        self.datetime_label.grid(row=2,column=0)
        self.datetime_entry=DateEntry(self.login_frame,font=(None,15),width=15, background='darkblue',
                    foreground='white', borderwidth=2)
        self.datetime_entry.grid(row=2,column=1,padx=10, pady=10)


        self.search_button = Button(self.login_frame, text = "SEARCH", width = 15)
        self.search_button.grid(row = 4, column = 1, pady = 5)

if __name__ == '__main__':
    login_window = LoginWindow()
    login_window.mainloop()
