# 📗 TOPIC 2: Linear Algebra
### IIT Madras WMT AI Entrance — Complete Notes
> 🔴 **HIGHEST PRIORITY** | ~15% of exam marks
> 📅 Study Days: 8–14

---

## 🧠 Why Linear Algebra Matters for AI
EVERY AI operation involves matrices. An image is a matrix of pixels. A neural network is matrix multiplications. PCA, SVD — all linear algebra. This isn't abstract math — it's the engine running all of AI.

---

# PART 1: VECTORS

## 1.1 What is a Vector?
A vector is an ordered list of numbers — it has magnitude AND direction.
```
v = [3, 4]       ← 2D vector
w = [1, 2, -3]   ← 3D vector
u = [x₁, x₂, ..., xₙ]  ← n-dimensional vector (column vector usually)
```
In AI: a data point with n features = an n-dimensional vector.

## 1.2 Vector Operations

### Addition:
```
[1, 2, 3] + [4, 5, 6] = [5, 7, 9]   ← add element by element
```

### Scalar Multiplication:
```
3 × [1, 2, 3] = [3, 6, 9]   ← multiply each element
```

### Dot Product (Inner Product): ⭐
```
a · b = a₁b₁ + a₂b₂ + ... + aₙbₙ

[1, 2, 3] · [4, 5, 6] = 1×4 + 2×5 + 3×6 = 4+10+18 = 32
```
**Geometric meaning:** a·b = |a| × |b| × cos(θ)

**Key results:**
- If a·b = 0: vectors are **perpendicular (orthogonal)**
- If a·b = |a|×|b|: vectors are parallel (θ=0°)

### Magnitude (Length):
```
|v| = √(v₁² + v₂² + ... + vₙ²)
|[3, 4]| = √(9 + 16) = √25 = 5
```

### Unit Vector:
```
v̂ = v / |v|     ← vector of length 1 in direction of v
```

### Distance Between Vectors (Euclidean):
```
d(a, b) = |a - b| = √Σ(aᵢ - bᵢ)²
```
This is exactly what kNN uses to find nearest neighbours!

---

# PART 2: VECTOR SPACES AND SUBSPACES

## 2.1 Vector Space
A set of vectors where addition and scalar multiplication are defined and stay within the set.

**Examples:**
- All 2D vectors (ℝ²): [x, y] for any real x, y
- All 3D vectors (ℝ³)
- Solutions to Ax = 0 form a vector space (null space!)

## 2.2 Linear Combination
A linear combination of vectors v₁, v₂, ..., vₖ is:
```
c₁v₁ + c₂v₂ + ... + cₖvₖ   where c₁, c₂, ..., cₖ are scalars
```

## 2.3 Span
The span of a set of vectors = all possible linear combinations of those vectors.
Think of it as: "All places you can reach using these vectors as building blocks."

## 2.4 Linear Independence ⭐⭐ (Very important!)

Vectors v₁, v₂, ..., vₖ are **linearly independent** if:
```
c₁v₁ + c₂v₂ + ... + cₖvₖ = 0   ONLY when c₁ = c₂ = ... = cₖ = 0
```
In plain English: **No vector can be written as a combination of the others.**

**Linearly DEPENDENT:** At least one vector is redundant (can be written as combo of others).

**Example:**
```
v₁ = [1, 0], v₂ = [0, 1], v₃ = [2, 3]
v₃ = 2v₁ + 3v₂  → v₃ is redundant → These are LINEARLY DEPENDENT

v₁ = [1, 0], v₂ = [0, 1] → No way to write one from the other → LINEARLY INDEPENDENT
```

**Quick test for 2 vectors:** Two vectors are dependent if one is a scalar multiple of the other.

**In matrix form:** Columns of matrix A are linearly independent ↔ Ax = 0 has ONLY the zero solution.

## 2.5 Basis
A basis for a vector space is:
1. A set of linearly independent vectors
2. That span the entire space

**The standard basis for ℝ²:** {[1,0], [0,1]}
**The standard basis for ℝ³:** {[1,0,0], [0,1,0], [0,0,1]}

**Dimension** = number of vectors in a basis.

## 2.6 Subspace
A subset of a vector space that is itself a vector space.

Must satisfy:
1. Contains zero vector
2. Closed under addition (add any two vectors → get another in subspace)
3. Closed under scalar multiplication

**Important subspaces of matrix A:**
- **Column space (range):** All linear combinations of columns of A
- **Null space (kernel):** All x where Ax = 0
- **Row space:** All linear combinations of rows of A

---

# PART 3: MATRICES

## 3.1 Matrix Basics
```
A = [1  2  3]   ← 2×3 matrix (2 rows, 3 columns)
    [4  5  6]

Element: aᵢⱼ = element in row i, column j
a₁₂ = 2 (row 1, column 2)
```

## 3.2 Matrix Operations

### Transpose (Aᵀ):
Flip rows and columns:
```
A = [1  2]    Aᵀ = [1  3]
    [3  4]         [2  4]
```
Properties:
- (Aᵀ)ᵀ = A
- (AB)ᵀ = BᵀAᵀ  ← ORDER REVERSES!
- (A+B)ᵀ = Aᵀ + Bᵀ

### Matrix Multiplication:
A is m×n, B is n×p → Result is m×p
```
(AB)ᵢⱼ = row i of A · column j of B = Σ aᵢₖ × bₖⱼ
```
**⚠️ NOT commutative:** AB ≠ BA in general!

**Example:**
```
[1  2] × [5  6] = [1×5+2×7  1×6+2×8] = [19  22]
[3  4]   [7  8]   [3×5+4×7  3×6+4×8]   [43  50]
```

## 3.3 Special Matrices

### Identity Matrix (I):
```
I₂ = [1  0]    I₃ = [1  0  0]
     [0  1]         [0  1  0]
                    [0  0  1]
```
AI = IA = A (multiplicative identity)

### Zero Matrix:
All elements are 0. A + 0 = A.

### Diagonal Matrix:
Non-zero elements only on main diagonal.
```
D = [3  0  0]
    [0  5  0]
    [0  0  2]
```
Easy to work with! D^n just raises diagonal elements to power n.

### Symmetric Matrix: ⭐
A = Aᵀ (symmetric across main diagonal)
```
[1  2  3]
[2  5  6]    ← A = Aᵀ
[3  6  9]
```
All eigenvalues of symmetric matrix are REAL.

### Orthogonal Matrix: ⭐ (exam favorite)
QᵀQ = QQᵀ = I  →  Qᵀ = Q⁻¹
```
Properties:
- det(Q) = +1 or -1
- Columns (and rows) are orthonormal (unit length, perpendicular to each other)
- Preserves lengths and angles (rotation/reflection matrices)
```

### Idempotent Matrix:
A² = A (applying twice = applying once)
```
Example: Projection matrix P = A(AᵀA)⁻¹Aᵀ is idempotent
P² = P
```

### Projection Matrix: ⭐
Projects vectors onto a subspace.
```
P = A(AᵀA)⁻¹Aᵀ
```
Properties:
- P² = P (idempotent)
- Pᵀ = P (symmetric)
- Eigenvalues are 0 or 1 only

---

# PART 4: DETERMINANT ⭐

## 4.1 What is Determinant?
A single number that tells you about a matrix's properties.
- **det(A) ≠ 0:** Matrix is invertible (non-singular)
- **det(A) = 0:** Matrix is singular (not invertible)
- **|det(A)|:** Scaling factor for volumes

## 4.2 Calculating Determinants

### 2×2:
```
det [a  b] = ad - bc
    [c  d]

det [3  2] = 3×4 - 2×1 = 12 - 2 = 10
    [1  4]
```

### 3×3 (Cofactor expansion along first row):
```
det [a  b  c]
    [d  e  f] = a×det[e f; h i] - b×det[d f; g i] + c×det[d e; g h]
    [g  h  i]
```

**Sarrus Rule (for 3×3 only):**
Write first two columns again, multiply diagonals:
- Add: top-left to bottom-right diagonals
- Subtract: top-right to bottom-left diagonals

## 4.3 Key Properties of Determinants (EXAM FAVORITES!)
```
det(AB) = det(A) × det(B)
det(Aᵀ) = det(A)
det(A⁻¹) = 1/det(A)
det(cA) = cⁿ × det(A)   for n×n matrix
If two rows are equal → det = 0
If one row is all zeros → det = 0
Swapping rows changes sign of det
Adding multiple of one row to another → det unchanged
```

## 4.4 Trace of a Matrix
```
tr(A) = sum of diagonal elements = a₁₁ + a₂₂ + ... + aₙₙ
```
Properties:
- tr(AB) = tr(BA)
- tr(A) = sum of eigenvalues
- det(A) = product of eigenvalues

---

# PART 5: RANK AND NULLITY ⭐⭐

## 5.1 Rank
```
Rank = number of linearly independent rows (or columns)
     = dimension of column space (= dimension of row space)
```
**How to find:** Row reduce to echelon form → count non-zero rows.

**Properties:**
- Rank(A) = Rank(Aᵀ)
- Rank(A) ≤ min(m, n) for m×n matrix
- Rank = n (full column rank) → columns are independent
- Rank = m (full row rank) → rows are independent

## 5.2 Nullity
```
Nullity = dimension of null space = n - Rank(A)
```
The null space = all x such that Ax = 0.

## 5.3 Rank-Nullity Theorem ⭐ (Very common in exams!)
```
Rank(A) + Nullity(A) = n    (n = number of columns)
```

**Example:**
Matrix A is 3×5.
Rank(A) = 2.
Nullity = 5 - 2 = 3.

## ✅ Exam Example:
**Q:** A 4×5 matrix A has rank 3. How many solutions does Ax = 0 have?
```
Nullity = 5 - 3 = 2
Null space has dimension 2 → INFINITE solutions (any linear combo of 2 basis vectors)
```

---

# PART 6: SYSTEMS OF LINEAR EQUATIONS ⭐⭐

## 6.1 Three Cases
Ax = b:
1. **Unique solution:** Rank(A) = Rank([A|b]) = n (consistent, full rank)
2. **Infinite solutions:** Rank(A) = Rank([A|b]) < n (consistent, not full rank)
3. **No solution:** Rank(A) ≠ Rank([A|b]) (inconsistent)

**[A|b]** = augmented matrix (A with column b appended)

## 6.2 Gaussian Elimination

**Goal:** Convert to row echelon form using row operations:
1. Swap two rows
2. Multiply a row by non-zero scalar
3. Add multiple of one row to another

**Example:**
```
x + 2y = 5
2x + 3y = 8

Augmented: [1  2 | 5]
           [2  3 | 8]

R2 = R2 - 2×R1:
[1  2 | 5]
[0 -1 |-2]

From R2: -y = -2 → y = 2
From R1: x + 4 = 5 → x = 1
Solution: x=1, y=2
```

---

# PART 7: EIGENVALUES AND EIGENVECTORS ⭐⭐⭐

## 7.1 The Big Idea
For a square matrix A, if:
```
Av = λv
```
Then v is an **eigenvector** and λ is its **eigenvalue**.
**Meaning:** When you apply matrix A to vector v, v only SCALES (by λ), doesn't rotate!

## 7.2 Finding Eigenvalues

**Characteristic equation:**
```
det(A - λI) = 0
```
Solve this polynomial for λ.

**Example (2×2):**
```
A = [4  1]
    [2  3]

A - λI = [4-λ   1 ]
         [2    3-λ]

det = (4-λ)(3-λ) - 2 = λ² - 7λ + 12 - 2 = λ² - 7λ + 10 = 0

(λ - 5)(λ - 2) = 0  →  λ₁ = 5, λ₂ = 2
```

## 7.3 Finding Eigenvectors

For each eigenvalue, solve (A - λI)v = 0:

**For λ₁ = 5:**
```
(A - 5I)v = [−1   1] [v₁] = [0]
            [ 2  −2] [v₂]   [0]

−v₁ + v₂ = 0 → v₂ = v₁
Eigenvector: v₁ = [1, 1] (any scalar multiple works)
```

## 7.4 Key Properties of Eigenvalues

```
- tr(A) = λ₁ + λ₂ + ... + λₙ  (trace = sum of eigenvalues)
- det(A) = λ₁ × λ₂ × ... × λₙ  (det = product of eigenvalues)
- If A is symmetric → all eigenvalues are REAL
- If A is positive definite → all eigenvalues > 0
- If rank < n → at least one eigenvalue = 0
- Eigenvalues of Aᵀ = Eigenvalues of A
- Eigenvalues of A⁻¹ = 1/λᵢ
- Eigenvalues of A^k = λᵢ^k
```

## 7.5 Eigendecomposition
If A has n linearly independent eigenvectors:
```
A = PDP⁻¹
```
Where D is diagonal matrix of eigenvalues, P has eigenvectors as columns.

**Power of matrix:** A^k = PD^kP⁻¹ (easy to compute since D^k just raises each diagonal element to k)

## 7.6 Positive Definite Matrices ⭐
A symmetric matrix A is positive definite if:
```
xᵀAx > 0 for all non-zero x
```
Equivalent conditions:
- All eigenvalues > 0
- All leading principal minors > 0 (Sylvester's criterion)
- Used in: optimization (A is positive definite → minimum, not maximum or saddle)

---

# PART 8: PROJECTIONS ⭐

## 8.1 Projection onto a Vector
Project vector b onto vector a:
```
proj_a(b) = (a·b / |a|²) × a = (aᵀb / aᵀa) × a
```

**Example:** Project b=[3,4] onto a=[1,0]:
```
proj = (1×3 + 0×4)/(1+0) × [1,0] = 3 × [1,0] = [3, 0]
```

## 8.2 Projection Matrix
To project onto subspace spanned by columns of A:
```
P = A(AᵀA)⁻¹Aᵀ
```
Then projection of any vector b = Pb.

**Why important:** Least squares regression finds the projection of y onto column space of X!

## 8.3 Gram-Schmidt Process
Convert any set of linearly independent vectors into orthonormal basis:
1. Normalize first vector
2. Subtract projection of each subsequent vector onto already-processed vectors
3. Normalize

---

# PART 9: MATRIX DECOMPOSITIONS ⭐⭐

## 9.1 LU Decomposition
Decompose matrix into Lower triangular × Upper triangular:
```
A = LU
```
**Use:** Efficient solution of Ax = b (solve Ly = b, then Ux = y)
**When does it exist?** When Gaussian elimination can proceed without row swaps.

```
L = lower triangular with 1s on diagonal
U = upper triangular

[2  1  1]   [1   0   0] [2   1   1]
[4  3  3] = [2   1   0] [0   1   1]
[8  7  9]   [4   3   1] [0   0   2]
```

## 9.2 SVD — Singular Value Decomposition ⭐⭐⭐ (Very important for ML!)

Any matrix A (even non-square!) can be decomposed as:
```
A = UΣVᵀ
```
Where:
- **U** = m×m orthogonal matrix (left singular vectors)
- **Σ** = m×n diagonal matrix with singular values σ₁ ≥ σ₂ ≥ ... ≥ 0
- **V** = n×n orthogonal matrix (right singular vectors)

**Singular values = √(eigenvalues of AᵀA)**

### Why SVD is used everywhere in AI:
- **PCA:** SVD of the data matrix → principal components
- **Recommendation systems:** Netflix, Amazon use SVD for matrix factorization
- **Image compression:** Keep only top k singular values
- **Rank determination:** Number of non-zero singular values = Rank(A)
- **Pseudo-inverse:** A⁺ = VΣ⁺Uᵀ

### Truncated SVD (for compression):
Keep only top k singular values → low-rank approximation
Best rank-k approximation is given by the first k terms of SVD!

---

# PART 10: QUADRATIC FORMS

```
Q(x) = xᵀAx = Σᵢ Σⱼ aᵢⱼ xᵢ xⱼ
```

For symmetric matrix A:
- **Positive definite:** xᵀAx > 0 for all x ≠ 0 → all eigenvalues > 0 → unique minimum
- **Negative definite:** xᵀAx < 0 for all x ≠ 0 → all eigenvalues < 0 → unique maximum
- **Indefinite:** Some eigenvalues positive, some negative → saddle point
- **Positive semidefinite:** xᵀAx ≥ 0 → all eigenvalues ≥ 0

**Why in AI:** Loss functions are quadratic forms! The nature of eigenvalues tells you whether you've found a min/max/saddle.

---

# 🔑 QUICK REFERENCE — All Key Facts

```
VECTORS:
|v| = √Σvᵢ²
a·b = Σaᵢbᵢ = |a||b|cos θ
a·b = 0 ↔ perpendicular

DETERMINANTS:
det[a b; c d] = ad - bc
det(AB) = det(A)det(B)
det(cA) = cⁿ det(A)

RANK:
Rank + Nullity = n (columns)
Rank(A) = Rank(Aᵀ)

EIGENVALUES:
det(A - λI) = 0
tr(A) = Σλᵢ
det(A) = Πλᵢ

DECOMPOSITIONS:
A = LU  (Gaussian elimination)
A = UΣVᵀ  (SVD — works for any matrix)
A = PDP⁻¹  (eigendecomposition — square matrix)

SPECIAL:
Orthogonal Q: QᵀQ = I, Qᵀ = Q⁻¹
Symmetric: A = Aᵀ, real eigenvalues
Idempotent: P² = P
Positive definite: all eigenvalues > 0
```

---

# 🎯 EXAM TIPS & TRICKS FOR LINEAR ALGEBRA

1. **For eigenvalues of 2×2:** Use trace and det as shortcuts
   - λ₁ + λ₂ = tr(A)
   - λ₁ × λ₂ = det(A)

2. **det = 0 ↔ singular ↔ rank < n ↔ Ax=0 has non-trivial solutions**

3. **For rank:** Row reduce! Count pivot rows.

4. **Orthogonal matrix checklist:**
   - Columns are unit vectors? ✓
   - Columns are perpendicular? ✓
   - Then det = ±1

5. **SVD singular values:** σᵢ = √λᵢ where λᵢ are eigenvalues of AᵀA

6. **Projection:** If P is projection matrix:
   - Pb = projected vector
   - b - Pb = error vector (perpendicular to subspace)

7. **Idempotent trick:** P² = P → eigenvalues of P are only 0 or 1

8. **For system Ax=b:**
   - Compute Rank(A) and Rank([A|b])
   - If Rank(A) = Rank([A|b]) = n: unique solution
   - If Rank(A) = Rank([A|b]) < n: infinitely many solutions
   - If Rank(A) < Rank([A|b]): no solution

9. **Positive definite shortcut:** Check if all eigenvalues > 0 OR check leading principal minors

---

# 📝 PRACTICE QUESTIONS

**Q1.** A = [2 1; 1 2]. Find eigenvalues.
> det([2-λ, 1; 1, 2-λ]) = (2-λ)² - 1 = λ² - 4λ + 3 = (λ-3)(λ-1) = 0
> **λ = 3, 1**. Check: tr(A)=4=3+1 ✓, det(A)=3=3×1 ✓

**Q2.** Is A = [1 2; 2 4] invertible?
> det(A) = 1×4 - 2×2 = 0 → **Not invertible**. Also rank=1 (row 2 = 2× row 1).

**Q3.** A is 4×6 with rank 3. Find nullity.
> Nullity = 6 - 3 = **3**

**Q4.** If A is orthogonal and det(A)=1, what type of transformation is it?
> **Rotation** (preserves orientation). det=-1 would be reflection.

**Q5.** Matrix A has eigenvalues 2, 0, -1. Is A invertible?
> One eigenvalue = 0 → det(A) = 0 → **A is NOT invertible**

**Q6.** For which value of k does the system have no solution?
```
x + 2y = 3
2x + ky = 5
```
> Augmented matrix: [1 2|3; 2 k|5]
> Rank(A) ≠ Rank([A|b]) when R2-2R1 gives [0, k-4|5-6] = [0, k-4|-1]
> If k=4: [0, 0|-1] → 0 = -1 → No solution! **k = 4**

---

> 📌 **Next: Read `03_Calculus_Optimization.md`**
