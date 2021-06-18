import cx_Oracle
f = open("database-user.txt", "r")
connection = cx_Oracle.connect(
    user=((f.readline()).strip('\n')),
    password=(f.readline().strip('\n')),
    dsn="localhost/xepdb1"
)

print("Successfully connected to Oracle Database")

cursor = connection.cursor()


# Create Alogin table if it doesn't already exist
# ----------------------------------------------------------------

cursor.execute("""
declare
    table_exists number:=0;
begin
     select count(table_name) into table_exists from USER_TABLES where table_name='ALOGIN';

    if (table_exists = 0) then
        execute immediate 'create table Alogin (email_id varchar2(40) ,password varchar2(20),type char(1) not null,constraint pk_emailid
    primary key(email_id))';
    end if;
end;
""")
# ----------------------------------------------------------------

# Create Admin table if it does not already exist
cursor.execute("""
declare
    table_exists number:=0;
begin
     select count(table_name) into table_exists from USER_TABLES where table_name='ADMIN';

    if (table_exists = 0) then
        execute immediate 'create table admin(admin_id number(7, 0), email_id varchar2(40), admin_name varchar2(20),
                   address varchar2(50),
                   constraint pk_adminid primary key(admin_id),
                   constraint fk_email1 foreign key(email_id) references Alogin(email_id) ON DELETE CASCADE)';
    end if;
end;
""")
# ----------------------------------------------------------------

# Create the employee table if it does not already exist
# ----------------------------------------------------------------
cursor.execute("""
declare
    table_exists number:=0;
begin
     select count(table_name) into table_exists
        from USER_TABLES where table_name='EMPLOYEE';

    if (table_exists = 0) then
        execute immediate 'create table employee (emp_id number(7,0) generated by default as identity,
        email_id varchar2(40) ,emp_name varchar2(20),
            address varchar2(50),
        constraint pk_empid primary key(emp_id),
        constraint fk_email2 foreign key(email_id)
            references Alogin(email_id) ON DELETE CASCADE
    )';
    end if;
end;
""")
# ----------------------------------------------------------------

# Create the loyalty table if it does not already exist
# ----------------------------------------------------------------

cursor.execute("""
declare
    table_exists number:=0;
begin
     select count(table_name) into table_exists from USER_TABLES where table_name='LOYALTY';

    if (table_exists = 0) then
        execute immediate 'create table loyalty(loyalty_id number(7,0),loyalty_name varchar2(20),constraint pk_custid
     primary key(loyalty_id))';
    end if;
end;
""")
# ----------------------------------------------------------------

# Create the Customer table if it does not already exist
# ----------------------------------------------------------------

cursor.execute("""
declare
    table_exists number:=0;
begin
     select count(table_name) into table_exists from USER_TABLES where table_name='CUSTOMER';

    if (table_exists = 0) then
        execute immediate 'create table Customer(cust_id number(7,0) generated by default as identity,email_id varchar2(40) ,cust_name varchar2(20),
    address varchar2(50),loyalty_id number(7,0),
    constraint pk_customerid primary key(cust_id),
    constraint fk_email3 foreign key(email_id) references Alogin(email_id) ON DELETE CASCADE,
    constraint fk_loyalty foreign key(loyalty_id)
    references
    loyalty(loyalty_id))';
    end if;
end;
""")

# ----------------------------------------------------------------

# create the adminphone table
# if it does not already exist
# ----------------------------------------------------------------

cursor.execute("""
declare
    table_exists number:=0;
begin
     select count(table_name) into table_exists from USER_TABLES where table_name='ADMINPHONE';

    if (table_exists = 0) then
        execute immediate 'create table adminphone (admin_id number(7,0),phone_no number(10,0),constraint fk_adminid
     foreign key(admin_id) references admin(admin_id) ON DELETE CASCADE) ';
    end if;
end;
""")
# ----------------------------------------------------------------

# Create the empphone table if it does not already exist
# ----------------------------------------------------------------

cursor.execute("""
declare
    table_exists number:=0;
begin
     select count(table_name) into table_exists from USER_TABLES where table_name='EMPPHONE';

    if (table_exists = 0) then
        execute immediate 'create table empphone (emp_id number(7,0),phone_no number(10,0),constraint fk_empid
     foreign key(emp_id) references employee(emp_id) ON DELETE CASCADE) ';
    end if;
end;
""")
# ----------------------------------------------------------------

# Create the table custphone if it does not already exist
# ----------------------------------------------------------------
cursor.execute("""
declare
    table_exists number:=0;
begin
     select count(table_name) into table_exists from USER_TABLES where table_name='CUSTPHONE';

    if (table_exists = 0) then
        execute immediate 'create table custphone (cust_id number(7,0),phone_no number(10,0),constraint fk_custid
        foreign key(cust_id) references Customer(cust_id) ON DELETE CASCADE ) ';
    end if;
end;
""")
# ----------------------------------------------------------------

# Create the Service table if it does not already exist
# ----------------------------------------------------------------

cursor.execute("""
declare
    table_exists number:=0;
begin
     select count(table_name) into table_exists from USER_TABLES where table_name='SERVICE';

    if (table_exists = 0) then
        execute immediate
        'create table service (service_id varchar2(15) ,service_name varchar2(50) UNIQUE,
    service_cost number(10,2),constraint pk_serviceid primary key(service_id))';
    end if;
end;
""")
# ----------------------------------------------------------------

# Create cust_avails_service table if it does not already exist
# ----------------------------------------------------------------

cursor.execute("""
declare
    table_exists number:=0;
begin
     select count(table_name) into table_exists from USER_TABLES where table_name='CUST_AVAILS_SERVICE';

    if (table_exists = 0) then
        execute immediate 'create table cust_avails_service (service_id varchar2(10),cust_id number(7,0),
        constraint fk_serviceid foreign key(service_id) references service(service_id),
        constraint fk_custid1 foreign key(cust_id) references Customer(cust_id))';
    end if;
end;
""")
# ----------------------------------------------------------------

# Create the EMPLOYEE PERFORMS SERVICE TABLE if it does not already exist
# ----------------------------------------------------------------

cursor.execute("""
declare
    table_exists number:=0;
begin
     select count(table_name) into table_exists from USER_TABLES where table_name='EMP_PERF_SERVICE';

    if (table_exists = 0) then
        execute immediate ' create table emp_perf_service 
        (service_id varchar2(10),
        emp_id number(7,0) ,
        salary number(7,0),
         constraint fk_serviceid1 foreign key(service_id) references service(service_id),
         constraint fk_empid1 foreign key(emp_id) references employee(emp_id) ON DELETE CASCADE,
         constraint pk_emp_id_serv_id primary key(service_id,emp_id)
         )';
         
    end if;
end;
""")

# ----------------------------------------------------------------

# Create the BILL 1 table if it does not already exist
# ----------------------------------------------------------------

cursor.execute("""
declare
    table_exists number:=0;
begin
     select count(table_name) into table_exists from USER_TABLES where table_name='BILL1';

    if (table_exists = 0) then
        execute immediate 'create table bill1 (bill_id varchar2(10),email_id varchar2(40),cust_id number(7,0),emp_id number(7,0),service_date date ,
         constraint fk_emailid4 foreign key(email_id) references Alogin(email_id),
         constraint fk_custid2 foreign key(cust_id) references Customer(cust_id),
         constraint pk_billid primary key(bill_id),
         constraint unq_bill_cust_emp UNIQUE (bill_id,cust_id,emp_id)
        )';
    end if;
end;
""")

# ----------------------------------------------------------------

# Create the BILL 2 table if it does not already exist
# ----------------------------------------------------------------

cursor.execute("""
declare
    table_exists number:=0;
begin
     select count(table_name) into table_exists from USER_TABLES where table_name='BILL2';

    if (table_exists = 0) then
        execute immediate 'create table bill2 (bill_id varchar2(10),service_id varchar2(10),email_id varchar2(40) ,
         constraint fk_serviceid2 foreign key(service_id) references service(service_id),
         constraint fk_emailid5 foreign key(email_id) references Alogin(email_id),
         constraint fk_billid foreign key(bill_id) references bill1(bill_id),
         constraint pk_billid_serviceid primary key (bill_id,service_id)
        )';
    end if;
end;
""")

# ----------------------------------------------------------------

# Insert
data = [("mina@gmail.com", "100001", "e"),
        ("rajiv@yahoo.com", "100002", "c"),
        ("anusha@gmail.com", "100003", "a"),
        ("jayendra@yahoo.com", "100004", "e"),
        ("hema@gmail.com", "100005", "c"),
        ("mohini@yahoo.com", "100006", "a"),
        ("amar@gmail.com", "100007", "e"),
        ("rati@yahoo.com", "100008", "c"),
        ("sunita@gmail.com", "100009", "a"),
        ("punit@yahoo.com", "1000010", "e"),
        ("narasimhan@gmail.com", "100011", "c"),
        ("shankar@yahoo.com", "100012", "a"),
        ("durga@gmail.com", "100013", "e"),
        ("gokul@yahoo.com", "100014", "c"),
        ("ram@gmail.com", "1000015", "a"),
        ("sona@yahoo.com", "100004", "e"),
        ("raj@gmail.com", "100005", "c"),
        ("yash@yahoo.com", "100006", "a"),
        ("devansh@gmail.com", "100007", "e"),
        ("aman@yahoo.com", "100008", "c"),
        ("kamala@gmail.com", "100009", "a"),
        ("rohit@yahoo.com", "100010", "e"),
        ("jagan@gmail.com", "100011", "c"),
        ("hari@yahoo.com", "100012", "a")
        ]

cursor.executemany(
    "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(Alogin(email_id)) */  into Alogin values(:1, :2,:3)",
    data)
print(cursor.rowcount, "Rows Inserted")

# ----------------------------------------------------------------

# Insert
# ----------------------------------------------------------------

admindata = [("3001", "anusha@gmail.com", "anusha", "alwarpet"), ("3002", "mohini@yahoo.com", "mohini", "chetpet"),
             ("3003", "sunita@gmail.com", "sunitha", "nungambakam"), ("3004",
                                                                      "shankar@yahoo.com", "shankar", "egmore"),
             ("3005", "ram@gmail.com", "ram", "anna nagar"), ("3006",
                                                              "yash@yahoo.com", "yash", "guindy"),
             ("3007", "kamala@gmail.com", "kamala", "adyar"), ("3008", "hari@yahoo.com", "hari", "kilpauk")]

cursor.executemany(
    "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(ADMIN(admin_id)) */  into admin values(:1,:2,:3,:4)",
    admindata)
print(cursor.rowcount, "Rows Inserted")

# Insert
# ----------------------------------------------------------------
empdata = [("1001", "mina@gmail.com", "mina", "mandaveli"),
           ("1002", "jayendra@yahoo.com", "jayendra", "perumbakkam"),
           ("1003", "amar@gmail.com", "amar", "nandanam"),
           ("1004", "punit@yahoo.com", "punit", "royapettah"),
           ("1005", "devansh@gmail.com", "devansh", "mudichur"),
           ("1006", "sona@yahoo.com", "sona", "porur"),
           ("1007", "durga@gmail.com", "durga", "perambur"),
           ("1008", "rohit@yahoo.com", "rohit", "saidapet")
           ]

cursor.executemany(
    "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(EMPLOYEE(emp_id)) */ into employee values(:1,:2,:3,:4)",
    empdata)
print(cursor.rowcount, "Rows Inserted")
# ----------------------------------------------------------------

# Insert
# ----------------------------------------------------------------
loyaltydata = [("101", "gold"), ("102", "silver"), ("103", "bronze")]
cursor.executemany(
    "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(LOYALTY(loyalty_id)) */into loyalty (loyalty_id,loyalty_name) values(:1,:2)",
    loyaltydata)
print(cursor.rowcount, "Rows Inserted")
# ----------------------------------------------------------------

# Insert
# ----------------------------------------------------------------

custdata = [("2001", "rajiv@yahoo.com", "rajiv", "addb", "101"),
            ("2002", "hema@gmail.com", "hema", "addh", "102"),
            ("2003", "rati@yahoo.com", "rati", "addn", "103"),
            ("2004", "narasimhan@gmail.com", "narasimhan", "addt", "101"),
            ("2005", "gokul@yahoo.com", "gokul", "adde", "102"),
            ("2006", "raj@gmail.com", "raj", "addk", "103"),
            ("2007", "aman@yahoo.com", "aman", "addq", "101"),
            ("2008", "jagan@gmail.com", "jagan", "addw", "101")
            ]

cursor.executemany(
    "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(CUSTOMER(cust_id)) */ into Customer values(:1,:2,:3,:4,:5)",
    custdata)
print(cursor.rowcount, "Rows Inserted")

# ----------------------------------------------------------------

# Insert
# ----------------------------------------------------------------

servicedata = [("a101", "office cleaning", 2000),
               ("b101", "vacuumming", 1000),
               ("a102", "disinfecting", 1500),
               ("c101", "painting", 4000),
               ("a103", "bathroom cleaning", 2500),
               ("b102", "plumbing", 2200),
               ("a104", "household cleaning", 5000),
               ("c102", "appliance repair", 1600),
               ('b103', 'pest control', 3700)]

cursor.executemany(
    """insert
        /*+ IGNORE_ROW_ON_DUPKEY_INDEX(SERVICE(service_id)) */
        into service(service_id,service_name,service_cost) values (:1,:2,:3)""",
    servicedata)
print(cursor.rowcount, "Rows Inserted")

# ----------------------------------------------------------------
# Insert
# ----------------------------------------------------------------

adminphonedata = [("3001", "9392246754"),
                  ("3002", "8966450921"),
                  ("3003", "7977234510"),
                  ("3004", "9932140076"),
                  ("3005", "9850457389"),
                  ("3006", "9126076732"),
                  ("3007", "9650123497"),
                  ("3008", "8935412765")]
cursor.executemany(
    "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(ADMIN(admin_id)) */  into adminphone values(:1,:2)",
    adminphonedata)
print(cursor.rowcount, "Rows Inserted")

# ----------------------------------------------------------------

# Insert
# ----------------------------------------------------------------
empphonedata = [("1001", "9766345483"),
                ("1002", "7893784629"),
                ("1003", "9352647251"),
                ("1004", "9083737721"),
                ("1005", "9874636263"),
                ("1006", "9352632752"),
                ("1007", "9463846010"),
                ("1008", "8637226377")]
cursor.executemany(
    "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(EMPLOYEE(emp_id)) */ into empphone values(:1,:2)",
    empphonedata)
print(cursor.rowcount, "Rows Inserted")
# ----------------------------------------------------------------

# Insert
# ----------------------------------------------------------------

custphonedata = [("2001", "9036373238"),
                 ("2002", "8736361190"),
                 ("2003", "7474939238"),
                 ("2004", "9473188765"),
                 ("2005", "9144537827"),
                 ("2006", "9772621900"),
                 ("2007", "8936211028"),
                 ("2008", "9836271263")]
cursor.executemany(
    "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(CUSTOMER(cust_id)) */ into Custphone values(:1,:2)",
    custphonedata)
print(cursor.rowcount, "Rows Inserted")
connection.commit()
# ----------------------------------------------------------------
# Insert
# ----------------------------------------------------------------

cust_avails_servicedata = [("b101", "2001"),
                           ("c102", "2008"),
                           ("b103", "2003"),
                           ("a101", "2004"),
                           ("a104", "2005"),
                           ("c101", "2006"),
                           ("a102", "2007"),
                           ("b102", "2008")]
cursor.executemany(
    "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(CUSTOMER(cust_id)) */ into cust_avails_service values(:1,:2)",
    cust_avails_servicedata)
print(cursor.rowcount, "Rows Inserted")

# Insert
# ----------------------------------------------------------------

emp_perf_servicedata = [("b101", "1001", "800"), ("c102", "1003", "700"),
                        ("b103", "1002", "500"), ("a101", "1004", "450"),
                        ("a104", "1005", "280"), ("c101", "1006", "300"),
                        ("a102", "1007", "400"), ("b102", "1003", "350")]
try:
    cursor.executemany(
        "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(DEMOPYTHON.PK_EMP_ID_SERV_ID) */ into emp_perf_service values(:1,:2,:3)",
        emp_perf_servicedata)
    print(cursor.rowcount, "Rows Inserted")

except cx_Oracle.IntegrityError:
    print("0 Rows inserted\n")

# Insert
# ----------------------------------------------------------------

bill1data = [("b001", "2001", "1001", "28 mar 20"),
             ("b005", "2008", "1003", "13 apr 20"),
             ("b002", "2003", "1002", "19 jan 21"),
             ("b006", "2004", "1004", "05 may 20"),
             ("b003", "2005", "1005", "23 sep 20"),
             ("b007", "2006", "1006", "11 dec 20"),
             ("b004", "2007", "1007", "20 apr 21"),
             ("b008", "2008", "1003", "30 jun 2020")]
cursor.executemany(
    """insert
        /*+ IGNORE_ROW_ON_DUPKEY_INDEX(BILL1,PK_BILLID) */
        into bill1(bill_id,cust_id,emp_id,service_date) values(:1,:2,:3,:4)""",
    bill1data)
print(cursor.rowcount, "Rows Inserted")

# ----------------------------------------------------------------
# Insert
# ----------------------------------------------------------------

bill2data = [("b001", "b101"), ("b005", "c102"),
             ("b002", "b103"), ("b006", "a101"),
             ("b003", "a104"), ("b007", "a104"),
             ("b004", "a102"), ("b008", "b102")]
try:
    cursor.executemany(
        "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(CUSTOMER(cust_id)) */ into bill2(bill_id,service_id) values(:1,:2)",
        bill2data)
    print(cursor.rowcount, "Rows Inserted")

except cx_Oracle.IntegrityError:
    print("0 Rows inserted\n")

# ----------------------------------------------------------------


connection.commit()

# ----------------------------------------------------------------


def auth_login(email, password):
    """
        given a username and password return
         whether it is valid or not
    """
    cursor.execute(
        """select * from Alogin
            where email_id='%s' and password='%s'"""
        % (email, password)
    )
    data = cursor.fetchall()
    if(data == []):
        return 0
    if(data[0][1] != password):
        return 0
    else:
        # data[0][2] is the person type
        return data[0][2]

# ----------------------------------------------------------------------------------------------


conv = {"c": "CUSTOMER", "e": "EMPLOYEE", "a": "ADMIN"}

# ----------------------------------------------------------------------------------------------


"""
    gets the basic details of an employee,customer and admin
    It returns only ID,email,Name and address.
"""


def get_details(email, person="c"):
    tb = conv[person]
    cursor.execute(
        """select * from %s
            where email_id='%s'"""
        % (tb, email)
    )
    temp = cursor.fetchall()
    print(temp)
    temp = list(temp[0])
    data = dict(zip(["ID", "Email", "Name", "Address"], temp))
    print(data)
    return data

# ----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------


def get_customer_details(email):

    # CUSTOMER
    cursor.execute(
        """select * from CUSTOMER
            where email_id='%s'"""
        % (email)
    )
    temp = list((cursor.fetchall())[0])
    print("temp= ", temp)
    data = dict(zip(["ID", "Email", "Name", "Address", "Loyalty_id"], temp))
    print("data: ", data)
    # assuming single phone number

    cursor.execute(
        """
            select phone_no from CUSTPHONE
            where cust_id='%s'

        """
        % (data["ID"])
    )
    phone_no = list(cursor.fetchall())
    if(phone_no == []):
        data["Mobile"] = None
        return data

    # phone[0] gives the phone number as a tuple
    # phone[0][0] gives the phone number as an integer
    data["Mobile"] = (phone_no[0][0])
    print(data)
    return data

# ----------------------------------------------------------------------------------------------


def get_employee_details(email):

    # EMPLOYEE
    cursor.execute(
        """select * from EMPLOYEE
            where email_id='%s'"""
        % (email)
    )
    temp = list((cursor.fetchall())[0])
    print("temp= ", temp)
    data = dict(zip(["ID", "Email", "Name", "Address"], temp))
    print("data: ", data)
    # assuming single phone number

    cursor.execute(
        """
            select phone_no from EMPPHONE
            where emp_id='%s'

        """
        % (data["ID"])
    )
    phone_no = list(cursor.fetchall())
    if(phone_no == []):
        data["Mobile"] = None
        return data

    # phone[0] gives the phone number as a tuple
    # phone[0][0] gives the phone number as an integer
    data["Mobile"] = (phone_no[0][0])
    print(data)
    return data


def get_admin_details(email):

    # ADMIN
    cursor.execute(
        """select * from ADMIN
            where email_id='%s'"""
        % (email)
    )
    temp = list((cursor.fetchall())[0])
    print("temp= ", temp)
    data = dict(zip(["ID", "Email", "Name", "Address"], temp))
    print("data: ", data)
    # assuming single phone number

    cursor.execute(
        """
            select phone_no from ADMINPHONE
            where admin_id='%s'
        """
        % (data["ID"])
    )
    phone_no = list(cursor.fetchall())
    if(phone_no == []):
        data["Mobile"] = None
        return data

    # phone[0] gives the phone number as a tuple
    # phone[0][0] gives the phone number as an integer
    data["Mobile"] = (phone_no[0][0])
    print(data)
    return data
# ----------------------------------------------------------------------------------------------


def get_loyalty(email):
    cursor.execute(
        """select A.*,B.loyalty_name from %s A, loyalty B
            where email_id='%s' and B.loyalty_id=A.loyalty_id"""
        % ("CUSTOMER", email)
    )
    data = cursor.fetchall()

    print(data)
    return data


"""
    ONLY THE CUSTOMER CAN SIGNUP
    IF an employee or admin account is to be made
    then it will be done by the existing admin account
"""
# ----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------


def auth_signup(email, password, Type="c"):
    """
        given a email and password
        check if this account already exists
        otherwise create the account
    """
    cursor.execute(
        """select * from Alogin
            where email_id='%s'"""
        % (email)
    )
    data = cursor.fetchall()
    print(data)
    if (data != []):
        return 0
    else:
        data = [(str(email), str(password), str(Type))]
        print(data)
        cursor.executemany("insert into Alogin values(:1, :2,:3)", data)
        cursor.execute(
            "insert into CUSTOMER(email_id) values(:EMAIL) ", EMAIL=email)
        print(cursor.rowcount, "Rows Inserted")
        connection.commit()
    return 1

# ----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------


def change_custdetails(cust_id, name=None, address=None, mobile=None):
    """
        if email or address are entered
        replace given value
    """

    cursor.execute(
        """select Customer.*,phone_no
                from Customer,Custphone
                where Customer.cust_id='%s'and CUSTPHONE.cust_id=Customer.cust_id """
        % (cust_id)
    )
    data = cursor.fetchall()
    print("data: ", data)
    if(data == []):
        return "No such account exists"
    else:
        print(data)
        # return data[0][2]
        if address != None:
            cursor.execute(
                """update Customer set address='%s'
                where cust_id='%s'"""
                % (address, cust_id)
            )
        if mobile != None:
            cursor.execute(
                """
            update Custphone
                 set phone_no='%s'
                 where cust_id='%s'
                """
                % (mobile, cust_id)
            )
        if name != None:
            cursor.execute(
                """
                update Customer set cust_name='%s'
                    where cust_id='%s'
                """
                % (name, cust_id)
            )

        connection.commit()
        return "update successfull"

# ----------------------------------------------------------------------------------------------


def change_empdetails(emp_id, name=None, address=None, mobile=None):
    """
        if email or address are entered
        replace given value
    """

    cursor.execute(
        """select *
                from EMPLOYEE
                where EMPLOYEE.emp_id='%s'"""
        % (emp_id)
    )
    data = cursor.fetchall()
    print("data: ", data)
    if(data == []):
        print("No such account exists")
        return "No such account exists"
    else:
        print(data)
        # return data[0][2]
        if address != None:
            cursor.execute(
                """update EMPLOYEE set address='%s'
                where emp_id='%s'"""
                % (address, emp_id)
            )
        if mobile != None:
            cursor.execute(
                """
            update EMPPHONE
                 set phone_no='%s'
                 where emp_id='%s'
                """
                % (mobile, emp_id)
            )
        if name != None:
            cursor.execute(
                """
                update EMPLOYEE set emp_name='%s'
                    where emp_id='%s'
                """
                % (name, emp_id)
            )

        connection.commit()
        return "update successfull"
# ----------------------------------------------------------------------------------------------


def get_services():
    cursor.execute(
        """select service_name from service"""
    )
    x = cursor.fetchall()
    print(x)
    return x

# ----------------------------------------------------------------------------------------------


def add_emp(name, address, mobile, email):
    try:
        cursor.execute(
            """
            INSERT INTO ALOGIN(
                EMAIL_ID,
                PASSWORD,
                "TYPE"
            )
            VALUES
            (
                '%s',
                'R^Y@WOkLlaeT',
                'e'
            )
            """
            % (email)
        )
    except:
        return 1

    cursor.execute(
        """
        INSERT INTO EMPLOYEE(
            EMAIL_ID,
            EMP_NAME,
            ADDRESS
        )
        VALUES
        (
            '%s',
            '%s',
            '%s'
        )
        """
        % (email, name, address)
    )
    cursor.execute(
        """
        select emp_id from employee where email_id='%s'

        """
        % (email)
    )
    empid = cursor.fetchone()[0]
    cursor.execute(
        """
        INSERT INTO EMPPHONE(
            EMP_ID,
            PHONE_NO
        )
        VALUES
        (
            '%s',
            '%d'
        )
        
        """
        % (empid, int(mobile))
    )
    connection.commit()

    # something
    return 0

# ----------------------------------------------------------------------------------------------


def remove_emp(emp_id):

    cursor.execute(
        """
            select email_id from employee
            where emp_id='%s'
        """
        % (emp_id))
    email = cursor.fetchone()[0]
    print(email)
    cursor.execute(
        """
        DELETE FROM ALOGIN
        WHERE
        EMAIL_ID='%s'

        """
        % (email)
    )
    cursor.execute(
        """DELETE FROM EMPLOYEE
            WHERE
                EMP_ID='%s'
        """
        % (emp_id)
    )
    connection.commit()

# ----------------------------------------------------------------------------------------------


def add_service(serv_id, name, cost):
    try:
        cursor.execute(
            """
            INSERT INTO SERVICE(
                SERVICE_ID,
                SERVICE_NAME,
                SERVICE_COST
            )
            VALUES
            (
                '%s',
                '%s',
                 %d
            )
            """
            % (serv_id, name, int(cost))
        )
        connection.commit()
        return 0

    except cx_Oracle.IntegrityError:
        return 1


def remove_service(serv_id):
    try:
        cursor.execute(
            """
            DELETE FROM SERVICE
            WHERE
                SERVICE_ID = '%s'
       
        """
            % (serv_id)
        )
        connection.commit()
        return 0

    except Exception as e:
        print(e)
        return 1


def get_services_enrolled(emp_id):

    cursor.execute(
        """
        SELECT
            B.SERVICE_NAME,
            SALARY
        FROM
            EMP_PERF_SERVICE A,Service B
        WHERE
            EMP_ID = '%s' AND 
            A.SERVICE_ID=B.SERVICE_ID
        
        """
        % (emp_id)
    )
    temp = cursor.fetchall()
    print(temp)

    return temp


get_services_enrolled(1003)

# ----------------------------------------------------------------------------------------------
# remove_emp(emp_id=1001)
# change_empdetails(1001, address="hwaii", mobile=1234567890, name="Ram")
# cursor.execute("""insert into EMPPHONE values(1001, 1234567890)""")
# print(add_service("b10001", "ooga", 100000))
# add_emp(name="Shyma", address="2nd wolf street",
#         mobile=1234567890, email="memem@gmail.com")
connection.commit()
