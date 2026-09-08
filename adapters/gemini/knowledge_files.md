# FIRE Agent — Gemini Knowledge Files Guide

This document describes the knowledge files to upload to your Gemini Gem. Upload each file via the **Knowledge** section in the Gem editor.

---

## Upload Instructions

1. Go to [gemini.google.com/gems](https://gemini.google.com/gems)
2. Open your FIRE Agent Gem (or create a new one)
3. Under **Knowledge**, click **"Upload files"**
4. Upload each file
5. Save the Gem

> **Supported formats:** `.txt`, `.pdf`, `.csv`, `.docx`, `.md`

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
   Mitigation: 2-3 year cash buffer, guardrails withdrawal strategy, spending flexibility

2. INFLATION RISK
   Severity: MEDIUM-HIGH
   Description: Purchasing power erodes over time
   Mitigation: Use real return rates, include inflation in projections, own inflation-resistant assets

3. LONGEVITY RISK
   Severity: MEDIUM
   Description: Living longer than expected means portfolio must last longer
   Mitigation: Plan for age 95+, consider annuities, maintain growth exposure

4. CONCENTRATION RISK
   Severity: VARIABLE
   Description: Over-allocation to single asset, sector, or geography
   Mitigation: Diversify across asset classes and geographies, cap single positions at 10-15%

5. LIQUIDITY RISK
   Severity: MEDIUM
   Description: Assets locked in non-liquid forms
   Mitigation: Maintain 1-2 years expenses in liquid assets, separate FIRE portfolio from illiquid investments

6. DEBT RISK
   Severity: VARIABLE
   Description: High-interest debt erodes savings rate
   Mitigation: Eliminate high-interest debt before FIRE, model debt payoff into timeline

7. INCOME RISK
   Severity: MEDIUM-HIGH
   Description: Job loss or career disruption before FIRE
   Mitigation: Build 6-12 month emergency fund, diversify income sources

8. MEDICAL / EMERGENCY EXPENSE RISK
   Severity: HIGH
   Description: Unexpected medical costs can devastate portfolio
   Mitigation: Factor healthcare into budget, maintain insurance, build emergency fund
```

---

### File 3: `scenario_templates.txt`
**Purpose:** Parameter templates for scenario analysis

**Contents:**
```
SCENARIO ANALYSIS TEMPLATES

CONSERVATIVE SCENARIO
  Real return: 3.0% | Inflation: 3.5% | Withdrawal: 3.5%
  Savings growth: 2.0%/yr | Expense growth: 3.5%/yr

BASE SCENARIO
  Real return: 5.0% | Inflation: 2.5% | Withdrawal: 4.0%
  Savings growth: 3.0%/yr | Expense growth: 2.5%/yr

OPTIMISTIC SCENARIO
  Real return: 7.0% | Inflation: 2.0% | Withdrawal: 4.5%
  Savings growth: 5.0%/yr | Expense growth: 2.0%/yr

MONTE CARLO PARAMETERS
  Iterations: 10,000 | Seed: 42
  Return: Normal(user_mean, user_std)
  Inflation: Normal(user_mean, 2.0%)
  Success: Portfolio > $0 at age 95
  Output: 10th, 25th, 50th, 75th, 90th percentiles
```

---

### File 4: `fire_types.txt`
**Purpose:** FIRE type classification definitions

**Contents:**
```
FIRE TYPE CLASSIFICATION

LEAN FIRE
  Expenses: < 75% of median | Budget: $25K-$40K/yr (US single)
  Characteristics: Minimalist, travel-focused, geographic arbitrage

REGULAR FIRE
  Expenses: 75-125% of median | Budget: $40K-$80K/yr (US)
  Characteristics: Maintain current lifestyle

COAST FIRE
  Current assets: Compound growth alone reaches FIRE number
  Required savings: $0 (just cover living expenses)

BARISTA FIRE
  Income source: Part-time or freelance work covers partial expenses
  Risk: Income uncertainty in "retirement" phase

FAT FIRE
  Expenses: > 125% of median | Budget: $100K+/yr (US)
  Characteristics: Luxury travel, premium healthcare, generous giving
```

---

### File 5: `monte_carlo_method.txt`
**Purpose:** Monte Carlo simulation methodology

**Contents:**
```
MONTE CARLO SIMULATION METHODOLOGY

PURPOSE: Model range of outcomes by randomly sampling key variables

PARAMETERS
  Iterations: 10,000 | Seed: 42
  Sampled: Annual return, inflation, expenses (optional variation)

SUCCESS CRITERION: Portfolio > $0 at target end age (default: 95)

OUTPUT INTERPRETATION
  Success Rate:     % of simulations surviving to end age
  Median Outcome:   50th percentile final balance
  10th Percentile:  Worst realistic case
  90th Percentile:  Best realistic case

BENCHMARKS
  > 95%:  Very strong | 85-95%: Strong | 70-85%: Moderate
  50-70%: Weak | < 50%: High risk

RULES
  1. Never present as certainty — it's probability modeling
  2. Show distribution, not just success rate
  3. Highlight 10th percentile as stress test
  4. Past returns do not guarantee future results
  5. If success rate < 85%, suggest specific adjustments

PYTHON: Use numpy, fixed seed, normal distribution sampling
```

---

## Creating These Files

1. Copy each section into a new `.txt` file
2. Name them as specified: `fire_formulas.txt`, `risk_framework.txt`, etc.
3. Upload to your Gemini Gem's Knowledge section

---

## File Maintenance

- Re-upload when you modify formulas or add new risk categories
- Include a version date at the top of each file
- Keep each file under 5 MB
