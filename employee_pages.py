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
        book_label = Label(self.parent, text="Book a Service:",
                           font=("Times", 11),
                           anchor='center'
                           )
        book_label.place(x=25/260*w, y=(h/8)+95)
        Book = Button(self.parent, text='Book')
        Book.place(x=25/150*w, y=(h/8)+120)

        # Book.bind('<Button-1>', self.bookservice)

        # for
        idk_label = Label(self.parent, text="Booking Details:",
                          font=("Times", 11),
                          anchor='center'
                          )
        idk_label.place(x=25/43*w, y=(h/8)+95)
        idk = Button(self.parent, text='View')
        idk.place(x=25/38*w, y=(h/8)+120)
        # idk.bind('<Button-1>', self.authenticate)

        # payment
        pay_label = Label(self.parent, text="Payment:",
                          font=("Times", 11),
                          anchor='center'
                          )
        pay_label.place(x=25/185*w, y=(h/8)+170)
        pay = Button(self.parent, text='View')
        pay.place(x=25/150*w, y=(h/8)+195)

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

    # def bookservice(self, event):

    #     self.hide()
    #     bookservice = Toplevel(self.parent)
    #     BookserviceWindow = Bookservice(bookservice)

    # ----------------------------------------------------------------

    def editinfo(self, event):

        self.hide()
        editinfo = Toplevel(self.parent)
        EditinfoWindow = Editinfo(
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
