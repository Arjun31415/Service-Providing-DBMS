import cx_Oracle
f = open("database-user.txt", "r")
connection = cx_Oracle.connect(
    user=((f.readline()).strip('\n')),
    password=(f.readline().strip('\n')),
    dsn="localhost/xepdb1"
)

print("Successfully connected to Oracle Database")

cursor = connection.cursor()

# deleting existing tables
cursor.execute("""
    begin
        execute immediate 'drop table adminphone';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")
cursor.execute("""
    begin
        execute immediate 'drop table empphone';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")
cursor.execute("""
    begin
        execute immediate 'drop table custphone';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")
cursor.execute("""
    begin
        execute immediate 'drop table admin';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")
cursor.execute("""
    begin
        execute immediate 'drop table cust_avails_service';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")
cursor.execute("""
    begin
        execute immediate 'drop table emp_perf_service';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")

cursor.execute("""
    begin
        execute immediate 'drop table bill2';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")
cursor.execute("""
    begin
        execute immediate 'drop table bill1';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")
cursor.execute("""
    begin
        execute immediate 'drop table service';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")
cursor.execute("""
    begin
        execute immediate 'drop table employee';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")
cursor.execute("""
    begin
        execute immediate 'drop table Customer';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")
cursor.execute("""
    begin
        execute immediate 'drop table loyalty';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")
cursor.execute("""
    begin
        execute immediate 'drop table Alogin';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")

# ALOGIN TABLE
# Create
cursor.execute("""
    create table Alogin (email_id varchar2(40) ,password varchar2(20),type char(1) not null,constraint pk_emailid
    primary key(email_id))"""
               )

# Insert
data = [("A", "100001", "e"), ("B", "100002", "c"), ("C", "100003", "a"),
        ("D", "100004", "e"), ("E", "100005", "c"), ("F", "100006", "c")]
cursor.executemany(
    "insert into Alogin values(:1, :2,:3)",
    data)
print(cursor.rowcount, "Rows Inserted")

connection.commit()

# ADMIN TABLE
# Create

cursor.execute("""
    create table admin (admin_id number(7,0),email_id varchar2(40) ,admin_name varchar2(20),
    address varchar2(50),constraint pk_adminid primary key(admin_id))"""
               )
cursor.execute("""
    alter table admin add constraint fk_email1 foreign key(email_id) references
     Alogin(email_id)""")

# Insert
admindata = [("10001", "A"), ("10002", "B"), ("10003", "C"), ("10004", "D"),
             ("10005", "E"), ("10006", "F"), ("10007", "A"), ("10008", "F"), ("10009", "C")]
cursor.executemany(
    "insert into admin (admin_id,email_id) values(:1,:2)",
    admindata)
print(cursor.rowcount, "Rows Inserted")

connection.commit()

# EMPLOYEE TABLE
# Create
cursor.execute("""
    create table employee (emp_id number(7,0),email_id varchar2(40) ,emp_name varchar2(20),
    address varchar2(50),constraint pk_empid primary key(emp_id))"""
               )
cursor.execute("""
    alter table employee add constraint fk_email2 foreign key(email_id)
    references Alogin(email_id)"""
               )

# Insert
empdata = [("1001", "A"), ("1002", "C"), ("1003", "D"), ("1004", "B"),
           ("1005", "E"), ("1006", "F"), ("1007", "B"), ("1008", "B")]
cursor.executemany(
    "insert into employee (emp_id,email_id) values(:1,:2)",
    empdata)
print(cursor.rowcount, "Rows Inserted")

connection.commit()

# LOYALTY TABLE
# Create

cursor.execute("""
    create table loyalty(loyalty_id number(7,0),loyalty_name varchar2(20),constraint pk_custid
     primary key(loyalty_id))"""
               )

# Insert
loyaltydata = [("101", "p"), ("102", "q"), ("103", "r")]
cursor.executemany(
    "insert into loyalty (loyalty_id,loyalty_name) values(:1,:2)",
    loyaltydata)
print(cursor.rowcount, "Rows Inserted")

connection.commit()
# CUSTOMER TABLE
# Create

cursor.execute("""
    create table Customer(cust_id number(7,0),email_id varchar2(40) ,cust_name varchar2(20),
    address varchar2(50),loyalty_id number(7,0),constraint pk_customerid primary key(cust_id))"""
               )
cursor.execute("""
    alter table Customer add constraint fk_email3 foreign key(email_id) references
    Alogin(email_id)"""
               )
cursor.execute("""
    alter table Customer add constraint fk_loyalty foreign key(loyalty_id) references
    loyalty(loyalty_id)"""
               )

# Insert
custdata = [("2001", "A"), ("2002", "B"), ("2003", "C"), ("2004", "D"), ("2005", "E"), ("2006", "F"), ("2007", "E"), ("2008", "F"),
            ("2009", "F"), ("2010", "A"), ("2011", "C"), ("2012", "C")]
cursor.executemany(
    "insert into Customer (cust_id,email_id) values(:1,:2)",
    custdata)
print(cursor.rowcount, "Rows Inserted")

connection.commit()

# ADMINPHONE TABLE
# Create

cursor.execute("""
    create table adminphone (admin_id number(7,0),phone_no number(10,0),constraint fk_adminid
     foreign key(admin_id) references admin(admin_id))""")

# Insert
# adminphonedata=[("65456","1","2","3"),("12567","4"),("20789","5")]
# cursor.executemany(
#     "insert into adminphone (admin_id,phone_no) values(:1,:2)",
#     adminphonedata)
# print(cursor.rowcount, "Rows Inserted")

connection.commit()

# EMPPHONE TABLE
# Create

cursor.execute("""
    create table empphone (emp_id number(7,0),phone_no number(10,0),constraint fk_empid
     foreign key(emp_id) references employee(emp_id))""")

# Insert
# adminphonedata=[("65456","1","2","3"),("12567","4"),("20789","5")]
# cursor.executemany(
#     "insert into adminphone (admin_id,phone_no) values(:1,:2)",
#     adminphonedata)
# print(cursor.rowcount, "Rows Inserted")

connection.commit()

# CUSTPHONE TABLE
# Create

cursor.execute("""
    create table custphone (cust_id number(7,0),phone_no number(10,0),constraint fk_custid
     foreign key(cust_id) references Customer(cust_id))""")

# Insert
# adminphonedata=[("65456","1","2","3"),("12567","4"),("20789","5")]
# cursor.executemany(
#     "insert into adminphone (admin_id,phone_no) values(:1,:2)",
#     adminphonedata)
# print(cursor.rowcount, "Rows Inserted")

connection.commit()

# SERVICE TABLE
# Create
cursor.execute("""
    create table service (service_id varchar2(10) ,service_name varchar2(20),
    service_cost number(5,0),constraint pk_serviceid primary key(service_id))"""
               )

# Insert
servicedata = [("a101", "sweeping"), ("b101", "vacuumming"), ("a102", "Mopping"), ("c101", "Sofa cleaning"),
               ("a103", "a3"), ("b102", "b2"), ("a104", "a4"), ("c102", "c2")]
cursor.executemany(
    "insert into service(service_id,service_name) values (:1,:2)",
    servicedata)
print(cursor.rowcount, "Rows Inserted")

connection.commit()

# CUSTOMER AVAILS SERVICE TABLE
# Create
cursor.execute("""
    create table cust_avails_service (service_id varchar2(10),cust_id number(7,0), constraint fk_serviceid foreign key(service_id)
    references service(service_id),constraint fk_custid1 foreign key(cust_id) references Customer(cust_id))"""
               )

# Insert
# custservdata = [("a101", "2001"), ("b101", "2012"), ("a102", "2003"),("c101","2010"),("a103", "2004"), ("b102", "2002"),
#  ("a104", "2005"),("c102","2006")]
# cursor.executemany(
#     "insert into service(service_id,service_name) values (:1,:2)",
#     servicedata)
# print(cursor.rowcount, "Rows Inserted")

connection.commit()

# EMPLOYEE PERFORMS SERVICE TABLE
# Create
cursor.execute("""
    create table emp_perf_service (service_id varchar2(10),emp_id number(7,0) ,salary number(7,0), constraint fk_serviceid1 foreign key(service_id)
    references service(service_id),constraint fk_empid1 foreign key(emp_id) references employee(emp_id))"""
               )

# Insert
# custservdata = [("a101", "2001"), ("b101", "2012"), ("a102", "2003"),("c101","2010"),("a103", "2004"), ("b102", "2002"),
#  ("a104", "2005"),("c102","2006")]
# cursor.executemany(
#     "insert into service(service_id,service_name) values (:1,:2)",
#     servicedata)
# print(cursor.rowcount, "Rows Inserted")

connection.commit()

# BILL 1 TABLE
# Create
cursor.execute("""
    create table bill1 (bill_id varchar2(10),email_id varchar2(40),cust_id number(7,0),emp_id number(7,0),service_date date , constraint fk_emailid4 foreign key(email_id)
    references Alogin(email_id),constraint fk_custid2 foreign key(cust_id) references Customer(cust_id), constraint pk_billid primary key(bill_id))"""
               )

# Insert
# custservdata = [("a101", "2001"), ("b101", "2012"), ("a102", "2003"),("c101","2010"),("a103", "a3"), ("b102", "2002"),
#  ("a104", "2005"),("c102","2006"),("a101", "2007"), ("b101", "2008"), ("a102", "2009"),("c101","2011")]
# cursor.executemany(
#     "insert into service(service_id,service_name) values (:1,:2)",
#     servicedata)
# print(cursor.rowcount, "Rows Inserted")

connection.commit()
# BILL 2 TABLE
# Create
cursor.execute("""
    create table bill2 (bill_id varchar2(10),service_id varchar2(10),email_id varchar2(40) , constraint fk_serviceid2 
    foreign key(service_id) references service(service_id),constraint fk_emailid5 foreign key(email_id) references Alogin(email_id), 
    constraint fk_billid foreign key(bill_id) references bill1(bill_id))"""
               )

# Insert
# custservdata = [("a101", "2001"), ("b101", "2012"), ("a102", "2003"),("c101","2010"),("a103", "a3"), ("b102", "2002"),
#  ("a104", "2005"),("c102","2006"),("a101", "2007"), ("b101", "2008"), ("a102", "2009"),("c101","2011")]
# cursor.executemany(
#     "insert into service(service_id,service_name) values (:1,:2)",
#     servicedata)
# print(cursor.rowcount, "Rows Inserted")

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
        return 1


def auth_signup(email, password, Type="e"):
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
