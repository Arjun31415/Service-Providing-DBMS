# Service-Providing-DBMS
## CSE2004 DBMS Project

This is a DBMS project done in 1st year.<br>
Minimum Software Requirements: <br>
- python 3.9 
- Oracle Database 18c 
- SQL*Plus: Release 18.0.0.0.0 
- Tkinter 8.6
- cx_Oracle
- pypubsub 4.0.3

## Setup:
1. [Download](https://www.oracle.com/in/database/technologies/xe-downloads.html "Download Oracle 18") Oracle 18 for the respective operating system
2. Extract the zip file and run the setup
3. Open command line and login to sqlplus
4. Run the following in the command line and substitute XXXX for your password<br><br>
    ```powershell
    sqlplus -l system/XXXX@localhost/xepdb1  
    ```
5. At the SQL> prompt enter the following statements (here the username is demopython change it with the appropriate username or use the same):
    ```sql
    define USERNAME = demopython

    create user &USERNAME;

    alter user &USERNAME
        default tablespace users
        temporary tablespace temp
        quota unlimited on users;

    grant create session,
        create view,
        create sequence,
        create procedure,
        create table,
        create trigger,
        create type,
        create materialized view
        to &USERNAME;
    ```
6. Still in SQL*Plus set a paswword for USERNAME. Replace YYYY with the password and run:<br>
    ```sql
    alter user &USERNAME identified by YYYY
    ```
7. Exit SQL*Plus 
    ```sql
    quit
    ```
8. Install PYTHON 3 or later. Ensure that both Python and pip are installed and present in the user/system path
9. install cx_Oracle:<br>
    1. From the command line type:<br>
     ```powershell
       python -m pip install cx_Oracle --upgrade --user
     ```
10. The setup is finsihed.After this just create a python file.refer [test.py](./test.py "test.py")
11. For creating windows and sending messages between pypubsub is required.<br>
    ```powershell
    pip install pypubsub
    ```


            