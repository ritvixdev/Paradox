# 📕 TOPIC 4: Machine Learning — Complete Notes
### IIT Madras WMT AI Entrance — Complete Notes
> 🔴 **HIGHEST PRIORITY** | ~25% of exam marks
> 📅 Study Days: 19–25

---

## 🧠 The Big Picture of ML
```
Data → Feature Extraction → Model Training → Prediction → Evaluation

Supervised:   Input + Label → Learn function → Predict label for new input
Unsupervised: Input only → Find patterns/structure in data
```

---

# PART 1: SUPERVISED LEARNING — REGRESSION

## 1.1 Simple Linear Regression ⭐⭐⭐

**Goal:** Predict continuous output y from one input x.
```
ŷ = β₀ + β₁x
```
- β₀ = intercept (y-value when x=0)
- β₁ = slope (change in y per unit change in x)

### Finding β (Least Squares):
Minimize SSE = Σ(yᵢ - ŷᵢ)² = Σ(yᵢ - β₀ - β₁xᵢ)²

**Formulas:**
```
β₁ = Σ(xᵢ - x̄)(yᵢ - ȳ) / Σ(xᵢ - x̄)²  =  Cov(X,Y) / Var(X)
β₀ = ȳ - β₁x̄
```

**Example:**
x: [1, 2, 3, 4, 5], y: [2, 4, 5, 4, 5]
```
x̄ = 3, ȳ = 4
Σ(xᵢ-x̄)(yᵢ-ȳ) = (−2)(−2)+(−1)(0)+(0)(1)+(1)(0)+(2)(1) = 4+0+0+0+2 = 6
Σ(xᵢ-x̄)² = 4+1+0+1+4 = 10
β₁ = 6/10 = 0.6
β₀ = 4 - 0.6×3 = 4 - 1.8 = 2.2
Line: ŷ = 2.2 + 0.6x
```

### Evaluation Metrics for Regression:
```
SSE (Sum of Squared Errors) = Σ(yᵢ - ŷᵢ)²
MSE = SSE/n
RMSE = √MSE
MAE = Σ|yᵢ - ŷᵢ|/n

R² (Coefficient of Determination) = 1 - SSE/SST
where SST = Σ(yᵢ - ȳ)²  = total variance in y
```

**R² interpretation:**
- R² = 1: Perfect fit (model explains all variance)
- R² = 0: Model no better than predicting mean
- R² can be negative (model worse than mean)!

## 1.2 Multiple Linear Regression

Multiple inputs x₁, x₂, ..., xₚ:
```
ŷ = β₀ + β₁x₁ + β₂x₂ + ... + βₚxₚ
```

**Matrix form:** ŷ = Xβ where X includes a column of 1s for intercept

**Closed-form solution (Normal Equations):**
```
β = (XᵀX)⁻¹Xᵀy
```
This is the PROJECTION of y onto the column space of X!

**Assumptions of Linear Regression:**
1. Linear relationship between X and y
2. Independence of errors
3. Homoscedasticity (constant variance of errors)
4. Normality of errors (for inference)
5. No multicollinearity (features not highly correlated with each other)

## 1.3 Ridge Regression (L2 Regularization) ⭐

**Problem:** When XᵀX is singular (near-singular), normal equation is unstable. Also when p >> n (more features than samples) → overfitting.

**Solution — Add penalty term to loss:**
```
Loss = Σ(yᵢ - ŷᵢ)² + λΣβⱼ²
```

**Solution:**
```
β_ridge = (XᵀX + λI)⁻¹Xᵀy
```

**Effect:**
- λ=0: ordinary least squares
- λ→∞: all β→0 (extreme shrinkage)
- λ > 0: XᵀX + λI is ALWAYS invertible → solves singularity problem!
- Ridge shrinks coefficients but doesn't make them exactly 0

**vs LASSO (L1 regularization):** Loss = SSE + λΣ|βⱼ|
- LASSO can make coefficients exactly 0 → feature selection!
- Ridge doesn't do feature selection

---

# PART 2: SUPERVISED LEARNING — CLASSIFICATION

## 2.1 Logistic Regression ⭐⭐⭐

**Goal:** Predict probability of class 1 given input X.

**Model:**
```
P(y=1|x) = σ(β₀ + β₁x₁ + ... + βₚxₚ)
where σ(z) = 1/(1 + e^(-z))  ← sigmoid function
```

**Decision rule:**
```
Predict class 1 if P(y=1|x) > 0.5  (threshold can be changed)
0.5 threshold ↔ β₀ + β₁x₁ + ... = 0 is the decision boundary
```

**Training: Maximum Likelihood Estimation (MLE)**
Minimize negative log-likelihood (= cross-entropy loss):
```
L = -Σ[yᵢ log(ŷᵢ) + (1-yᵢ) log(1-ŷᵢ)]
```
No closed form → use gradient descent.

**Gradient:**
```
∂L/∂β = Xᵀ(ŷ - y)   ← elegant formula!
```

**Multi-class:** One-vs-Rest or Softmax (multinomial logistic regression).

## 2.2 k-Nearest Neighbours (kNN) ⭐⭐

**How it works (Lazy Learner — no training!):**
1. Store all training data
2. For new point x:
   - Calculate distance to all training points
   - Find k nearest neighbours
   - Majority vote for classification / average for regression

**Distance metrics:**
```
Euclidean: d = √Σ(xᵢ-yᵢ)²     ← most common
Manhattan: d = Σ|xᵢ-yᵢ|        ← less sensitive to outliers
Minkowski: d = (Σ|xᵢ-yᵢ|^p)^(1/p)  ← generalizes above
```

**Effect of k:**
- k=1: Very flexible, overfits to noise
- Large k: Very smooth, underfits
- Optimal k: Found via cross-validation

**Curse of Dimensionality:** kNN performance degrades in high dimensions! All points become equidistant.

**Computational cost:** O(nd) per prediction where n=training size, d=dimensions → slow for large data.

## 2.3 Naive Bayes Classifier ⭐

**Applies Bayes theorem with "naive" assumption: features are conditionally independent given class.**

```
P(y|x₁,...,xₙ) ∝ P(y) × P(x₁|y) × P(x₂|y) × ... × P(xₙ|y)
```

**Classify:** Predict class with highest posterior probability.

**Types:**
- **Gaussian NB:** Features are normally distributed
- **Multinomial NB:** Features are counts (text classification!)
- **Bernoulli NB:** Binary features

**Why "Naive"?** In reality features ARE correlated. But it still works well in practice (especially text classification).

**Log trick:** Instead of multiplying probabilities (underflow), sum log probabilities:
```
log P(y|x) ∝ log P(y) + Σ log P(xᵢ|y)
```

## 2.4 Linear Discriminant Analysis (LDA) ⭐

**Find a linear combination of features that best separates classes.**

**Key assumptions:**
- Classes have same covariance matrix (homoscedasticity)
- Features are normally distributed within each class

**Fisher's LDA:** Maximize ratio of between-class variance to within-class variance:
```
J(w) = wᵀSBw / wᵀSWw
```
Where SB = between-class scatter, SW = within-class scatter.

**Also used for dimensionality reduction** (like PCA but supervised — uses class labels).

## 2.5 Support Vector Machine (SVM) ⭐⭐

**Goal:** Find the hyperplane that MAXIMALLY SEPARATES the two classes.

**The Margin:** Distance between the hyperplane and the nearest points of each class (support vectors).

**Hard Margin SVM (linearly separable):**
```
Maximize: 2/||w||  (margin width)
Subject to: yᵢ(wᵀxᵢ + b) ≥ 1  for all i
```

**Soft Margin SVM (allows some misclassifications):**
```
Minimize: (1/2)||w||² + C×Σξᵢ
Subject to: yᵢ(wᵀxᵢ + b) ≥ 1 - ξᵢ, ξᵢ ≥ 0
```
- C = regularization parameter
- Large C: tries to classify all correctly (may overfit)
- Small C: allows more errors (smoother boundary)

**Kernel Trick (for non-linear separation):**
Map data to higher dimension where it becomes linearly separable.

Common kernels:
```
Linear: K(x,y) = xᵀy
Polynomial: K(x,y) = (xᵀy + c)^d
RBF/Gaussian: K(x,y) = exp(-γ||x-y||²)   ← most popular
Sigmoid: K(x,y) = tanh(αxᵀy + c)
```

**Support Vectors:** Only the training points on or within the margin matter! (sparse representation)

## 2.6 Decision Trees ⭐⭐

**A tree-based model that makes sequential binary decisions.**

**Building the Tree (Recursive Partitioning):**
1. At each node, choose the feature and threshold that best splits the data
2. "Best" = minimizes impurity (Gini) or maximizes information gain (entropy)
3. Repeat recursively until stopping criterion met

### Impurity Measures:

**Gini Impurity:**
```
Gini(S) = 1 - Σ pᵢ²
where pᵢ = fraction of class i samples in node S
```
Ranges from 0 (pure) to 0.5 (most impure for binary).

**Entropy (Information Gain):**
```
Entropy(S) = -Σ pᵢ log₂(pᵢ)
Information Gain = Entropy(parent) - weighted avg Entropy(children)
```

**Example:**
Node with 10 samples: 6 class A, 4 class B
```
Gini = 1 - (6/10)² - (4/10)² = 1 - 0.36 - 0.16 = 0.48
Entropy = -(0.6)log₂(0.6) - (0.4)log₂(0.4) = 0.971
```

**Pros:** Interpretable, no scaling needed, handles mixed types.
**Cons:** Tends to overfit, unstable (small data changes → big tree changes).

**Pruning:** Remove branches that don't improve validation performance → reduce overfitting.

---

# PART 3: BIAS-VARIANCE TRADEOFF ⭐⭐⭐ (ALWAYS ASKED!)

## The Core Concept
```
Total Error = Bias² + Variance + Irreducible Noise
```

**Bias:** How far off are predictions on average? (Systematic error)
- High bias = underfitting (model too simple)
- Example: Fitting a line through curved data

**Variance:** How much do predictions vary for different training sets? (Sensitivity to training data)
- High variance = overfitting (model too complex, memorizes noise)
- Example: Fitting a 20-degree polynomial through 5 data points

```
                    Simple Model          Complex Model
Bias:               HIGH                  LOW
Variance:           LOW                   HIGH
Training Error:     HIGH                  LOW
Test Error:         HIGH (underfitting)   HIGH (overfitting)
```

**The Sweet Spot:** Find model complexity where test error is minimized.

## Bias-Variance for Common Models:

| Model | Bias | Variance |
|---|---|---|
| Linear Regression | High if data is non-linear | Low |
| Deep Neural Network | Low | High (if small data) |
| kNN (k=1) | Low | High |
| kNN (large k) | High | Low |
| Ridge Regression (large λ) | High | Low |
| Decision Tree (full depth) | Low | High |
| Decision Tree (pruned) | Higher | Lower |

---

# PART 4: CROSS-VALIDATION ⭐⭐

## 4.1 Why Cross-Validation?
- You can't just evaluate on training data (optimistic)
- You need to estimate generalization performance
- You don't want to waste data for a fixed test set

## 4.2 k-Fold Cross-Validation

```
Algorithm:
1. Split data into k equal folds
2. For each fold i = 1 to k:
   a. Use fold i as validation set
   b. Train on remaining k-1 folds
   c. Evaluate on fold i → get score_i
3. Final performance = average of k scores
```

**Typical values:** k=5 or k=10.

**Key properties:**
- Each sample used exactly once for validation
- Less variance in estimate than single train/test split
- k=n is LOO, k=10 is most common

## 4.3 Leave-One-Out (LOO) Cross-Validation

```
k = n (one sample left out each time)
```

**Pros:** Uses all data for training, unbiased estimate.
**Cons:** Computationally expensive (n models trained), high variance.

**When to use LOO:** Very small datasets where you can't afford to lose training data.

## 4.4 Stratified k-Fold

Ensures each fold has same class proportion as original dataset.
**Important for imbalanced datasets!**

## 4.5 Hyperparameter Tuning with Cross-Validation:

```
For each hyperparameter value:
    Compute k-fold CV score
Select hyperparameter with best CV score
Train final model on ALL data with best hyperparameter
```

---

# PART 5: MULTI-LAYER PERCEPTRON (MLP) / NEURAL NETWORKS ⭐⭐

## 5.1 Biological Inspiration
Loosely inspired by neurons in the brain. Each neuron:
- Receives inputs
- Computes weighted sum
- Applies activation function
- Passes output to next layer

## 5.2 Architecture of MLP
```
Input Layer → Hidden Layer(s) → Output Layer

Each layer: z = Wx + b    (linear transformation)
           a = f(z)       (activation function)
```

## 5.3 Activation Functions
```
Sigmoid: σ(z) = 1/(1+e^(-z))      Range: (0,1)   ← vanishing gradient problem
Tanh:    tanh(z) = (e^z-e^(-z))/(e^z+e^(-z))   Range: (-1,1)
ReLU:    f(z) = max(0, z)          Range: [0,∞)   ← most popular now
Leaky ReLU: max(αz, z) for small α ← avoids "dying ReLU"
Softmax: output layer for multi-class
```

**Why ReLU is popular:**
- No vanishing gradient for positive values
- Computationally cheap
- Sparse activation (neurons can be "dead" → regularization effect)

## 5.4 Forward Propagation
Pass input through layers, computing output step by step.

For 2-layer network (1 hidden layer):
```
z₁ = W₁x + b₁
a₁ = f(z₁)         ← hidden layer output
z₂ = W₂a₁ + b₂
ŷ  = g(z₂)         ← output (e.g., sigmoid for binary class)
```

## 5.5 Backpropagation ⭐
**How neural networks learn — chain rule applied backwards.**

1. Compute loss: L = loss(y, ŷ)
2. Compute ∂L/∂ŷ
3. Apply chain rule backwards through each layer
4. Update weights: W ← W - α × ∂L/∂W

**Key insight:** Chain rule means errors propagate backwards through the network, telling each weight how much it contributed to the error.

**Vanishing gradient problem:** In deep networks, gradients can become very small (especially with sigmoid/tanh), making learning of early layers very slow.

**Solutions:** ReLU activation, batch normalization, residual connections (skip connections).

---

# PART 6: UNSUPERVISED LEARNING

## 6.1 k-Means Clustering ⭐⭐

### Algorithm:
```
1. Initialize: pick k centroids (randomly or via k-means++)
2. Assignment: assign each point to nearest centroid
3. Update: move centroids to mean of assigned points
4. Repeat 2-3 until convergence (centroids don't move)
```

### Objective Function:
```
Minimize: Σᵢ Σₓ∈Cᵢ ||x - μᵢ||²
(sum of squared distances to cluster centers)
```

### Properties:
- Converges to LOCAL minimum (not necessarily global!)
- Sensitive to initialization → use k-means++ or run multiple times
- Assumes clusters are spherical and similar size → bad for elongated clusters
- Must specify k beforehand

### Choosing k — Elbow Method:
Plot SSE vs k. As k increases, SSE decreases. Look for "elbow" where decrease slows.

```
k:   1    2    3    4    5    6
SSE: 100  60   30   25   22   20
         ←bend here → k=3 is good
```

## 6.2 k-Medoid (vs k-Means)
- Uses actual data points as centroids (medoids) instead of means
- More robust to outliers than k-means
- Medoid = data point that minimizes sum of distances to others in cluster

## 6.3 Hierarchical Clustering ⭐

**No need to specify k! Produces a dendrogram (tree of merges).**

### Agglomerative (Bottom-Up) — most common:
```
1. Start: each point is its own cluster
2. Find two closest clusters
3. Merge them
4. Repeat until one cluster
5. Cut dendrogram at desired level to get k clusters
```

### Divisive (Top-Down):
Start with one cluster, recursively split.

### Linkage Criteria (how to measure distance between clusters):
```
Single linkage:   distance = min distance between points in clusters
                  → can create long "chain" clusters (chaining effect)
Complete linkage: distance = max distance between points
                  → compact, spherical clusters
Average linkage:  distance = average of all pairwise distances
                  → compromise
Ward linkage:     minimize increase in total within-cluster variance
                  → usually best, similar to k-means
```

### Dendrogram Reading:
- Height of merge = distance at which clusters merged
- Cut at height h → all clusters separated by more than h are distinct

## 6.4 Principal Component Analysis (PCA) ⭐⭐⭐

### Goal: Reduce dimensionality while preserving maximum variance.

### Steps:
```
1. Standardize data (subtract mean, divide by std for each feature)
2. Compute covariance matrix: C = (1/n) XᵀX
3. Compute eigenvalues and eigenvectors of C
4. Sort eigenvectors by eigenvalue (largest first)
5. Select top k eigenvectors (principal components)
6. Project data: Z = XW  where W = top k eigenvectors
```

### Key Concepts:
- **Principal Components:** Eigenvectors of covariance matrix (orthogonal directions of maximum variance)
- **Eigenvalues:** Amount of variance captured by each component
- **Explained Variance Ratio:** λᵢ / Σλⱼ (proportion of total variance in component i)

### How Many Components to Keep?
- Keep components that explain 95% of variance
- Or look at scree plot (eigenvalues vs component number)

### PCA via SVD:
```
X = UΣVᵀ
Principal components = columns of V
Scores (projected data) = XV = UΣ
Eigenvalues of covariance matrix = σᵢ²/n
```

### Limitations:
- Only captures LINEAR relationships
- Sensitive to scale (must standardize!)
- Components are less interpretable than original features
- Not directly supervised (doesn't use labels)

### Example Intuition:
You have data of people's height and weight (2D). PCA finds that the first principal component is roughly "body size" (both height and weight increase together). Keeping just this one component preserves most variance.

---

# PART 7: MODEL EVALUATION

## 7.1 Classification Metrics ⭐⭐

### Confusion Matrix:
```
                  Predicted Positive    Predicted Negative
Actual Positive:       TP                    FN
Actual Negative:       FP                    TN
```

### Key Metrics:
```
Accuracy  = (TP + TN) / (TP + TN + FP + FN)
Precision = TP / (TP + FP)     ← of predicted positives, how many are correct?
Recall    = TP / (TP + FN)     ← of actual positives, how many did we find?
F1 Score  = 2 × (Precision × Recall) / (Precision + Recall)
Specificity = TN / (TN + FP)  ← true negative rate
```

### When to use which:
- **High Precision needed:** Spam filter (don't want legit emails as spam)
- **High Recall needed:** Cancer detection (don't want to miss cancer)
- **F1:** When you want balance of precision and recall
- **Accuracy:** Balanced dataset. Don't use for imbalanced!

### ROC Curve and AUC:
- **ROC curve:** Plot True Positive Rate (Recall) vs False Positive Rate as threshold varies
- **AUC (Area Under Curve):** 0.5 = random, 1.0 = perfect
- Higher AUC → better model

## 7.2 Regression Metrics
```
MSE  = (1/n) Σ(yᵢ - ŷᵢ)²
RMSE = √MSE
MAE  = (1/n) Σ|yᵢ - ŷᵢ|
R²   = 1 - SSE/SST
```

---

# 🔑 QUICK REFERENCE — All ML Formulas

```
LINEAR REGRESSION:
β₁ = Cov(X,Y)/Var(X)
β = (XᵀX)⁻¹Xᵀy

RIDGE:
β_ridge = (XᵀX + λI)⁻¹Xᵀy

LOGISTIC REGRESSION:
P(y=1) = 1/(1 + e^(-wᵀx))
Loss = -Σ[y log(ŷ) + (1-y)log(1-ŷ)]

DECISION TREE:
Gini = 1 - Σpᵢ²
Entropy = -Σpᵢ log₂(pᵢ)

CLASSIFICATION METRICS:
Precision = TP/(TP+FP)
Recall = TP/(TP+FN)
F1 = 2×P×R/(P+R)

PCA:
Covariance matrix C = XᵀX/n
Eigenvectors of C = principal components
```

---

# 🎯 EXAM TIPS & TRICKS FOR ML

1. **Bias-Variance:** More parameters = lower bias, higher variance. Regularization reduces variance at cost of bias.

2. **kNN k selection:** k=1 (overfit), large k (underfit). Use cross-validation.

3. **Naive Bayes "naive":** Assumes conditional independence of features. Still works well in practice!

4. **SVM kernel trick:** Use when data is not linearly separable. RBF kernel is most powerful/flexible.

5. **Decision tree impurity:** Gini=0 or Entropy=0 → pure node. Gini ranges 0-0.5, Entropy 0-1 (binary).

6. **Ridge vs LASSO:**
   - Ridge: shrinks coefficients, never exactly 0, better for correlated features
   - LASSO: can make coefficients 0 → built-in feature selection

7. **PCA:** Always standardize first! First PC = direction of maximum variance.

8. **k-Means limitations:** Must specify k, sensitive to initialization, assumes spherical clusters.

9. **Hierarchical:** Complete linkage = compact clusters, Single linkage = chaining.

10. **For exam: identify algorithm type:**
    - "No training phase, just memory" → kNN
    - "Finds maximum margin hyperplane" → SVM
    - "Assumes feature independence" → Naive Bayes
    - "Reduces features while preserving variance" → PCA
    - "Groups without labels" → Clustering (k-means, hierarchical)

---

# 📝 PRACTICE QUESTIONS (GATE-Style)

**Q1.** For a binary classification with 100 samples: TP=40, FP=10, FN=20, TN=30. Find F1 score.
```
Precision = 40/(40+10) = 40/50 = 0.8
Recall = 40/(40+20) = 40/60 = 0.667
F1 = 2×0.8×0.667/(0.8+0.667) = 1.067/1.467 = 0.727
```

**Q2.** In PCA, if eigenvalues are [5, 3, 1.5, 0.5], how many components to explain 80% variance?
```
Total variance = 5+3+1.5+0.5 = 10
First component: 5/10 = 50%
First two: (5+3)/10 = 80% → 2 components ✓
```

**Q3.** Decision tree splits a node with 20 samples (12 class A, 8 class B). What is the Gini impurity?
```
Gini = 1 - (12/20)² - (8/20)² = 1 - 0.36 - 0.16 = 0.48
```

**Q4.** Which regularization method can set coefficients to exactly zero?
> **LASSO (L1 regularization)** — Ridge (L2) cannot.

**Q5.** A logistic regression model outputs 0.7. What does this mean?
> Probability of class 1 is **70%**. Since 0.7 > 0.5, predicted class = 1.

**Q6.** k-Means clustering: Why might you get different results each run?
> **Random initialization of centroids** — different starting points can converge to different local minima.

**Q7.** What is the time complexity of kNN prediction for n training samples and d features?
> **O(nd)** — must calculate distance to all n training points, each taking O(d) time.

**Q8.** In cross-validation with k=5, how many models are trained?
> **5 models** (one per fold).

**Q9.** What happens to bias and variance when you increase λ in Ridge Regression?
> Higher λ → more regularization → **bias increases, variance decreases**.

**Q10.** A model has 99% training accuracy but 60% test accuracy. What's the problem?
> **Overfitting** (high variance) — model memorized training data but doesn't generalize.

---

> 📌 **Next: Read `05_Quick_Revision_Cheatsheet.md` for final exam prep!**
