# IIT Madras Web M.Tech in Artificial Intelligence — Entrance Prep Master Guide (Improved)

**Program:** IIT Madras Web-Enabled M.Tech / PG Diploma in Artificial Intelligence  
**Target:** 2026 admission qualifier / entrance exam  
**Time available:** 1 month  
**Starting point:** Beginner in maths foundations, motivated working professional  
**Goal:** Clear the qualifier exam, build real conceptual clarity, and be interview-ready

---

## 1) What the official syllabus actually says

According to the IIT Madras Web M.Tech brochure, the AI entrance exam covers exactly four areas:

1. **Probability and Statistics**
2. **Linear Algebra**
3. **Optimization**
4. **Basic Machine Learning**

The official AI curriculum begins with:
- **DA5000W Mathematical Foundations for Data Science**
- **DA5301W Python and Data Structures for Data Science**
- **DA5400W Foundations of Machine Learning**
- **DA6401W Introduction to Deep Learning**
- plus labs and project work

### Meaning for you
This is **not** mainly a coding test. It is a **maths-for-ML readiness test**.  
The exam is likely designed to answer one question:

> “Can this student survive IITM’s AI foundation courses?”

So your prep must be **concept first**, then **problem solving**, then **speed**.

---

## 2) Honest verdict on the previous prep file

Your previous file was **good as a beginner roadmap**, but it was **not yet the best possible version** for this exam.

### What it did well
- Covered the official topics at a high level
- Gave a 30-day structure
- Was beginner-friendly
- Included formulas and interview pointers

### What it was missing
- No **topic priority ranking** within the official syllabus
- No **diagnostic test** to find weak areas fast
- No **“must-master vs nice-to-have” split**
- No **exam-style problem map** tied to each syllabus bullet
- No **resource mapping** from syllabus -> exact learning source
- No clear handling of the fact that **official previous-year papers are not publicly easy to find**
- Too little emphasis on **solving questions daily**
- Not enough help for someone weak in **vectors / matrices / stats tests**

This improved file fixes those gaps.

---

## 3) What I found on the internet

### Official / high-confidence findings
- IIT Madras officially lists the AI entrance syllabus as Probability & Statistics, Linear Algebra, Optimization, and Basic Machine Learning.
- The Web M.Tech in AI is the broader successor to the earlier “Industrial AI” program.
- The downstream coursework strongly suggests the entrance is testing mathematical readiness for ML-heavy study.

### What I could **not** verify officially
I could **not find an official IIT Madras public repository of previous-year question papers** for this specific Web M.Tech AI / Industrial AI qualifier exam.

### Unofficial but useful signal
A recent Reddit discussion from people talking about this exam said:
- prepare similarly to **GATE DA**
- difficulty felt **easy to medium**
- questions tested **basics and fundamentals**

Treat that only as **unofficial guidance**, not ground truth.

---

## 4) Best strategy if you are starting from scratch

Because you are weak in maths, probability, and vectors, your strategy should be:

### Phase 1 — Build intuition
You should first understand:
- what the symbols mean
- why the formula exists
- how to read a question

### Phase 2 — Solve small problems
Do short questions every day:
- 5 probability
- 5 linear algebra
- 3 optimization
- 5 ML concepts

### Phase 3 — Timed practice
Once concepts are okay, begin:
- 60–90 minute mixed sets
- formula recall drills
- mock tests

### Your target
You do **not** need research-level maths.  
You need:
- solid basics
- low mistake rate
- confidence with formulas
- ability to solve standard questions quickly

---

# 5) Syllabus breakdown — what to study and how deep

---

## A. Probability and Statistics

### Official topics
- Introduction to probability
- Conditional probability
- Joint probability
- Random variables
- PMF and PDF
- Joint distributions
- Sample statistics
- Graphical descriptive statistics
- Central Limit Theorem
- Hypothesis testing
- t-test, z-test, chi-square test, F-test

### Must-master topics
These are your **highest priority** in this block:
1. Basic probability rules
2. Conditional probability
3. Bayes theorem intuition
4. Discrete random variables
5. Mean, variance, standard deviation
6. Normal distribution and z-score
7. Sampling and CLT
8. Hypothesis testing basics
9. Which test to use: z / t / chi-square / F

### Nice-to-have but lower priority
- deeper derivations of distributions
- advanced proofs
- complicated joint density problems
- long theoretical statistics proofs

### Exam-style question patterns you should expect
- Compute **P(A ∪ B)** or **P(A | B)**
- Solve basic Bayes theorem problems
- Construct PMF for a small random variable
- Compute mean / variance from a small table
- Convert a raw number to a **z-score**
- Explain **CLT** in simple words
- Identify when to use **z-test vs t-test**
- Interpret a **p-value**

### Minimal formula set
```text
P(A') = 1 - P(A)
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
P(A|B) = P(A ∩ B) / P(B)
Bayes: P(A|B) = P(B|A)P(A)/P(B)

E[X] = ΣxP(x)
Var(X) = E[X²] - (E[X])²

z = (x - μ)/σ
Standard Error = σ/√n
```

### What beginner students usually get wrong
- confusing **independent** and **mutually exclusive**
- not understanding what conditional probability changes
- memorizing CLT without knowing what it means
- thinking p-value is “probability the null is true”

### Fast learning sequence
1. probability rules
2. conditional probability
3. random variables
4. expectation and variance
5. normal distribution
6. CLT
7. hypothesis testing

---

## B. Linear Algebra

### Official topics
- vectors
- matrices
- matrix-vector product
- rank
- null space
- set of equations and pseudo-inverse
- distance
- projections
- eigenvalue decomposition

### Must-master topics
1. Vectors, magnitude, dot product
2. Distance between vectors
3. Matrix dimensions and multiplication
4. Matrix-vector multiplication
5. Solving small systems of equations
6. Rank
7. Null space intuition
8. Projection
9. Eigenvalues / eigenvectors
10. Least-squares intuition and pseudo-inverse

### Nice-to-have but lower priority
- formal proof-heavy linear algebra
- advanced decomposition theory
- very abstract vector spaces

### Exam-style question patterns
- magnitude / dot product / angle
- distance between 2 points
- check if matrix multiplication is valid
- perform 2x2 or 2x3 multiplication
- identify rank of a small matrix
- solve Ax = b
- explain what null space means
- project one vector onto another
- identify eigenvalue for a diagonal matrix
- basic least-squares idea

### Minimal formula set
```text
||v|| = sqrt(v1² + v2² + ... + vn²)
a·b = Σ(aibi)
distance(a,b) = ||a - b||
cosθ = (a·b) / (||a|| ||b||)

Projection of b onto a = ((a·b)/(a·a)) a
Av = λv
Normal equation: AᵀAx = Aᵀb
```

### Biggest beginner pain points
- fear of matrices because the symbols look heavy
- not seeing vectors as “points with direction”
- memorizing rank without intuition
- not understanding why projections matter in regression

### Best intuition
Think:
- **row/vector/data point**
- **matrix = dataset or transformation**
- **projection = closest shadow**
- **eigenvector = direction that stays same**
- **least squares = best approximate fit**

### Fast learning sequence
1. vectors
2. dot product + distance
3. matrices + multiplication
4. linear equations
5. rank + null space
6. projection
7. eigenvalues
8. pseudo-inverse / least squares

---

## C. Optimization

### Official topics
- Types of optimization
- Unconstrained univariate optimization
- Unconstrained multivariate optimization
- Gradient descent

### Must-master topics
1. objective / cost / loss function
2. minimum vs maximum
3. derivative as slope
4. partial derivative
5. gradient
6. gradient descent update
7. learning rate
8. local vs global minimum

### Exam-style question patterns
- find derivative of simple functions
- identify minimum point of a quadratic
- run one or two steps of gradient descent
- explain effect of learning rate
- distinguish univariate vs multivariate optimization

### Minimal formula set
```text
For f(x), derivative = slope
For minimum of smooth function, derivative often becomes 0
Gradient descent:
x_new = x_old - α * gradient
```

### Most common mistakes
- knowing formula but not the meaning
- not understanding why gradient points uphill
- thinking gradient descent always works instantly
- confusing derivative with function value

### Best intuition
Optimization in ML means:

> “Change the parameters so prediction error goes down.”

That’s it.

### Fast learning sequence
1. slope and derivative
2. minima of quadratic functions
3. gradient in multiple variables
4. gradient descent
5. learning rate and convergence

---

## D. Basic Machine Learning

### Official topics
- simple linear regression
- multiple linear regression
- least-squares
- kNN
- logistic regression
- k-means clustering
- cross validation

### Must-master topics
1. supervised vs unsupervised learning
2. linear regression
3. least squares
4. train/test split
5. overfitting vs underfitting
6. cross-validation
7. kNN
8. logistic regression
9. k-means

### Exam-style question patterns
- identify regression vs classification vs clustering
- linear regression equation / prediction
- why least squares is used
- difference between linear and logistic regression
- basic kNN classification logic
- how k-means works
- what cross-validation does
- what overfitting means

### Minimal concept set
```text
Linear regression -> continuous output
Logistic regression -> classification probability
kNN -> classify using nearest neighbours
k-means -> cluster unlabeled points
Cross-validation -> test stability of model
```

### Most common mistakes
- mixing up **kNN** and **k-means**
- thinking logistic regression is a regression method in the same sense
- not understanding what cross-validation protects against
- not seeing least squares as a connection to linear algebra

### Fast learning sequence
1. supervised / unsupervised
2. simple linear regression
3. multiple regression
4. least squares
5. train-test split and overfitting
6. kNN
7. logistic regression
8. k-means
9. cross-validation

---

# 6) One-month study plan that is actually realistic

## Daily rule
### Weekdays
- **2.5 to 3.5 hours**

### Weekends
- **5 to 6 hours**

### Every study day must contain all 4 blocks
1. **Learn** a concept
2. **Solve** examples
3. **Do timed questions**
4. **Revise formulas**

### Daily template
- 45 min concept learning
- 45 min worked examples
- 45 min question practice
- 20 min formula revision
- 15 min mistake notebook

---

## Week 1 — Probability and Statistics foundation

### Goal
Become comfortable with uncertainty, distributions, averages, variance, and testing.

#### Day 1
- sample space, event, complement
- union, intersection
- independent vs mutually exclusive

#### Day 2
- conditional probability
- Bayes theorem
- tree diagrams

#### Day 3
- random variables
- PMF, PDF, CDF
- expectation

#### Day 4
- variance
- Bernoulli, Binomial, Normal
- z-score

#### Day 5
- mean, median, mode
- variance, std dev
- graphical statistics

#### Day 6
- sampling
- sample statistics
- CLT
- standard error

#### Day 7
- hypothesis testing
- p-value
- z-test, t-test, chi-square, F-test

**End-of-week target:** you should solve 20–25 basic probability/stat questions without panic.

---

## Week 2 — Linear Algebra foundation

### Goal
Stop being scared of vectors and matrices.

#### Day 8
- vectors
- magnitude
- dot product

#### Day 9
- distance
- angle
- unit vectors

#### Day 10
- matrices
- shapes / dimensions
- multiplication

#### Day 11
- matrix-vector multiplication
- systems of equations
- Ax = b

#### Day 12
- rank
- column space
- null space

#### Day 13
- projections
- least squares
- pseudo-inverse intuition

#### Day 14
- eigenvalues
- eigenvectors
- revision

**End-of-week target:** you should be able to solve standard 2D/3D vector questions and basic matrix questions confidently.

---

## Week 3 — Optimization + Machine Learning

### Goal
Understand how ML models fit data.

#### Day 15
- optimization basics
- minima/maxima
- objective function

#### Day 16
- derivatives
- multivariable intuition
- gradient

#### Day 17
- gradient descent
- learning rate
- convergence

#### Day 18
- simple linear regression
- error, MSE
- best-fit line

#### Day 19
- multiple regression
- least squares
- train/test split
- overfitting

#### Day 20
- logistic regression
- sigmoid intuition
- classification

#### Day 21
- kNN
- k-means
- cross-validation

**End-of-week target:** you should clearly explain each algorithm in plain English.

---

## Week 4 — Mixed practice and mock tests

#### Day 22
Probability revision + 25 questions

#### Day 23
Statistics revision + 25 questions

#### Day 24
Linear algebra revision + 25 questions

#### Day 25
Optimization revision + 15 questions

#### Day 26
ML revision + 25 questions

#### Day 27
Mock Test 1 (90–120 min)

#### Day 28
Error correction + weak-topic review

#### Day 29
Mock Test 2 + interview answers

#### Day 30
Formula-only revision + rest

---

# 7) Diagnostic test — take this before starting

Try to answer these without help.

### Probability
1. If P(A)=0.6, P(B)=0.5, P(A∩B)=0.2, find P(A∪B).
2. What is P(A|B)?
3. What is the difference between independent and mutually exclusive?

### Statistics
4. Mean of [2,4,6,8]?
5. What does standard deviation measure?
6. What does p-value mean?

### Linear Algebra
7. Magnitude of [3,4]?
8. Dot product of [1,2] and [3,4]?
9. What is a matrix rank?

### Optimization
10. Derivative of x²?
11. One gradient descent step from x=4 for f(x)=x² with lr=0.1?

### ML
12. Linear regression vs logistic regression?
13. Difference between kNN and k-means?
14. What is cross-validation?

### Score interpretation
- **0–4 correct:** build from absolute basics
- **5–9 correct:** beginner but recoverable
- **10–12 correct:** decent base
- **13–14 correct:** strong enough to push mocks early

---

# 8) If no official PYQs are public, what should you solve?

Use this substitution strategy:

## Primary style match
- **GATE Data Science / AI foundation-level problems**
- basic ML foundation MCQs
- probability and linear algebra drills
- short derivation-free applied maths questions

## Why this is reasonable
An unofficial Reddit comment from someone claiming to have taken the exam said the paper was **easy to medium** and tested **basics and fundamentals**, and another suggested preparing like **GATE DA**. That does not prove the exact exam style, but it is a practical proxy when official PYQs are not available.

---

# 9) Best resource stack for this syllabus

Use a **minimal stack**, not 20 random resources.

## A. Probability and Statistics
### Best learning sources
1. **Khan Academy** for basics and intuition
2. **StatQuest** for hypothesis testing intuition
3. **NPTEL / IIT resources** where available for formal grounding

### Study order
- probability basics
- conditional probability
- random variables
- distributions
- descriptive stats
- CLT
- hypothesis testing

---

## B. Linear Algebra
### Best learning sources
1. **3Blue1Brown – Essence of Linear Algebra** for intuition
2. **NPTEL Linear Algebra / Applied Linear Algebra** for structured coverage
3. standard problem solving from notes/books

### Study order
- vectors
- dot product
- matrices
- linear systems
- projections
- eigenvalues
- least squares

---

## C. Optimization
### Best learning sources
1. **Khan Academy** for derivatives
2. **StatQuest** for gradient descent
3. NPTEL / lecture notes for formal optimization basics

### Study order
- derivative as slope
- minima
- multivariable gradient
- gradient descent
- learning rate

---

## D. Basic Machine Learning
### Best learning sources
1. **NPTEL Introduction to ML / Data Science for Engineers**
2. **StatQuest** for algorithm intuition
3. light scikit-learn documentation reading only after concepts are clear

### Study order
- regression
- least squares
- train/test split
- overfitting
- logistic regression
- kNN
- k-means
- cross-validation

---

# 10) High-priority practice list

You should be able to do these confidently.

## Probability / Stats
- P(A ∪ B), P(A ∩ B), P(A|B)
- Bayes theorem
- expectation and variance
- z-score
- CLT explanation
- identify proper hypothesis test

## Linear Algebra
- vector magnitude and distance
- dot product
- 2x2 / 2x3 matrix multiplication
- solve small linear systems
- rank intuition
- projection
- eigenvalue on simple matrices

## Optimization
- derivative of simple polynomial
- locate minimum of quadratic
- one-step gradient descent

## ML
- simple linear regression prediction
- least squares intuition
- classify model type
- logistic vs linear regression
- kNN vs k-means
- cross-validation purpose

---

# 11) Formula sheet — memorize this

## Probability
```text
P(A') = 1 - P(A)
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
P(A|B) = P(A ∩ B) / P(B)
P(A ∩ B) = P(A|B)P(B)
Bayes: P(A|B) = P(B|A)P(A) / P(B)
```

## Random Variables / Statistics
```text
E[X] = ΣxP(x)
Var(X) = E[X²] - (E[X])²
Mean = Σx / n
Std deviation = sqrt(variance)
z = (x - μ)/σ
Standard Error = σ/√n
```

## Linear Algebra
```text
||v|| = sqrt(sum of squares)
a·b = Σaibi
distance(a,b) = ||a-b||
Projection of b onto a = ((a·b)/(a·a)) a
Av = λv
AᵀAx = Aᵀb
```

## Optimization
```text
x_new = x_old - α * gradient
```

## ML
```text
Linear regression: y = wx + b
MSE = average((y - y_hat)^2)
Sigmoid(z) = 1 / (1 + e^-z)
```

---

# 12) 40 must-do practice questions

## Probability / Stats
1. Compute union from intersection.
2. Compute conditional probability.
3. Bayes disease-test problem.
4. Build PMF for number of heads in 2 tosses.
5. Mean of a fair die.
6. Variance from small probability table.
7. Binomial probability for 3 heads in 5 tosses.
8. z-score calculation.
9. Explain CLT.
10. t-test vs z-test.
11. What does p-value mean?
12. Which test for categorical association?
13. Which test for comparing variances?
14. What is Type I error?
15. What is standard error?

## Linear Algebra
16. Magnitude of [6,8].
17. Dot product of [2,3] and [4,5].
18. Distance between [1,2] and [4,6].
19. Multiply 2x2 matrices.
20. Multiply matrix by vector.
21. Decide if matrix product AB is valid.
22. Solve a 2-variable linear system.
23. What is rank?
24. What is null space?
25. Project [3,4] onto [1,0].
26. Identify eigenvalues of diagonal matrix.
27. What is pseudo-inverse used for?

## Optimization
28. Derivative of x² + 3x.
29. Derivative of (x-5)².
30. Find minimum of quadratic.
31. One gradient descent step for f(x)=x².
32. What happens if learning rate is too large?
33. What is local vs global minimum?

## ML
34. Linear regression vs logistic regression.
35. What is least squares?
36. What is overfitting?
37. What is cross-validation?
38. Explain kNN.
39. Explain k-means.
40. Difference between supervised and unsupervised learning.

---

# 13) Mock-test design

## Mock 1
- 12 probability/stat
- 10 linear algebra
- 6 optimization
- 12 ML
- time: 90 min

## Mock 2
- same split
- time: 75 min
- stricter accuracy target

## After every mock, write
```text
Score:
Questions guessed:
Topics I blanked on:
Formulas forgotten:
3 concepts to revise tomorrow:
```

---

# 14) Interview preparation after the qualifier

Even if interview is not guaranteed, prepare short answers.

## Why this program?
> I want to strengthen my mathematical and machine learning foundations formally through IIT Madras while continuing my work as a software engineer. I am especially interested in building stronger fundamentals in probability, linear algebra, optimization, and applied AI systems.

## Why AI now?
> I already work close to data-heavy and AI-adjacent systems, but I want to move from implementation familiarity to deeper mathematical understanding and applied AI capability.

## Weakness?
> My weakness is that I have been away from formal mathematics for some time, especially probability and linear algebra. I am addressing this systematically through daily practice and concept revision.

## What AI areas interest you?
> Forecasting, analytics, ML systems, applied deep learning, MLOps, and AI solutions with real industry impact.

---

# 15) What to avoid

Do **not** waste precious month-one time on:
- advanced deep learning theory
- transformers and LLM internals
- long calculus proofs
- abstract theorem-heavy linear algebra
- coding huge projects
- random YouTube playlists with no exercises

This entrance is much more likely to reward:
- foundations
- formulas
- clean concept understanding
- standard applied questions

---

# 16) Final one-line priority order

If you panic and have very little time, study in this order:

1. Conditional probability + Bayes  
2. Mean / variance / normal / CLT  
3. Hypothesis testing basics  
4. Vectors + dot product + distance  
5. Matrices + rank + systems of equations  
6. Projection + least squares  
7. Gradient descent  
8. Linear regression  
9. Logistic regression  
10. kNN and k-means

---

# 17) Final message for you

You are **not too late** and you are **not bad at maths** — your maths is just **rusty**.

This exam does not require genius.  
It requires:
- disciplined basics
- repetition
- formula recall
- calm problem-solving

Because you already have software engineering maturity, your biggest job is to build comfort in the mathematical language of AI. If you follow this plan properly for one month, you can become genuinely competitive for the IIT Madras AI entrance.
