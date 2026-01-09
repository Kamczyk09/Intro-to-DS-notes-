
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

## Covariance 

$$
Cov(X,Y) = \mathbb{E}((X - \mathbb{E}[X])(Y - \mathbb{E}[Y])) = \\
= \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]
$$
how related are X and Y

# Lecture 4 

markov inequality
chebyshev inequality
hoeffding inequality

# Lesson 2


# Lecture 5

# Lecture 6

Markov 

$$
P(X \ge \epsilon) \le \frac{\mathbb{E}[X]}{\epsilon} \\
\epsilon \text{ is a number } X \text{is an RV such that } \mathbb{E}[X] < \infty
$$

Chebyshev 
$$
\mathbb{P}(|X - E[X]| \ge \epsilon) \le \frac{V[X]}{n\epsilon} 

$$

Hoeffding
$$



$$

