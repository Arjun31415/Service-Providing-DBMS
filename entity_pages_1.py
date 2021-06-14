from tkinter import*
from pubsub import pub
from tkinter import messagebox
import tables as tb
from tkinter import ttk
from tkcalendar import *

h = 400
w = 400


class Customer:

    def __init__(self, master, username):
        self.parent = master
        self.parent.geometry(str(w)+"x"+str(h))
        self.email = username
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)
        pub.subscribe(self.listner, "BookserviceWindowClosed")
        # Make the page widgets
        self.make_widgets()

    # ----------------------------------------------------------------

    def make_widgets(self):
        # put the widgets
        self.parent.title("Customer Page")
        heading = Label(self.parent, text="Welcome", font=("Arial", 16))
        heading.pack()

        # data = tb.get_details(self.email, person="c")
        data1 = tb.get_customer_details(self.email)
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
        Book.bind('<Button-1>', self.bookservice)

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

    def bookservice(self, event):

        self.hide()
        bookservice = Toplevel(self.parent)
        BookserviceWindow = Bookservice(bookservice)

    # ----------------------------------------------------------------

    def editinfo(self, event):

        self.hide()
        editinfo = Toplevel(self.parent)
        EditinfoWindow = Editinfo(editinfo)

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


class Bookservice:

    def __init__(self, master=None):
        self.parent = master

        # Creating tkinter window

        self.parent.title('Combobox')
        self.parent.geometry('500x250')

        # label text for title
        ttk.Label(self.parent, text="BooK Your Service",
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
        ################################
        conf = Button(self.parent, text='Confirm')
        conf.place(x=25/45*w, y=(h/8)+90)
        conf.bind('<Button-1>', self.on_closing)
        # service_offered.current(0)
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

        pick = Button(self.parent, text='Pick Data')
        pick.place(x=25/400*w, y=(h/8)+28)
        pick.bind('<Button-1>', self.pickdate)

        pro_label = Label(self.parent, text=":",
                          font=("Times", 14),
                          anchor='center'
                          )
        pro_label.place(x=25/100*w, y=(h/8)+28)

    # ----------------------------------------------------------------

    # def customer(self, event):

    #     self.hide()
    #     customer = Toplevel(self.parent)
    #     CustomerWindow = Customer(customer)
    # ----------------------------------------------------------------

    def pickdate(self, event):

        self.hide()
        # pickdate = Toplevel(self.parent)
        # PickdateWindow =Pickdate(pickdate)
        # Create Object
        date_window = Tk()

       # Set geometry
        date_window.geometry("500x400")

       # Add Calender

        cal = Calendar(date_window, selectmode='day',
                       year=2020, month=5,
                       day=22, date_pattern='dd/MM/yyyy')

        cal.pack(pady=20)

        # Add Button and Label
        date = Label(date_window, text="")

        # def grad_date(cal, date): return date.config(
        #     text="Selected Date is: " + cal.get_date())

        Button(date_window, text="Get Date",
               command=lambda: date.config(
                   text="Selected Date is: " +
                   cal.get_date()
               )
               ).pack(pady=20)

        def destroy_date_window():
            date_window.destroy()
            self.show()
        Button(date_window, text="Confirm",
               command=destroy_date_window).pack(pady=25)
        date.pack(pady=20)
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
        global bookservice
        # if messagebox.askokcancel("Quit", "Do you want to signout?"):
        self.parent.destroy()
        """
            closes the window and sends a message to the main window
        """
        pub.sendMessage("BookserviceWindowClosed", arg1="data")

########################################################################################################


class Editinfo:

    def __init__(self, master=None):
        self.parent = master
        self.parent.title('Edit profile')
        self.parent.geometry('500x250')
        data1 = tb.get_customer_details('nikhil')
        self.make_widgets()

    # ----------------------------------------------------------------

    def make_widgets(self):
        # put the widgets
        self.parent.title("Welcome")
        heading = Label(self.parent, text="Edit Profile", font=("Arial", 16))
        heading.pack()

        data = tb.get_customer_details('nikhil')
        # username
        usr_label = Label(self.parent, text="Username: %s" % (data["Email"]),
                          font=("Times", 11),
                          anchor='center'
                          )
        usr_label.place(x=25/400*w, y=(h/8))

        # Cust_id
        id_label = Label(self.parent, text="Identification No: %s" % (data["ID"]),
                         font=("Times", 11),
                         anchor='center'
                         )
        id_label.place(x=25/400*w, y=(h/8)+23)

        name_label = Label(self.parent, text="Name:",
                           font=("Times", 11),
                           anchor='center'
                           )
        name_label.place(x=25/400*w, y=(h/8)+43)
        self.addr = Entry(self.parent, bg='white', font=("Arail", 8))
        self.addr.place(x=25/135 * w, y=(h/8)+45)
        if (data["Name"] == None):
            self.addr.insert(END, "NA")
        else:
            self.addr.insert(END, data["Name"])

        add_label = Label(self.parent, text="Address: ",
                          font=("Times", 11),
                          anchor='center'
                          )
        add_label.place(x=25/400*w, y=(h/8)+63)
        self.phn = Entry(self.parent, bg='white', font=("Arail", 8))
        self.phn.place(x=25/120 * w, y=(h/8)+66)
        if (data["Address"] == None):
            self.phn.insert(END, "NA")
        else:
            self.phn.insert(END, data["Address"])

        Phone_label = Label(self.parent, text="Phone No:",
                            font=("Times", 11),
                            anchor='center'
                            )
        Phone_label.place(x=25/400*w, y=(h/8)+83)
        self.nam = Entry(self.parent, bg='white', font=("Arail", 8))
        self.nam.place(x=25/108 * w, y=(h/8)+86)
        if (data["Mobile"] == None):
            self.nam.insert(END, "NA")
        else:
            self.nam.insert(END, data["Mobile"])
        savech = Button(self.parent, text='Save Changes')
        savech.place(x=25/41*w, y=(h/8)+130)
        # savech.bind('<Button-1>', self.customer)

        canc = Button(self.parent, text='Cancel')
        canc.place(x=25/70*w, y=(h/8)+130)
        # canc.bind('<Button-1>', self.customer)

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

    def on_closing(self):
        global editinfo
        # if messagebox.askokcancel("Quit", "Do you want to signout?"):
        self.parent.destroy()
        """
            closes the window and sends a message to the main window
        """
        pub.sendMessage("EditinfoWindowClosed", arg1="data")


class Pickdate:

    def __init__(self, master=None):
        self.parent = master

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

    def on_closing(self):
        global pickdate
        # if messagebox.askokcancel("Quit", "Do you want to signout?"):
        self.parent.destroy()
        """
            closes the window and sends a message to the main window
        """
        pub.sendMessage("PickdateWindowClosed", arg1="data")
