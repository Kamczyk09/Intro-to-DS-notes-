
# Introduction to Data Science 

Passing the subject:
- hand-in assignments 
- final exam in January
  - computer based
  - 20/40 points
  - four additional programming assignments, each 24 points, you can get up to 6 points on the main exam for solving them


# Lecture 1 

Definition: An experiment is an activity that produces a distinct outcome.

- $ \Omega $ - sample space that contains all possible outcomes

<u>Ex</u>: Tossing a coin

$$
\Omega = \{ H, T\}
$$

Event: a set of outcomes



An event happens after an experiment if the outcome $ \omega \in \Omega $;  $ \omega \in A $  



<u>What is probability?</u>

(Idea) (Long term relative frequency)
Let's repeat an experiment n-times and count how many times an event A happens


$$
N(A,n) = \frac{\text{number of times A happens}}{n}
$$

- assume the experiment is independent 

Example: if $N(A,n) \to \frac{1}{2}$ as $n \to \infty$ then we could say "50%" chance of happening probability

Rules
1. $N( \Omega, n ) = 1$ - something happens
2. Take two events, A, B. $A \cap B = \emptyset$, then $N(A \cup B, n) = N(A, n) + N(B, n)$


Definition: A function $\mathbb{P}$ that assigns real values to each event is a probability "distribution"/"measure"

if $0 \le \mathbb{P} \le 1$
1. $\mathbb{P}(\Omega) = 1$
2. A, B  $A \cap B = \emptyset$, $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B)$


some other notations and cases:
- A and A' (complement) $\mathbb{P}(A) + \mathbb{P}(A') = 1$
- A and B intersect $\mathbb{P}(A \cap B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cup B)$

Bollies inequality (union bound):
$$
\mathbb{P}(A \cup B) \le \mathbb{P}(A) + \mathbb{P}(B)
$$


## Conditional probability

What is the probability of A, given that I know B happens?
- B becomes the new $\Omega$

$$
\mathbb{P}(A|B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}
$$

Example: SMS messages
- A - "message is spam"
- B - "free appears in the text"

## Law of total probability

Let $A_{1....n}$, $A_i \cap A_j = \emptyset$


$$
\bigcup_{i=1}^{n} A_i = \Omega
$$

then for any $B \in \Omega$

$$
\mathbb{P}(B) = \sum_{i=1}^{n} \mathbb{P}(B|A_i) \mathbb{P}(A_i) = \sum_{i=1}^{n} \mathbb{P}(B \cap A_i)
$$

basically to get probability of B, sum its itersections with A (A makes up the whole omega space)


# Lecture 2

## Random variables


A random variable (RV) is a mapping 
$$
X: \Omega \to \mathbb{R}
$$
that assignes a real number $X(\omega)$ to each outcome $\omega$.




$$
\mathbb{P}(X \le 1) := \mathbb{P}(\{\omega \in \Omega : X(\omega) \le 1\})
$$

all outcomes such that $X(\omega) \le 1$

Example.

$\Omega$ = { all possible texts of length 100}

Experiment: Receiving a text of length <= 100 $\omega$

X(u) = 1 if omega is spam, 0 if not
$$
X(u) = \begin{cases}
1 & \text{if } \omega \text{ is spam} \\
0 & \text{if not}
\end{cases}
$$

$$
P(X=1) = P(\omega \text{ is spam})
$$


**Cumulative distribution function CDF**

$$
F_X: \mathbb{R} \to [0,1] \\
F_X(x) = P(X \le x)
$$
Properties of CDF:
- non decreasing $x1 < x2$ implies that $F_X(x1) \le F_X(x2)$
- F is normalized $\lim_{x \to -\infty} F_X(x) = 0$ and $\lim_{x \to \infty} F_X(x) = 1$
- F is right continuous

- CDF gives the probability that an RV X will take a value less than or equal to a specific value x


If X is discrete, we can define a **probability mass function** (PMF)

$$
f_X(x) = P(X = x)
$$

Connection to the CDF:

$$
F_X(x) = \sum_{t \le x} f_X(t)
$$

For a continuous random variable we distinguish a **probability density function** (PDF) $f_X(x)$. It holds that for PDF:
$$
F_X(x) = \int_{-\infty}^x f_X(t)dt \\
\text{ and } \\
f_X(x) = F'_X(x)
$$

- PDF describes the relative likelihood for a continuous random variable to take on a specific value
- this is not a probability, it can be greater than 1
- total area under the curve must be 1

Inverse CDF (quantile function)

$$
F^{-1}(q) = \inf\{x: F(x) > q\} \\
q \in [0,1]
$$
If F is strictly increasing and continuous then $F^{-1}(F(x)) = x$ and $F(F^{-1}(q)) = q$

- Inverse CDF takes probability q and returns the corresponding value of x (an outcome)

We call 
- first quartile $F^{-1}(0.25)$
- median/second quartile $F^{-1}(0.5)$
- third quartile $F^{-1}(0.75)$

## Transformations of random variables


X is an RV with PDF f_X and CDF F_X. Let Y = g(X) be a transformation of X. How do we compute PDF and CDF of Y?

$$
f_Y(y) = f_X(g^{-1}(y)) \cdot | \frac{d}{dy} g^{-1}(y) | 
$$

## Some important discrete random variables

**Point Mass Distribution**
$$
X \sim \delta_a \text{ if } P(X=a) = 1
$$

$$
F(X) = 
\begin{cases}
0 & x < a \\
1 & x \ge a
\end{cases} \\
f(x) = 1 \text{ if } x = a \text{ else } 0
$$

**Discrete Uniform distribution**
$$
f(x) = \begin{cases}
\frac{1}{k} & \text{for } x = 1,\ldots,k \\
0 & \text{otherwise}
\end{cases}
$$

**Bernoulli distribution**
P(X=1) = p, P(X=0) = 1-p
$$
X \sim Bernoulli(p) \\
f(x) = p^x(1-p)^{1-x}
$$

**Binomial distribution**
Number of successes in n independent Bernoulli trials with success probability p

$$
X \sim Binomial(n, p) \\
f(x) = \binom{n}{x} p^x (1-p)^{n-x} \text{ for } x = 0, 1, ..., n
$$
x - number of successes

**Geometric Distribution**
$$
X \sim Geom(p) \\
P(X=k) = p(1-p)^{k-1}, \quad k \ge 1
$$
- interpretation: number of trials until first success in independent Bernoulli trials with success probability p

**Poisson Distribution**
$$
X \sim Poisson(\lambda) \\
f(x) = \frac{\lambda^x e^{-\lambda}}{x!}, \quad x \ge 0
$$

## Some important continuous random variables

**Uniform Distribution**
$$
X \sim U(a,b) \\
f(x) = \begin{cases}
\frac{1}{b-a} & a \le x \le b \\
0 & \text{otherwise}
\end{cases}
$$
Distribution function is
$$
F(x) = \begin{cases}
0 & x < a \\
\frac{x-a}{b-a} & a \le x \le b \\
1 & x > b
\end{cases}
$$

**Normal Gaussian Distribution**
$$
X \sim N(\mu, \sigma^2) \\
f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\{-\frac{1}{2\sigma^2}(x-\mu)^2\}
$$
- standard normal has sigma=1 and mean=0

$$
X \sim N(\mu, \sigma^2) \\ 
\text{then } Z = \frac{X-\mu}{\sigma} \sim N(0,1)
$$
- sum of gaussian independent RVs has the following distribution

$$
\sum X_i \sim N(\sum \mu_i, \sum \sigma_i^2)
$$

We can compute any probabilities as long as we compute the CDF $\Phi(z)$ of standard Normal

**Exponential distribution**
$$
X \sim Exp(\beta) \\
f(x) = \frac{1}{\beta} e^{-x/\beta}, \quad x > 0
$$

# Lecture 3


## Expectation


Toss a dice 100 times

$$

\frac{1 + 3 + 5 + 2 + ... + 3}{100} = 3.1 (?) 
$$


$$
\frac{\#1}{100} * 1 + \frac{\#2}{100} * 2 + ... + \frac{\#6}{100} * 6  = \\ = 1 * P(X=1) + 2 * P(X=2) + ... + 6 * P(X=6)
$$


$$
\mathbb{E}[X] = \sum_x x f_X(x) \text{ - expectation}\\
\text{reminder - }f_X(x) - P(X=x)
$$

What about random vectors? X is $R^m$ and discrete


$$
\mathbb{E}[X] = \sum_x x f_X(x) = (\sum_{x_1, x_2, ..., x_m}x_1f_X(x_1, x_2, ..., x_m), \\..., \sum_{x_1, x_2, ..., x_m}x_mf_X(x_1, x_2, ..., x_m))
$$

Linearity of expectation

Say we have X and Y RV's Z = (X, Y)


$$
\mathbb{E}[Z] = \mathbb{E}[X + Y] = \sum_{x,y}(x+y)f_{X,Y}(x,y) = \\ = \sum_{x,y}x*f_{X,Y}(x,y) + \sum_{x,y}y*f_{X,Y}(x,y) = \mathbb{E}[X] + \mathbb{E}[Y]
$$

## Law of the lazy statistician (LOLS)

Let's say we have a random variable X and a function $f : \mathbb{R} \to \mathbb{R}$

Let Y = f(X)


$$
\mathbb{E}[Y] = \sum_yyf_Y(y) = \mathbb{E}[f(X)] = \sum_x f(x) f_X(x)
$$

$f_Y(y)$ might be harder to find than $f_X(x)$

## Variance


$$
\mathbb{V}[X] = \mathbb{E}[(X - \mathbb{E}[X])^2] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2
$$
variance is the expectation of the squared deviation from the mean

Mean absolute deviation


$$
\mathbb{E}[|X - \mathbb{E}[X]|]
$$

<u>If X1, X2, ..., Xn are independent then the variance of the sum is the sum of the variances</u>

## Covariance 

$$
Cov(X,Y) = \mathbb{E}((X - \mathbb{E}[X])(Y - \mathbb{E}[Y])) = \\
= \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]
$$
how related are X and Y, how strong the linear relationship is
Correlation is normalized covariance
$$
\rho_{X,Y} = \frac{Cov(X,Y)}{\sqrt{\mathbb{V}[X] \mathbb{V}[Y]}} \in [-1, 1]
$$


If X and Y are RVs then
$$
V(X+Y) = V(X) + V(Y) + 2Cov(X,Y)
$$
If X and Y are independent then
$$
V(X+Y) = V(X) + V(Y)
$$

## Mean and variance of some important distributions

| Distribution | Mean | Variance |
| :--- | :--- | :--- |
| Point mass at $a$ | $a$ | $0$ |
| Bernoulli($p$) | $p$ | $p(1-p)$ |
| Binomial($n,p$) | $np$ | $np(1-p)$ |
| Geometric($p$) | $1/p$ | $(1-p)/p^2$ |
| Poisson($\lambda$) | $\lambda$ | $\lambda$ |
| Uniform($a,b$) | $(a+b)/2$ | $(b-a)^2/12$ |
| Normal($\mu, \sigma^2$) | $\mu$ | $\sigma^2$ |
| Exponential($\beta$) | $\beta$ | $\beta^2$ |
| Gamma($\alpha, \beta$) | $\alpha\beta$ | $\alpha\beta^2$ |
| Beta($\alpha, \beta$) | $\alpha/(\alpha+\beta)$ | $\alpha\beta/((\alpha+\beta)^2(\alpha+\beta+1))$ |
| $t_\nu$ | $0$ (if $\nu > 1$) | $\nu/(\nu-2)$ (if $\nu > 2$) |
| $\chi^2_p$ | $p$ | $2p$ |
| Multinomial($n,p$) | $np$ | <a href="https://www.youtube.com/watch?v=KSPxHniCtmw">skibidi</a> |
| Multivariate Normal($\mu, \Sigma$) | $\mu$ | $\Sigma$ |

## Tower rule
$$
\mathbb{E}[\mathbb{E}[X|Y]] = \mathbb{E}[X]
$$

## Cauchy distribution


$$
f_X(x) =\frac{1}{\pi(1+x^2)}
$$
It's mean does not exist because Cauchy has thic tails and hence extreme observations are common

## Moments of random variables 

The k-th moment of a random variable X is defined as
$$
\mu'_k = \mathbb{E}[X^k]
$$

The k-th central moment of a random variable X is defined as
$$
\mu_k = \mathbb{E}[(X - \mathbb{E}[X])^k]
$$

Moment generating function (MGF)


$$
M_X(t) = \mathbb{E}[e^{tX}] = \sum_x e^{tx} f_X(x)
$$

We obtain the moments of X by differentiating MGF and evaluating at t=0
$$
\mu'_k = M_X^{(k)}(0)
$$

Notable moments
- 1st moment = expectation
- 2nd central moment = variance
- 3rd central moment = skewness - asymmetry of the distribution
- 4th central moment = kurtosis - "tailedness" of the distribution, measure of the heaviness of the tails, e.g.
  - normal distribution kurtosis = 3
  - Cauchy distribution kurtosis = infinity
  - exponential distribution kurtosis = 9
  - the higher the kurtosis, the heavier the tails -> more prone to outliers and slower convergence to the mean

If kth moment exists and if j<k then the jth moment also exists

--- 
If X1, ..., Xn are random variables then we define the sample mean and sample variance as:


$$
\bar{X}_n = \frac{1}{n} \sum_{i=1}^{n} X_i \\
S_n^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar{X}_n)^2
$$

If X1, ..., Xn are iid with mean mu and variance sigma^2 then
$$
\mathbb{E}[\bar{X}_n] = \mu \\ 
\mathbb{V}[\bar{X}_n] = \frac{\sigma^2}{n} \\ 
\mathbb{E}[S_n^2] = \sigma^2
$$

# Lecture 4 

## Markov inequality

X - non negative RV, 
$$
P(X \ge \epsilon) \le \frac{\mathbb{E}[X]}{\epsilon} \\
\epsilon > 0
$$

## Chebyshev inequality

$$
P(|X - E[X]| \ge \epsilon) \le \frac{V[X]}{\epsilon^2} \\
$$
- requires finite variance
- polynomial decay


## Hoeffding inequality
Let X1, X2, ..., Xn be independent RVs such that $a_i \le X_i \le b_i$ almost surely. Let $\bar{X}_n = \frac{1}{n} \sum_{i=1}^{n} X_i$ be the sample mean. Then for any $\epsilon > 0$ it holds that

$$
P(|\bar{X}_n - \mathbb{E}[\bar{X}_n]| \ge \epsilon) \le 2 \exp\left(\frac{-2n\epsilon^2}{\sum_{i=1}^{n}(b_i - a_i)^2}\right)
$$

## confidence intervals:

Set the RHS equal to $\delta$ and solve for $\varepsilon$:

- Hoeffding:
$$
2 e^{-2n\varepsilon^2/(b-a)^2} = \delta
\Rightarrow
\varepsilon = \frac{b-a}{\sqrt{2n}} \sqrt{\ln\!\left(\frac{2}{\delta}\right)}.
$$

- Chebyshev:
$$
\frac{\sigma^2}{n\varepsilon^2} = \delta
\Rightarrow
\varepsilon = \sqrt{\frac{\sigma^2}{n\delta}}.
$$

$$

$$

## Sub-Gaussian and Sub-Exponential random variables

Let X be RV. We call it sub-Gaussian with parameter $\lambda$ if 
$$
E[e^{t(X - E[X])}] \le e^{\frac{\lambda^2 t^2}{2}} \text{ for all } t \in \mathbb{R}
$$
We call it sub-Exponential with parameters $(\nu, b)$ if
$$
E[e^{t(X - E[X])}] \le e^{\frac{\nu^2 t^2}{2}} \text{ for } |t| < \frac{1}{b}
$$
- here we bound the moment generating function 
- SG RVs have tails that decay at least as fast as Gaussian tails
- SE tail decays slower than Gaussian but still exponentially
- every SG is SE but not vice versa
- if X is SG then X^2 is SE
- bounded RVs are sub-Gaussian
- sum of SG RVs is SG
 

## Types of convergence of random variables

- convergence in probability
$$
X_n \xrightarrow{P} X \text{ if for any } \epsilon > 0 \quad P(|X_n - X| \ge \epsilon) \to 0 \text{ as } n \to \infty
$$
- convergence almost surely
$$
X_n \xrightarrow{a.s.} X \text{ if } P(\lim_{n \rightarrow \infty}X_n = X) = 1
$$
  - strongest form of convergence
  - Xn converges to X for almost every outcome omega in the sample space 
- convergencce in distribution
$$
X_n \xrightarrow{d} X \text{ if } F_{X_n}(x) \to F_X(x) \text{ for all points } x \text{ where } F_X \text{ is continuous}
$$
  - sequence of CDFs approaches the limit's CDF (the shape becomes the same)
- convergence in Lp
$$
\lim_{n \to \infty} \mathbb{E}[|X_n - X|^p] = 0
$$

Hierarchy of implications:
- almost surely => probability => distribution
- Lp => probability

## Weak law of large numbers (WLLN)

Let X1, X2, ..., Xn be iid RVs with mean mu and variance sigma^2 < infinity. Let $\bar{X}_n = \frac{1}{n} \sum_{i=1}^{n} X_i$ be the sample mean. Then for any $\epsilon > 0$ it holds that

$$
\bar{X}_n \xrightarrow{P} \mu \text{ as } n \to \infty \\
\lim_{n \to \infty} P(|\bar{X}_n - \mu| \ge \epsilon) = 0
$$
- requires only finite variance

## Strong law of large numbers

Let X1, X2, ..., Xn be iid RVs with mean mu. Let $\bar{X}_n = \frac{1}{n} \sum_{i=1}^{n} X_i$ be the sample mean. Then it holds that
$$
\bar{X}_n \xrightarrow{a.s.} \mu \text{ as } n \to \infty \\
$$
- requires finite mean (first moment)

## Central limit theorem (CLT)
Let X1, X2, ..., Xn be iid RVs with mean mu and variance sigma^2 < infinity. Let $\bar{X}_n = \frac{1}{n} \sum_{i=1}^{n} X_i$ be the sample mean. Then it holds that
$$
Z_n = \frac{\bar{X}_n - E[\bar{X}_n]}{\sqrt{\text{Var}(\bar{X}_n)}} \xrightarrow{d} N(0,1) \text{ as } n \to \infty
$$

# Lesson 2


# Lecture 5 - Estimation

Bias 
$$
Bias(\hat{\theta}) = \mathbb{E}[\hat{\theta}] - \theta
$$

MSE 
$$
MSE = \mathbb{E}[(\hat{\theta} - \theta)^2] = V[\hat{\theta}] + Bias(\hat{\theta})^2
$$

## DKW Inequality
Let X1, X2, ..., Xn be iid RVs with CDF F. Let $F_n$ be the empirical CDF. Then for any $\epsilon > 0$ it holds that
$$
P(\sup_x |F_n(x) - \hat{F}(x)| > \epsilon) \le 2e^{-2n\epsilon^2}
$$
A non-parametric 1-alpha confidence band for F
$$
L(x) = \hat{F}(x) - \epsilon \\
U(x) = \hat{F}(x) + \epsilon \\
\text{ where } \epsilon = \sqrt{\frac{1}{2n} \ln\left(\frac{2}{\alpha}\right)}
$$

# Lecture 6 - Random variable generation

## Congruential generator 

Parameters:
- a - multiplier
- b - increment
- m - modulus

$$
D(x) = (ax + b) \mod m \\
$$

## Hull-Dobell theorem
Congruential generator (a, b, M) has period M iff:
- gcd(b,M) = 1
- p divides a-1 for every prime p that divides M
- 4 divides a-1 if 4 divides M

Examples of (a,b,M):
- (1103515245,12345,2**32)
- (29,12345,2**32)


## Accept-Reject sampler
To sample from a distribution with PDF f(x):
1. Choose a proposal distribution with PDF g(x) such that f(x) <= c*g(x) for some c > 0
2. Repeat:
3. Sample Y from g(x)
4. Sample U from Uniform(0,1)
5. If U <= f(Y)/(c*g(Y)), return Y; else, go back to step 3
6. The accepted samples follow the distribution with PDF f(x)


## Bax-Muller 
To generate standard normal RVs:
1. Generate U1, U2 ~ Uniform(0,1)
2. Compute:
$$
Z_0 = \sqrt{-2 \ln(U_1)} \cos(2\pi U_2) \\
Z_1 = \sqrt{-2 \ln(U_1)} \sin(2\pi U_2)
$$
3. Z0 and Z1 are independent standard normal RVs

## Inverse transform sampling

**Goal:** Generate random samples from a target distribution $X$ using a source of uniform random numbers $U \sim \text{Unif}(0,1)$.

**Prerequisites:**
1. You must know the Cumulative Distribution Function (CDF), $F(x)$.
2. You must be able to calculate the inverse function, $F^{-1}(u)$.

## The Algorithm
1. **Generate** a random number $u$ from the uniform distribution $[0, 1]$.
2. **Compute** $x = F^{-1}(u)$.
3. **Result:** The value $x$ is a random draw from the distribution defined by $F$.

## Mathematical Proof
Let $U \sim \text{Unif}(0,1)$. We define $X = F^{-1}(U)$.
We verify the CDF of $X$:

$$
\begin{aligned}
P(X \le x) &= P(F^{-1}(U) \le x) \\
           &= P(U \le F(x)) \quad \text{(Applying } F \text{ to both sides)} \\
           &= F(x) \quad \text{(Property of Uniform distribution)}
\end{aligned}
$$

**Conclusion:** The variable $X$ has the CDF $F(x)$, meaning it follows the desired distribution.

## Example: Exponential Distribution
* **PDF:** $f(x) = \lambda e^{-\lambda x}$
* **CDF:** $F(x) = 1 - e^{-\lambda x}$
* **Inverse Step:**
  Let $u = 1 - e^{-\lambda x}$
  $$e^{-\lambda x} = 1 - u$$
  $$-\lambda x = \ln(1 - u)$$
  $$x = -\frac{1}{\lambda} \ln(1 - u)$$
* **Sampling Formula:** Generate $u$, then compute $x = -\frac{\ln(1-u)}{\lambda}$.


# Other notes

## Train-Validation-Test splitting 

IF we want to achieve 60/15/25 split:
1. First get 40% of the data as a 'temp' set and 60% as train set
2. Then split the 'temp' set into validation and test sets according to the formula
$$
test\_size = \frac{P_{test}}{P_{test} + P_{val}} 
$$


## Bennett's inequality
Let X1, X2, ..., Xn be independent, centered (mean 0) sub-Exponential RVs with parameters (nu_i, b_i). Let S_n = sum Xi. Then for any t > 0 it holds that
$$
P(S_n \ge t) \le \exp\left(-\frac{n\nu_n^2}{b_n^2} h\left(\frac{b_n t}{n \nu_n^2}\right)\right)
$$
where
$$
\nu_n^2 = \frac{1}{n} \sum_{i=1}^{n} \nu_i^2, \quad b_n = \max_{i} b_i, \quad h(u) = (1+u)\ln(1+u) - u
$$

Bernstein's inequality is a simpler version of Bennett's inequality

$$
P(S_n \ge t) \le \exp\left(-\frac{t^2/2}{n\nu_n^2 + b_n t/3}\right)
$$
Epsilon confidence interval:
$$
\varepsilon = \sqrt{\frac{2\sigma^2}{n} \ln\left(\frac{2}{\delta}\right)} + \frac{M}{3n} \ln\left(\frac{2}{\delta}\right)
$$
sigma^2 - average of variances of Xi
M = maximum possible range/bound of Xi
delta - confidence level (e.g. 0.01)

## Exam 2022 concentration of measure

## 1. Theoretical Background

Concentration of measure defines how fast a random variable (like an empirical mean) converges to its true expected value as the sample size $n$ grows.

### Exponential Concentration (Strong)
The probability of a deviation drops extremely fast (exponentially) as $n$ increases.
$$P(|Z - \mathbb{E}[Z]| \geq \epsilon) \leq C_1 e^{-C_2 n \epsilon^2}$$
This requires the underlying data to have **"light tails"** (extreme values are very rare).
* **Sub-Gaussian:** Tails decay like a Gaussian ($e^{-x^2}$). Examples: Normal distribution, Bounded variables (Bernoulli, Uniform).
* **Sub-Exponential:** Tails decay like an Exponential ($e^{-|x|}$). Examples: Exponential distribution, Chi-squared.

### Polynomial Concentration (Weak)
The probability drops much slower (polynomially), usually driven by **Chebyshev’s Inequality**.
$$P(|Z - \mathbb{E}[Z]| \geq \epsilon) \leq \frac{\text{Var}(Z)}{\epsilon^2} \propto \frac{1}{n \epsilon^2}$$
This only requires **Finite Variance**. Extreme values are possible, so we cannot guarantee the tight exponential bound.

---

## Part 1: Exponential Concentration
**Correct Answers:** `[1, 2, 5, 9, 10]`

These variables have "light tails" or are bounded, allowing for strong bounds like Hoeffding's or Bernstein's inequalities.

* **1. The empirical mean of i.i.d. sub-Gaussian random variables**
    * **Why:** By definition, sums of independent sub-Gaussian variables are sub-Gaussian. We can use **Hoeffding's Inequality**.
* **2. The empirical mean of i.i.d. sub-Exponential random variables**
    * **Why:** Sums of sub-Exponentials are sub-Exponential. We can use **Bernstein's Inequality**, which gives an exponential bound (specifically a mix of $e^{-n\epsilon^2}$ for small deviations and $e^{-n\epsilon}$ for large ones).
* **5. The empirical variance of i.i.d. sub-Gaussian random variables**
    * **Why:** The empirical variance depends on the average of $X^2$. If $X$ is sub-Gaussian (tail $e^{-x^2}$), then $Y = X^2$ is **sub-Exponential** (tail $e^{-y}$). Since we are taking the mean of sub-Exponential variables ($X^2$), this falls back to Case 2.
* **9. The empirical mean of i.i.d. deterministic random variables**
    * **Why:** A deterministic variable is a constant. The variance is 0. It equals its mean with probability 1 (infinite concentration).
* **10. The empirical tenth moment of i.i.d. Bernoulli random variables**
    * **Why:** A Bernoulli variable $B$ takes values $\{0, 1\}$. $B^{10}$ also takes values $\{0, 1\}$. All bounded variables are **sub-Gaussian**, so their mean concentrates exponentially (Hoeffding).

---

## Part 2: Weak Concentration
**Correct Answers:** `[3, 6, 7, 8]`

These variables have tails that are too "heavy" for exponential bounds but still have finite variance, satisfying Chebyshev's inequality.

* **3. The empirical mean of i.i.d. random variables with finite variance**
    * **Why:** We only know the variance is finite. We don't know if higher moments exist or if tails decay exponentially. We can strictly only apply **Chebyshev's Inequality**.
* **6. The empirical variance of i.i.d. sub-Exponential random variables**
    * **Why:** Empirical variance relies on $X^2$. If $X$ is sub-Exponential ($e^{-|x|}$), then $Y = X^2$ has a tail that behaves like $e^{-\sqrt{y}}$. This is heavier than a standard exponential tail ($e^{-y}$). It does *not* satisfy the sub-Exponential definition for Bernstein's bound, but since all moments exist, the variance is finite.
* **7. The empirical third moment of i.i.d. sub-Gaussian random variables**
    * **Why:** We look at $X^3$. If $X$ is sub-Gaussian ($e^{-x^2}$), then $Z = X^3$ has tails like $e^{-z^{2/3}}$. This decay is slower than exponential ($e^{-z}$), so no Hoeffding/Bernstein. However, finite moments exist.
* **8. The empirical fourth moment of i.i.d. sub-Gaussian random variables**
    * **Why:** We look at $X^4$. If $X$ is sub-Gaussian ($e^{-x^2}$), then $W = X^4$ has tails like $e^{-\sqrt{w}}$. This is significantly slower than exponential.

### Excluded Case
* **4. The empirical variance of i.i.d. random variables with finite variance**
    * **Why:** To compute the *concentration* of the variance, we need the **variance of the sample variance**, which depends on the **fourth moment** ($E[X^4]$). The problem only guarantees finite variance ($E[X^2] < \infty$), not finite fourth moment.


---
Additional notes at:
https://bluej1.github.io/IntroDSExamMaterial/

solutions to exercises:
https://github.com/sajad13901/Statistics_Wasserman/tree/main

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>