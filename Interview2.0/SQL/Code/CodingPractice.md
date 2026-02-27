# 💻 SQL Coding Practice — Zero to Interview Ready

> **Who is this for?**
> Anyone who knows a little SQL but wants to get truly comfortable writing
> real queries — from simple SELECTs all the way to window functions and
> tricky interview puzzles. Every concept builds on the last one.

> **How to use this file:**
> 1. Read the question
> 2. Try writing the query yourself (even a rough attempt!)
> 3. Check the answer and the explanation
> 4. Run it in your own SQL editor to see the real output
> 5. Try the variations at the end of each question

---

## 📋 Table of Contents

| Level | Section |
|-------|---------|
| 🔧 Setup | [The Schema & Sample Data](#-the-schema--sample-data) |
| ⭐ Level 1 | [Absolute Beginner — SELECT, WHERE, ORDER BY](#-level-1-absolute-beginner) |
| ⭐⭐ Level 2 | [Beginner+ — GROUP BY, HAVING, Aggregates](#-level-2-beginner--group-by-aggregates) |
| ⭐⭐⭐ Level 3 | [Intermediate — All JOINs](#-level-3-intermediate--all-joins) |
| ⭐⭐⭐⭐ Level 4 | [Intermediate+ — Subqueries & CTEs](#-level-4-intermediate--subqueries--ctes) |
| ⭐⭐⭐⭐⭐ Level 5 | [Advanced — Window Functions](#-level-5-advanced--window-functions) |
| 🔥 Level 6 | [Tricky Interview Questions](#-level-6-tricky-interview-questions) |
| 📌 Reference | [Pattern Cheatsheet](#-pattern-cheatsheet) |

---

## 🔧 The Schema & Sample Data

### Why this schema?

It's a **company database** — something every developer will encounter.
It's simple enough to understand in 2 minutes, complex enough to ask 50+ interesting questions.

```
+----------------+       +-------------------+       +------------------+
|   departments  |       |     employees      |       |    salaries      |
+----------------+       +-------------------+       +------------------+
| dept_id   (PK) |<------| dept_id      (FK)  |       | salary_id   (PK) |
| dept_name      |       | emp_id       (PK)  |------>| emp_id      (FK) |
| location       |       | name               |       | amount           |
| budget         |       | job_title          |       | from_date        |
+----------------+       | hire_date          |       | to_date          |
                         | manager_id   (FK)  |--+    +------------------+
                         | is_active          |  |
                         +-------------------+  |    +------------------+
                                                |    |    projects      |
                                                |    +------------------+
                                                |    | proj_id    (PK)  |
                              self-join! -------+    | proj_name        |
                              (manager is also        | dept_id    (FK)  |
                               an employee)           | start_date       |
                                                      | end_date         |
                                                      | budget           |
                                                      +------------------+
```

### Relationships

```
departments → employees   : one department has MANY employees
employees   → employees   : one manager manages MANY employees (self-join)
employees   → salaries    : one employee has MANY salary records (history)
departments → projects    : one department owns MANY projects
```

---

## 🔧 Setup — Run This First

```sql
-- ============================================================
-- CREATE TABLES
-- ============================================================

CREATE TABLE departments (
  dept_id   INT          PRIMARY KEY AUTO_INCREMENT,
  dept_name VARCHAR(50)  NOT NULL,
  location  VARCHAR(50),
  budget    DECIMAL(12,2)
);

CREATE TABLE employees (
  emp_id     INT          PRIMARY KEY AUTO_INCREMENT,
  name       VARCHAR(100) NOT NULL,
  job_title  VARCHAR(100),
  dept_id    INT,
  hire_date  DATE,
  manager_id INT,
  is_active  BOOLEAN      DEFAULT TRUE,
  FOREIGN KEY (dept_id)    REFERENCES departments(dept_id),
  FOREIGN KEY (manager_id) REFERENCES employees(emp_id)
);

CREATE TABLE salaries (
  salary_id INT            PRIMARY KEY AUTO_INCREMENT,
  emp_id    INT            NOT NULL,
  amount    DECIMAL(10,2)  NOT NULL,
  from_date DATE           NOT NULL,
  to_date   DATE,
  FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);

CREATE TABLE projects (
  proj_id    INT          PRIMARY KEY AUTO_INCREMENT,
  proj_name  VARCHAR(100) NOT NULL,
  dept_id    INT,
  start_date DATE,
  end_date   DATE,
  budget     DECIMAL(12,2),
  FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- ============================================================
-- INSERT DEPARTMENTS
-- ============================================================
INSERT INTO departments (dept_name, location, budget) VALUES
  ('Engineering',  'New York',    1500000.00),
  ('Marketing',    'Los Angeles', 800000.00),
  ('HR',           'Chicago',     400000.00),
  ('Finance',      'New York',    600000.00),
  ('Design',       'Remote',      350000.00),
  ('Legal',        'Chicago',     300000.00);

-- ============================================================
-- INSERT EMPLOYEES
-- ============================================================
INSERT INTO employees (name, job_title, dept_id, hire_date, manager_id, is_active) VALUES
  ('Sarah Connor',  'VP of Engineering',  1, '2018-03-01', NULL,  TRUE),   -- emp 1, no manager (top)
  ('John Reese',    'Senior Engineer',    1, '2019-06-15', 1,     TRUE),   -- emp 2
  ('Amy Chen',      'Engineer',           1, '2021-01-10', 2,     TRUE),   -- emp 3
  ('Mike Torres',   'Junior Engineer',    1, '2023-04-22', 2,     TRUE),   -- emp 4
  ('Lisa Park',     'VP of Marketing',    2, '2017-09-05', NULL,  TRUE),   -- emp 5
  ('David Kim',     'Marketing Manager',  2, '2020-02-18', 5,     TRUE),   -- emp 6
  ('Rachel Green',  'Marketing Analyst',  2, '2022-07-01', 6,     TRUE),   -- emp 7
  ('Tom Hardy',     'Marketing Analyst',  2, '2022-08-15', 6,     FALSE),  -- emp 8, inactive
  ('Nina Patel',    'HR Director',        3, '2016-11-20', NULL,  TRUE),   -- emp 9
  ('James Brown',   'HR Specialist',      3, '2020-05-12', 9,     TRUE),   -- emp 10
  ('Emma Wilson',   'CFO',                4, '2015-07-30', NULL,  TRUE),   -- emp 11
  ('Chris Evans',   'Finance Analyst',    4, '2021-03-08', 11,    TRUE),   -- emp 12
  ('Priya Sharma',  'Lead Designer',      5, '2019-10-14', NULL,  TRUE),   -- emp 13
  ('Lucas Martin',  'UI Designer',        5, '2022-01-25', 13,    TRUE),   -- emp 14
  ('Olivia Stone',  'Legal Counsel',      6, '2018-06-01', NULL,  TRUE);   -- emp 15

-- ============================================================
-- INSERT SALARIES (current + some history)
-- ============================================================
INSERT INTO salaries (emp_id, amount, from_date, to_date) VALUES
  (1,  140000, '2018-03-01', '2021-03-01'),
  (1,  160000, '2021-03-01', NULL),         -- current salary (NULL to_date = current)
  (2,   95000, '2019-06-15', '2022-06-15'),
  (2,  110000, '2022-06-15', NULL),         -- current
  (3,   75000, '2021-01-10', NULL),         -- current
  (4,   60000, '2023-04-22', NULL),         -- current
  (5,  130000, '2017-09-05', '2020-09-05'),
  (5,  150000, '2020-09-05', NULL),         -- current
  (6,   85000, '2020-02-18', NULL),         -- current
  (7,   62000, '2022-07-01', NULL),         -- current
  (8,   60000, '2022-08-15', '2023-08-15'), -- inactive employee, last salary
  (9,  115000, '2016-11-20', NULL),         -- current
  (10,  58000, '2020-05-12', NULL),         -- current
  (11, 180000, '2015-07-30', '2020-07-30'),
  (11, 200000, '2020-07-30', NULL),         -- current
  (12,  72000, '2021-03-08', NULL),         -- current
  (13,  90000, '2019-10-14', NULL),         -- current
  (14,  65000, '2022-01-25', NULL),         -- current
  (15, 120000, '2018-06-01', NULL);         -- current

-- ============================================================
-- INSERT PROJECTS
-- ============================================================
INSERT INTO projects (proj_name, dept_id, start_date, end_date, budget) VALUES
  ('Platform Rewrite',    1, '2023-01-01', '2023-12-31', 500000.00),
  ('API Modernisation',   1, '2022-06-01', '2023-06-30', 300000.00),
  ('Brand Refresh',       2, '2023-03-01', '2023-09-30', 150000.00),
  ('Q4 Campaign',         2, '2023-10-01', '2024-01-31', 200000.00),
  ('Talent Pipeline',     3, '2023-01-15', NULL,          80000.00),
  ('Budget Forecasting',  4, '2023-04-01', '2023-11-30', 120000.00),
  ('Design System v2',    5, '2022-09-01', '2023-08-31', 180000.00),
  ('Compliance Audit',    6, '2023-02-01', NULL,          60000.00);

-- ============================================================
-- VERIFY YOUR SETUP
-- ============================================================
SELECT 'departments' AS tbl, COUNT(*) AS rows FROM departments UNION ALL
SELECT 'employees',          COUNT(*)         FROM employees    UNION ALL
SELECT 'salaries',           COUNT(*)         FROM salaries     UNION ALL
SELECT 'projects',           COUNT(*)         FROM projects;
-- Expected: 6, 15, 19, 8
```

---

## ⭐ Level 1: Absolute Beginner

> **Goal:** Get comfortable reading and filtering data.
> **Concepts:** SELECT, WHERE, ORDER BY, LIMIT, DISTINCT, LIKE, BETWEEN, IN, NULL

---

### 💡 Tip Before You Start

```
Think of SELECT like picking what you want to see.
Think of FROM as telling SQL where to look.
Think of WHERE as a filter — only rows that pass the test come through.

SELECT what_you_want
FROM   which_table
WHERE  condition_to_filter;
```

---

### L1-Q1 · Show All Employees

**Question:** See every employee in the database.

```sql
SELECT * FROM employees;
```

> **Why `*` is OK for exploring but bad in production:**
```
In production:
  SELECT * fetches ALL columns — even ones you don't need.
  If a table has 50 columns, you're transferring unnecessary data.
  Always name the columns you actually need.
```

```sql
-- Better version for production:
SELECT emp_id, name, job_title, dept_id, hire_date
FROM employees;
```

---

### L1-Q2 · Show Only Active Employees

**Question:** List all employees who are currently active.

**Think:** You need a filter. Which column tells you if someone is active?

```sql
SELECT emp_id, name, job_title
FROM employees
WHERE is_active = TRUE;

-- Also valid:
WHERE is_active = 1;    -- MySQL stores TRUE as 1
WHERE is_active != FALSE;
```

> **Variation — inactive employees:**
```sql
WHERE is_active = FALSE;
WHERE is_active = 0;
```

---

### L1-Q3 · Employees in the Engineering Department

**Question:** Find all employees whose dept_id is 1 (Engineering).

```sql
SELECT name, job_title, hire_date
FROM employees
WHERE dept_id = 1;
```

> **What if you don't know the dept_id and only know the name?**
That's where JOINs come in (Level 3). For now, dept_id = 1 = Engineering.

---

### L1-Q4 · Sort Employees by Hire Date

**Question:** List all employees sorted from the most recently hired to the oldest.

**Think:** Sorting = ORDER BY. Newest first = DESC.

```sql
SELECT name, job_title, hire_date
FROM employees
ORDER BY hire_date DESC;
```

```sql
-- Oldest to newest (first hired first):
ORDER BY hire_date ASC;   -- ASC is the default, you can omit it

-- Sort by multiple columns:
ORDER BY dept_id ASC, hire_date DESC;  -- by dept, then newest within each dept
```

---

### L1-Q5 · Show Only the Top 5 Highest Salaries

**Question:** See the 5 highest salary records in the salaries table.

```sql
SELECT emp_id, amount
FROM salaries
ORDER BY amount DESC
LIMIT 5;
```

> **Common confusion:** LIMIT comes LAST in the query, but SQL processes ORDER BY first, then applies LIMIT. So this correctly sorts all rows, then takes the top 5.

---

### L1-Q6 · Find Employees Hired After 2021

**Question:** List employees who joined after January 1st, 2021.

```sql
SELECT name, job_title, hire_date
FROM employees
WHERE hire_date > '2021-01-01'
ORDER BY hire_date;
```

```sql
-- Variations to practice:
WHERE hire_date >= '2021-01-01'    -- on or after Jan 1 2021
WHERE hire_date BETWEEN '2021-01-01' AND '2022-12-31'  -- joined in 2021 or 2022
WHERE YEAR(hire_date) = 2022       -- only 2022 (uses function — avoid on large tables)
```

---

### L1-Q7 · Find Employees in Multiple Departments

**Question:** List employees who are in Engineering (1) OR Finance (4).

```sql
-- Method 1: IN (clean, recommended)
SELECT name, job_title, dept_id
FROM employees
WHERE dept_id IN (1, 4);

-- Method 2: OR
SELECT name, job_title, dept_id
FROM employees
WHERE dept_id = 1 OR dept_id = 4;
```

> **Use `IN` when you have 2 or more values to check — it's cleaner than chaining ORs.**

---

### L1-Q8 · Search by Name Pattern

**Question:** Find all employees whose name starts with the letter 'A'.

```sql
SELECT name, job_title
FROM employees
WHERE name LIKE 'A%';
```

### LIKE Patterns Visualised

```
Pattern   Meaning                 Example match
'A%'      Starts with A           Amy, Alice, Andrew
'%son'    Ends with son           Johnson, Robertson
'%ar%'    Contains ar anywhere    Sarah, Charlie, Martin
'_i%'     Second letter is i      Lisa, Mike, Nina
'Jo__'    Jo + exactly 2 letters  John, Joel
```

```sql
-- Case-insensitive search (MySQL is case-insensitive by default):
WHERE name LIKE '%chen%'    -- finds Amy Chen, Chen Wei, etc.

-- Find names with exactly 8 characters:
WHERE name LIKE '________'  -- 8 underscores
```

---

### L1-Q9 · Find Employees with No Manager

**Question:** Which employees have no manager (i.e., they ARE the top-level managers)?

```sql
SELECT emp_id, name, job_title
FROM employees
WHERE manager_id IS NULL;
```

> **Critical rule — NEVER use `= NULL`:**
```sql
WHERE manager_id = NULL    -- WRONG! Always returns 0 rows
WHERE manager_id IS NULL   -- CORRECT!

NULL means "unknown/missing". You can't compare unknown values with =.
You test for NULL with IS NULL or IS NOT NULL.
```

---

### L1-Q10 · Show Distinct Job Titles

**Question:** List all unique job titles in the company (no duplicates).

```sql
SELECT DISTINCT job_title
FROM employees
ORDER BY job_title;
```

> **When to use DISTINCT:**
```
Good: exploring what unique values exist in a column.
Bad: hiding a broken JOIN that accidentally duplicates rows.

If you find yourself adding DISTINCT to fix unexpected duplicates,
check your JOIN conditions first — the problem is usually there.
```

---

## ⭐⭐ Level 2: Beginner+ — GROUP BY & Aggregates

> **Goal:** Summarise and analyse data.
> **Concepts:** COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING, ROUND

---

### 💡 Tip Before You Start

```
Aggregate functions collapse many rows into one summary value.
GROUP BY splits rows into buckets before aggregating.

Think of it like a spreadsheet pivot table:
  GROUP BY dept_name    = rows of the pivot
  SUM(salary)           = values in the pivot cells
  HAVING SUM > 100000   = row filter on the pivot
```

---

### L2-Q1 · Count All Employees

**Question:** How many employees are in the database?

```sql
SELECT COUNT(*) AS total_employees
FROM employees;   -- 15
```

> **COUNT(\*) vs COUNT(column):**
```
COUNT(*)          → counts ALL rows, including NULLs
COUNT(manager_id) → counts only rows where manager_id is NOT NULL
COUNT(DISTINCT dept_id) → counts unique dept_ids

Try this to see the difference:
SELECT COUNT(*), COUNT(manager_id), COUNT(DISTINCT dept_id)
FROM employees;
-- Results: 15, 10 (5 managers have no manager), 5
```

---

### L2-Q2 · Count Employees per Department

**Question:** How many employees does each department have?

```sql
SELECT
  dept_id,
  COUNT(*)  AS employee_count
FROM employees
GROUP BY dept_id
ORDER BY employee_count DESC;
```

> **The GROUP BY rule:** Every column in SELECT that is NOT an aggregate function MUST be in GROUP BY.

```sql
-- WRONG (name is not in GROUP BY and not aggregated):
SELECT dept_id, name, COUNT(*) FROM employees GROUP BY dept_id;

-- RIGHT (only dept_id in SELECT non-aggregated, and it's in GROUP BY):
SELECT dept_id, COUNT(*) FROM employees GROUP BY dept_id;
```

---

### L2-Q3 · Total Salary Budget per Department

**Question:** What is the total salary cost for each department?

```sql
SELECT
  dept_id,
  COUNT(emp_id)              AS headcount,
  SUM(amount)                AS total_salary,
  ROUND(AVG(amount), 0)      AS avg_salary,
  MIN(amount)                AS lowest_salary,
  MAX(amount)                AS highest_salary
FROM employees e
JOIN salaries s ON e.emp_id = s.emp_id
WHERE s.to_date IS NULL       -- only current salaries
GROUP BY dept_id
ORDER BY total_salary DESC;
```

> **Why `WHERE s.to_date IS NULL`?**
```
Each employee can have multiple salary records (one per raise).
to_date IS NULL means "this is their current salary" (no end date yet).
Without this filter, you'd sum ALL historical salaries — wrong!
```

---

### L2-Q4 · Departments with More Than 3 Employees

**Question:** Find departments that have more than 3 employees.

**Think:** Filter on a COUNT → that's HAVING, not WHERE.

```sql
SELECT
  dept_id,
  COUNT(*) AS headcount
FROM employees
GROUP BY dept_id
HAVING COUNT(*) > 3
ORDER BY headcount DESC;
```

### WHERE vs HAVING — Side by Side

```sql
-- WHERE: filters INDIVIDUAL ROWS before grouping
SELECT dept_id, COUNT(*)
FROM employees
WHERE is_active = TRUE        -- ← removes inactive rows first
GROUP BY dept_id;

-- HAVING: filters GROUPS after aggregation
SELECT dept_id, COUNT(*)
FROM employees
GROUP BY dept_id
HAVING COUNT(*) > 3;          -- ← keeps only big departments

-- BOTH together:
SELECT dept_id, COUNT(*)
FROM employees
WHERE is_active = TRUE        -- ← step 1: remove inactive employees
GROUP BY dept_id              -- ← step 2: group active employees by dept
HAVING COUNT(*) > 2;          -- ← step 3: only departments with 2+ active employees
```

---

### L2-Q5 · Average Salary by Job Title

**Question:** What is the average current salary for each job title?

```sql
SELECT
  e.job_title,
  COUNT(*)                   AS employee_count,
  ROUND(AVG(s.amount), 2)    AS avg_salary,
  MIN(s.amount)              AS min_salary,
  MAX(s.amount)              AS max_salary
FROM employees e
JOIN salaries s ON e.emp_id = s.emp_id
WHERE s.to_date IS NULL
GROUP BY e.job_title
ORDER BY avg_salary DESC;
```

---

### L2-Q6 · Employees Hired Each Year

**Question:** How many employees were hired in each year?

```sql
SELECT
  YEAR(hire_date)  AS hire_year,
  COUNT(*)         AS new_hires
FROM employees
GROUP BY YEAR(hire_date)
ORDER BY hire_year;
```

```
Result:
+-----------+-----------+
| hire_year | new_hires |
+-----------+-----------+
| 2015      | 1         |
| 2016      | 1         |
| 2017      | 1         |
| 2018      | 2         |
| 2019      | 2         |
| 2020      | 2         |
| 2021      | 2         |
| 2022      | 3         |
| 2023      | 1         |
+-----------+-----------+
```

---

### L2-Q7 · Departments Spending Over 200k on Salaries

**Question:** Which departments have a total current salary bill above $200,000?

```sql
SELECT
  e.dept_id,
  SUM(s.amount)  AS total_salary_bill
FROM employees e
JOIN salaries s ON e.emp_id = s.emp_id
WHERE s.to_date IS NULL
GROUP BY e.dept_id
HAVING SUM(s.amount) > 200000
ORDER BY total_salary_bill DESC;
```

---

### L2-Q8 · Count Active vs Inactive Employees

**Question:** Show a count of active and inactive employees side by side.

```sql
SELECT
  is_active,
  COUNT(*)  AS employee_count
FROM employees
GROUP BY is_active;
```

```sql
-- Nicer labels using CASE WHEN:
SELECT
  CASE WHEN is_active THEN 'Active' ELSE 'Inactive' END AS status,
  COUNT(*) AS count
FROM employees
GROUP BY is_active;
```

---

## ⭐⭐⭐ Level 3: Intermediate — All JOINs

> **Goal:** Combine data from multiple tables.
> **Concepts:** INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN, SELF JOIN, CROSS JOIN

---

### 💡 Tip Before You Start

```
A JOIN connects two tables using a common column (usually PK → FK).
Think of it as: "for each row in table A, find the matching row in table B".

The most important question to ask before every JOIN:
"Do I want ALL rows from one side, or ONLY the matching ones?"

All left rows?  → LEFT JOIN
Only matches?   → INNER JOIN (just JOIN)
```

### Visual Guide

```
  TABLE A: employees            TABLE B: departments
  +----+-------+--------+       +----+-------------+
  | 1  | Alice | dept 1 |       | 1  | Engineering |
  | 2  | Bob   | dept 2 |       | 2  | Marketing   |
  | 3  | Carol | NULL   |       | 5  | Legal       |  ← no employees
  +----+-------+--------+       +----+-------------+

  INNER JOIN (only matches):
  Alice → Engineering ✓
  Bob   → Marketing   ✓
  Carol → NULL        ✗ (no dept match, excluded)
  Legal → no employee ✗ (excluded)

  LEFT JOIN (all employees):
  Alice → Engineering ✓
  Bob   → Marketing   ✓
  Carol → NULL        ✓ (Carol kept, dept columns = NULL)

  RIGHT JOIN (all departments):
  Alice → Engineering ✓
  Bob   → Marketing   ✓
  Legal → no employee ✓ (Legal kept, employee columns = NULL)

  FULL OUTER JOIN (everything):
  Alice  → Engineering ✓
  Bob    → Marketing   ✓
  Carol  → NULL        ✓
  Legal  → no employee ✓
```

---

### L3-Q1 · Show Employees WITH Their Department Name

**Question:** List each employee's name with their actual department name (not just dept_id).

```sql
SELECT
  e.emp_id,
  e.name,
  e.job_title,
  d.dept_name,
  d.location
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
ORDER BY d.dept_name, e.name;
```

> **Step by step:**
```
FROM employees e          → start with employees table (alias: e)
JOIN departments d        → bring in departments table (alias: d)
ON e.dept_id = d.dept_id  → the bridge: match dept_id in both tables
SELECT e.name, d.dept_name → pick columns from both tables
```

> **Always use table aliases** — `e.name` and `d.name` are unambiguous.
> Without aliases, SQL won't know which table's `name` you mean.

---

### L3-Q2 · Show Department Name with Employee Count

**Question:** For each department, show the department name and how many employees it has.

```sql
SELECT
  d.dept_name,
  d.location,
  COUNT(e.emp_id)  AS employee_count
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name, d.location
ORDER BY employee_count DESC;
```

> **Why LEFT JOIN here?**
```
INNER JOIN → departments with NO employees would disappear.
LEFT JOIN  → ALL departments appear, even if employee_count = 0.

In this dataset, all departments have employees, but in real data
there may be newly created empty departments — LEFT JOIN captures them.
```

---

### L3-Q3 · Employees with Their Current Salary

**Question:** Show each employee's name, job title, and their current salary.

```sql
SELECT
  e.name,
  e.job_title,
  d.dept_name,
  s.amount  AS current_salary
FROM employees    e
JOIN departments  d ON e.dept_id  = d.dept_id
JOIN salaries     s ON e.emp_id   = s.emp_id
WHERE s.to_date IS NULL        -- current salary only
ORDER BY s.amount DESC;
```

> **Joining 3 tables — think of it as a chain:**
```
employees → departments   (get dept name)
employees → salaries      (get salary amount)
Both JOINs go THROUGH the employees table using its emp_id or dept_id.
```

---

### L3-Q4 · Departments with No Projects

**Question:** Which departments currently have no projects assigned?

```sql
SELECT
  d.dept_id,
  d.dept_name
FROM departments  d
LEFT JOIN projects p ON d.dept_id = p.dept_id
WHERE p.proj_id IS NULL;
```

> **The LEFT JOIN + IS NULL pattern (Anti-Join):**
```
This is THE classic pattern for "find rows with no match".

LEFT JOIN keeps ALL departments.
For departments WITH projects → p.proj_id has a real value.
For departments WITHOUT projects → p.proj_id is NULL.
WHERE p.proj_id IS NULL → keep only the "no match" rows.

Memorise this pattern. It comes up in almost every SQL interview.
```

---

### L3-Q5 · Each Employee and Their Manager's Name (SELF JOIN)

**Question:** Show each employee alongside their manager's name.

```sql
SELECT
  e.name        AS employee,
  e.job_title   AS employee_role,
  m.name        AS manager_name,
  m.job_title   AS manager_role
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.emp_id
ORDER BY m.name NULLS LAST, e.name;
```

> **Self-Join explained:**
```
employees table has a manager_id column that points to another row
in the SAME employees table.

We join the table to itself using TWO different aliases:
  e = the employee
  m = the manager (also from the employees table)

  e.manager_id = m.emp_id  ← "the manager_id of the employee
                               matches the emp_id of the manager"

Why LEFT JOIN? Top-level managers (Sarah Connor, Lisa Park, etc.)
have manager_id = NULL. LEFT JOIN keeps them in the result with
manager_name = NULL. INNER JOIN would remove them.
```

---

### L3-Q6 · Employees and Projects in Their Department

**Question:** Show all employees alongside the projects their department is running.

```sql
SELECT
  e.name         AS employee,
  d.dept_name,
  p.proj_name,
  p.start_date,
  p.end_date
FROM employees    e
JOIN departments  d ON e.dept_id  = d.dept_id
JOIN projects     p ON d.dept_id  = p.dept_id
WHERE e.is_active = TRUE
ORDER BY d.dept_name, e.name, p.start_date;
```

---

### L3-Q7 · All Combinations of Departments and Locations (CROSS JOIN)

**Question:** Show every possible combination of department and location (for demonstration).

```sql
SELECT
  d.dept_name,
  l.location
FROM departments d
CROSS JOIN (
  SELECT DISTINCT location FROM departments
) l
ORDER BY d.dept_name;
```

> **CROSS JOIN in practice:**
```
CROSS JOIN creates a cartesian product — every row in A paired with every row in B.
If A has 6 rows and B has 5 rows → result has 30 rows.

Real uses: generating a report matrix, creating a date/dimension grid,
testing all combinations of settings.
Not often used, but examiners ask about it.
```

---

## ⭐⭐⭐⭐ Level 4: Intermediate+ — Subqueries & CTEs

> **Goal:** Write nested and modular queries.
> **Concepts:** Subqueries (scalar, correlated, multi-row), WITH (CTE), IN, EXISTS

---

### 💡 Tip Before You Start

```
A subquery is a query inside a query.
A CTE (Common Table Expression) is a named, reusable subquery.

Use subqueries when you need to:
  - Use an aggregate as a filter (WHERE salary > (SELECT AVG...))
  - Check existence in another table (WHERE EXISTS ...)
  - Break a complex problem into steps

Use CTEs when you need to:
  - Reuse the same subquery multiple times
  - Make a complex query readable (name each step)
  - Build up a multi-step solution clearly
```

---

### L4-Q1 · Employees Earning Above the Company Average

**Question:** Find employees whose current salary is above the company average.

```sql
SELECT
  e.name,
  e.job_title,
  s.amount              AS salary,
  (SELECT ROUND(AVG(amount), 0)
   FROM salaries
   WHERE to_date IS NULL) AS company_avg
FROM employees e
JOIN salaries s ON e.emp_id = s.emp_id
WHERE s.to_date IS NULL
  AND s.amount > (
    SELECT AVG(amount)
    FROM salaries
    WHERE to_date IS NULL
  )
ORDER BY s.amount DESC;
```

> **The subquery `(SELECT AVG(...))` runs once, returns a single number, and that number is used as the filter.**
> This is called a **scalar subquery** — it returns exactly one value.

---

### L4-Q2 · Departments with Above-Average Budget

**Question:** Find departments whose budget is higher than the average department budget.

```sql
SELECT
  dept_name,
  budget,
  ROUND((SELECT AVG(budget) FROM departments), 0) AS avg_budget
FROM departments
WHERE budget > (SELECT AVG(budget) FROM departments)
ORDER BY budget DESC;
```

---

### L4-Q3 · Find the Highest Paid Employee Using Subquery

**Question:** Find the employee(s) with the highest current salary.

```sql
-- Method 1: Subquery with MAX
SELECT e.name, e.job_title, s.amount
FROM employees e
JOIN salaries s ON e.emp_id = s.emp_id
WHERE s.to_date IS NULL
  AND s.amount = (
    SELECT MAX(amount)
    FROM salaries
    WHERE to_date IS NULL
  );
```

> **Why not just `ORDER BY amount DESC LIMIT 1`?**
```
If two employees both earn $200,000:
  LIMIT 1 → returns only ONE (arbitrary which one!)
  MAX subquery → returns BOTH (correct!)

In interviews, always ask: "What if there are ties?"
Using a subquery with MAX is the safe, correct answer.
```

---

### L4-Q4 · Employees in Departments That Have a Project

**Question:** List employees who belong to departments that currently have at least one project.

```sql
-- Method 1: IN with subquery
SELECT e.name, e.job_title, e.dept_id
FROM employees e
WHERE e.dept_id IN (
  SELECT DISTINCT dept_id FROM projects
)
ORDER BY e.dept_id;

-- Method 2: EXISTS (faster on large tables)
SELECT e.name, e.job_title, e.dept_id
FROM employees e
WHERE EXISTS (
  SELECT 1
  FROM projects p
  WHERE p.dept_id = e.dept_id    -- references the outer query!
)
ORDER BY e.dept_id;
```

### IN vs EXISTS — Visual Explanation

```
IN: builds the full list first, then checks each employee against it.
  Step 1: SELECT DISTINCT dept_id FROM projects → [1, 2, 3, 4, 5, 6]
  Step 2: For each employee, check if dept_id is in [1, 2, 3, 4, 5, 6]

EXISTS: for each employee, checks if at least ONE project match exists, then stops.
  For each employee:
    Does a project with this dept_id exist? YES → include. STOP LOOKING.

EXISTS is faster when the subquery returns many rows
because it stops at the FIRST match.
```

---

### L4-Q5 · Employees Who Got a Salary Raise

**Question:** Find employees who have more than one salary record (meaning they received a raise).

```sql
-- Using subquery
SELECT e.name, e.job_title
FROM employees e
WHERE e.emp_id IN (
  SELECT emp_id
  FROM salaries
  GROUP BY emp_id
  HAVING COUNT(*) > 1
)
ORDER BY e.name;
```

```sql
-- Using CTE (more readable):
WITH raised_employees AS (
  SELECT emp_id, COUNT(*) AS salary_records
  FROM salaries
  GROUP BY emp_id
  HAVING COUNT(*) > 1
)
SELECT e.name, e.job_title, r.salary_records
FROM employees      e
JOIN raised_employees r ON e.emp_id = r.emp_id
ORDER BY r.salary_records DESC;
```

---

### L4-Q6 · Step-by-Step with CTE: Dept Summary

**Question:** For each department, show: name, headcount, total salary, avg salary, number of projects. Use a CTE to keep it clean.

```sql
-- Build it step by step with CTEs:
WITH dept_headcount AS (
  SELECT dept_id, COUNT(*) AS headcount
  FROM employees
  WHERE is_active = TRUE
  GROUP BY dept_id
),
dept_salary AS (
  SELECT e.dept_id,
         SUM(s.amount)           AS total_salary,
         ROUND(AVG(s.amount), 0) AS avg_salary
  FROM employees e
  JOIN salaries  s ON e.emp_id = s.emp_id
  WHERE s.to_date IS NULL
  GROUP BY e.dept_id
),
dept_projects AS (
  SELECT dept_id, COUNT(*) AS project_count
  FROM projects
  GROUP BY dept_id
)
SELECT
  d.dept_name,
  d.location,
  COALESCE(h.headcount,     0)  AS headcount,
  COALESCE(sal.total_salary, 0) AS total_salary,
  COALESCE(sal.avg_salary,   0) AS avg_salary,
  COALESCE(p.project_count,  0) AS projects
FROM departments   d
LEFT JOIN dept_headcount h   ON d.dept_id = h.dept_id
LEFT JOIN dept_salary    sal ON d.dept_id = sal.dept_id
LEFT JOIN dept_projects  p   ON d.dept_id = p.dept_id
ORDER BY total_salary DESC;
```

> **CTE tip:** Name each CTE clearly — `dept_headcount`, `dept_salary`, etc.
> The interviewer can follow your logic without you explaining it.
> Clean CTEs = clean thinking.

---

### L4-Q7 · Correlated Subquery: Employees Earning More Than Dept Average

**Question:** Find employees who earn more than the average salary in their own department.

```sql
SELECT
  e.name,
  e.job_title,
  e.dept_id,
  s.amount AS salary
FROM employees e
JOIN salaries  s ON e.emp_id = s.emp_id
WHERE s.to_date IS NULL
  AND s.amount > (
    SELECT AVG(s2.amount)
    FROM employees e2
    JOIN salaries  s2 ON e2.emp_id = s2.emp_id
    WHERE s2.to_date IS NULL
      AND e2.dept_id = e.dept_id    -- ← references OUTER query's dept_id!
  )
ORDER BY e.dept_id, s.amount DESC;
```

### Correlated vs Regular Subquery

```
Regular subquery:
  Runs ONCE. Returns one fixed value.
  WHERE salary > (SELECT AVG(salary) FROM salaries WHERE to_date IS NULL)
                  ↑ runs once, returns e.g. 95000

Correlated subquery:
  Runs ONCE PER ROW of the outer query.
  WHERE salary > (SELECT AVG(s2.amount) ... WHERE e2.dept_id = e.dept_id)
                                                 ↑ changes for each employee row!

For Engineering employee → compares to Engineering average
For Marketing employee   → compares to Marketing average
```

---

## ⭐⭐⭐⭐⭐ Level 5: Advanced — Window Functions

> **Goal:** Analyse data across rows without collapsing them.
> **Concepts:** RANK, DENSE_RANK, ROW_NUMBER, SUM OVER, AVG OVER, LAG, LEAD, PARTITION BY

---

### 💡 Tip Before You Start

```
Window functions are like GROUP BY — but they DON'T collapse rows.
Every row keeps its own identity, but also gets a new calculated column.

GROUP BY:        1 row per group   (collapses)
Window function: 1 row per original row + extra calculated column (doesn't collapse)

Syntax:
FUNCTION() OVER (
  PARTITION BY column   ← like GROUP BY within the window
  ORDER BY column       ← defines the sequence for ranking/running totals
)
```

---

### L5-Q1 · Rank Employees by Salary

**Question:** Rank every employee by their current salary, highest first.

```sql
SELECT
  e.name,
  e.job_title,
  s.amount                                          AS salary,
  RANK()        OVER (ORDER BY s.amount DESC)       AS rank_w_gaps,
  DENSE_RANK()  OVER (ORDER BY s.amount DESC)       AS rank_no_gaps,
  ROW_NUMBER()  OVER (ORDER BY s.amount DESC)       AS row_num
FROM employees e
JOIN salaries  s ON e.emp_id = s.emp_id
WHERE s.to_date IS NULL
ORDER BY s.amount DESC;
```

### RANK vs DENSE_RANK vs ROW_NUMBER — Side by Side

```
Salary:       200000  160000  150000  140000  120000  115000 ...
Employee:     Emma    Sarah   Lisa    (tie)   Olivia  Nina

RANK:            1       2      3        4      5       6
  → After Emma (1) and Sarah (2), if TWO people tie at rank 3,
    next rank SKIPS to 5 (gap). Like Olympic medals — two silvers, no bronze.

DENSE_RANK:      1       2      3        3      4       5
  → Same tie, but next rank is 4 (no gap). Dense = no empty positions.

ROW_NUMBER:      1       2      3        4      5       6
  → Ties are broken arbitrarily. Every row gets a unique number.

Interview memory:
  "RANK = Olympic medals (skips after tie)"
  "DENSE_RANK = no skipping (use for Nth highest!)"
  "ROW_NUMBER = always unique"
```

---

### L5-Q2 · Rank Employees Within Each Department

**Question:** Rank employees by salary within their own department.

```sql
SELECT
  e.name,
  d.dept_name,
  s.amount                                                             AS salary,
  DENSE_RANK() OVER (
    PARTITION BY e.dept_id           -- restart ranking for each dept
    ORDER BY s.amount DESC
  )                                                                    AS dept_rank
FROM employees   e
JOIN departments d ON e.dept_id  = d.dept_id
JOIN salaries    s ON e.emp_id   = s.emp_id
WHERE s.to_date IS NULL
ORDER BY d.dept_name, dept_rank;
```

> **PARTITION BY = GROUP BY inside the window:**
```
Without PARTITION BY:  rank all 15 employees together (1 to 15)
With PARTITION BY dept_id:
  Engineering employees ranked 1-4 (within Engineering)
  Marketing employees ranked 1-4   (within Marketing)
  HR employees ranked 1-2          (within HR)
  Each department gets its OWN fresh ranking.
```

---

### L5-Q3 · Running Total of Salary by Hire Date

**Question:** Show the cumulative total salary spend as employees were hired (in hire order).

```sql
SELECT
  e.name,
  e.hire_date,
  s.amount                                                    AS salary,
  SUM(s.amount) OVER (
    ORDER BY e.hire_date, e.emp_id      -- emp_id breaks ties on same date
  )                                                           AS running_total,
  ROUND(AVG(s.amount) OVER (
    ORDER BY e.hire_date, e.emp_id
  ), 0)                                                       AS running_avg
FROM employees e
JOIN salaries  s ON e.emp_id = s.emp_id
WHERE s.to_date IS NULL
ORDER BY e.hire_date, e.emp_id;
```

> **Running total visualised:**
```
hire_date   name    salary   running_total
2015-07-30  Emma    200000   200000        ← just Emma
2016-11-20  Nina    115000   315000        ← Emma + Nina
2017-09-05  Lisa    150000   465000        ← + Lisa
2018-03-01  Sarah   160000   625000        ← + Sarah
...each new row adds its salary to the total so far
```

---

### L5-Q4 · Compare Each Employee to Previous and Next Salary

**Question:** For each salary record, show the previous and next salary for the same employee.

```sql
SELECT
  e.name,
  s.amount,
  s.from_date,
  LAG (s.amount) OVER (PARTITION BY s.emp_id ORDER BY s.from_date) AS prev_salary,
  LEAD(s.amount) OVER (PARTITION BY s.emp_id ORDER BY s.from_date) AS next_salary,
  s.amount - LAG(s.amount) OVER (
    PARTITION BY s.emp_id ORDER BY s.from_date
  )                                                                 AS raise_amount
FROM salaries  s
JOIN employees e ON s.emp_id = e.emp_id
ORDER BY e.name, s.from_date;
```

> **LAG and LEAD:**
```
LAG(col)  → value from the PREVIOUS row in the window
LEAD(col) → value from the NEXT row in the window

PARTITION BY emp_id means: only look at previous/next rows
for the SAME employee (don't cross employee boundaries).

This is how you calculate raise amounts, month-over-month growth,
or any "compare to previous period" analysis.
```

---

### L5-Q5 · Find the Top Earner in Each Department

**Question:** Show only the highest-paid employee in each department.

```sql
WITH ranked AS (
  SELECT
    e.name,
    d.dept_name,
    s.amount   AS salary,
    DENSE_RANK() OVER (
      PARTITION BY e.dept_id
      ORDER BY s.amount DESC
    ) AS dept_rank
  FROM employees   e
  JOIN departments d ON e.dept_id = d.dept_id
  JOIN salaries    s ON e.emp_id  = s.emp_id
  WHERE s.to_date IS NULL
)
SELECT dept_name, name, salary
FROM   ranked
WHERE  dept_rank = 1
ORDER BY salary DESC;
```

> **This is the canonical "top N per group" pattern. Memorise it.**

---

### L5-Q6 · Salary as Percentage of Department Total

**Question:** For each employee, show their salary and what percentage of their department's total salary budget it represents.

```sql
SELECT
  e.name,
  d.dept_name,
  s.amount                                                          AS salary,
  SUM(s.amount) OVER (PARTITION BY e.dept_id)                      AS dept_total,
  ROUND(s.amount * 100.0 /
        SUM(s.amount) OVER (PARTITION BY e.dept_id), 1)            AS pct_of_dept
FROM employees   e
JOIN departments d ON e.dept_id = d.dept_id
JOIN salaries    s ON e.emp_id  = s.emp_id
WHERE s.to_date IS NULL
ORDER BY d.dept_name, pct_of_dept DESC;
```

---

## 🔥 Level 6: Tricky Interview Questions

> **These are real questions asked in SQL interviews.**
> They test whether you can think carefully, handle edge cases, and write clean queries.

---

### 💡 How to Handle Tricky Questions in Interviews

```
1. Don't panic. Read the question twice.
2. Think out loud: "I need to... first, then..."
3. Start simple. Get it working, then optimise.
4. Ask about edge cases: "What if there are ties?" "What if a value is NULL?"
5. Show multiple solutions if you know them.
```

---

### 🔥 T1 · Find the Second Highest Salary

**Question:** Find the second highest distinct salary in the company.

```sql
-- Method 1: DENSE_RANK (best — handles ties correctly)
WITH ranked AS (
  SELECT
    amount,
    DENSE_RANK() OVER (ORDER BY amount DESC) AS rnk
  FROM salaries
  WHERE to_date IS NULL
)
SELECT DISTINCT amount AS second_highest_salary
FROM ranked
WHERE rnk = 2;

-- Method 2: Subquery
SELECT MAX(amount) AS second_highest
FROM salaries
WHERE to_date IS NULL
  AND amount < (SELECT MAX(amount) FROM salaries WHERE to_date IS NULL);

-- Method 3: OFFSET
SELECT DISTINCT amount
FROM salaries
WHERE to_date IS NULL
ORDER BY amount DESC
LIMIT 1 OFFSET 1;    -- skip the 1st, take the 2nd
```

> **Trap:** What if no second salary exists? (all employees have same salary, or only 1 employee)
```sql
-- Safe version that returns NULL instead of no rows:
SELECT IFNULL(
  (SELECT DISTINCT amount FROM salaries WHERE to_date IS NULL
   ORDER BY amount DESC LIMIT 1 OFFSET 1),
  NULL
) AS second_highest;
```

---

### 🔥 T2 · Find Employees Who Never Got a Raise

**Question:** Find employees who have only ONE salary record (never got a raise).

```sql
SELECT
  e.name,
  e.job_title,
  e.hire_date,
  s.amount AS current_salary
FROM employees e
JOIN salaries  s ON e.emp_id = s.emp_id
WHERE s.to_date IS NULL
  AND e.emp_id NOT IN (
    SELECT emp_id
    FROM salaries
    GROUP BY emp_id
    HAVING COUNT(*) > 1
  )
ORDER BY e.hire_date;
```

```sql
-- Alternative using LEFT JOIN anti-join:
WITH raised AS (
  SELECT emp_id FROM salaries GROUP BY emp_id HAVING COUNT(*) > 1
)
SELECT e.name, e.job_title, e.hire_date
FROM employees e
LEFT JOIN raised r ON e.emp_id = r.emp_id
WHERE r.emp_id IS NULL;
```

---

### 🔥 T3 · Find Duplicate Rows

**Question:** The salaries table might have accidental duplicate entries (same emp_id and same from_date). Find them.

```sql
-- Step 1: Find which (emp_id, from_date) combinations are duplicated
SELECT
  emp_id,
  from_date,
  COUNT(*) AS duplicate_count
FROM salaries
GROUP BY emp_id, from_date
HAVING COUNT(*) > 1;

-- Step 2: See the actual duplicate rows
SELECT *
FROM salaries
WHERE (emp_id, from_date) IN (
  SELECT emp_id, from_date
  FROM salaries
  GROUP BY emp_id, from_date
  HAVING COUNT(*) > 1
)
ORDER BY emp_id, from_date;
```

---

### 🔥 T4 · Manager Who Manages the Most People

**Question:** Which manager has the most direct reports?

```sql
SELECT
  m.name             AS manager_name,
  m.job_title        AS manager_title,
  COUNT(e.emp_id)    AS direct_reports
FROM employees e
JOIN employees m ON e.manager_id = m.emp_id   -- self-join: e=subordinate, m=manager
GROUP BY m.emp_id, m.name, m.job_title
ORDER BY direct_reports DESC
LIMIT 1;
```

> **Variation:** "Show all employees and their manager's headcount (how many people their manager manages)."
```sql
WITH manager_counts AS (
  SELECT manager_id, COUNT(*) AS direct_reports
  FROM employees
  WHERE manager_id IS NOT NULL
  GROUP BY manager_id
)
SELECT
  e.name,
  e.job_title,
  COALESCE(mc.direct_reports, 0) AS their_manager_has_n_reports
FROM employees       e
LEFT JOIN manager_counts mc ON e.manager_id = mc.manager_id;
```

---

### 🔥 T5 · Year-over-Year Salary Growth per Employee

**Question:** For each salary raise, calculate the percentage increase.

```sql
SELECT
  e.name,
  s.from_date,
  s.amount                                          AS new_salary,
  LAG(s.amount) OVER (
    PARTITION BY s.emp_id ORDER BY s.from_date
  )                                                 AS old_salary,
  ROUND(
    (s.amount - LAG(s.amount) OVER (
      PARTITION BY s.emp_id ORDER BY s.from_date
    )) * 100.0
    / LAG(s.amount) OVER (
      PARTITION BY s.emp_id ORDER BY s.from_date
    ),
    1
  )                                                 AS pct_increase
FROM salaries  s
JOIN employees e ON s.emp_id = e.emp_id
ORDER BY e.name, s.from_date;
```

---

### 🔥 T6 · Employees Hired in the Same Month as Someone Else

**Question:** Find pairs of employees who were hired in the same month and year.

```sql
SELECT
  e1.name        AS employee_1,
  e2.name        AS employee_2,
  e1.hire_date   AS hire_date_1,
  e2.hire_date   AS hire_date_2
FROM employees e1
JOIN employees e2
  ON  YEAR(e1.hire_date)  = YEAR(e2.hire_date)
  AND MONTH(e1.hire_date) = MONTH(e2.hire_date)
  AND e1.emp_id < e2.emp_id    -- avoid duplicates (A,B) and (B,A) and (A,A)
ORDER BY e1.hire_date;
```

> **The `e1.emp_id < e2.emp_id` trick:**
```
Without it:
  (Alice, Bob) AND (Bob, Alice) AND (Alice, Alice) — all appear!
With e1.emp_id < e2.emp_id:
  Only (Alice, Bob) appears — each pair shown once, no self-matches.
```

---

### 🔥 T7 · Classify Employees by Salary Band (CASE WHEN)

**Question:** Label each employee as 'Executive', 'Senior', 'Mid', or 'Junior' based on their salary.

```sql
SELECT
  e.name,
  e.job_title,
  d.dept_name,
  s.amount,
  CASE
    WHEN s.amount >= 150000 THEN 'Executive'
    WHEN s.amount >= 100000 THEN 'Senior'
    WHEN s.amount >=  70000 THEN 'Mid-level'
    ELSE                         'Junior'
  END                                               AS salary_band,
  CASE
    WHEN s.amount >= 150000 THEN '💎 Executive'
    WHEN s.amount >= 100000 THEN '🔷 Senior'
    WHEN s.amount >=  70000 THEN '🔹 Mid-level'
    ELSE                         '◽ Junior'
  END                                               AS band_label
FROM employees   e
JOIN departments d ON e.dept_id = d.dept_id
JOIN salaries    s ON e.emp_id  = s.emp_id
WHERE s.to_date IS NULL
ORDER BY s.amount DESC;
```

---

### 🔥 T8 · Projects Running Over Budget

**Question:** Find projects whose budget is more than the average project budget in their department.

```sql
WITH dept_avg_budget AS (
  SELECT
    dept_id,
    ROUND(AVG(budget), 0) AS avg_proj_budget
  FROM projects
  GROUP BY dept_id
)
SELECT
  p.proj_name,
  d.dept_name,
  p.budget,
  da.avg_proj_budget
FROM projects         p
JOIN departments      d  ON p.dept_id = d.dept_id
JOIN dept_avg_budget  da ON p.dept_id = da.dept_id
WHERE p.budget > da.avg_proj_budget
ORDER BY p.budget DESC;
```

---

### 🔥 T9 · Employees Whose Salary Is Exactly the Department Median

**Question:** This is a hard one. Find employees earning the median salary in their department.

```sql
WITH salary_ranked AS (
  SELECT
    e.emp_id,
    e.name,
    e.dept_id,
    s.amount,
    ROW_NUMBER() OVER (PARTITION BY e.dept_id ORDER BY s.amount)          AS rn,
    COUNT(*)     OVER (PARTITION BY e.dept_id)                            AS dept_count
  FROM employees e
  JOIN salaries  s ON e.emp_id = s.emp_id
  WHERE s.to_date IS NULL
)
SELECT
  sr.name,
  d.dept_name,
  sr.amount AS median_salary
FROM salary_ranked sr
JOIN departments   d ON sr.dept_id = d.dept_id
WHERE rn IN (
  FLOOR((dept_count + 1) / 2.0),
  CEIL( (dept_count + 1) / 2.0)
)
ORDER BY d.dept_name;
```

> **The median formula:**
```
For N values sorted ascending:
  If N is odd:  median is at position (N+1)/2
  If N is even: median is average of positions N/2 and (N/2)+1

FLOOR and CEIL handle both cases cleanly.
```

---

### 🔥 T10 · Write a Query Without Using DISTINCT

**Question:** Get a list of unique departments that have at least one active employee — but without using DISTINCT.

```sql
-- Without DISTINCT, use GROUP BY:
SELECT dept_id
FROM employees
WHERE is_active = TRUE
GROUP BY dept_id;

-- Or using EXISTS:
SELECT dept_id, dept_name
FROM departments d
WHERE EXISTS (
  SELECT 1 FROM employees e
  WHERE e.dept_id = d.dept_id
    AND e.is_active = TRUE
);
```

> **Why would an interviewer ask this?**
```
To check if you understand that DISTINCT and GROUP BY solve the same
deduplication problem in different ways.
Also tests whether you know EXISTS.
```

---

### 🔥 T11 · DELETE Duplicate Salary Records (Keeping Latest)

**Question:** If a salary has two identical records for the same emp_id and from_date, keep only the one with the highest salary_id and delete the rest.

```sql
-- Step 1: See what you're about to delete (ALWAYS do this first!)
SELECT *
FROM salaries s1
WHERE s1.salary_id NOT IN (
  SELECT MAX(salary_id)
  FROM salaries
  GROUP BY emp_id, from_date
);

-- Step 2: Delete after confirming the preview looks right
DELETE FROM salaries
WHERE salary_id NOT IN (
  SELECT MAX(salary_id)
  FROM salaries
  GROUP BY emp_id, from_date
);
```

> **Golden rule for DELETE queries:**
```
ALWAYS run a SELECT with the same WHERE clause first.
Look at what you're about to delete.
Then change SELECT to DELETE.
Never skip the preview step.
```

---

## 🎁 Bonus Challenges

> Try these on your own. Answers not provided — figure them out!

```
B1. Show each department's highest, lowest, and average salary on one row,
    along with how many employees earn above the department average.

B2. Find the employee who has been with the company the longest
    and the one hired most recently.

B3. List all managers who manage employees in more than one department.
    (Hint: managers can sometimes manage cross-department.)

B4. Find employees who share the same job title but are in different departments.

B5. Show a month-by-month count of how many employees were active
    during each month of 2023.

B6. Write a query that shows whether each project finished on time,
    is still ongoing, or went over the planned end date.
    (end_date is NULL = still running)

B7. Find the department where the gap between the highest and lowest
    salary is the smallest.
```

---

## 📌 Pattern Cheatsheet

### The Most Common SQL Patterns

```sql
-- PATTERN 1: Count rows with a condition
SELECT COUNT(*) FROM employees WHERE is_active = TRUE;

-- PATTERN 2: Aggregate per group
SELECT dept_id, SUM(amount) FROM salaries GROUP BY dept_id;

-- PATTERN 3: Filter on aggregate (HAVING)
SELECT dept_id, COUNT(*) FROM employees GROUP BY dept_id HAVING COUNT(*) > 3;

-- PATTERN 4: Find rows with NO match (anti-join)
SELECT * FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;

-- PATTERN 5: Use aggregate as a filter
SELECT name FROM employees WHERE salary > (SELECT AVG(salary) FROM salaries);

-- PATTERN 6: Top N per group
WITH ranked AS (
  SELECT *, DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk
  FROM ...
)
SELECT * FROM ranked WHERE rnk <= 3;

-- PATTERN 7: Running total
SELECT date, amount, SUM(amount) OVER (ORDER BY date) AS running_total FROM ...;

-- PATTERN 8: Compare to previous row
SELECT *, LAG(amount) OVER (PARTITION BY emp_id ORDER BY date) AS prev_amount FROM ...;

-- PATTERN 9: Self-join (hierarchies)
SELECT e.name AS employee, m.name AS manager
FROM employees e LEFT JOIN employees m ON e.manager_id = m.emp_id;

-- PATTERN 10: Classify rows with CASE WHEN
SELECT name, CASE WHEN salary > 100000 THEN 'Senior' ELSE 'Junior' END AS band
FROM employees;
```

---

### Words → SQL Translation

```
"how many"           → COUNT(*)
"total / sum of"     → SUM()
"average"            → AVG()
"highest / maximum"  → MAX() or ORDER BY DESC LIMIT 1
"lowest / minimum"   → MIN() or ORDER BY ASC LIMIT 1
"per / each / by"    → GROUP BY
"only if more than"  → HAVING (after GROUP BY)
"with no / never"    → LEFT JOIN + IS NULL, or NOT EXISTS
"top N"              → DENSE_RANK() + WHERE rank <= N
"rank within group"  → DENSE_RANK() OVER (PARTITION BY ...)
"running total"      → SUM() OVER (ORDER BY ...)
"compare to prev"    → LAG() OVER (PARTITION BY ... ORDER BY ...)
"classify / label"   → CASE WHEN ... THEN ... END
"exists in / at least one" → EXISTS or IN
"step by step"       → CTE (WITH clause)
```

---

### Common Mistakes to Avoid

```
❌ WHERE COUNT(*) > 5          → ✅ HAVING COUNT(*) > 5
❌ WHERE column = NULL         → ✅ WHERE column IS NULL
❌ SELECT * in production      → ✅ SELECT only needed columns
❌ ORDER BY + LIMIT for Nth    → ✅ DENSE_RANK() for Nth highest
❌ NOT IN when NULLs possible  → ✅ NOT EXISTS (safer)
❌ GROUP BY name only          → ✅ GROUP BY primary key + name
❌ INNER JOIN for "all + zero" → ✅ LEFT JOIN for "include zeros"
❌ YEAR(col) = 2022 in WHERE   → ✅ col BETWEEN '2022-01-01' AND '2022-12-31'
❌ Running LIMIT without ORDER → ✅ Always ORDER BY before LIMIT
❌ Forgetting DISTINCT in JOINs→ ✅ COUNT(DISTINCT order_id)
```

---

### Practice Sites (Free)

```
+---------------------------+-----------------------------------------------+
| Site                      | What's great about it                         |
+---------------------------+-----------------------------------------------+
| leetcode.com/sql          | 200+ real interview questions, easy to hard   |
| hackerrank.com/sql        | Structured levels, good for beginners         |
| sqlzoo.net                | Interactive, learn-by-doing format            |
| db-fiddle.com             | Paste and run SQL in browser instantly        |
| stratascratch.com         | Real company SQL questions (Google, Amazon)   |
| mode.com/sql-tutorial     | Great explanations + built-in editor          |
+---------------------------+-----------------------------------------------+
```

---

> **Final thought:**
> SQL mastery comes from writing queries, not just reading them.
> Set up this schema in any SQL editor and try every question from scratch.
> The more you type, the more natural it becomes.
> Good luck — you've got this! 🚀
