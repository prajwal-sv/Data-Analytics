# Complete Statistics Revision Chart

> **Hypothesis-testing approach: Defendant's approach**
>
> Think of **H₀ as the defendant** (default/innocent claim) and **H₁ as the prosecution's claim**.  
> Assume H₀ is true, collect evidence, calculate the test statistic and p-value, then decide.
>
> - **p-value < α → Reject H₀**
> - **p-value ≥ α → Fail to reject H₀**
> - Usually **α = 0.05**
>
> **Do not say "accept H₀"; say "fail to reject H₀".**

---

## 1. Complete Statistics Chart

| Topic | Definition | Real-life example | Formula / Test statistic | Conditions to apply | Rule / Interpretation | Python command |
|---|---|---|---|---|---|---|
| **Bar chart – single** | Shows frequencies/values for categorical groups using separate bars. | Number of students in each department. | No statistical formula. | Categorical/discrete groups. | Compare heights of bars. | `plt.bar(categories, values)` |
| **Bar chart – grouped** | Compares multiple categories across groups. | Male vs female students across departments. | No statistical formula. | Categorical variable + grouping variable. | Compare bars within and between groups. | `sns.barplot(data=df, x='dept', y='score', hue='gender')` |
| **Pie chart** | Shows each category as a proportion of the whole. | Market share of different brands. | Angle = proportion × 360°. | Categories should form a meaningful whole. | Larger slice = larger proportion. | `plt.pie(values, labels=labels, autopct='%1.1f%%')` |
| **Histogram – single** | Displays distribution of one numerical variable using bins. | Distribution of student marks. | Frequency/density per bin. | Continuous/numerical data. | Shape can indicate normality, skewness and modality. | `plt.hist(x, bins=10)` |
| **Histogram – grouped** | Compares distributions of numerical data for groups. | Salary distributions for two departments. | Same as histogram. | Numerical variable + grouping variable. | Compare center, spread and shape. | `sns.histplot(data=df, x='salary', hue='dept')` |
| **Box plot – single** | Summarizes numerical data using median, quartiles and potential outliers. | Distribution of employee salaries. | `IQR = Q3 - Q1` | Numerical data. | Median = center; box = middle 50%; extreme points may be outliers. | `plt.boxplot(x)` |
| **Box plot – grouped** | Compares distributions between groups. | Exam scores for different classes. | `IQR = Q3 - Q1` | Numerical variable + categorical grouping variable. | Compare median, spread and outliers. | `sns.boxplot(data=df, x='class', y='score')` |
| **Line chart – single** | Shows change/trend in a variable over an ordered variable or time. | Monthly sales. | No special formula. | Ordered/time-series data. | Slope shows increase/decrease. | `plt.plot(x, y)` |
| **Line chart – grouped** | Shows trends for several groups. | Monthly sales of 3 products. | No special formula. | Ordered x-variable + groups. | Compare trends across groups. | `sns.lineplot(data=df, x='month', y='sales', hue='product')` |
| **Scatter plot – single** | Shows relationship between two numerical variables. | Advertising expenditure vs sales. | `r = Cov(X,Y)/(sX sY)` | Two numerical variables. | Upward = positive; downward = negative; no pattern = weak/no relationship. | `plt.scatter(x, y)` |
| **Scatter plot – grouped** | Scatter plot with observations separated by groups. | Height vs weight by gender. | Correlation can be calculated within groups. | Two numerical variables + categorical group. | Compare relationships between groups. | `sns.scatterplot(data=df, x='height', y='weight', hue='gender')` |
| **Mean** | Arithmetic average. | Average salary. | `x̄ = Σxi / n` | Numerical data. | Sensitive to outliers. | `np.mean(x)` |
| **Median** | Middle value after sorting. | Typical house price when extreme houses exist. | Middle observation. | Ordinal/numerical data. | More robust than mean. | `np.median(x)` |
| **Mode** | Most frequently occurring value/category. | Most common shoe size. | Value with maximum frequency. | Categorical or numerical data. | Useful for categorical data. | `stats.mode(x)` |
| **Range** | Difference between maximum and minimum. | Difference between highest and lowest salary. | `Range = max - min` | Numerical data. | Larger range = greater overall spread. | `np.ptp(x)` |
| **IQR** | Spread of the middle 50% of observations. | Comparing salary variability while ignoring extremes. | `IQR = Q3 - Q1` | Numerical data. | Larger IQR = more central spread. | `stats.iqr(x)` |
| **Standard deviation** | Measures typical distance from the mean. | Variation in production time. | `s = sqrt[Σ(xi-x̄)²/(n-1)]` | Numerical data. | Larger SD = greater variability. | `np.std(x, ddof=1)` |
| **Variance** | Average squared deviation from the mean. | Variability of investment returns. | `s² = Σ(xi-x̄)²/(n-1)` | Numerical data. | SD = √variance. | `np.var(x, ddof=1)` |
| **Skewness** | Measures asymmetry of a distribution. | Income distribution often has right skew. | `E[(X-μ)³] / σ³` | Numerical data. | >0: right skew; <0: left skew; 0: symmetric. | `stats.skew(x)` |
| **Kurtosis** | Measures tail heaviness/peakedness relative to a normal distribution. | Detecting extreme values in financial returns. | Based on fourth standardized moment. | Numerical data. | Positive excess kurtosis = heavier tails; negative = lighter tails. | `stats.kurtosis(x)` |
| **Proportion** | Fraction/percentage of observations possessing a characteristic. | Proportion of customers who renew. | `p̂ = x/n` | Binary/categorical outcome. | Multiply by 100 for percentage. | `p = x/n` |
| **Binomial distribution** | Distribution of successes in a fixed number of independent trials. | Number of defective products in 20 products. | `P(X=x) = C(n,x)p^x(1-p)^(n-x)` | Fixed n, binary outcome, independent trials, constant p. | X = number of successes. | `stats.binom.pmf(x, n, p)` |
| **Poisson distribution** | Distribution of number of events in a fixed interval at a constant average rate. | Number of calls received per minute. | `P(X=x) = e^(-λ) λ^x / x!` | Count data, independent events, constant rate. | Mean = variance = λ. | `stats.poisson.pmf(x, mu)` |
| **Normal distribution** | Continuous bell-shaped symmetric distribution. | Heights of adults approximately follow a normal distribution. | `Z = (X-μ)/σ` | Continuous variable; normality appropriate. | 68–95–99.7 rule approximately applies. | `stats.norm.pdf(x, loc=mu, scale=sigma)` |
| **Student's t distribution** | Distribution used for inference about a mean when population SD is unknown. | Testing average exam score with a small sample. | `t = (x̄-μ0)/(s/√n)` | Independent sample; approximately normal population for small n. | Heavier tails than normal; df = n−1. | `stats.t.cdf(...)`, `stats.t.ppf(...)` |
| **Central Limit Theorem** | For sufficiently large samples, the sampling distribution of the sample mean approaches normality. | Estimating average customer spending from samples. | `SE = σ/√n` | Independent/random observations; sufficiently large n or approximately normal population. | Larger n → smaller SE. | `np.mean(sample)` |
| **CI for mean, σ known** | Range of plausible values for population mean. | Estimate average delivery time. | `x̄ ± Zα/2 σ/√n` | Random sample; known σ or appropriate normal approximation. | More confidence → wider interval. | `stats.norm.interval(...)` |
| **CI for mean, σ unknown** | CI using sample SD. | Estimate average customer spending. | `x̄ ± tα/2,n−1 s/√n` | Independent observations; approximately normal for small samples. | Larger n → narrower interval. | `stats.t.interval(...)` |
| **Effect of Z, σ and n on CI** | Describes how confidence interval width changes. | Planning sample size for a survey. | `ME = Zσ/√n` | Same assumptions as CI. | Z↑ → wider; σ↑ → wider; n↑ → narrower. | `ME = z*sigma/np.sqrt(n)` |
| **Sample size for mean** | Determines n needed for a desired margin of error. | How many people should be surveyed? | `n = (Zσ/E)²` | σ known/estimated; desired margin E. | Z↑ → n↑; σ↑ → n↑; E↑ → n↓. | `np.ceil((z*sigma/E)**2)` |
| **1-sample Z test** | Tests a population mean when population SD is known. | Is average filling volume 500 ml? | `Z = (x̄-μ0)/(σ/√n)` | Known σ; random/independent sample; normality or sufficiently large n. | Reject H₀ if p < α. | `ztest(x, value=mu0)` |
| **1-sample t test** | Tests population mean when population SD is unknown. | Is average delivery time 30 minutes? | `t = (x̄-μ0)/(s/√n)` | Independent observations; normal population for small n. | Reject H₀ if p < α. | `stats.ttest_1samp(x, popmean=mu0)` |
| **2-sample t test** | Compares means of two independent populations. | Average sales of Store A vs Store B. | `t = (x̄1-x̄2)/SE` | Two independent groups; numerical outcome; approximately normal; Welch avoids equal-variance assumption. | Reject H₀: μ1=μ2 if p < α. | `stats.ttest_ind(x1, x2, equal_var=False)` |
| **Paired t test** | Compares means of paired/dependent observations. | Blood pressure before vs after treatment. | `t = d̄/(sd/√n)` | Same subjects/items measured twice; differences approximately normal. | Reject H₀: μd=0 if p < α. | `stats.ttest_rel(before, after)` |
| **One-way ANOVA** | Tests whether 3+ independent group means are equal. | Comparing marks among 4 teaching methods. | `F = MSbetween / MSwithin` | Independent groups; numerical outcome; approximate normality; homogeneous variances. | Reject H₀ if p < α; at least one mean differs. | `stats.f_oneway(g1, g2, g3)` |
| **Multi-way ANOVA** | Tests effects of two or more categorical factors and their interaction on a numerical outcome. | Effect of teaching method and gender on marks. | `F = MSfactor / MSerror` | Independent observations; numerical outcome; residual assumptions. | Check main effects and interaction. | `ols('score ~ C(method)*C(gender)', data=df).fit()` + `sm.stats.anova_lm(model, typ=2)` |
| **One-proportion test** | Tests whether a population proportion equals a specified value. | Is defect rate 5%? | `Z = (p̂-p0)/sqrt[p0(1-p0)/n]` | Binary outcome; sufficiently large expected successes/failures. | Reject H₀:p=p0 if p < α. | `proportions_ztest(count, nobs, value=p0)` |
| **Two-proportion test** | Tests whether two population proportions are equal. | Is conversion rate different between two websites? | `Z = (p̂1-p̂2)/sqrt[p̂(1-p̂)(1/n1+1/n2)]` | Two independent samples; binary outcome; adequate counts. | Reject H₀:p1=p2 if p < α. | `proportions_ztest([x1,x2], [n1,n2])` |
| **Chi-square association/independence** | Tests whether two categorical variables are associated. | Is gender associated with product preference? | `χ² = Σ(O-E)²/E` | Categorical variables; independent observations; expected frequencies sufficiently large. | Reject H₀ → variables are associated. | `stats.chi2_contingency(table)` |
| **Chi-square goodness of fit** | Tests whether observed categorical frequencies follow a specified distribution. | Are customers equally likely to choose 4 brands? | `χ² = Σ(O-E)²/E` | Categorical counts; independent observations; adequate expected frequencies. | Reject H₀ → observed distribution differs from expected. | `stats.chisquare(f_obs, f_exp)` |
| **One-sample Poisson rate test** | Tests whether one Poisson event rate equals a specified rate. | Is a call center receiving 10 calls/minute? | Based on Poisson count/rate likelihood. | Count events; independent events; constant rate; known exposure. | Reject H₀: λ=λ0 if p < α. | Use an exact Poisson/rate procedure. |
| **Two-sample Poisson rate test** | Compares event rates from two independent Poisson processes. | Compare accident rates at two factories. | H₀: λ1 = λ2 | Independent Poisson counts with known/recorded exposure times. | Reject H₀ → rates differ. | Use rate-ratio / Poisson regression methods. |
| **One-sample variance test** | Tests whether population variance equals a specified value. | Is machine output variance equal to specification? | `χ² = (n−1)s²/σ0²` | Population approximately normal. | Reject H₀: σ²=σ0² if p < α. | Calculate χ² statistic and use `stats.chi2` for p-value. |
| **Two-sample variance test** | Tests equality of two population variances. | Are production processes equally variable? | `F = s1²/s2²` | Independent samples; populations approximately normal for classical F test. | Reject H₀: σ1²=σ2² if p < α. | `stats.levene(x1, x2)` is generally more robust. |

---

# 2. Hypothesis Testing — Defendant's Approach

Think of a court case:

| Court idea | Statistics equivalent |
|---|---|
| Defendant is assumed innocent | Assume H₀ is true |
| Prosecution makes an accusation | H₁ is the research claim |
| Evidence is collected | Sample data |
| Strength of evidence | Test statistic / p-value |
| Very strong evidence against defendant | Small p-value |
| Convict defendant | Reject H₀ |
| Not enough evidence to convict | Fail to reject H₀ |

## Step 1 — State hypotheses

Example: testing whether average delivery time is 30 minutes:

`H₀: μ = 30`

`H₁: μ ≠ 30`

## Step 2 — Select significance level

Usually:

`α = 0.05`

## Step 3 — Calculate test statistic

For a one-sample t-test:

`t = (x̄ − μ0) / (s/√n)`

## Step 4 — Calculate p-value

The p-value asks:

> If H₀ were actually true, how unusual would my observed result be?

Small p-value = strong evidence against H₀.

## Step 5 — Decision

`p < α → Reject H₀`

`p ≥ α → Fail to reject H₀`

### Do NOT write:

> Accept H₀.

### Write:

> Fail to reject H₀.

Failure to find sufficient evidence against H₀ does not prove H₀ is true.

---

# 3. Direction of the Alternative Hypothesis

| Research question | H₀ | H₁ | Test |
|---|---|---|---|
| Is mean different from 50? | μ = 50 | μ ≠ 50 | Two-tailed |
| Is mean greater than 50? | μ ≤ 50 | μ > 50 | Right-tailed |
| Is mean less than 50? | μ ≥ 50 | μ < 50 | Left-tailed |
| Is defect proportion different from 5%? | p = 0.05 | p ≠ 0.05 | Two-tailed |
| Is defect proportion greater than 5%? | p ≤ 0.05 | p > 0.05 | Right-tailed |

---

# 4. Which Statistical Test Should I Use?

| Question | Number of groups | Variable type | Test |
|---|---:|---|---|
| Test one population mean, σ known | 1 | Numerical | **One-sample Z** |
| Test one population mean, σ unknown | 1 | Numerical | **One-sample t** |
| Compare two independent means | 2 | Numerical | **Two-sample t** |
| Compare before vs after for same people | 2 paired | Numerical | **Paired t** |
| Compare 3+ independent means | 3+ | Numerical | **One-way ANOVA** |
| Two or more categorical factors affect numerical outcome | 2+ factors | Numerical | **Multi-way ANOVA** |
| Test one population proportion | 1 | Binary | **One-proportion Z** |
| Compare two proportions | 2 | Binary | **Two-proportion Z** |
| Relationship between two categorical variables | 2 categorical variables | Categorical | **Chi-square independence** |
| Compare observed vs expected category frequencies | 1 categorical variable | Categorical | **Chi-square goodness of fit** |
| Test one Poisson event rate | 1 | Count/rate | **One-sample Poisson rate** |
| Compare two Poisson event rates | 2 | Count/rate | **Two-sample Poisson rate** |
| Test one population variance | 1 | Numerical | **Chi-square variance test** |
| Compare two population variances | 2 | Numerical | **F / variance test** |

---

# 5. Most Important Formulas

## Mean

`x̄ = Σxi / n`

## Sample variance

`s² = Σ(xi − x̄)² / (n − 1)`

## Sample standard deviation

`s = √s²`

## IQR

`IQR = Q3 − Q1`

## Z-score

`Z = (x − μ) / σ`

## Standard error of mean

Known σ:

`SE = σ / √n`

Unknown σ:

`SE = s / √n`

## Confidence interval

Known σ:

`x̄ ± Zα/2 × σ/√n`

Unknown σ:

`x̄ ± tα/2,n−1 × s/√n`

## Margin of error

`E = Zσ/√n`

## Required sample size

`n = (Zσ/E)²`

**Always round n upward.**

---

# 6. How Confidence Interval Size Changes

`E = Zσ/√n`

| Change | Effect on CI |
|---|---|
| Z increases | CI becomes wider |
| σ increases | CI becomes wider |
| n increases | CI becomes narrower |
| Margin of error E decreases | Need larger n |
| Confidence level increases | CI becomes wider |

For sample size:

`n = (Zσ/E)²`

Therefore:

- Z ↑ → n ↑
- σ ↑ → n ↑
- E ↑ → n ↓

---

# 7. ANOVA

For one-way ANOVA:

`H₀: μ1 = μ2 = μ3 = ... = μk`

`H₁: At least one population mean is different`

F statistic:

`F = MSbetween / MSwithin`

If:

`p < 0.05`

then:

> Reject H₀ → there is evidence that at least one group mean differs.

### Important

ANOVA does **not** tell you which groups differ.

If ANOVA is significant, use a post-hoc test such as Tukey HSD:

```python
from statsmodels.stats.multicomp import pairwise_tukeyhsd

pairwise_tukeyhsd(df['score'], df['group'])
```

---

# 8. Chi-Square Tests — Do Not Confuse Them

## Chi-square independence/association

Question:

> Are two categorical variables related?

Example: **Gender × Product Preference**

`H₀: Variables are independent`

`H₁: Variables are associated`

```python
from scipy.stats import chi2_contingency

chi2, p, dof, expected = chi2_contingency(table)
```

## Chi-square goodness of fit

Question:

> Does my observed distribution match an expected distribution?

Example:

Observed:

`[18, 22, 27, 33]`

Expected:

`[25, 25, 25, 25]`

`H₀: Observed distribution follows expected distribution`

`H₁: Observed distribution does not follow expected distribution`

```python
from scipy.stats import chisquare

chi2, p = chisquare(observed, expected)
```

---

# 9. Python Imports to Know

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats

import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.weightstats import ztest
```

## Descriptive statistics

```python
np.mean(x)
np.median(x)
stats.mode(x)
np.ptp(x)
stats.iqr(x)
np.var(x, ddof=1)
np.std(x, ddof=1)
stats.skew(x)
stats.kurtosis(x)
```

## Hypothesis tests

```python
stats.ttest_1samp(x, mu0)

stats.ttest_ind(x1, x2, equal_var=False)

stats.ttest_rel(before, after)

stats.f_oneway(group1, group2, group3)

proportions_ztest(count, nobs, value=p0)

proportions_ztest([success1, success2],
                  [n1, n2])
```

## Visualization

```python
plt.bar(x, y)

plt.pie(values, labels=labels, autopct='%1.1f%%')

plt.hist(x, bins=10)

plt.boxplot(x)

plt.plot(x, y)

plt.scatter(x, y)

sns.boxplot(data=df, x='group', y='value')

sns.histplot(data=df, x='value', hue='group')

sns.scatterplot(data=df, x='x', y='y', hue='group')
```

---

# 10. Universal Exam Answer Format

For **every hypothesis test**, use this order:

## 1. Hypotheses

`H₀: ...`

`H₁: ...`

## 2. Significance level

`α = 0.05`

## 3. Test statistic

Write the appropriate formula and calculate it.

## 4. P-value

Report:

`p = value`

## 5. Decision — Defendant approach

If:

`p < 0.05`

**Reject H₀.**

If:

`p ≥ 0.05`

**Fail to reject H₀.**

## 6. Conclusion in words

If significant:

> Since the p-value is less than 0.05, we reject H₀. There is sufficient statistical evidence to conclude that ______.

If not significant:

> Since the p-value is greater than or equal to 0.05, we fail to reject H₀. There is insufficient statistical evidence to conclude that ______.

---

# 11. 10-Second Memory Trick

**MEAN → Z/t**

**2 MEANS → t**

**3+ MEANS → ANOVA**

**1 PROPORTION → 1-proportion Z**

**2 PROPORTIONS → 2-proportion Z**

**2 CATEGORICAL VARIABLES → Chi-square association**

**OBSERVED vs EXPECTED → Chi-square GOF**

**COUNT/RATE → Poisson**

**1 VARIANCE → Chi-square**

**2 VARIANCES → F / variance test**

For every test:

`Assume H₀ → Calculate evidence → p-value → Decision`

### Final rule

`p < 0.05 → Reject H₀`

`p ≥ 0.05 → Fail to reject H₀`