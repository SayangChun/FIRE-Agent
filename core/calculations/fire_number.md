# FIRE Number

## Definition

The FIRE Number is the target investment portfolio value required to generate sufficient income to cover annual living expenses indefinitely, based on a specified safe withdrawal rate.

## Why It Matters

The FIRE Number is the foundational metric of the FIRE movement. It defines the finish line — the point at which investment returns alone can sustain your lifestyle without requiring employment income. Miscalculating this number leads to either working unnecessarily long or retiring prematurely and running out of money.

## Mathematical Framework

### Core Formula

```
FIRE Number = Annual Expenses / Safe Withdrawal Rate
```

Or equivalently:

```
FIRE Number = Annual Expenses × Years of Expenses Needed
```

The most common implementation uses the **4% rule**, derived from the Trinity Study:

```
FIRE Number = Annual Expenses × 25
```

### Sensitivity Analysis Across Withdrawal Rates

| Withdrawal Rate | Multiplier | Example ($40K/yr expenses) |
|-----------------|------------|---------------------------|
| 3.0%            | 33.33×     | $1,333,333                |
| 3.25%           | 30.77×     | $1,230,769                |
| 3.5%            | 28.57×     | $1,142,857                |
| 4.0%            | 25.00×     | $1,000,000                |
| 4.5%            | 22.22×     | $888,889                  |
| 5.0%            | 20.00×     | $800,000                  |

Lower withdrawal rates provide higher survival probability but require larger portfolios and longer accumulation periods.

### Adjusted FIRE Number (Inflation)

```
Adjusted FIRE Number = Base FIRE Number × (1 + inflation_rate)^years_to_FI
```

## Examples

### Conservative FIRE ($30K/year expenses)
```
At 3.5% withdrawal rate: $30,000 × 28.57 = $857,143
At 4.0% withdrawal rate: $30,000 × 25.00 = $750,000
```

### Moderate FIRE ($60K/year expenses)
```
At 3.5% withdrawal rate: $60,000 × 28.57 = $1,714,286
At 4.0% withdrawal rate: $60,000 × 25.00 = $1,500,000
```

### Fat FIRE ($120K/year expenses)
```
At 3.5% withdrawal rate: $120,000 × 28.57 = $3,428,571
At 4.0% withdrawal rate: $120,000 × 25.00 = $3,000,000
```

## Edge Cases

1. **Variable expenses**: Use a rolling 3-year average of essential expenses; exclude one-time purchases.
2. **Pre-retirement income needs**: Separate transition expenses from steady-state retirement expenses.
3. **Geographic arbitrage**: Calculate FIRE Number using the lower cost-of-living location, not current location.
4. **Debt-free vs. debt-carrying**: Include mortgage payments if the mortgage will persist into retirement; exclude if paid off.
5. **Children**: Plan for changing family size — education costs, health insurance tier changes, and dependent care.
6. **Healthcare**: Add estimated annual healthcare premiums and out-of-pocket costs (ACA plans, Medicare gap).

## Mitigation Strategies for FIRE Number Miscalculation

- Use conservative withdrawal rates (3.0–3.5%) for longer retirements (40+ years)
- Build in a 10–20% buffer above calculated FIRE Number
- Recalculate annually as expenses and life circumstances change
- Separate essential FIRE (bare minimum) from comfortable FIRE (desired lifestyle)

## Relevance to FIRE Planning

The FIRE Number is the primary target that all accumulation strategies, savings rate decisions, and investment allocations aim toward. Every other calculation in this system — savings rate, compound growth, withdrawal strategy — feeds into or derives from this number.

---

*References: Trinity Study (Cooley, Hubbard, Walz, 1998); BigERN (ERN) Safe Withdrawal Rate series; earlyretirementnow.com*
