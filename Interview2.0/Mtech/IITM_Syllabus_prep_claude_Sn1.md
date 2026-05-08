# 🎯 IIT Madras Web M.Tech in AI — Complete Master Study Guide
### Goal: Clear the Qualifier Exam + Interview in ~1 Month | Designed for someone starting from scratch

> This guide consolidates the official IIT Madras Web M.Tech AI syllabus, real exam patterns from the IITM Industrial AI / Zanzibar program and the closely-aligned GATE DA (Data Science & AI) paper, and a structured roadmap for building math foundations from zero. Use it as your single source of truth.

---

## 📋 PART 0 — Exam Intelligence (What You're Actually Up Against)

### 0.1 Confirmed facts about the exam
Based on the official IIT Madras CODE brochure and the IIT Madras Zanzibar M.Tech Industrial AI screening test instructions (same program family, same syllabus):

| Item | Detail |
|---|---|
| Conducting body | IIT Madras CODE (Centre for Outreach and Digital Education) / Wadhwani School of Data Science & AI |
| Selection | Entrance test **and/or interview** (per official IIT Madras AI Web M.Tech announcement) |
| Mode | Computer-based, proctored — at designated exam centres |
| Duration | ~2 hours (per Zanzibar instructions for the same program) |
| Question types | **MCQ** (single correct), **MSQ** (multiple correct, all-or-nothing), **NAT** (Numerical Answer Type — type a number) |
| Negative marking | None confirmed for this program (NAT is always non-negative; MCQ/MSQ tend to be non-negative for this program) — attempt everything |
| Language | English |
| Calculator | On-screen scientific calculator typically provided |
| Subjects | Probability & Statistics, Linear Algebra, Optimization, Basic Machine Learning |

### 0.2 Topic weightage (estimated from the syllabus + comparable exams)
| Topic | Approximate share | Why this estimate |
|---|---|---|
| Probability & Statistics | 30–35% | Largest section in the syllabus; heavy in GATE DA |
| Linear Algebra | 25–30% | Core for AI/ML; eigenvalues + matrices appear repeatedly |
| Optimization | 10–15% | Smaller but high-yield; gradient descent always tested |
| Basic Machine Learning | 25–30% | Multiple sub-topics (LR, kNN, k-means, logistic, CV) |

### 0.3 What the questions actually look like
Three flavours dominate. Internalize each:

**Flavour 1 — "Plug & chug numeric"** (~40% of paper)
> "A fair coin is flipped twice and it is known that at least one tail is observed. The probability of getting two tails is ___."
> Answer: 1/3. (Conditional probability: P(TT|≥1T) = P(TT)/P(≥1T) = (1/4)/(3/4) = 1/3)

**Flavour 2 — "Concept check / which statement is true"** (~35% of paper)
> "Which of the following may help to reduce overfitting?
> (i) Change the loss function (ii) Reduce model complexity (iii) Increase training data (iv) Increase optimization steps"
> Answer: (i), (ii), (iii) — increasing optimization steps tends to *worsen* overfitting.

**Flavour 3 — "Apply algorithm by hand"** (~25% of paper)
> "Run one iteration of k-means on these 8 points with given centroids. Where is the new centroid C₃?"
> Answer requires walking through assignment + update once.

> 🎯 **Key implication for your prep:** Don't just read theory. For every concept, do at least 3–5 numerical problems by hand. The exam rewards procedural fluency, not memorized definitions.

### 0.4 The "and/or interview" part
The official press release explicitly states selection is via "entrance test **and/or interviews**." Past Industrial AI cohorts have had short faculty interviews for borderline candidates. Plan for a 15–20 minute interview where they will:
- Ask why you want this program
- Test 2–3 fundamental concepts from the syllabus (verbally, not numerically)
- Ask about your work and how you'd apply AI to it
- Possibly give a small reasoning puzzle

(Detailed interview prep is in Part 7.)

---

## 🗓️ PART 1 — The 1-Month Plan (28 Days)

> 6 days a week, 1 day rest. ~2 hours/day = 56 hours total. That is enough if every hour is focused.

### Phase 1 — Foundations (Days 1–7): Probability & Statistics
| Day | Focus |
|---|---|
| 1 | Probability basics, addition/multiplication rules, simple counting |
| 2 | Conditional probability, independence, tree diagrams |
| 3 | Bayes' theorem (do 10 problems — this is the #1 highest-yield topic) |
| 4 | Random variables, PMF, PDF, expectation |
| 5 | Mean, variance, std dev, distributions (uniform, binomial, normal) |
| 6 | CLT + hypothesis testing (t-test, z-test, chi-square, F-test — overview only) |
| 7 | **Mock test on Probability only**, review mistakes |

### Phase 2 — Foundations (Days 8–14): Linear Algebra
| Day | Focus |
|---|---|
| 8 | Vectors: addition, scalar multiplication, dot product, magnitude, distance |
| 9 | Matrices: multiplication, transpose, identity, special matrices |
| 10 | Rank, null space, linear independence (intuition first, then practice) |
| 11 | Solving Ax=b, pseudoinverse, least squares |
| 12 | Projections, orthogonality |
| 13 | Eigenvalues & eigenvectors (do 8 problems by hand) |
| 14 | **Mock test on Linear Algebra**, review mistakes |

### Phase 3 — Foundations (Days 15–21): Optimization + Basic ML
| Day | Focus |
|---|---|
| 15 | Univariate optimization (derivatives, max/min, second derivative test) |
| 16 | Multivariate optimization (partial derivatives, gradients) |
| 17 | Gradient descent + variants (Batch/SGD/Mini-batch), learning rate effects |
| 18 | Linear regression (least squares, closed-form solution) |
| 19 | Logistic regression + sigmoid + decision boundary |
| 20 | kNN, k-means clustering (work out 5 examples) |
| 21 | Cross-validation, train/test split, evaluation metrics (accuracy, precision, recall, F1, MSE, R²) |

### Phase 4 — Lock it in (Days 22–28): Revision + Mocks
| Day | Focus |
|---|---|
| 22 | Solve GATE DA 2024 sample paper (in this guide, Part 6) — full timed |
| 23 | Solve GATE DA 2024 actual paper (download from IISc website) |
| 24 | Solve GATE DA 2025 paper |
| 25 | Re-solve every question you got wrong from Days 22–24 |
| 26 | Solve all "Practice Question Banks" in Part 6 — timed |
| 27 | Light revision of formulas (Part 5) + interview preparation (Part 7) |
| 28 | **Rest day before exam.** Light formula sheet skim only. Sleep early. |

---

## 📘 PART 2 — PROBABILITY & STATISTICS (deep dive)

> 🧠 **Plain English first:** Probability = "how likely?", Statistics = "what does this data tell me?". Probability is the math; statistics is using that math on real-world numbers.

### 2.1 Counting (the hidden prerequisite)
Many probability problems hide a counting problem. Master these three first.

**Permutation P(n,r):** Arrangements of r things from n where order matters.
$$P(n,r) = \frac{n!}{(n-r)!}$$

**Combination C(n,r) or "n choose r":** Selections of r things from n where order does NOT matter.
$$C(n,r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$$

**Multiplication principle:** If task A has m ways and task B has n ways, doing both = m × n ways.

**Worked example:** From a deck of 52 cards, how many 5-card hands contain exactly 2 aces?
- Choose 2 aces from 4: C(4,2) = 6
- Choose 3 non-aces from 48: C(48,3) = 17,296
- Total = 6 × 17,296 = **103,776**

### 2.2 Probability axioms and basic rules

For any events A, B in sample space S:
1. **0 ≤ P(A) ≤ 1**
2. **P(S) = 1**
3. **P(A ∪ B) = P(A) + P(B)** if A and B are mutually exclusive
4. **P(A ∪ B) = P(A) + P(B) − P(A ∩ B)** in general (inclusion-exclusion)
5. **P(Aᶜ) = 1 − P(A)**  (complement)
6. **P(A ∩ B) = P(A) · P(B|A) = P(B) · P(A|B)** (multiplication)
7. **P(A ∩ B) = P(A) · P(B)** if A and B are independent

> ⚠️ **Common pitfall:** "Mutually exclusive" ≠ "Independent". Mutually exclusive events that both have non-zero probability are *never* independent (if one happens, the other can't, so they affect each other). Memorize this — it's tested.

### 2.3 Conditional probability & Bayes' theorem ⭐ (highest-yield topic)

**Conditional probability:**
$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

**Bayes' theorem:**
$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

**Total probability theorem (used to compute P(B) in the denominator):**
$$P(B) = P(B|A) P(A) + P(B|A^c) P(A^c)$$

**The classic medical-test problem (memorize the structure — it appears in every exam variant):**
> A disease affects 1% of people. A test is 99% accurate (both ways). You test positive. What's P(disease | positive)?
- P(D) = 0.01, P(D̄) = 0.99
- P(+|D) = 0.99, P(+|D̄) = 0.01
- P(+) = 0.99(0.01) + 0.01(0.99) = 0.0198
- P(D|+) = 0.99 × 0.01 / 0.0198 = **0.5 (50%)**

> 🎯 **Why this matters for AI:** Naive Bayes classifier, spam filtering, every "given an observation, what's the most likely class?" model uses Bayes.

**Box problem (another exam classic — GATE 2024 DA had a near-identical question):**
> Box A has 2 red, 3 blue. Box B has 4 red, 1 blue. Pick a box at random, draw a ball — it's red. P(came from A)?
- P(A)=P(B)=0.5; P(R|A) = 2/5, P(R|B) = 4/5
- P(R) = 0.5(2/5) + 0.5(4/5) = 1/5 + 2/5 = 3/5
- **P(A|R) = (2/5)(0.5) / (3/5) = 1/3**

### 2.4 Random variables, PMF, PDF, CDF

**Discrete RV → PMF (Probability Mass Function):** assigns a probability to each possible value.
- Conditions: each P(X=x) ≥ 0, and they sum to 1.

**Continuous RV → PDF (Probability Density Function):** a function f(x) where P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx.
- Conditions: f(x) ≥ 0 everywhere, and ∫ f(x) dx = 1 over all x.

**CDF (Cumulative Distribution Function):** F(x) = P(X ≤ x).
- For discrete: F(x) = sum of PMF up to x.
- For continuous: F(x) = ∫₋∞ˣ f(t) dt.
- Always non-decreasing, F(−∞) = 0, F(+∞) = 1.

**Expectation (mean) of X:**
- Discrete: E[X] = Σ x · P(X=x)
- Continuous: E[X] = ∫ x · f(x) dx

**Variance:**
$$\text{Var}(X) = E[(X - \mu)^2] = E[X^2] - (E[X])^2$$

**Useful properties:**
- E[aX + b] = a·E[X] + b
- Var(aX + b) = a²·Var(X)
- For independent X, Y: E[XY] = E[X]·E[Y], Var(X+Y) = Var(X) + Var(Y)

### 2.5 Common distributions to recognize on sight

**Bernoulli(p):** Single trial, success (1) with prob p or failure (0) with prob 1−p.
- E[X] = p, Var(X) = p(1−p)

**Binomial(n,p):** Number of successes in n independent Bernoulli trials.
$$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$$
- E[X] = np, Var(X) = np(1−p)
- *Worked example:* Toss fair coin 10 times. P(exactly 6 heads)? = C(10,6)·0.5⁶·0.5⁴ = 210 × 0.015625 × 0.0625 ≈ **0.205**

**Uniform(a,b) (continuous):** Equal density across [a,b].
- f(x) = 1/(b−a) for a ≤ x ≤ b
- E[X] = (a+b)/2, Var(X) = (b−a)²/12
- *Tested in GATE DA 2024:* "X is Uniform[0,1]. What is Var(X)?" → 1/12 ✓

**Normal(μ, σ²):** The bell curve.
- 68% within 1σ of mean, 95% within 2σ, 99.7% within 3σ
- z-score: z = (x − μ)/σ — converts any normal to standard normal N(0,1).

**Poisson(λ):** Number of rare events in fixed interval.
- P(X=k) = e^(−λ) λ^k / k!
- E[X] = Var(X) = λ

### 2.6 Sample statistics (statistics on data)

Given data x₁, x₂, ..., xₙ:
- **Sample mean:** x̄ = (Σxᵢ)/n
- **Sample variance:** s² = Σ(xᵢ − x̄)² / (n−1)   ← note the (n−1), not n, for unbiased estimator
- **Sample std dev:** s = √s²
- **Median:** middle value when sorted (avg of two middles if n is even)
- **Mode:** most frequent value
- **Range:** max − min
- **IQR (interquartile range):** Q3 − Q1
- **Correlation coefficient (Pearson):** r = Σ(xᵢ − x̄)(yᵢ − ȳ) / √[Σ(xᵢ − x̄)² · Σ(yᵢ − ȳ)²]
  - r ∈ [−1, 1]; r near ±1 = strong linear relationship; r near 0 = no linear relationship.

> 🎯 **Exam tip:** GATE DA 2024 asked the Pearson correlation coefficient between two columns. Be ready to compute it on a 5-row dataset by hand.

### 2.7 Central Limit Theorem (CLT)

> If X₁, X₂, ..., Xₙ are i.i.d. samples from any distribution with mean μ and variance σ², then for large n, the sample mean X̄ approximately follows N(μ, σ²/n).

**Implications:**
- The mean of many samples is normally distributed even if the underlying data isn't.
- Standard error of the mean = σ/√n. This is why bigger samples give tighter estimates.

### 2.8 Hypothesis testing

**The framework:**
1. State H₀ (null hypothesis — the "boring" claim) and H₁ (alternative).
2. Compute a test statistic from data.
3. Compute p-value (probability of seeing this data or more extreme under H₀).
4. If p < α (typically 0.05), reject H₀. Otherwise, fail to reject.

**Which test when:**
| Test | Use case |
|---|---|
| **z-test** | Compare a sample mean to known μ; large n (>30) or known σ |
| **t-test** | Same as z-test but small n with unknown σ; or compare two sample means |
| **chi-square (χ²)** | Test goodness-of-fit (does observed match expected?) or test independence in a contingency table |
| **F-test (ANOVA)** | Compare variances; test if 3+ group means differ |

**Two errors to memorize:**
- **Type I error:** Reject H₀ when it's true (false alarm). Probability = α.
- **Type II error:** Fail to reject H₀ when it's false (missed detection). Probability = β.
- **Power = 1 − β.**

> ⚠️ **Common trap:** "Failing to reject H₀" ≠ "Accepting H₀". You only ever conclude there's not enough evidence against H₀.

### 2.9 Practice problems — Probability & Statistics

**P1.** Two fair dice are rolled. Probability the sum is 7?
> 6 favorable / 36 = **1/6**

**P2.** P(A) = 0.4, P(B) = 0.5, P(A∩B) = 0.2. Are A and B independent?
> Independent iff P(A∩B) = P(A)·P(B) = 0.20. Yes, **independent**.

**P3.** A factory has 3 machines producing 50%, 30%, 20% of items, with defect rates 1%, 2%, 3%. An item is defective. P(it came from machine 3)?
> P(D) = 0.5(0.01) + 0.3(0.02) + 0.2(0.03) = 0.005 + 0.006 + 0.006 = 0.017
> P(M3|D) = 0.2(0.03)/0.017 = 0.006/0.017 ≈ **0.353**

**P4.** X ~ Uniform[0,4]. Find E[X] and Var(X).
> E[X] = (0+4)/2 = **2**; Var(X) = (4−0)²/12 = **16/12 = 4/3**

**P5.** A coin is biased with P(H) = 0.6. Tossed 4 times. P(exactly 2 heads)?
> C(4,2)·0.6²·0.4² = 6·0.36·0.16 = **0.3456**

**P6.** Sample mean of first 50 observations is 12. The 51st observation is 18. New mean?
> New sum = 50·12 + 18 = 618. New mean = 618/51 = **12.118 ≈ 12.12** *(GATE DA 2024 Q4)*

**P7.** Fair coin flipped twice. Given at least one tail observed, P(both tails)?
> Sample space given ≥1 T: {HT, TH, TT} (each 1/4 prior, total 3/4). P(TT|≥1T) = (1/4)/(3/4) = **1/3** *(GATE DA 2024 Q7)*

**P8.** B ⊂ A. Then P(B|A) compared to P(B)?
> P(B|A) = P(B∩A)/P(A) = P(B)/P(A). Since P(A) ≤ 1, P(B|A) ≥ P(B). Answer: **P(B|A) ≥ P(B)** *(GATE DA 2024 Q9)*


---

## 📗 PART 3 — LINEAR ALGEBRA (deep dive)

> 🧠 **Plain English first:** Linear algebra is the math of organizing many numbers into vectors and matrices, and operating on them in bulk. Every image, every dataset row, every neural-network weight is a vector or matrix. If you understand vectors and matrix multiplication, you understand 80% of why deep learning runs the way it does.

> 📺 **Single best free resource for visual intuition:** 3Blue1Brown's "Essence of Linear Algebra" YouTube series. 14 videos, ~3 hours total. If you watch nothing else, watch this. It builds the geometric picture that makes everything else click.

### 3.1 Vectors

A vector is an ordered list of numbers. Geometrically, it's an arrow from the origin.

```
v = [3, 4]         ← a 2D vector
w = [1, 2, 3]      ← a 3D vector
```

**Key operations:**

| Operation | Formula | Example |
|---|---|---|
| Addition | [a₁,a₂] + [b₁,b₂] = [a₁+b₁, a₂+b₂] | [1,2] + [3,4] = [4,6] |
| Scalar mult. | k·[a₁,a₂] = [ka₁, ka₂] | 3·[1,2] = [3,6] |
| Dot product | a·b = Σ aᵢbᵢ | [1,2]·[3,4] = 3+8 = 11 |
| Magnitude | ‖v‖ = √(Σ vᵢ²) | ‖[3,4]‖ = √25 = 5 |
| Distance | ‖a−b‖ = √(Σ (aᵢ−bᵢ)²) | between [1,2],[4,6] = √(9+16) = 5 |

**Critical fact:** Two non-zero vectors are **perpendicular (orthogonal)** if and only if their dot product is 0. *(GATE DA 2024 Q18 tested this.)*

**Cosine similarity** (used in NLP/ML):
$$\cos\theta = \frac{a \cdot b}{\|a\| \cdot \|b\|}$$

### 3.2 Matrices

An m × n matrix has m rows and n columns. Think of it as a transformation that takes vectors and produces other vectors.

**Matrix × vector** (this is what a neural-network layer does):

$$\begin{bmatrix}1 & 2 \\ 3 & 4\end{bmatrix} \begin{bmatrix}5 \\ 6\end{bmatrix} = \begin{bmatrix}1·5 + 2·6 \\ 3·5 + 4·6\end{bmatrix} = \begin{bmatrix}17 \\ 39\end{bmatrix}$$

**Matrix × matrix:** A(m×n) × B(n×p) = C(m×p). Each entry C[i][j] = (row i of A) · (column j of B).

**Properties to memorize:**
- Matrix multiplication is associative: (AB)C = A(BC)
- Matrix multiplication is **NOT commutative**: AB ≠ BA in general
- (AB)ᵀ = BᵀAᵀ ← swap order!
- (AB)⁻¹ = B⁻¹A⁻¹ when both inverses exist
- (Aᵀ)ᵀ = A
- Identity matrix I: AI = IA = A

**Determinant (for 2×2 matrix):**
$$\det\begin{bmatrix}a & b \\ c & d\end{bmatrix} = ad - bc$$

**Determinant (for 3×3 matrix) using cofactor expansion across row 1:**
$$\det\begin{bmatrix}a & b & c \\ d & e & f \\ g & h & i\end{bmatrix} = a(ei - fh) - b(di - fg) + c(dh - eg)$$

**Why determinant matters:**
- det(A) = 0 ⟺ A is singular (no inverse, has linearly dependent rows/columns)
- |det(A)| = volume scaling factor of the transformation
- det(AB) = det(A)·det(B)

### 3.3 Rank and null space

**Rank of A** = number of linearly independent rows = number of linearly independent columns.
- Rank tells you the "true dimension" of the space the matrix maps to.
- Maximum possible rank for an m×n matrix = min(m, n). This is "full rank".

**How to find rank quickly:** Apply row operations (Gaussian elimination) to reduce to row echelon form. Count non-zero rows.

**Example:**
$$A = \begin{bmatrix}1 & 2 & 3 \\ 2 & 4 & 6 \\ 0 & 1 & 2\end{bmatrix}$$
Row 2 = 2·Row 1, so it's redundant. Independent rows: Row 1 and Row 3. **Rank = 2.**

**Null space (kernel) of A:** all vectors x such that Ax = 0.
- If null space contains only the zero vector, columns are linearly independent.
- **Rank-nullity theorem:** rank(A) + nullity(A) = n (number of columns)

**The four fundamental subspaces** of an m×n matrix A:
1. **Column space** (range of A): spanned by columns of A — lives in ℝᵐ
2. **Null space** of A: solutions to Ax = 0 — lives in ℝⁿ
3. **Row space** (= column space of Aᵀ): lives in ℝⁿ
4. **Left null space** (= null space of Aᵀ): lives in ℝᵐ

**Key orthogonality facts** *(GATE DA 2024 Q38 tested this):*
- Row space ⊥ Null space ✓
- Column space ⊥ Left null space ✓
- (The other pairs are NOT orthogonal in general.)

### 3.4 Solving Ax = b

**Three cases:**
1. **Unique solution** when rank(A) = rank([A|b]) = n (number of unknowns)
2. **No solution** when rank(A) < rank([A|b])
3. **Infinitely many solutions** when rank(A) = rank([A|b]) < n

**Pseudoinverse (Moore-Penrose) A⁺:** generalizes the inverse to non-square / non-invertible matrices.
- Used to find the **best least-squares solution** when no exact solution exists.
- For a "tall" matrix A (m > n) with full column rank: A⁺ = (AᵀA)⁻¹Aᵀ
- This gives x* = A⁺b minimizing ‖Ax − b‖² — this is *exactly* the linear regression formula.

### 3.5 Projections

**Projection of b onto a vector a:**
$$\text{proj}_a(b) = \frac{a \cdot b}{\|a\|^2} \cdot a$$

**Projection onto a subspace spanned by columns of A:**
$$P = A(A^T A)^{-1}A^T$$
P is the projection matrix; Pb is the projection of b onto the column space of A.

**Why projections matter for ML:** Linear regression is geometrically the projection of y onto the column space of X. PCA is projection onto the directions of maximum variance.

### 3.6 Eigenvalues and eigenvectors ⭐⭐ (the most important LA topic for the exam)

For a square matrix A, an **eigenvector** v ≠ 0 and **eigenvalue** λ satisfy:
$$Av = \lambda v$$
i.e., the matrix doesn't rotate v — it just stretches/shrinks it by factor λ.

**Finding eigenvalues — the recipe:**
1. Solve **det(A − λI) = 0** — this is the characteristic polynomial.
2. The roots are your eigenvalues.

**Worked example (2×2):**
$$A = \begin{bmatrix}4 & 1 \\ 2 & 3\end{bmatrix}$$
$$\det(A - \lambda I) = (4-\lambda)(3-\lambda) - 2 = \lambda^2 - 7\lambda + 10 = 0$$
$$\lambda = 5 \text{ or } \lambda = 2$$

**Finding eigenvectors:** For each λ, solve (A − λI)v = 0.

For λ = 5 above: (A − 5I)v = 0 →
$$\begin{bmatrix}-1 & 1 \\ 2 & -2\end{bmatrix}\begin{bmatrix}x \\ y\end{bmatrix} = 0 \implies x = y \implies v = \begin{bmatrix}1 \\ 1\end{bmatrix}$$

**Critical shortcuts to memorize:**
1. **Sum of eigenvalues = trace(A)** = sum of diagonal entries
2. **Product of eigenvalues = det(A)**
3. For triangular matrices (upper or lower triangular), **eigenvalues = diagonal entries**
4. For symmetric matrices, eigenvalues are always real and eigenvectors are orthogonal

**GATE DA 2024 Q17 example (super common pattern):**
> H = [[9, −2], [−2, 6]]. One eigenvalue is 5. What's the other?
> trace = 9 + 6 = 15. So other eigenvalue = 15 − 5 = **10**. (Done in 5 seconds.)

**GATE DA 2024 Q25 example:**
> Two eigenvalues of a 3×3 matrix X are (1+i) and 2. Find det(X).
> Real matrices have complex eigenvalues in conjugate pairs, so the third eigenvalue is (1−i).
> det(X) = product = 2·(1+i)(1−i) = 2·(1−i²) = 2·2 = **4**.

**Why eigenvalues matter for AI:**
- **PCA:** Eigenvectors of the covariance matrix are the principal components; eigenvalues are the variance along each. Largest eigenvalue → most informative direction.
- **PageRank:** Google's original algorithm finds the dominant eigenvector of the link-graph matrix.
- **Stability of optimization:** Eigenvalues of the Hessian tell you whether you're at a minimum, maximum, or saddle point.

### 3.7 Special matrices to recognize

| Matrix type | Definition | Property |
|---|---|---|
| **Symmetric** | A = Aᵀ | Real eigenvalues, orthogonal eigenvectors |
| **Orthogonal** | AᵀA = I (so Aᵀ = A⁻¹) | Preserves length: ‖Ax‖ = ‖x‖ |
| **Idempotent** | A² = A | Eigenvalues are 0 or 1 (e.g., projection matrices) |
| **Diagonal** | All off-diagonal entries are 0 | Eigenvalues = diagonal entries |
| **Triangular** | Upper or lower zero-half | Eigenvalues = diagonal entries |
| **Positive definite** | xᵀAx > 0 for all x ≠ 0 | All eigenvalues > 0 |

### 3.8 Singular Value Decomposition (SVD) — bonus, but worth knowing

Any m×n matrix A can be written as **A = UΣVᵀ** where U is m×m orthogonal, V is n×n orthogonal, Σ is m×n with singular values σ₁ ≥ σ₂ ≥ … on the diagonal. Used in dimensionality reduction, recommender systems, and noise removal.

### 3.9 Practice problems — Linear Algebra

**LA1.** Compute [2, −1, 3] · [4, 2, −1].
> 2·4 + (−1)·2 + 3·(−1) = 8 − 2 − 3 = **3**

**LA2.** Find rank of [[1,2,3],[2,4,6],[0,1,2]].
> Row 2 = 2·Row 1. Row 3 is independent of Row 1. Rank = **2**.

**LA3.** Find eigenvalues of A = [[3,1],[0,2]].
> Triangular matrix. Eigenvalues = diagonal = **3, 2**.

**LA4.** Find eigenvalues of A = [[2,1],[1,2]].
> det(A−λI) = (2−λ)² − 1 = λ² − 4λ + 3 = 0 → λ = **3, 1**.

**LA5.** Trace of A is 7, det(A) is 12. A is 2×2. Eigenvalues?
> λ₁ + λ₂ = 7, λ₁·λ₂ = 12 → λ²−7λ+12 = 0 → **λ = 3, 4**.

**LA6.** ‖[1, 2, 2]‖ = ?
> √(1+4+4) = √9 = **3**.

**LA7.** Are [1,1] and [1,−1] orthogonal?
> Dot = 1·1 + 1·(−1) = 0. **Yes, orthogonal.**

**LA8.** A is 3×3 with eigenvalues 1, −1, 3. Find trace(A³ − 3A²).
> Eigenvalues of A³ − 3A² are λ³ − 3λ² for each λ.
> = 1³−3·1² = −2; (−1)³−3(−1)² = −4; 3³−3·3² = 0
> Trace = −2 + (−4) + 0 = **−6** *(GATE DA 2024 Q48)*

**LA9.** Matrix [[0,1,0],[a,2,d],[b,3,c]] cannot have which rank?
> Row 1 has only one non-zero entry → at least rank 1. Three rows means max rank 3. By varying a,b,c,d, we can achieve ranks 1, 2, or 3. The matrix **cannot have rank 0** because it's not the zero matrix. *(GATE DA 2024 Q39)*

**LA10.** H = [[3,−1],[−1,3]]. One eigenvector is [−1,−1]. Find the other.
> Symmetric matrix → eigenvectors orthogonal. A vector orthogonal to [−1,−1] is [1,−1]. **Answer: [1,−1].** *(GATE DA 2024 Q37)*

---

## 📙 PART 4 — OPTIMIZATION (deep dive)

> 🧠 **Plain English first:** Optimization = "find the input that makes some function as small (or big) as possible." In machine learning, the function is "how wrong is my model?", and we want to minimize it. Almost every ML algorithm is, at its core, an optimization problem.

### 4.1 Types of optimization

| Type | Meaning |
|---|---|
| **Unconstrained** | x can be any real number/vector |
| **Constrained** | x must satisfy g(x) ≤ 0 or h(x) = 0 |
| **Convex** | f is bowl-shaped (a line between any 2 points on the graph stays above the graph) — has only one minimum |
| **Non-convex** | f has multiple local minima — gradient descent may get stuck |

> 🎯 **Why convexity matters:** Linear regression and logistic regression are convex (one minimum, gradient descent always finds it). Deep neural networks are non-convex (many local minima — that's why training is hard).

### 4.2 Univariate optimization

To find min/max of f(x):
1. Compute f'(x) and solve f'(x) = 0 → critical points.
2. Use the second derivative test:
   - **f''(x) > 0** → local **minimum** (smile shape ⌣)
   - **f''(x) < 0** → local **maximum** (frown shape ⌢)
   - **f''(x) = 0** → inconclusive, check further

**Worked example:** Minimize f(x) = x² − 4x + 5
- f'(x) = 2x − 4 = 0 → x = 2
- f''(x) = 2 > 0 → minimum
- f(2) = 4 − 8 + 5 = **1**

**GATE DA 2024 Q19 example:**
> f(x) = 1 + x + x² has what at x = −0.5?
> f'(x) = 1 + 2x = 0 → x = −0.5. f''(x) = 2 > 0 → **minimum at x = −0.5**.

### 4.3 Multivariate optimization

For f(x₁, x₂, ..., xₙ):
1. Compute the **gradient** ∇f = [∂f/∂x₁, ..., ∂f/∂xₙ].
2. Set ∇f = 0 (every partial derivative = 0).
3. Solve the system to find critical points.
4. Use the **Hessian matrix** (matrix of second partial derivatives) to classify:
   - All eigenvalues of H > 0 → minimum
   - All eigenvalues of H < 0 → maximum
   - Mixed signs → saddle point

**Partial derivatives 101:** Treat all other variables as constants.

For f(x,y) = x² + 3xy + y²:
- ∂f/∂x = 2x + 3y
- ∂f/∂y = 3x + 2y

### 4.4 Gradient Descent ⭐⭐ (the heart of ML)

**The intuition:** You're blindfolded on a hill, and you want to walk down to the valley. You feel the slope under your feet (the gradient) and take a small step in the *opposite* direction. Repeat.

**Algorithm:**
```
Start at x₀ (any starting point)
Repeat until convergence:
    x_new = x_old − α · ∇f(x_old)
```
Where:
- **α (alpha)** = learning rate (step size)
- **∇f** = gradient (direction of steepest *increase*; we go opposite to descend)

**Choosing α:**
| Learning rate | Behavior |
|---|---|
| Too small | Very slow convergence — takes forever |
| Just right | Converges smoothly to minimum |
| Too large | Overshoots the minimum, may oscillate or diverge |

> 🎯 **Common practice:** Try learning rates like 0.1, 0.01, 0.001 — pick the one with smoothest decrease in loss.

**Variants of gradient descent:**
| Variant | Update rule | Pros / Cons |
|---|---|---|
| **Batch GD** | Use entire dataset for each step | Stable, but slow & memory-hungry |
| **Stochastic GD (SGD)** | One random sample per step | Fast, but noisy updates |
| **Mini-batch GD** | Small batch (e.g., 32 samples) | Best of both — used in practice |

**Other modern optimizers** (good to know names): **Momentum**, **RMSProp**, **Adam** (combines momentum + RMSProp; default for deep learning).

### 4.5 Convexity and global vs local minima

A function is **convex** if for any two points a, b and any t ∈ [0,1]:
$$f(ta + (1-t)b) \leq t f(a) + (1-t) f(b)$$
i.e., the line segment between any two points on the graph stays above the graph.

**Critical theorem:** For a **convex function**, every local minimum is a global minimum. *(GATE DA 2024 Q35: "All convex functions have a global minimum" — be careful, this is **false** in general because the function might be unbounded below, like f(x) = x. The correct statement is: every local min IS a global min for a convex function, but a global min may not exist.)*

> ⚠️ **Trap:** Convexity guarantees no spurious local minima, NOT that a minimum exists. f(x) = x is convex but has no minimum.

### 4.6 Practice problems — Optimization

**O1.** Minimize f(x) = (x − 3)² + 5.
> f'(x) = 2(x − 3) = 0 → x = 3. f''(x) = 2 > 0 → minimum. Min value = **5**.

**O2.** f(x,y) = x² + y² − 4x − 6y + 13. Find the minimum.
> ∂f/∂x = 2x − 4 = 0 → x = 2; ∂f/∂y = 2y − 6 = 0 → y = 3. f(2,3) = 4 + 9 − 8 − 18 + 13 = **0**.

**O3.** Run 1 step of gradient descent on f(x) = x² starting at x = 5 with α = 0.1.
> ∇f = 2x = 10 at x=5. x_new = 5 − 0.1·10 = **4**.

**O4.** Maximize f(x) = xe·e⁻ˣ for x ≥ 0. (GATE DA 2024 Q54)
> Let g(x) = xᵉ·e⁻ˣ where e ≈ 2.718. ln g = e·ln x − x. d/dx(ln g) = e/x − 1 = 0 → x = e ≈ **2.72**.

---

## 📕 PART 5 — BASIC MACHINE LEARNING (deep dive)

> 🧠 **Plain English first:** Machine learning = teaching a computer to find patterns in data so it can make predictions or decisions on new data — without being explicitly programmed for the specific task.

### 5.1 The big map: what kind of problem is this?

```
Do you have labels (correct answers)?
├── Yes (Supervised Learning)
│   ├── Predict a number → Regression (Linear, Polynomial, Ridge)
│   └── Predict a category → Classification (Logistic Regression, kNN, Decision Tree, Naive Bayes, SVM)
│
├── No (Unsupervised Learning)
│   ├── Group similar things → Clustering (k-means, hierarchical)
│   └── Reduce dimensions → PCA, t-SNE
│
└── Learn by trial and reward → Reinforcement Learning
```

### 5.2 Core ML vocabulary you must know

| Term | Meaning |
|---|---|
| **Feature (input variable, X)** | What the model sees |
| **Target / Label (output, y)** | What the model predicts |
| **Training set** | Data used to fit the model |
| **Validation set** | Data used to tune hyperparameters |
| **Test set** | Held-out data used only to evaluate final model |
| **Hyperparameter** | A knob you set before training (e.g., k in kNN, learning rate) |
| **Parameter** | What the model learns (e.g., β in linear regression) |
| **Loss function** | A number measuring how wrong the model is |
| **Bias** | Error from oversimplification (model too simple) |
| **Variance** | Error from being too sensitive to training data noise |
| **Overfitting** | Low training error, high test error (memorized noise) |
| **Underfitting** | High training and high test error (too simple) |
| **Generalization** | How well the model performs on unseen data |
| **Regularization** | Adding a penalty for complexity to prevent overfitting (e.g., L1/Lasso, L2/Ridge) |

### 5.3 Bias-variance tradeoff ⭐ (favorite exam topic)

```
Total error = Bias² + Variance + Irreducible noise
```

| Model | Bias | Variance |
|---|---|---|
| Linear regression on a curve | High (too simple) | Low |
| Deep neural net on a few points | Low | High (memorizes) |
| kNN with k=1 | Low | High |
| kNN with k=large | High | Low |

> 🎯 **Common exam question:** "Increasing regularization in ridge regression — what happens to bias and variance?"
> Answer: **Bias increases (or stays same), variance decreases.** *(GATE DA 2024 Q12 had this exact question.)*

### 5.4 Linear Regression ⭐

**Goal:** Predict continuous y from features X.

**Simple linear regression (one feature):**
$$\hat{y} = \beta_0 + \beta_1 x$$

**Multiple linear regression:**
$$\hat{y} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_n x_n = X\beta$$
(where X has a column of 1s for the intercept).

**Loss function — Sum of Squared Errors (SSE):**
$$\text{SSE} = \sum (y_i - \hat{y}_i)^2$$

**Closed-form solution (the "normal equation"):**
$$\beta = (X^T X)^{-1} X^T y$$
This is the pseudoinverse formula — it's the same calculation as projecting y onto the column space of X.

**Assumptions of linear regression (commonly tested):**
1. Linear relationship between X and y
2. Independent errors
3. Constant variance of errors (homoscedasticity)
4. Normally distributed errors
5. Little or no multicollinearity (features not strongly correlated with each other)

**Worked example:** Hours studied (x) vs marks (y). x: [1,2,3,4,5], y: [50,55,65,70,80].
- x̄ = 3, ȳ = 64
- β₁ = Σ(xᵢ−x̄)(yᵢ−ȳ) / Σ(xᵢ−x̄)² = (−2·−14 + −1·−9 + 0·1 + 1·6 + 2·16) / (4+1+0+1+4) = (28+9+0+6+32)/10 = 75/10 = **7.5**
- β₀ = ȳ − β₁·x̄ = 64 − 7.5·3 = **41.5**
- For x=6: ŷ = 41.5 + 7.5·6 = **86.5**

### 5.5 Regularized regression

**Ridge regression (L2):** Adds penalty λ·Σβᵢ² to SSE.
- Shrinks coefficients toward zero (but rarely makes them exactly 0).
- Always has a closed-form solution: β = (XᵀX + λI)⁻¹Xᵀy.

**Lasso regression (L1):** Adds penalty λ·Σ|βᵢ| to SSE.
- Can shrink coefficients to *exactly* zero — performs feature selection.

> 🎯 **Effect of increasing λ:** more regularization → simpler model → bias goes up, variance goes down.

### 5.6 Logistic Regression ⭐

> Despite the name, this is a **classification** algorithm.

**The idea:** Output a probability between 0 and 1 using the **sigmoid function**:
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$
where z = β₀ + β₁x₁ + ... + βₙxₙ.

- σ(z) > 0.5 → predict class 1
- σ(z) < 0.5 → predict class 0
- The decision boundary is where z = 0, i.e., a linear boundary in feature space.

**Loss: Cross-entropy (log loss)**
$$L = -[y \log(\hat{y}) + (1-y) \log(1-\hat{y})]$$

This loss is convex in β, so gradient descent always finds the global minimum.

**Sigmoid quick values to memorize:**
- σ(0) = 0.5
- σ(∞) = 1
- σ(−∞) = 0
- σ'(z) = σ(z)(1 − σ(z)) ← elegant derivative, used in backprop

### 5.7 k-Nearest Neighbours (kNN) ⭐

**Algorithm (lazy learning — no training!):**
1. Store all training data.
2. To classify a new point: find its k closest training points by some distance metric (usually Euclidean).
3. Take the majority vote (classification) or average (regression).

**Effect of k:**
- **k = 1:** very flexible, low bias, high variance (overfits).
- **k = large:** smoother decision boundary, high bias, low variance (may underfit).
- **Best k:** found via cross-validation. Often k = √n is a starting heuristic.

**Critical preprocessing requirement:** Always **standardize** features (subtract mean, divide by std). Without this, large-magnitude features dominate the distance metric.

**Pros:** Simple, no training time, works for non-linear boundaries.
**Cons:** Slow at prediction time (O(n) per query); suffers from "curse of dimensionality" in high dimensions.

### 5.8 k-Means Clustering ⭐

**Goal:** Group n unlabelled data points into k clusters.

**Algorithm:**
1. **Initialize:** Pick k centroids (e.g., randomly from data points).
2. **Assignment step:** Assign each point to the nearest centroid.
3. **Update step:** Recompute each centroid as the mean of points assigned to it.
4. **Repeat** steps 2–3 until centroids stop moving (convergence).

> 🎯 **k-means is an Expectation-Maximization (EM) algorithm**: assignment is the E-step, centroid update is the M-step. *(GATE DA 2024 Q42 used this exact phrasing.)*

**Choosing k — the elbow method:** Plot total within-cluster sum-of-squares vs k. Pick the "elbow" where adding more clusters stops helping much.

**Limitations:**
- Sensitive to initial centroids (run multiple times with random starts; "k-means++" is a smart initialization).
- Assumes spherical clusters of similar size.
- Must specify k in advance.

**Worked example:** Data points: 1, 2, 8, 9, 10. k=2. Initial centroids: 1 and 8.
- Round 1 assignment: {1,2} to centroid 1; {8,9,10} to centroid 8.
- Update: new centroids = mean(1,2) = 1.5; mean(8,9,10) = 9.
- Round 2 assignment: same. Converged.
- **Final clusters:** {1,2} and {8,9,10}.

### 5.9 Cross-validation ⭐

**Why:** A single train/test split gives a noisy performance estimate. Cross-validation gives a stable, less-biased estimate.

**k-fold cross-validation:**
1. Split data into k equal folds.
2. For each fold i: train on the other k−1 folds, evaluate on fold i.
3. Average the k scores.

**Standard choices:** k = 5 or 10.

**Leave-One-Out (LOO):** k = n. Most thorough but most expensive — typically only used for tiny datasets.

**Stratified k-fold:** for classification, ensures each fold has the same class proportions as the full dataset. Use this when classes are imbalanced.

> 🎯 **Common exam trap:** "We have a 5% positive class. Our model has 95% accuracy on a single test set." *Sounds great — but a model that always predicts "negative" gets 95% accuracy too!* For imbalanced data, prefer **AUC-ROC** or **F1**, and prefer cross-validation over a single split. *(GATE DA 2024 Q11 directly tested this.)*

### 5.10 Evaluation metrics

**For classification — confusion matrix:**

|  | Predicted + | Predicted − |
|---|---|---|
| Actual + | TP | FN |
| Actual − | FP | TN |

| Metric | Formula | Meaning |
|---|---|---|
| **Accuracy** | (TP+TN)/(TP+TN+FP+FN) | Fraction of correct predictions |
| **Precision** | TP/(TP+FP) | Of those predicted +, how many are really +? |
| **Recall (Sensitivity, TPR)** | TP/(TP+FN) | Of all real +, how many did we catch? |
| **Specificity (TNR)** | TN/(TN+FP) | Of all real −, how many did we identify? |
| **F1 Score** | 2·P·R/(P+R) | Harmonic mean of precision and recall |
| **AUC-ROC** | Area under ROC curve | Overall ranking quality; ≥0.5 (random); 1 = perfect |

**Worked example:** TP=40, TN=30, FP=10, FN=20.
- Accuracy = 70/100 = **0.70**
- Precision = 40/50 = **0.80**
- Recall = 40/60 ≈ **0.667**
- F1 = 2·0.8·0.667/(0.8+0.667) ≈ **0.727**

**For regression:**
| Metric | Formula | Notes |
|---|---|---|
| **MSE** | (1/n)Σ(yᵢ−ŷᵢ)² | Penalizes large errors heavily |
| **RMSE** | √MSE | Same units as y |
| **MAE** | (1/n)Σ\|yᵢ−ŷᵢ\| | Less sensitive to outliers |
| **R²** | 1 − SS_res/SS_tot | Fraction of variance explained; 1 = perfect, 0 = no better than mean |

### 5.11 Quick-fire ML facts (memorize these)

- **Decision tree** that achieves 100% training accuracy ≠ other classifiers on same data will. *(GATE DA 2024 Q13)*
- **PCA** on perfectly spherical 2D data: ANY pair of orthonormal vectors is a valid pair of principal components, because all directions have equal variance. *(GATE DA 2024 Q30)*
- **Naive Bayes** assumes features are conditionally independent given the class. Fast, often surprisingly accurate.
- **SVM** finds the maximum-margin separator. Linear-kernel SVM = logistic-regression-like decision boundary.
- **MLP / Feedforward NN parameter count** = (input_dim + 1) × hidden + (hidden + 1) × output. The "+1" is for bias terms.
  - *Example:* input=5, hidden=10, output=3 → (5+1)·10 + (10+1)·3 = 60 + 33 = **93 parameters**. *(GATE DA 2024 Q43)*

### 5.12 Practice problems — Machine Learning

**ML1.** Confusion matrix has TP=80, FN=20, FP=10, TN=90. Find precision, recall, F1.
> Precision = 80/90 ≈ 0.889; Recall = 80/100 = 0.80; F1 = 2·0.889·0.80/(0.889+0.80) ≈ **0.842**.

**ML2.** kNN classification with k=3, neighbours labelled [Pos, Neg, Pos]. Class?
> Majority vote: 2 Pos, 1 Neg → **Positive**.

**ML3.** k-means with data [2,4,10,12,3,11], initial centroids 2 and 10. After 1 iteration, what are the centroids?
> Distances: 2→2 closest, 4→2 (dist 2 vs 6), 10→10, 12→10 (dist 2 vs 10), 3→2, 11→10.
> Cluster 1: {2,4,3} → mean = 3. Cluster 2: {10,12,11} → mean = 11. **Centroids: 3 and 11.**

**ML4.** Increasing the regularization parameter λ in ridge regression: (i) what happens to bias? (ii) variance?
> Bias increases or stays the same; variance decreases. **(i) up, (ii) down.**

**ML5.** A model gets 95% accuracy on a dataset where only 5% of cases are positive. Is this impressive?
> No — the trivial model predicting "always negative" gets 95%. Look at recall, precision, AUC instead.

**ML6.** Build an MLP with 1 hidden layer of 8 neurons, input dim 4, output dim 2. How many trainable parameters?
> Layer 1: (4+1)·8 = 40. Layer 2: (8+1)·2 = 18. Total = **58**.


---

## 🔑 PART 6 — FORMULA SHEET (Print This Page)

> Skim this every morning. The day before the exam, this is the *only* thing to read.

### Probability
```
P(A∪B) = P(A) + P(B) − P(A∩B)
P(A|B) = P(A∩B) / P(B)
P(A∩B) = P(A) · P(B)            [if independent]
Bayes:  P(A|B) = P(B|A)·P(A) / P(B)
Total:  P(B) = P(B|A)P(A) + P(B|Aᶜ)P(Aᶜ)
Binomial: P(X=k) = C(n,k) p^k (1−p)^(n−k)    [E=np, Var=np(1−p)]
Bernoulli: E=p, Var=p(1−p)
Uniform[a,b]: E=(a+b)/2, Var=(b−a)²/12
Poisson(λ): P(X=k) = e^(−λ) λ^k / k!  [E=Var=λ]
```

### Statistics
```
Mean μ = (Σxᵢ)/n
Sample variance s² = Σ(xᵢ−x̄)² / (n−1)         ← (n−1), not n
Population variance σ² = Σ(xᵢ−μ)² / n
Std dev σ = √variance
z-score:    z = (x − μ) / σ
t-statistic: t = (x̄ − μ₀) / (s/√n)
SE of mean: σ/√n  (CLT)
Pearson r = Σ(xᵢ−x̄)(yᵢ−ȳ) / √[Σ(xᵢ−x̄)² · Σ(yᵢ−ȳ)²]
```

### Linear Algebra
```
Magnitude: ‖v‖ = √(v₁² + v₂² + … + vₙ²)
Dot product: a·b = Σ aᵢbᵢ
Cosine similarity: a·b / (‖a‖·‖b‖)
Det 2×2: |a b; c d| = ad − bc
Inverse 2×2: 1/det · [d −b; −c a]
Eigenvalues: solve det(A − λI) = 0
   • Sum of λ = trace(A)
   • Product of λ = det(A)
   • Triangular matrix: eigenvalues = diagonal entries
Projection of b onto a: (a·b / ‖a‖²) · a
Least squares: β = (XᵀX)⁻¹ Xᵀy
Ridge: β = (XᵀX + λI)⁻¹ Xᵀy
Rank-Nullity: rank(A) + nullity(A) = n
(AB)ᵀ = BᵀAᵀ;   (AB)⁻¹ = B⁻¹A⁻¹
```

### Optimization
```
1D minimum: f'(x) = 0 AND f''(x) > 0
Multivar minimum: ∇f = 0 AND Hessian eigenvalues all > 0
Gradient descent: x_new = x_old − α · ∇f(x_old)
Convex function: every local min is a global min
```

### Machine Learning
```
Sigmoid: σ(z) = 1/(1+e⁻ᶻ);  σ'(z) = σ(z)(1−σ(z))
Logistic loss: L = −[y log ŷ + (1−y) log(1−ŷ)]
Linear regression β: (XᵀX)⁻¹Xᵀy
Euclidean distance: √Σ(pᵢ−qᵢ)²
Total error = Bias² + Variance + Irreducible noise

Confusion matrix (rows = actual, cols = predicted):
        Pred+  Pred−
Actual+  TP     FN
Actual−  FP     TN

Accuracy = (TP+TN)/total
Precision = TP/(TP+FP)
Recall = TP/(TP+FN)
F1 = 2·P·R/(P+R)
MSE = (1/n)Σ(yᵢ−ŷᵢ)²
R² = 1 − SS_res/SS_tot

MLP params: Σ over layers (in+1) × out
```

---

## 🧪 PART 7 — Comprehensive Practice Question Bank

> 50+ exam-style questions modelled directly on the IIT Madras WMT AI syllabus and the closely-aligned GATE DA 2024 paper. Solve them on paper, time yourself (~2 min per question average).

### Section A — Probability & Statistics (20 Qs)

**Q1.** P(A) = 0.6, P(B) = 0.4, P(A∩B) = 0.24. Are A and B independent?
> P(A)·P(B) = 0.24 = P(A∩B). **Yes, independent.**

**Q2.** A box has 5 red and 5 blue balls. Two are drawn without replacement. P(both red)?
> (5/10)·(4/9) = **20/90 = 2/9 ≈ 0.222**

**Q3.** A fair die rolled twice. P(sum > 9)?
> Favorable sums: 10 (4 ways), 11 (2 ways), 12 (1 way) → 7 ways. P = **7/36**

**Q4.** Disease prevalence 2%. Test sensitivity 95%, specificity 90%. Person tests +. P(disease)?
> P(D)=0.02, P(+|D)=0.95, P(+|D̄)=0.10. P(+) = 0.02·0.95 + 0.98·0.10 = 0.019 + 0.098 = 0.117. P(D|+) = 0.019/0.117 ≈ **0.162 (16.2%)**

**Q5.** X ~ Binomial(5, 0.4). P(X = 2)?
> C(5,2)·0.4²·0.6³ = 10·0.16·0.216 ≈ **0.3456**

**Q6.** X ~ Uniform(2, 8). E[X] and Var(X)?
> E = (2+8)/2 = **5**; Var = (8−2)²/12 = **3**

**Q7.** Sample data: 4, 7, 8, 11, 10. Mean and sample variance?
> Mean = 40/5 = **8**. Deviations: −4, −1, 0, 3, 2. Squared: 16, 1, 0, 9, 4. Sum = 30. Sample variance = 30/(5−1) = **7.5**.

**Q8.** A coin is tossed 4 times. P(at least one head)?
> 1 − P(no heads) = 1 − (0.5)⁴ = 1 − 1/16 = **15/16**

**Q9.** Data follows N(50, 100). Find P(X > 70).
> z = (70−50)/10 = 2. P(Z > 2) ≈ **0.0228** (from standard normal table)

**Q10.** A student's score is 1.5 std dev above class mean. What percentile (approx)?
> z = 1.5. P(Z < 1.5) ≈ 0.9332. **≈ 93rd percentile.**

**Q11.** P(A) = 0.5, P(B|A) = 0.3, P(B|Aᶜ) = 0.6. Find P(B) and P(A|B).
> P(B) = 0.5·0.3 + 0.5·0.6 = **0.45**. P(A|B) = 0.15/0.45 = **1/3**

**Q12.** X has PDF f(x) = 2x for 0 ≤ x ≤ 1. Find E[X].
> E[X] = ∫₀¹ x·2x dx = ∫₀¹ 2x² dx = [2x³/3]₀¹ = **2/3**

**Q13.** Correlation between X and Y is 0. Are X and Y independent?
> Not necessarily. Zero correlation only means no *linear* relationship. Independence implies zero correlation, but not vice versa.

**Q14.** A fair coin is flipped until the first head appears. P(it takes more than 3 flips)?
> P(no head in first 3) = (1/2)³ = **1/8**

**Q15.** Among 1000 students, 60% are male, 40% female. 30% of males and 20% of females wear glasses. A randomly chosen student wears glasses. P(female)?
> P(G) = 0.6·0.3 + 0.4·0.2 = 0.18 + 0.08 = 0.26. P(F|G) = 0.08/0.26 ≈ **0.308**

**Q16.** Sample mean = 30, σ = 10, n = 100. 95% confidence interval for population mean?
> SE = σ/√n = 1. CI = 30 ± 1.96·1 = **(28.04, 31.96)**

**Q17.** Two independent random variables X and Y both ~ N(0,1). Find Var(X − 2Y).
> Var(X) + 4·Var(Y) = 1 + 4 = **5**

**Q18.** Roll a fair die. Let X = number on top. Find E[X²].
> E[X²] = (1+4+9+16+25+36)/6 = 91/6 ≈ **15.17**

**Q19.** A test has Type I error rate α = 0.05, power = 0.80. What's the Type II error rate?
> β = 1 − power = **0.20**

**Q20.** B ⊂ A, P(A) = 0.8, P(B) = 0.3. Find P(A | B).
> Since B ⊂ A, B happening means A happens automatically. P(A|B) = **1**.

### Section B — Linear Algebra (15 Qs)

**Q21.** A = [[2,3],[1,4]]. Find det(A) and A⁻¹.
> det = 8 − 3 = 5. A⁻¹ = (1/5)·[[4,−3],[−1,2]] = **[[0.8,−0.6],[−0.2,0.4]]**

**Q22.** Find the rank of A = [[1,2,3],[4,5,6],[7,8,9]].
> R3 − 2·R2 + R1 = 0. So rows are dependent. Row reduce: R2 − 4·R1 = [0,−3,−6]; R3 − 7·R1 = [0,−6,−12] = 2·R2_new. Rank = **2**.

**Q23.** v = [3, 4, 12]. Find ‖v‖ and the unit vector.
> ‖v‖ = √(9+16+144) = √169 = **13**. Unit vector = v/13 = **[3/13, 4/13, 12/13]**.

**Q24.** Eigenvalues of [[2,0,0],[1,3,0],[4,5,6]]?
> Lower triangular → eigenvalues = diagonal = **2, 3, 6**

**Q25.** Eigenvalues of A = [[5,4],[1,2]]?
> det(A−λI) = (5−λ)(2−λ) − 4 = λ² − 7λ + 6 = 0 → **λ = 6, 1**

**Q26.** A is 3×3 with trace 6 and det 0. One eigenvalue is 4. Find the others.
> Sum: λ₁+λ₂+4 = 6 → λ₁+λ₂ = 2. Product: λ₁·λ₂·4 = 0 → at least one is 0. So λ₁=0, λ₂=2. Eigenvalues: **0, 2, 4**.

**Q27.** Find Aᵀ if A = [[1,2,3],[4,5,6]].
> **Aᵀ = [[1,4],[2,5],[3,6]]**

**Q28.** Solve Ax = b where A=[[1,1],[2,3]], b=[3,8].
> det(A) = 1. x = A⁻¹b = [[3,−1],[−2,1]]·[3,8] = [3·3 − 1·8, −2·3 + 1·8] = **[1, 2]**

**Q29.** Two vectors u = [1,2,2], v = [2,−2,1]. Are they orthogonal?
> u·v = 2 − 4 + 2 = 0. **Yes.**

**Q30.** Find projection of b = [4,3] onto a = [1,0].
> proj = (a·b/‖a‖²)·a = 4·[1,0] = **[4, 0]**

**Q31.** A 4×3 matrix has rank 3. What is its nullity?
> Rank-nullity: nullity = n − rank = 3 − 3 = **0**

**Q32.** A symmetric matrix has eigenvalues 2, 5, 8. What is its determinant?
> Product of eigenvalues = **80**

**Q33.** Find AB if A=[[1,2],[3,4]], B=[[2,0],[1,2]].
> AB = [[1·2+2·1, 1·0+2·2],[3·2+4·1, 3·0+4·2]] = **[[4,4],[10,8]]**

**Q34.** If A is orthogonal and 3×3, what is det(A)?
> AAᵀ = I → det(A)² = 1 → det(A) = **±1**

**Q35.** A is a projection matrix (A² = A). Possible eigenvalues?
> If Av = λv then A²v = λ²v = Av = λv → λ² = λ → λ = **0 or 1**.

### Section C — Optimization (8 Qs)

**Q36.** Minimize f(x) = x² − 6x + 11.
> f'(x) = 2x − 6 = 0 → x = 3. f''=2>0 → min. f(3) = **2**.

**Q37.** Find critical points of f(x,y) = x² + y² − 2x + 4y.
> ∂f/∂x = 2x − 2 = 0; ∂f/∂y = 2y + 4 = 0. → (x, y) = **(1, −2)**. Hessian = [[2,0],[0,2]], both eigenvalues > 0 → minimum. f(1,−2) = 1+4−2−8 = **−5**.

**Q38.** One step of GD on f(x) = x² + 4x starting at x = 1, α = 0.2. New x?
> ∇f = 2x+4 = 6 at x=1. x_new = 1 − 0.2·6 = **−0.2**.

**Q39.** True or False: A non-convex function may have multiple local minima.
> **True.** That's the defining feature.

**Q40.** True or False: If learning rate is too large, gradient descent always converges faster.
> **False.** It can overshoot, oscillate, or diverge.

**Q41.** Convex combination of f and g (f, g convex) is also convex. T/F?
> **True.** Sum and non-negative scalar multiplications of convex functions are convex.

**Q42.** Maximum of f(x) = −x² + 4x − 3.
> f'(x) = −2x+4 = 0 → x=2. f''=−2<0 → max. f(2) = **1**.

**Q43.** Mini-batch GD with batch size 32 on a dataset of 6400 examples. How many gradient updates per epoch?
> 6400/32 = **200**.

### Section D — Machine Learning (12 Qs)

**Q44.** Decision tree achieves 100% training accuracy. Will it always generalize well?
> **No.** Likely overfitting. Validate on test data.

**Q45.** Ridge regression coefficient λ → ∞. What happens to all βᵢ?
> All βᵢ → 0 (model becomes the mean predictor).

**Q46.** Increasing k in kNN: bias increases or decreases?
> **Bias increases** (smoother decision boundary, model gets simpler).

**Q47.** A binary classifier gives equal probability 0.5 to each test point. AUC?
> **0.5** (random performance).

**Q48.** k-means iteration on points: [1,2,9,10] with initial centroids 1 and 10.
> Round 1 assignment: {1,2} → 1; {9,10} → 10. Update: centroids = 1.5 and 9.5. Converged: {1,2} and {9,10}.

**Q49.** A model has bias = 0.05, variance = 0.10, noise = 0.02. Expected test error?
> 0.05² + 0.10 + 0.02 = 0.0025 + 0.10 + 0.02 = **0.1225**

**Q50.** True or False: Increasing training data tends to reduce variance.
> **True.**

**Q51.** Logistic regression output for input z = β₀ + β₁x₁ + β₂x₂. If z = 0, predicted class?
> σ(0) = 0.5, exactly on the boundary. Convention: usually predict class 1 (or tie-break by another rule).

**Q52.** A confusion matrix has 100 actual positives and 200 actual negatives. Model predicts 150 positives total, of which 80 are TP. Find precision, recall, F1.
> Precision = 80/150 ≈ 0.533; Recall = 80/100 = 0.80; F1 ≈ 2·0.533·0.80/(1.333) ≈ **0.640**.

**Q53.** Standardization (z-score) of feature x: x_new = (x − μ)/σ. Why is this important for kNN?
> Without it, features with large numerical range dominate the Euclidean distance, washing out other features.

**Q54.** Which is non-parametric: linear regression, logistic regression, kNN, decision tree?
> **kNN** (and decision trees, depending on definition). Linear and logistic are parametric.

**Q55.** PCA on 100-dim data. After PCA, you keep 5 components. What does this mean?
> You project the data onto the 5 directions of maximum variance — keeping the most informative dimensions while discarding noise/redundancy.


---

## 🎙️ PART 8 — Interview Preparation

> The official IIT Madras announcement says selection is via "entrance test **and/or interviews**." If you're called for an interview, expect 15–25 minutes with a panel of 1–3 faculty members. Here is exactly what to prepare.

### 8.1 Five questions you will almost certainly be asked

**Q1: "Tell me about yourself."**
- 60–90 seconds. Cover: background, current role, why AI now, what you want to do after the program.
- Example structure: "I'm a software engineer with 6 years of experience at [companies]. I currently work on [type of systems]. Over the last [X] months I've been working with AI tools and built [small project / Kaggle / experimentation]. The Web M.Tech program is the right fit because I want a deep, structured, math-heavy foundation in AI rather than just learning to call APIs — and I want to apply it to [your domain]."

**Q2: "Why this program and not [GATE-based regular M.Tech / a Coursera course / an MS abroad]?"**
- Be honest. Working professional, can't quit job, want IIT Madras rigor + flexibility, want hands-on projects in your work domain.

**Q3: "What does 'machine learning' mean to you?" or "Explain in simple terms."**
- "ML is the practice of writing programs that improve their performance on a task by learning patterns from data, rather than being explicitly programmed for the task. The simplest example is linear regression: given pairs of (study hours, exam marks), the model learns the line that best predicts marks for a new student."

**Q4: A live mini-problem from the syllabus.** Examples I've seen reported across IITM CODE programs:
- *"Walk me through how Bayes' theorem works."*
- *"What does the determinant of a matrix tell you geometrically?"*
- *"Explain overfitting and how to detect/fix it."*
- *"What's the difference between mean and median, and when would you prefer median?"*
- *"Why would standardizing features matter for kNN but not for decision trees?"*

> 🎯 **Strategy for Q4:** Don't rush. Repeat the question to confirm you understood, think for 5 seconds, then answer in plain English first, then math. **It is OK to say "I'm not 100% sure but here's how I'd think about it..." — the panel cares about your reasoning, not perfect recall.**

**Q5: "How would you apply AI in your current job / company?"**
- This is your big chance. Have **one concrete project idea** ready (it's also the project they may want you to do later in the program).
- Structure: business problem → what data exists → which ML approach → how you'd evaluate.

### 8.2 Topics you MUST be conversational about

For each of these, be able to explain in 30 seconds, give 1 example, and answer one follow-up:

- Bayes' theorem (with the medical-test example)
- Overfitting vs underfitting
- Bias-variance tradeoff
- Train/test/validation split + cross-validation
- Difference between supervised and unsupervised learning
- What gradient descent does and why it might not converge
- What eigenvalues/eigenvectors mean intuitively
- Difference between classification and regression
- One classification metric beyond accuracy (precision/recall/F1) and when accuracy is misleading
- One unsupervised technique (k-means or PCA)

### 8.3 Soft skills checklist

- ☐ Have a quiet, well-lit space with good camera angle (if online).
- ☐ Wear formal/semi-formal attire.
- ☐ Have your CV / application + a paper notebook + working pen on your desk.
- ☐ Test your laptop's webcam and mic 30 minutes before.
- ☐ Have a glass of water within reach.
- ☐ Smile when you join. Keep eye contact (look at the camera, not the screen).
- ☐ It's fine to take 5 seconds to think before answering. Silence is not failure.
- ☐ At the end, when asked "any questions for us?": ask one thoughtful question (e.g., about the project component, or what makes this cohort's coursework different from the prior Industrial AI version).

### 8.4 Don'ts

- Don't say "I forgot." Say "I haven't worked with that recently, but my best guess based on first principles is…"
- Don't memorize a script. Speak naturally.
- Don't oversell. If you've done a small Kaggle, call it a small Kaggle project — don't call it production ML.
- Don't talk over the panel.

---

## 📚 PART 9 — Free Resource Library

> All resources below are 100% free and the highest quality available for each topic. Don't try to use all of them — pick one per topic and go deep.

### Probability & Statistics
- **Khan Academy** — *Statistics and Probability* (full course, beginner-friendly):
  https://www.khanacademy.org/math/statistics-probability
- **StatQuest with Josh Starmer** (YouTube) — quirky, brilliantly clear short videos:
  https://www.youtube.com/@statquest
- **MIT OCW 18.05 Introduction to Probability and Statistics** — every lecture freely available

### Linear Algebra
- ⭐ **3Blue1Brown – "Essence of Linear Algebra"** (YouTube, 14 short videos, ~3 hrs total) — the single best visual intuition resource ever made:
  https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab
- **MIT 18.06 Linear Algebra by Gilbert Strang** (free on OCW + YouTube) — the classic textbook + lectures
- **Khan Academy — Linear Algebra:** https://www.khanacademy.org/math/linear-algebra

### Calculus & Optimization
- **3Blue1Brown – "Essence of Calculus"** (YouTube, 12 videos): https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr
- **Khan Academy — Differential Calculus:** https://www.khanacademy.org/math/differential-calculus

### Machine Learning
- ⭐ **Google's Machine Learning Crash Course** (free, hands-on with TensorFlow):
  https://developers.google.com/machine-learning/crash-course
- **StatQuest — Machine Learning playlist** (YouTube): clear ELI5 explanations of every algorithm
- **Andrew Ng's Machine Learning Specialization** (Coursera — audit for free):
  Stanford, the most famous ML course in the world
- **Hands-On ML book** by Aurélien Géron — first 4 chapters cover everything in this exam

### IIT Madras specific (most authentic style you can practice)
- **NPTEL** — search for *"Probability for Computer Science"* and *"Linear Algebra"* by IIT Madras professors. These are the actual lecture style you'll experience after admission.
- **GATE DA 2024 sample paper** (IISc) — directly aligned syllabus:
  https://gate2024.iisc.ac.in/wp-content/uploads/2023/10/DataScienceAISampleQuestionPaper.pdf
- **GATE DA 2024 question paper** + **GATE DA 2025 question paper** — solve these as final mocks.

### Practice / quizzing
- **GeeksforGeeks GATE DA Quiz** (free, unlimited): https://www.geeksforgeeks.org/quizzes/data-science-and-ai/
- **Brilliant.org** — has free probability and linear algebra interactive courses

---

## 🧘 PART 10 — Final Tips for Exam Day

### Before the exam (the day before)
1. ☐ Print or save the **Formula Sheet** (Part 6) — read it twice.
2. ☐ Skim the **Practice Question Bank** (Part 7) — DON'T solve new problems. Just look at the patterns.
3. ☐ Pack: ID, hall ticket, pen, water, snack.
4. ☐ Sleep early — 7+ hours.
5. ☐ Light dinner. Stay off phones/screens 1 hour before bed.

### During the exam
1. **First 5 minutes:** Read all instructions. Note the duration, total marks, marking scheme. Confirm there's no negative marking.
2. **First pass (45 min):** Go through ALL questions once, answering only the easy ones (the ones you can do in <60 seconds). Mark the rest.
3. **Second pass (45 min):** Tackle the medium-difficulty marked questions.
4. **Third pass (last 30 min):** Hard questions + revisit your answers + attempt every NAT (numerical) question because there's no negative marking.
5. **Final 5 minutes:** Make sure no questions are left blank. **Guess every MCQ you don't know** — if there's no negative marking, blank = wasted opportunity.

### Strategic shortcuts (use these to save time)
- **Eigenvalues of 2×2:** sum = trace, product = det. Don't always need to solve the characteristic polynomial.
- **Eigenvalues of triangular matrix:** = diagonal entries. Instant.
- **Probability with "at least"/"at most":** compute the complement instead — usually faster.
- **MCQ elimination:** 2 of the 4 options are usually obviously wrong. Always eliminate first.
- **Plug in numbers:** for abstract algebra MCQs, plug in simple numbers (e.g., a=1, b=2) to check which option is correct.
- **NAT questions:** double-check by plugging your answer back into the equation. Arithmetic mistakes are the #1 source of lost marks.

### When you're stuck
- Move on. Don't sink 10 minutes into a single question. 5 easy questions answered = 5 marks. 1 hard question solved (or wrong) = 1 mark.
- If a question feels impossible, it's probably testing something specific you've seen — re-read it slowly. The trap word is usually "NOT", "always", "never", "least", "most".

### The mindset
You are not competing against IIT-level prodigies in this exam — you're competing against other working professionals (most with 2+ years of experience, often in non-AI roles), and the exam is calibrated for that pool. Your software engineering background gives you a major advantage in problem decomposition, pattern recognition, and algorithm tracing. **The math is just a notation — you already think this way every day.**

---

## 💪 Closing Note

You've been given an excellent existing study guide; this version goes deeper, adds the Industrial AI / Web M.Tech-specific exam intel, the GATE DA sample-question patterns, and the interview prep. Combined with consistent daily practice, this is sufficient material to clear the exam.

**The single most important thing you can do** in the next 30 days is **solve problems by hand** — not just read theory. Theory feels like learning; solving problems IS learning. Aim for 5–10 problems every single day, even on rest days, even when tired. After 28 days, you'll have done 200+ problems, and the patterns become automatic.

You can do this. Trust the plan, trust your engineering instincts, and put in the daily reps.

🎓 **All the best for the entrance exam and the interview!**

---

*Master Study Guide compiled from: IIT Madras CODE Web M.Tech AI official syllabus & brochure; IIT Madras Zanzibar M.Tech IAI screening test instructions; GATE DA 2024 sample question paper (IISc Bangalore); GATE DA 2024–2025 actual papers; IIT Madras admissions press release Feb 2025.*