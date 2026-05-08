# 🎯 IIT Madras Web M.Tech in AI — Complete 1-Month Master Prep Guide

> **For:** A motivated working professional starting from scratch in maths/probability/vectors
> **Goal:** Clear the qualifier exam + interview, with rock-solid concepts
> **Promise:** If you follow this file daily, you will not just memorise — you will *understand*

---

## 📑 How to use this file

This guide is **one big file but split into clear parts** so you don't lose interest. Each part has:

1. **Plain-English explanation** — like talking to a friend
2. **Why this matters for AI** — so you stay motivated
3. **Tips & tricks** — shortcuts to remember things
4. **Worked examples** — see the trick in action
5. **Practice questions** — with answers
6. **Common mistakes** — what to avoid

**Reading order suggestion:**
- Day 0: Read Parts 1 & 2 (overview + exam reality check) — 1 hour
- Day 1 onwards: Follow the daily plan in Part 3
- Use Parts 4–8 as your textbook (one section per day)
- Part 9 = mock tests
- Part 10 = interview prep

---

# 📚 TABLE OF CONTENTS

| Part | Topic | Time needed |
|---|---|---|
| **Part 1** | What this exam *actually* is (real PYQ analysis) | 30 min read |
| **Part 2** | Diagnostic test — where do you stand? | 45 min |
| **Part 3** | The 30-day battle plan | 30 min read |
| **Part 4** | 🎲 Probability & Statistics (from zero) | 7 days |
| **Part 5** | 📐 Linear Algebra (no fear edition) | 7 days |
| **Part 6** | 📉 Optimization & Calculus basics | 3 days |
| **Part 7** | 🤖 Basic Machine Learning | 4 days |
| **Part 8** | 🐍 Python essentials (bonus, for interview) | 2 days |
| **Part 9** | Mock tests + 50 PYQ-style questions with solutions | 4 days |
| **Part 10** | Interview prep + final tips | 1 day |
| **Part 11** | Master formula sheet (print this!) | reference |

---

# PART 1 — What this exam ACTUALLY is

## 🔍 The truth about the IITM AI entrance test

Here's what I confirmed from real sources:

### Exam format (officially confirmed)
- **Duration:** ~2 hours
- **Mode:** Online proctored (computer-based)
- **Question types:**
  - **MCQ** — Multiple Choice (one right answer)
  - **MSQ** — Multiple Select (more than one right answer, all must be picked)
  - **NAT** — Numerical Answer Type (you type a number)
- **Sections (typical):**
  - Verbal/Comprehension aptitude (~5 questions)
  - Analytical aptitude / logical reasoning (~5 questions)
  - **Technical** (probability, linear algebra, calculus, ML) (~20 questions, weighted heaviest)

### What the syllabus officially says
1. **Probability and Statistics** — basic to intermediate
2. **Linear Algebra** — vectors, matrices, eigenvalues
3. **Optimization** — derivatives, gradient descent
4. **Basic Machine Learning** — regression, kNN, k-means

### The hidden message in the syllabus
The exam is asking ONE question: **"Can this person survive Term 1 of the M.Tech?"**

Term 1 is **Mathematical Foundations for Data Science**. So the entrance is *exactly* a maths-readiness check for ML.

---

## 🎯 What real previous-year questions look like

I pulled the actual 2023 IIT Madras Zanzibar M.Tech Data Science & AI screening test (same syllabus pattern). Here are sample questions to set your expectations:

### Sample 1: Linear Algebra (1 mark NAT)
> Given matrix A = [[2,0,0,0],[0,0,3,0],[0,0,3,0],[0,0,0,2]], find the sum of eigenvalues.
>
> **Answer:** 7 (sum of eigenvalues = trace = 2+0+3+2 = 7)

### Sample 2: Probability (1 mark MCQ)
> If X follows Bernoulli with p=0.4, what is P(X=1)?
>
> **Answer:** 0.4 (definition of Bernoulli)

### Sample 3: Calculus/Optimization (1 mark NAT)
> A drug efficacy is modelled as E(d) = (4/5)d − (2/3)(d−7)². Find the d that maximises E.
>
> **Answer:** 7.6 (set derivative to zero)

### Sample 4: Probability (2 mark NAT)
> Average calls to a call center = 5 per 10 minutes (Poisson). P(exactly 7 calls in 10 min) = ?
>
> **Answer:** ~0.104 (Poisson formula)

### Sample 5: Statistics (1 mark MCQ)
> A 95% confidence interval is [1.8, 2.2]. Which statement is correct?
>
> **Answer:** "With 95% confidence, the interval [1.8, 2.2] captures the true mean."
> (Common trap: it does NOT mean "95% probability the true mean is between 1.8 and 2.2")

### Sample 6: Linear Algebra (1 mark MCQ)
> Projection of b=[1,1] onto a=[1,0]?
>
> **Answer:** [1,0] (project formula gives only the x-component)

### Sample 7: Linear Algebra (2 mark MSQ)
> For matrix P with given values, which are true?
> a) eigenvectors are orthogonal
> b) eigenvectors are not orthogonal
> c) one eigenvalue is zero
> d) one eigenvalue is not zero
>
> **Tip:** symmetric matrix → eigenvectors orthogonal; check rank for zero eigenvalue.

### Sample 8: Probability (2 mark MCQ)
> Toss fair coin until getting exactly 2 heads. P(exactly k tosses needed) = ?
>
> **Answer:** (k−1) × 0.5^k (Negative binomial — last toss is the 2nd head, so first k−1 tosses give exactly 1 head)

### Sample 9: Optimization (2 mark NAT)
> min(x²+y²) such that x−y=1. What is minimum value?
>
> **Answer:** 0.5 (substitute y=x−1, minimise x²+(x−1)², get x=0.5, value = 0.5)

### Sample 10: Logical Reasoning (1 mark)
> 216 cubes painted blue, then arranged into a big cube whose faces are painted pink. How many small cubes have only ONE colour?
>
> **Answer:** 64 (the inner 4×4×4 = 64 cubes never see the outside, so still all blue)

---

## 🧠 What this tells us

After studying the actual paper, here's the **real difficulty**:

| Topic | Weight (approx) | Difficulty |
|---|---|---|
| Linear Algebra | 25% | Easy–medium |
| Probability | 20% | Medium (traps in interpretation) |
| Statistics & hypothesis | 10% | Easy if formulas memorised |
| Calculus / Optimization | 15% | Easy |
| Basic ML concepts | 10% | Easy (mostly definitions) |
| Verbal & Logical | 20% | Easy (don't lose marks here!) |

**Key insight:** The technical questions are NOT GATE-level hard. They test whether you understand the *meaning* of concepts, not whether you can do 5-step derivations.

**Trap warning:** Many questions are designed to catch people who *memorised without understanding*. Example: the "95% confidence interval" question. If you crammed without understanding what a CI actually means, you will pick the wrong option.

---

## ✅ What this means for YOU

You are starting from scratch and you have 1 month. That's actually **plenty of time** if you don't waste it.

**Don't do:**
- Random YouTube playlists with no exercises
- Long calculus textbook proofs
- Transformer / LLM theory
- Hard GATE-CS problems

**Do:**
- Build *intuition* first
- Memorise a small set of formulas perfectly
- Solve 8–15 problems daily
- Take 2 timed mocks in the last week

Now let's check where you stand.

---

# PART 2 — Diagnostic Test (Take this BEFORE you study)

> **Time:** 45 minutes. No calculator at first, then you may use one for arithmetic.
> Don't worry about the score. This tells us where to focus.

## Section A — Probability (5 Q)
1. P(A) = 0.6, P(B) = 0.5, P(A∩B) = 0.2. Find P(A∪B).
2. A bag has 3 red, 2 blue balls. P(red on 2nd draw | red on 1st draw, no replacement)?
3. P(disease) = 0.01. Test correctly identifies sick people 99% of the time, gives false positives 5% of the time. Given a positive test, what is P(actually sick)? (Bayes)
4. Mean of fair die roll?
5. X ~ Binomial(n=4, p=0.5). P(X=2) = ?

## Section B — Statistics (3 Q)
6. Mean of [4, 8, 12, 16, 20]?
7. The standard deviation of a dataset measures: (a) center (b) spread (c) shape (d) skew
8. p-value of 0.03 in a hypothesis test means: (a) null is 3% likely (b) probability of observing this data (or more extreme) if null is true is 3% (c) you are 97% confident in alternative (d) data is 3% accurate

## Section C — Linear Algebra (5 Q)
9. Magnitude of vector [3, 4]?
10. Dot product of [1, 2, 3] and [4, 5, 6]?
11. Multiply: [[1,2],[3,4]] × [[5,6],[7,8]]?
12. What is the rank of [[1,2],[2,4]]?
13. Eigenvalues of diagonal matrix [[3,0],[0,5]]?

## Section D — Calculus / Optimization (3 Q)
14. d/dx of (x² + 3x − 5)?
15. Find x that minimises f(x) = (x − 4)² + 7.
16. One step of gradient descent from x=2 for f(x)=x², learning rate α=0.1. New x?

## Section E — Machine Learning (4 Q)
17. Linear regression predicts: (a) categories (b) continuous numbers (c) clusters (d) probabilities only
18. kNN is for: (a) classification only (b) clustering only (c) classification & regression (d) probability
19. k-means is: (a) supervised (b) unsupervised (c) reinforcement (d) generative
20. Cross-validation prevents: (a) speed issues (b) overfitting + reliable error estimate (c) memory issues (d) all of these

---

## ✅ Diagnostic Answers

| Q | Answer | Quick reason |
|---|---|---|
| 1 | 0.9 | 0.6 + 0.5 − 0.2 |
| 2 | 2/4 = 0.5 | After removing 1 red, 2 red left out of 4 |
| 3 | ~16.8% | Bayes: (0.99 × 0.01)/(0.99 × 0.01 + 0.05 × 0.99) ≈ 0.168 |
| 4 | 3.5 | (1+2+3+4+5+6)/6 |
| 5 | 0.375 | C(4,2) × 0.5⁴ = 6 × 0.0625 |
| 6 | 12 | sum/5 |
| 7 | b | spread |
| 8 | b | this is the *correct* technical meaning |
| 9 | 5 | √(9+16) |
| 10 | 32 | 4+10+18 |
| 11 | [[19,22],[43,50]] | row × column |
| 12 | 1 | row 2 = 2× row 1 |
| 13 | 3 and 5 | diagonal entries |
| 14 | 2x + 3 | power rule |
| 15 | x = 4 | vertex of parabola |
| 16 | 1.6 | x − α(2x) = 2 − 0.1(4) = 1.6 |
| 17 | b | continuous |
| 18 | c | both |
| 19 | b | unsupervised |
| 20 | b | model validation purpose |

## 🎯 Score interpretation

| Score | Action |
|---|---|
| **0–6** | Start at the absolute basics. Spend full Week 1 on probability and Week 2 on linear algebra without rushing. |
| **7–12** | You have some base. Follow the standard 30-day plan. |
| **13–17** | Strong base. Skim Parts 4–6, focus on solving questions and mocks. |
| **18–20** | You probably don't need this guide as much — go straight to mock tests + advanced ML. |

**Don't be discouraged by a low score.** A 4/20 today and 18/20 in 4 weeks is normal if you study right.

---


# PART 3 — Your 30-Day Battle Plan

## ⏰ Time commitment

| Day type | Hours | Why |
|---|---|---|
| Weekday | 2.5–3 hrs | Sustainable + you have a job |
| Weekend | 5–6 hrs | Catch up + practice mocks |

Total = roughly **75–90 hrs in a month**. That's enough.

## 🧱 Daily template (don't skip any block)

```
🧠 45 min — LEARN one concept (read this guide / watch one short video)
✏️  45 min — WORKED EXAMPLES (do them on paper, not in your head)
🎯 45 min — PRACTICE QUESTIONS (timed, no peeking at solutions)
📋 20 min — FORMULA REVISION
📓 15 min — MISTAKE NOTEBOOK (write down what you got wrong + why)
```

The **Mistake Notebook** is the secret weapon. By Week 4 it will become your best revision material.

## 📅 Week-by-week roadmap

### Week 1 — Probability & Statistics (Days 1–7)
| Day | Topic |
|---|---|
| Day 1 | Sample space, events, basic probability rules |
| Day 2 | Conditional probability, independence, Bayes theorem |
| Day 3 | Random variables, PMF, PDF, expectation |
| Day 4 | Variance, std dev, Bernoulli, Binomial, Poisson |
| Day 5 | Normal distribution, z-score, descriptive stats |
| Day 6 | Sampling, CLT, standard error, confidence intervals |
| Day 7 | Hypothesis testing: z, t, chi-square, F-tests |

### Week 2 — Linear Algebra (Days 8–14)
| Day | Topic |
|---|---|
| Day 8 | Vectors: magnitude, addition, scalar multiplication |
| Day 9 | Dot product, distance, angle, unit vectors |
| Day 10 | Matrices: shapes, multiplication, transpose |
| Day 11 | Solving Ax = b, row operations |
| Day 12 | Rank, null space, linear independence |
| Day 13 | Projections, least squares, pseudo-inverse |
| Day 14 | Eigenvalues, eigenvectors, diagonalisation |

### Week 3 — Optimization + ML (Days 15–21)
| Day | Topic |
|---|---|
| Day 15 | Derivatives review, finding minima |
| Day 16 | Partial derivatives, gradient |
| Day 17 | Gradient descent, learning rate |
| Day 18 | Linear regression (simple) + least squares |
| Day 19 | Multiple regression, train/test, overfitting |
| Day 20 | Logistic regression, sigmoid, classification basics |
| Day 21 | kNN, k-means, cross-validation |

### Week 4 — Mocks + Revision (Days 22–30)
| Day | Topic |
|---|---|
| Day 22 | Probability + Stats revision (25 Q) |
| Day 23 | Linear Algebra revision (25 Q) |
| Day 24 | Optimization + Calculus revision (15 Q) |
| Day 25 | ML revision (20 Q) |
| Day 26 | **Mock Test 1** (90 min, full mix) |
| Day 27 | Mock 1 review + weak topic recovery |
| Day 28 | **Mock Test 2** (90 min) |
| Day 29 | Mock 2 review + final formula sheet |
| Day 30 | Light revision + interview prep + REST |

## 🛑 Rules that will save your prep
1. **Never skip the mistake notebook.** It's where real learning happens.
2. **Do problems on paper, not in your head.** You'll skip steps and convince yourself you understand when you don't.
3. **One topic per day, fully.** Don't jump.
4. **If a day is missed, slide everything by 1 day. Don't pile up.**
5. **Re-take the diagnostic test on Day 15.** Track your progress.

---


# PART 4 — 🎲 Probability & Statistics (from absolute zero)

> **Mindset reset:** Probability is NOT scary maths. It's just careful counting + a few formulas. Most exam questions are 2-line problems if you know the trick.

## 4.1 The mental model — what probability really is

**Probability = a number between 0 and 1 that tells you "how likely"**

- 0 = impossible
- 1 = certain
- 0.5 = 50/50

You can also think of it as: **"if you repeat this 100 times, how many times does the event happen?"**

That's it. The whole subject is built on that.

### Key vocabulary (memorise once, use forever)

| Word | Meaning | Example |
|---|---|---|
| **Experiment** | The thing you do | Roll a die |
| **Outcome** | One result | "Got a 4" |
| **Sample space (S)** | All possible outcomes | {1,2,3,4,5,6} |
| **Event** | A subset of outcomes | "Even number" = {2,4,6} |
| **P(A)** | Probability of event A | P(even) = 3/6 = 0.5 |

### The fundamental formula
```
P(A) = (number of favourable outcomes) / (total outcomes)
```
This works when all outcomes are **equally likely**.

---

## 4.2 The 5 Basic Rules (you need ALL of these)

### Rule 1: Probability is between 0 and 1
```
0 ≤ P(A) ≤ 1
```

### Rule 2: Total = 1
```
P(S) = 1   (something must happen)
```

### Rule 3: Complement
```
P(not A) = 1 − P(A)
```
**Trick:** If "at least one" appears in a question, use complement: P(at least one) = 1 − P(none).

### Rule 4: Addition rule (for "OR")
```
P(A ∪ B) = P(A) + P(B) − P(A ∩ B)
```
**Why subtract?** Because if you just add, you've counted the overlap twice.

If A and B are **mutually exclusive** (can't happen together), then P(A∩B) = 0, so:
```
P(A ∪ B) = P(A) + P(B)
```

### Rule 5: Multiplication rule (for "AND")
```
P(A ∩ B) = P(A) × P(B|A)
```
If A and B are **independent**, P(B|A) = P(B), so:
```
P(A ∩ B) = P(A) × P(B)
```

### 🔑 BIG TRAP: Independent ≠ Mutually Exclusive
This trips up 80% of beginners. Memorise this:

| Concept | Meaning | Math |
|---|---|---|
| **Mutually exclusive** | Can't both happen | P(A∩B) = 0 |
| **Independent** | One doesn't affect the other | P(A∩B) = P(A)·P(B) |

Example: rolling a die.
- "Get a 1" and "Get a 6" → mutually exclusive (can't both happen on one roll)
- "Get a 1 on first roll" and "Get a 6 on second roll" → independent

If two events are mutually exclusive AND have non-zero probability, they are **NOT** independent! (Because if A happens, B definitely doesn't.)

---

## 4.3 Conditional Probability

**P(A|B) means: "probability of A given that B has happened."**

Formula:
```
P(A|B) = P(A ∩ B) / P(B)
```

**Intuition:** B has already happened, so your "world" shrinks to just the outcomes inside B. Now ask: of those, what fraction is also in A?

### Worked example (must understand)
A bag has 5 red and 3 blue balls. You draw 2 without replacement.
Find P(2nd is red | 1st was red).

**Solution:**
- After 1st red is drawn, 4 red and 3 blue remain. Total 7.
- P(2nd is red | 1st red) = 4/7

You **shrink the world** to "after the first red is drawn." Done.

### Tip for exam
If a question says "given that...", it's asking for conditional probability. Just write down what's known after the "given" condition, and re-count.

---

## 4.4 Bayes' Theorem (the magic formula)

**The formula:**
```
P(A|B) = P(B|A) × P(A) / P(B)
```

**Why care?** Because in real life, you often know P(B|A) but want P(A|B).

**Example you MUST know (medical test):**
- 1% of people have a disease: P(D) = 0.01
- Test correctly identifies sick: P(+ | D) = 0.99
- Test gives false positive: P(+ | not D) = 0.05
- Question: You tested positive. What's P(disease)?

**Solution:**
```
P(D|+) = P(+|D) × P(D) / P(+)

P(+) = P(+|D)P(D) + P(+|not D)P(not D)
     = 0.99 × 0.01 + 0.05 × 0.99
     = 0.0099 + 0.0495
     = 0.0594

P(D|+) = (0.99 × 0.01) / 0.0594
       ≈ 0.167  (about 16.7%)
```

**🤯 Surprise:** Even after a positive test, there's only ~17% chance you have the disease. That's because the disease is rare!

### Bayes shortcut (memorise the recipe)
1. Write P(A) — the **prior**
2. Write P(B|A) — likelihood
3. Compute P(B) by **total probability**: sum over all causes
4. Plug in

### Common Bayes question shapes
- Disease testing
- Spam email classification
- "Coin came from biased or fair? You see HHHH..."
- Manufacturing: "Defective from machine A or B?"

---

## 4.5 Random Variables

A **random variable** is just a function that turns outcomes into numbers.

Example: X = number of heads in 2 coin flips. X can be 0, 1, or 2.

### Two types
| Type | Description | Tool |
|---|---|---|
| **Discrete** | Countable values (0, 1, 2, ...) | PMF |
| **Continuous** | Any value in a range | PDF |

### PMF (Probability Mass Function) — for discrete
For X = number of heads in 2 flips:

| x | P(X=x) |
|---|---|
| 0 | 1/4 |
| 1 | 2/4 |
| 2 | 1/4 |

The PMF must sum to 1.

### PDF (Probability Density Function) — for continuous
For continuous X (like height, weight, time):
- P(X = exact value) = 0  (because there are infinite values!)
- P(a ≤ X ≤ b) = area under PDF curve from a to b
- Total area = 1

### CDF (Cumulative Distribution Function)
F(x) = P(X ≤ x). Always increases from 0 to 1.

---

## 4.6 Expectation and Variance (the centre and spread)

### Expectation = mean = average
For discrete:
```
E[X] = Σ x · P(X = x)
```

Think of it as a **weighted average** where weights are probabilities.

**Example:** Fair die.
```
E[X] = 1(1/6) + 2(1/6) + ... + 6(1/6) = 21/6 = 3.5
```

### Variance = how spread out
```
Var(X) = E[X²] − (E[X])²
```
or equivalently:
```
Var(X) = E[(X − μ)²]
```

**Tip:** The first formula is easier in calculations. Compute E[X] and E[X²] separately.

### Standard deviation
```
σ = √Var(X)
```
SD has the same units as X (variance has squared units, which is why we take the root).

### Useful properties
```
E[aX + b] = aE[X] + b
Var(aX + b) = a²Var(X)        (the +b doesn't matter — shifting doesn't change spread)
E[X + Y] = E[X] + E[Y]        (always)
Var(X + Y) = Var(X) + Var(Y)  (only if X, Y independent)
```

---

## 4.7 Important Distributions (memorise these 4)

### 1. Bernoulli — single yes/no trial
- X ∈ {0, 1}
- P(X=1) = p, P(X=0) = 1−p
- E[X] = p
- Var(X) = p(1−p)

**Use:** Did the email click? Did the customer buy? Coin toss with success.

### 2. Binomial — sum of n Bernoullis
- "How many successes in n independent trials?"
- P(X = k) = C(n,k) · p^k · (1−p)^(n−k)
- E[X] = np
- Var(X) = np(1−p)

**Tip to remember:** C(n,k) = "ways to pick which k trials succeed"; p^k = those k succeed; (1−p)^(n−k) = the rest fail.

**Example:** 5 coin tosses, P(exactly 3 heads) = C(5,3) × 0.5³ × 0.5² = 10 × 0.03125 = 0.3125

### 3. Poisson — counting rare events in fixed interval
- Examples: calls per hour, defects per metre, accidents per day
- P(X = k) = e^(−λ) · λ^k / k!
- E[X] = λ, Var(X) = λ (mean = variance, unique to Poisson!)

**Real PYQ:** Avg 5 calls per 10 min, P(7 calls in 10 min)?
```
P(X=7) = e^(−5) × 5^7 / 7! = 0.00674 × 78125 / 5040 ≈ 0.1044
```

### 4. Normal (Gaussian) — the bell curve
- X ~ N(μ, σ²)
- Symmetric around μ
- 68% within ±1σ, 95% within ±2σ, 99.7% within ±3σ (the 68-95-99.7 rule!)

### Z-score (standardising)
```
z = (x − μ) / σ
```
This converts ANY normal variable to standard normal Z ~ N(0,1).

**Use:** Look up probabilities from z-tables.

---

## 4.8 Sample Statistics & Central Limit Theorem (CLT)

### Sample vs population
- **Population:** ALL data you'd ideally see (often impossible)
- **Sample:** A subset you actually collect

| Quantity | Population (unknown, want this) | Sample (computed) |
|---|---|---|
| Mean | μ | x̄ |
| Variance | σ² | s² |
| Std dev | σ | s |

### The Central Limit Theorem (CLT) — most important idea in statistics

**Plain English:**
> If you take many samples (each of size n) from any population (even a weird non-normal one) and compute the mean of each sample, the distribution of those sample means is approximately **Normal** when n is large enough (n ≥ 30 is a common rule).

**Formula:**
```
x̄ ~ Normal(μ, σ²/n)
Standard Error: SE = σ/√n
```

**Why it matters:** This is why hypothesis testing works on means even when the data isn't normal. Magic.

**Trap:** CLT is about the distribution of **means**, NOT individual data points.

---

## 4.9 Confidence Intervals (CI)

A 95% CI for the mean looks like:
```
CI = x̄ ± z* · (σ/√n)
```
where z* = 1.96 for 95%.

### What it MEANS (real exam trap!)

✅ **Correct interpretation:** "If we repeated this sampling process many times and built a CI each time, about 95% of those intervals would contain the true mean."

❌ **Wrong (but tempting):** "There's a 95% probability the true mean is in [1.8, 2.2]." — The true mean is FIXED. Probability is about the *interval*, not the mean.

This is exactly the IIT Madras 2023 PYQ. Don't fall for it.

---

## 4.10 Hypothesis Testing

### The 6-step process
1. **State H₀ (null)**: usually "no effect" / "no difference"
2. **State H₁ (alternative)**: what you suspect
3. **Choose significance level α** (usually 0.05)
4. **Compute test statistic** (z, t, χ², or F)
5. **Compute p-value** (or compare with critical value)
6. **Decide:** if p < α, reject H₀

### What is a p-value?
> p-value = probability of observing data this extreme (or more extreme) **assuming the null hypothesis is true**.

**Trap:** p-value is NOT P(H₀ is true)!

### Errors
- **Type I (α):** rejecting a TRUE null (false alarm)
- **Type II (β):** keeping a FALSE null (missed catch)

### Which test when? (this is the most asked exam question!)

| Situation | Test | Why |
|---|---|---|
| Compare 1 sample mean to a known value, σ known | **z-test** | Use normal distribution |
| Compare 1 sample mean, σ unknown, small n | **t-test** | Use t-distribution |
| Compare 2 sample means | **t-test (two-sample)** | |
| Test if categorical data fits an expected distribution | **chi-square (χ²)** | Tests counts |
| Test independence of two categorical variables | **chi-square** | Contingency table |
| Compare variances of 2 groups | **F-test** | Ratio of variances |
| Compare means of 3+ groups | **ANOVA (uses F)** | Generalised t-test |

### 🎯 Memorise this decision tree
```
Comparing means? 
   → 1 sample: z if σ known, t if not
   → 2 samples: two-sample t
   → 3+ samples: ANOVA (F-test)

Categorical / counts? 
   → chi-square

Comparing variances? 
   → F-test
```

---

## 4.11 Common Probability Mistakes (avoid these!)

| Mistake | Reality |
|---|---|
| "Independent = mutually exclusive" | Opposite, almost! |
| "P(A|B) = P(B|A)" | Almost never. Use Bayes. |
| "p-value is probability null is true" | NO. It's prob of data given null. |
| "95% CI: 95% chance true mean is here" | NO. CI catches mean 95% of the time on repeat. |
| "If E[X]=3, then X is around 3" | Not always! Could oscillate widely. Variance matters. |
| "Variance has same units as data" | NO. Variance is squared. SD has the same units. |
| "Poisson is for any counting" | Only for INDEPENDENT rare events at constant rate. |

---

## 4.12 Probability Practice Questions (with solutions)

### Q1 (1 mark, basic)
A bag has 4 red and 6 blue balls. Two balls drawn without replacement. P(both red)?

**Solution:** P(R₁) × P(R₂|R₁) = (4/10) × (3/9) = 12/90 = 2/15 ≈ 0.133

### Q2 (1 mark, conditional)
P(rain) = 0.3, P(traffic) = 0.4, P(rain ∩ traffic) = 0.2. P(traffic | rain)?

**Solution:** 0.2 / 0.3 = 2/3 ≈ 0.667

### Q3 (2 marks, Bayes)
20% of emails are spam. 90% of spam contains "free". 5% of normal emails contain "free". P(spam | "free")?

**Solution:**
```
P(free) = 0.9 × 0.2 + 0.05 × 0.8 = 0.18 + 0.04 = 0.22
P(spam | free) = 0.9 × 0.2 / 0.22 = 0.18/0.22 ≈ 0.818
```

### Q4 (1 mark, Binomial)
n=10, p=0.3. E[X]?

**Solution:** np = 3

### Q5 (2 marks, normal/z)
Heights N(170, 100) (so σ=10). P(height > 185)?

**Solution:** z = (185−170)/10 = 1.5. From z-table, P(Z > 1.5) ≈ 0.0668

### Q6 (Real PYQ-style: CLT)
Sample of size n=100 from population with σ=20. SE of x̄?

**Solution:** σ/√n = 20/10 = 2

### Q7 (Hypothesis trap)
A researcher gets p = 0.02. With α = 0.05, should they:
- (a) accept H₀
- (b) reject H₀
- (c) accept H₁
- (d) inconclusive

**Solution:** (b). 0.02 < 0.05, so reject H₀. Note: we say "reject H₀", we don't say "accept H₁" technically.

### Q8 (PYQ-style: which test?)
Comparing if two factories have the same mean output. Sample sizes 25 and 28, σ unknown. Which test?

**Solution:** Two-sample t-test.

### Q9 (PYQ: Poisson)
λ = 3 calls/hour. P(exactly 2 calls in an hour)?

**Solution:** e^(−3) × 3² / 2! = 0.0498 × 9/2 ≈ 0.224

### Q10 (Variance)
X has E[X]=4, E[X²]=20. Var(X)?

**Solution:** 20 − 16 = 4

---

## 4.13 Probability Mini Formula Sheet

```
P(A') = 1 − P(A)
P(A ∪ B) = P(A) + P(B) − P(A ∩ B)
P(A ∩ B) = P(A) · P(B|A)
   if independent: P(A) · P(B)
P(A|B) = P(A ∩ B) / P(B)
Bayes: P(A|B) = P(B|A) · P(A) / P(B)

Discrete:
E[X] = Σ x · P(X=x)
Var(X) = E[X²] − (E[X])²
σ = √Var

Bernoulli(p): mean = p, var = p(1−p)
Binomial(n,p): mean = np, var = np(1−p)
   P(X=k) = C(n,k) p^k (1−p)^(n−k)
Poisson(λ): mean = λ, var = λ
   P(X=k) = e^(−λ) λ^k / k!
Normal(μ,σ²): z = (x−μ)/σ

Sampling:
SE = σ/√n
CLT: x̄ ≈ Normal(μ, σ²/n) for large n
95% CI: x̄ ± 1.96·(σ/√n)

Tests:
z-test: σ known
t-test: σ unknown
chi-square: categorical / goodness-of-fit
F-test: comparing variances
ANOVA: comparing 3+ means
```

---

# PART 5 — 📐 Linear Algebra (No-Fear Edition)

> **Mindset reset:** Don't be scared of vectors and matrices. A vector is just a list of numbers. A matrix is just a grid of numbers. The "tricks" are just careful arithmetic. You CAN do this.

## 5.1 Why ML people care about Linear Algebra

Every ML model is basically:
- **Data = matrix** (rows = samples, columns = features)
- **Parameters = vector**
- **Predictions = matrix × vector**
- **"Training" = solving a system of equations**

So linear algebra is literally the language of ML. Once you internalise this, the maths feels useful instead of abstract.

---

## 5.2 Vectors — the building block

### What is a vector?
A vector is just a list of numbers.
```
v = [3, 4]      (2D vector — has 2 components)
v = [1, 2, 3]   (3D vector)
```

### Two ways to think about a vector
1. **An arrow from origin to a point** in space (geometry)
2. **A point in space** itself (data)

Both are valid. Use whichever helps you visualise.

### Vector addition (component-wise)
```
[1, 2] + [3, 4] = [1+3, 2+4] = [4, 6]
```

### Scalar multiplication (multiply each component)
```
3 · [1, 2] = [3, 6]
```

### Magnitude (length) of a vector
```
||v|| = √(v₁² + v₂² + ... + vₙ²)
```

**Example:** v = [3, 4]. ||v|| = √(9+16) = √25 = **5**.

**🎯 Trick:** [3,4,5] type vectors give whole-number magnitudes (Pythagorean triples). Examiners love these.

### Distance between two vectors
```
distance(a, b) = ||a − b||
```
Just subtract them and find magnitude of the result.

**Example:** a=[1,2], b=[4,6]. a−b=[−3,−4]. distance = 5.

---

## 5.3 Dot Product (THE most important operation)

### Definition
```
a · b = a₁b₁ + a₂b₂ + ... + aₙbₙ
```

**Example:** [1,2,3] · [4,5,6] = 4 + 10 + 18 = 32.

### Two beautiful interpretations

**1. Algebraic:** sum of products
**2. Geometric:** ||a|| · ||b|| · cos(θ), where θ is the angle between them

So:
```
cos(θ) = (a · b) / (||a|| · ||b||)
```

### What dot product tells you

| Dot product value | Meaning |
|---|---|
| > 0 | Vectors point in similar direction (angle < 90°) |
| = 0 | Vectors are **perpendicular** (orthogonal) |
| < 0 | Vectors point in opposite directions (angle > 90°) |

### 🔥 KEY EXAM FACT
**Two vectors are perpendicular ⟺ their dot product = 0.**

Memorise this. Many MCQs hinge on it.

---

## 5.4 Projections (the "shadow")

**Question:** Given vectors a and b, what's the shadow of b on a's direction?

**Formula:**
```
proj_a(b) = ((a · b) / (a · a)) · a
```

**Real PYQ:** Project b=[1,1] onto a=[1,0].

**Solution:**
- a · b = 1·1 + 0·1 = 1
- a · a = 1·1 + 0·0 = 1
- proj = (1/1) · [1,0] = **[1,0]**

**Why we care:** This is the foundation of **least squares regression** (more in Part 7).

---

## 5.5 Matrices — grids of numbers

### Notation
```
A = [[1, 2, 3],
     [4, 5, 6]]
```
This is a **2×3 matrix** (2 rows, 3 columns).

### Important matrix shapes

| Shape | Name | Example |
|---|---|---|
| n×n | Square | 3×3 |
| Square with 1s on diagonal, 0s elsewhere | **Identity (I)** | I = [[1,0],[0,1]] |
| Square with 0s off-diagonal | Diagonal | [[3,0],[0,5]] |
| Same as transpose | Symmetric | A = Aᵀ |

### Matrix multiplication
**Rule:** (m × p) · (p × n) = (m × n).
The inner numbers must match.

**Wrong:** Don't multiply element-by-element.
**Right:** Each entry of the result = dot product of one row × one column.

**Worked example:**
```
A = [[1,2],     B = [[5,6],
     [3,4]]          [7,8]]

A·B = [[1·5+2·7, 1·6+2·8],     [[19, 22],
       [3·5+4·7, 3·6+4·8]]  =   [43, 50]]
```

### 🔑 Properties to remember
- **NOT commutative:** A·B ≠ B·A in general
- **Associative:** (AB)C = A(BC)
- **Distributive:** A(B+C) = AB + AC
- (AB)ᵀ = BᵀAᵀ  (notice the order flip!)

### Transpose
Flip rows and columns:
```
A = [[1, 2],     Aᵀ = [[1, 3],
     [3, 4]]            [2, 4]]
```

### Identity matrix
A · I = I · A = A. (Identity is the "1" of matrices.)

---

## 5.6 Solving Ax = b (systems of equations)

The system:
```
2x + 3y = 7
x + 4y = 9
```

In matrix form:
```
A = [[2, 3],   x = [x],   b = [7]
     [1, 4]]      [y]        [9]

A · x = b
```

### Three possible answers
1. **Unique solution** — det(A) ≠ 0, full rank
2. **No solution** — equations contradict
3. **Infinite solutions** — equations are dependent

**Real PYQ from 2023:** Given P and b, "the system Px = b has..."  
**Trick:** Try to compute the determinant or check rank vs augmented rank. If they don't match → no solution.

### How to check (small matrices)
- 2×2: det(A) = ad − bc. Non-zero → unique solution.
- 3×3: use cofactor expansion or row reduce.

**Tip:** For 2×2, finding x = (1/det) · [[d,−b],[−c,a]] · b gives you the answer instantly.

---

## 5.7 Rank (and why it matters)

**Rank = number of linearly independent rows (or columns).**

It's a measure of how much "real information" the matrix contains.

**Example 1:**
```
A = [[1, 2],
     [2, 4]]
```
Row 2 = 2 × Row 1. So rank = 1 (only one independent row).

**Example 2:**
```
A = [[1, 0],
     [0, 1]]
```
Rows are independent. Rank = 2.

### Properties
- rank(A) ≤ min(rows, cols)
- "Full rank" = max possible rank
- Full rank square matrix is **invertible**

### Why it matters in ML
- If your data matrix is rank-deficient → features are redundant → some are linear combinations of others → least squares fails (singular matrix)

---

## 5.8 Null Space (the "kernel")

The **null space** of A = all vectors x such that Ax = 0.

Think of it as: "directions where A flattens everything to zero."

- If null space is just {0}, the matrix is "non-degenerate" (good).
- If null space has more vectors, there's redundancy.

**Connection:** rank + nullity = n  (where n = number of columns; this is the "rank-nullity theorem")

For exam purposes: just understand that null space measures "degeneracy" of the matrix.

---

## 5.9 Eigenvalues and Eigenvectors

### The definition
For a square matrix A, an **eigenvector** v and **eigenvalue** λ satisfy:
```
A · v = λ · v
```

In words: when A acts on v, the result is just v scaled by λ. The direction doesn't change.

### Why care?
- Eigenvalues tell you the "stretch factors" of A
- Eigenvectors tell you the "preferred directions"
- Used in PCA, stability analysis, neural network weight analysis

### How to find them (small matrices)

For A = [[a, b], [c, d]]:
```
det(A − λI) = 0
(a−λ)(d−λ) − bc = 0
λ² − (a+d)λ + (ad−bc) = 0
```

Solve quadratic for λ.

### 🎯 Super important shortcuts

**1. Sum of eigenvalues = trace (sum of diagonal):**
```
λ₁ + λ₂ + ... = a₁₁ + a₂₂ + ... + aₙₙ
```

**2. Product of eigenvalues = determinant:**
```
λ₁ × λ₂ × ... = det(A)
```

**3. Diagonal matrix:** eigenvalues = diagonal entries (read them off!)

**4. Triangular matrix:** eigenvalues = diagonal entries.

**REAL PYQ:** Sum of eigenvalues of [[2,0,0,0],[0,0,3,0],[0,0,3,0],[0,0,0,2]]?
**Answer:** trace = 2+0+3+2 = **7**. (Don't even compute eigenvalues!)

### Symmetric matrix bonus property
If A = Aᵀ (symmetric):
- All eigenvalues are real
- Eigenvectors are **orthogonal** to each other

This is huge for exam MSQs about symmetric matrices.

### Eigenvalue tricks for MCQs
| Operation on A | Effect on eigenvalues |
|---|---|
| A → kA | λ → kλ |
| A → A + cI | λ → λ + c |
| A → A⁻¹ | λ → 1/λ |
| A → A² | λ → λ² |

**PYQ:** Eigenvalues of (P + 2I)⁻¹ if P = [[2,1],[0,3]]?
- P is upper triangular, so its eigenvalues are 2 and 3.
- P + 2I has eigenvalues 4 and 5.
- (P+2I)⁻¹ has eigenvalues 1/4 and 1/5.
- **Answer: 1/4, 1/5**

---

## 5.10 Pseudo-inverse and Least Squares

### Why we need pseudo-inverse
Normal inverse A⁻¹ only exists for square invertible matrices. But in ML, our data matrices are usually **tall** (more samples than features) and we still want to "solve" Ax = b.

### Pseudo-inverse A†
```
A† = (AᵀA)⁻¹ Aᵀ      (when A has full column rank)
```

### The least-squares solution
For Ax = b (when no exact solution exists):
```
Best x = A† · b = (AᵀA)⁻¹ Aᵀ b
```

This minimises ||Ax − b||².

### Why this matters
**This IS linear regression!**
- A = data matrix (rows = samples, columns = features)
- x = parameters (the weights)
- b = target values
- A†b = optimal weights (least squares solution)

### Properties of pseudo-inverse (PYQ alert)
- (A†)† = A ✓
- (Aᵀ)† = (A†)ᵀ ✓
- A† = A only if A is special (orthogonal, etc.) — usually NOT true
- A† = (AᵀA)†Aᵀ — true only under certain conditions, generally NOT

---

## 5.11 Linear Algebra Common Mistakes

| Mistake | Truth |
|---|---|
| AB = BA always | NO. Matrix multiplication is non-commutative. |
| Multiply matrices element-wise | NO. Use row × column dot products. |
| (AB)ᵀ = AᵀBᵀ | NO. It's BᵀAᵀ (order flips). |
| Det(A+B) = det(A)+det(B) | NO. There's no such formula. |
| Eigenvalue of A+I = eigenvalue of A | NO. It's λ+1. |
| If Ax = 0, then A = 0 or x = 0 | NO. Nontrivial null space exists. |
| Rank = number of rows | Only for full row rank. |
| Independent vectors are orthogonal | NO. Different concepts. (Orthogonal IS independent, but not vice versa.) |

---

## 5.12 Linear Algebra Practice Problems

### Q1 (Magnitude)
Find ||[1, −2, 2]||.
**Solution:** √(1+4+4) = √9 = **3**.

### Q2 (Dot product)
[2, 3] · [4, −1] = ?
**Solution:** 8 − 3 = **5**.

### Q3 (Orthogonal check)
Are [1, 2] and [4, −2] orthogonal?
**Solution:** Dot = 4 − 4 = 0. **Yes**.

### Q4 (Multiplication)
A = [[1,0],[2,1]], B = [[3,4],[5,6]]. Find AB.
**Solution:**
```
[[1·3+0·5, 1·4+0·6],   [[3, 4],
 [2·3+1·5, 2·4+1·6]] =  [11, 14]]
```

### Q5 (Rank)
Rank of [[1,1,1],[2,2,2],[3,3,3]]?
**Solution:** All rows are multiples of [1,1,1]. **Rank = 1**.

### Q6 (PYQ: Sum of eigenvalues)
Sum of eigenvalues of [[1,2,3],[4,5,6],[7,8,9]]?
**Solution:** trace = 1+5+9 = **15**.

### Q7 (PYQ: Eigenvalues of triangular)
Eigenvalues of [[5,7],[0,3]]?
**Solution:** Upper triangular → diagonal entries: **5 and 3**.

### Q8 (Projection)
Project [3, 4] onto [1, 0].
**Solution:** dot = 3, ||a||² = 1, so proj = 3·[1,0] = **[3, 0]**.

### Q9 (System of equations)
Does [[1,2],[2,4]] x = [3,5] have a solution?
**Solution:** Row 2 = 2·Row 1 of A, but b₂ ≠ 2·b₁ (5 ≠ 6). **No solution**.

### Q10 (Eigenvalue of inverse)
Eigenvalues of A are 2 and 3. Eigenvalues of A⁻¹?
**Solution:** **1/2 and 1/3**.

### Q11 (Composition — PYQ)
T(x) = Ax where A = [[1,2],[3,4]]. T(T(x)) = Px. Find P.
**Solution:** P = A². Compute:
```
A² = [[1·1+2·3, 1·2+2·4], [3·1+4·3, 3·2+4·4]]
   = [[7, 10], [15, 22]]
```
**Answer:** P = [[7,10],[15,22]]

### Q12 (Determinant)
det([[2,3],[1,4]]) = ?
**Solution:** 2·4 − 3·1 = 5.

### Q13 (Trace property)
If trace(A) = 5 and A is 2×2 with det(A) = 6, find eigenvalues.
**Solution:** λ₁+λ₂=5, λ₁λ₂=6 → solve: λ² − 5λ + 6 = 0 → **λ = 2, 3**.

### Q14 (Identity property)
What is I·v for any v?
**Solution:** **v** (identity does nothing).

### Q15 (Symmetric MSQ-style)
For a symmetric matrix, which are TRUE?
- a) eigenvalues are real ✓
- b) eigenvectors are orthogonal ✓
- c) eigenvalues are positive — only if positive definite (not always)
- d) det = 0 — only if singular

---

## 5.13 Linear Algebra Mini Formula Sheet

```
Vectors:
  ||v|| = √(Σ vᵢ²)
  a · b = Σ aᵢbᵢ = ||a||·||b||·cos(θ)
  distance(a,b) = ||a − b||
  cos(θ) = (a·b)/(||a||·||b||)

Projection of b onto a:
  proj_a(b) = ((a·b)/(a·a)) · a

Matrices:
  A · B is valid iff cols(A) = rows(B)
  (AB)ᵀ = BᵀAᵀ
  A·I = I·A = A
  
Solving Ax = b:
  Unique solution iff det(A) ≠ 0
  
Rank:
  rank(A) ≤ min(rows, cols)
  rank + nullity = number of cols
  
Eigenvalues:
  Av = λv
  Σλᵢ = trace(A)  (sum of diagonal)
  Πλᵢ = det(A)
  Triangular/diagonal: eigenvalues = diagonal entries
  Symmetric: real eigenvalues, orthogonal eigenvectors

Pseudo-inverse:
  A† = (AᵀA)⁻¹Aᵀ  (when AᵀA is invertible)
  Best fit Ax = b: x = A†b (minimises ||Ax−b||²)

Eigenvalue tricks:
  λ(kA) = k·λ
  λ(A + cI) = λ + c
  λ(A⁻¹) = 1/λ
  λ(Aⁿ) = λⁿ
```

---

# PART 6 — 📉 Optimization & Calculus Basics

> **Mindset reset:** Calculus for ML is NOT scary. You only need: derivatives = slope, gradient = multivariable slope, gradient descent = walk downhill. That's 90% of what you need.

## 6.1 Why ML cares about optimization

Every ML algorithm has this structure:
1. Define a **loss function** L (how bad your predictions are)
2. **Minimise** L by adjusting parameters
3. The minimum gives you the "best" model

So optimization = finding the bottom of a mathematical valley. That's literally it.

---

## 6.2 Derivatives — the slope at a point

**The derivative f'(x) = slope of f at x.**

### Common derivatives (memorise these!)
```
f(x) = c       → f'(x) = 0      (constant has slope 0)
f(x) = x       → f'(x) = 1
f(x) = xⁿ      → f'(x) = n·xⁿ⁻¹    (the power rule!)
f(x) = eˣ      → f'(x) = eˣ      (special!)
f(x) = ln(x)   → f'(x) = 1/x
f(x) = sin(x)  → f'(x) = cos(x)
f(x) = cos(x)  → f'(x) = −sin(x)
```

### Operating rules
```
(f + g)' = f' + g'      (linearity)
(c·f)' = c·f'
(f · g)' = f'g + fg'    (product rule)
(f/g)' = (f'g − fg')/g²  (quotient rule)
(f(g(x)))' = f'(g(x)) · g'(x)  (CHAIN RULE — most important!)
```

### Worked examples
1. d/dx (x² + 3x − 5) = 2x + 3
2. d/dx (3x⁴) = 12x³
3. d/dx ((x²+1)³) = 3(x²+1)² · 2x  [chain rule]
4. d/dx (x · eˣ) = eˣ + x·eˣ = (1+x)eˣ  [product rule]

---

## 6.3 Finding minima and maxima

### The basic recipe (one variable)
1. Compute f'(x)
2. Solve f'(x) = 0  → these are **critical points**
3. Use f''(x) to classify:
   - f''(x) > 0 → minimum (curve bowl-up)
   - f''(x) < 0 → maximum (curve bowl-down)
   - f''(x) = 0 → inconclusive (could be inflection)

### Worked Example (PYQ-style)
**Minimise f(x) = (x − 4)² + 7.**
- f'(x) = 2(x − 4) = 0 → x = 4
- f''(x) = 2 > 0 → minimum
- Min value = (0)² + 7 = 7

### Real PYQ
**E(d) = (4/5)d − (2/3)(d−7)². Find d that maximises E.**
- E'(d) = 4/5 − (4/3)(d − 7) = 0
- 4/5 = (4/3)(d − 7)
- (3/5) = d − 7
- d = 7.6 ✓

---

## 6.4 Multi-variable: Partial Derivatives

For a function f(x, y) of two variables:
- ∂f/∂x = derivative treating y as constant
- ∂f/∂y = derivative treating x as constant

**Example:** f(x, y) = x² + 3xy + y²
- ∂f/∂x = 2x + 3y
- ∂f/∂y = 3x + 2y

### Gradient
The **gradient** is the vector of all partial derivatives:
```
∇f = [∂f/∂x, ∂f/∂y, ...]
```

For our example: ∇f = [2x + 3y, 3x + 2y]

### What gradient means
- Direction of **steepest ascent** (uphill, fastest)
- Magnitude = how steep
- At a minimum/maximum, ∇f = 0 (zero vector)

### 🎯 Trick: To go DOWN (minimise), go in direction **−∇f**.

---

## 6.5 Gradient Descent (the heart of ML)

**The update rule:**
```
x_new = x_old − α · ∇f(x_old)
```
where α (alpha) is the **learning rate** (a small positive number).

### Step-by-step example
Minimise f(x) = x². Start at x = 4, α = 0.1.

- f'(x) = 2x
- Step 1: x = 4 − 0.1 × (2×4) = 4 − 0.8 = 3.2
- Step 2: x = 3.2 − 0.1 × 6.4 = 3.2 − 0.64 = 2.56
- Step 3: x = 2.56 − 0.1 × 5.12 = 2.048
- ... eventually converges to 0 ✓

### Effect of learning rate

| α (learning rate) | Effect |
|---|---|
| Too small | Very slow convergence |
| Just right | Smooth, fast convergence |
| Too large | Overshoots, may diverge or oscillate wildly |

### Local vs Global Minimum
- **Local minimum:** lowest in a neighbourhood
- **Global minimum:** lowest anywhere

For convex functions (like x², MSE loss), local = global. For non-convex (deep neural networks), they differ. Gradient descent might get stuck in a local minimum — a real concern in deep learning.

---

## 6.6 Constrained Optimization (a glimpse)

If you have a constraint like g(x, y) = 0, you can:

**Method 1: Substitution**
Solve constraint for one variable, plug into the objective.

**PYQ:** min(x² + y²) such that x − y = 1.
- From constraint: y = x − 1
- Plug in: f(x) = x² + (x−1)² = 2x² − 2x + 1
- f'(x) = 4x − 2 = 0 → x = 0.5
- y = −0.5
- Min value = 0.25 + 0.25 = **0.5** ✓

**Method 2: Lagrange multipliers** (more advanced — likely not on entrance, but useful to know it exists)

---

## 6.7 Convex vs Non-Convex

A function is **convex** if any line segment between two points on the curve lies *above* the curve.

| Convex | Non-convex |
|---|---|
| Bowl shape | Hills + valleys |
| One global min | Multiple local minima |
| GD always finds global min | GD can get stuck |

### Examples
- Convex: x², |x|, eˣ, MSE loss
- Non-convex: sin(x), neural network loss surfaces

---

## 6.8 Common Optimization Mistakes

| Mistake | Truth |
|---|---|
| Setting derivative = 0 always gives min | Could be max or saddle |
| Bigger learning rate = faster convergence | True up to a point, then catastrophic |
| Gradient points to minimum | NO. It points to maximum (steepest ascent). |
| GD always finds global min | Only for convex functions |
| Critical point = minimum | Could be max, saddle, inflection |

---

## 6.9 Optimization Practice Problems

### Q1
d/dx (5x³ − 2x + 7)?
**Solution:** 15x² − 2

### Q2
Find x that minimises f(x) = 2x² − 8x + 5.
**Solution:** f'(x) = 4x − 8 = 0 → x = 2

### Q3
∂/∂x (3x²y + xy² + y³)?
**Solution:** 6xy + y²

### Q4
Gradient of f(x,y) = x² + 4xy + y² at (1, 2)?
**Solution:** ∇f = [2x + 4y, 4x + 2y] at (1,2) = [10, 8]

### Q5 (PYQ-style)
Minimum value of x² − 4x + 7.
**Solution:** vertex at x=2, min = 4 − 8 + 7 = 3.

### Q6 (Gradient Descent step)
f(x) = x² − 4x. Start at x=5, α=0.5. New x?
**Solution:** f'(x) = 2x−4. x_new = 5 − 0.5·(6) = 5 − 3 = 2.

### Q7 (Conceptual)
What does it mean if α is too large?
**Answer:** Overshooting — gradient descent jumps over the minimum and may diverge.

### Q8 (PYQ-style)
min(x² + y²) such that 2x + y = 5. Min value?
**Solution:** y = 5 − 2x. f = x² + (5−2x)² = 5x² − 20x + 25. f' = 10x − 20 = 0 → x = 2, y = 1. Min = 4 + 1 = **5**.

---

## 6.10 Optimization Mini Formula Sheet
```
Power rule: d/dx xⁿ = n·xⁿ⁻¹
Chain rule: d/dx f(g(x)) = f'(g(x)) · g'(x)
Product: (fg)' = f'g + fg'

To find minimum of f:
  1. f'(x) = 0
  2. Check f''(x) > 0

Gradient: ∇f = [∂f/∂x₁, ∂f/∂x₂, ...]

Gradient Descent:
  x_new = x_old − α · ∇f(x_old)

For constraint min: substitute, then minimise.
```

---

# PART 7 — 🤖 Basic Machine Learning

> **Mindset reset:** ML is just "fit a function to data". The 5 algorithms in your syllabus are 5 different recipes for fitting. Don't memorise — *understand the recipe*.

## 7.1 The big picture

### The 3 types of ML

| Type | What it does | Has labels? | Examples |
|---|---|---|---|
| **Supervised** | Learn input→output mapping | YES | Regression, Classification |
| **Unsupervised** | Find structure in data | NO | Clustering, dimensionality reduction |
| **Reinforcement** | Learn from rewards | reward signal | Game playing, robots |

**Within supervised:**
- Predict a **number** → Regression (e.g., house price)
- Predict a **category** → Classification (e.g., spam/not spam)

### The standard ML workflow
1. **Collect data**
2. **Split** into train and test
3. **Train** model on train data
4. **Evaluate** on test data
5. **Tune** hyperparameters (cross-validation)
6. **Deploy**

---

## 7.2 Linear Regression (the foundation)

### Simple Linear Regression
Predict y from a single feature x:
```
y = w·x + b   (or sometimes: y = β₀ + β₁·x)
```
- w = slope (also called β₁)
- b = intercept (β₀)

### Multiple Linear Regression
Multiple features:
```
y = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
```

In matrix form: **y = Xw + b**

This is exactly the linear algebra you learned!

### How do we find w?

**Loss function: Mean Squared Error (MSE)**
```
MSE = (1/n) · Σ (yᵢ − ŷᵢ)²
```
where ŷᵢ is the prediction.

**The "least squares" solution** minimises MSE. Closed-form:
```
w = (XᵀX)⁻¹ Xᵀy
```

This is the **pseudo-inverse** from linear algebra! 🎯

### Why squared errors?
- Penalises large errors more
- Math is cleaner (differentiable)
- Geometric interpretation: projection of y onto column space of X

### Worked example
Data: (1,2), (2,3), (3,5).
Best fitting line? You'd compute slope and intercept using least-squares formula.
For exam: just understand the *concept* + the formula.

### Linear regression assumptions
1. Linear relationship between x and y
2. Errors are independent
3. Errors have constant variance (homoscedasticity)
4. Errors are normally distributed (for inference)

---

## 7.3 Logistic Regression (despite the name, it's classification!)

### The problem
Linear regression outputs any real number. For classification, we want a **probability between 0 and 1**.

### The trick: sigmoid (logistic) function
```
σ(z) = 1 / (1 + e⁻ᶻ)
```
- σ(0) = 0.5
- σ(+∞) → 1
- σ(−∞) → 0

### The model
```
P(y=1 | x) = σ(w·x + b)
```

### Decision rule
- If P > 0.5 → predict class 1
- Else predict class 0

### Key facts
- Output: **probability** (so it's NOT regression in the traditional sense!)
- Used for **binary** classification primarily
- Multinomial extension: softmax

### Loss function: Cross-entropy (log loss)
```
L = −[y·log(p) + (1−y)·log(1−p)]
```
This is the standard classification loss.

---

## 7.4 k-Nearest Neighbours (kNN)

### The idea (simplest possible)
> "I am like my nearest neighbours."

To classify a new point:
1. Find the **k** closest training points (by Euclidean distance)
2. Take a **vote** — most common class among neighbours wins

For regression: take **average** of neighbours' values.

### Choosing k
- Small k (e.g., k=1): very sensitive, can overfit
- Large k: smooth boundary, can underfit
- **Rule of thumb:** k = √n where n is training size

### Pros / Cons
| Pros | Cons |
|---|---|
| Simple, intuitive | Slow at prediction time (computes distance to all points) |
| No training | Curse of dimensionality (poor in high dims) |
| Works for both classification & regression | Need to standardise features |

### kNN vs k-means (THE most common confusion)
| | kNN | k-means |
|---|---|---|
| Type | Supervised | Unsupervised |
| Purpose | Classification/regression | Clustering |
| Uses labels? | YES | NO |
| What is k? | # neighbours | # clusters |

If you remember nothing else, remember this table.

---

## 7.5 k-Means Clustering

### The idea
Partition data into k groups by closeness to "centroids."

### Algorithm
1. **Initialise** k centroids randomly
2. **Assign** each point to the nearest centroid
3. **Update** centroids = mean of points assigned to it
4. **Repeat** until centroids stop moving

### Choosing k
- The **elbow method:** plot total within-cluster variance vs k. Pick the "elbow."
- Silhouette score
- Domain knowledge

### Pros / Cons
| Pros | Cons |
|---|---|
| Fast, simple | Need to pick k |
| Scales well | Sensitive to initialisation |
| Works on numeric data | Assumes spherical clusters |
| | Sensitive to outliers |

### Assumptions
- Clusters are roughly spherical
- Similar sizes
- Use Euclidean distance (so standardise features!)

---

## 7.6 Train/Test Split & Cross-Validation

### Why split?
If you train and test on the same data, you can't tell if the model is *memorising* or *generalising*.

### Standard split
- 70-80% training
- 20-30% test
- Sometimes also a **validation** set (for hyperparameter tuning)

### Cross-Validation (CV)
**k-fold CV:**
1. Split data into k equal folds
2. For each fold:
   - Train on k−1 folds
   - Test on the remaining fold
3. Average the k test scores

Most common: **5-fold or 10-fold CV**.

### Why use CV?
- Better estimate of model performance (uses all data for both train & test)
- Reduces variance of the performance estimate
- Especially useful for small datasets

### Leave-one-out CV (LOOCV)
k = n. Each point is held out once.

---

## 7.7 Overfitting and Underfitting

### Underfitting
- Model is too simple
- High train error AND high test error
- Example: fit a straight line to clearly curved data

### Overfitting
- Model is too complex
- LOW train error, HIGH test error
- Example: fit a wiggly curve through every training point — fails on new data

### The bias-variance tradeoff
- **Bias** = how wrong on average (underfit if too high)
- **Variance** = how much predictions vary across samples (overfit if too high)

You want both to be low. There's a tradeoff.

### How to avoid overfitting
1. More data
2. Simpler models
3. Regularisation (L1, L2)
4. Cross-validation
5. Early stopping (in iterative training)
6. Dropout (in neural networks)

---

## 7.8 Performance Metrics

### Regression metrics
- **MSE** (mean squared error)
- **RMSE** (square root of MSE — same units as data)
- **MAE** (mean absolute error)
- **R²** (coefficient of determination, 0 to 1, higher is better)

### Classification metrics
- **Accuracy** = (TP + TN) / total
- **Precision** = TP / (TP + FP) ("of those I predicted positive, how many are correct?")
- **Recall (Sensitivity)** = TP / (TP + FN) ("of all actual positives, how many did I catch?")
- **F1 Score** = harmonic mean of precision and recall
- **Confusion matrix** = table of TP, FP, TN, FN

### When accuracy is misleading
**Imbalanced data:** if 99% of emails are non-spam, predicting "non-spam" always gives 99% accuracy, but useless. Use precision/recall/F1 instead.

---

## 7.9 ML Common Mistakes

| Mistake | Truth |
|---|---|
| Logistic regression is regression | NO, it's classification (predicts probability of class). |
| kNN and k-means are similar | One is supervised, one is unsupervised. |
| 100% train accuracy = great model | Likely overfitting. Check test accuracy. |
| More features = better | NO. Curse of dimensionality. Feature selection helps. |
| MSE works for classification | NO. Use cross-entropy / log loss. |
| Cross-validation = test set | They're different. CV is for model selection during training. |
| Linear regression always linear in features | The features can be engineered (x², x·y, etc.). It's linear in *parameters*. |

---

## 7.10 ML Practice Problems

### Q1
Linear regression vs Logistic regression?
**Answer:** Linear → continuous output (numbers). Logistic → probability (used for classification).

### Q2
Difference between kNN and k-means?
**Answer:** kNN = supervised classification using nearest labelled points. k-means = unsupervised clustering using nearest centroids.

### Q3
What is overfitting?
**Answer:** Model fits training data too well, including noise → poor generalisation to new data.

### Q4
Purpose of cross-validation?
**Answer:** Get a reliable estimate of model performance and tune hyperparameters without leaking test data.

### Q5
What does MSE measure?
**Answer:** Average squared error between predictions and true values.

### Q6
For a fair coin classifier predicting "heads" always, accuracy and recall on actual heads?
**Answer:** Accuracy ~50%, recall = 100% (catches all heads), precision = 50%.

### Q7
Sigmoid function value at z=0?
**Answer:** 0.5

### Q8
Why do we standardise features in kNN?
**Answer:** Distance-based — without standardisation, features with larger scale dominate.

### Q9 (Conceptual)
You have 90% accuracy on training, 60% on test. What's happening?
**Answer:** Overfitting. The model memorised training but doesn't generalise.

### Q10 (PYQ-style)
Which of these is NOT a supervised algorithm?
- a) Linear regression
- b) Logistic regression
- c) kNN
- d) k-means
**Answer:** d (k-means is unsupervised)

---

## 7.11 ML Mini Formula Sheet

```
Linear regression:
  y = wx + b
  Loss (MSE) = (1/n)·Σ(yᵢ − ŷᵢ)²
  Closed-form: w = (XᵀX)⁻¹ Xᵀy

Logistic regression:
  σ(z) = 1/(1 + e⁻ᶻ)
  P(y=1|x) = σ(w·x + b)
  Loss (cross-entropy) = −[y·log(p) + (1−y)·log(1−p)]

kNN:
  classify by majority vote of k nearest training points
  k often √n
  
k-means:
  k clusters
  iterate: assign + update centroid
  unsupervised

Metrics:
  Accuracy = (TP+TN)/total
  Precision = TP/(TP+FP)
  Recall = TP/(TP+FN)
  F1 = 2·P·R/(P+R)
  R² = 1 − SS_res/SS_tot

Cross-validation:
  k-fold: split into k parts, rotate test fold
  
Overfitting: low train err, high test err
Underfitting: high err on both
```

---

# PART 8 — 🐍 Python Essentials (interview-focused, lightweight)

> Python isn't on the entrance exam syllabus, but **it WILL come up in the interview** if you get one, and you'll need it from Day 1 of the M.Tech (DA5301W is "Python and Data Structures"). Spend 1–2 days on this.

## 8.1 Python basics you must know

### Variables & types
```python
x = 5            # int
y = 3.14         # float
name = "Sam"     # str (string)
flag = True      # bool
items = [1,2,3]  # list
pair = (1, 2)    # tuple (immutable)
ages = {"a": 1, "b": 2}  # dict
unique = {1, 2, 3}       # set
```

### Operators
- Arithmetic: + − * / // ** %
- Comparison: == != < > <= >=
- Logical: `and`, `or`, `not`
- `//` is integer division. `**` is power. `%` is mod.

### Control flow
```python
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

for i in range(5):     # 0, 1, 2, 3, 4
    print(i)

while x > 0:
    x -= 1
```

### Functions
```python
def square(x):
    return x * x

def greet(name="World"):
    return f"Hello, {name}"
```

### List operations
```python
nums = [1, 2, 3, 4, 5]
nums.append(6)         # add to end
len(nums)              # 6
nums[0]                # 1
nums[-1]               # 6 (last element)
nums[1:3]              # [2, 3] — slicing
sum(nums)              # 21
max(nums), min(nums)   # 6, 1
sorted(nums)           # returns sorted copy
```

### List comprehensions (Pythonic & important)
```python
squares = [x*x for x in range(10)]
evens = [x for x in nums if x % 2 == 0]
```

### Dictionaries
```python
d = {"name": "Sam", "age": 25}
d["age"]               # 25
d["city"] = "Chennai"  # add key
"name" in d            # True
for k, v in d.items():
    print(k, v)
```

### File handling (basic)
```python
with open("file.txt") as f:
    content = f.read()
```

---

## 8.2 NumPy crash course (used everywhere in ML)

```python
import numpy as np

# Create arrays
a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])    # 2D matrix

# Shape
a.shape       # (3,)
b.shape       # (2, 2)

# Operations (element-wise!)
a + 1         # [2, 3, 4]
a * 2         # [2, 4, 6]
a + a         # [2, 4, 6]

# Matrix ops
np.dot(b, b)            # matrix multiplication
b @ b                   # same thing (Python 3.5+)
b.T                     # transpose
np.linalg.inv(b)        # inverse
np.linalg.eig(b)        # eigenvalues, eigenvectors

# Useful
np.zeros((3, 3))
np.ones((2, 3))
np.eye(3)               # identity matrix
np.arange(0, 10, 0.5)   # [0, 0.5, 1, ...]
np.linspace(0, 1, 5)    # 5 evenly spaced points

# Stats
np.mean(a)
np.std(a)
np.var(a)
np.sum(a)
```

---

## 8.3 Pandas basics (data handling)

```python
import pandas as pd

df = pd.read_csv("data.csv")
df.head()              # first 5 rows
df.columns             # column names
df.shape               # (rows, cols)
df["age"]              # one column
df[["age", "name"]]    # multiple columns
df[df["age"] > 30]     # filter rows
df.describe()          # summary stats
df.groupby("city").mean()
```

---

## 8.4 Common Python interview patterns

### Pattern 1: Read input, apply function
```python
n = int(input())
result = sum(i*i for i in range(1, n+1))
print(result)
```

### Pattern 2: Loop with conditions
```python
def count_vowels(s):
    count = 0
    for ch in s:
        if ch.lower() in "aeiou":
            count += 1
    return count
```

### Pattern 3: Dictionary counter
```python
def char_freq(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq
```

### Pattern 4: List of tuples (e.g., dataset)
```python
data = [(1, "a"), (2, "b"), (3, "a")]
# count by second element
from collections import Counter
counts = Counter(t[1] for t in data)
```

---

## 8.5 Basic Data Structures (likely interview)

| DS | Use case | Key ops |
|---|---|---|
| **List** | Ordered, mutable | append, pop, sort |
| **Tuple** | Ordered, immutable | indexing |
| **Dict** | Key-value | hash lookup |
| **Set** | Unique items | union, intersection |
| **Stack** | LIFO | push (append), pop |
| **Queue** | FIFO | enqueue, dequeue (use deque) |

### Time complexity (mention if asked)
- List: index O(1), search O(n), append O(1) amortised
- Dict: lookup, insert, delete — average O(1)
- Set: same as dict

---

# PART 9 — Mock Tests + 50 PYQ-Style Questions with Solutions

> This is your gold mine. Each question is modelled on the actual IIT Madras exam pattern. Solve them on paper, then check.

## 9.1 How to use this section

- Try each question for **2–3 minutes** before peeking at the solution
- Mark your level: ✅ solved | ⚠️ struggled | ❌ no idea
- After completing all 50, redo only your ❌ and ⚠️ ones until ✅
- Then take **Mock 1 and Mock 2** under timed conditions

---

## 9.2 50 PYQ-Style Practice Questions

### 🎲 Probability & Statistics (15 Q)

**Q1.** A coin is biased with P(H) = 0.6. It is flipped 3 times. P(exactly 2 heads)?
<details>
<summary>Solution</summary>

Binomial: C(3,2) × 0.6² × 0.4 = 3 × 0.36 × 0.4 = **0.432**
</details>

**Q2.** A box has 5 white and 3 black balls. Two are drawn without replacement. P(both same colour)?
<details>
<summary>Solution</summary>

P(WW) + P(BB) = (5/8)(4/7) + (3/8)(2/7) = 20/56 + 6/56 = **26/56 ≈ 0.464**
</details>

**Q3.** P(A) = 0.4, P(B) = 0.5, A and B independent. P(A ∪ B)?
<details>
<summary>Solution</summary>

P(A∩B) = 0.4 × 0.5 = 0.2
P(A∪B) = 0.4 + 0.5 − 0.2 = **0.7**
</details>

**Q4.** A factory's machine X produces 60%, machine Y produces 40%. X has 2% defect rate, Y has 5%. A defective item is chosen. P(it came from X)?
<details>
<summary>Solution</summary>

Bayes:
- P(D|X) = 0.02, P(D|Y) = 0.05
- P(D) = 0.6×0.02 + 0.4×0.05 = 0.012 + 0.020 = 0.032
- P(X|D) = (0.6 × 0.02)/0.032 = 0.012/0.032 = **0.375**
</details>

**Q5.** X ~ Poisson(λ=4). P(X=0)?
<details>
<summary>Solution</summary>

P(X=0) = e^(−4) = **≈ 0.0183**
</details>

**Q6.** E[X] = 2, Var(X) = 9. E[X²]?
<details>
<summary>Solution</summary>

Var(X) = E[X²] − (E[X])² → 9 = E[X²] − 4 → E[X²] = **13**
</details>

**Q7.** Heights ~ N(170, 25). P(165 ≤ X ≤ 175)?
<details>
<summary>Solution</summary>

σ = 5. z₁ = (165−170)/5 = −1; z₂ = (175−170)/5 = +1
P(−1 ≤ Z ≤ 1) ≈ 0.68 (the 68-95-99.7 rule)
</details>

**Q8.** A 95% confidence interval for the mean is (10, 14). Which is correct?
- a) 95% of data lies between 10 and 14
- b) The interval (10, 14) captures the true mean with 95% confidence
- c) There's a 95% probability the true mean is in (10, 14)
- d) None
<details>
<summary>Solution</summary>

**b**. (Common trap. The mean isn't random; the interval is.)
</details>

**Q9.** You sample n=64 from a population with σ=16. Standard error?
<details>
<summary>Solution</summary>

SE = σ/√n = 16/8 = **2**
</details>

**Q10.** You want to test if a sample mean differs from 100 (a known value), σ unknown, n=20. Which test?
<details>
<summary>Solution</summary>

**t-test** (one-sample). σ unknown + small n.
</details>

**Q11.** A test has α = 0.05. You compute p = 0.07. Decision?
<details>
<summary>Solution</summary>

p > α → **fail to reject H₀**
</details>

**Q12.** Joint PDF f(x,y) = (x+y)/24 for 0<x<3, x<y<x+2. E[Y|X=2]?
<details>
<summary>Solution</summary>

When X=2, Y ranges from 2 to 4. f(y|x=2) ∝ (2+y).

Normalising constant: ∫₂⁴ (2+y) dy = [2y + y²/2] from 2 to 4 = (8+8) − (4+2) = 10

E[Y|X=2] = (1/10) × ∫₂⁴ y(2+y) dy = (1/10) × [y² + y³/3] from 2 to 4 = (1/10) × [(16+64/3) − (4+8/3)] = (1/10) × (12 + 56/3) = (1/10)(36+56)/3 = **92/30 ≈ 3.07**
</details>

**Q13.** Two independent fair dice. P(sum = 7)?
<details>
<summary>Solution</summary>

Outcomes: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) = 6
Total = 36 → **6/36 = 1/6**
</details>

**Q14.** Variance of Binomial(n=10, p=0.4)?
<details>
<summary>Solution</summary>

np(1−p) = 10 × 0.4 × 0.6 = **2.4**
</details>

**Q15.** Correlation between X and Y is 0.8. Var(X)=4, Var(Y)=16. Covariance?
<details>
<summary>Solution</summary>

Cov(X,Y) = ρ·σ_X·σ_Y = 0.8 × 2 × 4 = **6.4**
</details>

---

### 📐 Linear Algebra (15 Q)

**Q16.** ||[1, −2, 2, 4]||?
<details>
<summary>Solution</summary>

√(1+4+4+16) = √25 = **5**
</details>

**Q17.** Are [1, 2, 3] and [2, −1, 0] orthogonal?
<details>
<summary>Solution</summary>

Dot = 2 − 2 + 0 = 0 → **yes**
</details>

**Q18.** A = [[2,1],[1,3]]. Eigenvalues?
<details>
<summary>Solution</summary>

det(A − λI) = (2−λ)(3−λ) − 1 = 0
λ² − 5λ + 5 = 0
λ = (5 ± √5)/2 → **≈ 3.618 and 1.382**
</details>

**Q19.** Sum of eigenvalues of [[3,1,2],[0,4,5],[0,0,−1]]?
<details>
<summary>Solution</summary>

Triangular → trace = 3 + 4 + (−1) = **6**
</details>

**Q20.** Project [4, 3] onto [1, 0].
<details>
<summary>Solution</summary>

dot = 4, |a|² = 1, proj = 4·[1,0] = **[4, 0]**
</details>

**Q21.** Rank of [[1,1,1],[1,1,1],[1,1,1]]?
<details>
<summary>Solution</summary>

All rows identical → **1**
</details>

**Q22.** A is 3×4 matrix with rank 3. Nullity?
<details>
<summary>Solution</summary>

cols=4. rank+nullity=4 → nullity = **1**
</details>

**Q23.** A = [[1,2],[3,4]]. det(A)?
<details>
<summary>Solution</summary>

1·4 − 2·3 = **−2**
</details>

**Q24.** Eigenvalues of A are 1 and 4. Eigenvalues of A²?
<details>
<summary>Solution</summary>

**1 and 16**
</details>

**Q25.** [[1,2],[3,4]] × [[5,0],[0,5]] = ?
<details>
<summary>Solution</summary>

[[5, 10], [15, 20]]
</details>

**Q26.** Solve x + 2y = 5; 2x + 4y = 11.
<details>
<summary>Solution</summary>

Eq2 = 2·Eq1 of LHS, but 11 ≠ 10 → **no solution**
</details>

**Q27.** Eigenvalues of [[3,0,0],[0,3,0],[0,0,5]]?
<details>
<summary>Solution</summary>

Diagonal → **3, 3, 5**
</details>

**Q28.** A is 2x2 symmetric with trace=5 and det=4. Eigenvalues?
<details>
<summary>Solution</summary>

λ₁+λ₂=5, λ₁λ₂=4 → solve: λ²−5λ+4=0 → **λ=1, 4**
</details>

**Q29.** Distance between (1,2,3) and (4,6,3)?
<details>
<summary>Solution</summary>

√(9 + 16 + 0) = **5**
</details>

**Q30.** A is 3×3 with eigenvalues 2, −1, 3. det(A)?
<details>
<summary>Solution</summary>

product = 2 × (−1) × 3 = **−6**
</details>

---

### 📉 Optimization & Calculus (10 Q)

**Q31.** d/dx (3x² − 4x + 7)?
<details>
<summary>Solution</summary>

**6x − 4**
</details>

**Q32.** Min of f(x) = x² − 6x + 10?
<details>
<summary>Solution</summary>

f'(x) = 2x − 6 = 0 → x=3. f(3) = 9 − 18 + 10 = **1**
</details>

**Q33.** d/dx (e^(2x))?
<details>
<summary>Solution</summary>

Chain rule: **2 e^(2x)**
</details>

**Q34.** GD step: f(x) = x², start x=10, α=0.2. New x?
<details>
<summary>Solution</summary>

f'=2x. x_new = 10 − 0.2·20 = **6**
</details>

**Q35.** ∂/∂y of f(x,y) = x²y + xy² + y³?
<details>
<summary>Solution</summary>

x² + 2xy + 3y²
</details>

**Q36.** Min of x² + y² subject to x + y = 4?
<details>
<summary>Solution</summary>

y=4−x. f = x²+(4−x)² = 2x²−8x+16. f'=4x−8=0 → x=2, y=2. Min = **8**
</details>

**Q37.** f(x) = (x−5)². Where is f differentiable?
<details>
<summary>Solution</summary>

**Everywhere** (it's a polynomial)
</details>

**Q38.** What if α (learning rate) is 0?
<details>
<summary>Solution</summary>

x doesn't update → no learning. Stuck.
</details>

**Q39.** Critical points of f(x) = x³ − 3x?
<details>
<summary>Solution</summary>

f'=3x²−3=0 → x = ±1. (Local max at −1, local min at +1)
</details>

**Q40.** Inflection point of f(x) = x³?
<details>
<summary>Solution</summary>

f''(x) = 6x = 0 at x=0. Inflection at **x=0**.
</details>

---

### 🤖 Machine Learning (10 Q)

**Q41.** Which is unsupervised?
- a) Linear regression
- b) Logistic regression
- c) k-means
- d) kNN
<details>
<summary>Solution</summary>

**c) k-means**
</details>

**Q42.** Sigmoid(0)?
<details>
<summary>Solution</summary>

1/(1+e⁰) = 1/2 = **0.5**
</details>

**Q43.** What does "overfitting" mean?
<details>
<summary>Solution</summary>

Model fits noise in training data → poor on new data. High variance.
</details>

**Q44.** When test accuracy << train accuracy, the model is...
<details>
<summary>Solution</summary>

**Overfitting**
</details>

**Q45.** In linear regression, MSE is...
<details>
<summary>Solution</summary>

(1/n) · Σ(yᵢ − ŷᵢ)²
</details>

**Q46.** What's the closed-form solution for linear regression?
<details>
<summary>Solution</summary>

w = (XᵀX)⁻¹ Xᵀ y
</details>

**Q47.** Why standardise features for kNN?
<details>
<summary>Solution</summary>

kNN uses distance — features with larger scale dominate. Standardising puts them on same scale.
</details>

**Q48.** 5-fold CV vs 10-fold CV?
<details>
<summary>Solution</summary>

10-fold = lower bias, more compute. 5-fold = faster, slightly more biased. Common choice depends on dataset size.
</details>

**Q49.** Confusion matrix: TP=80, FP=20, FN=10, TN=90. Precision?
<details>
<summary>Solution</summary>

TP/(TP+FP) = 80/100 = **0.8**
</details>

**Q50.** Same matrix. Recall?
<details>
<summary>Solution</summary>

TP/(TP+FN) = 80/90 = **0.889**
</details>

---

## 9.3 MOCK TEST 1 (90 minutes, 30 questions)

> Take this on Day 26 of your plan. Time yourself strictly. Calculator allowed for arithmetic.

### Section A — Probability & Statistics (10 Q)

1. P(A) = 0.7, P(B) = 0.4, P(A∩B) = 0.3. P(A | B)?
2. X ~ Bernoulli(0.6). E[X] and Var(X)?
3. λ = 2 calls/hr. P(X = 0)?
4. n=100, σ=10. SE of x̄?
5. p-value = 0.04, α = 0.05. Decision?
6. Two events independent with P(A)=0.3, P(B)=0.5. P(A∪B)?
7. The CLT says: distribution of sample means is approximately... what?
8. Comparing 3 group means. Which test?
9. Cov(X,Y) = 6, σ_X = 2, σ_Y = 5. Correlation?
10. P(at least one head in 4 tosses)?

### Section B — Linear Algebra (10 Q)

11. ||[3, 4, 12]||?
12. [[2,1],[1,2]] × [1, 2]ᵀ?
13. Rank of [[1,2],[2,4]]?
14. Eigenvalues of [[5,0],[0,5]]?
15. det of [[3,2],[1,4]]?
16. Sum of eigenvalues of [[1,2,3],[0,4,5],[0,0,6]]?
17. Project [3,3] onto [1,0].
18. A is 4×4 with rank 2. Nullity?
19. (A·B)ᵀ = ?
20. Are [1,1,0] and [0,0,1] orthogonal?

### Section C — Optimization & ML (10 Q)

21. d/dx of (x⁴ − 5x² + 3)?
22. min(x² − 4x + 7)?
23. GD step: f=x², x=4, α=0.5. New x?
24. ∂f/∂x of x²y + y²?
25. Sigmoid(z) at z = 0?
26. kNN is supervised or unsupervised?
27. k-means is supervised or unsupervised?
28. Train accuracy 99%, test 60% → ?
29. MSE formula?
30. Cross-validation purpose?

---

### ✅ MOCK 1 Answers

| Q | Answer |
|---|---|
| 1 | 0.75 |
| 2 | 0.6, 0.24 |
| 3 | e⁻² ≈ 0.135 |
| 4 | 1 |
| 5 | Reject H₀ |
| 6 | 0.65 (P(A∪B) = 0.3+0.5−0.15 = 0.65) |
| 7 | Normal |
| 8 | ANOVA (F-test) |
| 9 | 6/(2·5) = 0.6 |
| 10 | 1 − 0.5⁴ = 15/16 = 0.9375 |
| 11 | √(9+16+144) = 13 |
| 12 | [4, 5] |
| 13 | 1 |
| 14 | 5, 5 |
| 15 | 10 |
| 16 | 11 (1+4+6) |
| 17 | [3, 0] |
| 18 | 4−2 = 2 |
| 19 | BᵀAᵀ |
| 20 | Yes (dot=0) |
| 21 | 4x³ − 10x |
| 22 | x=2, min=3 |
| 23 | x_new = 4 − 0.5·8 = 0 |
| 24 | 2xy |
| 25 | 0.5 |
| 26 | Supervised |
| 27 | Unsupervised |
| 28 | Overfitting |
| 29 | (1/n)Σ(yᵢ − ŷᵢ)² |
| 30 | Reliable model evaluation + hyperparameter tuning |

**Scoring:**
- 24+: ready for the exam
- 18–23: solid base, focus on weak topics
- 12–17: revise the topics where you missed
- <12: take a step back and re-read the relevant Parts

---

## 9.4 MOCK TEST 2 (75 minutes, 25 questions — slightly tougher)

> Take on Day 28. Stricter timing, mixed difficulty.

1. A coin is tossed until 1st H. Expected number of tosses?
2. P(A∩B) = 0.1, P(A) = 0.4, P(B) = ? if A and B are independent.
3. X ~ N(50, 25). P(X > 60)?
4. 90% CI vs 99% CI — which is wider?
5. Type I error rate = α = 0.05 means...
6. n=36, σ=6. 95% CI half-width using z=1.96?
7. Bayes: P(D)=0.05, P(+|D)=0.95, P(+|¬D)=0.10. P(D|+)?
8. Eigenvalues of [[4,1],[2,3]]?
9. A 3×3 matrix has det=0. What does this mean?
10. ||[2,2,2,2]||?
11. Solve: [[1,2],[3,5]] x = [3, 8]ᵀ.
12. Project (2, 0) onto (1, 1).
13. (AB)⁻¹ = ?
14. Eigenvalues of A are 2, 3, 4. det(A)?
15. Trace of [[1,5,3],[2,4,6],[7,8,9]]?
16. d/dx (sin(x²))?
17. Critical points of x² − 4x + 5?
18. Find min of f(x,y) = (x−1)² + (y−2)².
19. ∇f for f(x,y) = 3x²y − xy² + y at (1,1)?
20. Logistic regression's output is a...
21. F1 score formula?
22. Why use a validation set in addition to test?
23. Curse of dimensionality affects which algorithm most?
24. Closed-form for linear regression?
25. Why is symmetric matrix special in eigen-analysis?

### ✅ MOCK 2 Answers

| Q | Answer |
|---|---|
| 1 | 1/p = 2 (geometric distribution, mean = 1/p, here p=0.5) |
| 2 | P(B) = P(A∩B)/P(A) = 0.25 |
| 3 | z = 2, P(Z>2) ≈ 0.025 (or 2.28%) |
| 4 | 99% (more confidence = wider) |
| 5 | Probability of falsely rejecting a true null = 0.05 |
| 6 | 1.96 × 6/6 = 1.96 |
| 7 | P(+) = 0.95·0.05 + 0.10·0.95 = 0.0475 + 0.095 = 0.1425; P(D|+) = 0.0475/0.1425 ≈ 0.333 |
| 8 | tr=7, det=10. λ²−7λ+10=0 → 2, 5 |
| 9 | Singular, not invertible, rank < 3 |
| 10 | √16 = 4 |
| 11 | Solve: x+2y=3, 3x+5y=8 → x=1, y=1 |
| 12 | dot = 2, |a|²=2, proj = 1·[1,1] = [1,1] |
| 13 | B⁻¹A⁻¹ |
| 14 | 24 |
| 15 | 14 |
| 16 | cos(x²) · 2x = 2x·cos(x²) |
| 17 | x = 2 |
| 18 | (1, 2), min value = 0 |
| 19 | ∇f = [6xy − y², 3x² − 2xy + 1] at (1,1) = [5, 2] |
| 20 | probability (between 0 and 1) |
| 21 | 2·P·R/(P+R) |
| 22 | Validation = used during training to tune hyperparameters; test = used only at the end for unbiased estimate |
| 23 | kNN (because of distance metric breaking down in high dims) |
| 24 | w = (XᵀX)⁻¹Xᵀy |
| 25 | Real eigenvalues + orthogonal eigenvectors |

---

# PART 10 — Interview Prep + Final Tips

## 10.1 The interview reality

**If you clear the qualifier**, you might get an interview (some web M.Tech batches skip this; some don't). Be ready either way.

### What they typically test
1. **Math foundations** — same as the exam, but they'll probe deeper
2. **ML concepts** — explain like a teacher, not a memoriser
3. **Motivation** — why this program?
4. **Background fit** — your work + how AI ties in
5. **Soft skills** — clear communication, calmness under pressure

### Question types reported by candidates (from similar programs)

**Math:**
- "What's an eigenvector intuitively?"
- "Why does gradient descent work?"
- "Explain Bayes theorem with an example."
- "Difference between independent and mutually exclusive events?"
- "What does the chain rule mean?"
- "Project a vector onto another and explain the meaning."

**ML:**
- "Why use logistic regression for classification, not linear?"
- "What is overfitting and how do you detect it?"
- "When would you use kNN vs k-means?"
- "What does the loss function do?"
- "Explain cross-validation simply."

**Motivation:**
- "Why this program?"
- "Why now?"
- "What will you do after the M.Tech?"
- "What's your biggest weakness?"

---

## 10.2 Strong answers to common interview questions

### Q: Why this program?
> "I've been working as a [your role] for [N] years. I've been increasingly involved with data and AI-adjacent systems, but I want to deepen my mathematical and theoretical understanding. IIT Madras's M.Tech in AI is a perfect fit because it covers the core mathematical foundations — probability, linear algebra, optimization — combined with applied ML and a project component. The web-enabled format lets me continue working while learning rigorously."

### Q: Why AI?
> "AI is reshaping every industry, but most professionals only use AI tools without understanding what's underneath. I want to move from 'using AI' to 'building AI', which requires the strong mathematical foundation this program provides."

### Q: What's your weakness?
> "I've been away from formal mathematics for a while. Concepts like eigendecomposition or hypothesis testing felt rusty when I started preparing. But I've spent the last month systematically rebuilding from basics, and I'm comfortable with the entrance syllabus now. I see my weakness as something I'm actively addressing."

### Q: Explain Bayes' theorem to a non-technical person.
> "Imagine a medical test for a rare disease. Bayes' theorem helps us combine two things: how rare the disease is, and how good the test is. Even with a 99% accurate test, if the disease is very rare, a positive result still mostly means a false alarm — because most positive tests come from healthy people. Bayes formalises this intuition."

### Q: What's overfitting and how do you avoid it?
> "Overfitting is when a model memorises the training data including its noise, so it does great on training but poorly on new data. I detect it by comparing train and test performance — a big gap means overfitting. To prevent it, I'd use simpler models, regularisation, more data, or cross-validation."

### Q: Eigenvalue intuition?
> "An eigenvector of a matrix is a special direction. When the matrix transforms that direction, it doesn't rotate — it just stretches or shrinks by the eigenvalue. So eigenvalues tell us 'how much' the matrix scales along its preferred axes. PCA, stability analysis, and many ML methods rely on this."

### Q: kNN vs k-means?
> "Both have a 'k' but very different purposes. kNN is supervised classification: I label a new point by looking at the k nearest labelled training points and voting. k-means is unsupervised clustering: I divide unlabelled data into k groups by proximity to k cluster centres. One uses labels, the other discovers structure."

### Q: Why does gradient descent work?
> "The gradient points uphill — towards the steepest increase. So if I take a step in the opposite direction, I'm moving downhill. With a small enough learning rate, repeating this slowly walks me to a minimum. For convex functions, that minimum is the global one. For non-convex functions, it could be a local minimum, which is a known limitation."

---

## 10.3 Behavioural / situational questions

- "Tell me about a time you faced a hard technical problem."
  > Pick a real story. Use STAR format: Situation, Task, Action, Result.

- "How do you balance work and study?"
  > Be concrete: weekday hours, weekend strategy, prioritisation, manager support.

- "What if you find the program too hard?"
  > "I'd reach out to TAs, peer groups, and rebuild fundamentals. The hardest courses are usually a sign of growth, and I've prepared by strengthening the basics first."

---

## 10.4 Final exam-day tips

### Day before the exam
- Don't learn new things
- Revise formula sheet (Part 11)
- Sleep 8 hours
- Test your computer/internet/webcam

### Exam day
- Eat a normal breakfast
- Set up early, no last-minute panic
- Read EACH question fully before answering
- **Easy questions first** — bank the marks
- For NAT (numeric type), double-check the unit and decimal places asked
- For MSQ (multiple select), only mark the choices you're SURE are correct (no partial credit usually)
- If stuck for >2 minutes, move on and come back

### Mental tips
- The exam wants to see if you've understood — not if you're a genius
- A wrong question costs you only that question, not the exam
- Stay calm. Breathing exercises help (4-4-4-4: inhale 4s, hold 4s, exhale 4s, hold 4s)

---

# PART 11 — 📋 MASTER FORMULA SHEET (Print this!)

> Print this page. Stick it on your wall. Glance at it every day.

## 🎲 Probability

```
Basic rules
P(A') = 1 − P(A)
P(A ∪ B) = P(A) + P(B) − P(A ∩ B)
P(A ∩ B) = P(A) · P(B|A)
   Independent: P(A) · P(B)
   Mutually exclusive: 0
P(A|B) = P(A ∩ B) / P(B)

Bayes
P(A|B) = P(B|A) · P(A) / P(B)
P(B) = Σ P(B|Aᵢ) P(Aᵢ)   (total probability)

Discrete RV
E[X] = Σ x · P(X=x)
Var(X) = E[X²] − (E[X])²
σ = √Var(X)

Properties
E[aX + b] = a·E[X] + b
Var(aX + b) = a²·Var(X)
E[X+Y] = E[X] + E[Y]
Var(X+Y) = Var(X) + Var(Y)   if independent

Distributions
Bernoulli(p):  E=p, Var=p(1−p)
Binomial(n,p): E=np, Var=np(1−p)
   P(X=k) = C(n,k) p^k (1−p)^(n−k)
Poisson(λ):    E=λ, Var=λ
   P(X=k) = e^(−λ) λ^k / k!
Normal(μ,σ²):  z = (x−μ)/σ
   68-95-99.7 rule for ±1σ, ±2σ, ±3σ
```

## 📊 Statistics

```
Sampling
SE = σ/√n
CLT: x̄ ≈ Normal(μ, σ²/n) for large n

Confidence Interval
95% CI: x̄ ± 1.96 · (σ/√n)

Tests
z-test: 1 sample, σ known
t-test: 1 or 2 samples, σ unknown
chi-square: categorical / counts
F-test: comparing variances
ANOVA: 3+ means

p-value: P(observe data this extreme | H₀ true)
Reject H₀ if p < α
Type I (α): reject TRUE null
Type II (β): keep FALSE null
```

## 📐 Linear Algebra

```
Vectors
||v|| = √(Σ vᵢ²)
a · b = Σ aᵢ bᵢ = ||a||·||b||·cos(θ)
distance(a,b) = ||a − b||
cos(θ) = (a·b) / (||a||·||b||)
Orthogonal ⟺ a · b = 0

Projection of b onto a:
proj_a(b) = ((a·b)/(a·a)) · a

Matrices
(AB)ᵀ = BᵀAᵀ
A·I = I·A = A
(AB)⁻¹ = B⁻¹A⁻¹
det([[a,b],[c,d]]) = ad − bc
Symmetric: A = Aᵀ

Solving Ax = b:
Unique solution iff det(A) ≠ 0

Rank
rank(A) ≤ min(rows, cols)
rank + nullity = number of cols

Eigenvalues
Av = λv
Σ λᵢ = trace(A) = sum of diagonal
Π λᵢ = det(A)
Triangular/diagonal: eigenvalues = diagonal entries
Symmetric matrix: real eigenvalues + orthogonal eigenvectors

Eigenvalue tricks
λ(kA) = k·λ
λ(A + cI) = λ + c
λ(A⁻¹) = 1/λ
λ(Aⁿ) = λⁿ

Pseudo-inverse
A† = (AᵀA)⁻¹ Aᵀ
Best fit Ax=b: x = A†b
```

## 📉 Calculus / Optimization

```
Power rule: d/dx xⁿ = n·xⁿ⁻¹
Chain rule: d/dx f(g(x)) = f'(g(x)) · g'(x)
Product rule: (fg)' = f'g + fg'
Common derivatives:
   d(eˣ)/dx = eˣ
   d(ln x)/dx = 1/x
   d(sin x)/dx = cos x
   d(cos x)/dx = −sin x

Find min:
1. f'(x) = 0
2. f''(x) > 0 → minimum

Multivariate
∇f = [∂f/∂x₁, ∂f/∂x₂, ...]
At minimum: ∇f = 0

Gradient Descent:
x_new = x_old − α · ∇f(x_old)
```

## 🤖 Machine Learning

```
Linear regression
y = wx + b (or y = Xw)
MSE = (1/n) Σ (yᵢ − ŷᵢ)²
Closed form: w = (XᵀX)⁻¹ Xᵀy

Logistic regression
σ(z) = 1/(1 + e⁻ᶻ)
P(y=1|x) = σ(wx + b)
Cross-entropy = −[y·log(p) + (1−y)·log(1−p)]

kNN
Classify by majority of k nearest neighbours
Supervised
Distance-based — standardise features

k-means
k clusters, iterative centroid update
Unsupervised
Sensitive to initialisation

Metrics
Accuracy = (TP+TN)/total
Precision = TP/(TP+FP)
Recall = TP/(TP+FN)
F1 = 2·P·R/(P+R)
R² = 1 − SS_res/SS_tot

Diagnose
Train ≫ test → overfitting
Both bad → underfitting

Cross-validation
k-fold: rotate test fold, average scores
LOOCV: k = n
```

---

# 🎯 FINAL ONE-PAGE PRIORITY ORDER

If you panic in the last week, study in this exact order:

| Priority | Topic | Why |
|---|---|---|
| 1 | Conditional probability + Bayes | High exam weight + interview |
| 2 | Mean/variance/normal/CLT | Foundation for stats |
| 3 | Hypothesis testing (which test when) | High exam weight |
| 4 | Vectors + dot product + magnitude | Building block |
| 5 | Matrix multiplication + Ax=b | Standard PYQ |
| 6 | Eigenvalues (trace/det shortcuts) | High exam weight |
| 7 | Projection + least squares | Connects to ML |
| 8 | Derivatives + finding minima | Easy marks |
| 9 | Gradient descent | Conceptual exam Q |
| 10 | Linear regression + MSE | ML foundation |
| 11 | Logistic regression + sigmoid | Classification |
| 12 | kNN vs k-means | High exam confusion |
| 13 | Cross-validation, overfitting | Conceptual MCQs |

---

# 💡 FINAL MESSAGE

You said you're not good at maths, probability, or vectors. Let me be direct with you:

**That's not a problem. That's just where you are right now.**

What you've shown by even reading this far is the only thing that actually predicts success: **willingness to do the work**. Maths is not a talent gene — it's a skill you build by doing problems, making mistakes, fixing them, and doing more problems.

In one month, with this guide, you can go from "scared of vectors" to "comfortable with the entrance syllabus." I've seen it happen many times.

Three things matter most:

1. **Show up daily** — even a bad 30-minute day beats a skipped day
2. **Solve problems on paper** — not in your head, not by reading solutions
3. **Track mistakes** — your mistake notebook is your fastest path to mastery

You don't need to be a maths genius to clear this exam. You need to:
- Know a small set of formulas cold
- Recognise question types fast
- Stay calm and avoid silly errors

If you follow this guide for 30 days, you will be ready. Period.

**Now close this file and start with Part 2 (the diagnostic test). Don't read more before doing.**

You've got this. 🚀

---

## 📚 Recommended supplementary resources (use sparingly)

| Topic | Best free resource |
|---|---|
| Linear Algebra intuition | 3Blue1Brown – "Essence of Linear Algebra" (YouTube) |
| Probability intuition | Khan Academy – Probability & Statistics |
| Statistics + ML | StatQuest with Josh Starmer (YouTube) |
| Calculus basics | 3Blue1Brown – "Essence of Calculus" |
| Hypothesis testing | StatQuest – "Hypothesis Testing in 10 Minutes" |
| ML overview | Andrew Ng's Machine Learning (Coursera, free audit) |
| Python | Codecademy or freeCodeCamp |
| NumPy/Pandas | Kaggle Learn (free, micro-courses) |

**⚠️ Use these for understanding, not as a substitute for solving problems.**

---

*End of guide. Good luck. You will earn this seat.* 🎓