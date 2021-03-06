import sys
from tkinter import*
from customer_pages import w, h
from tkinter import messagebox
from tkcalendar import *
from pubsub import pub
import tables as tb

#####################################################################################


class Admin:

    def __init__(self, master, username):
        self.parent = master
        self.parent.geometry(str(w)+"x"+str(h))
        self.email = username
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)
        pub.subscribe(self.listner, "AddempWindowClosed")
        pub.subscribe(self.listner, "RemoveempWindowClosed")
        pub.subscribe(self.listner, "AddservWindowClosed")
        pub.subscribe(self.listner, "RemservWindowClosed")
        # Make the page widgets
        self.make_widgets()

    # ----------------------------------------------------------------

    def make_widgets(self):
        # put the widgets
        self.parent.title("Admin Page")
        heading = Label(self.parent, text="Welcome",
                        font=("Arial", 16))
        heading.pack()

        # data = tb.get_details(self.email, person="c")
        data1 = tb.get_admin_details(self.email)
        # username
        usr_label = Label(self.parent, text="Username: %s" % (self.email),
                          font=("Times", 11),
                          anchor='center'
                          )
        usr_label.place(x=25/400*w, y=(h/8))

        # Cust_id
        id_label = Label(self.parent, text="Identification No: %s" % (data1["ID"]),
                         font=("Times", 11),
                         anchor='center'
                         )
        id_label.place(x=25/400*w, y=(h/8)+20)

        # address
        Add_label = Label(self.parent, text="Address:  %s" % (data1["Address"]),
                          font=("Times", 11),
                          anchor='center'
                          )
        Add_label.place(x=25/400*w, y=(h/8)+40)

        # Phone NUmmber
        Phone_label = Label(self.parent, text="Name:  %s" % (data1["Name"]),
                            font=("Times", 11),
                            anchor='center'
                            )
        Phone_label.place(x=25/400*w, y=(h/8)+60)

        # for emp
        ad_label = Label(self.parent, text="Add an Employee:",
                         font=("Times", 11),
                         anchor='center'
                         )
        ad_label.place(x=25/260*w, y=(h/8)+95)
        ad = Button(self.parent, text='Add')
        ad.place(x=25/150*w, y=(h/8)+120)
        ad.bind('<Button-1>', self.addemp)

        # for emp
        idk_label = Label(self.parent, text="Remove an employee",
                          font=("Times", 11),
                          anchor='center'
                          )
        idk_label.place(x=25/43*w, y=(h/8)+95)
        idk = Button(self.parent, text='Remove')
        idk.place(x=25/38*w, y=(h/8)+120)
        idk.bind('<Button-1>', self.removeemp)

        # servi
        serv_label = Label(self.parent, text="Add Service:",
                           font=("Times", 11),
                           anchor='center'
                           )
        serv_label.place(x=25/185*w, y=(h/8)+170)
        ser = Button(self.parent, text='Add')
        ser.place(x=25/150*w, y=(h/8)+195)
        ser.bind('<Button-1>', self.addserv)

        # serivce
        pro_label = Label(self.parent, text="Remove service:",
                          font=("Times", 11),
                          anchor='center'
                          )
        pro_label.place(x=25/42*w, y=(h/8)+170)
        pro = Button(self.parent, text='Remove')
        pro.place(x=25/38*w, y=(h/8)+195)
        pro.bind('<Button-1>', self.remserv)
     # ----------------------------------------------------------------

    def addemp(self, event):
        self.hide()
        addemp = Toplevel(self.parent)
        Addemp(master=addemp)
     # ----------------------------------------------------------------

    def removeemp(self, event):
        self.hide()
        removeemp = Toplevel(self.parent)
        Removeemp(master=removeemp)
 # ----------------------------------------------------------------

    def addserv(self, event):
        self.hide()
        addserv = Toplevel(self.parent)
        Addserv(master=addserv)
# ----------------------------------------------------------------

    def remserv(self, event):
        self.hide()
        Remserv(master=Toplevel(self.parent))

    # ----------------------------------------------------------------

    def on_closing(self):

        if messagebox.askokcancel("Quit", "Do you want to signout?"):
            self.parent.destroy()

            """
                closes the window and sends a message to the main window
            """
            pub.sendMessage("CustomerWindowClosed", arg1="data")

    # ----------------------------------------------------------------

    def show(self):
        self.parent.update()
        self.parent.deiconify()

    # ----------------------------------------------------------------

    def hide(self):
        self.parent.withdraw()

    # ----------------------------------------------------------------

    def listner(self, arg1, arg2=None):
        """
        pubsub listener - opens main frame when otherFrame closes
        """
        self.show()
    # ----------------------------------------------------------------
#####################################################################################


class Addemp:

    def __init__(self, master=None):
        self.parent = master
        self.parent.title('ADD EMPLOYEE')
        self.parent.geometry('500x250')
        self.make_widgets()
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

    # ----------------------------------------------------------------

    def make_widgets(self):
        # put the widgets
        self.parent.title("ADD Emp")
        heading = Label(self.parent, text="NEW EMPLOYEE", font=("Arial", 16))
        heading.pack()

        # ----------------------------------------------------------------

        def reset():
            # Email
            usr_label = Label(self.parent, text="Email:",
                              font=("Times", 12),
                              anchor='center'
                              )
            usr_label.place(x=25/400*w, y=(h/8))
            self.mail = Entry(self.parent, bg='white', font=("Arail", 12))
            self.mail.place(x=25/135 * w, y=(h/8)+2)

            # Name
            name_label = Label(self.parent, text="Name:",
                               font=("Times", 12),
                               anchor='center'
                               )
            name_label.place(x=25/400*w, y=(h/8)+23)

            self.nam = Entry(self.parent, bg='white', font=("Arail", 12))
            self.nam.place(x=25/135 * w, y=(h/8)+25)

            # Address
            add_label = Label(self.parent, text="Address: ",
                              font=("Times", 12),
                              anchor='center'
                              )
            add_label.place(x=25/400*w, y=(h/8)+43)
            self.addr = Entry(self.parent, bg='white', font=("Arail", 12))
            self.addr.place(x=25/120 * w, y=(h/8)+46)

            # Mobile Number
            Phone_label = Label(self.parent, text="Phone No:",
                                font=("Times", 12),
                                anchor='center'
                                )
            Phone_label.place(x=25/400*w, y=(h/8)+63)
            self.phn = Entry(self.parent, bg='white', font=("Arail", 12))
            self.phn.place(x=25/106 * w, y=(h/8)+66)

        # ----------------------------------------------------------------

        def get_changes():
            res = tb.add_emp(
                name=self.nam.get(),
                address=self.addr.get(),
                mobile=self.phn.get(),
                email=self.mail.get()
            )
            if(res == 1):
                messagebox.showerror(
                    title="Primary Key violated",
                    message="Another employee with same email-id already exists"
                )
            elif res == 0:
                messagebox.showinfo(
                    title="Success",
                    message="Employee successfull enrolled"
                )

        # ----------------------------------------------------------------

        reset()
        savech = Button(self.parent, text='ADD', command=get_changes)
        savech.place(x=25/40*w, y=(h/8)+130)

        canc = Button(self.parent, text='Cancel', command=reset)
        canc.place(x=25/70*w, y=(h/8)+130)

    # ----------------------------------------------------------------

    def hide(self):
        self.parent.withdraw()

    # ----------------------------------------------------------------

    def show(self):
        self.parent.update()
        self.parent.deiconify()

    # ----------------------------------------------------------------

    def listner(self, arg1, arg2=None):
        """
        pubsub listener - opens main frame when otherFrame closes
        """
        self.show()

    # ----------------------------------------------------------------

    def on_closing(self, arg1=None, arg2=None):

        self.parent.destroy()
        """
            closes the window and sends a message to the main window
        """
        pub.sendMessage("AddempWindowClosed", arg1="data")
    # ----------------------------------------------------------------


################################################################################

class Removeemp:

    def __init__(self, master=None):
        self.parent = master
        self.parent.title('REMOVE EMPLOYEE')
        self.parent.geometry('500x250')

        self.make_widgets()
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

    # ----------------------------------------------------------------

    def make_widgets(self):
        # put the widgets
        self.parent.title("Remove Emp")
        heading = Label(self.parent, text="REMOVE EMPLOYEE",
                        font=("Arial", 16))
        heading.pack()

        def reset():

            id_label = Label(self.parent, text="Identification No: ",
                             font=("Times", 11),
                             anchor='center'
                             )
            id_label.place(x=25/400*w, y=(h/8)+23)
            self.id = Entry(self.parent, bg='white', font=("Arail", 14))
            self.id.place(x=25/68 * w, y=(h/8)+25)

        def get_changes():
            tb.remove_emp(emp_id=self.id.get())

        reset()
        savech = Button(self.parent, text='Confirm', command=get_changes)
        savech.place(x=25/41*w, y=(h/8)+130)

        canc = Button(self.parent, text='Cancel', command=reset)
        canc.place(x=25/70*w, y=(h/8)+130)

    # ------------------------------------------------

    def hide(self):
        self.parent.withdraw()

    # ----------------------------------------------------------------

    def show(self):
        self.parent.update()
        self.parent.deiconify()

    # ----------------------------------------------------------------

    def listner(self, arg1, arg2=None):
        """
        pubsub listener - opens main frame when otherFrame closes
        """
        self.show()

    # ----------------------------------------------------------------

    def on_closing(self, arg1=None, arg2=None):
        # if messagebox.askokcancel("Quit", "Do you want to signout?"):
        self.parent.destroy()
        """
            closes the window and sends a message to the main window
        """
        pub.sendMessage("RemoveempWindowClosed", arg1="data")
      ##############################################################


class Addserv:

    def __init__(self, master=None):
        self.parent = master
        self.parent.title('ADD EMPLOYEE')
        self.parent.geometry('500x250')

        self.make_widgets()
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

    # ----------------------------------------------------------------

    def make_widgets(self):
        # put the widgets
        self.parent.title("ADD serv")
        heading = Label(self.parent, text="NEW SERVICE", font=("Arial", 16))
        heading.pack()

        def reset():
            # serv name
            ser_lbl = Label(self.parent, text="Service Name:",
                            font=("Times", 11),
                            anchor='center'
                            )
            ser_lbl.place(x=25/400*w, y=(h/8))
            self.serv_name = Entry(self.parent, bg='white', font=("Arail", 12))
            self.serv_name.place(x=25/86 * w, y=(h/8)+2)
            # serv_id
            id_label = Label(self.parent, text="Service ID:      ",
                             font=("Times", 11),
                             anchor='center'
                             )
            id_label.place(x=25/400*w, y=(h/8)+25)
            self.id = Entry(self.parent, bg='white', font=("Arail", 12))
            self.id.place(x=25/100 * w, y=(h/8)+27)

            # cost
            cost_label = Label(self.parent, text="Cost:",
                               font=("Times", 11),
                               anchor='center'
                               )
            cost_label.place(x=25/400*w, y=(h/8)+48)

            self.cost = Entry(self.parent, bg='white', font=("Arail", 12))
            self.cost.place(x=25/145 * w, y=(h/8)+50)

        def get_changes():
            res = tb.add_service(name=self.serv_name.get(),
                                 serv_id=self.id.get(),
                                 cost=self.cost.get(),
                                 )
            if(res == 1):
                messagebox.showerror(
                    title="Primary Key violated",
                    message="Another service with same service-id already exists"
                )
            elif res == 0:
                messagebox.showinfo(
                    title="Success",
                    message="Service successfull added"
                )

        reset()
        savech = Button(self.parent, text='ADD', command=get_changes)
        savech.place(x=25/41*w, y=(h/8)+130)

        canc = Button(self.parent, text='Cancel', command=reset)
        canc.place(x=25/70*w, y=(h/8)+130)

    # ------------------------------------------------

    def hide(self):
        self.parent.withdraw()

    # ----------------------------------------------------------------

    def show(self):
        self.parent.update()
        self.parent.deiconify()

    # ----------------------------------------------------------------

    def listner(self, arg1, arg2=None):
        """
        pubsub listener - opens main frame when otherFrame closes
        """
        self.show()

    # ----------------------------------------------------------------

    def on_closing(self, arg1=None, arg2=None):
        # if messagebox.askokcancel("Quit", "Do you want to signout?"):
        self.parent.destroy()
        """
            closes the window and sends a message to the main window
        """
        pub.sendMessage("AddservWindowClosed", arg1="data")
    # ----------------------------------------------------------------

################################################################################


class Remserv:

    def __init__(self,  master=None):
        self.parent = master
        self.parent.title('REMOVE SERVICE')
        self.parent.geometry('500x250')

        self.make_widgets()
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

    # ----------------------------------------------------------------

    def make_widgets(self):
        # put the widgets
        self.parent.title("remove serv")
        heading = Label(self.parent, text="DELETE SERVICE", font=("Arial", 16))
        heading.pack()
        id_label = Label(self.parent, text="Service ID:",
                         font=("Times", 11),
                         anchor='center'
                         )
        id_label.place(x=25/400*w, y=(h/8)+23)

        def reset():
            # Cust_id
            self.id = Entry(self.parent, bg='white', font=("Arail", 12))
            self.id.place(x=25/100 * w, y=(h/8)+25)

        def get_changes():
            res = tb.remove_service(self.id.get())
            if(res == 1):
                messagebox.showerror(
                    title="Error",
                    message="No such service exists"
                )
            elif res == 0:
                messagebox.showinfo(
                    title="Success",
                    message="Service successfull removed"
                )

        reset()
        savech = Button(self.parent, text='Remove', command=get_changes)
        savech.place(x=25/41*w, y=(h/8)+130)

        canc = Button(self.parent, text='Cancel', command=reset)
        canc.place(x=25/70*w, y=(h/8)+130)

    # ------------------------------------------------

    def hide(self):
        self.parent.withdraw()

    # ----------------------------------------------------------------

    def show(self):
        self.parent.update()
        self.parent.deiconify()

    # ----------------------------------------------------------------

    def listner(self, arg1, arg2=None):
        """
        pubsub listener - opens main frame when otherFrame closes
        """
        self.show()

    # ----------------------------------------------------------------

    def on_closing(self, arg1=None, arg2=None):

        self.parent.destroy()
        """
            closes the window and sends a message to the main window
        """
        pub.sendMessage("RemservWindowClosed", arg1="data")
    # ----------------------------------------------------------------

################################################################################
