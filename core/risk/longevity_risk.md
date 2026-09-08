# Longevity Risk

## Definition

Longevity risk is the possibility of outliving your retirement savings — the risk that your lifespan exceeds the time horizon your portfolio was designed to sustain. It is the intersection of uncertain life expectancy and finite financial resources.

## Why It Matters

FIRE retirees face an amplified longevity risk because they retire decades before traditional retirement age. A retiree at 35 may need their portfolio to last 50–60+ years. Traditional retirement planning assumes a 20–30 year horizon; FIRE demands planning for a timeframe that has no historical precedent for most retirement models. Additionally, healthcare improvements and lifestyle factors may extend life expectancy beyond statistical averages.

## Mathematical Framework

### Life Expectancy vs. Planning Horizon

The planning horizon should exceed life expectancy to provide a margin of safety:

```
Planning Horizon = Life Expectancy + Safety Margin
```

For a 35-year-old with expected lifespan of 85:
```
Minimum Planning Horizon = 85 - 35 = 50 years
With 10-year safety margin = 60 years
```

### Portfolio Survival Probability Over Time

Using the 4% rule with a 60/40 portfolio:

| Time Horizon | Success Rate |
|--------------|--------------|
| 30 years     | 95%          |
| 35 years     | 88%          |
| 40 years     | 82%          |
| 45 years     | 76%          |
| 50 years     | 70%          |

The longer the horizon, the lower the success rate for a fixed withdrawal rate.

### Required Withdrawal Rate for Extended Horizons

```
For 30 years: 4.0% withdrawal rate is reasonable
For 40 years: 3.5% recommended
For 50 years: 3.0% or lower
```

### Mortality Table Reference (US SSA, at age 30)

- Median lifespan: ~83 years (53 years remaining)
- 25th percentile: ~79 years (49 years remaining)
- 75th percentile: ~87 years (57 years remaining)
- 90th percentile: ~91 years (61 years remaining)
- Maximum observed: 122 years (historical)

### Portfolio Required for Different Lifespans

At 3.5% withdrawal rate, $60K/year expenses:

| Expected Lifespan | Planning Years | FIRE Number Required |
|--------------------|----------------|----------------------|
| 75                 | 40            | $1,714,286           |
| 80                 | 45            | $1,714,286           |
| 85                 | 50            | $1,714,286           |
| 90                 | 55            | $1,714,286           |

The FIRE Number itself doesn't change — the withdrawal rate and portfolio allocation must adapt.

## Examples

### Example 1: The 35-year-old FIRE retiree
- **Age at FIRE**: 35
- **Expected lifespan**: 85 (median)
- **Planning horizon needed**: 50 years minimum
- **Annual expenses**: $50,000
- **Required withdrawal rate**: 3.0% (for 50-year horizon)
- **FIRE Number**: $50,000 / 0.03 = **$1,666,667**

This is 25% larger than the same retiree would need using the 4% rule for a 30-year horizon.

### Example 2: Couple planning for 60 years
- **Ages**: Both 35
- **Joint planning horizon**: 60 years (to age 95)
- **Annual expenses**: $60,000
- **Required withdrawal rate**: 2.5% (extremely conservative for 60 years)
- **FIRE Number**: $60,000 / 0.025 = **$2,400,000**

### Example 3: Flexible withdrawal as longevity hedge
- **Portfolio**: $2M, **Initial withdrawal**: $70,000 (3.5%)
- **Year 10**: Market drops 30% → portfolio = $1.2M
- **New withdrawal**: $42,000 (3.5%) — reduced spending
- **Year 20**: Market recovers → portfolio = $2.5M
- **New withdrawal**: $87,500 (3.5%) — increased spending
- Flexibility allows the portfolio to survive longer than a fixed withdrawal

### Example 4: The survivor problem
- **Retiree A**: Dies at 78 (20 years of retirement) — large surplus remaining
- **Retiree B**: Dies at 98 (40 years of retirement) — may face scarcity
- Same portfolio, same withdrawal rate, completely different outcomes
- Planning must account for the tail risk of living longer than expected

## Strategies for Managing Longevity Risk

### 1. Flexible Withdrawal Rate
- Use variable withdrawals that adjust to portfolio performance
- Reduce spending in down markets; allow increases in good markets
- This is the single most powerful tool against longevity risk

### 2. Annuities (SPIA)
- **Single Premium Immediate Annuity** provides guaranteed lifetime income
- Eliminates longevity risk for the portion of expenses covered
- Limitation: illiquid, no inflation adjustment (unless inflation-linked annuity)
- **Recommended allocation**: 20–40% of portfolio for essential expenses

### 3. Social Security Optimization
- Delay claiming Social Security to age 70 if possible
- Each year of delay from 62 to 70 increases benefit by ~8%
- Social Security provides inflation-adjusted lifetime income — valuable longevity hedge

### 4. Healthcare Cost Planning
- Healthcare is the largest uncertain expense in long retirements
- Budget for ACA premiums, out-of-pocket costs, and potential long-term care
- Consider long-term care insurance (though expensive and complex)

### 5. Tax Diversification
- Maintain mix of taxable, tax-deferred, and tax-free (Roth) accounts
- Provides flexibility to manage tax brackets in later retirement years
- Roth withdrawals are tax-free and don't affect Medicare premiums

### 6. Geographic Flexibility
- Ability to relocate to lower cost-of-living areas extends portfolio
- International geo-arbitrage can reduce expenses by 30–50%
- Maintain ability to move while preserving social connections

### 7. Part-Time Work (Phased Retirement)
- Working 10–15 hours/week in early retirement reduces withdrawals
- Even minimal income ($20K–$30K/year) dramatically extends portfolio life
- Also provides social connection, purpose, and healthcare access

### 8. Insurance Products
- **Long-term care insurance**: Covers nursing home/assisted living costs
- **Health insurance bridge**: Cover gap between FIRE and Medicare (age 65)
- **Annuity laddering**: Purchase SPIAs at different ages for staged income

## Examples with Mathematical Framework

### Monte Carlo for 50-Year Horizon

**Inputs**: $2M portfolio, $60K/year withdrawal, 60/40 allocation, 10,000 simulations

| Percentile | Final Portfolio Value (Year 50) |
|------------|---------------------------------|
| 5th        | $0 (failed at year 38)          |
| 25th       | $800,000                        |
| 50th       | $3,200,000                      |
| 75th       | $7,500,000                      |
| 95th       | $14,000,000                     |

Success rate: 89% — 11% of simulations failed before year 50.

### Comparing Planning Horizons

**Same retiree, same $60K expenses, different planning assumptions:**

| Horizon | Withdrawal Rate | FIRE Number | Success Rate (MC) |
|---------|-----------------|-------------|---------------------|
| 30 years | 4.0%           | $1,500,000  | 95%                 |
| 40 years | 3.5%           | $1,714,286  | 91%                 |
| 50 years | 3.0%           | $2,000,000  | 87%                 |
| 60 years | 2.5%           | $2,400,000  | 84%                 |

## Relevance to FIRE Planning

Longevity risk is the defining challenge of FIRE planning. Traditional retirement assumes a 20–30 year horizon; FIRE requires planning for 40–60+ years. This demands:
- Lower withdrawal rates (3.0–3.5%)
- Larger FIRE Numbers
- Greater portfolio flexibility
- Diversified income sources (portfolio + Social Security + optional annuities)
- Explicit healthcare cost planning

Every FIRE plan must address longevity risk — it is not optional. The consequences of underestimating life expectancy are permanent and irreversible.

---

*References: SSA Life Tables; Wade Pfau "Retirement Planning Guidebook"; Michael Kitces longevity research; IRS life expectancy tables*
