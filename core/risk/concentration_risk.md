# Concentration Risk

## Definition

Concentration risk is the danger that a portfolio's value is disproportionately dependent on a single asset, sector, geography, or asset class. When a concentrated position declines, the portfolio suffers outsized losses relative to a diversified benchmark. It is the opposite of diversification — putting too many eggs in one basket.

## Why It Matters

FIRE portfolios are typically smaller than traditional retirement portfolios because they must last longer. A concentrated loss of 50–80% in a single position can permanently impair a FIRE portfolio, making recovery mathematically impossible without additional income. Concentration risk is particularly insidious because it often arises from success — a stock that has grown to dominate a portfolio was a good investment, but its growth has created new risk.

## Mathematical Framework

### Portfolio Concentration Measure

```
Concentration Ratio = Largest Position Value / Total Portfolio Value
```

| Concentration Level | Ratio | Risk Assessment |
|---------------------|-------|-----------------|
| Highly diversified  | < 5%  | Low             |
| Moderately diversified | 5–15% | Moderate      |
| Concentrated        | 15–30%| High            |
| Highly concentrated | > 30% | Very high       |

### Sector Concentration

```
Sector Weight = Sector Allocation / Total Equity Allocation
```

A portfolio with 60% in technology has high sector concentration.

### Single-Asset Impact Analysis

```
Portfolio Loss = Position Loss × Position Weight
```

If a 30% position drops 50%:
```
Portfolio Loss = 50% × 30% = 15% of total portfolio
```

A diversified portfolio with the same stock at 5% weight:
```
Portfolio Loss = 50% × 5% = 2.5% of total portfolio
```

The concentrated portfolio loses 6× more from the same stock decline.

### Correlation and Diversification Benefit

```
Portfolio Variance = Σ(w_i² × σ_i²) + Σ Σ(w_i × w_j × σ_i × σ_j × ρ_ij)
```

Where:
- `w_i`, `w_j` = portfolio weights
- `σ_i`, `σ_j` = standard deviations
- `ρ_ij` = correlation between assets

Diversification benefit occurs when ρ_ij < 1.0. Perfect diversification requires low or negative correlations across positions.

### Number of Stocks for Diversification

Research shows:
- **1 stock**: 49.2% annual standard deviation (US)
- **10 stocks**: 23.9% (significant reduction)
- **30 stocks**: 20.5% (diminishing returns)
- **50+ stocks**: 19.5% (nearly maximally diversified)

Most diversification benefit is achieved with 30–50 well-chosen stocks across sectors.

## Examples

### Example 1: Tech concentration in 2022
- **Portfolio**: $1.5M, 60% in tech (Apple, Microsoft, Google, Amazon, Meta)
- **2022 tech drawdown**: NASDAQ dropped ~33%
- **Portfolio impact**: 60% × 33% = 19.8% loss = **$297,000**
- **Diversified equivalent**: Same tech stocks at 15% weighting → 4.95% loss = **$74,250**
- Difference: $222,750 from concentration alone

### Example 2: Single stock blowup
- **Retiree A**: 40% in company stock (employer), drops 70% in scandal
- Portfolio loss: 40% × 70% = 28% = **$420,000** on a $1.5M portfolio
- Recovery requires +39% gain just to break even
- **Retiree B**: 5% in same company stock
- Portfolio loss: 5% × 70% = 3.5% = **$52,500**
- Recovery requires +3.6% gain — easily achievable

### Example 3: Geographic concentration
- **Portfolio**: 100% US equities
- **Scenario**: US underperforms international for a decade (as 2000–2010)
- US stocks: +1.4% annualized (S&P 500, 2000–2010)
- International stocks: +4.6% annualized (MSCI EAFE, 2000–2010)
- A diversified 60/40 US/international portfolio outperformed by 2%+ annually

### Example 4: Sector rotation
- **2000**: 40% in technology → dot-com crash → -78% in NASDAQ
- **2008**: 40% in financials → financial crisis → -83% in financial stocks
- **2020**: 30% in energy → oil price collapse → -55% in energy stocks
- Each decade, a different sector devastated concentrated portfolios

### Example 5: The crypto concentration risk
- **Portfolio**: $500K in Bitcoin and Ethereum (100% crypto)
- **2022 crypto winter**: -75% drawdown
- Portfolio value: $500K → $125K
- FIRE plan destroyed — requires +300% to recover

## Diversification Benefits

### Asset Class Diversification

| Portfolio           | Expected Return | Standard Deviation | Sharpe Ratio |
|---------------------|-----------------|---------------------|--------------|
| 100% US Stocks      | 10.0%           | 15.5%              | 0.52         |
| 60/40 Stocks/Bonds  | 8.5%            | 11.0%              | 0.59         |
| Global 60/40        | 8.2%            | 10.5%              | 0.60         |
| Global with TIPS    | 7.8%            | 9.8%               | 0.59         |

Diversification can improve risk-adjusted returns (higher Sharpe ratio) while reducing absolute risk.

### Geographic Diversification

```
Diversification Ratio = (Average Individual Volatility) / (Portfolio Volatility)
```

A ratio > 1.0 indicates diversification benefit. Typical global equity portfolios achieve 1.2–1.5.

## Mitigation Strategies

### 1. Position Size Limits
- No single stock > 5–10% of portfolio
- No single sector > 25% of equity allocation
- No single country > 50% of equity allocation (except home country bias of up to 60%)

### 2. Regular Rebalancing
- **Frequency**: Quarterly or when allocation drifts > 5% from target
- **Method**: Sell overvalued, buy undervalued (natural buy-low-sell-high)
- **Tax consideration**: Use tax-advantaged accounts for rebalancing when possible

### 3. Index Fund Diversification
- US Total Market Index: ~3,500 stocks in one fund
- International Index: ~7,000+ stocks globally
- Bond Index: Broad market bond exposure
- Single fund provides instant diversification

### 4. Asset Allocation Framework

**FIRE-appropriate allocation:**
- 60–80% equities (US + International)
  - 60% US (total market)
  - 40% International (developed + emerging)
- 15–30% fixed income (bonds + TIPS)
- 5–10% real assets (REITs, commodities)

### 5. Employer Stock Diversification
- If > 10% of portfolio is employer stock, systematically sell
- Use 10b5-1 plan for tax-advantaged diversification
- Priority: reduce to < 5% within 3–5 years of FIRE

### 6. Rebalancing Tax Optimization
- Rebalance in tax-advantaged accounts first (no tax consequence)
- In taxable accounts, use new contributions to rebalance
- Harvest tax losses when rebalancing out of losing positions

### 7. Correlation Monitoring
- Review portfolio correlations annually
- If correlations increase (assets moving together), diversification benefit decreases
- Consider adding uncorrelated assets (alternative investments, managed futures)

## Concentration Risk Assessment Checklist

```
□ No single stock > 10% of portfolio
□ No single sector > 25% of equity allocation
□ No single country > 60% of equity allocation
□ Portfolio of 30+ individual stocks OR broad index funds
□ Fixed income diversified across duration and credit quality
□ Real assets present (REITs, commodities, or real estate)
□ No more than 50% in correlated assets (e.g., all tech, all growth)
□ Annual review of correlation matrix
□ Rebalancing schedule established
□ Employer stock < 5% of portfolio
```

## Relevance to FIRE Planning

Concentration risk is particularly dangerous for FIRE retirees because:
1. **Smaller portfolios** have less margin for error — a 30% loss is harder to recover from
2. **Longer horizons** increase the probability of experiencing a concentration-related drawdown
3. **Withdrawals during drawdowns** lock in losses from concentrated positions
4. **Recovery mathematics** — a 50% loss requires a 100% gain; a 70% loss requires a 233% gain

Every FIRE portfolio should be stress-tested for concentration risk using the checklist above. Diversification is the only free lunch in investing — it reduces risk without necessarily reducing expected returns.

---

*References: Modern Portfolio Theory (Markowitz); Fama-French research on diversification; Bogleheads investment philosophy; AQR research on diversification benefits*
