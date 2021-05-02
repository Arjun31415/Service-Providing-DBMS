# Setup Workspace For Oracle 
## Oracle Dev Tools

download the [extension](https://marketplace.visualstudio.com/items?itemName=Oracle.oracledevtools "Oracle Dev Tools") from vscode market place
or paste `oracle.oracledevtools` in the extensions Menu inside Vscode.<br><br>
In the Oracle tools extension, for connecting to database enter
```
connection type:basic
database host name : <your host name>
Port Number:1521
Service name: xepdb1(for demopython or XE for system login)
Role: default
User name: Demopython (or the appropriate username)
Password: <whatever it is>
```


To get the various details first login in to sql plus as demopython

## For Service Name:
```sql
select sys_context('userenv','service_name') from dual;
```


## For host name:

login as SYSDBA:
<br></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If in terminal enter:
```cmd
    sqlplus / as sysdba
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inside sql*plus
```cmd
conn / as sysdba
```
and then execute:
```sql
	SELECT UTL_INADDR.get_host_name FROM dual;
```
paste that host name in vscode
