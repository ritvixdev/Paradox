# 📚 GATE DS&AI 2024 — Previous Year Questions with Solutions
### Complete Analysis | Answers | Tricks | Concepts
> **Exam:** GATE Data Science & Artificial Intelligence 2024 (IISc Bangalore — First Year!)
> **Prepared for:** IIT Madras WMT AI Entrance — Suvam Das

---

## ⚠️ YOUR EXAM FILTER
> 🎯 = **Directly in your WMT AI syllabus — MUST STUDY**
> ⚪ = NOT in your WMT syllabus (skip for now)

---

# GENERAL APTITUDE

---

## GA Q3 — Counting with Divisibility
**Answer: B (48)**

**Question:** 4-digit numbers divisible by 3, using digits {1,3,4,6,7}, no digit repeated.

**Solution:**
A number is divisible by 3 ↔ sum of digits is divisible by 3.

Digit sums of 4-digit subsets from {1,3,4,6,7}:
- {1,3,4,6}: sum=14 → 14 mod 3 = 2 ✗
- {1,3,4,7}: sum=15 → 15 mod 3 = 0 ✓
- {1,3,6,7}: sum=17 → 17 mod 3 = 2 ✗
- {1,4,6,7}: sum=18 → 18 mod 3 = 0 ✓
- {3,4,6,7}: sum=20 → 20 mod 3 = 2 ✗

Valid sets: {1,3,4,7} and {1,4,6,7}
For each set: 4! = 24 arrangements
Total = 2 × 24 = **48 ✓**

**Trick:** Sum of digits divisibility rule. Check all C(5,4)=5 subsets.

---

## GA Q7 — Probability of Two Girls, One Boy
**Answer: A (3/8)**

P(2G, 1B) = C(3,2) × (1/2)² × (1/2)¹ = 3 × 1/8 = **3/8 ✓**

**Binomial Formula:** P(k successes in n trials) = C(n,k) × p^k × (1-p)^(n-k)

---

# CORE DA — PROBABILITY & STATISTICS

---

## 🎯 Q1 — Poisson and Normal Distribution Facts
**Answer: A (Both true)** | **Topic: Key Distribution Properties**

**Statement (i):** Mean and variance of Poisson are EQUAL — **TRUE**
For Poisson(λ): E[X] = λ, Var[X] = λ → Mean = Variance ✓

**Statement (ii):** Standard normal: mean=0, variance=1 — **TRUE**
N(0,1) by definition: μ=0, σ²=1 ✓

**Answer: A (Both true) ✓**

**Must Memorize for GATE:**
| Distribution | Mean | Variance |
|---|---|---|
| Bernoulli(p) | p | p(1-p) |
| Binomial(n,p) | np | np(1-p) |
| **Poisson(λ)** | **λ** | **λ** |
| Exponential(λ) | 1/λ | 1/λ² |
| Normal(μ,σ²) | μ | σ² |
| Uniform(a,b) | (a+b)/2 | (b-a)²/12 |

---

## 🎯 Q2 — Mutually Exclusive Events
**Answer: A (P(T∩S)=0)** | **Topic: Probability**

**Question:** 3 coins. T = "2 or more heads", S = "2 or more tails". P(T∩S)?

**Solution:**
- T occurs: HHH, HHT, HTH, THH (2+ heads)
- S occurs: TTT, TTH, THT, HTT (2+ tails)
- T∩S: need both 2+ heads AND 2+ tails in 3 tosses → **impossible** (you can't have ≥2H and ≥2T with only 3 coins)

**P(T∩S) = 0 ✓**

T and S are **mutually exclusive** events.

**Trick:** Count: 2 heads + 2 tails requires 4 tosses, but we only have 3. Hence impossible.

---

## 🎯 Q17 — Z-Score Normalization
**Answer: B (0.476)** | **Topic: Z-Score**

**Question:** Income: min=46000, max=170000, mean=96000, std=21000. Z-score of ₹106000?

**Solution:**
```
z = (x - mean) / std = (106000 - 96000) / 21000 = 10000 / 21000 ≈ 0.476 ✓
```

**Answer: B ✓**

**Z-Score Formula:** z = (x - μ) / σ

**What z-score tells you:** How many standard deviations away from the mean.

**Quick Check:**
- z=0: exactly at mean
- z=1: one std above mean
- z=-1: one std below mean

---

## 🎯 Q23 — Sigmoid Derivative
**Answer: 0.24** | **Topic: Calculus, Activation Functions**

**Question:** f(x) = 1/(1+e^(-x)). Find f'(x) where f(x)=0.4.

**Solution:**
The beautiful derivative property of sigmoid:
```
f'(x) = f(x) × (1 - f(x))
```

So when f(x) = 0.4:
```
f'(x) = 0.4 × (1 - 0.4) = 0.4 × 0.6 = 0.24 ✓
```

**Answer: 0.24 ✓**

**MEMORIZE:** σ'(x) = σ(x)(1-σ(x))

**Derivation (in case asked):**
σ'(x) = d/dx[1/(1+e^(-x))] = e^(-x)/(1+e^(-x))² = [1/(1+e^(-x))] × [e^(-x)/(1+e^(-x))]
= σ(x) × (1 - σ(x))

**This is tested repeatedly in GATE — memorize it!**

---

## 🎯 Q24 — Updated Sample Mean
**Answer: 42** | **Topic: Statistics**

**Question:** 50 data points, mean=40. Add one data point with value 142. New mean?

**Solution:**
```
Old sum = 50 × 40 = 2000
New sum = 2000 + 142 = 2142
New count = 51
New mean = 2142 / 51 = 42 ✓
```

**Updated Mean Formula:**
```
new_mean = (n × old_mean + new_value) / (n+1)
         = (50×40 + 142) / 51 = 2142/51 = 42
```

**Shortcut:** new_mean = old_mean + (new_value - old_mean)/(n+1) = 40 + (142-40)/51 = 40 + 2 = 42

---

## 🎯 Q26 — Expected Consecutive Even Numbers
**Answer: C (6)** | **Topic: Geometric Distribution, Expected Value**

**Question:** Roll die until TWO CONSECUTIVE even numbers. Expected number of rolls?

**Solution:**
P(even) = 1/2 on each roll.

Let E = expected rolls to get 2 consecutive evens.

**States:** Let E₀ = starting state, E₁ = just got one even.

Setting up equations:
```
E₀ = 1 + (1/2)E₁ + (1/2)E₀   [with prob 1/2 move to E₁, with 1/2 stay at E₀]
E₁ = 1 + (1/2)×0 + (1/2)E₀   [with prob 1/2 done (two evens!), with 1/2 back to E₀]
```

From E₁: E₁ = 1 + (1/2)E₀
Substitute into E₀: E₀ = 1 + (1/2)(1 + (1/2)E₀) + (1/2)E₀
= 1 + 1/2 + (1/4)E₀ + (1/2)E₀
= 3/2 + (3/4)E₀

(1/4)E₀ = 3/2 → **E₀ = 6 ✓**

**Answer: C ✓**

**Technique:** Use state-based equations. Define states based on progress, write equations for expected steps from each state.

---

## 🎯 Q46 — Joint Uniform Distribution
**Answer: 0.125** | **Topic: Joint Probability, Continuous**

**Question:** X~Uniform(1,3), Y~Uniform(2,4), independent. Find P(X≥Y).

**Solution:**
Joint pdf = f_X(x) × f_Y(y) = (1/2) × (1/2) = 1/4 on the rectangle [1,3]×[2,4].

```
P(X≥Y) = ∫∫_{X≥Y} (1/4) dx dy
```

Region where X≥Y within [1,3]×[2,4]:
- Need x≥y, 1≤x≤3, 2≤y≤4
- For x≥y: y≤x, combined with y∈[2,4]: need y∈[2,x] (only when x≥2)
- x range where X≥Y possible: x∈[2,3] (since y≥2 always)

```
P(X≥Y) = (1/4) × ∫₂³ ∫₂ˣ dy dx
        = (1/4) × ∫₂³ (x-2) dx
        = (1/4) × [(x-2)²/2]₂³
        = (1/4) × [1/2 - 0]
        = 1/8 = 0.125 ✓
```

**Answer: 0.125 ✓**

**Geometric approach:** Area where X≥Y within rectangle [1,3]×[2,4]:
The overlap region is a triangle with vertices (2,2), (3,2), (3,3). Area = (1/2)(1)(1) = 0.5.
Total rectangle area = 2×2 = 4. P = 0.5/4 = 0.125 ✓ (faster!)

---

## 🎯 Q47 — Exponential Distribution: Find λ
**Answer: 0.2** | **Topic: Exponential Distribution**

**Question:** X ~ Exp(λ). 5E(X) = Var(X). Find λ.

**Solution:**
For Exponential(λ): E(X) = 1/λ, Var(X) = 1/λ²

```
5 × (1/λ) = 1/λ²
5/λ = 1/λ²
5λ² = λ    [multiply both sides by λ²]
5λ = 1
λ = 1/5 = 0.2 ✓
```

**Answer: λ = 0.2 ✓**

---

## 🎯 Q48 — Bayes' Theorem Application
**Answer: 0.25** | **Topic: Bayes' Theorem**

**Question:** P(T̄)=0.6, P(S|T)=0.3, P(S|T̄)=0.6. Find P(T|S).

**Solution:**
```
P(T) = 1 - P(T̄) = 1 - 0.6 = 0.4

P(S) = P(S|T)P(T) + P(S|T̄)P(T̄)
     = 0.3×0.4 + 0.6×0.6
     = 0.12 + 0.36 = 0.48

P(T|S) = P(S|T)P(T) / P(S)
        = 0.12 / 0.48
        = 0.25 ✓
```

**Answer: 0.25 ✓**

**Bayes Template:**
```
P(H|E) = P(E|H) × P(H) / [P(E|H)P(H) + P(E|H̄)P(H̄)]
```

---

## 🎯 Q50 — Limit using L'Hôpital / Taylor
**Answer: 0.5** | **Topic: Limits**

**Question:** lim(x→0) ln((x²+1)cos(x)) / x²

**Solution:**
```
ln((x²+1)cos(x)) = ln(x²+1) + ln(cos(x))
```

Using Taylor series near x=0:
```
ln(1+x²) ≈ x² - x⁴/2 + ...
ln(cos x) ≈ ln(1 - x²/2 + ...) ≈ -x²/2 + ...

Sum ≈ x² - x²/2 = x²/2

Divide by x²: x²/2 / x² = 1/2 = 0.5 ✓
```

**Answer: 0.5 ✓**

**Trick:** For limits of type 0/0, use Taylor series expansion and keep only leading terms.

---

## 🎯 Q51 — SVD of Rank-1 Matrix
**Answer: 55** | **Topic: SVD, Rank-1 Matrix**

**Question:** u=[1,2,3,4,5]ᵀ. M = uuᵀ. Find Σσᵢ.

**Solution:**
M = uuᵀ is a rank-1 matrix. It has exactly ONE non-zero singular value.

For rank-1 matrix uuᵀ:
- Only one singular value: σ₁ = ||u||² = 1²+2²+3²+4²+5² = 1+4+9+16+25 = 55
- All other singular values = 0

**Σσᵢ = 55 + 0 + 0 + 0 + 0 = 55 ✓**

**Answer: 55 ✓**

**Key Result:** For matrix M = uuᵀ:
- Rank = 1
- One singular value = ||u||²
- All other singular values = 0
- Only non-zero eigenvalue = ||u||² (with eigenvector u/||u||)

---

## 🎯 Q55 — Covariance Calculation
**Answer: 0.0625** | **Topic: Covariance**

**Question:** 2 coins. X=1 if both heads, 0 otherwise. Y=1 if at least one head, 0 otherwise. Find Cov(X,Y).

**Solution:**
```
Sample space: HH, HT, TH, TT (each prob 1/4)

X: HH→1, others→0
Y: HH→1, HT→1, TH→1, TT→0

E[X] = 1/4
E[Y] = 3/4
E[XY] = E[X×Y]:
  HH: 1×1=1, prob=1/4
  HT: 0×1=0
  TH: 0×1=0
  TT: 0×0=0
E[XY] = 1/4

Cov(X,Y) = E[XY] - E[X]E[Y]
          = 1/4 - (1/4)(3/4)
          = 1/4 - 3/16
          = 4/16 - 3/16 = 1/16 = 0.0625 ✓
```

**Answer: 0.0625 ✓**

**Covariance Formula:** Cov(X,Y) = E[XY] - E[X]E[Y]

---

## 🎯 Q52 — Decision Tree Information Gain
**Answer: ~0.125** | **Topic: Decision Trees**

**Question:** 10 cricket matches. 4 Green wins, 6 Blue wins. Compute InfoGain(Pitch).

**Solution:**
```
Dataset: 10 matches. Wins: Green=4, Blue=6.

Entropy(root) = -( 4/10 × log₂(4/10) + 6/10 × log₂(6/10) )
               = -(0.4×(-1.322) + 0.6×(-0.737))
               = -(−0.529 − 0.442) = 0.971

Split by Pitch:
- S (Spin): matches 1,2,4,7,10 = 5 matches; Green:3 (1,7,10), Blue:2 (2,4)
- F (Pace): matches 3,5,6,8,9 = 5 matches; Green:1 (5), Blue:4 (3,6,8,9)

Entropy(S) = -(3/5×log₂(3/5) + 2/5×log₂(2/5))
           = -(0.6×(-0.737) + 0.4×(-1.322))
           = -(−0.442 − 0.529) = 0.971

Entropy(F) = -(1/5×log₂(1/5) + 4/5×log₂(4/5))
           = -(0.2×(-2.322) + 0.8×(-0.322))
           = -(−0.464 − 0.258) = 0.722

Weighted entropy after split:
= (5/10)×0.971 + (5/10)×0.722 = 0.4855 + 0.361 = 0.8465

InfoGain = 0.971 - 0.8465 ≈ 0.124 ≈ 0.12 ✓
```

**Answer: ~0.12 ✓**

**Information Gain Formula:**
```
IG(S, A) = Entropy(S) - Σᵥ (|Sᵥ|/|S|) × Entropy(Sᵥ)
```

---

# LINEAR ALGEBRA

---

## 🎯 Q3 — Eigenvalues of 2×2 Matrix
**Answer: B (Complex conjugate pairs)** | **Topic: Eigenvalues**

**Question:** M = [[2,-1],[3,1]]. What type of eigenvalues?

**Solution:**
```
det(M - λI) = det([[2-λ,-1],[3,1-λ]]) = (2-λ)(1-λ)+3
= 2 - 2λ - λ + λ² + 3 = λ² - 3λ + 5 = 0

Discriminant: 9 - 20 = -11 < 0

→ Complex conjugate eigenvalues! ✓
```

**Answer: B ✓**

**Eigenvalue Types for 2×2 [[a,b],[c,d]]:**
- Discriminant of characteristic equation = (a+d)² - 4(ad-bc)
- Discriminant > 0: Two distinct real eigenvalues
- Discriminant = 0: Repeated real eigenvalue
- Discriminant < 0: Complex conjugate pair

**Trick:** For a real non-symmetric matrix, complex eigenvalues come in conjugate pairs. Real symmetric matrices ALWAYS have real eigenvalues.

---

## 🎯 Q5 — Second Derivative Test
**Answer: A (Local minimum)** | **Topic: Calculus, Optimization**

**Question:** f'(x*) = 0 and f''(x*) > 0. Then f has a ___ at x*.

**Solution:**
**Second Derivative Test:**
- f'(x*) = 0: x* is a critical point
- f''(x*) > 0: concave UP → local **minimum** ✓
- f''(x*) < 0: concave DOWN → local maximum

**Key:** This is only local minimum, NOT necessarily global!

**Answer: A ✓**

**Why not global?** f could have lower values elsewhere. f''(x*)>0 only guarantees local behavior.

---

## 🎯 Q25 — Determinant Property
**Answer: 0** | **Topic: Determinant, Eigenvalues**

**Question:** M = [[1,2,3],[3,1,3],[4,3,6]]. Find det(M²+12M).

**Solution:**
Factor: M²+12M = M(M+12I)

So det(M²+12M) = det(M) × det(M+12I)

**First, find det(M):**
```
det(M) = 1(1×6-3×3) - 2(3×6-3×4) + 3(3×3-1×4)
        = 1(6-9) - 2(18-12) + 3(9-4)
        = 1(-3) - 2(6) + 3(5)
        = -3 - 12 + 15 = 0
```

Since det(M) = 0 → **det(M²+12M) = 0 × det(M+12I) = 0 ✓**

**Answer: 0 ✓**

**Trick:** det(AB) = det(A)×det(B). If either factor has det=0, product is 0!

**Alternative:** Since det(M)=0, M is singular. Then M has eigenvalue 0. So M² has eigenvalue 0, 12M has eigenvalue 0. But M²+12M = M(M+12I) still has det=0.

---

## 🎯 Q27 — Continuity and Differentiability
**Answer: A (a=1/4, b=0, c=1)** | **Topic: Calculus**

**Question:** Piecewise f(x): -x for x<-2, ax²+bx+c for -2≤x≤2, x for x>2. Find a,b,c for smooth function.

**Solution:**
**Continuity at x=-2:** Left = -(-2) = 2; Right = 4a-2b+c = 2 → 4a-2b+c = 2

**Differentiability at x=-2:** f'(-x) = -1; f'(ax²+bx+c) = 2ax+b → at x=-2: -4a+b = -1

**Continuity at x=2:** Right = 2; Left = 4a+2b+c = 2 → 4a+2b+c = 2

From continuity equations: (4a+2b+c) - (4a-2b+c) = 0 → 4b = 0 → **b = 0**

From differentiability at x=-2: -4a+0 = -1 → **a = 1/4**

From continuity: 4(1/4)-0+c = 2 → 1+c = 2 → **c = 1** ✓

**Differentiability at x=2:** f'(ax²+bx+c) at x=2 = 2(1/4)(2)+0 = 1 = f'(x) at x=2 ✓

**Answer: A ✓**

**Method for piecewise functions:**
1. Continuity at boundary: left limit = right limit = function value
2. Differentiability: left derivative = right derivative

---

## 🎯 Q37 — Subspaces of R³
**Answer: A;C** | **Topic: Vector Spaces, Subspaces**

**Question:** Which are subspaces of R³?

**Solution:**

**A: {x = α[1,1,0]+β[1,0,0], α,β∈R}** — This is the span of two vectors. Span is ALWAYS a subspace (closed under addition and scalar multiplication, contains zero). ✓

**B: {x = α²[1,2,0]+β²[1,0,1], α,β∈R}** — Contains α²[1,2,0]+β²[1,0,1]. If α=β=1, x=[2,2,1]. But scalar multiplication by -1: -1×[2,2,1]=[-2,-2,-1] must also be in set. Can we write [-2,-2,-1] as α²[1,2,0]+β²[1,0,1]? We need α²=-2 which is impossible for real α. **NOT a subspace** ✗

**C: {x ∈ R³: 5x₁+2x₃=0, 4x₁-2x₂+3x₃=0}** — Solution set of homogeneous system. Null space of a matrix is ALWAYS a subspace. ✓

**D: {x ∈ R³: 5x₁+2x₃+4=0}** — Doesn't contain zero vector (5(0)+2(0)+4=4≠0). **NOT a subspace** ✗

**Answer: A;C ✓**

**Key Rules for Subspace:**
1. Contains zero vector
2. Closed under addition
3. Closed under scalar multiplication

**Quick Test:**
- Span of vectors: ALWAYS subspace
- Solution to Ax=0: ALWAYS subspace (null space)
- Solution to Ax=b (b≠0): NEVER subspace (no zero vector)
- Quadratic constraints (α², β²): usually NOT subspace

---

## 🎯 Q38 — System of Equations: Existence
**Answer: B;D** | **Topic: Linear Systems**

**Question:** Which combinations of solution types are possible?

**Solution:**

**A: 3×3 matrix, Mx=p unique, Mx=q infinite** — IMPOSSIBLE. If rank(M)=n=3 for unique solution, then ALL systems Mx=b have unique solutions (if consistent). Can't have one unique and one infinite with SAME matrix.

**B: 3×3 matrix, Mx=p no solution, Mx=q infinite** ✓ — If rank(M)=r<3, some b's are in column space (infinite solutions) and some aren't (no solution). **POSSIBLE** ✓

**C: 2×3 matrix, Mx=p unique, Mx=q infinite** — IMPOSSIBLE. For 2×3 matrix, even if rank=2, the system Ax=b in 3 unknowns with 2 equations can never have a unique solution (null space has dimension 3-2=1 > 0, so infinite solutions or none).

**D: 3×2 matrix, Mx=p unique, Mx=q no solution** ✓ — 3×2 matrix means 3 equations, 2 unknowns. Can have unique solution for some b (consistent) and no solution for other b (inconsistent with overdetermined system). **POSSIBLE** ✓

**Answer: B;D ✓**

**Key Rules:**
- m×n matrix: at most min(m,n) independent equations
- If n > m: cannot have unique solution (too many unknowns)
- If m > n: can have no solution (overdetermined)
- Unique ↔ no solution: IMPOSSIBLE with same matrix (either null space is trivial or not)

---

## 🎯 Q39 — Projection Matrix Properties
**Answer: B;C;D** | **Topic: Projection Matrices**

**Question:** M is projection matrix onto subspace U of R³. Which are true?

**Solution:**

**A: U is 1D → null space of M is 1D** — FALSE. If U is 1D (line), projection onto 1D → null space is the orthogonal complement = 2D. So null space has dimension 3-1=2. ✗

**B: U is 2D → null space of M is 1D** ✓ — 2D subspace → projection kills everything orthogonal (1D). Null space dim = 3-2=1. ✓

**C: M² = M** ✓ — Projection matrices are idempotent. ✓

**D: M³ = M** ✓ — M³ = M²×M = M×M = M. (Since M²=M) ✓

**Answer: B;C;D ✓**

---

## 🎯 Q40 — Local Extrema
**Answer: A;B** | **Topic: Calculus, Optimization**

**Question:** f(x) = x⁴/4 - 2x³/3 - 3x²/2 + 1. Which are true?

**Solution:**
```
f'(x) = x³ - 2x² - 3x = x(x² - 2x - 3) = x(x-3)(x+1) = 0
Critical points: x = 0, x = 3, x = -1

f''(x) = 3x² - 4x - 3

f''(0) = -3 < 0 → local MAXIMUM at x=0 ✓ (A)
f''(3) = 27-12-3 = 12 > 0 → local MINIMUM at x=3 ✓ (B)
f''(-1) = 3+4-3 = 4 > 0 → local MINIMUM at x=-1 ✗ (C says maximum, FALSE)
```

**Answer: A;B ✓**

---

# MACHINE LEARNING

---

## 🎯 Q7 — SVM Support Vectors
**Answer: D ({x1,x2,x3,x4})** | **Topic: SVM**

**Question:** 6 data points. Hard-margin SVM. Which set is valid support vectors?

**Solution:**
Support vectors are the points closest to the decision boundary (on the margin).

For hard-margin SVM with this data, the separating hyperplane is along x₁+x₂=0 (the line y=−x in 2D sense). The margin boundary includes the inner points x₁=[1,0], x₂=[0,1], x₃=[0,-1], x₄=[-1,0].

The outer points x₅=[2,2] and x₆=[-2,-2] are further from the boundary, so they are NOT support vectors.

{x₁,x₂,x₃,x₄} are the closest to the boundary → support vectors ✓

**Answer: D ✓**

---

## 🎯 Q8 — Algorithm Classification
**Answer: C (PCA-dim reduction, NB-generative, LR-discriminative)** | **Topic: ML Taxonomy**

**Solution:**
- **PCA:** Dimensionality Reduction → **ii** ✓
- **Naive Bayes:** Models P(x|y) and P(y) (the data generation process) → **Generative Model** → **iii** ✓
- **Logistic Regression:** Directly models P(y|x) without modelling data generation → **Discriminative Model** → **i** ✓

**Answer: C ✓**

**Generative vs Discriminative:**
| Type | Models | Examples |
|---|---|---|
| **Generative** | P(x\|y) and P(y) | Naive Bayes, GMM, HMM |
| **Discriminative** | P(y\|x) directly | Logistic Regression, SVM, Neural Networks |

**Memory Trick:** "Generative = Generates data (models how data is generated). Discriminative = Discriminates between classes."

---

## 🎯 Q9 — k-Means Cluster Membership
**Answer: D ([0,1])** | **Topic: k-Means**

**Question:** [1,1] and [-1,1] are both in cluster 3. Which is necessarily also in cluster 3?

**Solution:**
The centroid of cluster 3 must be such that both [1,1] and [-1,1] are closer to it than to centroids of other clusters.

The midpoint of [1,1] and [-1,1] is [0,1]. By symmetry, the centroid must have x-coordinate = 0.

Point [0,1] is equidistant from both [1,1] and [-1,1] (distance = 1 each). It's between them.

If [1,1] and [-1,1] are both in cluster 3, the centroid is somewhere around [0,1]. The point [0,1] must be in the same cluster because:
- Distance from [0,1] to [1,1]: √(1+0) = 1
- Distance from [0,1] to [-1,1]: √(1+0) = 1
- [0,1] is the average of the two → same cluster

More rigorously: any point on the line between two points in a convex region is in the same cluster.

**Answer: D ([0,1]) ✓**

---

## 🎯 Q10 — Naive Bayes Parameters
**Answer: B (2K+1)** | **Topic: Naive Bayes, Parameters**

**Question:** K binary attributes, 2-class problem. How many parameters for Naive Bayes?

**Solution:**
For Naive Bayes with K binary features and 2 classes:

- **Class prior:** P(y=1) = 1 parameter (P(y=0) = 1 - P(y=1))
- **Feature likelihoods:** For each class (2) and each feature (K), need P(xⱼ=1|y):
  - 2 classes × K features = 2K parameters
  - (P(xⱼ=0|y) = 1 - P(xⱼ=1|y), so only 1 param per feature-class combo)

**Total = 2K + 1 ✓**

**Answer: B ✓**

---

## 🎯 Q12 — Linear Discriminant Analysis
**Answer: A** | **Topic: LDA, Generalized Eigenvalue Problem**

The Fisher LDA maximizes J(u) = (uᵀSBu)/(uᵀSWu).

Setting gradient to zero leads to: SB×u = λ×SW×u

If SW is non-singular: SW⁻¹×SB×u = λ×u → **eigenvalue problem** ✓

**Answer: A ✓**

---

## 🎯 Q32 — Single Linkage Clustering
**Answer: A** | **Topic: Hierarchical Clustering**

**Question:** Distance matrix given. Single linkage clustering. Find result after all merges.

**Solution — Step by step (Single linkage = minimum distance):**

Distance matrix:
```
     x1  x2  x3  x4  x5
x1    0   1   4   3   6
x2    1   0   3   5   3
x3    4   3   0   2   5
x4    3   5   2   0   1
x5    6   3   5   1   0
```

**Step 1:** Minimum distance = 1 between (x1,x2) AND (x4,x5). Merge first found: **(x1,x2)** → cluster A={x1,x2}

**Step 2:** Update distances (single linkage = min):
- d(A,x3) = min(d(x1,x3), d(x2,x3)) = min(4,3) = 3
- d(A,x4) = min(d(x1,x4), d(x2,x4)) = min(3,5) = 3
- d(A,x5) = min(d(x1,x5), d(x2,x5)) = min(6,3) = 3
- d(x4,x5) = 1 ← minimum!

**Step 3:** Merge (x4,x5) → cluster B={x4,x5}

**Step 4:** Distances:
- d(A,x3) = 3
- d(A,B) = min(d(x1,x4),d(x1,x5),d(x2,x4),d(x2,x5)) = min(3,6,5,3) = 3
- d(x3,B) = min(d(x3,x4),d(x3,x5)) = min(2,5) = 2 ← minimum!

**Step 5:** Merge (x3,B) → {x3,x4,x5}

**Step 6:** d(A, {x3,x4,x5}) = min of all = 3. Merge everything → {x1,x2,x3,x4,x5}

**Clusters at cut: {x1,x2} and {x3,x4,x5} ✓ → Answer A**

---

## 🎯 Q54 — Bayesian Network Joint Probability
**Answer: 0.125** | **Topic: Bayesian Networks, Joint Probability**

**Question:** Bayesian network with U,V,W,Z. Find P(U=1,V=1,W=1,Z=1).

**Solution:**
Using the chain rule (Bayesian network factorization):
```
P(U=1,V=1,W=1,Z=1) = P(U=1) × P(V=1|U=1) × P(W=1|U=1) × P(Z=1|V=1,W=1)

From tables:
P(U=1) = 0.5
P(V=1|U=1) = 0.5
P(W=1|U=1) = 1    [from table: P(W=1|U=1)=1]
P(Z=1|V=1,W=1) = 0.5  [from table: P(Z=1|V=1,W=1)=0.5]

Product = 0.5 × 0.5 × 1 × 0.5 = 0.125 ✓
```

**Answer: 0.125 ✓**

**Bayesian Network Rule:** 
```
P(x₁,...,xₙ) = Π P(xᵢ | parents(xᵢ))
```
Read CPT for each variable given its parents.

---

# PROGRAMMING & DSA

> ⚪ These topics are NOT in your WMT AI entrance exam.

---

## ⚪ Q28 — Tree Node Counting (Python)
**Answer: D (9)**

Recursive function counts nodes in a tree. Node 0 has children [1,2]. Node 1 has [3,4,5]. Node 2 has [6,7,8].

count(0) = 1 + count(1) + count(2)
count(1) = 1 + count(3) + count(4) + count(5) = 1+1+1+1 = 4
count(2) = 1 + count(6) + count(7) + count(8) = 1+1+1+1 = 4
count(0) = 1 + 4 + 4 = **9** ✓

---

## ⚪ Q31 — Python Function: Reversal
**Answer: C (Reverses D between s1 and s2)**

The function swaps D[s1] and D[s2], then recursively swaps inner elements → **reverse** in-place.

---

# 📊 2024 QUESTION SUMMARY FOR WMT EXAM

| Category | Questions | Concept Tested |
|---|---|---|
| **Probability** | Q1, Q2, Q17, Q23, Q24, Q26, Q46, Q47, Q48, Q50, Q55 | Distributions, Bayes, Moments |
| **Linear Algebra** | Q3, Q5, Q25, Q27, Q37, Q38, Q39, Q40 | Eigenvalues, Subspaces, Systems |
| **Machine Learning** | Q7, Q8, Q9, Q10, Q12, Q32, Q52, Q54 | SVM, NB, Clustering, Decision Trees |
| **Calculus** | Q5, Q23, Q27, Q50 | Derivatives, Limits, Optimization |

---

# 🔑 KEY FORMULAS FROM 2024 PAPER

```
PROBABILITY:
Poisson: E[X] = Var[X] = λ
P(T∩S) = 0 if mutually exclusive
Bayes: P(T|S) = P(S|T)P(T) / P(S)
Joint Uniform: P(X≥Y) via geometric/integral method

Z-SCORE: z = (x - μ) / σ

SIGMOID: f'(x) = f(x)(1-f(x))
→ If f(x) = 0.4, f'(x) = 0.4 × 0.6 = 0.24

UPDATED MEAN: new_mean = (n×old_mean + new_value) / (n+1)

EXPONENTIAL: E(X)=1/λ, Var(X)=1/λ²

LINEAR ALGEBRA:
Discriminant < 0 → complex eigenvalues
Subspace test: span = always; Ax=0 = always; Ax=b (b≠0) = never
Projection: M²=M (idempotent)
Rank-1 matrix: one singular value = ||u||²

MACHINE LEARNING:
Naive Bayes parameters: 2K+1 for K binary features, 2 classes
SVM margin = 2/||w||
IG = Entropy(parent) - weighted Entropy(children)
Fisher LDA: SW⁻¹SBu = λu (generalized eigenvalue)

CALCULUS:
f'(x*)=0 and f''(x*)>0 → local minimum
f'(x*)=0 and f''(x*)<0 → local maximum
For piecewise: continuity + equal derivatives at boundaries
```

---

*GATE DS&AI 2024 | IISc Bangalore (First Edition) | Solutions for Suvam Das | WMT AI 2026*
