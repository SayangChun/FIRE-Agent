# FIRE Calculations

## FIRE Number
```
FIRE# = Annual Expenses × Multiplier
Adjusted FIRE# = Base × (1 + inflation)^years_to_FI
```

| WR | Multiplier | $40K/yr Example |
|----|-----------|-----------------|
| 3.0% | 33.33× | $1,333K |
| 3.5% | 28.57× | $1,143K |
| 4.0% | 25.00× | $1,000K |
| 4.5% | 22.22× | $889K |
| 5.0% | 20.00× | $800K |

Edge cases: rolling 3-yr avg essential expenses, exclude one-time purchases, add healthcare premiums, adjust for geo-arbitrage.

## Savings Rate
```
SR = (Income − Expenses) / Income × 100%
Years = −ln(1 − (SR×(1+r))/(r×(1−SR))) / ln(1+r)
```
Expense lever is dual-power: lowers expenses → raises SR *and* lowers FIRE#.

| SR | Years (5% real) |
|----|----------------|
| 10% | ~51 |
| 20% | ~37 |
| 30% | ~28 |
| 40% | ~22 |
| 50% | ~17 |
| 60% | ~12.5 |
| 80% | ~5.5 |

## Compound Growth
```
FV = PV × (1+r)^n + PMT × [((1+r)^n − 1) / r]
PV = FV / (1+r)^n
Real Return = (1+Nominal)/(1+Inflation) − 1
```
Rule of 72: double ≈ 72/(r×100). 1% fee diff ≈ 25% less wealth over 30yr.

## Withdrawal Strategies

**4% Rule:** `Year 1 = FIRE# × 4%`, subsequent = prev × (1+inflation). Success (30yr): 3%→100%, 3.5%→99%, 4%→95%, 5%→70%.

**Bucket:** 1–2yr cash, 3–7yr bonds, 8+yr growth stocks.

**Guardrails:** WR>5.5% → cut 10%; WR<3.5% → increase 10%; else adjust inflation.

**VPW:** adjusts % based on life expectancy + recent returns.

## Inflation
```
Real Value = Nominal / (1+inflation)^years
Min Required Return = Inflation + WR
```

| Inflation | Years to Halve Purchasing Power |
|-----------|-------------------------------|
| 2% | ~35 |
| 3% | ~24 |
| 4% | ~18 |
| 5% | ~14 |

3% inflation: $60K/yr → $145K needed by year 30.

## Monte Carlo
```
r_t = μ − σ²/2 + σ × Z    (Z ~ N(0,1))
Portfolio(t+1) = Portfolio(t) × (1+r_t) − Withdrawal
```

| Asset | μ | σ |
|-------|-----|------|
| US Large Cap | 10.0% | 15.5% |
| Int'l | 9.0% | 17.5% |
| Bonds | 5.0% | 6.0% |
| 60/40 | 8.5% | 11.0% |

>95% success = robust, 90–95% = solid, 80–90% = acceptable, <80% = revise. Run ≥5K sims, report percentiles.
