# SQL Interview Questions — Salary & Core Patterns

> Organised from **easy → hard** across 5 categories. Every query uses a single `employees` table unless stated otherwise.

---

## Table Schema (used throughout)

```sql
CREATE TABLE employees (
  id          INT PRIMARY KEY,
  name        VARCHAR(100),
  salary      DECIMAL(10,2),
  department  VARCHAR(50),
  manager_id  INT  -- references id of the manager row
);
```

---

## Category 1 — Basic Salary Queries ⭐ Easy

These are the first questions an interviewer asks to warm up.

---

### Q1 — Find the highest salary

```sql
SELECT MAX(salary)
FROM employees;
```

---

### Q2 — Find the 2nd highest salary

```sql
SELECT MAX(salary)
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

> **Why it works:** The subquery finds the top salary, then the outer query finds the max of everything below it.

---

### Q3 — Find employees with the highest salary

```sql
SELECT *
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);
```

> **Note:** Returns all employees tied at the top — not just one row.

---

### Q4 — Find department-wise highest salary

```sql
SELECT department, MAX(salary) AS highest_salary
FROM employees
GROUP BY department;
```

---

## Category 2 — GROUP BY & HAVING ⭐⭐ Easy–Medium

Must-know patterns for filtering aggregated results.

---

### Q5 — Count employees in each department

```sql
SELECT department, COUNT(*) AS total
FROM employees
GROUP BY department;
```

---

### Q6 — Departments with more than 5 employees

```sql
SELECT department
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

> **Rule:** Use `WHERE` to filter rows before grouping. Use `HAVING` to filter after grouping.

---

### Q7 — Find duplicate records (by name)

```sql
SELECT name, COUNT(*) AS occurrences
FROM employees
GROUP BY name
HAVING COUNT(*) > 1;
```

---

## Category 3 — Subqueries ⭐⭐ Medium

Core interview favourites — shows you can think in layers.

---

### Q8 — Find employees above average salary

```sql
SELECT *
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

---

### Q9 — Find the 3rd highest salary (subquery style)

```sql
SELECT salary
FROM employees e1
WHERE 2 = (
    SELECT COUNT(DISTINCT salary)
    FROM employees e2
    WHERE e2.salary > e1.salary
);
```

> **Logic:** For the 3rd highest, exactly 2 distinct salaries must be greater than it.

---

### Q10 — Find the Nth highest salary without OFFSET (e.g. 5th)

```sql
SELECT DISTINCT salary
FROM employees e1
WHERE 5 = (
    SELECT COUNT(DISTINCT salary)
    FROM employees e2
    WHERE e2.salary >= e1.salary
);
```

> **Interview tip:** The interviewer often says "without using LIMIT/OFFSET" — this correlated subquery is the answer.

---

### Q11 — Find employees with same salary as someone else

```sql
SELECT *
FROM employees
WHERE salary IN (
    SELECT salary
    FROM employees
    GROUP BY salary
    HAVING COUNT(*) > 1
);
```

---

### Q12 — Find missing IDs in a sequence

```sql
SELECT id + 1 AS missing_id
FROM employees
WHERE (id + 1) NOT IN (SELECT id FROM employees);
```

---

## Category 4 — JOINs ⭐⭐ Medium

Shows you understand table relationships.

---

### Q13 — Find employees without a department

```sql
SELECT e.*
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id
WHERE d.id IS NULL;
```

> **Why LEFT JOIN + NULL?** LEFT JOIN keeps all employees. If no matching department, `d.id` is NULL.

---

### Q14 — Find employees earning more than their manager

```sql
SELECT e.name AS employee, e.salary, m.salary AS manager_salary
FROM employees e
JOIN employees m ON e.manager_id = m.id
WHERE e.salary > m.salary;
```

> **Self-join:** Same table joined to itself. Alias `e` = employee, alias `m` = their manager.

---

### Q15 — Top 3 highest salaries

```sql
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 3;
```

---

## Category 5 — Window Functions ⭐⭐⭐ Medium–Hard

Modern SQL interviews almost always include at least one window function question.

---

### Q16 — Rank employees by salary

```sql
SELECT
    name,
    salary,
    RANK() OVER (ORDER BY salary DESC) AS rnk
FROM employees;
```

> **RANK vs DENSE_RANK:** `RANK()` skips numbers after a tie (1,2,2,4). `DENSE_RANK()` does not (1,2,2,3).

---

### Q17 — Department-wise salary ranking

```sql
SELECT
    name,
    department,
    salary,
    DENSE_RANK() OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) AS dept_rank
FROM employees;
```

> **PARTITION BY** = reset the ranking for each department. Think of it like GROUP BY but for window functions.

---

### Q18 — Find the 2nd highest salary in each department

```sql
SELECT department, name, salary
FROM (
    SELECT
        department,
        name,
        salary,
        DENSE_RANK() OVER (
            PARTITION BY department
            ORDER BY salary DESC
        ) AS rnk
    FROM employees
) ranked
WHERE rnk = 2;
```

> **Pattern:** Wrap the window function in a subquery, then filter on the rank outside.

---

### Q19 — Running total of salary

```sql
SELECT
    name,
    salary,
    SUM(salary) OVER (ORDER BY id) AS running_total
FROM employees;
```

---

### Q20 — Find median salary

```sql
SELECT AVG(salary) AS median_salary
FROM (
    SELECT salary
    FROM employees
    ORDER BY salary
    LIMIT 2 - (SELECT COUNT(*) FROM employees) % 2
    OFFSET (SELECT (COUNT(*) - 1) / 2 FROM employees)
) t;
```

> **Hard one:** The LIMIT/OFFSET formula picks the middle 1 or 2 rows depending on odd/even count, then AVG handles both cases.

---

## Quick Reference Cheat Sheet

| Concept | Key Syntax |
|---|---|
| Highest salary | `MAX(salary)` |
| Nth highest (no OFFSET) | Correlated subquery with `COUNT(DISTINCT)` |
| Filter groups | `GROUP BY ... HAVING` |
| Self-join (manager) | `JOIN employees m ON e.manager_id = m.id` |
| No match (LEFT JOIN) | `LEFT JOIN ... WHERE right.id IS NULL` |
| Rank with gaps | `RANK() OVER (ORDER BY salary DESC)` |
| Rank without gaps | `DENSE_RANK() OVER (ORDER BY salary DESC)` |
| Per-group ranking | `DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC)` |
| Running total | `SUM(col) OVER (ORDER BY id)` |

---

## Interview Tips

1. **Always ask** — "Should I handle ties?" before writing a salary query. It decides RANK vs DENSE_RANK vs MAX.
2. **Correlated subquery** — When they say "without LIMIT/OFFSET", this is the answer.
3. **HAVING vs WHERE** — WHERE filters rows, HAVING filters groups. Say this out loud to the interviewer.
4. **Self-join** — The manager/employee question is always a self-join. Draw it on paper first.
5. **Window functions** — If the question says "per department" or "for each group", reach for PARTITION BY.