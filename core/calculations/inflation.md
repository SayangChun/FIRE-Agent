# Inflation Impact

## Definition

Inflation is the rate at which the general price level of goods and services rises over time, eroding the purchasing power of money. In FIRE planning, inflation reduces the real value of both accumulated wealth and future income, making it one of the most critical variables to model correctly.

## Why It Matters

A portfolio that appears adequate today may be insufficient in 20 or 30 years due to inflation. Planning with nominal (non-inflation-adjusted) numbers systematically overstates the real purchasing power of future withdrawals. Even modest 3% inflation halves purchasing power in approximately 24 years. FIRE retirees with 30–50 year horizons must account for inflation to avoid running out of money.

## Mathematical Framework

### Purchasing Power Decay

```
Future Value in Today's Dollars = Nominal Amount / (1 + inflation_rate)^years
```

Or equivalently:

```
Purchasing Power = 1 / (1 + inflation_rate)^years
```

### Inflation-Adjusted FIRE Number

```
FIRE Number (real) = FIRE Number (nominal today) × (1 + inflation_rate)^years_to_FI
```

### Real vs. Nominal Returns

```
Real Return ≈ Nominal Return - Inflation Rate (approximate)
Real Return = (1 + Nominal Return) / (1 + Inflation Rate) - 1 (exact)
```

### Future Expenses in Today's Dollars

```
Real Expenses(t) = Current Expenses × (1 + real_spending_growth)^t
```

### Purchasing Power Halving Time

```
Years to halve = ln(0.5) / ln(1 / (1 + inflation_rate))
```

| Inflation Rate | Years to Halve Purchasing Power |
|----------------|----------------------------------|
| 2%             | ~35 years                        |
| 3%             | ~24 years                        |
| 4%             | ~18 years                        |
| 5%             | ~14 years                        |
| 6%             | ~12 years                        |

## Historical Inflation Data (US CPI, Selected Years)

| Period | Average Annual Inflation |
|--------|--------------------------|
| 1970–1980 | 7.4%                  |
| 1980–1990 | 5.1%                  |
| 1990–2000 | 2.9%                  |
| 2000–2010 | 2.5%                  |
| 2010–2020 | 1.8%                  |
| 2020–2023 | 5.2% (post-COVID surge)|
| Long-term average | ~3.0%             |

## Examples

### Example 1: Inflation eroding a $1M portfolio
- **Today**: $1,000,000 buys 1,000,000 units of "stuff"
- **Year 10** (3% inflation): $1,000,000 buys 744,090 units (25.6% loss)
- **Year 20** (3% inflation): $1,000,000 buys 553,676 units (44.6% loss)
- **Year 30** (3% inflation): $1,000,000 buys 411,987 units (58.8% loss)

### Example 2: Adjusting FIRE Number for inflation
- **Current expenses**: $50,000/year
- **Years to FIRE**: 10 years
- **Expected inflation**: 3%/year

```
FIRE Number today = $50,000 × 25 = $1,250,000 (at 4% withdrawal)
Actual FIRE Number needed at year 10 = $50,000 × (1.03)^10 × 25
= $50,000 × 1.3439 × 25
= $1,679,888
```

The $1,250,000 target is **$429,888 too low** if inflation is not accounted for.

### Example 3: Real vs. nominal return impact
- **Nominal return**: 8%
- **Inflation**: 3%
- **Real return**: (1.08 / 1.03) - 1 = 4.85%

A $1M portfolio growing at 8% nominal for 30 years = $10.06M nominal
But in today's dollars: $10.06M / (1.03)^30 = $4.12M real

Planning with the 8% nominal return would overstate real wealth by 144%.

### Example 4: Inflation's asymmetric impact on retirees
- Retiree with $60K annual withdrawal at 4% inflation
- Year 1: $60,000
- Year 10: $89,157 (50% more spending needed for same lifestyle)
- Year 20: $132,488 (121% more)
- Year 30: $196,677 (228% more)

## Mitigation Strategies

1. **Use real returns for all projections** — Never plan with nominal returns alone
2. **Build inflation-adjusted withdrawal increases** — Withdrawal amounts must increase with CPI
3. **Hold inflation-protected securities** — TIPS (Treasury Inflation-Protected Securities) provide guaranteed inflation adjustment
4. **Maintain equity exposure** — Stocks historically outpace inflation over long periods
5. **Diversify internationally** — Geographic diversification hedges against US-specific inflation
6. **Include real assets** — Real estate, commodities, and TIPS provide inflation hedging
7. **Reassess FIRE Number every 5 years** — Recalculate as actual inflation data emerges
8. **Use conservative inflation assumptions** — Plan for 3–4% inflation even if recent data shows lower

## Relevance to FIRE Planning

Inflation is the silent destroyer of retirement plans. A FIRE Number calculated without inflation adjustment will systematically underestimate the required portfolio. Every calculation in this system — FIRE Number, savings rate, compound growth, and withdrawal strategies — must incorporate inflation to produce reliable results. The difference between nominal and real planning can be hundreds of thousands of dollars over a multi-decade retirement.

---

*References: Bureau of Labor Statistics CPI data; FRED (Federal Reserve Economic Data); historical inflation calculators*
