# 📙 TOPIC 3: Calculus & Optimization
### IIT Madras WMT AI Entrance — Complete Notes
> 🟡 **HIGH PRIORITY** | ~10% of exam marks
> 📅 Study Days: 15–18

---

## 🧠 Why This Matters for AI
Every ML algorithm "learns" by minimizing a loss function. Gradient descent, backpropagation, parameter updates — all rely on derivatives. You don't need to be a calculus wizard — but you MUST know the key concepts.

---

# PART 1: FUNCTIONS OF A SINGLE VARIABLE

## 1.1 Limits

**What it means:** What value does f(x) approach as x approaches some point?
```
lim[x→a] f(x) = L   means f(x) gets arbitrarily close to L as x gets close to a
```

**Key limit rules:**
```
lim[x→a] [f(x) + g(x)] = lim f(x) + lim g(x)
lim[x→a] [f(x) × g(x)] = lim f(x) × lim g(x)
lim[x→0] sin(x)/x = 1   ← memorize!
lim[x→∞] (1 + 1/x)^x = e ≈ 2.718   ← memorize!
```

## 1.2 Continuity
f(x) is continuous at x=a if:
```
1. f(a) is defined
2. lim[x→a] f(x) exists
3. lim[x→a] f(x) = f(a)
```
**Common discontinuities:** Jump (step functions), holes, vertical asymptotes.

## 1.3 Differentiability
If f is differentiable at a point → it's continuous there (but not vice versa!).

A function is NOT differentiable where:
- It has a corner/kink (like |x| at x=0)
- It's discontinuous
- It has a vertical tangent

---

# PART 2: DERIVATIVES ⭐⭐

## 2.1 What is a Derivative?
The instantaneous rate of change. The slope of the tangent line.
```
f'(x) = df/dx = lim[h→0] [f(x+h) - f(x)] / h
```

## 2.2 Basic Derivative Rules (MEMORIZE!)

```
d/dx [constant] = 0
d/dx [xⁿ] = n × xⁿ⁻¹        ← Power rule
d/dx [eˣ] = eˣ               ← e^x is its own derivative!
d/dx [ln x] = 1/x
d/dx [sin x] = cos x
d/dx [cos x] = -sin x

Chain Rule: d/dx [f(g(x))] = f'(g(x)) × g'(x)
Product Rule: d/dx [f×g] = f'g + fg'
Quotient Rule: d/dx [f/g] = (f'g - fg') / g²
```

**Examples:**
```
d/dx [x³] = 3x²
d/dx [e^(2x)] = 2e^(2x)    ← chain rule: outer=e^u, inner=2x
d/dx [x² × ln x] = 2x × ln x + x² × (1/x) = 2x ln x + x
d/dx [ln(x²+1)] = 2x/(x²+1)   ← chain rule
```

## 2.3 Partial Derivatives
For functions of multiple variables, differentiate with respect to one variable while holding others constant.

```
f(x, y) = x³ + 2x²y + y²

∂f/∂x = 3x² + 4xy    ← treat y as constant
∂f/∂y = 2x² + 2y     ← treat x as constant
```

## 2.4 Gradient ⭐⭐ (Heart of ML!)
The gradient is the vector of all partial derivatives:
```
∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]
```
**Geometric meaning:** The gradient points in the direction of STEEPEST INCREASE.

**So for minimization → move in NEGATIVE gradient direction!** (This is gradient descent!)

---

# PART 3: MAXIMA AND MINIMA ⭐⭐

## 3.1 Finding Critical Points
Critical points: where f'(x) = 0 OR f'(x) is undefined.

## 3.2 Second Derivative Test (Single Variable)
At a critical point x₀ where f'(x₀) = 0:
```
f''(x₀) > 0 → Local MINIMUM  (smile shape ∪)
f''(x₀) < 0 → Local MAXIMUM  (frown shape ∩)
f''(x₀) = 0 → Inconclusive (could be inflection point)
```

**Visual memory:** 
- f'' > 0 means concave UP → water fills the cup = minimum
- f'' < 0 means concave DOWN → water falls out = maximum

## 3.3 Example
**Find min/max of f(x) = x³ - 3x + 2:**
```
f'(x) = 3x² - 3 = 0 → 3(x²-1) = 0 → x = ±1

f''(x) = 6x
f''(1) = 6 > 0  → LOCAL MINIMUM at x=1, f(1) = 1-3+2 = 0
f''(-1) = -6 < 0 → LOCAL MAXIMUM at x=-1, f(-1) = -1+3+2 = 4
```

## 3.4 Global vs Local Extrema
- **Local:** Best in a neighborhood
- **Global:** Best over entire domain

For finding global on closed interval [a,b]:
1. Find all critical points in (a,b)
2. Evaluate f at critical points AND endpoints a,b
3. Largest = global max, smallest = global min

---

# PART 4: TAYLOR SERIES ⭐

## 4.1 What is Taylor Series?
Approximate a complex function using polynomial terms:
```
f(x) ≈ f(a) + f'(a)(x-a) + f''(a)(x-a)²/2! + f'''(a)(x-a)³/3! + ...
```

## 4.2 Maclaurin Series (Taylor at a=0):
```
eˣ = 1 + x + x²/2! + x³/3! + ...
sin x = x - x³/3! + x⁵/5! - ...
cos x = 1 - x²/2! + x⁴/4! - ...
ln(1+x) = x - x²/2 + x³/3 - ...  (valid for |x| < 1)
(1+x)ⁿ ≈ 1 + nx  for small x  ← first-order approximation
```

## 4.3 Why Taylor Matters for ML
- Loss functions are approximated using Taylor series near optimal points
- Newton's method for optimization uses second-order Taylor approximation
- Understanding convergence of gradient descent uses Taylor expansion

## 4.4 First-Order Approximation (Linear Approximation):
```
f(x) ≈ f(a) + f'(a)(x - a)   for x near a
```
This is exactly how gradient descent computes local behavior!

---

# PART 5: OPTIMIZATION ⭐⭐⭐

## 5.1 Types of Optimization Problems

### Unconstrained:
```
minimize f(x)   with no restrictions on x
```

### Constrained:
```
minimize f(x)
subject to: g(x) = 0  (equality constraint)
            h(x) ≤ 0  (inequality constraint)
```

## 5.2 Gradient Descent ⭐⭐⭐ (Most important for AI)

### The Algorithm:
```
Initialize: x₀ (random or zeros)
Repeat:
    x_{t+1} = x_t - α × ∇f(x_t)
Until: |∇f| ≈ 0 OR max iterations reached
```

### Learning Rate α:
- **Too small:** Takes forever to converge (thousands of steps)
- **Too large:** Overshoots, may diverge (bounces back and forth)
- **Goldilocks:** Converges efficiently

```
Too small α:    ....→....→....→...→ (slow)
Too large α:    →  ←  →  ← (bouncing, diverging)
Just right α:   → → → ✓ (converges)
```

### Variants:
| Type | Updates using | Pros | Cons |
|---|---|---|---|
| **Batch GD** | Full dataset | Stable, accurate gradient | Slow for large data |
| **SGD** | 1 random sample | Fast per step | Noisy, unstable |
| **Mini-batch GD** | Small batch (32-256) | Balance of above | Most common in practice |

### Convergence Conditions:
- Learning rate satisfies Robbins-Monro conditions for SGD
- For convex functions → guaranteed to reach global minimum
- For non-convex → may get stuck in local minimum

## 5.3 Second-Order Optimization
**Newton's Method:**
```
x_{t+1} = x_t - [H(x_t)]⁻¹ × ∇f(x_t)
```
Where H is the **Hessian matrix** (matrix of second derivatives).

**Hessian:**
```
H = [∂²f/∂x₁²    ∂²f/∂x₁∂x₂  ...]
    [∂²f/∂x₂∂x₁  ∂²f/∂x₂²    ...]
```
- Positive definite Hessian → local minimum
- Negative definite Hessian → local maximum
- Indefinite Hessian → saddle point

## 5.4 Convex vs Non-Convex Optimization

### Convex Function:
```
f(λx + (1-λ)y) ≤ λf(x) + (1-λ)f(y)   for 0 ≤ λ ≤ 1
```
**Plain English:** The function looks like a bowl — any local minimum is the global minimum!

**Test:** f''(x) ≥ 0 everywhere (single variable), or Hessian is positive semidefinite (multivariate)

**Examples of convex functions:**
- MSE loss (linear regression) → bowl shaped → easy to optimize
- Any linear function
- Exponentials, squared functions

**Examples of non-convex:**
- Deep neural network loss functions (many local minima!)
- This is why training neural networks is hard

---

# PART 6: KEY FUNCTIONS IN ML

## 6.1 Sigmoid Function
```
σ(x) = 1 / (1 + e^(-x))

σ'(x) = σ(x)(1 - σ(x))   ← derivative in terms of itself!

Range: (0, 1)   ← outputs probabilities
```
- Squashes any real number to (0,1)
- Used in logistic regression, neural network activation

## 6.2 Softmax Function (multi-class sigmoid):
```
softmax(xᵢ) = e^(xᵢ) / Σⱼ e^(xⱼ)
```
Outputs sum to 1 → probability distribution over classes.

## 6.3 Log Loss (Cross-Entropy):
```
L = -[y log(ŷ) + (1-y) log(1-ŷ)]   binary
L = -Σ yᵢ log(ŷᵢ)                   multi-class
```

Derivative: ∂L/∂ŷ = -(y/ŷ) + (1-y)/(1-ŷ) = (ŷ - y) / [ŷ(1-ŷ)]

## 6.4 MSE Loss:
```
L = (1/n) Σ (yᵢ - ŷᵢ)²

∂L/∂ŷᵢ = -2(yᵢ - ŷᵢ)/n = 2(ŷᵢ - yᵢ)/n
```

---

# 🔑 QUICK REFERENCE

```
DERIVATIVES:
d/dx[xⁿ] = nxⁿ⁻¹
d/dx[eˣ] = eˣ
d/dx[ln x] = 1/x
Chain rule: [f(g(x))]' = f'(g)×g'

CRITICAL POINTS: f'(x)=0
MIN: f''(x) > 0
MAX: f''(x) < 0

GRADIENT DESCENT: x = x - α∇f(x)

CONVEX: f''(x) ≥ 0, one global minimum
```

---

# 🎯 EXAM TIPS & TRICKS

1. **For min/max questions:** Always find f'=0 first, then check f'' sign.

2. **Convexity check:** f is convex ↔ f''(x) ≥ 0 everywhere. For ML: MSE is always convex!

3. **Gradient descent won't converge if:** learning rate too large, non-convex loss with bad initialization.

4. **Taylor series approximation:** For small ε, f(x+ε) ≈ f(x) + f'(x)ε

5. **For closed interval optimization:** Don't forget to check boundary values!

6. **Sigmoid derivative trick:** σ'(x) = σ(x)(1-σ(x)). If σ(x)=0.8, σ'(x)=0.8×0.2=0.16

---

# 📝 PRACTICE QUESTIONS

**Q1.** Find the minimum of f(x) = x² - 6x + 10.
```
f'(x) = 2x - 6 = 0 → x = 3
f''(x) = 2 > 0 → minimum
f(3) = 9 - 18 + 10 = 1
Answer: minimum value = 1 at x=3
```

**Q2.** Gradient of f(x,y) = x²y + y³ at point (1,2)?
```
∂f/∂x = 2xy → at (1,2): 2×1×2 = 4
∂f/∂y = x² + 3y² → at (1,2): 1 + 12 = 13
∇f(1,2) = [4, 13]
```

**Q3.** Which function is convex: f(x) = x², g(x) = x³, h(x) = |x|?
```
f''(x) = 2 > 0 → convex ✓
g''(x) = 6x (negative for x<0) → NOT convex
h(x) is convex (bowl shape) but not differentiable at 0
```

**Q4.** In gradient descent with f(x,y) = x² + y². Current point: (3,4). α=0.1. Next point?
```
∇f = [2x, 2y] = [6, 8] at (3,4)
x_new = [3,4] - 0.1×[6,8] = [3-0.6, 4-0.8] = [2.4, 3.2]
```

---

> 📌 **Next: Read `04_Machine_Learning.md`**
