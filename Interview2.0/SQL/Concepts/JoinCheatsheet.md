# SQL JOIN Cheat Sheet

> Source: [Beekeeper Studio](https://beekeeperstudio.io/sql-join-cheat-sheet)

---

## INNER JOIN — Most Common

<svg width="100%" viewBox="0 0 260 100" role="img"><title>INNER JOIN diagram</title><desc>Two overlapping circles with only the intersection highlighted, representing INNER JOIN</desc>
  <circle cx="95" cy="50" r="42" fill="#B5D4F4" fill-opacity="0.35" stroke="#185FA5" stroke-width="1.5"/>
  <circle cx="165" cy="50" r="42" fill="#B5D4F4" fill-opacity="0.35" stroke="#185FA5" stroke-width="1.5"/>
  <clipPath id="innerA"><circle cx="95" cy="50" r="42"/></clipPath>
  <circle cx="165" cy="50" r="42" fill="#185FA5" fill-opacity="0.7" clip-path="url(#innerA)"/>
  <text font-family="sans-serif" font-size="11" font-weight="600" fill="#042C53" text-anchor="middle" x="75" y="54">A</text>
  <text font-family="sans-serif" font-size="11" font-weight="600" fill="#042C53" text-anchor="middle" x="185" y="54">B</text>
  <text font-family="sans-serif" font-size="10" fill="#fff" text-anchor="middle" x="130" y="54">∩</text>
</svg>

Returns only rows with matching values in **both** tables. Most efficient JOIN for performance.

```sql
SELECT orders.id, customers.name
FROM orders
INNER JOIN customers
ON orders.customer_id = customers.id
```

- Only matching records from both tables
- Can be written as just `JOIN`
- Filters non-matching rows

---

## LEFT JOIN

<svg width="100%" viewBox="0 0 260 100" role="img"><title>LEFT JOIN diagram</title><desc>Two overlapping circles with the entire left circle highlighted, representing LEFT JOIN</desc>
  <circle cx="95" cy="50" r="42" fill="#185FA5" fill-opacity="0.7" stroke="#185FA5" stroke-width="1.5"/>
  <circle cx="165" cy="50" r="42" fill="#B5D4F4" fill-opacity="0.25" stroke="#185FA5" stroke-width="1.5"/>
  <text font-family="sans-serif" font-size="11" font-weight="600" fill="#fff" text-anchor="middle" x="75" y="54">A</text>
  <text font-family="sans-serif" font-size="11" font-weight="600" fill="#042C53" text-anchor="middle" x="185" y="54">B</text>
</svg>

Returns **all rows from the left table** and matching rows from the right table. `NULL` for non-matches.

```sql
SELECT customers.name, orders.amount
FROM customers
LEFT JOIN orders
ON customers.id = orders.customer_id
```

- Preserves all left table records
- Also called `LEFT OUTER JOIN`
- Useful to find records without related data

---

## RIGHT JOIN

<svg width="100%" viewBox="0 0 260 100" role="img"><title>RIGHT JOIN diagram</title><desc>Two overlapping circles with the entire right circle highlighted, representing RIGHT JOIN</desc>
  <circle cx="95" cy="50" r="42" fill="#B5D4F4" fill-opacity="0.25" stroke="#185FA5" stroke-width="1.5"/>
  <circle cx="165" cy="50" r="42" fill="#185FA5" fill-opacity="0.7" stroke="#185FA5" stroke-width="1.5"/>
  <text font-family="sans-serif" font-size="11" font-weight="600" fill="#042C53" text-anchor="middle" x="75" y="54">A</text>
  <text font-family="sans-serif" font-size="11" font-weight="600" fill="#fff" text-anchor="middle" x="185" y="54">B</text>
</svg>

Returns **all rows from the right table** and matching rows from the left table. Opposite of `LEFT JOIN`.

```sql
SELECT orders.amount, customers.name
FROM orders
RIGHT JOIN customers
ON orders.customer_id = customers.id
```

- Preserves all right table records
- Can be rewritten as a `LEFT JOIN`
- Also called `RIGHT OUTER JOIN`

---

## FULL OUTER JOIN

<svg width="100%" viewBox="0 0 260 100" role="img"><title>FULL OUTER JOIN diagram</title><desc>Two overlapping circles both fully highlighted, representing FULL OUTER JOIN</desc>
  <circle cx="95" cy="50" r="42" fill="#185FA5" fill-opacity="0.65" stroke="#185FA5" stroke-width="1.5"/>
  <circle cx="165" cy="50" r="42" fill="#185FA5" fill-opacity="0.65" stroke="#185FA5" stroke-width="1.5"/>
  <text font-family="sans-serif" font-size="11" font-weight="600" fill="#fff" text-anchor="middle" x="75" y="54">A</text>
  <text font-family="sans-serif" font-size="11" font-weight="600" fill="#fff" text-anchor="middle" x="185" y="54">B</text>
</svg>

Returns **all rows from both tables** with `NULL` where no matches exist in either direction.

```sql
SELECT customers.name, orders.amount
FROM customers
FULL OUTER JOIN orders
ON customers.id = orders.customer_id
```

- Combines `LEFT` and `RIGHT JOIN`
- ⚠️ Not supported in MySQL
- Shows all relationships and gaps

---

## CROSS JOIN — ⚠️ Caution

<svg width="100%" viewBox="0 0 260 100" role="img"><title>CROSS JOIN diagram</title><desc>Two separate rectangles with a grid between them showing Cartesian product</desc>
  <rect x="20" y="25" width="60" height="50" rx="6" fill="#B5D4F4" fill-opacity="0.4" stroke="#185FA5" stroke-width="1.5"/>
  <rect x="180" y="25" width="60" height="50" rx="6" fill="#B5D4F4" fill-opacity="0.4" stroke="#185FA5" stroke-width="1.5"/>
  <text font-family="sans-serif" font-size="11" font-weight="600" fill="#042C53" text-anchor="middle" x="50" y="54">A</text>
  <text font-family="sans-serif" font-size="11" font-weight="600" fill="#042C53" text-anchor="middle" x="210" y="54">B</text>
  <!-- grid symbol in center -->
  <g stroke="#185FA5" stroke-width="1" stroke-opacity="0.6">
    <line x1="105" y1="30" x2="155" y2="30"/>
    <line x1="105" y1="45" x2="155" y2="45"/>
    <line x1="105" y1="60" x2="155" y2="60"/>
    <line x1="105" y1="75" x2="155" y2="75"/>
    <line x1="115" y1="20" x2="115" y2="80"/>
    <line x1="130" y1="20" x2="130" y2="80"/>
    <line x1="145" y1="20" x2="145" y2="80"/>
  </g>
  <text font-family="sans-serif" font-size="9" fill="#042C53" text-anchor="middle" x="130" y="94">A × B</text>
</svg>

Returns the **Cartesian product** — every row from the first table combined with every row from the second.

```sql
SELECT sizes.name, colors.name
FROM sizes
CROSS JOIN colors

-- Alternative syntax
SELECT * FROM sizes, colors
```

- No `ON` clause needed
- Can produce **huge** result sets
- Useful for generating combinations

---

## LEFT ANTI JOIN

<svg width="100%" viewBox="0 0 260 100" role="img"><title>LEFT ANTI JOIN diagram</title><desc>Two overlapping circles with only the non-overlapping left part highlighted</desc>
  <circle cx="95" cy="50" r="42" fill="#185FA5" fill-opacity="0.65" stroke="#185FA5" stroke-width="1.5"/>
  <clipPath id="antiLA"><circle cx="95" cy="50" r="42"/></clipPath>
  <circle cx="165" cy="50" r="42" fill="#e8e8e8" fill-opacity="0.9" clip-path="url(#antiLA)"/>
  <circle cx="165" cy="50" r="42" fill="#B5D4F4" fill-opacity="0.15" stroke="#185FA5" stroke-width="1.5"/>
  <text font-family="sans-serif" font-size="11" font-weight="600" fill="#fff" text-anchor="middle" x="72" y="54">A</text>
  <text font-family="sans-serif" font-size="11" font-weight="600" fill="#042C53" text-anchor="middle" x="185" y="54">B</text>
</svg>

Returns rows from the left table with **no matching rows** in the right table. Find missing relationships.

```sql
SELECT customers.name
FROM customers
LEFT JOIN orders
ON customers.id = orders.customer_id
WHERE orders.id IS NULL
```

- Uses `LEFT JOIN` + `WHERE IS NULL`
- Example: customers with no orders
- Also called **LEFT EXCLUDING JOIN**

---

## RIGHT ANTI JOIN

<svg width="100%" viewBox="0 0 260 100" role="img"><title>RIGHT ANTI JOIN diagram</title><desc>Two overlapping circles with only the non-overlapping right part highlighted</desc>
  <circle cx="95" cy="50" r="42" fill="#B5D4F4" fill-opacity="0.15" stroke="#185FA5" stroke-width="1.5"/>
  <circle cx="165" cy="50" r="42" fill="#185FA5" fill-opacity="0.65" stroke="#185FA5" stroke-width="1.5"/>
  <clipPath id="antiRA"><circle cx="165" cy="50" r="42"/></clipPath>
  <circle cx="95" cy="50" r="42" fill="#e8e8e8" fill-opacity="0.9" clip-path="url(#antiRA)"/>
  <text font-family="sans-serif" font-size="11" font-weight="600" fill="#042C53" text-anchor="middle" x="72" y="54">A</text>
  <text font-family="sans-serif" font-size="11" font-weight="600" fill="#fff" text-anchor="middle" x="188" y="54">B</text>
</svg>

Returns rows from the right table with **no matching rows** in the left table. Find orphaned records.

```sql
SELECT orders.id
FROM orders
LEFT JOIN customers
ON orders.customer_id = customers.id
WHERE customers.id IS NULL
```

- Uses `RIGHT JOIN` + `WHERE IS NULL`
- Example: orders without customers
- Can be rewritten as a `LEFT ANTI JOIN`

---

## Quick Reference

| JOIN Type          | Returns                               | NULL for non-matches? | MySQL |
|--------------------|---------------------------------------|-----------------------|-------|
| `INNER JOIN`       | Matching rows from both tables        | No (excluded)         | ✅    |
| `LEFT JOIN`        | All left + matching right             | Right side            | ✅    |
| `RIGHT JOIN`       | All right + matching left             | Left side             | ✅    |
| `FULL OUTER JOIN`  | All rows from both tables             | Both sides            | ❌    |
| `CROSS JOIN`       | Every combination (Cartesian product) | N/A                   | ✅    |
| `LEFT ANTI JOIN`   | Left rows with no match in right      | N/A (filtered)        | ✅    |
| `RIGHT ANTI JOIN`  | Right rows with no match in left      | N/A (filtered)        | ✅    |