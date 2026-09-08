# FIRE Analysis Report

**Generated:** {{report_date}}
**Client:** {{client_name}}
**Currency:** {{currency}}

---

## 1. Executive Summary

| Metric | Value |
|--------|-------|
| FIRE Number | {{fire_number}} |
| Current Net Worth | {{net_worth}} |
| FIRE Progress | {{fire_progress_pct}}% |
| Estimated FIRE Age | {{estimated_fire_age}} |
| Years to FIRE | {{years_to_fire}} |
| Required Savings Rate | {{required_savings_rate}} |

**FIRE Type:** {{fire_type}} — {{fire_type_description}}

---

## 2. Financial Profile

### Personal
| Field | Value |
|-------|-------|
| Age | {{age}} |
| Target FIRE Age | {{target_fire_age}} |
| Country | {{country}} |

### Income
| Field | Value |
|-------|-------|
| Monthly Income | {{monthly_income}} |
| Annual Income | {{annual_income}} |
| Income Growth Rate | {{income_growth_rate}} |

### Expenses
| Field | Value |
|-------|-------|
| Monthly Expenses | {{monthly_expenses}} |
| Annual Expenses | {{annual_expenses}} |
| Retirement Annual Expenses | {{retirement_annual_expenses}} |
| Retirement Expense Ratio | {{retirement_expense_ratio}} |

### Assets
| Category | Value |
|----------|-------|
| Cash | {{cash}} |
| Stocks | {{stocks}} |
| ETFs | {{etf}} |
| Bonds | {{bonds}} |
| Crypto | {{crypto}} |
| Real Estate | {{real_estate}} |
| Other | {{other_assets}} |
| **Total Assets** | **{{total_assets}}** |

### Liabilities
| Category | Value |
|----------|-------|
| Mortgage | {{mortgage}} |
| Consumer Debt | {{consumer_debt}} |
| Other | {{other_liabilities}} |
| **Total Liabilities** | **{{total_liabilities}}** |

### Net Worth
**{{net_worth}}** (Assets − Liabilities)

---

## 3. FIRE Number Analysis

The FIRE Number is the total investment assets needed to sustain retirement withdrawals indefinitely.

| Component | Value |
|-----------|-------|
| Annual Retirement Expenses | {{retirement_annual_expenses}} |
| Safe Withdrawal Rate | {{withdrawal_rate}} |
| Inflation-Adjusted Expenses | {{inflation_adjusted_expenses}} |
| **FIRE Number** | **{{fire_number}}** |
| FIRE Number (Inflation-Adj, {{years_to_fire}}yr) | {{fire_number_inflation_adj}} |

---

## 4. Current Progress

| Metric | Value |
|--------|-------|
| Current Investable Assets | {{investable_assets}} |
| FIRE Number | {{fire_number}} |
| Progress | {{fire_progress_pct}}% |
| Remaining Gap | {{fire_gap}} |
| Monthly Savings | {{monthly_savings}} |
| Annual Savings | {{annual_savings}} |

---

## 5. Savings Rate Analysis

| Metric | Value |
|--------|-------|
| Annual Income | {{annual_income}} |
| Annual Savings | {{annual_savings}} |
| Current Savings Rate | {{current_savings_rate_pct}}% |
| Required Savings Rate for Target Age | {{required_savings_rate_pct}}% |
| Savings Rate Gap | {{savings_rate_gap}} |

**Savings Rate Assessment:** {{savings_rate_assessment}}

---

## 6. Estimated FIRE Age

| Scenario | Estimated Age | Years to FIRE |
|----------|---------------|---------------|
| Conservative ({{conservative_return}}% return) | {{conservative_fire_age}} | {{conservative_years}} |
| Base Case ({{base_return}}% return) | {{base_fire_age}} | {{base_years}} |
| Optimistic ({{optimistic_return}}% return) | {{optimistic_fire_age}} | {{optimistic_years}} |

**Target:** {{target_fire_age}} ({{years_to_fire}} years from now)

---

## 7. Scenario Analysis

### Scenario: Savings Rate Change
| Change | New FIRE Age | Difference |
|--------|-------------|------------|
| +5% savings rate | {{sr_plus5_age}} | {{sr_plus5_diff}} |
| +10% savings rate | {{sr_plus10_age}} | {{sr_plus10_diff}} |
| −5% savings rate | {{sr_minus5_age}} | {{sr_minus5_diff}} |

### Scenario: Return Rate Change
| Return Rate | FIRE Number | FIRE Age |
|-------------|-------------|----------|
| 5% | {{return5_fire_number}} | {{return5_fire_age}} |
| 7% (base) | {{return7_fire_number}} | {{base_fire_age}} |
| 9% | {{return9_fire_number}} | {{return9_fire_age}} |
| 12% | {{return12_fire_number}} | {{return12_fire_age}} |

### Scenario: Expense Reduction
| Reduction | FIRE Number | FIRE Age |
|-----------|-------------|----------|
| −10% expenses | {{exp_minus10_fire_number}} | {{exp_minus10_fire_age}} |
| −20% expenses | {{exp_minus20_fire_number}} | {{exp_minus20_fire_age}} |
| −30% expenses (Lean FIRE) | {{exp_minus30_fire_number}} | {{exp_minus30_fire_age}} |

---

## 8. Monte Carlo Results

Based on {{monte_carlo_simulations}} simulations with random return sequences:

| Percentile | FIRE Age | Outcome |
|------------|----------|---------|
| 5th (worst) | {{mc_5th_age}} | {{mc_5th_outcome}} |
| 25th | {{mc_25th_age}} | {{mc_25th_outcome}} |
| 50th (median) | {{mc_50th_age}} | {{mc_50th_outcome}} |
| 75th | {{mc_75th_age}} | {{mc_75th_outcome}} |
| 95th (best) | {{mc_95th_age}} | {{mc_95th_outcome}} |

**Probability of reaching FIRE by target age ({{target_fire_age}}):** {{mc_success_rate}}%

---

## 9. FIRE Type Classification

**{{fire_type}}** — {{fire_type_description}}

| Type | Description | FIRE Number | Fits Profile? |
|------|-------------|-------------|---------------|
| Lean FIRE | Minimalist retirement, low expenses | {{lean_fire_number}} | {{lean_fits}} |
| Regular FIRE | Comfortable middle-class retirement | {{regular_fire_number}} | {{regular_fits}} |
| Fat FIRE | Luxury retirement, high expenses | {{fat_fire_number}} | {{fat_fits}} |
| Barista FIRE | Part-time work + reduced portfolio | {{barista_fire_number}} | {{barista_fits}} |

---

## 10. Risk Analysis

### Identified Risks
{{#risks}}
- **{{risk_category}}**: {{risk_description}} — Impact: {{risk_impact}}, Likelihood: {{risk_likelihood}}
{{/risks}}

### Risk Mitigation Recommendations
{{#risk_mitigations}}
- {{mitigation}}
{{/risk_mitigations}}

---

## 11. Trade-off Analysis

| Trade-off | Option A | Option B | Recommendation |
|-----------|----------|----------|----------------|
| Aggressive vs Conservative Investing | Higher expected return, more volatility | Lower return, more stability | {{investing_recommendation}} |
| Reduce Expenses vs Increase Income | Immediate savings boost | Long-term growth potential | {{income_expense_recommendation}} |
| Real Estate vs Liquid Assets | Rental income, leverage | Diversification, liquidity | {{asset_allocation_recommendation}} |
| Crypto Allocation | High potential return | Extreme volatility | {{crypto_recommendation}} |

---

## 12. Recommended Actions

### Priority 1: Immediate (0-3 months)
{{#immediate_actions}}
{{action_number}}. {{action_description}}
   - Expected impact: {{action_impact}}
{{/immediate_actions}}

### Priority 2: Short-term (3-12 months)
{{#short_term_actions}}
{{action_number}}. {{action_description}}
   - Expected impact: {{action_impact}}
{{/short_term_actions}}

### Priority 3: Long-term (1-5 years)
{{#long_term_actions}}
{{action_number}}. {{action_description}}
   - Expected impact: {{action_impact}}
{{/long_term_actions}}

---

## 13. Important Assumptions

| Assumption | Value | Notes |
|------------|-------|-------|
| Investment Return | {{expected_return}} | Nominal annual return |
| Inflation Rate | {{inflation_rate}} | Annual inflation assumption |
| Safe Withdrawal Rate | {{withdrawal_rate}} | Based on Trinity Study |
| Income Growth | {{income_growth_rate}} | Annual salary increase |
| Life Expectancy | {{life_expectancy}} | Portfolio depletion horizon |
| Tax Rate | {{tax_rate}} | Applied to investment gains |
| Healthcare Costs | {{healthcare_assumption}} | Post-retirement medical expenses |

---

## 14. Disclaimer

This analysis is for informational and educational purposes only. It does not constitute financial advice. The projections are based on historical data and assumptions that may not reflect future conditions. Investment returns are not guaranteed, and past performance does not predict future results. Inflation, market volatility, tax law changes, and personal circumstances can significantly affect outcomes.

Please consult a licensed financial advisor before making any investment decisions. The author assumes no liability for financial losses based on this analysis.

---

*Report generated by FIRE Agent*
