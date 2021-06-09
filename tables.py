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
                   constraint fk_email1 foreign key(email_id) references Alogin(email_id))';
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
     select count(table_name) into table_exists from USER_TABLES where table_name='EMPLOYEE';

    if (table_exists = 0) then
        execute immediate 'create table employee (emp_id number(7,0),email_id varchar2(40) ,emp_name varchar2(20),
    address varchar2(50),constraint pk_empid primary key(emp_id),
    constraint fk_email2 foreign key(email_id)
    references Alogin(email_id))';
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
    constraint fk_email3 foreign key(email_id) references
    Alogin(email_id),
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
     foreign key(admin_id) references admin(admin_id))';
    end if;
end;
""")
# ----------------------------------------------------------------

# Create the emphone table if it does not already exist
# ----------------------------------------------------------------

cursor.execute("""
declare
    table_exists number:=0;
begin
     select count(table_name) into table_exists from USER_TABLES where table_name='EMPPHONE';

    if (table_exists = 0) then
        execute immediate 'create table empphone (emp_id number(7,0),phone_no number(10,0),constraint fk_empid
     foreign key(emp_id) references employee(emp_id))';
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
     foreign key(cust_id) references Customer(cust_id))';
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
        execute immediate 'create table service (service_id varchar2(10) ,service_name varchar2(20),
    service_cost number(5,0),constraint pk_serviceid primary key(service_id))';
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
        execute immediate 'create table cust_avails_service (service_id varchar2(10),cust_id number(7,0), constraint fk_serviceid foreign key(service_id)
    references service(service_id),constraint fk_custid1 foreign key(cust_id) references Customer(cust_id))';
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
        execute immediate ' create table emp_perf_service (service_id varchar2(10),emp_id number(7,0) ,salary number(7,0), constraint fk_serviceid1 foreign key(service_id)
    references service(service_id),constraint fk_empid1 foreign key(emp_id) references employee(emp_id))';
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
        execute immediate 'create table bill1 (bill_id varchar2(10),email_id varchar2(40),cust_id number(7,0),emp_id number(7,0),service_date date , constraint fk_emailid4 foreign key(email_id)
    references Alogin(email_id),constraint fk_custid2 foreign key(cust_id) references Customer(cust_id), constraint pk_billid primary key(bill_id))';
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
        execute immediate 'create table bill2 (bill_id varchar2(10),service_id varchar2(10),email_id varchar2(40) , constraint fk_serviceid2
    foreign key(service_id) references service(service_id),constraint fk_emailid5 foreign key(email_id) references Alogin(email_id),
    constraint fk_billid foreign key(bill_id) references bill1(bill_id))';
    end if;
end;
""")

# ----------------------------------------------------------------

# Insert
data = [("A", "100001", "e"), ("B", "100002", "c"), ("C", "100003", "a"), ("D", "100004", "e"), ("E", "100005", "c"), ("F", "100006", "a"),
        ("G", "100007", "e"), ("H", "100008", "c"), ("I", "100009", "a"), ("J",
                                                                           "1000010", "e"), ("K", "100011", "c"), ("L", "100012", "a"),
        ("M", "100013", "e"), ("N", "100014", "c"), ("O", "1000015",
                                                     "a"), ("P", "100004", "e"), ("Q", "100005", "c"), ("R", "100006", "a"),
        ("S", "100007", "e"), ("T", "100008", "c"), ("U", "100009", "a"), ("V", "1000010", "e"), ("W", "100011", "c"), ("X", "100012", "a")]
cursor.executemany(
    "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(Alogin(email_id)) */  into Alogin values(:1, :2,:3)",
    data)
print(cursor.rowcount, "Rows Inserted")

# ----------------------------------------------------------------

# Insert
# ----------------------------------------------------------------

admindata = [("3001", "C", "c", "addc"), ("3002", "I", "i", "addi"), ("3003", "O", "o", "addo"), ("3004", "U", "u", "addu"),
             ("3005", "L", "l", "addl"), ("3006", "F", "f", "addf"), ("3007", "R", "r", "addr"), ("3008", "X", "x", "addx")]
cursor.executemany(
    "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(ADMIN(admin_id)) */  into admin values(:1,:2,:3,:4)",
    admindata)
print(cursor.rowcount, "Rows Inserted")

# Insert
# ----------------------------------------------------------------
empdata = [("1001", "A", "a", "adda"), ("1002", "G", "g", "addg"), ("1003", "M", "m", "addm"), ("1004", "S", "s", "adds"),
           ("1005", "D", "d", "addd"), ("1006", "J", "j", "addj"), ("1005", "P", "p", "addp"), ("1006", "V", "v", "addv")]
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

custdata = [("2001", "B", "b", "addb", "101"), ("2002", "H", "h", "addh", "102"), ("2003", "N", "n", "addn", "103"), ("2004", "T", "t", "addt", "101"),
            ("2005", "E", "e", "adde", "102"), ("2006", "K", "k", "addk", "103"), ("2007", "Q", "q", "addq", "101"), ("2008", "W", "w", "addw", "101")]
cursor.executemany(
    "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(CUSTOMER(cust_id)) */ into Customer values(:1,:2,:3,:4,:5)",
    custdata)
print(cursor.rowcount, "Rows Inserted")

# ----------------------------------------------------------------

# Insert
# ----------------------------------------------------------------

servicedata = [("a101", "sweeping"), ("b101", "vacuumming"), ("a102", "Mopping"), ("c101", "Sofa cleaning"),
               ("a103", "a3"), ("b102", "b2"), ("a104", "a4"), ("c102", "c2")]
cursor.executemany(
    """insert 
        /*+ IGNORE_ROW_ON_DUPKEY_INDEX(SERVICE(service_id)) */ 
        into service(service_id,service_name) values (:1,:2)""",
    servicedata)
print(cursor.rowcount, "Rows Inserted")

# ----------------------------------------------------------------------------------------------

connection.commit()

# ----------------------------------------------------------------------------------------------


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


get_details('A', 'e')
get_loyalty('B')


def change_custdetails(cust_id, email=None, address=None):
    """
        if email or address are entered
        replace given value 
    """
    if email != None:
        def auth_login(email, password):
            cursor.execute(
                """select * from Alogin
             where email_id='%s' """
                % (email)
            )
    data = cursor.fetchall()
    if(data == []):
        return 0
    else:
        return data[0][2]
        cursor.execute(
            """update Customer set email_id=%s
            where cust_id='%s'"""
            % (email, cust_id)
        )
    if address != None:
        cursor.execute(
            """update Customer set address=%s
            where cust_id='%s'"""
            % (address, cust_id)
        )


def get_services():
    cursor.execute(
        """select service_name from service"""
    )
    all_services = list(cursor.fetchall())
    print(all_services)
    return all_services
