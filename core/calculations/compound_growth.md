# Compound Growth

## Definition

Compound growth is the process by which an investment earns returns on both the original principal and previously accumulated returns, creating exponential growth over time. Combined with regular contributions, it is the engine that transforms savings into wealth.

## Why It Matters

Compound growth is the mathematical reason long-term investing works. A dollar invested at age 25 is worth dramatically more than a dollar invested at age 45 — not because the first dollar is "better," but because it has more time to compound. Understanding compound growth allows FIRE planners to quantify exactly how much time and how many contributions are needed to reach their targets.

## Mathematical Framework

### Simple Future Value (No Contributions)

```
FV = PV × (1 + r)^n
```

Where:
- `FV` = Future Value
- `PV` = Present Value (initial investment)
- `r` = periodic rate of return
- `n` = number of periods

### Future Value with Regular Contributions

```
FV = PV × (1 + r)^n + PMT × [((1 + r)^n - 1) / r]
```

Where:
- `PMT` = regular contribution per period
- The second term is a **future value of an annuity**

### Present Value of a Future Goal

```
PV = FV / (1 + r)^n
```

This tells you how much to invest today to reach a future target.

### Effective Annual Rate (Inflation-Adjusted)

```
Real Rate ≈ Nominal Rate - Inflation Rate (approximate)
Real Rate = (1 + Nominal Rate) / (1 + Inflation Rate) - 1 (exact)
```

### Rule of 72

```
Years to double ≈ 72 / (rate of return × 100)
```

Example at 7% return: 72 / 7 ≈ 10.3 years to double.

### Rule of 114 (Triple)

```
Years to triple ≈ 114 / (rate of return × 100)
```

### Rule of 144 (Quadruple)

```
Years to quadruple ≈ 144 / (rate of return × 100)
```

## Examples

### Example 1: Single lump sum
- **$10,000 invested at 7% for 30 years**
- FV = $10,000 × (1.07)^30 = $10,000 × 7.612 = **$76,123**
- The $10,000 grew 7.6× without any additional contributions

### Example 2: Monthly contributions
- **$500/month at 7% annual (0.583%/month) for 30 years**
- FV = $0 × (1.00583)^360 + $500 × [((1.00583)^360 - 1) / 0.00583]
- FV ≈ **$610,075**
- Total contributions: $180,000 → Investment gains: $430,075

### Example 3: Combining lump sum and contributions
- **$50,000 initial + $500/month at 7% for 30 years**
- Lump sum component: $50,000 × 7.612 = $380,600
- Contribution component: $610,075
- Total: **$990,675**
- Total out-of-pocket: $230,000 → Investment gains: $760,675

### Example 4: Impact of starting early
- **Investor A**: Starts at 25, invests $300/month for 30 years (age 25–55), then stops
  - Total contributions: $108,000 → Value at 55: ~$380,000
- **Investor B**: Starts at 35, invests $300/month for 30 years (age 35–65)
  - Total contributions: $108,000 → Value at 65: ~$340,000
- Investor A contributed the same amount but ended up with more — and retired 10 years earlier

### Real vs. Nominal Returns

| Metric | Nominal | Real (2% inflation) |
|--------|---------|---------------------|
| Annual return | 7% | 4.9% |
| $10K after 10 years | $19,672 | $16,098 |
| $500/mo after 30 years | $610,075 | $424,536 |

Always plan using real returns to maintain purchasing power.

## Mitigation Strategies

1. **Start immediately** — Time is the most powerful variable in compound growth equations
2. **Maximize tax-advantaged accounts** — Roth IRA, 401(k), HSA shield returns from taxation
3. **Reinvest dividends** — Dividend reinvestment accelerates compounding
4. **Minimize fees** — A 1% fee difference compounds to ~25% less wealth over 30 years
5. **Use real returns for planning** — Nominal returns overstate growth in real terms

## Relevance to FIRE Planning

Compound growth determines how quickly your portfolio reaches the FIRE Number. The interplay between savings rate (which determines contribution volume), investment returns (which determine growth rate), and time (which determines compounding duration) defines your FIRE timeline. Every year you delay saving costs you exponentially more in future wealth.

---

*References: Principles of Corporate Finance (Brealey, Myers, Allen); Bogleheads investment philosophy; Portfolio Visualizer backtests*
