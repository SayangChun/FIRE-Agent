# Savings Rate

## Definition

The savings rate is the percentage of income saved and invested rather than consumed. It is the single most influential variable in determining the timeline to financial independence.

## Why It Matters

The savings rate has a nonlinear, outsized impact on the FIRE timeline. Increasing savings rate from 10% to 20% doesn't halve the timeline — it reduces it by far more than half because it simultaneously:
1. Increases the amount invested each period
2. Decreases the annual expenses that must be covered in retirement (lowering the FIRE Number)

## Mathematical Framework

### Core Formula

```
Savings Rate = (Income - Expenses) / Income × 100%
```

Equivalently:

```
Savings Rate = (Income - Expenses) / Income
```

### Years to FIRE

```
Years to FIRE = -ln(1 - (Savings Rate × (1 + r) / (r × (1 - Savings Rate)))) / ln(1 + r)
```

Where:
- `r` = real rate of return (investment returns minus inflation)
- `ln` = natural logarithm

Simplified for a 0% real return (pure savings accumulation):

```
Years to FIRE = -ln(1 - Savings Rate) / ln(1 + 0)
```

This simplifies to: Years = -ln(1 - Savings Rate)

### Sensitivity Table (Real Return = 5%)

| Savings Rate | Years to FIRE | Multiplier vs. 10% |
|--------------|---------------|---------------------|
| 10%          | ~51 years     | 1.00×               |
| 15%          | ~43 years     | 0.84×               |
| 20%          | ~37 years     | 0.73×               |
| 25%          | ~32 years     | 0.63×               |
| 30%          | ~28 years     | 0.55×               |
| 40%          | ~22 years     | 0.43×               |
| 50%          | ~17 years     | 0.33×               |
| 60%          | ~12.5 years   | 0.25×               |
| 70%          | ~8.5 years    | 0.17×               |
| 80%          | ~5.5 years    | 0.11×               |
| 90%          | ~2.5 years    | 0.05×               |

### Relationship to Income and Expenses

```
Savings Rate = 1 - (Expenses / Income)
```

To increase savings rate, you have two levers:
1. **Increase income** — raises the numerator directly
2. **Decrease expenses** — raises the numerator and lowers the FIRE Number

The expense lever is more powerful because it has a dual effect.

## Examples

### Example 1: Two earners, same income
- **Person A**: $80K income, $60K expenses → 25% savings rate → ~32 years to FIRE
- **Person B**: $80K income, $40K expenses → 50% savings rate → ~17 years to FIRE
- Person B reaches FIRE **15 years sooner** by spending $20K less per year

### Example 2: Income increase impact
- **Before raise**: $100K income, $70K expenses → 30% savings rate → ~28 years
- **After raise** (spending same): $120K income, $70K expenses → 41.7% savings rate → ~22 years
- **After raise** (lifestyle inflation): $120K income, $90K expenses → 25% savings rate → ~32 years

Lifestyle inflation negates the benefit of income growth.

### Example 3: Geographic arbitrage
- **High-cost city**: $150K income, $100K expenses → 33% savings rate → ~26 years
- **Low-cost city**: $150K income, $60K expenses → 60% savings rate → ~12.5 years
- Same income, half the time to FIRE

## Mitigation Strategies

1. **Automate savings** — Set up automatic transfers before spending is possible
2. **Track expenses quarterly** — Identify creeping lifestyle inflation
3. **Use the 50/30/20 rule as a floor** — Never drop below 20% savings rate
4. **Increase savings rate with each raise** — Commit 50%+ of every raise to savings
5. **Separate wants from needs** — Essentials (housing, food, healthcare) vs. discretionary (travel, dining, entertainment)

## Relevance to FIRE Planning

The savings rate is the primary lever for accelerating FIRE. It determines both how much you invest and how large your FIRE Number needs to be. A 50% savings rate is often cited as the target for a ~17-year FIRE timeline, but any increase from current levels compounds dramatically over time.

---

*References: Mr. Money Mustache "The Shockingly Simple Math Behind Early Retirement"; cFIREsim; earlyretirementnow.com*
