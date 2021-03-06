from customer_pages import*
from employee_pages import*
from admin_pages import*
##################################################################################
#  Height and width of our window

h = 400
w = 400

# a global variable to keep track of the login window
login = None
signup = None


##################################################################################


class WelcomeWindow:
    # ----------------------------------------------------------------

    def __init__(self, parent=None):
        self.parent = parent
        # self.pack()
        self.make_widgets()

    # ----------------------------------------------------------------

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
        self.btn2.bind('<Button-1>', self.signup)

        # Create a listner for the event "login Window closed"
        pub.subscribe(self.listner, "LoginWindowClosed")

        # Create a listner for the event "login Window closed"
        pub.subscribe(self.listner, "SignupWindowClosed")
        pub.subscribe(self.listner, "CustomerWindowClosed")
        pub.subscribe(self.listner, "EmployeeWindowClosed")
        pub.subscribe(self.listner, "AdminWindowClosed")

        # place the widgets
        self.heading.place(x=w/2, y=2/30*h, anchor='center')
        self.lbl1.place(x=w/2, y=75, anchor='center')
        self.btn1.place(x=140, y=150)
        self.btn2.place(x=200, y=150)

    # ----------------------------------------------------------------

    def listner(self, arg1, arg2=None):
        """
        pubsub listener - opens main frame when otherFrame closes
        """
        self.show()

    # ----------------------------------------------------------------

    def hide(self):
        self.parent.withdraw()

    # ----------------------------------------------------------------

    def show(self):
        self.parent.update()
        self.parent.deiconify()

    # ----------------------------------------------------------------

    def login(self, event):
        global login
        # if login is not null then create a login window otherwise focus the login window
        if not login:
            self.hide()
            login = Toplevel(self.parent)
            Login(login)
        else:
            login.focus()

    # ----------------------------------------------------------------

    def signup(self, event):
        global signup
        # if signup is not null then create a signup window otherwise focus the sign window
        if not signup:
            self.hide()
            signup = Toplevel(self.parent)
            Signup(signup)
        else:
            signup.focus()

##################################################################################


class Login:
    # ----------------------------------------------------------------
    def __init__(self, master=None):
        self.root = master

        self.root.geometry(str(w)+"x"+str(h))
        self.make_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        pub.subscribe(self.force_close, "CustomerWindowClosed")
        pub.subscribe(self.force_close, "EmployeeWindowClosed")
        pub.subscribe(self.force_close, "AdminWindowClosed")

    # ----------------------------------------------------------------
    def listner(self, arg1, arg2=None):
        """
        pubsub listener - opens main frame when otherFrame closes
        """
        self.show()
    # -----------------------------------------------------------------

    def make_widgets(self):
        self.root.title("Login")
        heading = Label(self.root, text="Login Window", font=("Arial", 16))
        heading.pack()
        self.username = Entry(self.root, bg='white', font=("Arail", 14))

        # Email Entry field
        self.username.place(x=160/400 * w, y=h/6)
        usr_label = Label(self.root, text="Enter Email:",
                          font=("Times", 14),
                          anchor='center'
                          )
        usr_label.place(x=25/400*w, y=h/6)

        # Password label
        Label(self.root, text="Enter Password:",
              font=("Times", 14),
              anchor='center'
              ).place(x=25, y=(h/6)+35)

        # password entry field
        self.password = Entry(self.root, bg='white',
                              font=('Arial', 14),
                              show='*',
                              )
        self.password.place(x=160/400*w, y=(h/6)+35)

        Submit = Button(self.root, text='Submit')
        Submit.place(x=0.75*w, y=h/2)
        Submit.bind('<Button-1>', self.authenticate)

    # ----------------------------------------------------------------

    def hide(self):
        self.root.withdraw()

    # ----------------------------------------------------------------

    def show(self):
        self.root.update()
        self.root.deiconify()

    def authenticate(self, event):
        """
            authenticate the login
        """
        # the result of the entered details
        res = tb.auth_login(self.username.get(), self.password.get())
        if not res:
            messagebox.showinfo("Error", "Username/Password is incorrect")
        else:
            self.login_username = self.username.get()
            self.next_page(person=res)

    # ----------------------------------------------------------------

    def next_page(self, person):

        print("Person= ", person)
        if(person == "c"):
            self.hide()
            Customer(Toplevel(self.root), self.login_username)
        elif(person == "e"):
            self.hide()
            Employee(Toplevel(self.root), self.login_username)
        elif(person == "a"):
            self.hide()
            Admin(master=Toplevel(self.root), username=self.login_username)
            #    CustomerPage.focus()

    # ----------------------------------------------------------------

    def on_closing(self):
        global login

        # if messagebox.askokcancel("Quit", "Do you want to quit?"):
        self.root.destroy()
        login = None
        """
            closes the window and sends a message to the main window
        """
        pub.sendMessage("LoginWindowClosed", arg1="data")

    # ----------------------------------------------------------------

    def force_close(self, arg1, arg2="None"):
        global login

        # if messagebox.askokcancel("Quit", "Do you want to quit?"):
        self.root.destroy()
        login = None

    # ----------------------------------------------------------------


##################################################################################
""" 
    ONLY CUSTOMERS CAN SIGN UP
    EMPLOYEE SIGNUP WILL BE MANAGED BY ADMIN
"""


class Signup:
    # ----------------------------------------------------------------
    def __init__(self, master=None):
        self.sgup = master

        self.sgup.geometry(str(w)+"x"+str(h))
        self.make_widgets()
        self.sgup.protocol("WM_DELETE_WINDOW", self.on_closing)

    # ----------------------------------------------------------------
    def make_widgets(self):
        self.sgup.title("Sign-Up")
        heading = Label(self.sgup, text="Signup Window", font=("Arial", 16))
        heading.pack()
        self.username = Entry(self.sgup, bg='white', font=("Arail", 14))
        self.username.place(x=160/400 * w, y=h/6)
        usr_label = Label(self.sgup, text="Enter Username:",
                          font=("Times", 14),
                          anchor='center'
                          )
        usr_label.place(x=25/400*w, y=h/6)

        # Password label
        Label(self.sgup, text="Enter Password:",
              font=("Times", 14),
              anchor='center'
              ).place(x=25, y=(h/6)+35)
        self.password = Entry(self.sgup, bg='white',
                              font=('Arial', 14),
                              show='*',
                              )
        self.password.place(x=160/400*w, y=(h/6)+35)

        # Confirm Password label
        Label(self.sgup, text="Confirm Password:",
              font=("Times", 14),
              anchor='center'
              ).place(x=8, y=(h/6)+70)
        self.conf_password = Entry(self.sgup, bg='white',
                                   font=('Arial', 14),
                                   show='*',
                                   )
        self.conf_password.place(x=160/400*w, y=(h/6)+70)

        Submit = Button(self.sgup, text='Submit')
        Submit.place(x=0.75*w, y=h/2)
        Submit.bind('<Button-1>', self.authenticate)

    # ----------------------------------------------------------------

    def authenticate(self, event):
        """
        authenticate the signup
        """
        # the result of the entered details
        if self.password.get() != self.conf_password.get():
            messagebox.showinfo("Error", "Password fields do not match")
            return

        res = tb.auth_signup(self.username.get(),
                             self.password.get(), "c")
        if not res:
            messagebox.showinfo("Error", "Account already Exists")
            return
        else:
            messagebox.showinfo("Success", "Account Created")

    # ----------------------------------------------------------------

    def on_closing(self):
        global signup

        # if messagebox.askokcancel("Quit", "Do you want to quit?"):
        self.sgup.destroy()
        signup = None
        """
            closes the window and sends a message to the main window
        """
        pub.sendMessage("SignupWindowClosed", arg1="data")


##################################################################################


if __name__ == '__main__':
    #  a global variable to keep track of the root window
    global root
    root = Tk()
    root.geometry(str(w)+"x"+str(h)+"+200+200")
    Project = WelcomeWindow(root)

    root.mainloop()

##################################################################################
