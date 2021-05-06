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
# Create Admin table if it does not already exist
cursor.execute("""
declare 
    table_exists number:=0;
begin
     select count(table_name) into table_exists from USER_TABLES where table_name='ADMIN'; 
    
    if (table_exists = 0) then
        execute immediate 'create table admin(admin_id number(7, 0), email_id varchar2(40), admin_name varchar2(20),
                   address varchar2(50), 
                   constraint pk_adminid primary key(admin_id)),
                   constraint fk_email1 foreign key(email_id) references Alogin(email_id)';
    end if;
end;
""")

# Create the employee table if it does not already exist
cursor.execute("""
declare 
    table_exists number:=0;
begin
     select count(table_name) into table_exists from USER_TABLES where table_name='EMPLOYEE'; 
    
    if (table_exists = 0) then
        execute immediate 'create table employee (emp_id number(7,0),email_id varchar2(40) ,emp_name varchar2(20),
    address varchar2(50),constraint pk_empid primary key(emp_id)),
    constraint fk_email2 foreign key(email_id)
    references Alogin(email_id';
    end if;
end;
""")

# Create the loyalty table if it does not already exist
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

# Create the Customer table if it does not already exist
cursor.execute("""
declare 
    table_exists number:=0;
begin
     select count(table_name) into table_exists from USER_TABLES where table_name='CUSTOMER'; 
    
    if (table_exists = 0) then
        execute immediate 'create table Customer(cust_id number(7,0),email_id varchar2(40) ,cust_name varchar2(20),
    address varchar2(50),loyalty_id number(7,0),
    constraint pk_customerid primary key(cust_id)),
    constraint fk_email3 foreign key(email_id) references
    Alogin(email_id),
    constraint fk_loyalty foreign key(loyalty_id)
    references
    loyalty(loyalty_id)';
    end if;
end;
""")

# create the adminphone table
# if it does not already exist

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

# Create the emphone table if it does not already exist

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

# Create the table custphone if it does not already exist

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
# Create the Service table if it does not already exist
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

# Create cust_avails_service table if it does not already exist

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

# Create the EMPLOYEE PERFORMS SERVICE TABLE if it does not already exist

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

# Create the BILL 1 table if it does not already exist
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

# Create the BILL 2 table if it does not already exist

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

# Insert
data = [("A", "100001", "e"), ("B", "100002", "c"), ("C", "100003", "a"),
        ("D", "100004", "e"), ("E", "100005", "c"), ("F", "100006", "c")]
cursor.executemany(
    "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(Alogin(email_id)) */  into Alogin values(:1, :2,:3)",
    data)
print(cursor.rowcount, "Rows Inserted")

# Insert
admindata = [("10001", "A"), ("10002", "B"), ("10003", "C"), ("10004", "D"),
             ("10005", "E"), ("10006", "F"), ("10007", "A"), ("10008", "F"), ("10009", "C")]
cursor.executemany(
    "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(ADMIN(admin_id)) */  into admin (admin_id,email_id) values(:1,:2)",
    admindata)
print(cursor.rowcount, "Rows Inserted")

# Insert
empdata = [("1001", "A"), ("1002", "C"), ("1003", "D"), ("1004", "B"),
           ("1005", "E"), ("1006", "F"), ("1007", "B"), ("1008", "B")]
cursor.executemany(
    "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(EMPLOYEE(emp_id)) */ into employee (emp_id,email_id) values(:1,:2)",
    empdata)
print(cursor.rowcount, "Rows Inserted")

# Insert
loyaltydata = [("101", "p"), ("102", "q"), ("103", "r")]
cursor.executemany(
    "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(LOYALTY(loyalty_id)) */into loyalty (loyalty_id,loyalty_name) values(:1,:2)",
    loyaltydata)
print(cursor.rowcount, "Rows Inserted")

# Insert
custdata = [("2001", "A"), ("2002", "B"), ("2003", "C"), ("2004", "D"), ("2005", "E"), ("2006", "F"), ("2007", "E"), ("2008", "F"),
            ("2009", "F"), ("2010", "A"), ("2011", "C"), ("2012", "C")]
cursor.executemany(
    "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(CUSTOMER(cust_id)) */ into Customer (cust_id,email_id) values(:1,:2)",
    custdata)
print(cursor.rowcount, "Rows Inserted")


# Insert
servicedata = [("a101", "sweeping"), ("b101", "vacuumming"), ("a102", "Mopping"), ("c101", "Sofa cleaning"),
               ("a103", "a3"), ("b102", "b2"), ("a104", "a4"), ("c102", "c2")]
cursor.executemany(
    "insert /*+ IGNORE_ROW_ON_DUPKEY_INDEX(SERVICE(service_id)) */ into service(service_id,service_name) values (:1,:2)",
    servicedata)
print(cursor.rowcount, "Rows Inserted")

connection.commit()


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
        return data[0][2]


""" 
    ONLY THE CUSTOMER CAN SIGNUP
    IF an employee or admin account is to be made
    then it will be done by the existing admin account
"""


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
        print(cursor.rowcount, "Rows Inserted")
        connection.commit()
    return 1
