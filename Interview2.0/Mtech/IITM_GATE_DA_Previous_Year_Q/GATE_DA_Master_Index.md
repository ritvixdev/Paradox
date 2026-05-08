# 🎯 GATE DA PYQ Master Index — Study Guide for WMT AI Entrance
### Suvam Das | Application: W26OTHAI00797 | IIT Madras M.Tech AI 2026

---

## 📁 Files in This Collection

| File | Content | Pages |
|---|---|---|
| `GATE_DA_2026_Solutions.md` | 55 questions with full solutions | 2026 paper |
| `GATE_DA_2025_Solutions.md` | 55 questions with full solutions | 2025 paper |
| `GATE_DA_2024_Solutions.md` | 55 questions with full solutions | 2024 (first year) |

---

## 🔥 HIGHEST FREQUENCY TOPICS (Across All 3 Papers)

### Probability & Statistics (appears in EVERY paper, ~25% marks)
| Topic | 2024 | 2025 | 2026 | How Often |
|---|---|---|---|---|
| Bayes Theorem | Q48 | Q21 | Q47 | 🔴 Every year |
| Exponential Distribution | Q47 | Q11,Q31 | Q24 | 🔴 Every year |
| CLT / Normal Approximation | Q17 | Q30 | Q35 | 🔴 Every year |
| CDF Properties | — | Q9,Q29 | Q44 | 🟡 Most years |
| Conditional Expectation | — | Q1 | — | 🟡 |
| Chi-Squared Distribution | — | Q26 | Q43 | 🟡 |
| Covariance/Correlation | Q55 | Q44 | Q53 | 🟡 |

### Linear Algebra (appears in every paper, ~15% marks)
| Topic | 2024 | 2025 | 2026 | How Often |
|---|---|---|---|---|
| Eigenvalue computation | Q3 | Q27,Q28 | Q36 | 🔴 Every year |
| Projection Matrices | Q39 | Q40 | Q42,Q55 | 🔴 Every year |
| Subspaces | Q37 | Q15 | Q12 | 🔴 Every year |
| Trace = Sum of eigenvalues | Q25 | — | Q36 | 🟡 |
| SVD | Q51 | Q40 | — | 🟡 |

### Machine Learning (appears in every paper, ~25% marks)
| Topic | 2024 | 2025 | 2026 | How Often |
|---|---|---|---|---|
| Clustering (k-means/hierarchical) | Q9,Q32 | Q20 | Q26 | 🔴 Every year |
| SVM | Q7 | Q43 | — | 🟡 |
| Ridge Regression | — | — | Q27,Q45 | 🟡 |
| Neural Networks | — | Q32 | Q46 | 🟡 |
| Naive Bayes | Q10 | Q25 | Q13 | 🔴 Every year |
| Metrics (Precision/Recall) | — | — | Q37 | 🟡 |
| PCA | Q8 | Q50 | Q1 | 🔴 Every year |

### Calculus & Optimization (~10% marks)
| Topic | 2024 | 2025 | 2026 | How Often |
|---|---|---|---|---|
| Local min/max (2nd derivative test) | Q5,Q40 | Q39,Q41 | Q17 | 🔴 Every year |
| Sigmoid derivative | Q23 | — | — | 🟡 |
| Limits (rationalization) | Q50 | Q22 | Q25 | 🟡 |
| Taylor Series | — | Q4 | — | 🟡 |

---

## ⚡ QUICK REFERENCE: Most Important Formulas

### Must Memorize Before Exam

```
══════════════════════════════════════════════════════
PROBABILITY ESSENTIALS
══════════════════════════════════════════════════════

Bayes:  P(H|E) = P(E|H)·P(H) / P(E)
        P(E) = Σ P(E|Hᵢ)·P(Hᵢ)

Complement: P(at least 1) = 1 - P(none)

Memoryless (Exponential): P(X>s+t|X>s) = P(X>t)

Distributions:
  Poisson(λ):    E=λ,    Var=λ
  Binomial(n,p): E=np,   Var=np(1-p)
  Exp(λ):        E=1/λ,  Var=1/λ²
  Normal(μ,σ²):  E=μ,    Var=σ²

Z-score: z = (x-μ)/σ
Updated mean: μ_new = (n·μ_old + x_new)/(n+1)

Law of Total Expectation: E[X] = E[E[X|Y]]

Chi-Squared χ²(k): E=k, Var=2k
  Sum of k squared N(0,1) variables ~ χ²(k)

CLT: X̄ ~ N(μ, σ²/n) for large n

══════════════════════════════════════════════════════
LINEAR ALGEBRA ESSENTIALS
══════════════════════════════════════════════════════

Trace = sum of eigenvalues
Determinant = product of eigenvalues
Eigenvalues from: det(A - λI) = 0

For 2×2 [[a,b],[c,d]]:
  λ² - (a+d)λ + (ad-bc) = 0
  Discriminant = (a+d)² - 4(ad-bc)
    > 0: real distinct
    < 0: complex conjugate

Projection Matrix P:
  Symmetric: P = Pᵀ
  Idempotent: P² = P
  Eigenvalues: only 0 or 1

Orthogonal Matrix Q:
  QᵀQ = I, so Qᵀ = Q⁻¹
  Preserves lengths

max(xᵀAx) s.t. xᵀx=1 = largest eigenvalue of A

Rank-Nullity: Rank(A) + Nullity(A) = n (columns)

Subspace test:
  ✓ Span of vectors
  ✓ Solution to Ax=0 (null space)
  ✗ Solution to Ax=b (b≠0)
  ✗ Non-linear constraints

══════════════════════════════════════════════════════
MACHINE LEARNING ESSENTIALS
══════════════════════════════════════════════════════

Sigmoid: σ(x) = 1/(1+e^(-x))
         σ'(x) = σ(x)(1-σ(x))   ← MEMORIZE!

Ridge Loss = MSE + λ||w||₂²
β_ridge = (XᵀX + λI)⁻¹Xᵀy
Effect: ↑λ → ↑Bias, ↓Variance

Linear Regression (no intercept):
w = Σ(xᵢyᵢ) / Σ(xᵢ²)

Naive Bayes:
Parameters for K binary features, 2 classes: 2K+1
Classify: argmax_y P(y) × ΠP(xᵢ|y)

SVM:
Margin = 2/||w||
Support vectors = points on margin boundary

Hierarchical Clustering:
Single linkage = min distance (chaining effect)
Complete linkage = max distance (compact clusters)
Ward = minimize variance increase

PCA:
Components = eigenvectors of covariance matrix
Variance along kth PC = kth largest eigenvalue
All components are ORTHOGONAL (90° apart)

LOOCV with n samples: n validation splits

MLP Parameters (no bias):
Total = Σ (layer_i × layer_{i+1})

Evaluation Metrics:
Accuracy  = (TP+TN)/Total
Precision = TP/(TP+FP)
Recall    = TP/(TP+FN)
F1 = 2PR/(P+R)

══════════════════════════════════════════════════════
CALCULUS ESSENTIALS
══════════════════════════════════════════════════════

2nd Derivative Test:
f'(x*)=0 AND f''(x*)>0 → local MINIMUM
f'(x*)=0 AND f''(x*)<0 → local MAXIMUM

Critical points: f'(x) = 0

Gradient Descent: x = x - α∇f(x)

Geometric Series: Σ(r^n, n=0 to ∞) = 1/(1-r), |r|<1
Starting at n=1: Σ(r^n, n=1 to ∞) = r/(1-r)

Rationalization: √(t²+t) - t → multiply by conjugate → t/(√(t²+t)+t) → 1/2 as t→∞

Taylor key: sinh(x) has only odd powers → even derivatives at 0 = 0

════════════════════════════════════════════════════
```

---

## 📅 1-Month Study Plan Using These PYQs

### Week 1-2: Learn Concepts (Use your Study Notes)
Complete the 5 study notes files first.

### Week 3: GATE PYQ Practice
```
Day 15-16: GATE 2024 - Probability & Statistics questions only
           Q1, Q2, Q17, Q23, Q24, Q26, Q46, Q47, Q48, Q50, Q55

Day 17-18: GATE 2025 - Probability & Statistics questions only
           Q1, Q9, Q10, Q11, Q21, Q25, Q26, Q29, Q30, Q31, Q35, Q44, Q51

Day 19-20: GATE 2026 - Probability & Statistics questions only
           Q9, Q10, Q18, Q24, Q34, Q35, Q43, Q44, Q47, Q52, Q53
```

### Week 4: Full Mixed Practice
```
Day 22-23: Linear Algebra across all 3 years
Day 24-25: ML questions across all 3 years
Day 26-27: Calculus questions across all 3 years
Day 28-30: Timed mixed practice (simulate exam conditions)
```

---

## 🎯 Top 20 Questions to Practice FIRST

These questions test the most frequently repeated concepts:

| Priority | Question | Year | Concept | Why Important |
|---|---|---|---|---|
| 1 | Q47 | 2026 | Bayes Theorem | Classic template, always in exam |
| 2 | Q48 | 2024 | Bayes Theorem | Different numbers, same structure |
| 3 | Q21 | 2025 | Bayes (3 boxes) | Common variant |
| 4 | Q24 | 2026 | Exponential Memoryless | Golden rule, instant answer |
| 5 | Q11 | 2025 | Exponential: Find λ | Standard calculation |
| 6 | Q30 | 2025 | CLT + Binomial | Standardization technique |
| 7 | Q35 | 2025 | Complement method | "At least one" pattern |
| 8 | Q23 | 2024 | Sigmoid derivative | σ(x)(1-σ(x)) — memorize! |
| 9 | Q1 | 2026 | PCA orthogonality | Conceptual, always tested |
| 10 | Q27 | 2026 | Ridge regression | Bias-variance tradeoff |
| 11 | Q36 | 2026 | Trace=sum eigenvalues | Key formula |
| 12 | Q37 | 2026 | Precision/Recall | Confusion matrix calculation |
| 13 | Q40 | 2024 | Local extrema | Second derivative test |
| 14 | Q5 | 2024 | Second derivative test | Fundamental |
| 15 | Q22 | 2025 | Limits (rationalization) | Technique question |
| 16 | Q10 | 2024 | Naive Bayes params | Parameter counting |
| 17 | Q9 | 2026 | Counting (complement) | Probability of even product |
| 18 | Q51 | 2024 | SVD rank-1 | SVD fundamentals |
| 19 | Q46 | 2026 | MLP parameters | Architecture calculation |
| 20 | Q26 | 2025 | Chi-squared variance | Distribution property |

---

## ⚠️ COMMON TRAPS IN GATE DA

### Probability Traps:
1. **Memoryless = Always exponential:** Geometric distribution is also memoryless (discrete version). When you see P(X>s+t|X>s), answer is P(X>t) — no calculation needed!

2. **Correlation ≠ Independence:** Q53 in 2026 proves this — Y depends on X² but correlation(X,Y)=0 because X³ is symmetric.

3. **Rare disease + Accurate test ≠ High posterior:** Bayes surprises in medical testing. Low prevalence overwhelms test accuracy.

4. **Mean of Poisson = Variance of Poisson:** Unique property! χ²(2) also has this (mean=2, variance=4=2×2). Be careful.

### Linear Algebra Traps:
1. **Symmetric matrices have REAL eigenvalues** — not necessarily positive!

2. **Projection matrix P:** P²=P and P=Pᵀ. Eigenvalues are ONLY 0 or 1.

3. **Trace = sum of eigenvalues** is the shortcut for nearly all trace questions.

4. **Rank-Nullity:** Always applies to NUMBER OF COLUMNS, not rows.

5. **AB ≠ BA** (matrix multiplication not commutative). (AB)ᵀ = BᵀAᵀ (order reverses).

### Machine Learning Traps:
1. **High training accuracy ≠ good model.** Overfitting = high train, low test accuracy.

2. **Ridge never makes coefficients exactly 0.** LASSO does — that's the whole difference.

3. **LOOCV splits = n of training set**, not total dataset.

4. **PCA components are always 90° apart** — regardless of data shape.

5. **Single linkage creates "chains"** — elongated clusters. Complete linkage creates compact clusters.

6. **Accuracy is misleading for imbalanced data** — use F1 or precision/recall instead.

### Calculus Traps:
1. **f'(x*)=0 and f''(x*)>0 → LOCAL min** (NOT global!). f(x)=eˣ has no local min despite f''>0 everywhere.

2. **sinh(x) has only odd powers in Taylor series** → all even derivatives at 0 are ZERO.

3. **For limits with √(t²+t)-t form**: ALWAYS rationalize. Result: coefficient of t / 2.

---

## 📊 Exam Day Strategy

```
Your WMT AI Exam:
✅ No negative marking → attempt EVERYTHING
✅ Time: ~2 min per question average
✅ Focus: Probability+ML take priority (60%+ marks)

Order of attack:
1. Start with questions you're confident about
2. ML conceptual MCQs (usually fastest)
3. Probability calculation questions
4. Linear algebra eigenvalue questions
5. Optimization/calculus
6. Flag and return to uncertain ones
7. Guess remaining before time up
```

---

*Master Index | GATE DA PYQ 2024-2026 | For Suvam Das | IIT Madras WMT AI Application W26OTHAI00797*
