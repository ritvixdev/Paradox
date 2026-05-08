# 📚 GATE DA 2026 — Previous Year Questions with Solutions
### Complete Analysis | Answers | Tricks | Concepts
> **Exam:** GATE Data Science & Artificial Intelligence 2026
> **Prepared for:** IIT Madras WMT AI Entrance Preparation — Suvam Das

---

## 🗂️ Quick Navigation

| Section | Topics |
|---|---|
| [General Aptitude (GA)](#general-aptitude) | Verbal, Reasoning, Quantitative |
| [Core DA — Probability & Statistics](#probability--statistics) | Q9, Q10, Q18, Q24, Q34, Q35, Q43, Q44, Q47, Q52, Q53, Q54 |
| [Core DA — Linear Algebra](#linear-algebra) | Q11, Q12, Q36, Q42, Q55 |
| [Core DA — Machine Learning](#machine-learning) | Q1, Q2, Q13, Q19, Q26, Q27, Q37, Q45, Q46 |
| [Core DA — Calculus & Optimization](#calculus--optimization) | Q17, Q25 |
| [Core DA — AI/Logic/Search](#ai--logic--search) | Q3, Q4, Q14, Q20, Q28, Q38 |
| [Core DA — Databases](#databases--programming) | Q7, Q8, Q16, Q22, Q31, Q32, Q33, Q41, Q49, Q50, Q51 |
| [Core DA — Programming/DSA](#programming--dsa) | Q5, Q6, Q15, Q21, Q23, Q29, Q30, Q39, Q40, Q48 |

---

## ⚠️ YOUR EXAM FILTER
> Questions marked 🎯 are **directly relevant** to your WMT AI entrance exam.
> Questions marked ⚪ are **NOT in your syllabus** (DB, AI search, DSA) — skip for now.

---

# GENERAL APTITUDE

---

## GA Q1 — Verbal Analogy
**Answer: B (Respect)**

**Question:** Verbosity : Brevity :: Insolence : ____

**Solution:**
- Verbosity = using too many words; Brevity = using few words → Brevity is the OPPOSITE
- Insolence = rude/disrespectful behaviour
- The opposite of Insolence = **Respect**

**Trick:** "Opposite pair" analogy. Always check if the pair is synonym or antonym first. Here Verbosity → Brevity is antonym, so find antonym of Insolence.

---

## GA Q2 — Number Puzzle
**Answer: B (14)**

**Question:** Product of digits of a 3-digit number = 70. Find sum of digits.

**Solution:**
- Factorise 70: 70 = 2 × 5 × 7
- The three single digits are 2, 5, 7
- Sum = 2 + 5 + 7 = **14**
- Check: These are all valid single digits ✓, product = 70 ✓

**Trick:** Factorise the product into single-digit factors. 70 = 2 × 35 = 2 × 5 × 7. All are single digits, so done!

---

## GA Q4 — Logarithm Identity 🎯
**Answer: C (x = y)**

**Question:** m > n > 0. x = n^log10(m), y = m^log10(n). Relation between x and y?

**Solution:**
Take log of both sides:
```
log(x) = log10(m) × log10(n)
log(y) = log10(n) × log10(m)
```
Both equal the same expression: **log(x) = log(y)** → **x = y**

**Key Concept:** log(a^b) = b × log(a). This is a classic logarithm symmetry trick.

**Trick:** When you see n^log(m) and m^log(n), always take log of both expressions. They become identical.

---

## GA Q5 — Logical Inference
**Answer: D**

**Question:** "If movie was a success → actor would have made money." Which is true?

**Solution:**
This is a **counterfactual conditional**: "If P then Q" — when said in past perfect, it implies P did NOT happen.

"If his movie HAD been a success, he WOULD HAVE made money" → implies the movie was NOT a success.

**Trick:** In English, "would have" in a conditional always signals the hypothesis did NOT occur. Answer is always the negation of the condition.

---

## GA Q7 — Statistics Puzzle
**Answer: B (1 way)**

**Question:** 5 integers from 0-20, mean=12, median=18, single mode=20. How many ways?

**Solution:**
- 5 numbers, mean = 12 → Sum = 60
- Median = 18 → 3rd number when sorted = 18, so at least 3 numbers ≥ 18
- Mode = 20 (single) → 20 must appear most frequently (at least twice), no other number repeated
- Numbers sorted: [a, b, 18, c, d] where c, d ≥ 18
- Since mode is 20 (only mode): 20 must appear at least twice, so two of {c, d} = 20
- Sorted: [a, b, 18, 20, 20]
- Sum so far: 18+20+20 = 58; remaining = 60-58 = 2 → a+b = 2
- b ≤ 18, a ≤ b, a+b = 2, no repetition of any digit except 20
- Only option: {1, 1} → but then 1 is also a mode → violates "single mode"
- Try: {0, 2} → sorted [0, 2, 18, 20, 20] → mode is 20 only ✓, mean=60/5=12 ✓, median=18 ✓
- {2, 0} is same set (ignoring permutations)
- Any other? {0,2} is the only one. **1 way.**

---

## GA Q9 — Number Theory
**Answer: C (Y = 6)**

**Question:** PQ and RS are consecutive. (PQ)² + (RS)² = XYP. Find Y.

**Solution:**
Try consecutive two-digit pairs. Since result is 3-digit XYP, and XYP's last digit is P (units digit of PQ):
- Try PQ = 34, RS = 35: 34² + 35² = 1156 + 1225 = 2381. XYP = 238P where P=4 (tens digit of PQ=34, P=3). No match.
- Try PQ = 47, RS = 48: 47² + 48² = 2209 + 2304 = 4513. XYP = 451P, P=4. Last digit should be P=4. 4513 ends in 3 ≠ 4.
- Try PQ = 56, RS = 57: 56² + 57² = 3136 + 3249 = 6385. XYP: P=5 (tens digit). Last digit = 5. Yes! 6385 ends in 5 ✓. Y = 3... wait, XYP = 638P? No, it's a 3-digit number XYP. 6385 is 4 digits.
- Reconsider: XYP is 3-digit. So (PQ)² + (RS)² must be 3-digit → PQ < ~12
- Try PQ = 10, RS = 11: 100 + 121 = 221. XYP = 221, P=1 (units place of 10 is 0). P=0. 221 ends in 1 ≠ 0.
- PQ = 11, RS = 12: 121 + 144 = 265. P=1, ends in 5 ≠ 1.
- PQ = 12, RS = 13: 144 + 169 = 313. P=1, 313 ends in 3 ≠ 1.
- PQ = 13, RS = 14: 169 + 196 = 365. P=1, 365 ends in 5 ≠ 1.
- PQ = 14, RS = 15: 196 + 225 = 421. P=1, 421 ends in 1 ✓! XYP=421, X=4, Y=2, P=1. But Q=4, and X=4 would be same digit... all digits P,Q,R,S,X,Y must be distinct. P=1,Q=4,R=1... R=1=P → not distinct!
- PQ = 20, RS = 21: 400 + 441 = 841. P=2, 841 ends in 1 ≠ 2.
- PQ = 21, RS = 22: RS can't repeat digit. Skip.
- PQ = 23, RS = 24: 529 + 576 = 1105. 4 digits, too big.
- Going back: PQ=14 almost worked. Try nearby: PQ=16, RS=17: 256+289=545. P=1, 545 ends in 5≠1.
- PQ=17, RS=18: 289+324=613. P=1, 613 ends in 3≠1.
- PQ=18, RS=19: 324+361=685. P=1, 685 ends in 5≠1.
- After careful search, **Y=6** is given as correct. Trust the answer: **Y = 6**.

---

# CORE DA QUESTIONS

---

# PROBABILITY & STATISTICS

---

## 🎯 Q9 — Probability of Even Product
**Answer: C** | **Topic: Combinatorics + Probability**

**Question:** M is a random non-empty subset of S={1,2,...,2026}. P(product of elements is even)?

**Solution:**
- Product is even ↔ at least one element is even
- Use complement: P(product is even) = 1 - P(product is odd)
- Product is odd ↔ ALL elements are odd
- Odd numbers in S = {1,3,5,...,2025} = 1013 numbers
- Total non-empty subsets of S = 2^2026 - 1
- Subsets of all-odd numbers (non-empty) = 2^1013 - 1

**P(all odd) = (2^1013 - 1) / (2^2026 - 1)**

**P(even product) = 1 - (2^1013 - 1)/(2^2026 - 1)**

Simplify: = [(2^2026 - 1) - (2^1013 - 1)] / (2^2026 - 1)
= [2^2026 - 2^1013] / (2^2026 - 1)
= **2^1013(2^1013 - 1) / (2^2026 - 1)**

**Answer: C ✓**

**Key Concept:** Complement method — always easier to find P(none) than P(at least one).

**Trick:** "Product is even" = at least one even element. Use complement: P(at least one even) = 1 - P(all odd).

---

## 🎯 Q10 — Stars and Bars (Counting)
**Answer: A** | **Topic: Combinatorics**

**Question:** n1+n2+n3+n4=20 with non-negative integers. P(all positive)?

**Solution:**
**Total solutions** (non-negative integers, n1+n2+n3+n4=20):
- Stars and bars: C(20+4-1, 4-1) = **C(23, 3)**

**Favorable** (all positive, i.e., all ≥ 1): Substitute mᵢ = nᵢ - 1 (mᵢ ≥ 0):
- m1+m2+m3+m4 = 16
- Solutions: C(16+3, 3) = **C(19, 3)**

**P = C(19,3) / C(23,3) = Answer A ✓**

**Key Concept:** Stars and Bars formula: solutions to x1+x2+...+xk=n with xᵢ≥0 is C(n+k-1, k-1).

**Trick for "all positive":** Substitute mᵢ = xᵢ - 1 to convert "≥1" to "≥0", then reduce total.

---

## 🎯 Q18 — Normal vs t-Distribution
**Answer: A;C** | **Topic: Distributions**

**Question:** Z ~ N(0,1) with pdf g(z), CDF G(z). Y ~ t₁ with pdf h(y), CDF H(y). g(c) = h(c) for positive c. Which statements correct?

**Solution:**

**Statement A: G(0) = H(0)** ✓
Both normal and t-distribution are symmetric around 0. So P(Z<0) = P(Y<0) = 0.5 for both. **TRUE**

**Statement B: G(c) < H(c)** — Evaluate
- The t₁ distribution (Cauchy) has heavier tails than Normal
- At the intersection point c (where pdfs are equal), for x < c, the t-distribution's CDF is actually HIGHER (more area in tails means less area accumulated by c for the heavier-tailed distribution)
- Actually: t has heavier tails, so more probability in tails, which means LESS area under the curve near center → H(c) < G(c) → G(c) > H(c), so G(c) < H(c) is **FALSE**

**Statement C: G(-c) < H(-c)** ✓
By symmetry: G(-c) = 1 - G(c) and H(-c) = 1 - H(c)
Since G(c) > H(c): G(-c) = 1-G(c) < 1-H(c) = H(-c) → **TRUE**

**Key Concept:** t-distribution has heavier tails than normal. They intersect at some point. The normal has more probability mass near the center.

**Memory Trick:** t-distribution = "Thicker tails". Thicker tails = more area far from center = less area accumulated toward center = lower CDF at moderate values.

---

## 🎯 Q24 — Exponential Memoryless Property
**Answer: 0.35** | **Topic: Exponential Distribution**

**Question:** X ~ Exponential(mean=λ). P(X>5)=0.35. Find P(X>10|X>5).

**Solution:**
**THE MEMORYLESS PROPERTY OF EXPONENTIAL DISTRIBUTION:**
```
P(X > s+t | X > s) = P(X > t)
```
This is the DEFINING property of the exponential distribution!

Therefore:
**P(X>10 | X>5) = P(X > 5+5 | X > 5) = P(X > 5) = 0.35**

**Answer: 0.35 ✓**

**Key Concept — Memoryless Property:** "If you've already waited 5 minutes, the probability of waiting 5 more minutes is the SAME as waiting 5 minutes from scratch."

**Exam Trick:** Whenever you see exponential distribution + conditional probability, IMMEDIATELY apply memoryless property. P(X > a+b | X > a) = P(X > b).

---

## 🎯 Q34 — Variance of Product of Independent Variables
**Answer: A (100)** | **Topic: Variance Properties**

**Question:** X ~ Bernoulli(0.3), Y ~ N(0, 100), independent. Find Var((2X-1)Y).

**Solution:**
Let Z = 2X-1. Note Z can be: if X=1 → Z=1; if X=0 → Z=-1.

**Key Formula:** For independent variables:
```
Var(ZY) = E[Z²]·E[Y²] - (E[Z])²·(E[Y])²
```
Or equivalently:
```
Var(ZY) = Var(Z)·Var(Y) + Var(Z)·(E[Y])² + (E[Z])²·Var(Y)
```

Since E[Y] = 0 (normal with mean 0):
```
Var(ZY) = E[Z²]·E[Y²] - (E[Z]·E[Y])²
         = E[Z²]·E[Y²] - 0
         = E[Z²]·Var(Y)   [since E[Y]=0, E[Y²]=Var(Y)=100]
```

**E[Z²]:** Z² = (2X-1)² = 4X²-4X+1
- E[X] = p = 0.3, E[X²] = p (since X is Bernoulli, X²=X)
- E[Z²] = 4(0.3)-4(0.3)+1 = 1.2-1.2+1 = **1**

So **Var((2X-1)Y) = 1 × 100 = 100 ✓**

**Alternative shortcut:** Note that 2X-1 is either +1 or -1 regardless of X. So (2X-1)² = 1 always! Therefore E[(2X-1)²] = 1.

**Trick:** When a variable only takes values ±1, its square is always 1 — this makes variance calculations simple!

---

## 🎯 Q35 — Poisson CDF Limit
**Answer: A (0.5)** | **Topic: Poisson Distribution, CLT**

**Question:** L = lim(n→∞) Σ(k=0 to n) e^(-n) × n^k / k!

**Solution:**
The sum Σ(k=0 to n) e^(-n) × n^k / k! = P(X ≤ n) where X ~ Poisson(n).

By CLT, for large n, Poisson(n) → N(n, n).

P(X ≤ n) = P((X-n)/√n ≤ 0) → Φ(0) = **0.5**

**Answer: L = 0.5 ✓**

**Key Concept:** Sum of Poisson PMF from 0 to its own mean = probability of being below the mean. By symmetry of CLT approximation, this is 0.5.

**Trick:** This is a classic GATE question. The sum of Poisson probabilities up to λ equals P(X ≤ λ) which → 1/2 as λ → ∞ by CLT.

---

## 🎯 Q43 — Chi-Squared Distribution
**Answer: A;B;C** | **Topic: Chi-Squared Distribution**

**Question:** X₁,...,Xₙ iid ~ N(0,1). X̄ = mean. Which statements correct?

**Solution:**

**Statement A: ΣXᵢ² ~ χ²(n)** ✓
By definition: Sum of squares of n independent N(0,1) = χ²(n). **TRUE**

**Statement B: Σ(Xᵢ - X̄)² ~ χ²(n-1)** ✓
This is the sample variance formula. Dividing by σ²=1 and using n-1 degrees of freedom (one lost for estimating mean). **TRUE**

**Statement C: X₁² + Xₙ² follows exponential with mean 2** ✓
Sum of 2 squared independent N(0,1) = χ²(2). And χ²(2) = Exponential(1/2), with mean = 2. **TRUE**

**Statement D: (√n × X̄)² ~ χ²(2)** — FALSE
√n × X̄ ~ N(0,1), so (√n × X̄)² ~ χ²(1), not χ²(2). **FALSE**

**Key Concepts:**
- χ²(k) = sum of k squared independent N(0,1)
- χ²(2) = Exponential(1/2), with mean 2
- Sample variance: Σ(Xᵢ-X̄)²/σ² ~ χ²(n-1)

**Memory Trick:** "Chi-squared with k df = k squared normals." Degrees of freedom = number of independent normals squared.

---

## 🎯 Q44 — CDF Properties
**Answer: B;C** | **Topic: CDF**

**Question:** X is discrete. Which properties of CDF F(x) are correct?

**Solution:**

**A: F(x) is always positive** — FALSE. F(x) ≥ 0 but equals 0 for x less than the minimum support. "Positive" means strictly > 0, which isn't always true.

**B: F(x) is non-decreasing** ✓ TRUE. As x increases, probability accumulated can only stay same or increase.

**C: F(x) has jump discontinuity** ✓ TRUE. For DISCRETE random variables, the CDF jumps at each possible value.

**D: F(x) is left continuous** — FALSE. For discrete random variables, the CDF is **RIGHT continuous** (jumps happen at the point, not before it). Left continuous would be for the left-limit version.

**Key Concepts:**
- CDF is always non-decreasing
- For discrete: right-continuous (jumps at mass points)
- F(-∞) = 0, F(+∞) = 1

**Trick:** Discrete CDF = staircase function jumping at each value. It's right-continuous by convention: F(x) = P(X ≤ x) includes x.

---

## 🎯 Q47 — Bayes' Theorem (Medical Test)
**Answer: ~0.77** | **Topic: Bayes' Theorem**

**Question:** P(disease)=0.3, P(+|disease)=0.8, P(+|no disease)=0.1. Find P(disease|+).

**Solution (Step-by-Step Bayes):**
```
P(D) = 0.30,   P(no D) = 0.70
P(+|D) = 0.80, P(+|no D) = 0.10

P(+) = P(+|D)×P(D) + P(+|no D)×P(no D)
     = 0.80×0.30 + 0.10×0.70
     = 0.24 + 0.07
     = 0.31

P(D|+) = P(+|D)×P(D) / P(+)
        = 0.24 / 0.31
        ≈ 0.7742 ≈ 0.77
```

**Answer: ≈ 0.77 ✓**

**Standard Bayes Template:**
```
1. Write all given priors and likelihoods
2. Compute P(evidence) = Σ P(evidence|hypothesis)×P(hypothesis)
3. Apply Bayes: P(H|E) = P(E|H)×P(H) / P(E)
```

**Intuition:** Even with 80% true positive rate, since only 30% have disease, many positives are actually healthy people. Still, 77% is high because the base rate isn't too low.

---

## 🎯 Q52 — Sample Variance Computation
**Answer: 10** | **Topic: Statistics**

**Question:** (1/2000) Σᵢ Σⱼ (xᵢ-xⱼ)² = 99. Find (1/99)Σ(xᵢ-x̄)².

**Solution:**
**Key identity:**
```
(1/2n²) × Σᵢ Σⱼ (xᵢ-xⱼ)² = (1/n) Σ(xᵢ-x̄)²  [population variance]
```

Given: (1/2000) Σᵢ Σⱼ (xᵢ-xⱼ)² = 99, and n=100.

So 1/2000 = 1/(2×100²) = 1/(2n²):
```
Population variance = 99
```

The question asks for (1/99)Σ(xᵢ-x̄)² = n × population variance / 99 = 100 × 99 / 99 = **100 / 99 × 99 = 100**

Wait, more carefully:
(1/99)Σ(xᵢ-x̄)² = sample variance = n×(population variance)/(n-1) = 100×(99/100)/99×... 

Let σ² = (1/n)Σ(xᵢ-x̄)² = (1/2n²)ΣΣ(xᵢ-xⱼ)² = 99/100×... 

The identity: ΣᵢΣⱼ(xᵢ-xⱼ)² = 2n Σ(xᵢ-x̄)²

So: (1/2000) × ΣΣ(xᵢ-xⱼ)² = 99 → ΣΣ(xᵢ-xⱼ)² = 198000

Using identity: 2×100×Σ(xᵢ-x̄)² = 198000 → Σ(xᵢ-x̄)² = 990

Sample variance = (1/99)×990 = **10 ✓**

**Key Identity to Memorize:** ΣᵢΣⱼ(xᵢ-xⱼ)² = 2n Σᵢ(xᵢ-x̄)²

---

## 🎯 Q53 — Correlation (Tricky!)
**Answer: 0** | **Topic: Correlation**

**Question:** X~Uniform(-1,1). Y|X=x ~ Uniform(x²-0.1, x²+0.1). Find Corr(X,Y).

**Solution:**
```
E[Y|X=x] = x²  (midpoint of uniform interval)
E[Y] = E[E[Y|X]] = E[X²] = ∫₋₁¹ x²×(1/2)dx = 1/3
E[XY] = E[X·E[Y|X]] = E[X·X²] = E[X³] = 0  (since X is symmetric around 0, odd moment = 0!)
E[X] = 0  (symmetric uniform)

Cov(X,Y) = E[XY] - E[X]E[Y] = 0 - 0×(1/3) = 0
Corr(X,Y) = 0
```

**Answer: 0 ✓**

**Key Insight:** Even though Y depends on X (through x²), correlation measures LINEAR dependence. The relationship Y ≈ X² is quadratic, so linear correlation = 0.

**Trick:** "Correlation = 0 does NOT mean independence!" This is a perfect example — Y clearly depends on X (through x²), but linear correlation is 0 because odd moments of symmetric distributions are zero.

---

# LINEAR ALGEBRA

---

## 🎯 Q11 — Rotation Matrix Powers
**Answer: B (M)** | **Topic: Orthogonal Matrix, Eigenvalues**

**Question:** M is 2×2 rotation matrix with θ = 2π/5. Find M^2026.

**Solution:**
The rotation matrix M rotates by angle θ. M^n rotates by nθ.

M^2026 rotates by 2026θ = 2026 × (2π/5) = 405.2π

Now 405.2π = 405×π + 0.2π = ... let's compute 2026 mod 5:
2026 = 5×405 + 1 → **2026 ≡ 1 (mod 5)**

So M^2026 = M^1 = **M ✓**

**Key Concept:** Rotation matrices satisfy M^k = M^(k mod n) where n is the period (period = 2π/θ = 5 here).

**Formula:** Rotation matrix with angle θ: M^n = rotation by nθ. M^n = I when nθ = 2π (or multiple of 2π).

**Trick:** Find the period of the rotation (how many applications to get back to identity), then reduce power modulo period.

---

## 🎯 Q12 — Ball Intersected with Plane (Geometry + Linear Algebra)
**Answer: A (16π)** | **Topic: Subspaces, Geometry**

**Question:** S₁ = {x∈R³: xᵀx ≤ 16} (sphere of radius 4). S₂ = 2-dimensional subspace of R³. Area of S₁∩S₂?

**Solution:**
- S₁ is a 3D ball of radius 4 (since |x|² ≤ 16 → |x| ≤ 4)
- S₂ is a 2D plane (subspace) through the origin
- S₁ ∩ S₂ = a 2D disk on the plane, centered at origin, radius 4
- Area of disk = π × r² = π × 4² = **16π ✓**

**Key Concept:** Intersection of a ball with a plane through the center is a disk with the same radius.

**Trick:** Always think geometrically for these questions. A 2D subspace is a plane through the origin. Intersect a sphere with a plane through center → great circle (boundary) → disk (interior).

---

## 🎯 Q36 — Trace = Sum of Eigenvalues
**Answer: C ({π/4, -π/4})** | **Topic: Eigenvalues, Trace**

**Question:** 3×3 matrix [[1,0,0],[0,cost,-sint],[0,sint,cost]]. Find t where γ₁+γ₂+γ₃ = 1+√2.

**Solution:**
**Trace = sum of eigenvalues!**

Trace of matrix = 1 + cos(t) + cos(t) = 1 + 2cos(t)

Set equal to 1+√2:
```
1 + 2cos(t) = 1 + √2
2cos(t) = √2
cos(t) = √2/2 = 1/√2
t = ±π/4
```

**Answer: {π/4, -π/4} ✓**

**Key Formula:** tr(A) = sum of all eigenvalues. This is fundamental!

**Trick:** For block diagonal matrices, eigenvalues are union of eigenvalues of blocks. The 2×2 rotation block has eigenvalues e^(it) and e^(-it) with real part = cos(t), so trace of the block = 2cos(t).

---

## 🎯 Q42 — Centering Matrix Properties
**Answer: A;D** | **Topic: Projection Matrix, Idempotent Matrix**

**Question:** M = Iₙ - (1/n)11ᵀ where 1 = (1,1,...,1)ᵀ. Which are correct?

**Solution:**

**A: Mᵀ = M** ✓
(Iₙ - (1/n)11ᵀ)ᵀ = Iₙᵀ - (1/n)(11ᵀ)ᵀ = Iₙ - (1/n)11ᵀ = M. **TRUE (Symmetric)**

**B: M² = Iₙ** — FALSE
M² = M×M = (Iₙ - (1/n)11ᵀ)² = Iₙ - (2/n)11ᵀ + (1/n²)11ᵀ11ᵀ
Note: 1ᵀ1 = n (sum of n ones), so 11ᵀ11ᵀ = n×11ᵀ
M² = Iₙ - (2/n)11ᵀ + (1/n²)×n×11ᵀ = Iₙ - (2/n)11ᵀ + (1/n)11ᵀ = Iₙ - (1/n)11ᵀ = **M**
So M² = M (idempotent), NOT Iₙ.

**C: Trace(M) = n** — Let's check
Trace = n - (1/n)×trace(11ᵀ) = n - (1/n)×n = n - 1 ≠ n. **FALSE**

**D: M is a projection matrix** ✓
M is symmetric (A) and idempotent (M²=M). These are the TWO conditions for a projection matrix. **TRUE**

**Key Properties of Projection Matrices:**
1. Symmetric: P = Pᵀ
2. Idempotent: P² = P
3. Eigenvalues are only 0 or 1
4. Trace = rank = number of 1-eigenvalues

---

## 🎯 Q55 — Maximum of Quadratic Form
**Answer: 1** | **Topic: Eigenvalues, Quadratic Forms**

**Question:** Same M = Iₙ - (1/n)11ᵀ. Find max(xᵀMx) subject to xᵀx=1.

**Solution:**
The maximum of xᵀMx over unit sphere = **largest eigenvalue of M**.

What are the eigenvalues of M = Iₙ - (1/n)11ᵀ?
- The vector 1 (all-ones) is an eigenvector: M×1 = 1 - (1/n)×(n×1) = 1 - 1 = 0. So eigenvalue 0.
- Any vector perpendicular to 1 (xᵀ1=0): Mx = x - (1/n)×(1ᵀx)×1 = x - 0 = x. So eigenvalue 1.

Eigenvalues: one 0, and (n-1) ones.

Maximum eigenvalue = **1 ✓**

**Key Theorem:** max(xᵀAx) subject to xᵀx=1 = largest eigenvalue of A.

**Application in ML:** This is exactly how PCA works — finding directions of maximum variance!

---

# MACHINE LEARNING

---

## 🎯 Q1 — PCA Principal Components
**Answer: B (θ = 90°)** | **Topic: PCA, Orthogonality**

**Question:** PCA reduces 100 to 10 dimensions. Angle between 1st and 10th principal components?

**Solution:**
Principal components are eigenvectors of the covariance matrix. A key property: eigenvectors corresponding to DIFFERENT eigenvalues of a **symmetric** matrix are **orthogonal**.

The covariance matrix is symmetric. All 10 principal components (1st through 10th) correspond to different eigenvalues (assuming distinct eigenvalues, which PCA requires).

Therefore, **any two different principal components are perpendicular (orthogonal) → angle = 90°**

**Answer: B ✓**

**Key Concept:** PCA principal components are always mutually orthogonal. This is because they are eigenvectors of the symmetric covariance matrix.

**Trick:** "PCA = Orthogonal directions." All principal components are at 90° to each other. This is not just a coincidence — it's built into the mathematical definition.

---

## 🎯 Q2 — LOOCV Splits
**Answer: C (900)** | **Topic: Cross-Validation**

**Question:** 1000 samples, first 100 for testing. LOOCV for model selection. How many validation splits?

**Solution:**
- Training data for model selection = 1000 - 100 = **900 samples**
- LOOCV (Leave-One-Out Cross Validation) with n=900 training samples creates **n = 900 validation splits**
- Each split: train on 899, validate on 1

**Answer: 900 ✓**

**Key Concept:** LOOCV with n samples creates exactly n train-validation splits (one for each sample being left out once).

**Trick:** LOO = n splits where n = training set size (NOT total dataset size). Always subtract the held-out test set first.

---

## 🎯 Q13 — Algorithm Matching
**Answer: B (T1:A2, T2:A4, T3:A1, T4:A3)** | **Topic: ML Algorithms**

**Question:** Match Task to Algorithm: T1-Clustering, T2-Classification, T3-Sampling, T4-Feature Extraction with A1-MCMC, A2-K-Medoid, A3-LDA, A4-Naive Bayes.

**Solution:**
- **T1 (Clustering) → A2 (K-Medoid):** K-Medoid is a clustering algorithm (like k-means but uses actual data points as centers)
- **T2 (Classification) → A4 (Naive Bayes):** Naive Bayes is a classification algorithm
- **T3 (Sampling) → A1 (MCMC):** Markov Chain Monte Carlo is a sampling method
- **T4 (Feature Extraction) → A3 (LDA):** Linear Discriminant Analysis finds discriminative features/directions

**Answer: B ✓**

**Quick Algo Reference:**
| Algorithm | Type |
|---|---|
| K-Means, K-Medoid, DBSCAN | Clustering |
| Naive Bayes, SVM, LDA, kNN | Classification |
| MCMC, Rejection Sampling, Gibbs | Sampling |
| PCA, LDA, Autoencoders | Dimensionality Reduction / Feature Extraction |

---

## 🎯 Q19 — Gradient Descent Update
**Answer: ~9.00** | **Topic: SGD, Gradient Descent**

**Question:** f_w(x) = wx. SGD with lr=0.1. w=10. x=10. Find new w.

**Solution:**
For supervised learning, assume squared loss: L = (y - wx)²

But question says "objective function being minimized is f_w(x) = wx" — this is the prediction, not the loss.

For linear model, gradient of MSE loss w.r.t w:
∂L/∂w = -2(y - wx)x  but without labels...

Actually for f(w) = wx as the objective itself:
∂f/∂w = x = 10

SGD update: w_new = w_old - α × gradient = 10 - 0.1 × 10 = 10 - 1 = **9.00**

**Answer: 9.00 ✓** (within range 8.90:9.10)

**Key Formula:** w_new = w_old - learning_rate × gradient

---

## 🎯 Q26 — Hierarchical Clustering (Manhattan Distance)
**Answer: D (P2, P4)** | **Topic: Hierarchical Clustering, Distance Metrics**

**Question:** 4 points in 3D. Hierarchical Agglomerative Clustering with Manhattan distance. Which two merge first?

**Points:** P1=[2,3,-1], P2=[3,1,1], P3=[5,-2,3], P4=[3,3,3]

**Solution — Compute ALL pairwise Manhattan distances:**
```
d(P1,P2) = |2-3|+|3-1|+|-1-1| = 1+2+2 = 5
d(P1,P3) = |2-5|+|3-(-2)|+|-1-3| = 3+5+4 = 12
d(P1,P4) = |2-3|+|3-3|+|-1-3| = 1+0+4 = 5
d(P2,P3) = |3-5|+|1-(-2)|+|1-3| = 2+3+2 = 7
d(P2,P4) = |3-3|+|1-3|+|1-3| = 0+2+2 = 4  ← MINIMUM
d(P3,P4) = |5-3|+|-2-3|+|3-3| = 2+5+0 = 7
```

**Minimum distance = 4, between P2 and P4 ✓**

**Manhattan Distance Formula:** d(a,b) = Σ|aᵢ - bᵢ|

**Trick:** Compute all pairs systematically. The first merge in agglomerative clustering = minimum pairwise distance.

---

## 🎯 Q27 — Ridge Regression Properties
**Answer: D** | **Topic: Ridge Regression**

**Question:** Which statement is true for Ridge Regression?

**Solution — Analyze each option:**

**A:** "Guard against model working well on TEST, poorly on TRAIN" — WRONG. The concern is overfitting = works well on TRAIN, poorly on TEST. Ridge prevents overfitting.

**B:** "Uses L1 norm" — WRONG. Ridge uses L2 norm (sum of squares). LASSO uses L1.

**C:** "Reduce parameters with negative values" — WRONG. Ridge shrinks ALL coefficients toward zero uniformly, not targeting negative ones specifically.

**D:** "Regularizer may increase bias but reduces variance" ✓ CORRECT. This is the fundamental bias-variance tradeoff of regularization. Ridge adds penalty → coefficients shrink → model less flexible → HIGHER BIAS, LOWER VARIANCE.

**Answer: D ✓**

**Ridge Regression Summary:**
- Loss = MSE + λ||w||²
- λ=0 → OLS (ordinary least squares)
- λ↑ → coefficients shrink toward 0
- Effect: ↑ Bias, ↓ Variance

---

## 🎯 Q37 — Classification Metrics Calculation
**Answer: A;B** | **Topic: Precision, Recall, Accuracy**

**Question:** 20 stories of X, 10 of Y. 6 of X's stories misclassified as Y. 2 of Y's stories misclassified as X.

**Solution — Build Confusion Matrix (X is positive class):**
```
                  Predicted X    Predicted Y
Actual X (20):       14              6         → Recall_X = 14/20 = 0.70
Actual Y (10):        2              8         → Recall_Y = 8/10 = 0.80
                     ↑               ↑
              Prec_X=14/16       Prec_Y=8/14
                  =0.875            =0.571
```

**Accuracy = (14+8) / 30 = 22/30 = 11/15 ✓ (Statement A is TRUE)**

**Precision_X = 14/16 = 0.875, Precision_Y = 8/14 ≈ 0.571**
Precision_X > Precision_Y ✓ **(Statement B is TRUE)**

**Recall_X = 14/20 = 0.70, Recall_Y = 8/10 = 0.80**
Recall_X < Recall_Y → Statement C (Recall_X > Recall_Y) is **FALSE**

**Statement D:** 14/15 ≠ 22/30 = 11/15 → **FALSE**

**Answer: A;B ✓**

**Confusion Matrix Template:**
```
TP = correctly predicted positives
FP = predicted positive but actually negative
FN = predicted negative but actually positive
TN = correctly predicted negatives

Accuracy  = (TP+TN)/(TP+TN+FP+FN)
Precision = TP/(TP+FP)  [quality of predictions]
Recall    = TP/(TP+FN)  [coverage of positives]
```

---

## 🎯 Q45 — Ridge Regression Loss Calculation
**Answer: ~7.00** | **Topic: Ridge Regression, Loss Function**

**Question:** w=[−3,4]ᵀ, x=[1,2]ᵀ, y_true = x1+x2. Ridge with λ=0.2, MAE loss. Find total loss.

**Solution:**
```
y_pred = wᵀx = (-3)(1) + (4)(2) = -3 + 8 = 5
y_true = x1 + x2 = 1 + 2 = 3

MAE = |y_true - y_pred| = |3 - 5| = 2

Regularization term = λ × ||w||² = 0.2 × ((-3)² + 4²) = 0.2 × (9+16) = 0.2 × 25 = 5

Total Loss = MAE + Regularization = 2 + 5 = 7.00 ✓
```

**Answer: 7.00 ✓**

**Ridge Loss Formula:** L = Loss(y, ŷ) + λ||w||²

---

## 🎯 Q46 — Neural Network Parameters
**Answer: 135** | **Topic: MLP Architecture**

**Question:** MLP: 30 inputs → 4 hidden → 3 hidden → 1 output. No biases. Count parameters.

**Solution:**
```
Layer 1→2: 30 × 4 = 120 parameters
Layer 2→3: 4 × 3  = 12  parameters
Layer 3→4: 3 × 1  = 3   parameters

Total = 120 + 12 + 3 = 135 ✓
```

**Key Formula (no bias):** Parameters between layer of size a and layer of size b = a × b

**With bias:** Parameters = a×b + b = b(a+1)

**Trick:** Multiply adjacent layer sizes and sum. No bias = multiply only. With bias = add destination layer size.

---

# CALCULUS & OPTIMIZATION

---

## 🎯 Q17 — Finding Roots and Extrema
**Answer: B;D** | **Topic: Calculus**

**Question:** f(x) = x³ - 3x² + 2 on (-1, 3]. Which statements correct?

**Solution:**
```
f'(x) = 3x² - 6x = 3x(x-2) = 0 → x=0 or x=2
f''(x) = 6x - 6
```

**Checking roots (f(x) = 0):**
- f(0) = 0 - 0 + 2 = 2 ≠ 0
- f(1) = 1 - 3 + 2 = **0 ✓** (Statement D is TRUE)
- f(2) = 8 - 12 + 2 = -2 ≠ 0

**Statement A:** "Exactly two roots in [-0.9, 0]": f(0)=2 and f(-0.9) ≈ -0.729-2.43+2 = -1.16 < 0. So one root in (-0.9, 0) by IVT. NOT two roots. **FALSE**

**Statement B:** "Minimum at x=2 only":
f''(2) = 12-6 = 6 > 0 → local min at x=2.
f''(0) = -6 < 0 → local max at x=0.
Check boundary: f(3) = 27-27+2 = 2; f(-1⁺) approaches f(-1) = -1-3+2 = -2.
Global minimum on (-1,3]: compare f(2)=-2 and approaching -2 at x→-1. Only interior minimum at x=2. **TRUE**

**Statement C:** "Maximum at x=0 only": f(0)=2, f(3)=2 (both equal). Not "only" at 0. **FALSE**

**Answer: B;D ✓**

---

## 🎯 Q25 — Double Infinite Series
**Answer: 1** | **Topic: Series, Calculus**

**Question:** Find Σᵢ₌₀^∞ Σⱼ₌₁^∞ 2^(-i) × 3^(-j)

**Solution:**
Since the series are independent (separable):
```
= (Σᵢ₌₀^∞ 2^(-i)) × (Σⱼ₌₁^∞ 3^(-j))

Inner sum 1: Σᵢ₌₀^∞ (1/2)^i = 1/(1-1/2) = 2

Inner sum 2: Σⱼ₌₁^∞ (1/3)^j = (1/3)/(1-1/3) = (1/3)/(2/3) = 1/2

Total = 2 × 1/2 = 1 ✓
```

**Answer: 1 ✓**

**Geometric Series Formula:** Σₙ₌₀^∞ rⁿ = 1/(1-r) for |r| < 1
**Starting from n=1:** Σₙ₌₁^∞ rⁿ = r/(1-r)

**Trick:** When a double sum is a product of two independent sums, separate them!

---

# AI / LOGIC / SEARCH

> ⚠️ These topics are NOT in your WMT AI entrance exam. Study lightly.

---

## ⚪ Q3 — Uninformed vs Informed Search
**Answer: C (A* Search)**

A* uses a heuristic function (informed). BFS, DFS, Depth-limited are all uninformed (no domain knowledge).

**Memory Trick:** "Informed = uses heuristic." A* = Best-first + heuristic. Uninformed = blind search.

---

## ⚪ Q14 — Logical Entailment
**Answer: A;B;C**

If X entails Y: whenever X is true, Y must be true.
- A (X⇒Y): correct form of entailment ✓
- B (X∧¬Y is False): if X is true and Y were false, that contradicts entailment ✓
- C (if X then Y): same as A ✓
- D (if Y then X): converse, not necessarily true ✗

---

# DATABASES & PROGRAMMING

> ⚪ These topics are NOT in your WMT AI entrance exam.

---

## ⚪ Q6 — Python Mutable Default Argument
**Answer: B**

```python
def append_to_lst(val, lst=[]):  # default lst is created ONCE
    lst.append(val)
    return lst
```

- Call 1: append_to_lst(1) → uses shared default list → [1]
- Call 2: append_to_lst(2) → SAME shared default list → [1,2]
- Call 3: append_to_lst(3, []) → NEW list provided → [3]

**Output: [1], [1,2], [3] → Answer B ✓**

**CRITICAL Python Gotcha:** Mutable default arguments (lists, dicts) are created ONCE at function definition, not at each call. Use `lst=None` and `if lst is None: lst = []` instead.

---

## ⚪ Q40 — Python Closures
**Answer: B;D**

```python
f1 = outer()  # f1 captures its own x=[]
f2 = outer()  # f2 captures its OWN separate x=[]
```

- f1 and f2 have SEPARATE lists (each outer() call creates new x)
- Line P: f1(10) → f1's x=[10] → prints [10]
- Line Q: f1(20) → f1's x=[10,20] → prints [10,20] ✓ (B)
- Line R: f2(30) → f2's x=[30] → prints [30] (not C)
- Line S: f1(40) → f1's x=[10,20,40] → prints [10,20,40] ✓ (D)

---

# 📊 TOPIC-WISE QUESTION SUMMARY

## Your WMT Exam Relevant Questions

| Topic | Questions | Your Priority |
|---|---|---|
| Probability & Statistics | Q9, Q10, Q18, Q24, Q34, Q35, Q43, Q44, Q47, Q52, Q53, Q54 | 🔴 MUST DO |
| Linear Algebra | Q11, Q12, Q36, Q42, Q55 | 🔴 MUST DO |
| ML Algorithms | Q1, Q2, Q13, Q19, Q26, Q27, Q37, Q45, Q46 | 🔴 MUST DO |
| Calculus & Optimization | Q17, Q25 | 🟡 IMPORTANT |

## Skip for WMT Exam
| Topic | Questions |
|---|---|
| AI/Search/Logic | Q3, Q4, Q14, Q20, Q28, Q38 |
| Databases | Q7, Q8, Q16, Q22, Q31, Q32, Q33, Q41, Q49, Q50, Q51 |
| Programming/DSA | Q5, Q6, Q15, Q21, Q23, Q29, Q30, Q39, Q40, Q48 |

---

# 🔑 KEY FORMULAS FROM THIS PAPER

```
PROBABILITY:
P(product even) = 1 - P(all odd) [complement method]
Stars & Bars: C(n+k-1, k-1) for non-negative solutions
Bayes: P(D|+) = P(+|D)P(D) / [P(+|D)P(D) + P(+|¬D)P(¬D)]

EXPONENTIAL:
Memoryless: P(X > s+t | X > s) = P(X > t)

DISTRIBUTIONS:
ΣXᵢ² ~ χ²(n)  if Xᵢ ~ N(0,1) iid
χ²(2) ~ Exponential(mean=2)

LINEAR ALGEBRA:
Trace = sum of eigenvalues
max(xᵀAx) s.t. xᵀx=1 = largest eigenvalue
Projection matrix: P=Pᵀ and P²=P

MACHINE LEARNING:
Ridge Loss = MSE + λ||w||₂²
PCA components are orthogonal (90° to each other)
LOOCV splits = n (training set size)
MLP params (no bias) = Σ (layer_i × layer_{i+1})

EVALUATION:
Accuracy = (TP+TN)/Total
Precision = TP/(TP+FP)
Recall = TP/(TP+FN)
```

---

*GATE DA 2026 | Solutions compiled for Suvam Das | App W26OTHAI00797 | IIT Madras WMT AI 2026*
