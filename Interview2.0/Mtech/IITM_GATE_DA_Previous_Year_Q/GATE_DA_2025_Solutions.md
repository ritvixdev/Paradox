# 📚 GATE DA 2025 — Previous Year Questions with Solutions
### Complete Analysis | Answers | Tricks | Concepts
> **Exam:** GATE Data Science & Artificial Intelligence 2025 (IIT Roorkee)
> **Prepared for:** IIT Madras WMT AI Entrance — Suvam Das

---

## ⚠️ YOUR EXAM FILTER
> 🎯 = **Directly in your WMT AI syllabus — MUST STUDY**
> ⚪ = NOT in your WMT syllabus (skip for now)

---

# GENERAL APTITUDE

---

## GA Q5 — Area Calculation
**Answer: C (Area increases by 10%)**

Width W increased by 10% → new width = 1.1W. Length L unchanged.
New area = L × 1.1W = 1.1 × (L×W) = **10% increase ✓**

Perimeter: 2(L + 1.1W) ≠ 10% increase (depends on L/W ratio). Not always 10%.

**Trick:** Area = L×W. If only W changes by 10%, Area changes by exactly 10% regardless of L.

---

## GA Q9 — Exponential Equations
**Answer: C (2³)**

3^(x²) = 27 × 9^x → 3^(x²) = 3³ × 3^(2x) → 3^(x²) = 3^(3+2x)

Equating exponents: x² = 3 + 2x → x² - 2x - 3 = 0 → (x-3)(x+1) = 0 → x = 3 or x = -1

Find 2^(x²) / (2^x)² = 2^(x²) / 2^(2x) = 2^(x²-2x)

For x=3: 2^(9-6) = 2³ = 8 ✓
For x=-1: 2^(1+2) = 2³ = 8 ✓ (same answer!)

**Answer: 2³ = 8 ✓**

---

# CORE DA — PROBABILITY & STATISTICS

---

## 🎯 Q1 — Law of Total Expectation
**Answer: C (E[X])** | **Topic: Conditional Expectation**

**Question:** E[E[X|Y]] = ?

**Solution:**
This is the **Law of Total Expectation** (also called the Tower Property):
```
E[E[X|Y]] = E[X]
```

Think of it this way: E[X|Y] is a function of Y. When you take expectation over Y, you get the unconditional mean of X.

**Answer: E[X] ✓**

**Law of Total Expectation:** E[X] = E[E[X|Y]]

This is fundamental. It says: "If you first compute the conditional average, then average those, you get the overall average."

**Analogy:** Average exam score = Average of (average score within each class). The class averages, when averaged together (weighted by class size), give overall average.

**Exam Trick:** Whenever you see E[E[X|Y]], the answer is always E[X]. No calculation needed!

---

## 🎯 Q4 — Taylor Series (sinh function)
**Answer: A (0)** | **Topic: Taylor Series, Derivatives**

**Question:** f(x) = (eˣ - e⁻ˣ)/2. Find f^(10)(0) (10th derivative at 0).

**Solution:**
f(x) = sinh(x) = x + x³/3! + x⁵/5! + x⁷/7! + ...

**The Taylor series of sinh(x) has ONLY ODD powers!**

The nth derivative at 0 equals n! × (coefficient of xⁿ in Taylor series).

For n=10 (even): coefficient of x¹⁰ = 0 (no even powers in sinh)

Therefore **f^(10)(0) = 0 ✓**

**Key Concept:** 
- sinh(x) = odd function → only odd powers in Taylor series → all even derivatives at 0 are ZERO
- cosh(x) = even function → only even powers → all odd derivatives at 0 are ZERO

**Quick Check:** sinh'(x) = cosh(x), sinh''(x) = sinh(x), sinh^(10)(x) = sinh(x) (period 2).
sinh^(10)(0) = sinh(0) = 0 ✓

---

## 🎯 Q5 — Logical Equivalence (Propositional Logic)
**Answer: A (S1 ≡ S3)** | **Topic: Logic**

**Question:** S1: p→q, S2: ¬p∧q, S3: ¬p∨q, S4: ¬p∨¬q. Which are equivalent?

**Solution:**
The key identity: **p→q ≡ ¬p∨q**

| p | q | S1: p→q | S2: ¬p∧q | S3: ¬p∨q | S4: ¬p∨¬q |
|---|---|---|---|---|---|
| T | T | T | F | T | F |
| T | F | F | F | F | T |
| F | T | T | T | T | T |
| F | F | T | F | T | T |

**S1 = S3 (same column) ✓**

**Answer: A ✓**

**Key Equivalences to Memorize:**
```
p → q  ≡  ¬p ∨ q     ← MOST IMPORTANT
¬(p∧q) ≡  ¬p ∨ ¬q   ← De Morgan
¬(p∨q) ≡  ¬p ∧ ¬q   ← De Morgan
p → q  ≡  ¬q → ¬p   ← Contrapositive
```

---

## 🎯 Q9 — Finding t from Median of CDF
**Answer: A (t = 2)** | **Topic: CDF, Median**

**Question:** CDF = 0 for x≤t, (x-t)/(4-t) for t≤x≤4, 1 for x≥4. Median = 3. Find t.

**Solution:**
**Median** = value m where F(m) = 0.5

```
F(3) = 0.5
(3-t)/(4-t) = 0.5
3-t = 0.5(4-t)
3-t = 2 - 0.5t
3-2 = t - 0.5t
1 = 0.5t
t = 2 ✓
```

**Answer: t = 2 ✓**

**Key Concept:** Median is the value where CDF = 0.5. Set F(median) = 0.5 and solve.

**Trick:** For continuous distributions, median m satisfies F(m) = 0.5. Always set up and solve the equation directly.

---

## 🎯 Q10 — Normal Distribution Parameters
**Answer: A (a=-2, b=1)** | **Topic: Normal Distribution, Moments**

**Question:** X = aZ + b where Z ~ N(0,1). Given E[X]=1, E[(X-E[X])Z]=-2, E[(X-E[X])²]=4.

**Solution:**
```
E[X] = a×E[Z] + b = 0 + b = b = 1 → b = 1

Var(X) = a²×Var(Z) = a² = 4 → a = ±2

E[(X-E[X])Z] = E[(aZ+b-b)Z] = E[aZ²] = a×E[Z²] = a×1 = a
Given this = -2 → a = -2 ✓
```

**Answer: a = -2, b = 1 ✓**

**Key Properties:**
- If X = aZ+b, then E[X] = b, Var(X) = a²
- E[Z²] = Var(Z) + (E[Z])² = 1 + 0 = 1 for standard normal

---

## 🎯 Q11 — Exponential Distribution: Finding λ
**Answer: A (ln 2)** | **Topic: Exponential Distribution**

**Question:** X ~ Exponential(λ). P(X ≥ 2) = 0.25. Find λ.

**Solution:**
For exponential: P(X > x) = e^(-λx)

```
P(X ≥ 2) = e^(-2λ) = 0.25 = 1/4
-2λ = ln(1/4) = -ln(4) = -2ln(2)
λ = ln(2) ✓
```

**Answer: ln 2 ✓**

**Exponential Survival Function:** P(X > t) = e^(-λt)

**Trick:** Convert P(X > x) = p to: -λx = ln(p) → λ = -ln(p)/x

---

## 🎯 Q21 — Bayes Theorem (Three Boxes)
**Answer: 0.25** | **Topic: Bayes' Theorem**

**Question:** Box1: 2B+1W, Box2: 1B+2W, Box3: 3B+3W. P(B1)=1/2, P(B2)=1/6, P(B3)=1/3. Given white drawn, P(from Box2)?

**Solution:**
```
P(W|B1) = 1/3, P(W|B2) = 2/3, P(W|B3) = 3/6 = 1/2

P(W) = P(W|B1)P(B1) + P(W|B2)P(B2) + P(W|B3)P(B3)
     = (1/3)(1/2) + (2/3)(1/6) + (1/2)(1/3)
     = 1/6 + 2/18 + 1/6
     = 3/18 + 2/18 + 3/18
     = 8/18 = 4/9

P(B2|W) = P(W|B2)P(B2) / P(W)
         = (2/3)(1/6) / (4/9)
         = (2/18) / (4/9)
         = (1/9) / (4/9)
         = 1/4 = 0.25 ✓
```

**Answer: 0.25 ✓**

---

## 🎯 Q22 — Limit Calculation
**Answer: 0.5** | **Topic: Calculus — Limits**

**Question:** lim(t→+∞) (√(t²+t) - t)

**Solution:**
**Rationalization trick:**
```
√(t²+t) - t = [√(t²+t) - t] × [√(t²+t) + t] / [√(t²+t) + t]
= (t²+t - t²) / (√(t²+t) + t)
= t / (√(t²+t) + t)

Divide numerator and denominator by t (t>0):
= 1 / (√(1+1/t) + 1)

As t→∞: 1/t→0, so:
= 1 / (√1 + 1) = 1/2 = 0.5 ✓
```

**Answer: 0.5 ✓**

**Technique:** For limits of form √(a²+b) - a as a→∞, ALWAYS rationalize by multiplying by conjugate.

**General Result:** lim(t→∞) (√(t²+ct) - t) = c/2

---

## 🎯 Q24 — Linear Regression (No Intercept)
**Answer: 0.286** | **Topic: Linear Regression**

**Question:** Data: {(-1,1), (2,-5), (3,5)}. Fit y=wx. Find optimal w.

**Solution:**
For y=wx (no intercept), least squares solution:
```
w = Σ(xᵢyᵢ) / Σ(xᵢ²)

Numerator: (-1)(1) + (2)(-5) + (3)(5) = -1 - 10 + 15 = 4
Denominator: (-1)² + 2² + 3² = 1 + 4 + 9 = 14

w = 4/14 = 2/7 ≈ 0.286 ✓
```

**Answer: 2/7 ≈ 0.286 ✓**

**Formulas for Linear Regression:**

With intercept (y = wx + b): Normal equations or formulas
Without intercept (y = wx): **w = (XᵀY)/(XᵀX) = Σxᵢyᵢ / Σxᵢ²**

**Trick:** For no-intercept regression, just compute: w = (dot product of x and y) / (squared norm of x).

---

## 🎯 Q25 — Naive Bayes Classification
**Answer: 0.40** | **Topic: Naive Bayes**

**Question:** P(y1)=1/3, P(y2)=2/3, P(x|y1)=3/4, P(x|y2)=1/4. Probability of misclassification?

**Solution:**
```
Posterior for y1: P(y1|x) ∝ P(x|y1)P(y1) = (3/4)(1/3) = 3/12 = 1/4
Posterior for y2: P(y2|x) ∝ P(x|y2)P(y2) = (1/4)(2/3) = 2/12 = 1/6

Compare: 1/4 = 3/12 > 1/6 = 2/12
→ Classify as y1 (higher posterior)

P(x) = 1/4 + 1/6 = 3/12 + 2/12 = 5/12

P(y1|x) = (1/4) / (5/12) = 3/5 = 0.6
P(y2|x) = (1/6) / (5/12) = 2/5 = 0.4

Classified as y1 → P(misclassification) = P(y2|x) = 0.4 ✓
```

**Answer: 0.40 ✓**

**Key Rule:** Naive Bayes classifies to class with highest posterior. Misclassification probability = sum of probabilities of other classes.

---

## 🎯 Q26 — Chi-Squared Variable Variance
**Answer: B (2)** | **Topic: Chi-Squared Distribution**

**Question:** Y = Z², Z = (X-μ)/σ where X ~ N(μ, σ²). Find Var(Y).

**Solution:**
Z ~ N(0,1), so Y = Z² ~ χ²(1)

For χ²(k): Mean = k, **Variance = 2k**

For χ²(1): **Var(Y) = 2 ✓**

**Answer: B ✓**

**Chi-Squared Properties:**
| Property | Formula |
|---|---|
| Distribution | Z₁²+Z₂²+...+Zₖ² where Zᵢ~N(0,1) iid |
| Mean | k |
| **Variance** | **2k** |
| Special case k=2 | Equivalent to Exp(1/2) with mean 2 |

---

## 🎯 Q29 — CDF Probability Calculation
**Answer: C (0.5)** | **Topic: CDF**

**Question:** F_X(x) = 0 for x≤-1, (1/4)(x+1)² for -1≤x≤1, 1 for x≥1. Find P(X²≤0.25).

**Solution:**
```
X² ≤ 0.25 ↔ |X| ≤ 0.5 ↔ -0.5 ≤ X ≤ 0.5

P(-0.5 ≤ X ≤ 0.5) = F(0.5) - F(-0.5)

F(0.5) = (1/4)(0.5+1)² = (1/4)(1.5)² = (1/4)(2.25) = 0.5625
F(-0.5) = (1/4)(-0.5+1)² = (1/4)(0.5)² = (1/4)(0.25) = 0.0625

P = 0.5625 - 0.0625 = 0.50 ✓
```

**Answer: 0.5 ✓**

**Trick:** P(X² ≤ a) = P(|X| ≤ √a) = P(-√a ≤ X ≤ √a) = F(√a) - F(-√a)

---

## 🎯 Q30 — CLT Application (Binomial)
**Answer: A (Φ(2)-Φ(-2))** | **Topic: Central Limit Theorem**

**Question:** Y = Σᵢ₌₁^300 Xᵢ where Xᵢ ~ Bernoulli(0.25). Find P(60 ≤ Y ≤ 90) using CLT.

**Solution:**
```
Y ~ Binomial(300, 0.25)
E[Y] = np = 300 × 0.25 = 75
Var[Y] = np(1-p) = 300 × 0.25 × 0.75 = 56.25
SD[Y] = √56.25 = 7.5

Standardize:
z₁ = (60 - 75)/7.5 = -15/7.5 = -2
z₂ = (90 - 75)/7.5 = 15/7.5 = 2

P(60 ≤ Y ≤ 90) ≈ P(-2 ≤ Z ≤ 2) = Φ(2) - Φ(-2) ✓
```

**Answer: A ✓**

**CLT Standard Template:**
```
1. Find μ = np, σ² = np(1-p) for Binomial
2. Standardize: Z = (Y - μ)/σ
3. Express as P(z₁ ≤ Z ≤ z₂) = Φ(z₂) - Φ(z₁)
```

**Trick:** Always compute mean and standard deviation first. The standardization always gives nice round numbers in GATE.

---

## 🎯 Q31 — Exponential + Floor Function
**Answer: A (q = 0.1)** | **Topic: Exponential Distribution**

**Question:** X ~ Exp(mean = 1/ln10). Y = ⌊X⌋. P(Y=ℓ) = qˡ(1-q). Find q.

**Solution:**
```
λ = 1/mean = ln(10)

P(Y = ℓ) = P(ℓ ≤ X < ℓ+1)
           = e^(-λℓ) - e^(-λ(ℓ+1))
           = e^(-λℓ)(1 - e^(-λ))

Let q = e^(-λ) = e^(-ln10) = 1/10 = 0.1

P(Y = ℓ) = (0.1)^ℓ × (1 - 0.1) = qˡ(1-q) ✓
```

**Answer: q = 0.1 ✓**

**Key Steps:**
1. Express P(Y=ℓ) as P(ℓ ≤ X < ℓ+1)
2. Use exponential CDF: P(X > t) = e^(-λt)
3. Factor to geometric form

---

## 🎯 Q35 — Complement for "At Least One"
**Answer: C (1-(5/6)^100)** | **Topic: Probability, Complement**

**Question:** 100 fair dice. P(at least one die shows 1)?

**Solution:**
Use complement: P(at least one 1) = 1 - P(no die shows 1)

```
P(one die ≠ 1) = 5/6
P(all 100 dice ≠ 1) = (5/6)^100    [independent]

P(at least one 1) = 1 - (5/6)^100 ✓
```

**Answer: C ✓**

**Golden Rule:** "At least one" = 1 - P(none). Always use complement!

---

## 🎯 Q44 — Sample Mean Properties (Estimation)
**Answer: A;C** | **Topic: Statistics, Estimation**

**Question:** p̂ = (1/n)ΣXᵢ where Xᵢ ~ Bernoulli(p). Which are correct?

**Solution:**

**A: E[p̂] = p** ✓
E[p̂] = (1/n)Σ E[Xᵢ] = (1/n)×n×p = p. This is called **unbiasedness**. ✓

**B: E[p̂] = p/n** — FALSE. As shown above, E[p̂] = p.

**C: As n increases, Var(p̂) decreases** ✓
Var(p̂) = Var((1/n)ΣXᵢ) = (1/n²)×n×p(1-p) = p(1-p)/n
As n increases, Var(p̂) = p(1-p)/n **decreases** ✓

**D: Var(p̂) does not depend on n** — FALSE. Var(p̂) = p(1-p)/n depends on n.

**Key Concepts:**
- Unbiasedness: E[estimator] = true parameter
- Consistency: as n→∞, estimator converges to true value
- Variance of sample mean = σ²/n (decreases with n)

---

## 🎯 Q51 — Binomial Expected Value
**Answer: 66.7** | **Topic: Binomial Distribution, Expectation**

**Question:** 5 white, 10 black balls. Draw 100 with replacement. E[number of black]?

**Solution:**
```
P(black on each draw) = 10/15 = 2/3

E[S100] = n × p = 100 × (2/3) = 200/3 ≈ 66.67 ✓
```

**Answer: 66.7 ✓**

**Key:** E[Binomial(n,p)] = np. Straightforward application.

---

# LINEAR ALGEBRA

---

## 🎯 Q2 — Gaussian Elimination Complexity
**Answer: B (O(n²))** | **Topic: Linear Algebra**

**Question:** Additions and multiplications in Gaussian elimination on n×n UPPER TRIANGULAR matrix?

**Solution:**
For an **upper triangular** matrix, back-substitution is O(n²):
- Solve for last variable: 1 division
- Solve for second-to-last: 1 mult + 1 sub + 1 div
- Total: O(n²) operations

For general matrix, full elimination is O(n³).

**Answer: O(n²) ✓** (upper triangular is already partially eliminated!)

**Key Facts:**
- Full Gaussian elimination: O(n³)
- Already upper triangular (back substitution only): O(n²)
- Matrix-vector multiplication: O(n²)
- Matrix-matrix multiplication: O(n³)

---

## 🎯 Q3 — Eigenvalue Property
**Answer: C (Infinitely many solutions)** | **Topic: Eigenvalues**

**Question:** Row sums of A ∈ Rⁿˣⁿ all equal 1. B = A³-2A²+A. Does Bx=0 have unique, no, or infinite solutions?

**Solution:**
**Key Insight:** If each row sums to 1, then A×1 = 1 (where 1 is all-ones vector).
→ **λ=1 is an eigenvalue of A**, with eigenvector 1.

Now compute B's eigenvalue for this eigenvector:
```
B = A³ - 2A² + A
B×1 = A³×1 - 2A²×1 + A×1
     = 1 - 2×1 + 1   [since A×1=1, A²×1=A×A×1=A×1=1, A³×1=1]
     = 0
```

So B×1 = 0 → **1 is a non-trivial solution to Bx=0!**

Since we have a non-zero solution, Bx=0 has **infinitely many solutions** ✓

**Answer: C ✓**

**Key Trick:** Row sum = 1 → eigenvalue 1 with eigenvector [1,1,...,1]ᵀ. This is a classic pattern!

---

## 🎯 Q15 — Orthonormal Basis
**Answer: B;D** | **Topic: Vector Spaces, Basis**

**Question:** Which are correct?
A. Rⁿ has unique set of orthonormal basis vectors
B. Rⁿ does NOT have unique set of orthonormal basis vectors
C. Linearly independent vectors are orthonormal
D. Orthonormal vectors are linearly independent

**Solution:**

**A** — FALSE. There are INFINITELY many orthonormal bases (any rotation of one gives another).

**B** — TRUE ✓. Any rotation of an orthonormal basis gives another valid one.

**C** — FALSE. Linearly independent ≠ orthogonal. Example: [1,0] and [1,1] are independent but not orthogonal.

**D** — TRUE ✓. If vectors are orthonormal, they are automatically linearly independent (orthogonality ensures no vector is a combination of others).

**Key Properties:**
```
Orthonormal → Linearly Independent (always)
Linearly Independent → Orthonormal? (NOT necessarily)
Orthonormal basis of Rⁿ → is NOT unique
```

---

## 🎯 Q18 — Eigenvalues of Identity + Outer Product
**Answer: A;B** | **Topic: Eigenvalues, Rank-1 Updates**

**Question:** A = Iₙ + xxᵀ where xᵀx = 1. Which are correct?

**Solution:**
**Finding eigenvalues of A:**

For any vector v ⊥ x (i.e., xᵀv = 0):
Av = Iₙv + xxᵀv = v + x(xᵀv) = v + 0 = v → eigenvalue **1**

For v = x:
Ax = x + xxᵀx = x + x(1) = 2x → eigenvalue **2**

So eigenvalues are: one **2** and (n-1) **1s**.

**A: Rank of A is n** ✓ — All eigenvalues > 0 → full rank → det ≠ 0 → rank = n. ✓

**B: A is invertible** ✓ — Since all eigenvalues > 0, det(A) > 0 → invertible. ✓

**C: 0 is an eigenvalue** — FALSE. Eigenvalues are 1 and 2, not 0.

**D: A⁻¹ has negative eigenvalue** — FALSE. A⁻¹ has eigenvalues 1 and 1/2 (reciprocals), both positive.

**Answer: A;B ✓**

**Sherman-Morrison Identity (bonus):** (A+uvᵀ)⁻¹ = A⁻¹ - (A⁻¹uvᵀA⁻¹)/(1+vᵀA⁻¹u)

---

## 🎯 Q27 — Matrix Property: A³=A
**Answer: D** | **Topic: Eigenvalues, Rank**

**Question:** A³ = A. Which is ALWAYS correct?

**Solution:**
From A³ = A → A(A²-I) = 0 → eigenvalues λ satisfy λ³ = λ → λ(λ²-1) = 0 → λ ∈ {-1, 0, 1}

**A: A is invertible** — FALSE. λ=0 might be an eigenvalue (e.g., A=0 satisfies A³=A).

**B: det(A) = 0** — FALSE. If A=I, then A³=I=A, and det(I)=1≠0.

**C: Trace = 1** — FALSE. If A=I₂, trace=2. If A=0, trace=0.

**D: A and A² have the same rank** ✓
Rank(A²) ≤ Rank(A). But A = A³ = A(A²), so columns of A are in column space of A² → Rank(A) ≤ Rank(A²). Therefore **Rank(A) = Rank(A²)** ✓

**Answer: D ✓**

**Trick:** When given a matrix polynomial equation, find what eigenvalues must satisfy. Then analyze each claim.

---

## 🎯 Q28 — Gram Matrix Invertibility
**Answer: A (A is invertible)** | **Topic: Linear Algebra**

**Question:** x₁,...,xₙ linearly independent in Rⁿ. A_ij = xᵢᵀxⱼ. Which is correct?

**Solution:**
Matrix A = XᵀX where X has xᵢ as rows (each xᵢ ∈ Rⁿ, n vectors in Rⁿ).

Since x₁,...,xₙ are linearly independent → X is invertible → Rank(X) = n.

For any non-zero z: zᵀAz = zᵀXᵀXz = ||Xz||² ≥ 0.

If zᵀAz = 0 → Xz = 0 → z = 0 (since X invertible). So A is **positive definite → invertible** ✓

**Answer: A ✓**

**Key Result:** If columns of X are linearly independent, then XᵀX is positive definite (hence invertible).

---

## 🎯 Q40 — Projection Matrix from Orthonormal Vectors
**Answer: A;B** | **Topic: SVD, Projection, Eigenvalues**

**Question:** x₁,...,x₅ orthonormal in R¹⁰. A = x₁x₁ᵀ+...+x₅x₅ᵀ. Which correct?

**Solution:**
A is a projection matrix onto the subspace spanned by x₁,...,x₅.

**A: Singular values = eigenvalues** ✓ — Since A is symmetric and positive semidefinite, its singular values equal its eigenvalues (for PSD matrices, all eigenvalues ≥ 0 and singular values = absolute values of eigenvalues = eigenvalues). ✓

**B: Singular values are 0 or 1** ✓ — A is a projection matrix (Aᵀ=A and A²=A), so eigenvalues are 0 or 1, hence singular values are 0 or 1. ✓

**C: det(A) = 1** — FALSE. det(A) = 0 (since rank=5 < 10, not full rank).

**D: A is invertible** — FALSE. Same reason, rank=5 < 10.

**Answer: A;B ✓**

---

## 🎯 Q41 — Convex Function Properties
**Answer: B;C;D** | **Topic: Optimization, Convexity**

**Question:** f''(x) > 0 for all x. Which are ALWAYS correct?

**Solution:**

f''(x) > 0 means f is **strictly convex** everywhere.

**A: f has a local minimum** — NOT always. f(x)=eˣ has f''(x)=eˣ>0 but no local minimum (f decreases as x→-∞). ✗

**B: No two distinct points where f'(x)=f'(y)=0** ✓ — For strictly convex f, f' is strictly increasing. So f'(x)=0 can occur at most once. Cannot have two distinct zeros of f'. ✓

**C: At most one global minimum** ✓ — Strictly convex → any local min is global, and can have at most one. ✓

**D: At most one local minimum** ✓ — Strictly convex functions have at most one local minimum. ✓

**Answer: B;C;D ✓**

---

## 🎯 Q42 — Orthogonal Matrix = Isometry
**Answer: A;D** | **Topic: Orthogonal Matrices**

**Question:** A satisfies ||Ax||₂ = ||x||₂ for all x. Which are ALWAYS correct?

**Solution:**
||Ax||₂ = ||x||₂ for all x → A preserves lengths → **A is orthogonal** (Aᵀ=A⁻¹).

**A: A must be orthogonal** ✓ — By definition, length-preserving linear maps are orthogonal. ✓

**B: A=I is only solution** — FALSE. Any rotation/reflection matrix works.

**C: Eigenvalues are ±1** — NOT always. Complex eigenvalues of orthogonal matrices have magnitude 1 (can be complex). For real matrices, eigenvalues can be complex conjugate pairs with |λ|=1.

**D: A has full rank** ✓ — Orthogonal matrices are invertible → full rank. ✓

**Answer: A;D ✓**

---

# MACHINE LEARNING

---

## 🎯 Q12 — Perceptron Update Rule
**Answer: A** | **Topic: Perceptron, Linear Classifier**

**Question:** Classifier f(x) = sign(wᵀx+b). Update: w_new = w_old + yₙxₙ when wrong. Given (xₙ,+1) and f(xₙ;w_old,b_old)<0. Then?

**Solution:**
```
f_new(xₙ) = w_new^T × xₙ + b_new
           = (w_old + xₙ)^T × xₙ + (b_old + 1)   [since y_n = +1]
           = w_old^T × xₙ + xₙ^T × xₙ + b_old + 1
           = f_old(xₙ) + ||xₙ||² + 1

Since ||xₙ||² + 1 > 0:
f_new(xₙ) > f_old(xₙ) ✓
```

**Answer: A ✓** (f increases, moving toward correct classification)

**Key Concept:** The perceptron update moves the decision boundary in the direction that corrects the error. After update, the score for the misclassified example INCREASES.

---

## 🎯 Q20 — Hierarchical Clustering Linkage
**Answer: B;D** | **Topic: Hierarchical Clustering**

**Question:** DIS-1 = max distance, DIS-2 = min distance between clusters. Single/Complete linkage?

**Solution:**
- **Single linkage:** Merges clusters with the **MINIMUM** distance between any pair of points → uses **DIS-2** ✓
- **Complete linkage:** Merges clusters with the **MAXIMUM** distance between any pair of points → uses **DIS-1** ✓

**Answer: B;D ✓** (B: Single uses DIS-2, D: Complete uses DIS-1)

**Linkage Methods Summary:**
| Method | Distance Used | Effect |
|---|---|---|
| **Single linkage** | **min** between clusters | Chaining; elongated clusters |
| **Complete linkage** | **max** between clusters | Compact, spherical clusters |
| Average linkage | average of all pairs | Compromise |
| Ward | minimize variance increase | Most similar to k-means |

**Memory Trick:** "Single = Smallest, Complete = Comprehensive (maximum)"

---

## 🎯 Q43 — SVM Hard Margin
**Answer: B;C** | **Topic: SVM**

**Question:** Class-1: {(2,0),(0,2),(2,2)}, Class-2: {(0,0)}. Hard-margin SVM. Which correct?

**Solution:**
The decision boundary maximizes margin between classes.

The optimal hyperplane for this data: x₁+x₂=1 (you can verify: all class-1 points satisfy x₁+x₂≥2, class-2 satisfies x₁+x₂=0).

Actually, decision boundary: w=[1,1], b=-1: wᵀx+b = x₁+x₂-1

Support vectors = closest points to boundary:
- From class-1: (2,0) → 2+0-1=1 ✓ and (0,2) → 0+2-1=1 ✓
- From class-2: (0,0) → 0+0-1=-1 ✓

All 3 listed points are support vectors! → **3 support vectors ✓ (B)**

Margin = 2/||w|| = 2/√(1²+1²) = 2/√2 = **√2 ✓ (C)**

**Answer: B;C ✓**

---

## 🎯 Q45 — Distance-Based Classifier Analysis
**Answer: B;C** | **Topic: Linear Classifiers, Geometry**

**Question:** f(x) = ||μ_red - x||² - ||μ_green - x||². Is f linear?

**Solution:**
Expand:
```
f(x) = (μ_red-x)ᵀ(μ_red-x) - (μ_green-x)ᵀ(μ_green-x)
= ||μ_red||² - 2μ_red^T×x + ||x||² - ||μ_green||² + 2μ_green^T×x - ||x||²
= ||μ_red||² - ||μ_green||² + 2(μ_green - μ_red)^T × x
```

The ||x||² terms cancel! → **f(x) is LINEAR in x ✓ (B)**

f(x) = wᵀx + b where w = 2(μ_green - μ_red) and b = ||μ_red||² - ||μ_green||² ✓ **(C)**

**A:** x=0 is green if f(0) ≥ 0 → ||μ_red||² - ||μ_green||² ≥ 0 → ||μ_red|| ≥ ||μ_green||. NOT if ||μ_red|| < ||μ_green||. Statement A says "assigned green if ||μ_red|| < ||μ_green||" → we need to check: if ||μ_red||<||μ_green||, f(0) = ||μ_red||²-||μ_green||² < 0 → label red (f<0 means red). So A is WRONG.

**D:** f is NOT quadratic — the x² terms canceled! → FALSE.

**Answer: B;C ✓**

**Key Trick:** When computing ||μ-x||² - ||ν-x||², the ||x||² terms ALWAYS cancel → result is LINEAR in x!

---

# CALCULUS & OPTIMIZATION

---

## 🎯 Q39 — Finding Extrema on Interval
**Answer: C;D** | **Topic: Calculus, Optimization**

**Question:** f(x) = x³/3 + 7x²/2 + 10x + 133/2 on [-8,0]. Which correct?

**Solution:**
```
f'(x) = x² + 7x + 10 = (x+2)(x+5) = 0
Critical points: x = -2 and x = -5

f''(x) = 2x + 7
f''(-2) = -4+7 = 3 > 0 → local min at x=-2
f''(-5) = -10+7 = -3 < 0 → local max at x=-5
```

**Evaluate at critical points and boundaries:**
```
f(-8) = -512/3 + 448/2 - 80 + 133/2 = -512/3 + 224 - 80 + 66.5 = -170.67 + 210.5 = 39.83
f(-5) = -125/3 + 175/2 - 50 + 133/2 = -41.67 + 87.5 - 50 + 66.5 = 62.33
f(-2) = -8/3 + 14 - 20 + 66.5 = -2.67 + 60.5 = 57.83
f(0)  = 0 + 0 + 0 + 133/2 = 66.5
```

**A:** Maximum at x=-5? No, maximum is at x=0 (f(0)=66.5=133/2 is largest). **FALSE**

**B:** Minimum at x=-2? Minimum is at x=-8 (f(-8)≈39.83 < f(-2)≈57.83). **FALSE** — global min is at boundary x=-8.

**C:** Maximum value is 133/2 = f(0) ✓. **TRUE**

**D:** Minimum of f'(x): f'(x) = x² + 7x + 10. Minimum of a quadratic ax²+bx+c (a>0) at x=-b/2a = -7/2 = **-7/2** ✓. **TRUE**

**Answer: C;D ✓**

---

## 🎯 Q41 — Strictly Convex Function
**Answer: B;C;D** | Covered above in Linear Algebra section.

---

## 🎯 Q49 — Lipschitz Condition and Differentiability
**Answer: 0** | **Topic: Calculus**

**Question:** |f(x)-f(y)| ≤ (x-y)² for all x,y. Find f(1)-f(0).

**Solution:**
The condition |f(x)-f(y)| ≤ (x-y)² tells us f is **uniformly Lipschitz with any Lipschitz constant** (since (x-y)² = |x-y|×|x-y| → as |x-y|→0, the bound → 0 faster than linearly).

**Check the derivative:**
```
|f'(x)| = |lim(h→0) [f(x+h)-f(x)]/h|
         ≤ lim(h→0) h²/|h| = lim(h→0) |h| = 0
```

So f'(x) = 0 everywhere → f is CONSTANT → f(1) - f(0) = **0 ✓**

**Answer: 0 ✓**

**Key Insight:** A function satisfying |f(x)-f(y)| ≤ C|x-y|² is differentiable everywhere with derivative = 0, hence constant.

---

## 🎯 Q50 — PCA Variance
**Answer: 100** | **Topic: PCA**

**Question:** n observations in R¹⁰⁰, mean=0. Eigenvalues λᵢ=100^(2-i). u = direction of max variance. Find (1/n)Σ(uᵀx^(i))².

**Solution:**
The quantity (1/n)Σ(uᵀx^(i))² is the **variance of the projection onto u**.

The direction of maximum variance u = first principal component = eigenvector of covariance matrix with LARGEST eigenvalue.

The variance along this direction = **largest eigenvalue** = λ₁ = 100^(2-1) = 100^1 = **100 ✓**

**Answer: 100 ✓**

**Key PCA Result:** The variance of data projected onto the k-th principal component = k-th largest eigenvalue of the covariance matrix.

---

# 📊 2025 QUESTION SUMMARY FOR WMT EXAM

## Must-Study Questions (Your Syllabus)

| Category | Questions | Key Concept |
|---|---|---|
| Probability | Q1, Q9, Q10, Q11, Q21, Q25, Q26, Q29, Q30, Q31, Q35, Q44, Q51 | Core probability rules |
| Linear Algebra | Q2, Q3, Q15, Q18, Q27, Q28, Q40, Q41, Q42 | Eigenvalues, PCA, projections |
| ML | Q12, Q20, Q38, Q43, Q44, Q45 | Classification, clustering |
| Calculus | Q4, Q5, Q22, Q39, Q49, Q50 | Derivatives, limits |

---

# 🔑 KEY FORMULAS FROM 2025 PAPER

```
PROBABILITY:
Law of Total Expectation: E[X] = E[E[X|Y]]
Bayes: P(Bᵢ|E) = P(E|Bᵢ)P(Bᵢ) / ΣP(E|Bⱼ)P(Bⱼ)
Complement: P(at least one) = 1 - P(none)

EXPONENTIAL:
P(X > t) = e^(-λt)
Find λ: e^(-λt) = p → λ = -ln(p)/t

CLT FOR BINOMIAL:
μ = np, σ² = np(1-p)
P(a ≤ Y ≤ b) ≈ Φ((b-μ)/σ) - Φ((a-μ)/σ)

LINEAR REGRESSION (no intercept):
w = Σ(xᵢyᵢ) / Σ(xᵢ²)

NAIVE BAYES:
Classify to class with max P(class)×Π P(xᵢ|class)

SVM:
Margin = 2/||w||
Support vectors = points on margin boundary

PCA:
Variance along kth PC = kth largest eigenvalue
```

---

*GATE DA 2025 | IIT Roorkee | Solutions for Suvam Das | WMT AI 2026*
