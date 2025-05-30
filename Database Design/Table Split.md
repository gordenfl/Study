# Table Split

How to Split the table in the Enterprise system. Alway the table have a lot of data in the table. 

## Methods

* Range-based Sharding
* Hash-based Sharding
* Catalog-base Sharding
* Compose Strategy

## Table Split Layer

All the system logic don't need to deal with Table Split itself. All the divided table can be managed by the middleware, such like ShardingSphere, Mycat, Vitess. It's transparent to the logic layer.

such like:

```sql
SELECT * FROM User WHERE UserId in (1233,4444,556,7778,9999);
```

The middleware will analysis all the condition, divide them into different SQL, send to different SQL server to execute.

Server1:

```sql
SELECT * FROM User_Tbl1 WHERE UserId in (1233);
SELECT * FROM User_Tbl2 WHERE UserId in (4444, 556);
SELECT * FROM User_Tbl3 WHERE UserId in (7778,9999);
```

then combine all the result data together send back to outside.

The middleware will provide a XDBC interface for the logic layer.
you can connect the database such like one database.

```
shadingsphere-proxy:3306
```

Actually, shadingsphere-proxy connection a lot of database(MySQL).

So we dont need to know too detail about each of the middleware.

Give a list of these middleware:

* ShardingSphere: : support split DB, Table, separate the read and write, Elastic extend, support distribute transactions.
* Mycat: based on MySQL protocol. Implement the router analysis with each SQL. It's fix for middle or small system
* Vitess: developed by Google Youtube.