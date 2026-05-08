# 🎯 IIT Madras Web M.Tech AI — Entrance Exam Complete Study Guide
### Prepared for: Suvam Das | Application No: W26OTHAI00797
### Goal: Clear the Qualifier Exam in ~1 Month | Starting from Scratch

---

## 📋 About the Exam

| Feature | Details |
|---|---|
| **Exam Type** | Computer-Based / Written Proctored Test (Qualifier Exam) |
| **Question Types** | MCQ (Multiple Choice), MSQ (Multiple Select), SA (Short Answer / Numeric) |
| **No Negative Marking** | Generally no negative marking — attempt all! |
| **Subjects Tested** | Probability & Statistics, Linear Algebra, Optimization, Basic ML |
| **Exam Mode** | In-person at designated exam centres |

> 💡 **Strategy:** The exam tests conceptual understanding + application. You do NOT need to prove theorems. You need to understand WHY things work and apply formulas correctly. Focus on MCQ pattern — recognize question types and eliminate wrong options.

---

## 🗓️ 1-Month Study Plan

| Week | Focus Area | Daily Time |
|---|---|---|
| Week 1 | Probability & Statistics (Basics → Intermediate) | 2 hrs/day |
| Week 2 | Linear Algebra (Vectors → Matrices → Eigenvalues) | 2 hrs/day |
| Week 3 | Optimization + Basic Machine Learning | 2 hrs/day |
| Week 4 | Revision + Practice Questions + Mock Tests | 2-3 hrs/day |

---

---

# 📘 SECTION 1: PROBABILITY & STATISTICS

> 🧠 **Plain English First:** Probability = "How likely is something to happen?" Statistics = "How do we make sense of data we already have?"

---

## 1.1 Basic Probability

### What is Probability?
- A number between **0 and 1** that tells you how likely an event is.
- `P(Event) = (Favourable outcomes) / (Total outcomes)`

### Example (Exam-style):
> A bag has 3 red and 5 blue balls. What is the probability of picking a red ball?
> **Answer:** 3 / (3+5) = 3/8 = **0.375**

---

### Key Rules You MUST Know

**Rule 1 — Addition Rule:**
```
P(A or B) = P(A) + P(B) - P(A and B)
```
- If A and B cannot happen together (mutually exclusive): `P(A or B) = P(A) + P(B)`

**Rule 2 — Multiplication Rule:**
```
P(A and B) = P(A) × P(B|A)
```
- If A and B are independent: `P(A and B) = P(A) × P(B)`

**Rule 3 — Complement:**
```
P(A does NOT happen) = 1 - P(A)
```

### Practice Questions:
1. In a class of 60, 30 like cricket, 20 like football, 10 like both. How many like at least one sport?
   - Answer: 30 + 20 - 10 = **40**

2. A coin is tossed twice. What is P(at least one head)?
   - Answer: 1 - P(no heads) = 1 - (1/2 × 1/2) = **3/4**

---

## 1.2 Conditional Probability

### What is it?
The probability of event A happening **given that** event B has already happened.

```
P(A|B) = P(A and B) / P(B)
```

### Real Example:
A company interviews 100 people: 60 are engineers, 40 are non-engineers. Of the 60 engineers, 45 pass the test.

**Q: If someone passed, what's the probability they are an engineer?**

- P(engineer AND pass) = 45/100 = 0.45
- P(pass) = 45/100 = 0.45 ← (only engineers passed in this example)
- P(engineer | pass) = 0.45 / 0.45 = **1**

---

## 1.3 Bayes' Theorem ⭐ (Very Important for AI!)

### Formula:
```
P(A|B) = [P(B|A) × P(A)] / P(B)
```

### Think of it this way:
- You have a **prior belief** (P(A))
- You see **new evidence** (B)
- Bayes tells you how to **update your belief**

### Classic Exam Question:
> A disease affects 1% of the population. A test is 99% accurate.
> You test positive. What's the probability you actually have the disease?

- P(Disease) = 0.01, P(No Disease) = 0.99
- P(Positive | Disease) = 0.99
- P(Positive | No Disease) = 0.01 (false positive)
- P(Positive) = (0.99 × 0.01) + (0.01 × 0.99) = 0.0099 + 0.0099 = 0.0198
- **P(Disease | Positive) = (0.99 × 0.01) / 0.0198 ≈ 0.50 = 50%**

> 🤯 Surprise! Even with a 99% accurate test, if the disease is rare, you only have 50% chance of actually having it. This is why Bayes matters in AI!

---

## 1.4 Random Variables

- A **random variable** assigns a number to each outcome.
- **Discrete:** Countable values (e.g., number of heads in 5 coin flips: 0,1,2,3,4,5)
- **Continuous:** Any value in a range (e.g., height of a person: 5.7 ft, 5.71 ft...)

### PMF (Probability Mass Function) — for Discrete:
- Gives the probability of each specific value
- Must satisfy: all probabilities ≥ 0 and they sum to **1**

| X (Dice) | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| P(X) | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 |

### PDF (Probability Density Function) — for Continuous:
- Area under the curve = probability
- Total area = 1

---

## 1.5 Key Statistical Measures

### Mean (Average):
```
Mean = Sum of all values / Number of values
```

### Median:
- Middle value when data is sorted
- If even number of values: average of two middle values

### Mode:
- Most frequently occurring value

### Variance & Standard Deviation:
```
Variance (σ²) = Average of (each value - mean)²
Standard Deviation (σ) = √Variance
```

> 🎯 **Exam Tip:** Variance tells you how "spread out" data is. Small variance = data clustered near mean.

### Example:
Data: [2, 4, 4, 4, 5, 5, 7, 9]
- Mean = (2+4+4+4+5+5+7+9) / 8 = 40/8 = **5**
- Variance = [(2-5)² + (4-5)² + (4-5)² + (4-5)² + (5-5)² + (5-5)² + (7-5)² + (9-5)²] / 8
  = [9+1+1+1+0+0+4+16] / 8 = 32/8 = **4**
- Standard Deviation = √4 = **2**

---

## 1.6 Common Probability Distributions

### Normal Distribution (Bell Curve) ⭐
- Symmetric, bell-shaped
- Described by mean (μ) and std dev (σ)
- **68-95-99.7 Rule:**
  - 68% of data falls within 1σ of mean
  - 95% within 2σ
  - 99.7% within 3σ

### Binomial Distribution:
- For n trials, each with probability p of success
```
P(X = k) = C(n,k) × p^k × (1-p)^(n-k)
```
- Example: Toss a fair coin 10 times. P(exactly 6 heads)?
  - n=10, k=6, p=0.5
  - P = C(10,6) × 0.5⁶ × 0.5⁴ = 210 × 0.015625 × 0.0625 ≈ **0.205**

---

## 1.7 Central Limit Theorem (CLT) ⭐

> **Plain English:** If you take many large samples from ANY distribution and calculate their means, those means will follow a **Normal distribution** — no matter what the original distribution looked like!

- **Why it matters:** This is why we can use normal distribution assumptions in statistics even when data isn't normal.
- Sample mean distribution: Mean = μ, Standard Deviation = σ/√n

---

## 1.8 Hypothesis Testing

### The Idea:
- You have a **null hypothesis (H₀):** "Nothing special is happening" (e.g., "Drug has no effect")
- You have an **alternative hypothesis (H₁):** "Something IS happening"
- You collect data and decide whether to **reject H₀** or **not**

### p-value:
- Probability of getting your result (or more extreme) IF H₀ were true
- If p-value < 0.05: **Reject H₀** (result is statistically significant)
- If p-value > 0.05: **Fail to reject H₀**

### Key Tests:

| Test | When to Use |
|---|---|
| **t-test** | Compare means, small sample, unknown variance |
| **z-test** | Compare means, large sample (n > 30) OR known variance |
| **Chi-square (χ²) test** | Test if categorical data fits expected distribution; test independence |
| **F-test** | Compare variances; used in ANOVA |

### t-test Example:
> A company claims their battery lasts 500 hours. You test 25 batteries and find mean = 490 hours, std dev = 20 hours. Is the claim false?

- H₀: μ = 500, H₁: μ ≠ 500
- t = (490 - 500) / (20/√25) = -10 / 4 = **-2.5**
- Check t-table for 24 degrees of freedom at 0.05 significance → critical value ≈ 2.064
- |t| = 2.5 > 2.064 → **Reject H₀. The battery claim is likely false.**

---

---

# 📗 SECTION 2: LINEAR ALGEBRA

> 🧠 **Plain English First:** Linear Algebra = the mathematics of data organized in tables (matrices) and arrows with direction (vectors). Everything in AI — images, text, predictions — is stored as matrices and vectors.

---

## 2.1 Vectors

A vector is a list of numbers with both **magnitude (size)** and **direction**.

```
v = [3, 4]    ← 2D vector
w = [1, 2, 3] ← 3D vector
```

### Vector Operations:
- **Addition:** Add element-by-element: [1,2] + [3,4] = [4,6]
- **Scalar multiplication:** Multiply each element: 3 × [1,2] = [3,6]
- **Dot Product:** `a · b = a₁b₁ + a₂b₂ + ...`
  - Example: [1,2] · [3,4] = 1×3 + 2×4 = 3 + 8 = **11**
  - If dot product = 0, vectors are **perpendicular (orthogonal)**

### Magnitude (Length) of a vector:
```
|v| = √(v₁² + v₂² + ... + vₙ²)
```
- Example: |[3,4]| = √(9+16) = √25 = **5**

### Distance between vectors:
```
distance = |a - b| = √(sum of (aᵢ - bᵢ)²)
```
This is called **Euclidean Distance** — used heavily in ML (kNN algorithm!)

---

## 2.2 Matrices

A matrix is a 2D array of numbers.

```
A = [1  2  3]    ← 2×3 matrix (2 rows, 3 columns)
    [4  5  6]
```

### Matrix Operations:

**Addition:** Same size matrices, add element-by-element.

**Multiplication (A × B):**
- A must be (m × n), B must be (n × p) → Result is (m × p)
- Each element of result = dot product of A's row with B's column

```
[1  2] × [5  6] = [1×5+2×7  1×6+2×8] = [19  22]
[3  4]   [7  8]   [3×5+4×7  3×6+4×8]   [43  50]
```

> ⚠️ Matrix multiplication is NOT commutative! A×B ≠ B×A in general.

### Transpose (Aᵀ):
- Flip rows and columns
```
A = [1  2  3]  →  Aᵀ = [1  4]
    [4  5  6]           [2  5]
                         [3  6]
```

### Identity Matrix (I):
- Like the number "1" for matrices
- Diagonal is 1, rest is 0
- A × I = A

---

## 2.3 Rank of a Matrix

- Rank = number of **linearly independent rows (or columns)**
- Think of it as: "How much unique information does this matrix carry?"
- If rank < number of rows/columns → some rows are redundant (one is a combination of others)

### Example:
```
A = [1  2]
    [2  4]   ← Row 2 = 2 × Row 1. So rank = 1 (only 1 independent row)
```

### Why rank matters in AI:
- Low rank = redundant features in your data
- Used in **dimensionality reduction** (PCA, SVD)

---

## 2.4 Null Space

- The set of all vectors x such that: **A × x = 0**
- If null space contains only the zero vector: columns are linearly independent
- Used to understand if a system of equations has a unique solution

---

## 2.5 Solving Systems of Equations

System: Ax = b (where A is matrix of coefficients, x is unknowns, b is right-hand side)

**Cases:**
1. **Unique solution:** Rank(A) = number of unknowns → exactly one solution
2. **No solution:** Equations contradict each other
3. **Infinite solutions:** Some equations are redundant

**Pseudo-inverse (A⁺):**
- When A is not square or not invertible
- Used to find the **best approximate solution**
- `x = A⁺ × b`
- This is the foundation of **Least Squares** in ML!

---

## 2.6 Projections

- Projection of vector b onto vector a:
```
proj_a(b) = (b·a / |a|²) × a
```

### Why this matters for ML:
- Linear regression finds the projection of the output onto the space spanned by input features
- PCA projects data onto directions of maximum variance

---

## 2.7 Eigenvalues and Eigenvectors ⭐ (Very Important!)

### What are they?
For a matrix A, if: **A × v = λ × v**
- **v** is an eigenvector (a special direction that doesn't change, just scales)
- **λ** (lambda) is the eigenvalue (how much the eigenvector scales)

### How to find eigenvalues:
```
Solve: det(A - λI) = 0
```

### Example (2×2 matrix):
```
A = [4  1]
    [2  3]

det(A - λI) = det([4-λ   1 ]) = (4-λ)(3-λ) - 2 = λ² - 7λ + 10 = 0
                  [2    3-λ])

λ = 5 or λ = 2  ← eigenvalues
```

### Why eigenvalues matter for AI:
- **PCA (Principal Component Analysis):** Eigenvectors = principal components; eigenvalues = importance of each direction
- **Google PageRank:** Uses eigenvectors to rank web pages
- **Stability analysis** in optimization

---

---

# 📙 SECTION 3: OPTIMIZATION

> 🧠 **Plain English First:** Optimization = finding the minimum or maximum of some function. In ML, we want to minimize "error" (loss). The way we do this is called optimization.

---

## 3.1 Types of Optimization

| Type | Description | Example |
|---|---|---|
| **Unconstrained** | No restrictions on variable values | Minimize loss function |
| **Constrained** | Variables must satisfy conditions | Minimize cost, but only use ≤ budget |
| **Convex** | Only one global minimum (bowl shape) | Linear regression loss |
| **Non-convex** | Multiple local minima (hilly terrain) | Deep neural networks |

---

## 3.2 Univariate Optimization (One Variable)

To find minimum/maximum of f(x):

1. Find derivative: f'(x) = 0 → These are "critical points"
2. Check second derivative:
   - f''(x) > 0 → **minimum** (smile shape)
   - f''(x) < 0 → **maximum** (frown shape)

### Example:
Minimize f(x) = x² - 4x + 5
- f'(x) = 2x - 4 = 0 → x = 2
- f''(x) = 2 > 0 → **minimum** at x = 2
- f(2) = 4 - 8 + 5 = **1**

---

## 3.3 Multivariate Optimization (Multiple Variables)

For f(x₁, x₂, ..., xₙ):

1. Find **partial derivatives** and set all to 0:
   - ∂f/∂x₁ = 0, ∂f/∂x₂ = 0, ...
2. Solve the system of equations

### Partial Derivative (Simple Explanation):
- Treat all other variables as constants and differentiate with respect to one variable
- Example: f(x,y) = x² + 3xy + y²
  - ∂f/∂x = 2x + 3y
  - ∂f/∂y = 3x + 2y

---

## 3.4 Gradient Descent ⭐ (Heart of Machine Learning!)

### The Intuition:
Imagine you're blindfolded on a hilly terrain and want to reach the valley (minimum). You feel the slope around you and take a small step downhill. Repeat until you're at the bottom.

### Algorithm:
```
Start at any point x₀
Repeat:
  x_new = x_old - α × gradient(f at x_old)
Until convergence
```

Where:
- **α (alpha)** = learning rate (step size)
- **gradient** = direction of steepest ascent; we subtract it to go down

### Learning Rate:
- Too small α → very slow convergence
- Too large α → overshooting, may never converge
- Just right → converges to minimum

### Variants:
| Type | Update Using |
|---|---|
| **Batch GD** | Entire dataset |
| **Stochastic GD (SGD)** | One random sample at a time |
| **Mini-batch GD** | Small batch (e.g., 32 samples) — most common in practice |

---

---

# 📕 SECTION 4: BASIC MACHINE LEARNING

> 🧠 **Plain English First:** Machine Learning = teaching computers to learn patterns from data instead of programming every rule manually.

---

## 4.1 Core ML Concepts

### Supervised vs Unsupervised Learning:
- **Supervised:** You have labelled data (input + correct output). Learn to predict output for new inputs.
  - Examples: Spam detection, house price prediction
- **Unsupervised:** No labels. Find hidden patterns.
  - Examples: Customer segmentation, anomaly detection

### Overfitting vs Underfitting:
- **Overfitting:** Model memorizes training data, fails on new data ("too complex")
- **Underfitting:** Model too simple, can't even fit training data ("too simple")
- **Goal:** Find the sweet spot (generalization)

---

## 4.2 Linear Regression ⭐

### Simple Linear Regression:
Predict a continuous output y from one input x:
```
y = mx + b   (or: ŷ = β₀ + β₁x)
```
- β₀ = intercept (value when x=0)
- β₁ = slope (how much y changes per unit increase in x)

### Multiple Linear Regression:
Multiple inputs x₁, x₂, ..., xₙ:
```
ŷ = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ
```
In matrix form: **ŷ = Xβ**

### Least Squares (How we find β):
Minimize the **Sum of Squared Errors (SSE)**:
```
SSE = Σ(yᵢ - ŷᵢ)²   (actual - predicted)²
```
Optimal solution: **β = (XᵀX)⁻¹ Xᵀ y**

This is the pseudo-inverse of X applied to y!

### Example:
> You have data: Hours studied (x) vs Marks (y):
> x: [1, 2, 3, 4, 5], y: [50, 55, 65, 70, 80]
>
> Fit a line and predict marks for 6 hours.

---

## 4.3 Logistic Regression ⭐

> Despite the name, this is a **classification** algorithm!

### Idea:
Instead of predicting a number, predict a **probability (0 to 1)** that an input belongs to class 1.

### Sigmoid Function:
```
σ(z) = 1 / (1 + e^(-z))
```
- Always outputs between 0 and 1
- If σ(z) > 0.5 → predict class 1
- If σ(z) < 0.5 → predict class 0

### Decision Boundary:
```
z = β₀ + β₁x₁ + β₂x₂  ← Linear combination
ŷ = σ(z)
```

### Loss Function (Log Loss / Cross-Entropy):
```
L = -[y × log(ŷ) + (1-y) × log(1-ŷ)]
```

### Real-World Uses:
- Email spam or not spam
- Patient has disease or not
- Customer will churn or not

---

## 4.4 k-Nearest Neighbors (kNN) ⭐

### Idea (Lazy Learning!):
To classify a new point, look at its **k nearest neighbours** in training data and take a majority vote.

### Distance Metric:
Usually Euclidean Distance:
```
d(p, q) = √Σ(pᵢ - qᵢ)²
```

### How k affects results:
- Small k (e.g., k=1) → Overfitting (too sensitive to noise)
- Large k (e.g., k=100) → Underfitting (too smooth)
- Optimal k: found via cross-validation

### Example:
> You want to classify a fruit as apple or orange based on weight and color.
> Find 3 nearest labelled fruits. If 2 are apples and 1 is orange → **Classify as Apple**

---

## 4.5 k-Means Clustering ⭐

### Idea (Unsupervised):
Group n data points into k clusters without labels.

### Algorithm:
1. Randomly pick k points as cluster centers (centroids)
2. Assign each data point to the nearest centroid
3. Update each centroid to be the mean of its assigned points
4. Repeat steps 2-3 until centroids don't move

### Choosing k:
- **Elbow Method:** Plot SSE vs k. Choose k where improvement slows ("elbow")

### Exam-style Question:
> Data points: [1], [2], [8], [9], [10]. k=2.
> Initial centroids: 1 and 8.
> Round 1: {1,2} cluster (centroid=1), {8,9,10} cluster (centroid=9)
> Round 2: Assign to 1 or 9 → {1,2} → {8,9,10}, centroids become (1.5) and (9) → converged!

---

## 4.6 Cross-Validation ⭐

### Why it's needed:
To estimate how well your model generalizes to unseen data without wasting test data.

### k-Fold Cross-Validation:
1. Split data into k equal parts (folds)
2. Train on k-1 folds, test on remaining 1 fold
3. Repeat k times (each fold gets to be test set once)
4. Average the k scores → final performance estimate

### Common Values:
- k=5 or k=10 are standard
- **Leave-One-Out (LOO):** k = n (each point is its own test set) — computationally expensive

### Why not just use train/test split?
- High variance in performance estimate
- Wastes data

---

## 4.7 Model Evaluation Metrics

### For Classification:

| Metric | Formula | Meaning |
|---|---|---|
| **Accuracy** | Correct predictions / Total | Overall correctness |
| **Precision** | TP / (TP + FP) | Of predicted positives, how many are actually positive? |
| **Recall** | TP / (TP + FN) | Of actual positives, how many did we find? |
| **F1 Score** | 2 × (Precision × Recall) / (Precision + Recall) | Balance of precision and recall |

### Confusion Matrix:
```
              Predicted Positive | Predicted Negative
Actual Positive:    TP           |       FN
Actual Negative:    FP           |       TN
```

### For Regression:
- **MSE (Mean Squared Error):** Average of (actual - predicted)²
- **RMSE:** √MSE
- **MAE:** Average of |actual - predicted|
- **R² Score:** How much variance in y is explained by the model. 1 = perfect, 0 = no better than mean

---

---

# 🔑 QUICK REFERENCE — Formulas to Memorize

## Probability:
```
P(A|B) = P(A∩B) / P(B)
P(A∩B) = P(A) × P(B)  [if independent]
Bayes: P(A|B) = P(B|A) × P(A) / P(B)
Binomial: P(X=k) = C(n,k) × p^k × (1-p)^(n-k)
```

## Statistics:
```
Mean = Σxᵢ/n
Variance = Σ(xᵢ - μ)²/n
Std Dev = √Variance
z-score = (x - μ) / σ    ← How many std devs from mean?
t-statistic = (x̄ - μ) / (s/√n)
```

## Linear Algebra:
```
|v| = √(v₁² + v₂² + v₃²)
a·b = Σaᵢbᵢ
det([a b; c d]) = ad - bc
Eigenvalue: det(A - λI) = 0
Least Squares: β = (XᵀX)⁻¹Xᵀy
```

## Optimization:
```
Gradient Descent: x = x - α∇f(x)
Minimum condition: f'(x) = 0 AND f''(x) > 0
```

---

# 🧪 EXAM-STYLE PRACTICE QUESTIONS

## Section A: Probability

**Q1.** In a group of 100 people, 60 drink tea, 50 drink coffee, and 20 drink both. What is the probability that a randomly selected person drinks tea or coffee?
> Answer: P(T∪C) = P(T) + P(C) - P(T∩C) = 0.6 + 0.5 - 0.2 = **0.9**

**Q2.** A die is rolled twice. What is the probability that the sum is 7?
> Favourable: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) = 6 cases. Total = 36. P = 6/36 = **1/6**

**Q3.** Box A has 2 red, 3 blue balls. Box B has 4 red, 1 blue ball. A box is chosen at random and a ball is drawn. It's red. What is the probability it came from Box A?
> P(A) = P(B) = 0.5; P(Red|A) = 2/5; P(Red|B) = 4/5
> P(Red) = 0.5×0.4 + 0.5×0.8 = 0.2 + 0.4 = 0.6
> P(A|Red) = (0.4 × 0.5) / 0.6 = 0.2/0.6 = **1/3 ≈ 0.333**

## Section B: Linear Algebra

**Q4.** What is the dot product of [2, -1, 3] and [4, 2, -1]?
> 2×4 + (-1)×2 + 3×(-1) = 8 - 2 - 3 = **3**

**Q5.** Find the rank of:
```
[1  2  3]
[2  4  6]
[0  1  2]
```
> Row 2 = 2 × Row 1. So after elimination: 2 independent rows. Rank = **2**

**Q6.** Matrix A = [3 1; 0 2]. Find eigenvalues.
> det([3-λ  1; 0  2-λ]) = (3-λ)(2-λ) = 0
> λ = **3 or 2**

## Section C: ML

**Q7.** In kNN with k=3, a new point has neighbours with labels [Positive, Negative, Positive]. What class is predicted?
> Majority vote: 2 Positive, 1 Negative → **Positive**

**Q8.** A model has: TP=40, TN=30, FP=10, FN=20. Calculate Accuracy, Precision, and Recall.
> Accuracy = (40+30)/(40+30+10+20) = 70/100 = **0.70**
> Precision = 40/(40+10) = 40/50 = **0.80**
> Recall = 40/(40+20) = 40/60 = **0.667**

**Q9.** You run k-means with k=2 on: [2,4,10,12,3,11]. Starting centroids: 2 and 10.
> Distances from 2: |2-2|=0, |4-2|=2, |10-2|=8, |12-2|=10, |3-2|=1, |11-2|=9
> Distances from 10: |2-10|=8, |4-10|=6, |10-10|=0, |12-10|=2, |3-10|=7, |11-10|=1
> Cluster 1 (near 2): {2, 4, 3} → centroid = 3
> Cluster 2 (near 10): {10, 12, 11} → centroid = 11
> **Final clusters: {2,3,4} and {10,11,12}**

---

# 📚 RECOMMENDED FREE RESOURCES

| Topic | Resource |
|---|---|
| **Probability & Stats** | Khan Academy — Statistics & Probability (free, beginner-friendly) |
| **Linear Algebra** | 3Blue1Brown "Essence of Linear Algebra" YouTube series (HIGHLY RECOMMENDED — visual!) |
| **ML Basics** | Google's Machine Learning Crash Course (free) |
| **Python + ML** | Kaggle Learn — Intro to ML (free, hands-on) |
| **IIT Madras Style** | NPTEL courses by IIT Madras on YouTube (exact professors who may teach you!) |

---

# 🧘 FINAL TIPS FOR EXAM DAY

1. **Attempt ALL questions** — no negative marking typically.
2. For MCQs — **eliminate wrong answers** first; often 2 are clearly wrong.
3. For Numeric answers — **double-check your arithmetic**; small errors cost marks.
4. **Don't spend too much time** on one question — mark and move on.
5. **Read questions carefully** — "at least", "at most", "exactly" change everything in probability.
6. For ML questions — always think about **what the algorithm is doing intuitively** before plugging into formula.
7. **Practice daily** — even 30 minutes of problem-solving is better than 3 hours of just reading.

---

> 💪 **You've got this, Suvam!** 6 years of Software Engineering gives you a massive advantage — you think logically, you understand data, and you know how systems work. The math is just a language to formalize what you already intuitively do. Trust the process, stay consistent, and go get that IIT Madras seat! 🎓

---
*Study Guide prepared based on official IIT Madras WMT AI entrance syllabus | May 2026*