import sys
from tkinter import*
from customer_pages import w, h
from customer_pages import Editinfo
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import *
from pubsub import pub
import tables as tb
#import tabulate


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
        pub.subscribe(self.listner, "ViewdetWindowClosed")
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

        # Phone NUmmber
        name_label = Label(self.parent, text="Name:  %s" % (data1["Name"]),
                           font=("Times", 11),
                           anchor='center'
                           )
        name_label.place(x=25/400*w, y=(h/8)+78)
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
        idk.bind('<Button-1>', self.viewdet)

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
    def viewdet(self, event):

        self.hide()
        viewdet = Toplevel(self.parent)
        Viewdet(viewdet, self.empid)

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
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.create_widget(emp_id)

     # ----------------------------------------------------------------
    def create_widget(self, emp_id):
        services = tb.get_services()

        n = StringVar()
        self.service_offered = ttk.Combobox(
            self.parent, width=27, textvariable=n)

        # Adding combobox drop down list
        services = tb.get_services()
        self.service_offered['values'] = (services)

        self.service_offered.grid(column=1, row=5)
        # self.service_offered = Entry(
        #     self.parent,
        #     width=30,
        #     font=('Arial', 16)
        # )
        # self.service_offered.place(x=25/100 * w, y=(h/8)+100)

        Button(self.parent,
               text='Confirm',
               command=lambda: self.enroll_service(emp_id=emp_id)).place(x=25/45*w, y=(h/8)+90)

    def hide(self):
        self.parent.withdraw()

    def enroll_service(self, emp_id):
        self.val = self.service_offered.get()
        res = tb.enroll_service(emp_id, self.val)
        if(res == 0):
            messagebox.showinfo(
                title="Success", message="enroll successfull")
        else:
            messagebox.showinfo(
                title="Failure",
                message="Already enrolled in such a service/service does not exist"
            )
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
        self.parent.title('Unenroll')
        self.parent.geometry('500x250')

        # label text for title
        ttk.Label(self.parent, text="Unenroll Your Service",
                  foreground="black",
                  font=("Times New Roman", 12)).grid(row=0, column=1)
        self.emp_id = emp_id
        self.make_widgets()
        # label

        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

     # ----------------------------------------------------------------
    def make_widgets(self):
        ttk.Label(self.parent, text="Enter the service name :",
                  font=("Times New Roman", 10)).grid(column=0,
                                                     row=5, padx=10, pady=25)

        def remove():
            self.val = service_unenroll.get()
            res = tb.unenroll(self.emp_id, self.val)
            if(res == 0):
                messagebox.showinfo(
                    title="Success", message="delete successfull")
            else:
                messagebox.showinfo(
                    title="Failure",
                    message="Not enrolled in such a service"
                )
        service_unenroll = Entry(self.parent, bg='white', font=("Arail", 8))
        service_unenroll.place(x=25/135 * w, y=(h/8)+45)

        # print("val: ", self.val)
        conf = Button(self.parent, text='Confirm',
                      command=remove)
        #
        conf.place(x=25/45*w, y=(h/8)+90)
        # service_offered.current(0)

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


class Viewdet:

    def __init__(self, master=None, emp_id=None):
        self.parent = master
        self.parent.geometry('1500x500')
        self.emp_id = emp_id

        # label

        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.make_widgets()

     # ----------------------------------------------------------------
    def make_widgets(self):
        lst = tb.get_services_to_be_done(self.emp_id)
        lst.insert(0, ("service Name", "Customer Name",
                   "Address", "Phone No.", "Date", "Cost"))
        total_rows = len(lst)
        total_columns = len(lst[0])
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(self.parent, width=20, fg='Black',
                               font=('Arial', 12, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
# ----------------------------------------------------------------

        # print("val: ", self.val)
        conf = Button(self.parent, text='Done')
        #
        conf.place(x=25/45*w, y=(h/8)+90)
        # service_offered.current(0)

    # _____________________________________________
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
        pub.sendMessage("ViewdetWindowClosed", arg1="data")
