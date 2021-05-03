import cx_Oracle

connection = cx_Oracle.connect(
    user="demopython",
    password="jonu123",
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
        execute immediate 'drop table service';
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
data = [("a", "123","e"), ("b", "567","c"), ("c", "789","a")]
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
admindata = [("65456", "a"), ("12567", "b"), ("20789", "c")]
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
empdata = [("1001", "a"), ("1002", "b"), ("1003", "c")]
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
custdata = [("2001", "a"), ("2002", "b"), ("2003", "c")]
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
servicedata = [("a101", "Something"), ("b102", "A2"), ("c103", "Mopping")]
cursor.executemany(
    "insert into service(service_id,service_name) values (:1,:2)",
    servicedata)
print(cursor.rowcount, "Rows Inserted")

connection.commit()


# Now query the rows back

# for row in cursor.execute('select * from Alogin'):

#     print(row)
