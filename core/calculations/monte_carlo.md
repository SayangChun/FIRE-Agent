# Monte Carlo Simulation

## Definition

Monte Carlo simulation is a computational technique that models the probability of different outcomes by running thousands of randomized scenarios using probability distributions for uncertain variables. In FIRE planning, it tests whether a given portfolio and withdrawal strategy will survive across a range of possible market sequences.

## Why It Matters

Historical backtests and deterministic models assume a single future. Monte Carlo simulation acknowledges uncertainty by testing your plan against thousands of possible futures — including worst-case scenarios that never occurred historically but could occur in the future. It quantifies the probability of success rather than providing a single binary answer.

## Mathematical Framework

### Log-Normal Return Distribution

Stock returns are modeled as log-normally distributed:

```
r_t = μ - σ²/2 + σ × Z
```

Where:
- `r_t` = simulated return in period t
- `μ` = expected annual return (mean of log returns)
- `σ` = standard deviation of annual returns (volatility)
- `Z` = random draw from standard normal distribution N(0,1)

The log-normal model ensures returns never drop below -100% (no negative portfolio values).

### Typical Parameters

| Asset Class | Expected Return (μ) | Volatility (σ) |
|-------------|---------------------|-----------------|
| US Large Cap | 10.0% | 15.5% |
| International | 9.0% | 17.5% |
| Bonds (Aggregate) | 5.0% | 6.0% |
| 60/40 Portfolio | 8.5% | 11.0% |

### Simulation Process

```
For each simulation s = 1 to N (e.g., 10,000):
    Portfolio = Starting Value
    For each year y = 1 to Retirement Length:
        Draw random return r from log-normal distribution
        Portfolio = Portfolio × (1 + r) - Withdrawal
        If Portfolio <= 0: mark simulation as FAILED, break
    Record final portfolio value

Success Rate = (Simulations where Portfolio > 0 at end) / N
```

### Confidence Intervals

```
5th percentile = Value below which 5% of simulations fell (worst case)
25th percentile = Conservative outcome
50th percentile = Median outcome
75th percentile = Optimistic outcome
95th percentile = Value above which 5% of simulations fell (best case)
```

### Interpretation of Success Rate

| Success Rate | Interpretation |
|--------------|----------------|
| > 95%        | Very robust plan |
| 90–95%       | Solid plan with minor risk |
| 80–90%       | Acceptable if flexibility exists |
| 70–80%       | Moderate risk; consider adjustments |
| < 70%        | High failure probability; revise plan |

## Examples

### Example 1: $1.5M portfolio, $60K/year withdrawal
- **Inputs**: $1.5M starting, $60K/yr withdrawal, 60/40 portfolio, 30-year horizon
- **Results** (10,000 simulations):
  - Success rate: 92%
  - Median final value: $2.1M
  - 5th percentile: -$180K (failure)
  - 95th percentile: $5.8M

### Example 2: Impact of withdrawal rate
- Same $1.5M portfolio, 30-year horizon, 10,000 simulations:

| Withdrawal Rate | Annual Amount | Success Rate |
|-----------------|---------------|--------------|
| 3.0%            | $45,000       | 99.2%        |
| 3.5%            | $52,500       | 97.5%        |
| 4.0%            | $60,000       | 92.1%        |
| 4.5%            | $67,500       | 82.4%        |
| 5.0%            | $75,000       | 68.7%        |

### Example 3: Sequence sensitivity
Two retirees, same $1.5M portfolio, same $60K/year withdrawal, different starting markets:
- **Retiree A** (2000–2030): Starts with dot-com crash and 2008 → 85% success rate in simulations
- **Retiree B** (2010–2040): Starts with bull market → 97% success rate in simulations
- Monte Carlo captures this variation across thousands of randomized sequences

### Example 4: Impact of flexibility
- **Rigid withdrawal** (always $60K): 92% success rate
- **Flexible withdrawal** (cut to $48K if portfolio drops 20%): 97% success rate
- 5% improvement from a single adaptive rule

## Limitations

1. **Assumes stationary distributions** — Past return distributions may not predict future ones
2. **Ignores fat tails** — Log-normal may underestimate extreme events (market crashes, hyperinflation)
3. **Path dependency** — Actual withdrawal timing and amounts matter; simplified models may miss this
4. **Correlation assumptions** — Asset class correlations may change during crises
5. **Does not model behavioral responses** — Real people may panic-sell or reduce spending irrationally
6. **Computation cost** — High-fidelity simulations with many variables are computationally expensive
7. **Garbage in, garbage out** — Results are only as good as input assumptions

## Best Practices for FIRE Monte Carlo

1. **Use at least 5,000 simulations** — 10,000+ for stable confidence intervals
2. **Test multiple scenarios** — Bull base, bear base, and custom stress cases
3. **Report percentile ranges, not just success rate** — The distribution matters, not just the binary outcome
4. **Combine with historical backtesting** — Monte Carlo and backtests complement each other
5. **Stress test inputs** — Run simulations with higher inflation, lower returns, and longer horizons
6. **Update annually** — Re-run simulations with current portfolio values and revised assumptions

## Relevance to FIRE Planning

Monte Carlo simulation provides the most comprehensive risk assessment for FIRE plans. It moves beyond simple "will it work?" questions to "how confident am I?" and "what's the worst realistic outcome?" For any FIRE plan, running a Monte Carlo simulation is essential to validate that the chosen withdrawal rate, portfolio allocation, and savings trajectory have a sufficient margin of safety.

---

*References: Portfolio Visualizer Monte Carlo; cFIREsim; ERN's Monte Carlo toolkit; Zvi Bodle "Quantitative Finance for Dummies"*
