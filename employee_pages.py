import sys
from tkinter import*
from customer_pages import w, h
from customer_pages import Editinfo
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import *
from pubsub import pub
import tables as tb


class Employee:
    def __init__(self, master, username):
        self.parent = master
        self.parent.geometry(str(w)+"x"+str(h))
        self.email = username
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

        # pub.subscribe(self.listner, "BookserviceWindowClosed")
        pub.subscribe(self.listner, "EditinfoWindowClosed")
        pub.subscribe(self.listner, "EnrollWindowClosed")
        pub.subscribe(self.listner, "UnenrollWindowClosed")
        # Make the page widgets
        self.make_widgets()

    # ----------------------------------------------------------------

    def make_widgets(self):
        # put the widgets
        self.parent.title("Employee Dashboard")
        heading = Label(self.parent, text="Welcome", font=("Arial", 16))
        heading.pack()

        # data = tb.get_details(self.email, person="c")
        data1 = tb.get_employee_details(self.email)
        # username
        usr_label = Label(self.parent, text="Email-ID: %s" % (self.email),
                          font=("Times", 11),
                          anchor='center'
                          )
        usr_label.place(x=25/400*w, y=(h/8))

        self.empid = data1["ID"]
        # emp_id
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
        Phone_label = Label(self.parent, text="Phone No:  %s" % (data1["Mobile"]),
                            font=("Times", 11),
                            anchor='center'
                            )
        Phone_label.place(x=25/400*w, y=(h/8)+60)

        # for service
        book_label = Label(self.parent, text="Enroll a Service:",
                           font=("Times", 11),
                           anchor='center'
                           )
        book_label.place(x=25/260*w, y=(h/8)+95)
        Book = Button(self.parent, text='Enroll')
        Book.place(x=25/150*w, y=(h/8)+120)

        Book.bind('<Button-1>', self.enroll)

        # for
        idk_label = Label(self.parent, text="Services to be Done:",
                          font=("Times", 11),
                          anchor='center'
                          )
        idk_label.place(x=25/43*w, y=(h/8)+95)
        idk = Button(self.parent, text='View')
        idk.place(x=25/38*w, y=(h/8)+120)
        # idk.bind('<Button-1>', self.authenticate)

        # payment
        pay_label = Label(self.parent, text="Unenroll serivce:",
                          font=("Times", 11),
                          anchor='center'
                          )
        pay_label.place(x=25/185*w, y=(h/8)+170)
        pay = Button(self.parent, text='Unenroll')
        pay.place(x=25/150*w, y=(h/8)+195)
        pay.bind('<Button-1>', self.unenroll)

        # details
        pro_label = Label(self.parent, text="Edit Profile:",
                          font=("Times", 11),
                          anchor='center'
                          )
        pro_label.place(x=25/42*w, y=(h/8)+170)
        pro = Button(self.parent, text='Edit')
        pro.place(x=25/38*w, y=(h/8)+195)
        pro.bind('<Button-1>', self.editinfo)
     # ----------------------------------------------------------------

    def enroll(self, event):

        self.hide()
        enroll = Toplevel(self.parent)
        Enroll(enroll, self.empid)

    # ----------------------------------------------------------------

    def unenroll(self, event):

        self.hide()
        unenroll = Toplevel(self.parent)
        Unenroll(unenroll, self.empid)

    # ----------------------------------------------------------------

    def editinfo(self, event):

        self.hide()
        editinfo = Toplevel(self.parent)
        Editinfo(
            email=self.email,
            person='e',
            master=editinfo)

# ----------------------------------------------------------------
    def on_closing(self):

        if messagebox.askokcancel("Quit", "Do you want to signout?"):
            self.parent.destroy()

            """
                closes the window and sends a message to the main window
            """
            pub.sendMessage("EmployeeWindowClosed", arg1="data")

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

####################################################################################################################################


class Enroll:

    def __init__(self, master=None, emp_id=None):
        self.parent = master
        self.parent.title('Combobox')
        self.parent.geometry('500x250')

        # label text for title
        ttk.Label(self.parent, text="Enroll Your Service",
                  foreground="black",
                  font=("Times New Roman", 12)).grid(row=0, column=1)

        # label
        ttk.Label(self.parent, text="Select the service :",
                  font=("Times New Roman", 10)).grid(column=0,
                                                     row=5, padx=10, pady=25)

        # Combobox creation
        n = StringVar()
        service_offered = ttk.Combobox(self.parent, width=27, textvariable=n)

        # Adding combobox drop down list
        services = tb.get_services()
        service_offered['values'] = (services)

        service_offered.grid(column=1, row=5)

        conf = Button(self.parent, text='Confirm')
        conf.place(x=25/45*w, y=(h/8)+90)
        conf.bind('<Button-1>', self.on_closing)
        # service_offered.current(0)
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

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
        pub.sendMessage("EnrollWindowClosed", arg1="data")

########################################################################################################


class Unenroll:

    def __init__(self, master=None, emp_id=None):
        self.parent = master
        self.parent.title('Combobox')
        self.parent.geometry('500x250')

        # label text for title
        ttk.Label(self.parent, text="Unenroll Your Service",
                  foreground="black",
                  font=("Times New Roman", 12)).grid(row=0, column=1)

        # label
        ttk.Label(self.parent, text="Select the service :",
                  font=("Times New Roman", 10)).grid(column=0,
                                                     row=5, padx=10, pady=25)

        # Combobox creation
        n = StringVar()
        service_offered = ttk.Combobox(self.parent, width=27, textvariable=n)

        # Adding combobox drop down list
        services = tb.get_services_enrolled(emp_id)
        service_offered['values'] = (services)

        service_offered.grid(column=1, row=5)
        val = service_offered.get()

        conf = Button(self.parent, text='Confirm')
        conf.place(x=25/45*w, y=(h/8)+90)
        conf.bind('<Button-1>', tb.unenroll(emp_id, val))
        # service_offered.current(0)
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

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
        pub.sendMessage("UnenrollWindowClosed", arg1="data")

########################################################################################################
