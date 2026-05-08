# 📘 TOPIC 1: Probability & Statistics
### IIT Madras WMT AI Entrance — Complete Notes
> 🔴 **HIGHEST PRIORITY** | ~25% of your exam marks come from here
> 📅 Study Days: 1–7

---

## 🧠 Why This Topic Matters
Every AI/ML algorithm is built on probability. When a spam filter says "90% chance this is spam" — that's probability. When a doctor's AI says "70% chance of disease" — that's probability + statistics. Master this and the rest of ML becomes easy.

---

# PART 1: COUNTING (Permutations & Combinations)

> Before probability, you need to COUNT outcomes. This is the foundation.

## 1.1 Factorial
```
n! = n × (n-1) × (n-2) × ... × 1
5! = 5 × 4 × 3 × 2 × 1 = 120
0! = 1  ← memorize this special case
```

## 1.2 Permutation — ORDER MATTERS

**"How many ways can I ARRANGE r items from n items?"**

```
P(n, r) = n! / (n-r)!
```

**Memory trick:** Think "PLACE" — Permutation = PLACEment, order matters.

**Example:** How many 3-letter codes from {A, B, C, D, E}?
```
P(5,3) = 5! / (5-3)! = 5! / 2! = 120 / 2 = 60
```

**Example:** How many ways can 5 people sit in 3 chairs?
```
P(5,3) = 5 × 4 × 3 = 60  ← (multiply down from n, r times)
```

## 1.3 Combination — ORDER DOESN'T MATTER

**"How many ways can I CHOOSE r items from n items?"**

```
C(n, r) = n! / [r! × (n-r)!]    also written as ⁿCᵣ or (n choose r)
```

**Memory trick:** Combination = Committee. A committee of 3 from 5 people — you don't care WHO sits in which chair.

**Example:** Choose 3 people from 5 for a committee:
```
C(5,3) = 5! / (3! × 2!) = 120 / (6 × 2) = 120/12 = 10
```

## 1.4 KEY SHORTCUT: When to use which?
| Question says... | Use |
|---|---|
| "arrange", "order", "sequence", "rank", "queue" | Permutation |
| "choose", "select", "committee", "group", "team" | Combination |

## ✅ Practice Questions

**Q1.** A PIN has 4 digits (0-9), no repetition. How many PINs possible?
> P(10,4) = 10×9×8×7 = **5040**

**Q2.** A team of 4 from 10 employees. How many combinations?
> C(10,4) = 10!/(4!×6!) = **210**

**Q3.** How many 3-digit numbers from {1,2,3,4,5} with no repetition?
> P(5,3) = 5×4×3 = **60**

---

# PART 2: PROBABILITY FOUNDATIONS

## 2.1 Sample Space and Events

- **Sample Space (S or Ω):** All possible outcomes
  - Toss 1 coin: S = {H, T}
  - Roll 1 die: S = {1, 2, 3, 4, 5, 6}
  - Toss 2 coins: S = {HH, HT, TH, TT}

- **Event:** A subset of the sample space
  - Event A = "get heads" = {H}
  - Event B = "get even number on die" = {2, 4, 6}

## 2.2 Probability Axioms (The 3 Rules)

These are the LAWS of probability — everything follows from them:

```
Axiom 1: P(A) ≥ 0       (probability is never negative)
Axiom 2: P(S) = 1        (something must happen)
Axiom 3: If A∩B = ∅ then P(A∪B) = P(A) + P(B)  (mutually exclusive events)
```

## 2.3 Core Probability Formula

```
P(Event) = Number of favourable outcomes / Total number of outcomes
```
This ONLY works when all outcomes are equally likely!

## 2.4 Types of Events

### Mutually Exclusive Events
- Cannot happen at the same time
- A die shows 3 AND shows 5 — impossible!
- P(A ∩ B) = 0
- **Addition Rule for ME events:** P(A ∪ B) = P(A) + P(B)

### Independent Events
- One event's outcome does NOT affect the other
- Tossing a coin twice — first toss doesn't affect second
- P(A ∩ B) = P(A) × P(B)
- **⚠️ EXAM TRAP:** Mutually exclusive ≠ Independent! In fact, if A and B are mutually exclusive AND both have P>0, they CANNOT be independent.

### Complementary Events
```
P(A does NOT happen) = P(A') = 1 - P(A)
```
**Tip:** "At least one" problems → use complement!
P(at least one) = 1 - P(none)

## 2.5 Addition Rule (General)
```
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
```
**Why subtract P(A∩B)?** Because you counted it twice!

**Visual (Venn Diagram logic):**
```
P(A or B) = (all of A) + (all of B) - (the overlap you counted twice)
```

**Three events version (rare but asked):**
```
P(A∪B∪C) = P(A)+P(B)+P(C) - P(A∩B) - P(B∩C) - P(A∩C) + P(A∩B∩C)
```

## ✅ Classic GATE-style Questions

**Q1.** In a class of 100: 60 play cricket, 50 play football, 25 play both. P(plays at least one sport)?
```
P(C∪F) = 60/100 + 50/100 - 25/100 = 0.6 + 0.5 - 0.25 = 0.85
```

**Q2.** P(A) = 0.4, P(B) = 0.3, A and B are independent. Find P(A∪B).
```
P(A∩B) = 0.4 × 0.3 = 0.12
P(A∪B) = 0.4 + 0.3 - 0.12 = 0.58
```

**Q3.** A coin is tossed 3 times. P(at least one head)?
```
P(at least one H) = 1 - P(no H) = 1 - (1/2)³ = 1 - 1/8 = 7/8
```

---

# PART 3: CONDITIONAL PROBABILITY

## 3.1 What is it?

**"Given that B happened, what's the probability A also happens?"**

```
P(A|B) = P(A ∩ B) / P(B)
```
Read as: "Probability of A GIVEN B"

**Real-world intuition:** You know it's raining. What's the probability your friend is late? The rain gives you extra information that changes your estimate.

**Example:** Cards from a deck (52 cards):
- P(King) = 4/52
- P(King | card is face card) = ?
  - Face cards = {Jack, Queen, King} = 12 cards
  - Kings among face cards = 4
  - P(King | face card) = 4/12 = 1/3

## 3.2 Multiplication Rule
```
P(A ∩ B) = P(A) × P(B|A)   OR   P(B) × P(A|B)
```

**Example:** P(pick 2 aces from deck without replacement)?
```
P(1st ace) = 4/52
P(2nd ace | 1st was ace) = 3/51
P(both aces) = (4/52) × (3/51) = 12/2652 ≈ 0.0045
```

## 3.3 Law of Total Probability
If B₁, B₂, ..., Bₙ partition the sample space:
```
P(A) = P(A|B₁)P(B₁) + P(A|B₂)P(B₂) + ... + P(A|Bₙ)P(Bₙ)
```

**Intuition:** Split the problem into cases, solve each case, add weighted by how likely each case is.

---

# PART 4: BAYES' THEOREM ⭐⭐⭐ (Always in Exam!)

## 4.1 The Formula
```
P(A|B) = P(B|A) × P(A) / P(B)
```

## 4.2 Full Form (Using Law of Total Probability for denominator):
```
P(Aᵢ|B) = P(B|Aᵢ) × P(Aᵢ) / [P(B|A₁)P(A₁) + P(B|A₂)P(A₂) + ...]
```

## 4.3 Terminology (Important for AI)
- **Prior probability P(A):** Your belief BEFORE seeing evidence
- **Likelihood P(B|A):** How likely is the evidence if A is true
- **Posterior probability P(A|B):** Updated belief AFTER seeing evidence
- **Evidence P(B):** Total probability of seeing the evidence

## 4.4 Step-by-Step Method for Bayes Problems:
```
Step 1: Identify the "hypothesis" events (A₁, A₂, ...)
Step 2: Write down all given probabilities
Step 3: Calculate P(B) using Law of Total Probability
Step 4: Apply Bayes formula
```

## ✅ Classic Bayes Problems

**Q1 (Medical Test — most common type):**
A disease affects 1% of population. Test is 95% accurate (true positive rate), 2% false positive rate.
Person tests positive. Probability they have disease?

```
P(Disease) = 0.01,   P(No Disease) = 0.99
P(+|Disease) = 0.95, P(+|No Disease) = 0.02

P(+) = P(+|D)×P(D) + P(+|¬D)×P(¬D)
     = 0.95×0.01 + 0.02×0.99
     = 0.0095 + 0.0198 = 0.0293

P(Disease|+) = 0.0095 / 0.0293 ≈ 0.324 ≈ 32.4%
```
**Key insight:** Even with accurate test, if disease is rare, most positives are false positives!

**Q2 (Factory Problem — second most common):**
Factory has 3 machines: M1 makes 50% of output, M2 makes 30%, M3 makes 20%.
Defect rates: M1=2%, M2=3%, M3=5%.
A defective item is found. Probability it came from M2?

```
P(M1)=0.5, P(M2)=0.3, P(M3)=0.2
P(D|M1)=0.02, P(D|M2)=0.03, P(D|M3)=0.05

P(D) = 0.02×0.5 + 0.03×0.3 + 0.05×0.2
     = 0.010 + 0.009 + 0.010 = 0.029

P(M2|D) = (0.03×0.3) / 0.029 = 0.009/0.029 ≈ 0.310 = 31%
```

---

# PART 5: RANDOM VARIABLES

## 5.1 What is a Random Variable?
A function that maps outcomes → numbers.
- Toss 2 coins: X = number of heads → X can be 0, 1, or 2
- Roll a die: Y = value shown → Y can be 1, 2, 3, 4, 5, 6

## 5.2 Discrete vs Continuous

| Feature | Discrete | Continuous |
|---|---|---|
| Values | Countable (0,1,2...) | Any real number in a range |
| Examples | # of emails, dice roll | Height, temperature, time |
| Described by | PMF (mass function) | PDF (density function) |

## 5.3 PMF (Probability Mass Function)
For discrete X:
```
P(X = xᵢ) = pᵢ

Requirements:
1. pᵢ ≥ 0 for all i
2. Σpᵢ = 1 (all probabilities sum to 1)
```

**Example — Roll a fair die:**
| X | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| P(X) | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 |
Sum = 1 ✓

## 5.4 PDF (Probability Density Function)
For continuous X:
```
P(a ≤ X ≤ b) = ∫ from a to b of f(x)dx

Requirements:
1. f(x) ≥ 0
2. ∫ from -∞ to +∞ of f(x)dx = 1
```
**Key Point:** For continuous variables, P(X = exact value) = 0! We only ask for P(a < X < b).

## 5.5 CDF (Cumulative Distribution Function)
```
F(x) = P(X ≤ x)
```
**Properties:**
- F(-∞) = 0, F(+∞) = 1
- F is non-decreasing
- For discrete: step function
- For continuous: smooth curve

**Exam use:** P(a < X ≤ b) = F(b) - F(a)

---

# PART 6: KEY STATISTICS MEASURES

## 6.1 Measures of Central Tendency

### Mean (Expected Value)
```
Discrete:   E[X] = Σ xᵢ × P(X = xᵢ)
Continuous: E[X] = ∫ x × f(x) dx
Sample mean: x̄ = (x₁ + x₂ + ... + xₙ) / n
```

### Median
- Middle value when sorted
- Not affected by outliers!
- If n is even: average of two middle values

### Mode
- Most frequent value
- A distribution can have multiple modes

**When to use which?**
- Mean: symmetric data, no outliers
- Median: skewed data, has outliers
- Mode: categorical data, most popular value

## 6.2 Measures of Spread

### Variance
```
Population: σ² = Σ(xᵢ - μ)² / N
Sample:     s² = Σ(xᵢ - x̄)² / (n-1)   ← note: divide by n-1, not n!
```
**Why n-1 for sample?** Bessel's correction — makes it unbiased estimate.

### Standard Deviation
```
σ = √(variance)
```

### Properties of Variance (EXAM FAVORITE!):
```
Var(aX + b) = a² × Var(X)    ← adding constant doesn't change spread!
Var(X + Y) = Var(X) + Var(Y)  if X, Y are independent
E[X²] = Var(X) + (E[X])²     ← very useful formula!
```

## 6.3 Correlation and Covariance

### Covariance
```
Cov(X, Y) = E[(X - μₓ)(Y - μᵧ)] = E[XY] - E[X]E[Y]
```
- Positive: X and Y increase together
- Negative: when X increases, Y decreases
- Zero: no LINEAR relationship (but could be non-linear!)

### Correlation (Pearson's r)
```
ρ(X, Y) = Cov(X, Y) / (σₓ × σᵧ)
```
**Range: -1 ≤ ρ ≤ 1**
- ρ = 1: perfect positive linear relationship
- ρ = -1: perfect negative linear relationship
- ρ = 0: no linear relationship

**Key exam point:** Correlation = 0 does NOT mean independent! (only true for normal distributions)

---

# PART 7: PROBABILITY DISTRIBUTIONS

## 7.1 DISCRETE DISTRIBUTIONS

### Uniform (Discrete)
All outcomes equally likely.
```
P(X = k) = 1/n    for k = 1, 2, ..., n
E[X] = (n+1)/2
Var[X] = (n²-1)/12
```
Example: Fair die — P(X=k) = 1/6, E[X] = 3.5

---

### Bernoulli Distribution
Single trial with success probability p.
```
P(X = 1) = p    (success)
P(X = 0) = 1-p  (failure)

E[X] = p
Var[X] = p(1-p)
```
Example: One coin flip where heads = success, p = 0.5.

---

### Binomial Distribution ⭐ (Very common in exam!)
**n independent Bernoulli trials, each with P(success) = p.**
**X = total number of successes.**

```
P(X = k) = C(n,k) × p^k × (1-p)^(n-k)

E[X] = np
Var[X] = np(1-p)
```

**When to identify Binomial:** Fixed n trials, each is success/fail, same p, independent.

**Example:** Roll a die 10 times. P(exactly 3 sixes)?
```
n=10, k=3, p=1/6, (1-p)=5/6
P(X=3) = C(10,3) × (1/6)³ × (5/6)⁷
= 120 × (1/216) × (78125/279936)
≈ 120 × 0.00463 × 0.2791 ≈ 0.155
```

**GATE-style shortcut:** Use E[X]=np for quick answers.
"Expected number of sixes in 10 rolls = 10 × 1/6 ≈ 1.67"

---

### Poisson Distribution ⭐ (Very common!)
**Counts the number of events in a fixed interval of time/space.**
**Events occur independently at constant average rate λ.**

```
P(X = k) = (e^(-λ) × λ^k) / k!

E[X] = λ
Var[X] = λ   ← mean equals variance! (unique property)
```

**When to use Poisson:**
- Number of calls per hour
- Number of typos per page
- Number of customers per day

**Example:** A website gets 5 visits/minute on average. P(exactly 3 visits in 1 minute)?
```
λ=5, k=3
P(X=3) = e^(-5) × 5³ / 3! = 0.0067 × 125 / 6 ≈ 0.1404
```

**Key insight:** Binomial → Poisson when n is large, p is small, and np = λ.

---

## 7.2 CONTINUOUS DISTRIBUTIONS

### Uniform (Continuous)
All values in [a, b] equally likely.
```
f(x) = 1/(b-a)    for a ≤ x ≤ b

E[X] = (a+b)/2
Var[X] = (b-a)²/12
P(c ≤ X ≤ d) = (d-c)/(b-a)
```

---

### Exponential Distribution ⭐
**Models time between events in a Poisson process.**
**Memoryless property — what makes it unique!**

```
f(x) = λe^(-λx)    for x ≥ 0
F(x) = 1 - e^(-λx)

E[X] = 1/λ
Var[X] = 1/λ²
```

**Memoryless property:** P(X > s+t | X > s) = P(X > t)
"If a bulb has survived 100 hours, its remaining life has same distribution as a new bulb."

**Example:** Average inter-arrival time = 5 min → λ = 1/5 = 0.2.
P(wait > 10 min) = e^(-0.2×10) = e^(-2) ≈ 0.135

---

### Normal Distribution ⭐⭐⭐ (Most Important!)
The "bell curve" — foundation of all statistics.

```
f(x) = (1/√(2πσ²)) × e^(-(x-μ)²/(2σ²))

E[X] = μ   (mean)
Var[X] = σ² (variance)
```

**The 68-95-99.7 Rule (MEMORIZE!):**
```
P(μ - σ < X < μ + σ)   = 0.6827 ≈ 68%
P(μ - 2σ < X < μ + 2σ) = 0.9545 ≈ 95%
P(μ - 3σ < X < μ + 3σ) = 0.9973 ≈ 99.7%
```

**Standardization (z-score):**
If X ~ N(μ, σ²), then Z = (X - μ)/σ ~ N(0, 1)
```
z-score = (value - mean) / standard deviation
```
This converts ANY normal to the standard normal (Z), so you can use z-tables!

**Standard Normal N(0,1):** Mean=0, Variance=1
- P(Z < 0) = 0.5
- P(Z < 1.96) ≈ 0.975
- P(-1.96 < Z < 1.96) ≈ 0.95

**Properties:**
- Symmetric around mean
- Mean = Median = Mode
- Sum of independent normals is normal: if X~N(μ₁,σ₁²) and Y~N(μ₂,σ₂²), then X+Y~N(μ₁+μ₂, σ₁²+σ₂²)

---

### t-Distribution
- Like normal but with heavier tails
- Used when sample size is small (n < 30) OR population variance unknown
- Parameterized by **degrees of freedom (df)**
- As df → ∞, t-distribution → Normal distribution

---

### Chi-Squared Distribution (χ²)
- Sum of squares of independent standard normals
- If Z₁, Z₂, ..., Zₖ ~ N(0,1) independent, then Z₁²+Z₂²+...+Zₖ² ~ χ²(k)
- Used in: hypothesis testing, goodness of fit, test of independence

---

### Poisson Distribution (moved to discrete above)

---

# PART 8: CENTRAL LIMIT THEOREM ⭐⭐ (ALWAYS ASKED)

## The Most Important Theorem in Statistics

**Statement:** If you take many large random samples from ANY distribution (with finite mean μ and variance σ²), the distribution of sample means will be approximately NORMAL, regardless of the original distribution's shape.

```
If X₁, X₂, ..., Xₙ are iid with mean μ and variance σ²:
X̄ ~ N(μ, σ²/n) approximately, when n is large (n ≥ 30)
```

**Key insight:** The standard deviation of the sample mean = σ/√n (called "standard error")

**Why it's powerful:** It lets us use normal distribution tools even when the underlying data isn't normal!

## CLT Example:
Weights of packages ~ any distribution with μ=500g, σ=50g.
50 packages are selected. P(sample mean < 490g)?

```
X̄ ~ N(500, 50²/50) = N(500, 50) → standard deviation of X̄ = √50 ≈ 7.07

z = (490 - 500) / 7.07 = -1.41

P(X̄ < 490) = P(Z < -1.41) ≈ 0.079 = 7.9%
```

---

# PART 9: CONFIDENCE INTERVALS

## What is it?
A range of values that likely contains the true population parameter.
"We are 95% confident the true mean lies between [a, b]."

## Formula for Mean (large sample):
```
CI = x̄ ± z* × (σ/√n)

where z* = 1.645 for 90% CI
      z* = 1.96  for 95% CI
      z* = 2.576 for 99% CI
```

## For small sample (σ unknown):
```
CI = x̄ ± t* × (s/√n)    ← use t-distribution with df = n-1
```

**Exam tip:** Wider CI = more confident. 99% CI is wider than 95% CI.

---

# PART 10: HYPOTHESIS TESTING ⭐⭐

## The Framework

```
Step 1: State H₀ (null hypothesis — "no effect", "no difference")
Step 2: State H₁ (alternative hypothesis)
Step 3: Choose significance level α (usually 0.05)
Step 4: Calculate test statistic
Step 5: Find p-value or critical value
Step 6: Decision: if p-value < α → REJECT H₀
```

## Type I and Type II Errors (EXAM FAVORITE!)

|  | H₀ is True | H₀ is False |
|---|---|---|
| **Reject H₀** | Type I Error (α) 😱 | Correct ✅ |
| **Don't Reject H₀** | Correct ✅ | Type II Error (β) 😱 |

- **Type I Error (False Positive):** Rejecting H₀ when it's actually true
  - Convicting an innocent person
  - P(Type I Error) = α = significance level
- **Type II Error (False Negative):** Not rejecting H₀ when it's false
  - Letting a guilty person go free
  - P(Type II Error) = β
- **Power = 1 - β:** Probability of correctly rejecting false H₀

## z-Test (Large Sample, σ known)
```
H₀: μ = μ₀

Test statistic: z = (x̄ - μ₀) / (σ/√n)

Reject H₀ if |z| > z_critical (1.96 for α=0.05 two-tailed)
```

## t-Test (Small Sample, σ unknown)
```
H₀: μ = μ₀

Test statistic: t = (x̄ - μ₀) / (s/√n)

df = n - 1
Reject H₀ if |t| > t_critical (from t-table)
```

**Two-Sample t-Test:** Compare means of two groups
```
t = (x̄₁ - x̄₂) / √(s²(1/n₁ + 1/n₂))
```

## Chi-Squared Test (χ²-Test)

### Goodness of Fit: Does data fit expected distribution?
```
χ² = Σ (Observed - Expected)² / Expected

df = (number of categories - 1)
```

### Independence Test: Are two categorical variables independent?
```
χ² = Σ (O - E)² / E    where E = (row total × column total) / grand total

df = (rows - 1) × (columns - 1)
```

## Exam-Style Question on Hypothesis Testing:

**Q:** A sample of 25 students has mean score 72, s=10. Test if population mean = 75 (α=0.05).
```
H₀: μ = 75, H₁: μ ≠ 75 (two-tailed)
t = (72 - 75) / (10/√25) = -3 / (10/5) = -3/2 = -1.5
df = 24, t_critical(0.025, 24) ≈ 2.064
|t| = 1.5 < 2.064 → FAIL TO REJECT H₀
Conclusion: No significant evidence that mean ≠ 75
```

---

# PART 11: CONDITIONAL EXPECTATION & VARIANCE

## Conditional Expectation
```
E[X|Y=y] = Σ x × P(X=x | Y=y)   for discrete
```
The expected value of X, given you know Y=y.

**Law of Total Expectation:**
```
E[X] = E[E[X|Y]]
```

## Conditional Variance
```
Var[X|Y=y] = E[X²|Y=y] - (E[X|Y=y])²
```

**Law of Total Variance:**
```
Var[X] = E[Var[X|Y]] + Var[E[X|Y]]
```

---

# 🔑 SUPER QUICK REFERENCE — All Key Formulas

```
COUNTING:
P(n,r) = n!/(n-r)!
C(n,r) = n!/[r!(n-r)!]

PROBABILITY:
P(A|B) = P(A∩B)/P(B)
P(A∪B) = P(A)+P(B)-P(A∩B)
Bayes: P(A|B) = P(B|A)×P(A)/P(B)

DISTRIBUTIONS:
Binomial:   E=np,  Var=np(1-p)
Poisson:    E=λ,   Var=λ
Exponential: E=1/λ, Var=1/λ²
Normal:     E=μ,   Var=σ²

STATISTICS:
z = (x - μ)/σ
t = (x̄ - μ₀)/(s/√n)
χ² = Σ(O-E)²/E

CLT: X̄ ~ N(μ, σ²/n)
CI: x̄ ± 1.96×σ/√n  (95%)
```

---

# 🎯 EXAM TIPS & TRICKS FOR PROBABILITY

1. **"At least one" → Always use complement:** P(at least 1) = 1 - P(none)

2. **Bayes problems — Always draw a tree:** List all possibilities, fill in numbers, then apply formula.

3. **Identify distribution quickly:**
   - Fixed trials, success/fail → **Binomial**
   - Count in interval, rare events → **Poisson**
   - Time between events → **Exponential**
   - Heights, errors, natural phenomena → **Normal**
   - Single trial → **Bernoulli**

4. **Normal distribution shortcuts:**
   - P(μ-σ to μ+σ) = 68%
   - P(μ-2σ to μ+2σ) = 95%
   - Symmetry: P(X > μ) = P(X < μ) = 0.5

5. **Variance property trick:** Var(3X+5) = 9×Var(X) — the constant 5 disappears!

6. **Mean of sum = sum of means** (always!): E[X+Y] = E[X] + E[Y]
   **Variance of sum = sum of variances** (ONLY if independent!)

7. **χ² test for independence:** If χ²_calculated > χ²_critical → variables are NOT independent

8. **CLT magic number:** n ≥ 30 is usually enough for CLT to apply

---

# 📝 TOPIC-WISE PRACTICE QUESTIONS (Exam-Style)

**Counting:**
- Q: How many ways to choose a team of 3 from 8 players? → C(8,3) = 56
- Q: How many 4-digit PINs with digits 1-9, no repeat? → P(9,4) = 9×8×7×6 = 3024

**Probability:**
- Q: P(A)=0.6, P(B)=0.4, P(A∩B)=0.2. Are A,B independent?
  - Check: P(A)×P(B) = 0.24 ≠ 0.20 → NOT independent

**Bayes:**
- Q: Email is spam 30% of time. Spam emails contain word "offer" 80%. Non-spam has "offer" 10%. Email has "offer". P(spam)?
  - P(S)=0.3, P(offer|S)=0.8, P(offer|¬S)=0.1
  - P(offer)=0.8×0.3+0.1×0.7=0.24+0.07=0.31
  - P(S|offer)=0.24/0.31 ≈ 0.774 = **77.4%**

**Distributions:**
- Q: Poisson with λ=3. P(X=0)?
  - e^(-3)×3⁰/0! = e^(-3) ≈ 0.0498

**Hypothesis:**
- Q: Which test for comparing means with n=10, unknown variance? → **t-test, df=9**
- Q: Which test to check if die is fair? → **Chi-squared goodness of fit test**

---

> 📌 **Next: Read `02_Linear_Algebra.md`**
