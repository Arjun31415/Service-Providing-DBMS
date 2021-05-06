from tkinter import*
from pubsub import pub
from tkinter import messagebox
import tables as tb

CustomerPage = None
EmployeePage = None
AdminPage = None
h = 600
w = 400


class Customer:

    def __init__(self, master=None):
        self.parent = master

        self.parent.geometry(str(w)+"x"+str(h))
        self.make_widgets()
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

    # ----------------------------------------------------------------

    def make_widgets(self):
        # put the widgets
        nothing = 0

    # ----------------------------------------------------------------

    def on_closing(self):
        global CustomerPage
        # if messagebox.askokcancel("Quit", "Do you want to signout?"):
        self.parent.destroy()
        CustomerPage = None
        """
                closes the window and sends a message to the main window
        """
        print(CustomerPage)
        pub.sendMessage("CustomerWindowClosed", arg1="data")
