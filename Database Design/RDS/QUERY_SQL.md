# RDS SQL functions

## JOIN
Select data from multi tables based on their logic connection (Primary Key and Foreign Key)

1. INNER JOIN
    only return the record with record common data

    ```sql
    SELECT a.name, b.salary
    FROM employee a 
    INNER JOIN salaries b ON a.emp_id = b.emp_id
    ```

2. LEFT JOIN
    return left table's record, even if there no record matches in the right table. fill all these right table's column with NULL

    

    Student:

    | id | name  |
    | -- | ----- |
    | 1  | Alice |
    | 2  | Bob   |
    | 3  | Carl  |

    Grade:

    | student_id | grade |
    | ----------- | ----- |
    | 1           | A     |
    | 2           | B     |
    | 4           | C     |

    ```sql
    SELECT s.id, s.name, g.grade
    FROM students s
    LEFT JOIN grades g ON s.id = g.student_id;
    ```

    | id | name  | grade |
    | -- | ----- | ----- |
    | 1  | Alice | A     |
    | 2  | Bob   | B     |
    | 3  | Carl  | NULL  |



3. RIGHT JOIN
    return right table's record, even if there no record matches in the right table. fill all these left table's column with NULL.

    ```sql
    SELECT s.id, s.name, g.grade
    FROM students s
    RIGHT JOIN grades g ON s.id = g.student_id;
    ```

    | id   | name  | grade |
    | ---- | ----- | ----- |
    | 1    | Alice | A     |
    | 2    | Bob   | B     |
    | NULL | NULL  | C     |

4. FULL JOIN
    return all the record both in right and left table. fill all these column with NULL if there are no data.

    ```sql
    SELECT s.id, s.name, g.grade
    FROM students s
    LEFT JOIN grades g ON s.id = g.student_id
    UNION
    SELECT s.id, s.name, g.grade
    FROM students s
    RIGHT JOIN grades g ON s.id = g.student_id;
    ```

    | id   | name  | grade |
    | ---- | ----- | ----- |
    | 1    | Alice | A     |
    | 2    | Bob   | B     |
    | 3    | Carl  | NULL  |
    | NULL | NULL  | C     |

## Aggregate Functions

| Function        | Desc   |
| --------- | ---- |
| `COUNT()` | How many record |
| `SUM()`   | sum   |
| `AVG()`   | average value  |
| `MAX()`   | max value  |
| `MIN()`   | min value  |

## Subquery

subquery is a SQL which embedded in another SQL. It can put in:

* WHERE as a condition

```sql
SELECT name
FROM employees
WHERE dept_id IN (SELECT id FROM departments WHERE name = 'Sales');
```

* FROM as a temple table

```sql
SELECT dept, avg_salary
FROM (
  SELECT department AS dept, AVG(salary) AS avg_salary
  FROM employees
  GROUP BY department
) AS dept_avg;
```

* SELECT as an column value

```sql
SELECT 
    emp_id,
    name,
    (SELECT dept_name 
     FROM departments 
     WHERE departments.dept_id = employees.dept_id) AS department_name
FROM employees;
```

## Window Function

| Function Name                         | Description         |
| --------------------------- | ---------- |
| `ROW_NUMBER()`              | Order（Not parallel）  |
| `RANK()`                    | Tied ranking (with jumps)  |
| `DENSE_RANK()`              | Tied ranking (no jump)  |
| `SUM()` / `AVG()` OVER(...) | Calculate cumulative values ​​or group means |
