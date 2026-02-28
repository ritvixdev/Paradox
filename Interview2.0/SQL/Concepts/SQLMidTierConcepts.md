# 🗄️ SQL Interview Preparation Guide

> **Goal:** Read this once and confidently crack any SQL interview.
> All concepts are grouped logically — from basics to advanced, with memory tips and code examples.

---

## 📋 Table of Contents

| # | Section |
|---|---------|
| 1 | [SQL Fundamentals](#1-sql-fundamentals) |
| 2 | [Database Basics — Tables, Fields & Keys](#2-database-basics--tables-fields--keys) |
| 3 | [Constraints](#3-constraints) |
| 4 | [SQL Commands — DDL, DML, DCL, TCL](#4-sql-commands--ddl-dml-dcl-tcl) |
| 5 | [CRUD Operations](#5-crud-operations) |
| 6 | [Filtering — WHERE, HAVING, GROUP BY, ORDER BY](#6-filtering--where-having-group-by-order-by) |
| 7 | [JOINs](#7-joins) |
| 8 | [Subqueries & CTEs](#8-subqueries--ctes) |
| 9 | [Aggregate & Scalar Functions](#9-aggregate--scalar-functions) |
| 10 | [Indexes](#10-indexes) |
| 11 | [Normalization & Denormalization](#11-normalization--denormalization) |
| 12 | [Views](#12-views) |
| 13 | [Stored Procedures & Functions](#13-stored-procedures--functions) |
| 14 | [Triggers](#14-triggers) |
| 15 | [Transactions & ACID Properties](#15-transactions--acid-properties) |
| 16 | [Advanced Concepts](#16-advanced-concepts) |
| 17 | [Security — SQL Injection](#17-security--sql-injection) |
| 18 | [Top Interview Q&A](#18-top-interview-qa) |
| 19 | [Quick Cheatsheet & Memory Tips](#19-quick-cheatsheet--memory-tips) 

---

## 1. SQL Fundamentals

### What is SQL?

**SQL (Structured Query Language)** is the standard language used to **talk to relational databases**. It lets you create, read, update, and delete data.

```
SQL = the language
Database = where data lives
Table = where data is stored (like a spreadsheet)
```

### What is a Database?

A **database** is an **organized collection of structured data** stored electronically. Data is stored in **tables** (rows and columns).

```
+----------+-------+------------------+------+
| book_id  | title | author           | year |
+----------+-------+------------------+------+
| 1        | 1984  | George Orwell    | 1949 |
| 2        | Dune  | Frank Herbert    | 1965 |
+----------+-------+------------------+------+
  ^-- row = 1 record (1 book)
             ^-- column = 1 field (one attribute)
```

### What is DBMS vs RDBMS?

| DBMS | RDBMS |
|---|---|
| Database Management System — general system for managing data | Relational DBMS — data stored in **related tables** |
| Data stored in files or hierarchical structures | Data stored in tables with rows and columns |
| No relationship between data entities | Tables are linked via **primary and foreign keys** |
| Example: XML database, file systems | Example: MySQL, PostgreSQL, Oracle, MS SQL Server |

> **Memory Tip:** RDBMS = DBMS + Relationships between tables.

### What is the Difference Between SQL and MySQL?

| SQL | MySQL |
|---|---|
| A **language** — used to query databases | A **software/database system** — uses SQL as its language |
| Not a product — it's a standard | An open-source RDBMS product by Oracle |
| Works with any relational database | Specific product with its own features and syntax |

> **Analogy:** SQL is like English. MySQL is like a book written in English.

### SQL vs NoSQL

| SQL Database | NoSQL Database |
|---|---|
| Relational (RDBMS) | Non-relational |
| Fixed/static schema — rows & columns | Dynamic schema — JSON, key-value, graph |
| Best for complex queries and joins | Best for large-scale, unstructured data |
| Vertically scalable | Horizontally scalable |
| Examples: MySQL, PostgreSQL, Oracle | Examples: MongoDB, Cassandra, Redis |

---

## 2. Database Basics — Tables, Fields & Keys

### Table and Field

- **Table** — A collection of data organized in rows and columns (like a spreadsheet).
- **Field** — A single column in a table representing one attribute.
- **Record/Row** — A single entry in a table (one complete set of data).

```
employees table:
+----+----------+--------+------------+
| id | name     | salary | department |
+----+----------+--------+------------+
| 1  | Alice    | 70000  | IT         |  <-- one record (row)
| 2  | Bob      | 50000  | HR         |
+----+----------+--------+------------+
       ^-- one field (column)
```

### What is a Primary Key?

A **Primary Key** is a column (or set of columns) that **uniquely identifies each row** in a table.

Rules:
- Must be **UNIQUE** — no two rows can have the same value
- Cannot be **NULL** — must always have a value
- A table can have **only ONE** primary key

```sql
CREATE TABLE employees (
  emp_id   INT PRIMARY KEY,  -- primary key
  name     VARCHAR(100),
  salary   DECIMAL(10,2)
);
```

### What is a Foreign Key?

A **Foreign Key** is a column in one table that **references the Primary Key** of another table. It creates a **relationship** between two tables.

```
employees table              departments table
+---------+------+---------+   +--------+-----------+
| emp_id  | name | dept_id |   | dep_id | dept_name |
+---------+------+---------+   +--------+-----------+
| 1       | Alice| 10      |-->| 10     | IT        |
| 2       | Bob  | 20      |-->| 20     | HR        |
+---------+------+---------+   +--------+-----------+
              dept_id is a FK      dep_id is a PK
```

```sql
CREATE TABLE employees (
  emp_id  INT PRIMARY KEY,
  name    VARCHAR(100),
  dept_id INT,
  FOREIGN KEY (dept_id) REFERENCES departments(dep_id)
);
```

### Primary Key vs Unique Key vs Foreign Key

| | Primary Key | Unique Key | Foreign Key |
|---|---|---|---|
| Uniqueness | Must be unique | Must be unique | Can have duplicates |
| NULL values | NOT allowed | Allowed (one NULL) | Allowed |
| Count per table | Only ONE | Multiple allowed | Multiple allowed |
| Purpose | Identify rows | Prevent duplicates | Link two tables |

### What is Data Integrity?

**Data integrity** means ensuring data is **accurate, consistent, and reliable** throughout its lifecycle. Enforced through:
- **Primary keys** — no duplicate rows
- **Foreign keys** — referential integrity between tables
- **Constraints** — rules on what data can be stored
- **Transactions** — ACID properties

### What is a NULL value in SQL?

**NULL** means **the absence of a value** — it is not zero, not empty string, just "unknown" or "missing".

```sql
-- NULL is NOT equal to 0 or ''
SELECT * FROM employees WHERE salary IS NULL;     -- correct
SELECT * FROM employees WHERE salary = NULL;      -- WRONG! Never use = with NULL

-- Use IS NULL or IS NOT NULL
SELECT * FROM employees WHERE email IS NOT NULL;
```

> **Memory Tip:** NULL = "nothing recorded here" — not zero, not blank.

---

## 3. Constraints

### What is a Constraint?

A **constraint** is a **rule applied to a column or table** to ensure data accuracy and consistency.

```
+------------------+
|  CONSTRAINT TYPES|
+------------------+
| NOT NULL         | -- value cannot be empty
| UNIQUE           | -- no duplicate values
| PRIMARY KEY      | -- unique + not null
| FOREIGN KEY      | -- links to another table
| CHECK            | -- value must meet a condition
| DEFAULT          | -- default value if none provided
+------------------+
```

### All Constraints with Examples

```sql
CREATE TABLE employees (
  emp_id     INT          PRIMARY KEY,           -- unique + not null
  name       VARCHAR(100) NOT NULL,              -- cannot be empty
  email      VARCHAR(200) UNIQUE,                -- no duplicates
  salary     DECIMAL(10,2) CHECK (salary > 0),   -- must be positive
  dept_id    INT          DEFAULT 1,             -- default value if not provided
  manager_id INT,
  FOREIGN KEY (manager_id) REFERENCES employees(emp_id)  -- links to same table
);
```

### Column-level vs Table-level Constraints

| Column-level | Table-level |
|---|---|
| Defined alongside the column | Defined after all columns |
| Applies to a single column | Can apply to multiple columns |
| `salary DECIMAL CHECK (salary > 0)` | `CONSTRAINT pk PRIMARY KEY (emp_id, name)` |

---

## 4. SQL Commands — DDL, DML, DCL, TCL

### Overview of SQL Command Types

```
SQL Commands
|
+-- DDL (Data Definition Language)  -- defines structure
|   CREATE, ALTER, DROP, TRUNCATE, RENAME
|
+-- DML (Data Manipulation Language) -- manipulates data
|   SELECT, INSERT, UPDATE, DELETE
|
+-- DCL (Data Control Language)     -- controls access
|   GRANT, REVOKE
|
+-- TCL (Transaction Control Language) -- controls transactions
    COMMIT, ROLLBACK, SAVEPOINT
```

### DDL Commands

```sql
-- CREATE — create a new table
CREATE TABLE products (
  id    INT PRIMARY KEY,
  name  VARCHAR(100),
  price DECIMAL(10,2)
);

-- ALTER — modify an existing table
ALTER TABLE products ADD COLUMN stock INT;
ALTER TABLE products DROP COLUMN stock;
ALTER TABLE products MODIFY COLUMN price FLOAT;

-- DROP — permanently delete table + all data
DROP TABLE products;

-- TRUNCATE — delete all data but keep table structure
TRUNCATE TABLE products;

-- RENAME — rename a table
RENAME TABLE products TO items;
```

### DML Commands

```sql
-- INSERT — add new rows
INSERT INTO products (id, name, price) VALUES (1, 'Laptop', 999.99);

-- SELECT — read data
SELECT name, price FROM products WHERE price > 500;

-- UPDATE — modify existing rows
UPDATE products SET price = 899.99 WHERE id = 1;

-- DELETE — remove specific rows
DELETE FROM products WHERE id = 1;
```

### DCL Commands

```sql
-- GRANT — give user permission
GRANT SELECT, INSERT ON products TO user_name;

-- REVOKE — remove user permission
REVOKE INSERT ON products FROM user_name;
```

### TCL Commands

```sql
-- COMMIT — permanently save changes
COMMIT;

-- ROLLBACK — undo changes since last COMMIT
ROLLBACK;

-- SAVEPOINT — create a checkpoint to roll back to
SAVEPOINT before_update;
UPDATE employees SET salary = 80000 WHERE emp_id = 1;
ROLLBACK TO before_update;  -- undo only back to savepoint
```

### DELETE vs TRUNCATE vs DROP — Most Common Interview Question

```
+----------+------------------+-------------------+------------------+
| Command  | What it does     | Rollback possible?| Speed            |
+----------+------------------+-------------------+------------------+
| DELETE   | Remove specific  | YES (DML)         | Slower (logs     |
|          | rows (with WHERE)|                   | each row)        |
+----------+------------------+-------------------+------------------+
| TRUNCATE | Remove ALL rows  | NO (auto-commit)  | Faster (no logs) |
|          | keep structure   |                   |                  |
+----------+------------------+-------------------+------------------+
| DROP     | Remove entire    | NO                | Fastest          |
|          | table + data     |                   | (gone forever)   |
+----------+------------------+-------------------+------------------+
```

```sql
DELETE FROM employees WHERE dept_id = 5;  -- deletes only dept 5
TRUNCATE TABLE employees;                 -- deletes ALL employees
DROP TABLE employees;                     -- deletes the whole table
```

> **Memory Tip:** DELETE = remove selected rows | TRUNCATE = wipe all rows | DROP = destroy the whole table.

---

## 5. CRUD Operations

### SELECT Statement

```sql
-- Basic SELECT
SELECT name, salary FROM employees;

-- Select all columns
SELECT * FROM employees;           -- avoid in production (fetches everything)

-- With alias (temporary rename)
SELECT first_name AS "First Name", salary AS "Annual Salary"
FROM employees;

-- With DISTINCT (remove duplicates)
SELECT DISTINCT department FROM employees;

-- With WHERE filter
SELECT * FROM employees WHERE salary > 60000;

-- With ORDER BY
SELECT name, salary FROM employees ORDER BY salary DESC;

-- With LIMIT
SELECT * FROM employees ORDER BY salary DESC LIMIT 5;
```

### INSERT Statement

```sql
-- Insert a single row
INSERT INTO employees (emp_id, name, salary) VALUES (1, 'Alice', 70000);

-- Insert multiple rows at once
INSERT INTO employees (emp_id, name, salary) VALUES
  (2, 'Bob',   50000),
  (3, 'Carol', 90000);

-- Insert with NULL
INSERT INTO employees (emp_id, name, salary, email) VALUES (4, 'Dave', 60000, NULL);
```

### UPDATE Statement

```sql
-- Update specific rows
UPDATE employees SET salary = 80000 WHERE emp_id = 1;

-- Update multiple columns
UPDATE employees SET salary = 75000, department = 'IT' WHERE name = 'Bob';

-- Update all rows (dangerous! no WHERE)
UPDATE employees SET bonus = 1000;
```

### DELETE Statement

```sql
-- Delete specific rows
DELETE FROM employees WHERE emp_id = 3;

-- Delete with condition
DELETE FROM employees WHERE salary < 30000;
```

---

## 6. Filtering — WHERE, HAVING, GROUP BY, ORDER BY

### WHERE Clause

**WHERE** filters **individual rows** before any grouping or aggregation. It works on raw column values.

```sql
-- Comparison
SELECT * FROM employees WHERE salary > 50000;
SELECT * FROM employees WHERE department = 'IT';

-- Multiple conditions
SELECT * FROM employees WHERE salary > 50000 AND department = 'IT';
SELECT * FROM employees WHERE department = 'IT' OR department = 'HR';

-- BETWEEN (inclusive)
SELECT * FROM employees WHERE salary BETWEEN 40000 AND 80000;

-- IN (match any value in list)
SELECT * FROM employees WHERE department IN ('IT', 'HR', 'Finance');

-- LIKE (pattern matching)
SELECT * FROM employees WHERE name LIKE 'A%';    -- starts with A
SELECT * FROM employees WHERE name LIKE '%son';  -- ends with son
SELECT * FROM employees WHERE name LIKE '_a%';   -- second letter is a

-- IS NULL / IS NOT NULL
SELECT * FROM employees WHERE email IS NULL;
```

### GROUP BY Clause

**GROUP BY** groups rows with the same values into summary rows (like grouping all IT employees together to count them).

```sql
-- Count employees per department
SELECT department, COUNT(*) AS emp_count
FROM employees
GROUP BY department;

-- Average salary per department
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
```

### HAVING Clause

**HAVING** filters **groups** after aggregation (like WHERE but for grouped results).

```sql
-- Only departments with more than 5 employees
SELECT department, COUNT(*) AS emp_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;

-- Departments with average salary over 60000
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;
```

### WHERE vs HAVING — Most Asked Interview Question

```
+------------+-------------------------------+-----------------------------+
|            | WHERE                         | HAVING                      |
+------------+-------------------------------+-----------------------------+
| Filters    | Individual rows               | Groups (after GROUP BY)     |
| Timing     | BEFORE grouping               | AFTER grouping              |
| Aggregate  | CANNOT use aggregate          | CAN use aggregate functions |
| functions  | functions (SUM, AVG, etc.)    | (SUM, COUNT, AVG, etc.)     |
| GROUP BY   | Can be used without GROUP BY  | Cannot be used without      |
| required   |                               | GROUP BY                    |
+------------+-------------------------------+-----------------------------+
```

```sql
-- WHERE filters rows first, then GROUP BY groups, then HAVING filters groups
SELECT department, AVG(salary)
FROM employees
WHERE hire_date > '2020-01-01'     -- first: filter rows
GROUP BY department                -- second: group them
HAVING AVG(salary) > 60000;        -- third: filter groups
```

> **Memory Tip:** WHERE = "filter before cooking" | HAVING = "filter after cooking"

### ORDER BY Clause

```sql
SELECT name, salary FROM employees
ORDER BY salary DESC;         -- descending (highest first)

ORDER BY salary ASC;          -- ascending (lowest first)

ORDER BY department, salary DESC;  -- multiple columns
```

### Full Query Order

```sql
-- This is the order SQL processes clauses:
SELECT column(s)          -- 5. select output columns
FROM table                -- 1. get data from table
JOIN other_table ...      -- 2. join tables
WHERE condition           -- 3. filter rows
GROUP BY column           -- 4. group rows
HAVING condition          -- 6. filter groups
ORDER BY column           -- 7. sort results
LIMIT n;                  -- 8. limit output

-- Memory: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT
```

---

## 7. JOINs

### What is a JOIN?

A **JOIN** combines rows from two or more tables based on a **related column** between them.

### Visual Guide to All JOIN Types

```
   TABLE A          TABLE B
 +---------+      +---------+
 | 1 Alice |      | 1 IT    |
 | 2 Bob   |      | 3 HR    |
 | 4 Carol |      | 4 Finance|
 +---------+      +---------+

 INNER JOIN               LEFT JOIN
 (only matching)          (all A + matches from B)
 +---+-------+---+        +---+-------+---------+
 | 1 | Alice | IT|        | 1 | Alice | IT      |
 | 4 | Carol |Fin|        | 2 | Bob   | NULL    |
 +---+-------+---+        | 4 | Carol | Finance |
                          +---+-------+---------+
 RIGHT JOIN               FULL OUTER JOIN
 (all B + matches from A) (all from both)
 +---+-------+---------+  +---+-------+---------+
 | 1 | Alice | IT      |  | 1 | Alice | IT      |
 | 4 | Carol | Finance |  | 2 | Bob   | NULL    |
 | 3 | NULL  | HR      |  | 3 | NULL  | HR      |
 +---+-------+---------+  | 4 | Carol | Finance |
                          +---+-------+---------+
```

### All JOIN Types with SQL

```sql
-- INNER JOIN — only matching rows in BOTH tables
SELECT e.name, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;

-- LEFT JOIN — all rows from LEFT table + matches from right (NULL if no match)
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;

-- RIGHT JOIN — all rows from RIGHT table + matches from left (NULL if no match)
SELECT e.name, d.dept_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id;

-- FULL OUTER JOIN — all rows from BOTH tables (NULL where no match)
SELECT e.name, d.dept_name
FROM employees e
FULL OUTER JOIN departments d ON e.dept_id = d.dept_id;

-- CROSS JOIN — every row in A combined with every row in B (cartesian product)
SELECT e.name, d.dept_name
FROM employees e
CROSS JOIN departments d;
-- If employees has 5 rows and departments has 3, result = 5 x 3 = 15 rows

-- SELF JOIN — join a table with itself (useful for hierarchies)
SELECT e.name AS employee, m.name AS manager
FROM employees e
JOIN employees m ON e.manager_id = m.emp_id;

-- NATURAL JOIN — automatically joins on columns with same name
SELECT * FROM employees NATURAL JOIN departments;
```

### CROSS JOIN vs NATURAL JOIN

| CROSS JOIN | NATURAL JOIN |
|---|---|
| Returns the **Cartesian product** — every row from A combined with every row from B | Automatically joins on **columns with the same name** in both tables |
| No ON condition needed | No ON condition needed |
| Result = rows in A × rows in B | Result = only matching rows based on common columns |
| Rarely used in practice | Convenient but risky if column names match unexpectedly |

### Joins Venn Diagram (Text Version)

```
INNER JOIN:         LEFT JOIN:          RIGHT JOIN:
   A ∩ B               A ∪ (A∩B)           B ∪ (A∩B)
  +-----+             +--------+           +--------+
  | A|B |             |  A |B  |           |  A|B   |
  +-----+             +--------+           +--------+
  (overlap)          (all left)           (all right)

FULL OUTER JOIN:    CROSS JOIN:
   A ∪ B               A × B
 +----------+        +---------+
 |   A  B   |        |all combo|
 +----------+        +---------+
  (everything)      (cartesian)
```

---

## 8. Subqueries & CTEs

### What is a Subquery?

A **subquery** is a query nested **inside another query**. The inner query runs first and passes its result to the outer query.

```sql
-- Find employees earning more than the average salary
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
--              ^--- subquery runs first, returns a number
```

### Types of Subqueries

```
Subquery Types
|
+-- Single-row subquery     -- returns ONE row
|   WHERE salary = (SELECT MAX(salary) FROM employees)
|
+-- Multi-row subquery      -- returns MULTIPLE rows
|   WHERE dept_id IN (SELECT dept_id FROM departments WHERE location = 'NY')
|
+-- Correlated subquery     -- references outer query
|   WHERE salary > (SELECT AVG(salary) FROM employees e2
|                   WHERE e2.dept_id = e1.dept_id)  <- references outer table
|
+-- Scalar subquery         -- returns single value used as a column
    SELECT name, (SELECT AVG(salary) FROM employees) AS avg_sal FROM employees
```

### Correlated Subquery vs Regular Subquery

| Regular Subquery | Correlated Subquery |
|---|---|
| Runs **once** independently | Runs **once per row** of outer query |
| Doesn't reference outer query | References columns from outer query |
| Generally faster | Generally slower |

```sql
-- Correlated subquery: find employees earning more than dept average
SELECT e1.name, e1.salary, e1.department
FROM employees e1
WHERE e1.salary > (
  SELECT AVG(e2.salary)
  FROM employees e2
  WHERE e2.department = e1.department  -- references outer query!
);
```

### CTEs — Common Table Expressions

A **CTE (WITH clause)** creates a **named temporary result set** you can reference in the main query. Makes complex queries more readable.

```sql
-- Without CTE (hard to read):
SELECT name FROM (
  SELECT name, RANK() OVER (ORDER BY salary DESC) AS rnk FROM employees
) ranked WHERE rnk = 2;

-- With CTE (easy to read):
WITH ranked_employees AS (
  SELECT name, salary,
         RANK() OVER (ORDER BY salary DESC) AS rnk
  FROM employees
)
SELECT name, salary
FROM ranked_employees
WHERE rnk = 2;
```

### Multiple CTEs

```sql
WITH
  high_earners AS (
    SELECT * FROM employees WHERE salary > 80000
  ),
  it_dept AS (
    SELECT * FROM departments WHERE dept_name = 'IT'
  )
SELECT h.name, h.salary
FROM high_earners h
JOIN it_dept d ON h.dept_id = d.dept_id;
```

### IN vs EXISTS — Interview Favourite

| `IN` | `EXISTS` |
|---|---|
| Compares against a **list** of values | Checks if a **row exists** in a subquery |
| Works on result lists | Works with correlated subqueries |
| Compares **every value** in the list | **Stops** as soon as a match is found |
| Slower for large result sets | Faster for large result sets |

```sql
-- IN: find employees in specific departments
SELECT name FROM employees
WHERE dept_id IN (SELECT dept_id FROM departments WHERE location = 'NY');

-- EXISTS: same query using EXISTS (faster for large datasets)
SELECT name FROM employees e
WHERE EXISTS (
  SELECT 1 FROM departments d
  WHERE d.dept_id = e.dept_id AND d.location = 'NY'
);
```

> **Memory Tip:** Use `IN` for small, known lists. Use `EXISTS` for large subqueries.

### Joins vs Subqueries — When to Use Each

| Use JOINs When | Use Subqueries When |
|---|---|
| You need columns from multiple tables | You only need columns from the main table |
| Performance matters (JOINs are usually faster) | Logic is cleaner as a nested query |
| Combining data from related tables | Using aggregate results as a filter |

---

## 9. Aggregate & Scalar Functions

### Aggregate Functions

**Aggregate functions** operate on **groups of rows** and return a **single result**.

```
+----------+----------------------------------------+
| Function | Purpose                                |
+----------+----------------------------------------+
| COUNT(*) | Count ALL rows (including NULLs)       |
| COUNT(col)| Count non-NULL values in a column     |
| SUM(col) | Total sum of numeric values            |
| AVG(col) | Average of numeric values              |
| MIN(col) | Smallest value                         |
| MAX(col) | Largest value                          |
+----------+----------------------------------------+
```

```sql
SELECT
  COUNT(*)              AS total_rows,     -- counts ALL rows
  COUNT(email)          AS rows_with_email,-- counts non-NULL emails
  SUM(salary)           AS total_payroll,
  AVG(salary)           AS avg_salary,
  MIN(salary)           AS lowest_salary,
  MAX(salary)           AS highest_salary
FROM employees;
```

### COUNT(*) vs COUNT(column) — Interview Favourite

```sql
-- Table: employees
-- +----+-------+--------+
-- | id | name  | email  |
-- +----+-------+--------+
-- | 1  | Alice | a@b.com|
-- | 2  | Bob   | NULL   |  <- email is NULL
-- | 3  | Carol | c@d.com|
-- +----+-------+--------+

SELECT COUNT(*)     FROM employees;  -- result: 3 (counts ALL rows)
SELECT COUNT(email) FROM employees;  -- result: 2 (ignores NULL)
```

> **Memory Tip:** `COUNT(*)` = count all rows. `COUNT(col)` = count non-null values.

### Scalar Functions

**Scalar functions** operate on **individual values** and return one value per row.

```sql
-- String functions
SELECT UPPER('hello');           -- HELLO
SELECT LOWER('HELLO');           -- hello
SELECT LENGTH('hello');          -- 5
SELECT TRIM('  hello  ');        -- 'hello'
SELECT SUBSTRING('hello', 1, 3); -- 'hel'
SELECT CONCAT('Hello', ' ', 'World'); -- 'Hello World'
SELECT LEFT('Hello', 3);         -- 'Hel'
SELECT RIGHT('Hello', 3);        -- 'llo'
SELECT REPLACE('Hello', 'l', 'r'); -- 'Herro'

-- Numeric functions
SELECT ROUND(3.14159, 2);  -- 3.14
SELECT CEIL(3.2);          -- 4
SELECT FLOOR(3.9);         -- 3
SELECT ABS(-5);            -- 5

-- Date functions
SELECT NOW();              -- current date + time
SELECT CURDATE();          -- current date only
SELECT YEAR(NOW());        -- current year
SELECT DATEDIFF('2024-12-31', '2024-01-01'); -- days between dates

-- COALESCE — returns first non-NULL value
SELECT COALESCE(email, phone, 'No contact') AS contact FROM employees;
-- If email is NULL, use phone. If both NULL, use 'No contact'

-- CASE WHEN — conditional logic
SELECT name,
  CASE
    WHEN salary > 80000 THEN 'Senior'
    WHEN salary > 50000 THEN 'Mid-level'
    ELSE 'Junior'
  END AS level
FROM employees;

-- NULLIF — returns NULL if two values are equal
SELECT NULLIF(10, 10);  -- NULL (they're equal)
SELECT NULLIF(10, 5);   -- 10 (they're different)
```

### Window Functions (Advanced)

**Window functions** perform calculations **across related rows** without collapsing them like GROUP BY does.

```sql
-- RANK() — rank employees by salary (gaps in ranking for ties)
SELECT name, salary,
  RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;

-- DENSE_RANK() — rank with no gaps
SELECT name, salary,
  DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
FROM employees;

-- ROW_NUMBER() — unique row number
SELECT name,
  ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
FROM employees;

-- PARTITION BY — rank within each department
SELECT name, department, salary,
  RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;

-- LAG / LEAD — compare with previous/next row
SELECT name, salary,
  LAG(salary, 1) OVER (ORDER BY emp_id)  AS prev_salary,
  LEAD(salary, 1) OVER (ORDER BY emp_id) AS next_salary
FROM employees;
```

---

## 10. Indexes

### What is an Index?

An **index** is a data structure that provides a **fast way to look up data** in a table — like the index at the back of a book. Without an index, SQL scans every row (full table scan).

```
Without Index:       With Index on "name":
Scan all rows        Jump directly to result
+----+-------+       name index:
| 1  | Alice |       Alice -> row 1
| 2  | Bob   |  -->  Bob   -> row 2
| 3  | Carol |       Carol -> row 3
| .. | ...   |
(slow for big tables) (fast lookup)
```

```sql
-- Create an index
CREATE INDEX idx_employee_name ON employees(name);

-- Create a unique index
CREATE UNIQUE INDEX idx_email ON employees(email);

-- Multi-column (composite) index
CREATE INDEX idx_dept_salary ON employees(department, salary);

-- Drop an index
DROP INDEX idx_employee_name;

-- Automatic: PRIMARY KEY always creates a unique clustered index
```

### Clustered vs Non-Clustered Index

```
+---------------------+----------------------------+----------------------------+
|                     | Clustered Index            | Non-Clustered Index        |
+---------------------+----------------------------+----------------------------+
| Data storage        | Data physically sorted     | Separate structure with    |
|                     | by index order             | pointers to actual data    |
+---------------------+----------------------------+----------------------------+
| Count per table     | Only ONE                   | Multiple allowed           |
+---------------------+----------------------------+----------------------------+
| Speed               | Faster for range queries   | Faster for exact lookups   |
+---------------------+----------------------------+----------------------------+
| Example             | PRIMARY KEY                | INDEX on email column      |
+---------------------+----------------------------+----------------------------+
```

```
Clustered Index (data IS the index):         Non-Clustered Index (separate structure):
+----+-------+--------+                      +-------+----------+
| 1  | Alice | IT     |  <-- stored in        | Alice | -> Row 1 |
| 2  | Bob   | HR     |     sorted order      | Bob   | -> Row 2 |
| 3  | Carol | Finance|                       | Carol | -> Row 3 |
+----+-------+--------+                      +-------+----------+
                                              (index) (pointer to data)
```

> **Memory Tip:** Clustered = data sorted like a phone book. Non-Clustered = index at the back of a textbook with page numbers.

### When to Use Indexes

**Use indexes on:**
- Columns used frequently in `WHERE`, `JOIN ON`, `ORDER BY`
- Primary and foreign key columns
- High-cardinality columns (many unique values like email, ID)

**Avoid indexes on:**
- Small tables (full scan is faster)
- Columns that are updated very frequently
- Low-cardinality columns (like gender: only 2-3 values)

---

## 11. Normalization & Denormalization

### What is Normalization?

**Normalization** is the process of **organizing data to reduce redundancy** (duplicate data) and improve data integrity. It splits large tables into smaller, related tables.

```
BEFORE normalization (one big messy table):
+--------+-------+--------+----------+---------+
| emp_id | name  | salary | dept_name| location|
+--------+-------+--------+----------+---------+
| 1      | Alice | 70000  | IT       | Mumbai  |
| 2      | Bob   | 50000  | IT       | Mumbai  |  <- IT/Mumbai duplicated!
| 3      | Carol | 90000  | HR       | Delhi   |
+--------+-------+--------+----------+---------+

AFTER normalization (split into 2 clean tables):
employees:                  departments:
+--------+-------+--------+  +--------+----------+---------+
| emp_id | name  | dept_id|  | dept_id| dept_name| location|
+--------+-------+--------+  +--------+----------+---------+
| 1      | Alice | 10     |  | 10     | IT       | Mumbai  |
| 2      | Bob   | 10     |  | 20     | HR       | Delhi   |
| 3      | Carol | 20     |  +--------+----------+---------+
+--------+-------+--------+
```

### Normal Forms

```
+------+------------------+-------------------------------------------+
| Form | Name             | Rule                                      |
+------+------------------+-------------------------------------------+
| 1NF  | First Normal Form | - Each column must have ATOMIC values    |
|      |                  | - No repeating groups or arrays            |
|      |                  | - Each row must be unique                  |
+------+------------------+-------------------------------------------+
| 2NF  | Second Normal    | - Must be in 1NF                          |
|      | Form             | - No PARTIAL DEPENDENCY                    |
|      |                  | (non-key columns must depend on FULL key)  |
+------+------------------+-------------------------------------------+
| 3NF  | Third Normal     | - Must be in 2NF                          |
|      | Form             | - No TRANSITIVE DEPENDENCY                 |
|      |                  | (non-key columns must depend ONLY on PK)   |
+------+------------------+-------------------------------------------+
| BCNF | Boyce-Codd       | - Stricter version of 3NF                 |
|      | Normal Form      | - Every determinant must be a candidate key|
+------+------------------+-------------------------------------------+
```

**1NF Example — Atomic Values:**
```
NOT in 1NF:                    IN 1NF:
+------+------------+          +------+--------+
| id   | hobbies    |          | id   | hobby  |
+------+------------+          +------+--------+
| 1    | read, swim |  -->     | 1    | read   |
+------+------------+          | 1    | swim   |
(not atomic! list in 1 cell)   +------+--------+
```

**2NF Example — No Partial Dependency:**
```
NOT in 2NF (composite PK: order_id + product_id):
+----------+------------+-----------+----------+
| order_id | product_id | quantity  | price    |
+----------+------------+-----------+----------+
| price depends on product_id ALONE (not full composite key) -> bad!

IN 2NF (split into 2 tables):
orders_products table:         products table:
order_id | product_id | qty     product_id | price
```

### Denormalization

**Denormalization** is the opposite — **intentionally adding redundancy** to improve read/query performance.

```
Use denormalization when:
- Read-heavy workloads (data warehouse, reporting)
- Query performance is more important than storage
- Data is mostly static (rarely updated)
- You want to avoid complex JOINs for speed
```

---

## 12. Views

### What is a View?

A **view** is a **saved SELECT query** that acts like a virtual table. It doesn't store data — it shows a live result of the underlying query.

```
Real Table: employees          View: it_employees
+----+-------+------+----------+ +----+-------+--------+
| id | name  | sal  | dept     | | id | name  | salary |
+----+-------+------+----------+ +----+-------+--------+
| 1  | Alice | 70000| IT       | | 1  | Alice | 70000  |
| 2  | Bob   | 50000| HR       | | 3  | Carol | 90000  |
| 3  | Carol | 90000| IT       | +----+-------+--------+
+----+-------+------+----------+  (virtual table - no actual data stored)
```

```sql
-- Create a view
CREATE VIEW it_employees AS
  SELECT emp_id, name, salary
  FROM employees
  WHERE department = 'IT';

-- Use it like a table
SELECT * FROM it_employees;
SELECT * FROM it_employees WHERE salary > 80000;

-- Update a view
CREATE OR REPLACE VIEW it_employees AS
  SELECT emp_id, name, salary, hire_date
  FROM employees
  WHERE department = 'IT';

-- Drop a view
DROP VIEW it_employees;
```

### Why Use Views?

1. **Security** — Hide sensitive columns (e.g., hide salary from some users)
2. **Simplicity** — Save complex queries for reuse
3. **Consistency** — Ensure all users see the same version of complex data
4. **Abstraction** — Hide underlying table complexity

---

## 13. Stored Procedures & Functions

### What is a Stored Procedure?

A **stored procedure** is a **saved, precompiled set of SQL statements** that can be executed together. Think of it as a reusable SQL script stored in the database.

```sql
-- Create a stored procedure
CREATE PROCEDURE GetEmployeeByDept(IN dept_name VARCHAR(100))
BEGIN
  SELECT emp_id, name, salary
  FROM employees
  WHERE department = dept_name;
END;

-- Execute the procedure
CALL GetEmployeeByDept('IT');
```

### Stored Procedure with Logic

```sql
CREATE PROCEDURE GiveRaise(
  IN emp_id_param INT,
  IN raise_percent DECIMAL(5,2)
)
BEGIN
  DECLARE current_salary DECIMAL(10,2);

  SELECT salary INTO current_salary
  FROM employees WHERE emp_id = emp_id_param;

  UPDATE employees
  SET salary = current_salary * (1 + raise_percent/100)
  WHERE emp_id = emp_id_param;

  SELECT CONCAT('New salary: ', salary) AS result
  FROM employees WHERE emp_id = emp_id_param;
END;

CALL GiveRaise(1, 10);  -- give employee 1 a 10% raise
```

### Advantages and Disadvantages of Stored Procedures

| Advantages | Disadvantages |
|---|---|
| Improved performance (precompiled) | Hard to debug |
| Reusable across applications | Database-specific syntax |
| Reduced network traffic | Can become very complex |
| Encapsulates business logic | Version control is tricky |
| Security — users don't need direct table access | Harder to unit test |

### User-Defined Functions (UDF)

**Functions** always **return a value** and can be used inline in SELECT queries — unlike stored procedures.

```sql
-- Create a scalar function
CREATE FUNCTION GetAnnualSalary(monthly DECIMAL(10,2))
RETURNS DECIMAL(10,2)
BEGIN
  RETURN monthly * 12;
END;

-- Use it in a query
SELECT name, GetAnnualSalary(salary) AS annual_salary FROM employees;
```

### Stored Procedure vs Function

| Stored Procedure | Function |
|---|---|
| Does NOT have to return a value | MUST return a value |
| Cannot be used inside SELECT | Can be used inside SELECT |
| Can have DML operations | Usually no DML |
| Called with CALL | Called inline |
| Can have IN, OUT, INOUT params | Usually only IN params |

### Recursive Stored Procedure

A **recursive stored procedure** calls itself — useful for hierarchical data like org charts.

```sql
CREATE PROCEDURE GetOrgChart(IN mgr_id INT, IN level INT)
BEGIN
  SELECT emp_id, name, level FROM employees WHERE manager_id = mgr_id;
  -- recursively call for each employee found...
END;
```

---

## 14. Triggers

### What is a Trigger?

A **trigger** is a **set of SQL statements that automatically executes** in response to a specific event (INSERT, UPDATE, or DELETE) on a table.

```
Normal Flow:               With Trigger:
User INSERT row      -->   Trigger fires automatically
                           -> validates data
                           -> logs the action
                           -> updates related tables
```

```sql
-- Trigger that logs every salary update
CREATE TRIGGER log_salary_change
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
  IF OLD.salary <> NEW.salary THEN
    INSERT INTO salary_audit (emp_id, old_salary, new_salary, changed_at)
    VALUES (NEW.emp_id, OLD.salary, NEW.salary, NOW());
  END IF;
END;
```

### Types of Triggers

| Type | When it fires |
|---|---|
| `BEFORE INSERT` | Before a new row is inserted |
| `AFTER INSERT` | After a new row is inserted |
| `BEFORE UPDATE` | Before a row is updated |
| `AFTER UPDATE` | After a row is updated |
| `BEFORE DELETE` | Before a row is deleted |
| `AFTER DELETE` | After a row is deleted |

### Why Use Triggers?

1. **Auditing** — Log who changed what and when
2. **Data consistency** — Automatically update related tables
3. **Validation** — Enforce complex business rules
4. **Automation** — Automate repetitive tasks

---

## 15. Transactions & ACID Properties

### What is a Transaction?

A **transaction** is a **group of SQL operations** that are treated as a **single unit** — either ALL succeed or ALL fail. This ensures database integrity.

```
Transfer $100 from Alice to Bob:
Step 1: Deduct $100 from Alice  --|
Step 2: Add $100 to Bob         --|- these 2 MUST succeed together
                                    or BOTH must fail (no half-completed state)
```

```sql
-- Transaction example
START TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;  -- deduct
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;  -- add

-- If everything is OK:
COMMIT;

-- If something went wrong:
ROLLBACK;
```

### ACID Properties

```
+-------------+-----------------------------------------------------+
| Property    | What it means                                       |
+-------------+-----------------------------------------------------+
| Atomicity   | ALL or NOTHING — if one step fails, all fail        |
|             | "The transaction is atomic — indivisible"           |
+-------------+-----------------------------------------------------+
| Consistency | Data remains VALID before and after transaction     |
|             | Rules/constraints must still be met after commit    |
+-------------+-----------------------------------------------------+
| Isolation   | Concurrent transactions DON'T interfere each other |
|             | Each transaction sees a consistent snapshot         |
+-------------+-----------------------------------------------------+
| Durability  | Committed changes are PERMANENT — survive crashes   |
|             | Stored to disk, not just memory                     |
+-------------+-----------------------------------------------------+
```

> **Memory Trick:** **A**ll **C**ommitted **I**n **D**isk = ACID

### What is a Deadlock?

A **deadlock** occurs when **two or more transactions are waiting for each other** to release locks — creating a standoff where neither can proceed.

```
Transaction A holds lock on Table1, waiting for Table2
Transaction B holds lock on Table2, waiting for Table1
   --> Neither can proceed = DEADLOCK!
```

**How to prevent deadlocks:**
1. Always lock tables in the **same order** across all transactions
2. Use **shorter transactions** (commit quickly)
3. Use **timeouts** — abort if waiting too long
4. Use **deadlock detection** algorithms

---

## 16. Advanced Concepts

### UNION vs UNION ALL

| UNION | UNION ALL |
|---|---|
| Combines results + **removes duplicates** | Combines results + **keeps duplicates** |
| Slower (has to check for duplicates) | Faster (no duplicate removal) |
| Use when you need unique results | Use when duplicates are OK or won't exist |

```sql
-- Returns unique departments from both tables
SELECT department FROM employees
UNION
SELECT department FROM contractors;

-- Returns all departments including duplicates
SELECT department FROM employees
UNION ALL
SELECT department FROM contractors;
```

### CHAR vs VARCHAR

| CHAR | VARCHAR |
|---|---|
| Fixed length — always uses the defined size | Variable length — uses only what's needed |
| `CHAR(10)` stores 'Hi' as 'Hi        ' (padded with spaces) | `VARCHAR(10)` stores 'Hi' as 'Hi' |
| Faster for fixed-length data | More efficient for variable-length data |
| Use for: phone numbers, country codes, fixed IDs | Use for: names, emails, descriptions |

### SQL Data Types

```
Numeric:       INT, BIGINT, DECIMAL(10,2), FLOAT, DOUBLE
Text:          VARCHAR(n), CHAR(n), TEXT, LONGTEXT
Date/Time:     DATE, TIME, DATETIME, TIMESTAMP
Boolean:       BOOLEAN (stored as 0 or 1 in MySQL)
Binary:        BINARY, BLOB, IMAGE
Other:         JSON, XML, ENUM
```

### LIKE Operator — Pattern Matching

```sql
-- % = zero or more characters
SELECT * FROM employees WHERE name LIKE 'A%';     -- starts with A
SELECT * FROM employees WHERE name LIKE '%son';   -- ends with son
SELECT * FROM employees WHERE name LIKE '%ar%';   -- contains ar

-- _ = exactly one character
SELECT * FROM employees WHERE name LIKE '_ob';    -- 3 chars, ends with ob (Bob)
SELECT * FROM employees WHERE name LIKE 'J__n';   -- 4 chars, J??n (John, Joan)
```

### STUFF vs REPLACE

```sql
-- STUFF — delete part of a string and insert another string
STUFF('Hello World', 7, 5, 'SQL')   -- 'Hello SQL' (replace 'World' at pos 7)

-- REPLACE — replace ALL occurrences of a substring
REPLACE('Hello World', 'World', 'SQL')  -- 'Hello SQL'
```

### SET Operators

```sql
-- UNION: unique rows from both
-- UNION ALL: all rows including duplicates
-- INTERSECT: only rows that exist in BOTH results
-- EXCEPT (or MINUS): rows in first result but NOT in second

SELECT emp_id FROM employees
INTERSECT
SELECT emp_id FROM managers;

SELECT emp_id FROM employees
EXCEPT
SELECT emp_id FROM managers;
```

### AUTO_INCREMENT / IDENTITY

```sql
-- MySQL: AUTO_INCREMENT
CREATE TABLE employees (
  emp_id INT AUTO_INCREMENT PRIMARY KEY,
  name   VARCHAR(100)
);
INSERT INTO employees (name) VALUES ('Alice');  -- emp_id = 1 automatically

-- SQL Server: IDENTITY
CREATE TABLE employees (
  emp_id INT IDENTITY(1,1) PRIMARY KEY,
  name   VARCHAR(100)
);
```

### ALIAS

```sql
-- Column alias
SELECT first_name AS "First Name", salary * 12 AS "Annual Salary"
FROM employees;

-- Table alias (especially useful in JOINs)
SELECT e.name, d.dept_name
FROM employees AS e
JOIN departments AS d ON e.dept_id = d.dept_id;
```

### Collation

**Collation** defines how string data is **sorted and compared** — case sensitivity, accent sensitivity, etc.

```sql
-- Case-insensitive (default in MySQL): 'Alice' = 'alice' = 'ALICE'
SELECT * FROM employees WHERE name = 'alice';  -- finds Alice, ALICE, alice

-- Force case-sensitive search
SELECT * FROM employees WHERE BINARY name = 'Alice';  -- only finds 'Alice'
```

### How to Get Count of Records

```sql
SELECT COUNT(*) FROM employees;                    -- count all rows
SELECT COUNT(DISTINCT department) FROM employees;  -- count unique departments
SELECT COUNT(*) FROM employees WHERE salary > 50000; -- count with condition
```

---

## 17. Security — SQL Injection

### What is SQL Injection?

**SQL injection** is a security attack where an attacker inserts **malicious SQL code** into input fields, potentially accessing, modifying, or deleting database data.

```
User login form:
Username: alice' OR '1'='1
Password: anything

Constructed query:
SELECT * FROM users WHERE username = 'alice' OR '1'='1' AND password = '...'
                                               ^^^^^^^^
                                 This is ALWAYS TRUE -> bypasses login!
```

### How to Prevent SQL Injection

```sql
-- BAD: string concatenation (vulnerable!)
query = "SELECT * FROM users WHERE name = '" + userInput + "'";

-- GOOD: use parameterized queries / prepared statements
-- PHP example:
$stmt = $pdo->prepare("SELECT * FROM users WHERE name = ?");
$stmt->execute([$userInput]);

-- GOOD: use stored procedures
CALL GetUserByName(@username);  -- parameter is treated as data, not code

-- Other prevention methods:
-- 1. Input validation (only allow expected formats)
-- 2. Limit database permissions (principle of least privilege)
-- 3. Escape special characters
-- 4. Use ORM (Object-Relational Mapper)
-- 5. Enable Web Application Firewall (WAF)
```

---

## 18. Top Interview Q&A

### Q1. How do you find duplicate records in a table?

```sql
-- Method 1: GROUP BY + HAVING
SELECT name, email, COUNT(*) AS count
FROM employees
GROUP BY name, email
HAVING COUNT(*) > 1;

-- Method 2: COUNT vs COUNT DISTINCT
SELECT COUNT(*) AS total, COUNT(DISTINCT email) AS unique_emails
FROM employees;
-- If total != unique_emails, duplicates exist
```

---

### Q2. How do you find the Nth highest salary?

```sql
-- Method 1: DENSE_RANK() (best approach)
SELECT name, salary
FROM (
  SELECT name, salary,
         DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
  FROM employees
) ranked
WHERE rnk = 2;  -- change 2 for Nth highest

-- Method 2: Subquery
SELECT MAX(salary) FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);  -- second highest

-- Method 3: LIMIT + OFFSET
SELECT DISTINCT salary FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;  -- skip 1 (highest), take 1 (second highest)
```

---

### Q3. How do you find employees whose names start with 'A'?

```sql
SELECT * FROM employees WHERE name LIKE 'A%';
```

---

### Q4. How do you compare two tables and find extra/missing rows?

```sql
-- Method 1: FULL OUTER JOIN
SELECT
  CASE WHEN a.emp_id IS NULL THEN 'Only in B'
       WHEN b.emp_id IS NULL THEN 'Only in A'
       ELSE 'In both'
  END AS status,
  COALESCE(a.emp_id, b.emp_id) AS emp_id
FROM table_a a
FULL OUTER JOIN table_b b ON a.emp_id = b.emp_id
WHERE a.emp_id IS NULL OR b.emp_id IS NULL;

-- Method 2: EXCEPT/MINUS
SELECT emp_id FROM table_a
EXCEPT
SELECT emp_id FROM table_b;
```

---

### Q5. How do you get alternate (odd/even) rows?

```sql
-- Odd rows (1, 3, 5...)
SELECT * FROM (
  SELECT *, ROW_NUMBER() OVER (ORDER BY emp_id) AS rn FROM employees
) t WHERE rn % 2 = 1;

-- Even rows (2, 4, 6...)
SELECT * FROM (
  SELECT *, ROW_NUMBER() OVER (ORDER BY emp_id) AS rn FROM employees
) t WHERE rn % 2 = 0;
```

---

### Q6. How do you fetch common records from two tables?

```sql
-- Method 1: INTERSECT
SELECT emp_id FROM table_a
INTERSECT
SELECT emp_id FROM table_b;

-- Method 2: INNER JOIN
SELECT a.* FROM table_a a
INNER JOIN table_b b ON a.emp_id = b.emp_id;
```

---

### Q7. How do you convert text to date format?

```sql
-- MySQL
SELECT STR_TO_DATE('25-12-2024', '%d-%m-%Y');  -- returns 2024-12-25

-- SQL Server
SELECT CONVERT(DATE, '25-12-2024', 105);

-- Standard SQL
SELECT CAST('2024-12-25' AS DATE);
```

---

### Q8. Write a query using WHERE and HAVING together

```sql
SELECT department, AVG(salary) AS avg_salary, COUNT(*) AS emp_count
FROM employees
WHERE hire_date > '2020-01-01'         -- filter rows first
GROUP BY department
HAVING AVG(salary) > 60000             -- then filter groups
ORDER BY avg_salary DESC;
```

---

### Q9. What is a self-join? Give an example.

```sql
-- Find each employee and their manager's name
SELECT
  e.name         AS employee_name,
  m.name         AS manager_name,
  e.salary       AS employee_salary
FROM employees e
JOIN employees m ON e.manager_id = m.emp_id;
-- Same table joined to itself using different aliases
```

---

### Q10. Explain COALESCE with a real example.

```sql
-- Return the first non-NULL contact method
SELECT
  name,
  COALESCE(mobile_phone, home_phone, work_phone, 'No contact available') AS contact
FROM employees;
-- If mobile_phone is NULL, tries home_phone. If also NULL, tries work_phone, etc.
```

---

### Q11. How to handle NULL values in SQL?

```sql
-- IS NULL / IS NOT NULL
SELECT * FROM employees WHERE email IS NULL;

-- COALESCE — replace NULL with a default
SELECT COALESCE(email, 'no-email@company.com') AS email FROM employees;

-- ISNULL (SQL Server) / IFNULL (MySQL)
SELECT IFNULL(email, 'N/A') FROM employees;

-- NULL in arithmetic — any operation with NULL returns NULL
SELECT salary + NULL;  -- result: NULL (not salary!)
SELECT 5 + NULL;       -- result: NULL
```

---

### Q12. How do you write a CASE WHEN query?

```sql
-- Categorize employees by tenure
SELECT name,
  hire_date,
  DATEDIFF(NOW(), hire_date) / 365 AS years,
  CASE
    WHEN DATEDIFF(NOW(), hire_date) / 365 < 1  THEN 'New Joiner'
    WHEN DATEDIFF(NOW(), hire_date) / 365 < 2  THEN '1-2 Years'
    WHEN DATEDIFF(NOW(), hire_date) / 365 < 5  THEN '2-5 Years'
    ELSE 'Senior (5+ years)'
  END AS tenure_category
FROM employees;
```

---

### Q13. Why is SELECT * bad in production?

```sql
-- BAD: SELECT *
SELECT * FROM employees JOIN departments ON employees.dept_id = departments.dept_id;
-- Problems:
-- 1. Fetches ALL columns (including ones you don't need) -> slow
-- 2. If table schema changes (new column added), query result changes
-- 3. Ambiguous column names in JOINs (if both tables have 'name' column)
-- 4. More network bandwidth used

-- GOOD: specify columns
SELECT e.emp_id, e.name, e.salary, d.dept_name
FROM employees e JOIN departments d ON e.dept_id = d.dept_id;
```

---

### Q14. How do you write a query that uses indexes efficiently?

```sql
-- BAD: function on indexed column (index NOT used!)
WHERE YEAR(hire_date) = 2023

-- GOOD: range query (index IS used)
WHERE hire_date BETWEEN '2023-01-01' AND '2023-12-31'

-- BAD: leading wildcard (index NOT used)
WHERE name LIKE '%Alice%'

-- GOOD: prefix search (index IS used)
WHERE name LIKE 'Alice%'

-- BAD: OR with non-indexed column (full scan)
WHERE indexed_col = 1 OR non_indexed_col = 2

-- GOOD: both columns indexed or use UNION
WHERE indexed_col = 1
UNION
WHERE other_indexed_col = 2
```

---

### Q15. What is a MERGE statement?

The **MERGE** statement performs INSERT, UPDATE, or DELETE operations in a **single statement** based on whether a matching record exists.

```sql
MERGE INTO employees AS target
USING new_employees AS source
ON target.emp_id = source.emp_id
WHEN MATCHED THEN
  UPDATE SET target.salary = source.salary
WHEN NOT MATCHED BY TARGET THEN
  INSERT (emp_id, name, salary) VALUES (source.emp_id, source.name, source.salary)
WHEN NOT MATCHED BY SOURCE THEN
  DELETE;
-- Updates existing, inserts new, deletes removed employees in one statement
```

---

## 19. Quick Cheatsheet & Memory Tips

### SQL Execution Order

```
1. FROM           (which table?)
2. JOIN           (combine tables)
3. WHERE          (filter rows)
4. GROUP BY       (group rows)
5. HAVING         (filter groups)
6. SELECT         (choose columns)
7. DISTINCT       (remove duplicates)
8. ORDER BY       (sort)
9. LIMIT/OFFSET   (paginate)

Memory: "From Where Groups Have Selected Distinct Order Limit"
        FR-WH-GR-HA-SE-DI-OR-LI
```

### One-Line Definitions

| Term | One-Line Definition |
|---|---|
| **SQL** | Language to communicate with relational databases. |
| **RDBMS** | Database system that stores data in related tables. |
| **Table** | Data organized in rows and columns. |
| **Primary Key** | Unique, non-null identifier for each row. |
| **Foreign Key** | Column that references a primary key in another table. |
| **Unique Key** | Ensures no duplicate values; allows one NULL. |
| **NOT NULL** | Column must always have a value. |
| **DEFAULT** | Provides a fallback value if none is given. |
| **CHECK** | Validates that a value meets a condition. |
| **DDL** | Commands that define database structure (CREATE, ALTER, DROP). |
| **DML** | Commands that manipulate data (SELECT, INSERT, UPDATE, DELETE). |
| **DCL** | Commands that control access (GRANT, REVOKE). |
| **TCL** | Commands that manage transactions (COMMIT, ROLLBACK, SAVEPOINT). |
| **JOIN** | Combines rows from two tables based on a related column. |
| **INNER JOIN** | Returns only matching rows from both tables. |
| **LEFT JOIN** | Returns all rows from left table + matching rows from right. |
| **FULL OUTER JOIN** | Returns all rows from both tables. |
| **WHERE** | Filters rows before grouping. |
| **HAVING** | Filters groups after GROUP BY. |
| **GROUP BY** | Groups rows with same values for aggregation. |
| **ORDER BY** | Sorts results. |
| **Aggregate Function** | Works on groups of rows (COUNT, SUM, AVG, MIN, MAX). |
| **Scalar Function** | Works on individual values (UPPER, LENGTH, ROUND). |
| **Window Function** | Calculates across related rows without collapsing (RANK, ROW_NUMBER). |
| **Subquery** | A query nested inside another query. |
| **CTE** | Named temporary result set using WITH clause. |
| **Index** | Data structure for fast data retrieval. |
| **Clustered Index** | Data stored physically sorted by index (one per table). |
| **Non-Clustered Index** | Separate structure pointing to data (multiple allowed). |
| **Normalization** | Reducing redundancy by splitting tables. |
| **Denormalization** | Adding redundancy for read performance. |
| **View** | Virtual table based on a saved SELECT query. |
| **Stored Procedure** | Saved, reusable SQL code block with optional parameters. |
| **Function** | Returns a single value; used inline in queries. |
| **Trigger** | Auto-executes SQL on INSERT/UPDATE/DELETE events. |
| **Transaction** | Group of operations that succeed or fail together. |
| **ACID** | Atomicity, Consistency, Isolation, Durability. |
| **Deadlock** | Two transactions waiting on each other's locks indefinitely. |
| **SQL Injection** | Security attack inserting malicious SQL through input fields. |
| **COALESCE** | Returns first non-NULL value from a list. |
| **UNION** | Combines query results, removing duplicates. |
| **UNION ALL** | Combines query results, keeping duplicates. |
| **INTERSECT** | Returns rows common to both queries. |
| **EXCEPT/MINUS** | Returns rows in first query not in second. |
| **LIKE** | Pattern matching (% = any chars, _ = one char). |
| **IN** | Matches any value in a list. |
| **EXISTS** | Returns true if subquery returns any rows. |
| **AUTO_INCREMENT** | Automatically assigns incrementing numbers to a column. |
| **ALIAS** | Temporary name for a column or table. |
| **DISTINCT** | Returns only unique values. |

---

### Key Commands Quick Reference

```sql
-- DATABASE
CREATE DATABASE mydb;
USE mydb;
DROP DATABASE mydb;

-- TABLE
CREATE TABLE t (id INT PRIMARY KEY, name VARCHAR(100));
ALTER TABLE t ADD COLUMN email VARCHAR(200);
DROP TABLE t;
TRUNCATE TABLE t;

-- CRUD
SELECT * FROM t WHERE id = 1;
INSERT INTO t VALUES (1, 'Alice');
UPDATE t SET name = 'Bob' WHERE id = 1;
DELETE FROM t WHERE id = 1;

-- JOIN
SELECT * FROM a INNER JOIN b ON a.id = b.id;
SELECT * FROM a LEFT  JOIN b ON a.id = b.id;
SELECT * FROM a RIGHT JOIN b ON a.id = b.id;
SELECT * FROM a FULL OUTER JOIN b ON a.id = b.id;

-- AGGREGATE
SELECT dept, COUNT(*), AVG(salary), MAX(salary) FROM employees GROUP BY dept;

-- WINDOW FUNCTIONS
SELECT name, RANK() OVER (ORDER BY salary DESC) FROM employees;

-- INDEX
CREATE INDEX idx ON employees(name);
DROP INDEX idx;

-- VIEW
CREATE VIEW v AS SELECT * FROM employees WHERE dept = 'IT';

-- TRANSACTION
START TRANSACTION; UPDATE ...; COMMIT;
```

---

### Memory Tips & Tricks

**1. Remember SQL Clause Order:**
```
"Friendly Whales Go Have Some Drinks On Lazy Lakes"
 FROM  WHERE  GROUP  HAVE  SELECT  DISTINCT  ORDER  LIMIT
```

**2. Remember JOINs:**
```
INNER = Intersection (only matching)
LEFT  = All Left + matching Right
RIGHT = All Right + matching Left
FULL  = All from Both
CROSS = Everything × Everything
```

**3. Remember ACID:**
```
All Committed In Disk
Atomicity - Consistency - Isolation - Durability
```

**4. DELETE vs TRUNCATE vs DROP:**
```
DELETE = remove SELECTED rows (can undo)
TRUNCATE = erase ALL rows (can't undo, table stays)
DROP = destroy ENTIRE table (can't undo)
```

**5. WHERE vs HAVING:**
```
WHERE  = filters BEFORE cooking (raw ingredients)
HAVING = filters AFTER cooking (finished dish)
WHERE can't taste the dish (no aggregates)
HAVING can taste the dish (can use aggregates)
```

**6. Normalization forms:**
```
1NF = One value per cell (no lists, no arrays)
2NF = No partial dependency (whole key matters)
3NF = No transitive dependency (non-key -> non-key bad)
```

**7. NULL rules:**
```
NULL is NOT 0, NOT '', NOT false
NULL = "unknown/missing"
Use IS NULL, not = NULL
Any math with NULL = NULL
```

---

### Study Priority Guide

| Level | Must-Know Topics |
|---|---|
| **Junior/Fresher** | SELECT, INSERT, UPDATE, DELETE, WHERE, JOINs (INNER, LEFT), GROUP BY, HAVING, Aggregate functions, Primary/Foreign Key, Constraints, Normalization basics |
| **Mid-level** | All JOIN types, Subqueries, CTEs, Window functions, Indexes (clustered/non-clustered), Views, Stored procedures, Transactions & ACID, UNION/INTERSECT |
| **Senior** | Query optimization, Index strategy, Deadlocks, Triggers, SQL injection prevention, Partitioning, Database design, Query execution plans |

---

> **Final Interview Tip:** SQL interviewers love to ask:
> - "Write a query to find the Nth highest salary" → Use DENSE_RANK()
> - "Difference between DELETE, TRUNCATE, DROP" → Know all three cold
> - "WHERE vs HAVING" → Before vs after grouping
> - "What is a clustered index?" → One per table, physically sorted
> - "What is SQL injection and how to prevent it?" → Parameterized queries
>
> If you can answer all 20 Q&As and explain each concept with an example, you're ready for any SQL interview!

---