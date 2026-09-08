# Withdrawal Strategies

## Definition

Withdrawal strategies are methods for drawing income from a retirement portfolio to sustain spending over a multi-decade retirement without depleting the portfolio. They balance the need for current income against the risk of outliving assets.

## Why It Matters

Reaching FIRE is only half the challenge. The other half is spending that wealth sustainably over 30–50+ years. A poorly chosen withdrawal strategy can lead to portfolio depletion in bad markets; an overly conservative strategy leads to unnecessary deprivation. The right strategy adapts to market conditions while maintaining quality of life.

## Mathematical Framework

### The 4% Rule (Trinity Study)

```
Year 1 Withdrawal = FIRE Number × 4%
Subsequent Years = Previous Year Withdrawal × (1 + inflation)
```

The Trinity Study found that a 4% initial withdrawal rate, adjusted annually for inflation, had a ~95% success rate over 30 years using a 50/50 or 75/25 stock/bond portfolio.

**Survival rates by withdrawal rate (30-year horizon, historical US data):**

| Withdrawal Rate | Success Rate |
|-----------------|--------------|
| 3.0%            | ~100%        |
| 3.5%            | ~99%         |
| 4.0%            | ~95%         |
| 4.5%            | ~85%         |
| 5.0%            | ~70%         |

For 40+ year retirements, use 3.5% or lower.

### Constant Percentage Withdrawal

```
Annual Withdrawal = Portfolio Value × Fixed Percentage
```

This never depletes the portfolio (mathematically) but produces highly variable income.

### Variable Percentage Withdrawal (VPW)

```
Withdrawal = Portfolio Value × Variable Percentage(Timeline, Returns)
```

Adjusts withdrawal percentage based on remaining life expectancy and recent returns.

### Bucket Strategy

```
Bucket 1: 1-2 years expenses → Cash/short-term bonds
Bucket 2: 3-7 years expenses → Intermediate bonds/conservative allocation
Bucket 3: 8+ years expenses → Growth stocks/index funds
```

During downturns, spend from Bucket 1 and 2; allow Bucket 3 to recover.

### Floor-and-Ceiling Approach

```
Floor = Minimum acceptable income (essential expenses)
Ceiling = Maximum lifestyle spending (desired expenses)
Target = Portfolio value × Withdrawal Rate
Actual Withdrawal = clamp(Target, Floor, Ceiling)
```

This guarantees essential expenses are met while allowing upside participation.

### Guyton-Klinger Guardrails

```
If withdrawal rate > ceiling (e.g., 5.5%): reduce spending by 10%
If withdrawal rate < floor (e.g. 3.5%): increase spending by 10%
Otherwise: adjust for inflation as normal
```

Withdrawal rate = Current Withdrawal / Current Portfolio Value

## Examples

### Example 1: 4% Rule with $1.5M portfolio
- **Year 1**: $1,500,000 × 4% = $60,000
- **Year 2** (3% inflation): $60,000 × 1.03 = $61,800
- **Year 3**: $61,800 × 1.03 = $63,654
- Portfolio needs to sustain ~$60K+ annual withdrawals for 30+ years

### Example 2: Bucket strategy in a crash
- Market drops 30% in Year 3
- Bucket 1 (cash): $120,000 — spend from here for 2 years
- Bucket 2 (bonds): $300,000 — replenish Bucket 1 as needed
- Bucket 3 (stocks): $900,000 → $630,000 — let recover, don't sell
- When Bucket 3 recovers, rebalance to refill Buckets 1 and 2

### Example 3: Guardrails in action
- Portfolio: $1.5M, Withdrawal: $60,000 (4.0%)
- **Good year**: Portfolio grows to $1.65M → rate = 3.64% → below floor → increase spending by 10% to $66,000
- **Bad year**: Portfolio drops to $1.2M → rate = 5.0% → above ceiling → decrease spending by 10% to $54,000

### Example 4: Dynamic withdrawal with VPW
- Age 30, expected 60-year retirement
- VPW rate ≈ 1.8% (conservative for long horizon)
- Portfolio: $1.5M → $27,000/year (very conservative)
- Age 40, 50 years left → VPW rate ≈ 2.1% → $31,500/year
- Rate increases as remaining timeline shortens

## Mitigation Strategies

1. **Use a conservative baseline** — 3.5% for 40-year retirements, 4.0% for 30-year retirements
2. **Maintain flexibility** — Have discretionary expenses you can cut in bad years
3. **Keep 2–3 years in cash/bonds** — Avoid selling stocks during drawdowns
4. **Rebalance annually** — Maintain target allocation to capture recovery
5. **Consider part-time work** — Even minimal income reduces portfolio withdrawals
6. **Track withdrawal rate monthly** — Early warning if rate exceeds guardrails

## Relevance to FIRE Planning

The withdrawal strategy determines whether your FIRE portfolio sustains you for life or runs dry. It must be selected during the accumulation phase so you can plan portfolio size and allocation accordingly. Most FIRE planners should plan for 40+ year retirements, making conservative withdrawal rates (3.0–3.5%) prudent.

---

*References: Trinity Study (1998); Guyton-Klinger Decision Rules; VPW (Longinvest); ERN Safe Withdrawal Rate series; BigERN's GoCurryCracker analyses*
