from tkinter import*
from pubsub import pub
from tkinter import messagebox

#  Height and width of our window

h = 600
w = 400

# a global variable to keep track of the login window
login = None


class WelcomeWindow:

    def __init__(self, parent=None):
        self.parent = parent
        # self.pack()
        self.make_widgets()

    def make_widgets(self):

        self.parent.winfo_toplevel().title("Welcome")

        # THINK of a BETTER HEADING
        self.heading = Label(self.parent, text='Service Providing DBMS')

        # text labels
        self.lbl1 = Label(self.parent, text='Welcome')
        self.btn1 = Button(self.parent, text='Login')
        self.btn2 = Button(self.parent, text='Sign-Up')

        # bind left click on the login button to open the login screen
        self.btn1.bind('<Button-1>', self.login)

        # Create a listner for the even "login Window closed"
        pub.subscribe(self.listner, "LoginWindowClosed")

        # place the widgets
        self.heading.place(x=w/2, y=2/30*h, anchor='center')
        self.lbl1.place(x=w/2, y=75, anchor='center')
        self.btn1.place(x=100, y=150)
        self.btn2.place(x=200, y=150)

    def listner(self, arg1, arg2=None):
        """
        pubsub listener - opens main frame when otherFrame closes
        """
        self.show()

    def hide(self):
        self.parent.withdraw()

    def show(self):
        self.parent.update()
        self.parent.deiconify()

    def login(self, event):
        global login
        # if login is not null then create a login window otherwise focus the login window
        if not login:
            self.hide()
            login = Toplevel(self.parent)
            LoginWindow = Login(login)
        else:
            login.focus()


class Login:

    def __init__(self, master=None):
        self.root = master
        self.root.title("Login")
        self.root.geometry(str(w)+"x"+str(h))
        label = Label(self.root, text="This is a new Window")
        label.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        global login
        global root
        # if messagebox.askokcancel("Quit", "Do you want to quit?"):
        self.root.destroy()
        login = None
        """
            closes the window and sends a message to the main window
        """
        pub.sendMessage("LoginWindowClosed", arg1="data")


if __name__ == '__main__':
    #  a global variable to keep track of the root window
    global root
    root = Tk()
    root.geometry(str(w)+"x"+str(h)+"+200+200")
    Project = WelcomeWindow(root)

    root.mainloop()
