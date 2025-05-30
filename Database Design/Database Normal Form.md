# Database Normal Form (数据库设计范式)

This is what I first heard about. What is Normal Form?

This is the Rule of database design. How to reduce the data repeat. How to organize all the data. How to reduce the exception occur. It's all used on the RDS.
The target of Normal Form is to keep database structure are Reasonableness and Consistency(合理性和一致性)

## First Normal Format

* every field are all the atom. It's all the value can not be divided.
* All the data type must be the same in one column
* All the field and collection value can not be repeat.

| Student ID | Name | Telephone   |
| ---- | -- | ------ |
| 1    | Tom | 123456 |
| 1    | Tom | 789101 |

This is error design. because the name could not be repeat. you need to separate the telephone  with student table.

## Second Normal Format

* Fit for 1NF
* Each attribute must depend on the Primary Key. not the part depend.

| Order ID（Primary） | Product ID（Primary） | Product Name | Count |
| -------- | -------- | ---- | -- |

Here is against the Second NF. A Count is not depend the primary key.
You should separate this table into two tables:

| Order ID（Primary） | Product ID（Primary） | Count |
|----------|---------|----|

and

| Product ID（Primary） | Product Name |
|----------|---------|

## Third NF

* Fit for 2NF
* It can not pass dependency between not Primary attributes
  (Primary cannot depend other attributes which is not Primary)

| Student ID (PK)| Name| Grade Id| Grade Name|
|------|----|-----|-----|

student id cannot depend grade id. 
Grade Name depend on Grade Id. GradeId depend on StudentID only.
It should separate to:

|StudentId (PK)| Name| GradeId|
|------|-------|-------|

and

| GradeId | GradeName|
|----|----|

## BCNF (Boyce-Codd Normal Form)

* Fit for 3NF
* For all functional dependencies, the determinant must be a CANDIDATE KEY.

## Fourth Normal Form

* Fit for BCNF
* avoid multi value dependency

| StudentID | Interesting | Features |
|----|----|----|

Interest and Features are independent attribute. One Student may have multi Interesting and many Features

## Fifth Normal Form

* avoid connection dependency
* keep every normal connection dependency will decided by CANDIDATE KEY.

It's very complex. not alway  to be used.

## Sixth Normal Form

* avoid all the dependency for all attribute in History Record.
* It's always use to the database with time series(时间序列的数据库)
