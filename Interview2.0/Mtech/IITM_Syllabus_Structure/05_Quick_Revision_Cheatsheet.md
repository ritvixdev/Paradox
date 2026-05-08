# ⚡ TOPIC 5: Quick Revision Cheatsheet
### IIT Madras WMT AI — Everything on 1 Page Per Topic
> 📅 Use in Week 4 (Days 26–30) and on exam day morning

---

# 🎯 EXAM STRATEGY OVERVIEW

```
Your exam format:
- MCQ (1 correct answer)
- MSQ (multiple correct answers — can have partial marks)
- NAT (numeric — type the number)

NO NEGATIVE MARKING → Attempt EVERY single question!

Time: ~2 min per question average
High value: Probability, ML, Linear Algebra (together = 80%+ marks)
```

---

# 📘 PROBABILITY & STATISTICS — One Page

## Counting
```
Permutation (order matters):  P(n,r) = n!/(n-r)!
Combination (order doesn't):  C(n,r) = n!/[r!(n-r)!]
```

## Core Probability
```
P(A∪B) = P(A) + P(B) - P(A∩B)
P(A|B) = P(A∩B)/P(B)
Independent: P(A∩B) = P(A)×P(B)
Mutually Exclusive: P(A∩B) = 0
Complement: P(A') = 1 - P(A)
Bayes: P(A|B) = P(B|A)×P(A)/P(B)
```

## Distributions Quick Table
| Distribution | PMF/PDF | Mean | Variance |
|---|---|---|---|
| Bernoulli | P(X=1)=p | p | p(1-p) |
| Binomial | C(n,k)p^k(1-p)^(n-k) | np | np(1-p) |
| Poisson | e^(-λ)λ^k/k! | λ | λ |
| Uniform(a,b) | 1/(b-a) | (a+b)/2 | (b-a)²/12 |
| Exponential | λe^(-λx) | 1/λ | 1/λ² |
| Normal | (1/σ√2π)e^(-(x-μ)²/2σ²) | μ | σ² |

## Key Facts
```
Normal: 68-95-99.7 rule
z-score: z = (x-μ)/σ
CLT: X̄ ~ N(μ, σ²/n) for large n
95% CI: x̄ ± 1.96σ/√n

t-test: t = (x̄-μ₀)/(s/√n), df=n-1
χ²: Σ(O-E)²/E
Type I Error = α (reject true H₀)
Type II Error = β (accept false H₀)
```

## Variance Properties (Exam Traps!)
```
E[X+Y] = E[X]+E[Y]  (always)
Var[aX+b] = a²Var[X]
Var[X+Y] = Var[X]+Var[Y]  (only if independent)
E[X²] = Var[X] + (E[X])²
```

---

# 📗 LINEAR ALGEBRA — One Page

## Vectors
```
|v| = √Σvᵢ²
a·b = Σaᵢbᵢ = |a||b|cosθ
Perpendicular ↔ a·b = 0
```

## Matrix Properties (Exam Favorites)
```
det[a b; c d] = ad-bc
det(AB) = det(A)×det(B)
det(cA) = cⁿ×det(A)
tr(A) = Σdiagonal = Σeigenvalues
det(A) = Πeigenvalues
(AB)ᵀ = BᵀAᵀ  ← ORDER REVERSES
```

## Special Matrices Quick Reference
| Matrix | Property | What it means |
|---|---|---|
| Orthogonal Q | QᵀQ=I | Columns are orthonormal |
| Symmetric | A=Aᵀ | Real eigenvalues |
| Idempotent P | P²=P | Eigenvalues: only 0 or 1 |
| Positive Definite | All λ>0 | xᵀAx>0, has minimum |

## Rank, Nullity, Solutions
```
Rank + Nullity = n (columns)
Ax=b: Rank(A)=Rank([A|b])=n → unique solution
      Rank(A)=Rank([A|b])<n → infinite solutions
      Rank(A)<Rank([A|b])  → no solution
```

## Eigenvalues
```
det(A - λI) = 0  → characteristic equation
Shortcut 2×2: λ² - tr(A)λ + det(A) = 0
After finding λ: (A-λI)v = 0 → find eigenvector
```

## Decompositions
```
A = LU       (Gaussian elimination, square matrix)
A = UΣVᵀ    (SVD, any matrix — most powerful!)
A = PDP⁻¹   (eigendecomposition, square, n independent eigenvectors)
Projection:  P = A(AᵀA)⁻¹Aᵀ
```

---

# 📙 OPTIMIZATION — One Page

## Derivatives
```
[xⁿ]' = nxⁿ⁻¹
[eˣ]' = eˣ
[ln x]' = 1/x
[sin x]' = cos x
Chain rule: [f(g(x))]' = f'(g)×g'
```

## Finding Extrema
```
Step 1: Set f'(x) = 0 → find critical points
Step 2: Check f''(x):
  f''(x) > 0 → MINIMUM ∪
  f''(x) < 0 → MAXIMUM ∩
  f''(x) = 0 → inconclusive
```

## Gradient Descent
```
x_{t+1} = x_t - α × ∇f(x_t)
∇f = [∂f/∂x₁, ∂f/∂x₂, ...]
Converges to global min if f is CONVEX
```

## Convexity Test
```
f is convex ↔ f''(x) ≥ 0 everywhere
MSE loss is convex → gradient descent finds global minimum
Neural network loss is non-convex → local minima possible
```

---

# 📕 MACHINE LEARNING — One Page

## Regression
```
Simple: ŷ = β₀ + β₁x
β₁ = Cov(X,Y)/Var(X)
β = (XᵀX)⁻¹Xᵀy  (normal equations)
Ridge: β = (XᵀX+λI)⁻¹Xᵀy
R² = 1 - SSE/SST  (0=bad, 1=perfect)
```

## Classification Algorithms
```
Logistic: P(y=1) = σ(wᵀx), σ(z)=1/(1+e^(-z))
kNN: majority vote of k nearest neighbours
SVM: max margin hyperplane, kernel trick for non-linear
Naive Bayes: P(y|x) ∝ P(y)×ΠP(xᵢ|y)
Decision Tree: split by Gini/Entropy/Info Gain
```

## Confusion Matrix Metrics
```
Accuracy  = (TP+TN)/Total
Precision = TP/(TP+FP)    ← quality of positives
Recall    = TP/(TP+FN)    ← coverage of positives
F1 = 2×P×R/(P+R)
```

## Bias-Variance
```
Error = Bias² + Variance + Noise
High Bias = underfitting (too simple)
High Variance = overfitting (too complex)
Ridge/LASSO: ↑λ → ↑Bias, ↓Variance
```

## Unsupervised
```
k-Means: minimize Σ||x-μᵢ||² (sensitive to init, k known)
Hierarchical: dendrogram, no need to specify k
PCA: eigenvectors of covariance matrix = principal components
     Explained variance = λᵢ/Σλⱼ
```

---

# 🧠 IDENTIFY THE ALGORITHM QUICK TABLE

| Clue in question | Answer |
|---|---|
| "No training, uses distance" | kNN |
| "Maximum margin hyperplane" | SVM |
| "Assumes feature independence" | Naive Bayes |
| "Minimizes squared error" | Linear Regression |
| "Outputs probability for binary" | Logistic Regression |
| "Splits nodes by impurity" | Decision Tree |
| "Finds directions of max variance" | PCA |
| "Groups without labels" | Clustering (k-means) |
| "Builds tree of merges" | Hierarchical Clustering |
| "L1 regularization" | LASSO |
| "L2 regularization" | Ridge Regression |
| "Higher λ → more shrinkage" | Ridge or LASSO |

---

# ⚠️ MOST COMMON EXAM TRAPS

## Probability Traps:
1. **Mutually exclusive ≠ independent** (they're opposites for events with P>0!)
2. **Correlation = 0 does NOT mean independent** (for non-normal distributions)
3. **Rare disease + accurate test = low posterior probability** (Bayes)
4. **P(A and B) uses multiplication rule, P(A or B) uses addition rule**

## Linear Algebra Traps:
1. **AB ≠ BA** (matrix multiplication not commutative)
2. **(AB)ᵀ = BᵀAᵀ** (transpose reverses order)
3. **Rank 0 → det = 0 → not invertible → infinite solutions to Ax=0**
4. **Eigenvalues of Aᵀ = eigenvalues of A**

## ML Traps:
1. **High train accuracy + low test accuracy = overfitting** (not a good model)
2. **Accuracy is misleading for imbalanced data** (use F1 instead)
3. **Ridge never makes coefficients exactly 0** (only LASSO does)
4. **kNN with k=1 has 0 training error** (but overfits!)
5. **Gini impurity = 0 means pure node, not 0.5**

---

# 📚 RECOMMENDED PRACTICE PLAN (WEEK 4)

## Days 22-24: GATE DA Practice
```
Download (search online):
1. "GATE DA 2024 question paper PDF" — solve prob/stats/LA/ML questions
2. "GATE DA 2025 question paper PDF" — same
SKIP: Programming, Database, AI search questions
```

## Days 25-27: Weak Topic Focus
```
Rate each topic after practice:
✅ Comfortable: probability axioms, matrix operations
⚠️  Shaky: Bayes theorem, eigenvalues, PCA
❌ Need work: hypothesis testing, SVM details
→ Revisit ❌ topics in these days
```

## Days 28-30: Final Revision
```
- Read this cheatsheet daily
- Do 5 questions per topic each day
- Review mistakes carefully
- Sleep well before exam!
```

---

# 🎯 ON EXAM DAY

```
1. Read question fully — "at least", "exactly", "at most" change everything
2. For MCQ: Eliminate clearly wrong options first
3. For NAT (numeric): Double-check arithmetic
4. For MSQ: Check ALL options — partial marks available
5. Attempt EVERY question — no negative marking!
6. Flag uncertain questions and return to them
7. Probability + ML questions first (your strongest topics)
8. Don't spend more than 3 min on any single question
```

---

## 💪 Final Message for Suvam

You're a Senior Software Engineer with 6 years of experience.
You solve complex technical problems daily.
This exam tests concepts — and you have the discipline to learn them.

**The formula for success:**
- 1 month of consistent 2-hour daily study
- Understanding > memorization
- Practice questions > re-reading notes
- Sleep > last-minute cramming

**You've already done the hard part** — applied, planned, and committed.
Now just execute.

**Go get that IIT Madras M.Tech seat! 🎓**

---
*Cheatsheet prepared specifically for Suvam Das | WMT AI 2026 Entrance | App: W26OTHAI00797*
