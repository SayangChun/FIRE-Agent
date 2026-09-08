# FIRE Agent — ChatGPT Knowledge Files Guide

This document describes the knowledge files to upload to your ChatGPT Custom GPT. Upload each file listed below via the **Knowledge** section in the GPT Editor.

---

## Upload Instructions

1. Open your Custom GPT at [chat.openai.com/gpts](https://chat.openai.com/gpts)
2. Go to the **Configure** tab
3. Scroll to **Knowledge** → click **"Upload files"**
4. Upload each file one at a time
5. The GPT will reference these files when relevant during conversations

> **Limits:** Max 20 files, each under 10 MB. Supported formats: `.txt`, `.pdf`, `.csv`, `.docx`, `.md`

---

## Knowledge File List

### File 1: `fire_formulas.txt`
**Purpose:** Core FIRE calculation formulas and constants

**Contents:**
```
FIRE CALCULATION FORMULAS

1. FIRE Number
   FIRE Number = Annual Retirement Expenses / Withdrawal Rate
   Example: $40,000 / 0.04 = $1,000,000

2. Withdrawal Rates (sensitivity range)
   Conservative: 2.5% — safe for 50+ year retirements
   Moderate:     3.0% — balanced safety margin
   Standard:     3.5% — common target
   Classic:      4.0% — traditional Trinity Study rate
   Aggressive:   4.5% — higher risk
   Very Aggressive: 5.0% — significant depletion risk

3. FIRE Progress
   Progress % = (Current Investable Assets / FIRE Number) × 100
   Note: Primary residence excluded from investable assets

4. Savings Rate
   Savings Rate = (Annual Income - Annual Expenses) / Annual Income × 100

5. Years to FIRE (compound growth)
   N = -ln(1 - (FIRE Number × r) / (Savings × (1 + r))) / ln(1 + r)
   Where r = expected annual real return rate

6. Monte Carlo Parameters
   - Default iterations: 10,000
   - Random seed: 42 (reproducible)
   - Annual return: normal distribution, mean = user input, std = 15%
   - Inflation: normal distribution, mean = user input, std = 2%

7. Savings Rate Impact on Years to FIRE
   | Savings Rate | Years to FIRE (7% real return) |
   |-------------|-------------------------------|
   | 10%         | ~51 years                     |
   | 20%         | ~37 years                     |
   | 30%         | ~28 years                     |
   | 40%         | ~22 years                     |
   | 50%         | ~17 years                     |
   | 60%         | ~12.5 years                   |
   | 70%         | ~8.5 years                    |
   | 80%         | ~5.5 years                    |
```

---

### File 2: `risk_framework.txt`
**Purpose:** Complete risk analysis framework with 8 risk categories

**Contents:**
```
FIRE RISK ANALYSIS FRAMEWORK

1. SEQUENCE OF RETURNS RISK
   Severity: HIGH
   Description: Poor returns in early retirement years can permanently deplete portfolio
   Mitigation: 
   - 2-3 year cash buffer in high-yield savings
   - Guardrails withdrawal strategy (adjust spending based on portfolio performance)
   - Partial flexibility to reduce spending in down markets

2. INFLATION RISK
   Severity: MEDIUM-HIGH
   Description: Purchasing power erodes over time; expenses may outpace assumptions
   Mitigation:
   - Use real (inflation-adjusted) return rates
   - Include inflation in all projections (default 2.5-3%)
   - Own inflation-resistant assets (TIPS, I-Bonds, real estate, equities)

3. LONGEVITY RISK
   Severity: MEDIUM
   Description: Living longer than expected means portfolio must last longer
   Mitigation:
   - Plan for age 95+ (conservative)
   - Consider annuity allocation for base expenses
   - Maintain some growth exposure indefinitely

4. CONCENTRATION RISK
   Severity: VARIABLE
   Description: Over-allocation to single asset, sector, or geography
   Mitigation:
   - Diversify across asset classes (equities, bonds, real estate, alternatives)
   - Diversify geographically
   - Cap single-position exposure at 10-15%

5. LIQUIDITY RISK
   Severity: MEDIUM
   Description: Assets locked in non-liquid forms (real estate, private equity)
   Mitigation:
   - Maintain 1-2 years of expenses in liquid assets
   - Separate "FIRE portfolio" from illiquid investments
   - Establish credit lines as emergency backup

6. DEBT RISK
   Severity: VARIABLE
   Description: High-interest debt erodes savings rate and portfolio growth
   Mitigation:
   - Eliminate high-interest debt before FIRE
   - Model debt payoff into FIRE timeline
   - Low-interest mortgage may be acceptable if LTV < 50%

7. INCOME RISK
   Severity: MEDIUM-HIGH
   Description: Job loss, career disruption, or reduced earning capacity before FIRE
   Mitigation:
   - Build 6-12 month emergency fund
   - Diversify income sources (side hustles, rental income)
   - Maintain marketable skills

8. MEDICAL / EMERGENCY EXPENSE RISK
   Severity: HIGH (especially in countries without universal healthcare)
   Description: Unexpected medical costs can devastate portfolio
   Mitigation:
   - Factor healthcare costs into retirement budget
   - Maintain adequate insurance coverage
   - Build dedicated emergency/medical fund
```

---

### File 3: `scenario_templates.txt`
**Purpose:** Parameter templates for Conservative/Base/Optimistic scenarios

**Contents:**
```
SCENARIO ANALYSIS TEMPLATES

CONSERVATIVE SCENARIO
  Real return rate:     3.0%
  Inflation rate:       3.5%
  Withdrawal rate:      3.5%
  Savings growth:       2.0% per year
  Expense growth:       3.5% per year
  Use case: Stress-testing under adverse conditions

BASE SCENARIO
  Real return rate:     5.0%
  Inflation rate:       2.5%
  Withdrawal rate:      4.0%
  Savings growth:       3.0% per year
  Expense growth:       2.5% per year
  Use case: Most likely outcome based on historical averages

OPTIMISTIC SCENARIO
  Real return rate:     7.0%
  Inflation rate:       2.0%
  Withdrawal rate:      4.5%
  Savings growth:       5.0% per year
  Expense growth:       2.0% per year
  Use case: Best-case with favorable markets and career growth

CUSTOM SCENARIO
  All parameters user-defined
  Use case: Testing specific life changes (job change, relocation, etc.)

MONTE CARLO PARAMETERS
  Iterations:          10,000 (default, adjustable)
  Random seed:         42
  Annual return:       Normal distribution(user_mean, user_std)
  Inflation:           Normal分布(user_mean, 2.0%)
  Success threshold:   Portfolio balance > $0 at age 95
  Output percentiles:  10th, 25th, 50th (median), 75th, 90th
```

---

### File 4: `fire_types.txt`
**Purpose:** FIRE type classification definitions and criteria

**Contents:**
```
FIRE TYPE CLASSIFICATION

LEAN FIRE
  Retirement expenses: < 75% of median lifestyle
  Annual budget:       Typically $25,000-$40,000 (US single)
  Characteristics:    Minimalist lifestyle, travel-focused, geographic arbitrage
  Risk:               Less buffer for unexpected expenses
  Confidence:         High if expenses are genuinely low and sustainable

REGULAR FIRE (also called "Modest FIRE")
  Retirement expenses: 75-125% of current lifestyle
  Annual budget:       Typically $40,000-$80,000 (US)
  Characteristics:    Maintain current lifestyle, no major changes
  Risk:               Standard — moderate buffer
  Confidence:         Highest confidence level for most people

COAST FIRE
  Current assets:      Enough that compound growth alone reaches FIRE number
  Required savings:    $0 (just cover current expenses)
  Characteristics:    Work covers living expenses only; no additional saving needed
  Risk:               Depends on timeline and return assumptions
  Confidence:         High if coast number is clearly reached

BARISTA FIRE
  Retirement from:     Full-time corporate work
  Income source:       Part-time, freelance, or passion-project work
  Coverage:            Partial expenses covered by part-time income
  Risk:               Income uncertainty in "retirement" phase
  Confidence:         Medium — depends on part-time income reliability

FAT FIRE
  Retirement expenses: > 125% of median lifestyle
  Annual budget:       Typically $100,000+ (US)
  Characteristics:    Luxury travel, premium healthcare, generous giving
  Risk:               Higher portfolio requirement; sequence risk increases
  Confidence:         Lower — requires substantial assets or high savings rate

CLASSIFICATION RULES
  1. Compare annual retirement expenses to current expenses
  2. Check if coast number is reached (Coast FIRE test)
  3. Assess part-time income plans (Barista FIRE test)
  4. Classify based on expense level relative to median
  5. If data insufficient, state: "Unable to classify — need [specific data]"
```

---

### File 5: `monte_carlo_method.txt`
**Purpose:** Monte Carlo simulation methodology and interpretation guide

**Contents:**
```
MONTE CARLO SIMULATION METHODOLOGY

PURPOSE
  Model the range of possible outcomes for a FIRE plan by randomly
  sampling from probability distributions of key variables.

PARAMETERS
  Default iterations:     10,000
  Random seed:            42 (fixed for reproducibility)
  Variables sampled:
    - Annual investment return:  Normal distribution (mean, std dev)
    - Annual inflation:          Normal distribution (mean, std dev)
    - Annual expenses:           Optional variation (±5% default)
    - Annual income growth:      Optional variation

SUCCESS CRITERION
  Portfolio balance > $0 at target end age (default: age 95)
  Secondary: Portfolio balance > $0 at age 85, 90, 95, 100

OUTPUT INTERPRETATION
  Success Rate:        % of simulations where portfolio survives to end age
  Median Outcome:      50th percentile portfolio balance at end age
  10th Percentile:     Worst-case (90% of outcomes are better)
  90th Percentile:     Best-case (90% of outcomes are worse)
  Failure Point Age:   Average age when portfolio depletes (failed simulations only)

SUCCESS RATE BENCHMARKS
  > 95%:   Very strong plan — high confidence
  85-95%:  Strong plan — standard target
  70-85%:  Moderate plan — consider adjustments
  50-70%:  Weak plan — significant risk of failure
  < 50%:   High risk — fundamental changes needed

INTERPRETATION RULES
  1. Never present Monte Carlo as certainty — it's probability modeling
  2. Always show the distribution, not just the success rate
  3. Highlight the 10th percentile as the "stress test" outcome
  4. Explain that past returns do not guarantee future results
  5. If success rate < 85%, suggest specific adjustments

PYTHON IMPLEMENTATION NOTES
  Use numpy for random sampling
  Use fixed seed: np.random.seed(42)
  Generate returns: np.random.normal(mean_return, std_return, iterations)
  Track portfolio balance year-by-year across all iterations
  Calculate percentiles from final balances
```

---

## Creating These Files

To create the actual upload files:

1. Copy the contents of each section above into a new `.txt` file
2. Name them exactly as specified: `fire_formulas.txt`, `risk_framework.txt`, etc.
3. Keep formatting clean — the GPT will read them as plain text references

Alternatively, if you prefer `.md` format, the GPT will still read them — just change the extension.

---

## File Maintenance

- **Update frequency:** Re-upload files when you modify formulas or add new risk categories
- **Versioning:** Include a version date at the top of each file
- **Size check:** Keep each file under 5 MB for fast reference
