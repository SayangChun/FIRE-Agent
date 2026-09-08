# Sequence of Returns Risk

## Definition

Sequence of returns risk is the danger that the order of investment returns — not just their average — will negatively impact a portfolio's longevity. Specifically, receiving poor returns early in retirement (when the portfolio is largest and withdrawals are being made) can permanently damage a portfolio's ability to recover, even if average returns over the full period are identical.

## Why It Matters

Two retirees with the same average return, same starting portfolio, and same withdrawal rate can have dramatically different outcomes depending on whether bad returns came early or late. Early retirees are especially vulnerable because they are withdrawing from a large portfolio during the critical first 5–10 years of retirement. A 30% crash in year 1 while withdrawing $60K is far more damaging than the same crash in year 20 when the portfolio is smaller and has already grown.

## Mathematical Framework

### The Asymmetry Problem

```
Portfolio(t+1) = (Portfolio(t) - Withdrawal) × (1 + Return(t))
```

Because the withdrawal is subtracted before the return is applied, negative returns on a post-withdrawal portfolio reduce the base for future compounding. The portfolio never gets to participate in the recovery.

### Demonstration: Same Average Return, Different Sequences

**Sequence A** (bad returns early): -15%, +20%, -10%, +25%, +15%
**Sequence B** (good returns early): +15%, +25%, -10%, +20%, -15%

Both have the same arithmetic average return: +7% per year.

Starting with $1,000,000 and $40,000 annual withdrawal:

| Year | Sequence A | Sequence B |
|------|-----------|-----------|
| 0    | $1,000,000 | $1,000,000 |
| 1    | $810,000   | $1,110,000 |
| 2    | $932,000   | $1,347,500 |
| 3    | $798,800   | $1,172,750 |
| 4    | $948,500   | $1,415,938 |
| 5    | $1,050,775 | $1,173,547 |

Sequence A ends higher despite early losses — but if withdrawals are higher, early losses compound devastatingly.

### Critical Vulnerability Period

The first 5–10 years of retirement represent the **danger zone** where sequence risk is most impactful. After this period, the portfolio has either survived or been sufficiently damaged that the outcome is largely determined.

### Quantifying Sequence Risk Impact

```
Effective Loss = Actual Loss × (Portfolio Size at Time of Loss / Average Portfolio Size)
```

A -30% return when the portfolio is $1.5M costs $450K.
The same -30% return when the portfolio is $800K costs $240K.

The withdrawal rate amplifies this: higher withdrawal rates create larger post-withdrawal portfolios exposed to negative returns.

## Examples

### Example 1: The Year 1 Crash
- **Retiree A**: $1M portfolio, $40K/yr withdrawal
  - Year 1: -30% → ($1M - $40K) × 0.70 = $672,000
  - Recovery requires +49% gain just to break even
- **Retiree B**: $1M portfolio, $40K/yr withdrawal
  - Year 1: +15% → ($1M - $40K) × 1.15 = $1,104,000
  - Year 2: -30% → ($1,104,000 - $40K) × 0.70 = $745,200
  - The same crash happens but the portfolio has a larger base

### Example 2: Historical sequence risk
- **2000 retiree** (S&P 500): -9.1% (2000), -11.9% (2001), -22.1% (2002) → devastating sequence
- **2003 retiree** (S&P 500): +28.7% (2003), +10.9% (2004), +4.9% (2005) → strong start
- Both had similar average returns over 2000–2020, but very different portfolio outcomes

### Example 3: Impact on withdrawal sustainability
- **Portfolio**: $1.5M, **Withdrawal**: $60K/yr (4% rate)
- **Sequence A** (bad early): 30-year Monte Carlo success rate = 85%
- **Sequence B** (good early): 30-year Monte Carlo success rate = 97%
- Same average return assumption, 12% difference in success rate

### Example 4: The math of recovery
- Portfolio drops 30%: needs +42.9% to recover
- Portfolio drops 40%: needs +66.7% to recover
- Portfolio drops 50%: needs +100% to recover
- Withdrawals make recovery even harder because you're withdrawing during the recovery period

## Mitigation Strategies

1. **Cash buffer (2–3 years)** — Keep 2–3 years of expenses in cash or short-term bonds. During a downturn, spend from the buffer and avoid selling equities at a loss.

2. **Flexible spending** — Reduce discretionary spending by 10–20% during the first 5 years if the market drops. This single rule can increase success rate by 5–10%.

3. **Guardrails approach** — Set floor (3.5%) and ceiling (5.5%) withdrawal rates. If the withdrawal rate rises above the ceiling, cut spending; if it drops below the floor, increase spending.

4. **Bucket strategy** — Separate the portfolio into time-segmented buckets:
   - Bucket 1 (Years 1–2): Cash
   - Bucket 2 (Years 3–7): Bonds
   - Bucket 3 (Years 8+): Growth stocks

5. **Reduce withdrawal rate** — Use 3.5% or lower for the first 5–10 years, then increase once past the danger zone.

6. **Part-time income** — Working part-time for 2–5 years in early retirement directly reduces withdrawals during the most vulnerable period.

7. **Annuity floor** — A single-premium immediate annuity (SPIA) covering essential expenses eliminates sequence risk for that portion of spending.

8. **Laddered bond portfolio** — Pre-construct a bond ladder covering 5–10 years of expenses to guarantee income regardless of equity market performance.

## Relevance to FIRE Planning

Sequence of returns risk is arguably the most critical risk for FIRE retirees because:
- FIRE retirees have 40–50+ year horizons (longer danger zone)
- They are withdrawing during the very period when sequence risk is most damaging
- The FIRE community typically uses low withdrawal rates (3–4%) partly to mitigate this risk
- It explains why the same historical data can support very different conclusions about safe withdrawal rates

Every withdrawal strategy and cash reserve decision in a FIRE plan should explicitly account for sequence risk.

---

*References: Wade Pfau "Retirement Planning Guidebook"; Michael Kitces sequence risk research; ERN Safe Withdrawal Rate series; Financial Planning Association studies*
