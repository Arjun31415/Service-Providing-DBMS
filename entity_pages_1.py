from tkinter import*
from pubsub import pub
from tkinter import messagebox
import tables as tb
import tkinter as tk
from tkinter import ttk


CustomerPage = None
EmployeePage = None
AdminPage = None
bookservice = None
h = 400
w = 400


class Customer:

    def __init__(self, master=None):
        self.parent = master
        

        self.parent.geometry(str(w)+"x"+str(h))
        self.make_widgets()
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)
        pub.subscribe(self.listner, "BookserviceWindowClosed")

    # ----------------------------------------------------------------

    def make_widgets(self):
        # put the widgets
        self.parent.title("Customer Page")
        heading = Label(self.parent, text="Welcome", font=("Arial", 16))
        heading.pack()

        #username 
        usr_label = Label(self.parent, text="Username:",
                          font=("Times", 11),
                          anchor='center'
                          )
        usr_label.place(x=25/400*w, y=(h/8))

        #Cust_id
        id_label = Label(self.parent, text="Identification No:",
                          font=("Times", 11),
                          anchor='center'
                          )
        id_label.place(x=25/400*w, y=(h/8)+20)

        #address
        Add_label = Label(self.parent, text="Address:",
                          font=("Times", 11),
                          anchor='center'
                          )
        Add_label.place(x=25/400*w, y=(h/8)+40)

        #Phone NUmmber
        Phone_label = Label(self.parent, text="Phone No:",
                          font=("Times", 11),
                          anchor='center'
                          )
        Phone_label.place(x=25/400*w, y=(h/8)+60)

        #for service
        book_label = Label(self.parent, text="Book a Service:",
                          font=("Times", 11),
                          anchor='center'
                          )
        book_label.place(x=25/260*w, y=(h/8)+95)
        Book = Button(self.parent, text='Book')
        Book.place(x=25/150*w, y=(h/8)+120)
        Book.bind('<Button-1>', self.bookservice)
        
        #for 
        idk_label = Label(self.parent, text="Booking Details:",
                          font=("Times", 11),
                          anchor='center'
                          )
        idk_label.place(x=25/43*w, y=(h/8)+95)
        idk = Button(self.parent, text='View')
        idk.place(x=25/38*w, y=(h/8)+120)
        #idk.bind('<Button-1>', self.authenticate)
       
        #payment
        pay_label = Label(self.parent, text="Payment:",
                          font=("Times", 11),
                          anchor='center'
                          )
        pay_label.place(x=25/185*w, y=(h/8)+170)
        pay = Button(self.parent, text='View')
        pay.place(x=25/150*w, y=(h/8)+195)

        #details
        pro_label = Label(self.parent, text="Edit Profile:",
                          font=("Times", 11),
                          anchor='center'
                          )
        pro_label.place(x=25/42*w, y=(h/8)+170)
        pro = Button(self.parent, text='Edit')
        pro.place(x=25/38*w, y=(h/8)+195)
        
     # ----------------------------------------------------------------
    def bookservice(self, event):
        
        self.hide()
        bookservice = Toplevel(self.parent)
        BookserviceWindow = Bookservice(bookservice)
        
            
         

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
    
    def show(self):
        self.parent.update()
        self.parent.deiconify()

    def hide(self):
        self.parent.withdraw()

    def listner(self, arg1, arg2=None):
        """
        pubsub listener - opens main frame when otherFrame closes
        """
        self.show()


class Bookservice:

    def __init__(self, master=None):
        self.parent = master
        

        # Creating tkinter window
        
        self.parent.title('Combobox')
        self.parent.geometry('500x250')
  
        # label text for title
        ttk.Label(self.parent, text = "BooK Your Service", 
           foreground ="black", 
          font = ("Times New Roman", 12)).grid(row = 0, column = 1)
  
        # label
        ttk.Label(self.parent, text = "Select the Month :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)
  
        # Combobox creation
        n = tk.StringVar()
        monthchoosen = ttk.Combobox(self.parent, width = 27, textvariable = n)
  
        # Adding combobox drop down list
        monthchoosen['values'] = ('')
  
        monthchoosen.grid(column = 1, row = 5)
        monthchoosen.current()
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    
    
    def hide(self):
        self.parent.withdraw()

    
    def show(self):
        self.parent.update()
        self.parent.deiconify()



    def listner(self, arg1, arg2=None):
        """
        pubsub listener - opens main frame when otherFrame closes
        """
        self.show()

    def on_closing(self):
        global bookservice
        # if messagebox.askokcancel("Quit", "Do you want to signout?"):
        self.parent.destroy()
        bookservice = None
        """
                closes the window and sends a message to the main window
        """
        print(CustomerPage)
        pub.sendMessage("BookserviceWindowClosed", arg1="data")

