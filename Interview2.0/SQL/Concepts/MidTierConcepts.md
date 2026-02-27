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
| 19 | [Quick Cheatsheet & Memory Tips](#19-quick-cheatsheet--memory-tips) |
| 20 | [Real-World SQL Practice Problems](#20-real-world-sql-practice-problems) |

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

## 20. Real-World SQL Practice Problems

> These questions are asked in **live coding rounds** and **take-home SQL tests**.
> They test whether you can write actual queries on a real schema — not just recite theory.
> Study the schema first, then try each query yourself before reading the answer.

---

### Database Schema — E-Commerce Dataset

This is the schema used for all 20 problems below. Understand the relationships before writing any query.

```
+------------------+          +-------------------+          +------------------+
|    customers     |          |      orders        |          |    products       |
+------------------+          +-------------------+          +------------------+
| customer_id (PK) |----+     | order_id (PK)     |     +----| product_id (PK)  |
| name             |    +---->| customer_id (FK)  |     |    | product_name     |
| city             |          | order_date        |     |    | category         |
| signup_date      |          | total_amount      |     |    | price            |
+------------------+          +-------------------+     |    +------------------+
                                       |                |
                              +--------+--------+       |
                              | order_items      |      |
                              +-----------------+       |
                              | item_id (PK)    |       |
                              | order_id (FK)   |       |
                              | product_id (FK) |-------+
                              | quantity        |
                              | unit_price      |
                              +-----------------+
```

### Setup — Create Tables and Insert Sample Data

```sql
-- Create customers table
CREATE TABLE customers (
  customer_id  INT          PRIMARY KEY AUTO_INCREMENT,
  name         VARCHAR(100) NOT NULL,
  city         VARCHAR(100),
  signup_date  DATE
);

-- Create products table
CREATE TABLE products (
  product_id   INT          PRIMARY KEY AUTO_INCREMENT,
  product_name VARCHAR(100) NOT NULL,
  category     VARCHAR(50),
  price        DECIMAL(10,2)
);

-- Create orders table
CREATE TABLE orders (
  order_id     INT          PRIMARY KEY AUTO_INCREMENT,
  customer_id  INT,
  order_date   DATE,
  total_amount DECIMAL(10,2),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create order_items table
CREATE TABLE order_items (
  item_id     INT  PRIMARY KEY AUTO_INCREMENT,
  order_id    INT,
  product_id  INT,
  quantity    INT,
  unit_price  DECIMAL(10,2),
  FOREIGN KEY (order_id)   REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample customers
INSERT INTO customers (name, city, signup_date) VALUES
  ('Alice Johnson', 'New York',    '2022-03-15'),
  ('Bob Smith',     'Los Angeles', '2021-07-22'),
  ('Carol White',   'New York',    '2022-09-10'),
  ('Dave Brown',    'Chicago',     '2020-11-05'),
  ('Eva Green',     'New York',    '2023-01-18'),
  ('Frank Miller',  'Boston',      '2022-04-30'),
  ('Grace Lee',     'Chicago',     '2021-12-01'),
  ('Henry Davis',   'New York',    '2022-07-14');

-- Insert sample products
INSERT INTO products (product_name, category, price) VALUES
  ('Laptop',        'Electronics', 999.99),
  ('Phone',         'Electronics', 699.99),
  ('Headphones',    'Electronics', 149.99),
  ('Desk Chair',    'Furniture',   299.99),
  ('Coffee Table',  'Furniture',   199.99),
  ('T-Shirt',       'Clothing',     29.99),
  ('Jeans',         'Clothing',     59.99),
  ('Python Book',   'Books',        39.99),
  ('SQL Guide',     'Books',        34.99),
  ('Blender',       'Appliances',   89.99);

-- Insert sample orders
INSERT INTO orders (customer_id, order_date, total_amount) VALUES
  (1, '2022-03-20', 1199.98),
  (1, '2022-08-15',  299.99),
  (2, '2022-01-10',  699.99),
  (3, '2022-03-05',  149.99),
  (3, '2022-11-20',  329.98),
  (4, '2022-03-18', 1099.98),
  (5, '2023-02-14',  699.99),
  (6, '2022-03-25',   89.99),
  (7, '2021-12-20',  259.98),
  (8, '2022-05-11',  999.99);
-- Note: customer_id 7 (Grace) is in orders but has no order in 2022 range used later
-- Note: No orders for customer Eva (5) in 2022 — signed up 2023

-- Insert sample order_items
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
  (1, 1, 1, 999.99),   -- Alice: Laptop
  (1, 6, 5,  29.99),   -- Alice: 5 T-Shirts (5x29.99 = 149.95 -> approx)
  (2, 4, 1, 299.99),   -- Alice: Desk Chair
  (3, 2, 1, 699.99),   -- Bob: Phone
  (4, 3, 1, 149.99),   -- Carol: Headphones
  (5, 5, 1, 199.99),   -- Carol: Coffee Table
  (5, 6, 5,  29.99),   -- Carol: T-Shirts
  (6, 1, 1, 999.99),   -- Dave: Laptop
  (6, 7, 1,  59.99),   -- Dave: Jeans
  (7, 2, 1, 699.99),   -- Eva: Phone
  (8, 10,1,  89.99),   -- Frank: Blender
  (9, 8, 2,  39.99),   -- Grace: 2x Python Book
  (9, 7, 3,  59.99),   -- Grace: 3x Jeans
  (10,1, 1, 999.99);   -- Henry: Laptop
```

---

### Beginner SQL Practice Questions

---

#### Q1. Count Total Customers

**Question:** How many customers are registered in the database?

**Concept tested:** `COUNT(*)` basic aggregate

```sql
SELECT COUNT(*) AS total_customers
FROM customers;

-- Result: 8
```

> **What interviewer looks for:** Do you use `COUNT(*)` vs `COUNT(customer_id)`? Both work here since PK is never NULL. `COUNT(*)` is most common.

---

#### Q2. Find Customers from New York

**Question:** List all customers who are from New York.

**Concept tested:** `WHERE` clause with string filter

```sql
SELECT customer_id, name, city, signup_date
FROM customers
WHERE city = 'New York';

-- Result: Alice Johnson, Carol White, Eva Green, Henry Davis
```

> **Variation asked in interviews:** "Find customers NOT from New York" → use `WHERE city != 'New York'` or `WHERE city <> 'New York'`

---

#### Q3. Total Orders per Customer

**Question:** Show how many orders each customer has placed.

**Concept tested:** `GROUP BY`, `COUNT`, `JOIN`

```sql
-- Method 1: JOIN + GROUP BY
SELECT
  c.customer_id,
  c.name,
  COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_orders DESC;

-- Why LEFT JOIN? To include customers with 0 orders too.
-- INNER JOIN would exclude customers who never ordered.
```

```
Result:
+-----------+---------------+--------------+
|customer_id| name          | total_orders |
+-----------+---------------+--------------+
| 1         | Alice Johnson | 2            |
| 3         | Carol White   | 2            |
| 2         | Bob Smith     | 1            |
| 4         | Dave Brown    | 1            |
| 5         | Eva Green     | 1            |
| 6         | Frank Miller  | 1            |
| 7         | Grace Lee     | 1            |
| 8         | Henry Davis   | 1            |
+-----------+---------------+--------------+
```

> **Key interview insight:** Always use `LEFT JOIN` when you want customers with zero orders to appear.

---

#### Q4. Total Revenue

**Question:** What is the total revenue from all orders?

**Concept tested:** `SUM()` aggregate

```sql
-- Method 1: Sum from orders table
SELECT SUM(total_amount) AS total_revenue
FROM orders;

-- Method 2: Calculate from order_items (more granular)
SELECT SUM(quantity * unit_price) AS total_revenue
FROM order_items;
```

> **Interview variation:** "Revenue for a specific date range" → add `WHERE order_date BETWEEN '2022-01-01' AND '2022-12-31'`

---

#### Q5. Average Order Value

**Question:** What is the average value of all orders?

**Concept tested:** `AVG()` aggregate

```sql
SELECT
  ROUND(AVG(total_amount), 2) AS avg_order_value
FROM orders;

-- Always use ROUND() for monetary values to avoid long decimals
```

> **Follow-up question:** "Average order value per customer?" → add `GROUP BY customer_id`

```sql
SELECT
  c.name,
  ROUND(AVG(o.total_amount), 2) AS avg_order_value
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY avg_order_value DESC;
```

---

#### Q6. Customers Who Signed Up in 2022

**Question:** List all customers who registered during the year 2022.

**Concept tested:** Date filtering with `YEAR()` or `BETWEEN`

```sql
-- Method 1: YEAR() function
SELECT name, signup_date
FROM customers
WHERE YEAR(signup_date) = 2022;

-- Method 2: BETWEEN (preferred — uses indexes)
SELECT name, signup_date
FROM customers
WHERE signup_date BETWEEN '2022-01-01' AND '2022-12-31';

-- Result: Alice, Carol, Frank, Henry (all signed up in 2022)
```

> **Remember:** `BETWEEN` is **index-friendly**. `YEAR(signup_date) = 2022` prevents index usage on signup_date.

---

#### Q7. Customers with More Than One Order

**Question:** Find customers who have placed more than one order.

**Concept tested:** `GROUP BY` + `HAVING` + `COUNT`

```sql
SELECT
  c.customer_id,
  c.name,
  COUNT(o.order_id) AS order_count
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) > 1
ORDER BY order_count DESC;

-- Result: Alice Johnson (2), Carol White (2)
```

> **Classic WHERE vs HAVING:** You CANNOT write `WHERE COUNT(*) > 1` — that's a HAVING job.
> Rule: filters on aggregates go in HAVING, not WHERE.

---

#### Q8. Customer Name with Total Spending

**Question:** Show each customer's name and their total spending across all orders.

**Concept tested:** `JOIN` + `GROUP BY` + `SUM`

```sql
SELECT
  c.name,
  SUM(o.total_amount)        AS total_spending,
  COUNT(o.order_id)          AS total_orders,
  ROUND(AVG(o.total_amount), 2) AS avg_order_value
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spending DESC;
```

```
Result:
+---------------+----------------+--------------+-----------------+
| name          | total_spending | total_orders | avg_order_value |
+---------------+----------------+--------------+-----------------+
| Alice Johnson | 1499.97        | 2            | 749.99          |
| Dave Brown    | 1099.98        | 1            | 1099.98         |
| Henry Davis   | 999.99         | 1            | 999.99          |
+---------------+----------------+--------------+-----------------+
```

---

#### Q9. Customers with No Orders

**Question:** Find customers who have never placed an order.

**Concept tested:** `LEFT JOIN` + `WHERE IS NULL` (classic anti-join pattern)

```sql
-- Method 1: LEFT JOIN + IS NULL (most common)
SELECT
  c.customer_id,
  c.name,
  c.signup_date
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- Method 2: NOT EXISTS (often faster on large datasets)
SELECT customer_id, name
FROM customers c
WHERE NOT EXISTS (
  SELECT 1 FROM orders o
  WHERE o.customer_id = c.customer_id
);

-- Method 3: NOT IN (careful with NULLs!)
SELECT customer_id, name
FROM customers
WHERE customer_id NOT IN (SELECT DISTINCT customer_id FROM orders);
```

> **Critical Interview Point:**
> - `LEFT JOIN + IS NULL` — most readable, universally supported
> - `NOT EXISTS` — fastest for large tables
> - `NOT IN` — **dangerous if subquery can return NULL values** — avoid or add `WHERE customer_id IS NOT NULL` in subquery

---

#### Q10. Orders Placed in March 2022

**Question:** List all orders placed in March 2022.

**Concept tested:** Date filtering with `YEAR()` + `MONTH()` or `BETWEEN`

```sql
-- Method 1: YEAR + MONTH functions
SELECT
  o.order_id,
  c.name        AS customer_name,
  o.order_date,
  o.total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE YEAR(o.order_date) = 2022
  AND MONTH(o.order_date) = 3
ORDER BY o.order_date;

-- Method 2: BETWEEN (index-friendly)
WHERE o.order_date BETWEEN '2022-03-01' AND '2022-03-31'
```

```
Result: Alice (2022-03-20), Carol (2022-03-05), Dave (2022-03-18), Frank (2022-03-25)
```

---

### Intermediate SQL Practice Questions

---

#### Q11. Highest Order Amount

**Question:** Find the order with the highest total amount, including the customer's name.

**Concept tested:** `MAX()` with subquery or `ORDER BY + LIMIT`

```sql
-- Method 1: Subquery
SELECT
  o.order_id,
  c.name       AS customer_name,
  o.order_date,
  o.total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.total_amount = (SELECT MAX(total_amount) FROM orders);

-- Method 2: ORDER BY + LIMIT (simpler, but returns only 1 row even for ties)
SELECT
  o.order_id,
  c.name,
  o.total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
ORDER BY o.total_amount DESC
LIMIT 1;
```

> **Prefer Method 1 (subquery) in interviews** — it correctly handles ties (multiple orders with same highest amount). Method 2 would miss the duplicate.

---

#### Q12. Total Quantity Sold per Product

**Question:** Show how many units of each product have been sold across all orders.

**Concept tested:** `JOIN` across 3 tables + `GROUP BY` + `SUM`

```sql
SELECT
  p.product_id,
  p.product_name,
  p.category,
  SUM(oi.quantity)               AS total_qty_sold,
  ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY total_qty_sold DESC;
```

```
Result:
+-------------+----------+---------+----------------+
| product_name| category | qty_sold| total_revenue  |
+-------------+----------+---------+----------------+
| T-Shirt     | Clothing | 10      | 299.90         |
| Laptop      | Electronics| 3     | 2999.97        |
| Jeans       | Clothing | 4       | 239.96         |
+-------------+----------+---------+----------------+
```

---

#### Q13. Rank Customers by Total Spending

**Question:** Rank all customers from highest to lowest total spending using window functions.

**Concept tested:** Window functions — `RANK()`, `DENSE_RANK()`, `ROW_NUMBER()`

```sql
SELECT
  c.name,
  SUM(o.total_amount)                                        AS total_spending,
  RANK()       OVER (ORDER BY SUM(o.total_amount) DESC)     AS rank,
  DENSE_RANK() OVER (ORDER BY SUM(o.total_amount) DESC)     AS dense_rank,
  ROW_NUMBER() OVER (ORDER BY SUM(o.total_amount) DESC)     AS row_num
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spending DESC;
```

### RANK vs DENSE_RANK vs ROW_NUMBER Explained

```
Spending:  1500, 1100, 1100, 1000

RANK:        1,    2,    2,    4   <- gap after tie (skips 3)
DENSE_RANK:  1,    2,    2,    3   <- no gap after tie
ROW_NUMBER:  1,    2,    3,    4   <- always unique, no ties
```

> **Interview Tip:** Use `DENSE_RANK()` for "find Nth highest" problems — it handles ties without gaps.

---

#### Q14. Top 2 Highest-Spending Customers

**Question:** Find the top 2 customers by total spending. Handle ties correctly.

**Concept tested:** CTE + Window function + filtering ranked results

```sql
-- Using CTE + DENSE_RANK (handles ties correctly)
WITH customer_spending AS (
  SELECT
    c.customer_id,
    c.name,
    SUM(o.total_amount)                                    AS total_spending,
    DENSE_RANK() OVER (ORDER BY SUM(o.total_amount) DESC)  AS spending_rank
  FROM customers c
  JOIN orders o ON c.customer_id = o.customer_id
  GROUP BY c.customer_id, c.name
)
SELECT name, total_spending, spending_rank
FROM customer_spending
WHERE spending_rank <= 2;

-- Why NOT just ORDER BY + LIMIT 2?
-- If two customers tie for 2nd, LIMIT 2 returns only one of them.
-- DENSE_RANK correctly includes both tied customers.
```

---

#### Q15. Running Total of Revenue by Date

**Question:** Show the cumulative (running) total of revenue ordered by date.

**Concept tested:** Window function — `SUM() OVER` with `ORDER BY` (running total)

```sql
SELECT
  order_date,
  total_amount                                                   AS daily_revenue,
  SUM(total_amount) OVER (ORDER BY order_date)                   AS running_total,
  SUM(total_amount) OVER (
    ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  )                                                              AS running_total_explicit
FROM orders
ORDER BY order_date;
```

```
Date           | Amount  | Running Total
2022-01-10     | 699.99  | 699.99
2022-03-05     | 149.99  | 849.98
2022-03-18     | 1099.98 | 1949.96
2022-03-20     | 1199.98 | 3149.94
...
```

> **Key concept:** `SUM(...) OVER (ORDER BY date)` = running total. Without `ORDER BY` inside OVER, it gives a grand total for all rows.

---

### Advanced SQL Practice Questions

---

#### Q16. Category-wise Revenue

**Question:** Show total revenue grouped by product category, sorted from highest to lowest.

**Concept tested:** Multi-table JOIN + GROUP BY + SUM

```sql
SELECT
  p.category,
  COUNT(DISTINCT oi.order_id)                       AS total_orders,
  SUM(oi.quantity)                                  AS total_qty_sold,
  ROUND(SUM(oi.quantity * oi.unit_price), 2)        AS total_revenue,
  ROUND(AVG(oi.unit_price), 2)                      AS avg_unit_price
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;
```

```
Category     | Orders | Qty Sold | Revenue  | Avg Price
Electronics  |   6    |    6     | 3549.93  | 616.66
Clothing     |   4    |   14     |  539.86  |  44.99
Furniture    |   3    |    3     |  759.97  | 253.33
```

---

#### Q17. Most Sold Product (by Quantity)

**Question:** Find the single product that has been sold in the highest quantity overall.

**Concept tested:** Subquery + MAX or LIMIT, GROUP BY

```sql
-- Method 1: CTE + RANK (handles ties)
WITH product_sales AS (
  SELECT
    p.product_name,
    p.category,
    SUM(oi.quantity)                                     AS total_qty,
    RANK() OVER (ORDER BY SUM(oi.quantity) DESC)         AS qty_rank
  FROM products p
  JOIN order_items oi ON p.product_id = oi.product_id
  GROUP BY p.product_id, p.product_name, p.category
)
SELECT product_name, category, total_qty
FROM product_sales
WHERE qty_rank = 1;

-- Method 2: Simple ORDER BY + LIMIT (if ties don't matter)
SELECT
  p.product_name,
  SUM(oi.quantity) AS total_qty
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_qty DESC
LIMIT 1;
```

---

#### Q18. Customers Spending Above Average

**Question:** Find all customers whose total spending is above the average customer spending.

**Concept tested:** Subquery returning a scalar value as a filter

```sql
-- Step 1: Calculate average customer spending
-- Step 2: Find customers above that average

SELECT
  c.name,
  SUM(o.total_amount) AS total_spending
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING SUM(o.total_amount) > (
  -- Subquery: average total spending per customer
  SELECT AVG(customer_total)
  FROM (
    SELECT SUM(total_amount) AS customer_total
    FROM orders
    GROUP BY customer_id
  ) AS customer_totals
)
ORDER BY total_spending DESC;
```

```sql
-- Cleaner version using CTE:
WITH customer_spending AS (
  SELECT customer_id, SUM(total_amount) AS total_spending
  FROM orders
  GROUP BY customer_id
),
avg_spending AS (
  SELECT AVG(total_spending) AS avg_val FROM customer_spending
)
SELECT c.name, cs.total_spending
FROM customers c
JOIN customer_spending cs ON c.customer_id = cs.customer_id
CROSS JOIN avg_spending av
WHERE cs.total_spending > av.avg_val
ORDER BY cs.total_spending DESC;
```

> **Interview insight:** Show the interviewer you can solve it multiple ways. CTEs show you think about readability; subqueries show you understand nesting.

---

#### Q19. Customer Spending Classification (CASE WHEN)

**Question:** Classify each customer as 'High Spender', 'Medium Spender', or 'Low Spender' based on their total spending.

**Concept tested:** `CASE WHEN` with aggregation and conditional classification

```sql
SELECT
  c.name,
  SUM(o.total_amount)                   AS total_spending,
  CASE
    WHEN SUM(o.total_amount) >= 1000 THEN 'High Spender'
    WHEN SUM(o.total_amount) >= 500  THEN 'Medium Spender'
    ELSE                                  'Low Spender'
  END                                   AS spending_category
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spending DESC NULLS LAST;
```

```
+--------------+----------------+----------------+
| name         | total_spending | category       |
+--------------+----------------+----------------+
| Alice Johnson| 1499.97        | High Spender   |
| Dave Brown   | 1099.98        | High Spender   |
| Henry Davis  | 999.99         | Medium Spender |
| Bob Smith    | 699.99         | Medium Spender |
| Carol White  | 479.97         | Low Spender    |
| Eva Green    | NULL           | Low Spender    |  <- no orders
+--------------+----------------+----------------+
```

> **Why LEFT JOIN here?** To include customers with no orders (spending = NULL → 'Low Spender').
> With INNER JOIN, customers with no orders would be excluded entirely.

---

#### Q20. Customers Who Purchased Electronics

**Question:** Find all customers who have purchased at least one product from the 'Electronics' category.

**Concept tested:** Multi-table JOIN + filtering on joined data + DISTINCT

```sql
-- Method 1: JOIN chain (most readable)
SELECT DISTINCT
  c.customer_id,
  c.name,
  c.city
FROM customers c
JOIN orders     o  ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id   = oi.order_id
JOIN products   p  ON oi.product_id = p.product_id
WHERE p.category = 'Electronics'
ORDER BY c.name;

-- Method 2: EXISTS (efficient — stops as soon as match found)
SELECT customer_id, name
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
  JOIN order_items oi ON o.order_id   = oi.order_id
  JOIN products    p  ON oi.product_id = p.product_id
  WHERE o.customer_id = c.customer_id
    AND p.category    = 'Electronics'
);
```

```
Result: Alice Johnson, Bob Smith, Carol White, Dave Brown, Eva Green, Henry Davis
```

> **Why DISTINCT?** A customer may have ordered multiple Electronics products — without DISTINCT they'd appear multiple times.

---

### Bonus: Combining Multiple Concepts

#### Bonus Q1. Monthly Revenue Report

```sql
-- Revenue, orders, and avg order value per month
SELECT
  YEAR(order_date)              AS year,
  MONTH(order_date)             AS month,
  COUNT(order_id)               AS total_orders,
  SUM(total_amount)             AS monthly_revenue,
  ROUND(AVG(total_amount), 2)   AS avg_order_value,
  SUM(SUM(total_amount)) OVER (
    PARTITION BY YEAR(order_date)
    ORDER BY MONTH(order_date)
  )                             AS ytd_revenue  -- year-to-date running total
FROM orders
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month;
```

#### Bonus Q2. Customer Retention — Repeat vs One-Time Buyers

```sql
SELECT
  CASE
    WHEN order_count = 1 THEN 'One-time buyer'
    WHEN order_count = 2 THEN 'Repeat buyer'
    ELSE 'Loyal customer (3+ orders)'
  END                          AS customer_type,
  COUNT(*)                     AS customer_count,
  ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) AS percentage
FROM (
  SELECT customer_id, COUNT(order_id) AS order_count
  FROM orders
  GROUP BY customer_id
) order_counts
GROUP BY customer_type;
```

#### Bonus Q3. Product Performance Report (Full Analytics)

```sql
WITH product_stats AS (
  SELECT
    p.product_id,
    p.product_name,
    p.category,
    p.price                                             AS list_price,
    SUM(oi.quantity)                                    AS total_qty_sold,
    ROUND(SUM(oi.quantity * oi.unit_price), 2)          AS total_revenue,
    COUNT(DISTINCT oi.order_id)                         AS times_ordered,
    RANK() OVER (ORDER BY SUM(oi.quantity) DESC)        AS qty_rank,
    RANK() OVER (PARTITION BY p.category
                 ORDER BY SUM(oi.quantity * oi.unit_price) DESC) AS category_revenue_rank
  FROM products p
  JOIN order_items oi ON p.product_id = oi.product_id
  GROUP BY p.product_id, p.product_name, p.category, p.price
)
SELECT
  product_name,
  category,
  total_qty_sold,
  total_revenue,
  times_ordered,
  qty_rank          AS overall_qty_rank,
  category_revenue_rank
FROM product_stats
ORDER BY total_revenue DESC;
```

---

### Summary: Concepts Tested by Each Question

| Q# | Question | Concepts Tested |
|---|---|---|
| Q1 | Count customers | `COUNT(*)` |
| Q2 | Customers from NY | `WHERE` string filter |
| Q3 | Orders per customer | `LEFT JOIN`, `GROUP BY`, `COUNT` |
| Q4 | Total revenue | `SUM()` |
| Q5 | Average order value | `AVG()`, `ROUND()` |
| Q6 | Sign-ups in 2022 | `YEAR()`, `BETWEEN`, date filtering |
| Q7 | Customers with 1+ order | `GROUP BY`, `HAVING COUNT > 1` |
| Q8 | Customer total spending | Multi-column `GROUP BY`, `SUM` + `JOIN` |
| Q9 | Customers with no orders | `LEFT JOIN + IS NULL`, `NOT EXISTS`, `NOT IN` |
| Q10 | Orders in March 2022 | `MONTH()`, `YEAR()`, date range |
| Q11 | Highest order amount | `MAX()` with subquery, handles ties |
| Q12 | Qty sold per product | 3-table `JOIN`, `SUM`, `GROUP BY` |
| Q13 | Rank by spending | `RANK()`, `DENSE_RANK()`, `ROW_NUMBER()` |
| Q14 | Top 2 spenders | CTE + `DENSE_RANK()`, handles ties |
| Q15 | Running revenue total | `SUM() OVER (ORDER BY)` window function |
| Q16 | Category-wise revenue | Multi-table `JOIN`, `GROUP BY` category |
| Q17 | Most sold product | CTE + `RANK()` or `ORDER BY + LIMIT` |
| Q18 | Above-average spenders | Nested subquery / CTE + `HAVING` |
| Q19 | Spending classification | `CASE WHEN` + aggregation + `LEFT JOIN` |
| Q20 | Electronics purchasers | 4-table JOIN, `DISTINCT`, `EXISTS` |

---

> **Practice Tip:** Set up this exact schema in MySQL Workbench, DBeaver, or any online SQL editor (sqlfiddle.com, db-fiddle.com, or mode.com). Write each query from scratch before checking the answer above. Solving these 20 problems from memory will prepare you for any real SQL coding round.
