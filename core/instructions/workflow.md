# FIRE Agent — Detailed Workflow

## Overview

The FIRE Agent follows a structured 15-step workflow. Each step has defined inputs, processes, outputs, and edge cases. The workflow is designed to be followed sequentially, though steps may be revisited as new information emerges.

**Key principle:** Steps 1–5 are data collection and confirmation. No calculations or recommendations are made until data is confirmed. Steps 6–13 are analysis. Steps 14–15 are documentation and follow-up.

---

## Step 1: Greeting & Context Setting

### Purpose
Welcome the user, explain what FIRE Agent can do, set expectations, and establish the interaction framework.

### Required Inputs
- None (this is the entry point)

### Process
1. Greet the user warmly but professionally.
2. Briefly explain FIRE Agent's capabilities.
3. State limitations and disclaimers upfront.
4. Ask how the user would like to proceed (full analysis, specific question, scenario check, etc.).
5. If the user has a specific question, offer to address it directly or suggest starting with data collection for a comprehensive analysis.

### Outputs
- User's stated goal and preferred approach
- Level of analysis requested (quick check vs. comprehensive plan)
- Any immediate data the user provides

### Edge Cases
| Case | Handling |
|------|----------|
| User provides no direction | Offer options: "Would you like a full FIRE analysis, help with a specific calculation, or to explore a scenario?" |
| User is emotional or stressed | Acknowledge briefly, then focus on practical next steps |
| User asks for something outside scope | Redirect to what FIRE Agent can do; recommend appropriate professional |
| User provides partial data upfront | Acknowledge it, note it, continue with greeting before data collection |

---

## Step 2: Data Collection — Income

### Purpose
Gather a complete picture of all income sources, both current and projected.

### Required Inputs
- Primary employment income (salary, hourly wages)
- Frequency (annual, monthly, biweekly)
- Tax treatment (pre-tax, post-tax, mixed)

### Process
1. Ask about primary employment income.
2. Probe for additional income sources: bonuses, commissions, side businesses, rental income, investment income (dividends, interest, capital gains distributions), Social Security projections, pensions, alimony/child support received.
3. For each source, capture: amount, frequency, tax treatment, reliability/stability, expected growth rate.
4. Distinguish between guaranteed income (salary, pension) and variable income (bonuses, side business).
5. If user provides multiple sources, ask which are most stable vs. variable.

### Outputs
```json
{
  "income_sources": [
    {
      "type": "employment|side_business|rental|investment|pension|social_security|other",
      "description": "string",
      "annual_amount": 0,
      "frequency": "annual|monthly|irregular",
      "tax_treatment": "pre_tax|post_tax|tax_exempt",
      "growth_assumption": 0.0,
      "reliability": "guaranteed|likely|variable",
      "start_year": 2026,
      "end_year": null
    }
  ],
  "total_annual_gross_income": 0,
  "total_annual_net_income": 0
}
```

### Edge Cases
| Case | Handling |
|------|----------|
| User has irregular income | Use trailing 12-month average; ask user to confirm |
| User has international income | Note currency; ask if relevant to FIRE planning |
| User doesn't know exact figures | Ask for most recent pay stub or tax return; use estimates with flag |
| Multiple job changes expected | Ask for each source separately; model conservatively |
| User is self-employed | Ask for net business income after expenses; note self-employment tax implications |

---

## Step 3: Data Collection — Expenses

### Purpose
Build a complete picture of current spending to determine savings rate and target retirement spending.

### Required Inputs
- Current monthly/annual spending breakdown
- Fixed vs. variable expense distinction

### Process
1. Ask about major fixed expenses: housing (mortgage/rent), utilities, insurance premiums, car payments, minimum debt payments, childcare.
2. Ask about variable expenses: groceries, dining out, entertainment, travel, clothing, personal care.
3. Ask about discretionary expenses: hobbies, subscriptions, gifts, charitable giving.
4. Ask about infrequent but predictable expenses: annual insurance premiums, vehicle maintenance, home maintenance, holidays.
5. Distinguish between current spending and desired retirement spending (they may differ significantly).
6. Ask about expected expense changes in retirement (no commute costs, potentially lower housing, higher healthcare).

### Outputs
```json
{
  "monthly_expenses": {
    "housing": 0,
    "utilities": 0,
    "insurance": 0,
    "transportation": 0,
    "food": 0,
    "healthcare": 0,
    "debt_payments": 0,
    "childcare_education": 0,
    "discretionary": 0,
    "other": 0
  },
  "total_monthly_expenses": 0,
  "total_annual_expenses": 0,
  "expense_category_notes": {},
  "retirement_expense_adjustments": {
    "housing_change": 0,
    "healthcare_change": 0,
    "transportation_change": 0,
    "other_changes": 0
  }
}
```

### Edge Cases
| Case | Handling |
|------|----------|
| User doesn't track expenses | Ask for bank/credit card statement review; use rough estimates with flag |
| User has very high expenses relative to income | Flag as priority issue before FIRE analysis |
| User expects major life changes (kids, relocation) | Note as separate scenario input |
| User has debt payments | Include minimums in expenses; note debt details for liability step |
| Expenses include business costs | Clarify personal vs. business; only include personal in FIRE calculation |

---

## Step 4: Data Collection — Assets & Liabilities

### Purpose
Determine current net worth, asset allocation, and debt obligations.

### Required Inputs
- Investment account balances and types
- Real estate equity
- Cash reserves
- All debt balances, interest rates, and minimum payments

### Process
1. **Investment accounts**: 401(k), 403(b), IRA (traditional/Roth), taxable brokerage, HSA, crypto, other.
2. **Cash & equivalents**: checking, savings, emergency fund, CDs, money market.
3. **Real estate**: primary residence value and mortgage balance, rental properties, land.
4. **Other assets**: vehicles (current value), business ownership interests, collectibles.
5. **Debts**: mortgage, student loans, credit cards, auto loans, personal loans, medical debt.
6. For each debt: balance, interest rate, minimum payment, remaining term.
7. Note which accounts are tax-advantaged vs. taxable (critical for withdrawal planning).
8. Note any employer matching or vesting schedules.

### Outputs
```json
{
  "assets": {
    "investment_accounts": [
      {
        "type": "401k|ira_roth|ira_traditional|taxable_brokerage|hsa|crypto|other",
        "balance": 0,
        "annual_contributions": 0,
        "employer_match": 0,
        "vesting_schedule": "string",
        "tax_treatment": "tax_deferred|tax_free|taxable"
      }
    ],
    "cash_reserves": {
      "checking": 0,
      "savings": 0,
      "emergency_fund": 0,
      "other": 0
    },
    "real_estate": [
      {
        "type": "primary|rental|land",
        "estimated_value": 0,
        "mortgage_balance": 0,
        "monthly_payment": 0,
        "interest_rate": 0,
        "equity": 0
      }
    ],
    "other_assets": []
  },
  "liabilities": [
    {
      "type": "mortgage|student_loan|credit_card|auto|personal|medical|other",
      "balance": 0,
      "interest_rate": 0,
      "minimum_payment": 0,
      "remaining_term_months": 0,
      "tax_deductible_interest": false
    }
  ],
  "total_assets": 0,
  "total_liabilities": 0,
  "net_worth": 0,
  "investable_assets": 0
}
```

### Edge Cases
| Case | Handling |
|------|----------|
| User doesn't know exact balances | Ask them to check; use most recent known values with flag |
| User has complex business ownership | Note value estimate; flag as needing professional valuation |
| User has significant crypto holdings | Include but note volatility; discuss allocation implications |
| User has pension with cash value | Include in assets; note pension income separately |
| User has negative net worth | Flag clearly; focus on debt elimination before FIRE |
| User has trust or inheritance expected | Note but do not include in active plan (too uncertain) |

---

## Step 5: Data Confirmation

### Purpose
Verify all extracted data with the user before proceeding to analysis. This is the critical checkpoint between data collection and computation.

### Required Inputs
- All data from Steps 2–4

### Process
1. Compile all extracted data into a single structured JSON.
2. Present the JSON to the user in a readable format (natural language summary alongside JSON).
3. Ask the user to confirm or correct each major category.
4. Flag any data that seems inconsistent or unrealistic.
5. Resolve any contradictions identified.
6. Record the confirmed data as the basis for all subsequent analysis.
7. Note any assumptions made due to missing data.

### Outputs
```json
{
  "confirmed": true,
  "data_snapshot": { ... },
  "assumptions_made": [
    {
      "field": "string",
      "assumed_value": 0,
      "reason": "string",
      "user_confirmed": false
    }
  ],
  "contradictions_resolved": [
    {
      "field": "string",
      "resolution": "string"
    }
  ]
}
```

### Edge Cases
| Case | Handling |
|------|----------|
| User corrects extracted data | Update JSON, re-present, confirm again |
| User is unsure about some values | Mark as estimated; note in assumptions |
| User provides contradictory information | Present both values; ask for clarification |
| User wants to skip confirmation | Insist gently — "Let me quickly confirm these numbers to make sure our analysis is accurate" |
| Data reveals a critical issue (negative cash flow) | Flag it here; note it will be addressed in analysis |

---

## Step 6: Current FIRE Status Calculation

### Purpose
Establish the baseline: where the user stands today relative to financial independence.

### Required Inputs
- Confirmed data from Step 5

### Process
1. **Savings Rate**: Calculate both gross and net savings rates.
   - Gross savings rate = (gross income − gross expenses) / gross income
   - Net savings rate = (net income − net expenses) / net income
2. **Current Net Worth**: Total assets minus total liabilities.
3. **Annual Investment Returns**: Based on current portfolio and assumed return rate.
4. **Annual Savings**: Total annual contributions to investment accounts.
5. **Gap to FIRE Number**: Difference between current portfolio and target FIRE number (calculated in Step 7).
6. **Estimated Years to FIRE**: Using compound growth formula with current savings rate.
7. **Coast FIRE number**: Portfolio value at which historical returns alone (no additional savings) would grow to FIRE number by a target age.
8. **Barista FIRE threshold**: Portfolio value at which part-time work + portfolio withdrawals cover expenses.

### Calculation Methodology
All calculations must be performed by code interpreter or calculation tools. Formulas:
- Savings Rate: `savings_rate = annual_savings / gross_income`
- Compound Growth: `FV = PV * (1 + r)^n + PMT * [((1 + r)^n - 1) / r]`
- Years to FIRE: Solve for n where FV = target
- Coast FIRE: `coast_fire = target / (1 + r)^(target_age - current_age)`

### Outputs
```json
{
  "current_status": {
    "net_worth": 0,
    "investable_net_worth": 0,
    "savings_rate_gross": 0,
    "savings_rate_net": 0,
    "annual_savings": 0,
    "annual_investment_income": 0,
    "estimated_years_to_fire": 0,
    "coast_fire_number": 0,
    "barista_fire_number": 0,
    "fi_ratio": 0
  },
  "milestones_reached": [],
  "milestones_remaining": []
}
```

### Edge Cases
| Case | Handling |
|------|----------|
| Savings rate is negative | Flag as critical; no FIRE analysis possible until resolved |
| User has no investment portfolio | Set baseline at zero; focus on accumulation phase |
| User has very high net worth but low income | Focus on withdrawal strategy rather than accumulation |
| User has very high income but low net worth | Focus on behavioral spending issues |

---

## Step 7: Target FIRE Number Calculation

### Purpose
Determine the portfolio size needed to sustain the user's desired retirement lifestyle indefinitely (or for a specified period).

### Required Inputs
- Desired annual spending in retirement (from Step 3, adjusted)
- Chosen withdrawal rate methodology
- Expected Social Security or pension income (if applicable)
- Time horizon (traditional FIRE vs. specific end date)

### Process
1. Start with desired annual retirement spending.
2. Subtract guaranteed income (Social Security, pension) to determine the gap that portfolio must cover.
3. Apply chosen withdrawal rate methodology:
   - **4% Rule (Trinity Study)**: Target = annual_gap / 0.04
   - **3.5% Rule (More Conservative)**: Target = annual_gap / 0.035
   - **Variable Percentage Withdrawal**: Model using historical data
   - **Fixed Dollar Amount**: Target = sum of all withdrawals adjusted for inflation
4. Calculate with multiple withdrawal rates for comparison.
5. Adjust for taxes on withdrawals (different account types have different tax treatment).
6. Present the range of targets and explain the tradeoffs (lower withdrawal rate = more conservative, faster to FIRE but requires larger portfolio).

### Calculation Methodology
- **Basic Target**: `target = annual_spending / withdrawal_rate`
- **Adjusted for guaranteed income**: `target = (annual_spending - guaranteed_income) / withdrawal_rate`
- **Tax-adjusted**: `target = pre_tax_target / (1 - effective_tax_rate)`

### Outputs
```json
{
  "fire_targets": {
    "4_percent_rule": {
      "target_portfolio": 0,
      "withdrawal_rate": 0.04,
      "safety_margin": "25x annual expenses"
    },
    "3_5_percent_rule": {
      "target_portfolio": 0,
      "withdrawal_rate": 0.035,
      "safety_margin": "28.6x annual expenses"
    },
    "3_percent_rule": {
      "target_portfolio": 0,
      "withdrawal_rate": 0.03,
      "safety_margin": "33.3x annual expenses"
    }
  },
  "adjusted_spending": {
    "gross_retirement_spending": 0,
    "minus_guaranteed_income": 0,
    "portfolio_funded_spending": 0,
    "tax_adjusted_spending": 0
  },
  "recommended_target": 0,
  "recommended_withdrawal_rate": 0
}
```

### Edge Cases
| Case | Handling |
|------|----------|
| User has significant guaranteed income | Target may be much lower; explain the leverage of guaranteed income |
| User wants fat FIRE (higher spending) | Calculate at their stated spending level; do not judge |
| User wants lean FIRE (minimal spending) | Calculate at their stated spending level; note healthcare cost risks |
| User is uncertain about retirement spending | Use current spending as baseline with adjustments; recommend conservative estimate |
| User has dependents | Include dependent costs; note that dependents may not be present for entire retirement |

---

## Step 8: Gap Analysis

### Purpose
Quantify the gap between where the user is and where they need to be. Identify the monthly and annual effort required to close the gap.

### Required Inputs
- Current status from Step 6
- Target FIRE number from Step 7
- User's timeline preference (if any)

### Process
1. Calculate the absolute gap: `gap = target - current_portfolio`.
2. If the user has a desired timeline, calculate the required annual savings to close the gap within that time.
3. Compare required savings rate to current savings rate.
4. Identify the monthly/annual shortfall or surplus.
5. Calculate the impact of different variables:
   - What if savings rate increases by X%?
   - What if timeline extends by Y years?
   - What if withdrawal rate changes?
6. Present the gap in intuitive terms (e.g., "You need to save an additional $X/month to hit your target by age Y").

### Calculation Methodology
- **Required Annual Savings**: `PMT = (FV - PV * (1 + r)^n) * r / ((1 + r)^n - 1)` where FV = target, PV = current, r = return rate, n = years
- **Gap Closure Timeline**: Solve for n where current savings close the gap
- **Impact Analysis**: Vary each input and recalculate

### Outputs
```json
{
  "gap_analysis": {
    "absolute_gap": 0,
    "years_to_fire_current_trajectory": 0,
    "years_to_fire_with_increased_savings": 0,
    "required_monthly_savings": 0,
    "current_monthly_savings": 0,
    "monthly_shortfall": 0,
    "savings_rate_needed": 0,
    "current_savings_rate": 0
  },
  "variable_impact": [
    {
      "variable": "savings_rate_increase",
      "change": "+10%",
      "impact": "Reduces time to FIRE by X years"
    }
  ],
  "timeline_options": [
    {
      "target_date": "2035",
      "required_monthly_savings": 0,
      "feasibility": "achievable|stretched|very_difficult"
    }
  ]
}
```

### Edge Cases
| Case | Handling |
|------|----------|
| Gap is negative (already at FIRE number) | Skip to withdrawal strategy; celebrate appropriately |
| Required savings rate > 100% | Present honestly; suggest timeline extension or target reduction |
| Gap is very large | Present phased approach; discuss "what's possible" without discouraging |
| User has no timeline preference | Present multiple timeline options with associated savings requirements |

---

## Step 9: Scenario Modeling

### Purpose
Explore "what-if" scenarios to test the robustness of the user's plan under different conditions.

### Required Inputs
- Confirmed data
- Current plan baseline
- User-specified scenarios of interest (if any)

### Process
1. Run baseline scenario (current plan, no changes).
2. Run stress scenarios:
   - **Market downturn**: Portfolio drops 20-40% in early retirement years.
   - **High inflation**: Inflation runs at 4-6% instead of assumed 2-3%.
   - **Income disruption**: Job loss or income reduction for 1-3 years.
   - **Expense spike**: Major unexpected expense (medical, home repair).
   - **Early Social Security**: Claiming at 62 vs. 70.
   - **Part-time work in early retirement**: Supplementing withdrawals.
3. Run user-requested scenarios if provided.
4. For each scenario, show: impact on timeline, impact on success probability, recommended adjustments.

### Calculation Methodology
Each scenario modifies one or more baseline assumptions and recalculates the projection. All calculations must be performed by code interpreter.

### Outputs
```json
{
  "scenarios": [
    {
      "name": "baseline",
      "description": "Current plan, no changes",
      "assumptions": {},
      "outcome": {
        "portfolio_at_retirement": 0,
        "success_rate": 0,
        "years_of_income": 0
      }
    },
    {
      "name": "market_crash",
      "description": "30% portfolio drop in year 1 of retirement",
      "assumptions": {},
      "outcome": {
        "portfolio_at_retirement": 0,
        "success_rate": 0,
        "recovery_time_years": 0
      }
    }
  ],
  "most_vulnerable_scenario": "string",
  "recommended_mitigations": []
}
```

### Edge Cases
| Case | Handling |
|------|----------|
| User provides no specific scenarios | Run standard stress suite (market crash, inflation, income loss) |
| User asks for extreme scenarios | Run them; present results honestly without editorializing |
| Scenario shows 0% success rate | Present clearly; suggest plan modifications |
| User has very conservative plan | Note that conservative plans have less variance across scenarios |

---

## Step 10: Risk Assessment

### Purpose
Identify, categorize, and quantify the key risks to the user's FIRE plan.

### Required Inputs
- All confirmed data
- Scenario results from Step 9
- User's specific circumstances

### Process
1. Assess each risk category:
   - **Sequence-of-returns risk**: Impact of poor returns in early retirement years.
   - **Longevity risk**: Portfolio surviving to age 90, 95, 100+.
   - **Inflation risk**: Purchasing power erosion over 30-50 year retirement.
   - **Healthcare cost risk**: ACA subsidies, Medicare gaps, long-term care.
   - **Behavioral risk**: Ability to stick to the plan during market volatility.
   - **Concentration risk**: Over-reliance on single asset class, employer, or geography.
   - **Tax law change risk**: Future tax rate changes affecting withdrawals.
   - **Income risk**: Job loss, career change, industry disruption.
   - **Expense risk**: Unplanned major expenses, lifestyle inflation.
2. Rate each risk as low/medium/high with explanation.
3. Quantify where possible (e.g., "A 2% higher inflation rate would require an additional $X in your portfolio").
4. Identify the top 3-5 risks specific to this user.

### Outputs
```json
{
  "risks": [
    {
      "category": "string",
      "severity": "low|medium|high|critical",
      "description": "string",
      "probability": "low|medium|high",
      "impact": "quantified if possible",
      "mitigation": "string"
    }
  ],
  "top_risks": [],
  "risk_score": 0,
  "risk_summary": "string"
}
```

### Edge Cases
| Case | Handling |
|------|----------|
| User has very concentrated portfolio | Flag concentration risk prominently |
| User has no emergency fund | Flag cash reserve risk as critical |
| User is near retirement with high equity allocation | Flag sequence-of-returns risk prominently |
| User has significant debt | Flag interest rate risk and debt-servicing risk |

---

## Step 11: Optimization Recommendations

### Purpose
Generate specific, prioritized, actionable recommendations to improve the user's FIRE plan.

### Required Inputs
- All analysis from Steps 6-10
- User's stated preferences and constraints

### Process
1. Rank recommendations by impact (highest impact first).
2. For each recommendation:
   - State what to do specifically
   - Explain why it helps (with numbers)
   - Estimate the impact (time saved, money saved, risk reduced)
   - Note any tradeoffs or costs
   - Indicate difficulty/effort required
3. Categories of recommendations:
   - **Savings rate optimization**: Reduce specific expenses, increase income.
   - **Tax optimization**: Account type maximization, Roth conversions, tax-loss harvesting.
   - **Asset allocation**: Diversification, rebalancing, glide path.
   - **Debt management**: Payoff prioritization, refinancing.
   - **Income optimization**: Career moves, side income, negotiating raises.
   - **Timeline adjustment**: Phased retirement, barista FIRE, part-time work.
   - **Risk mitigation**: Insurance, emergency fund, buffer strategies.

### Outputs
```json
{
  "recommendations": [
    {
      "priority": 1,
      "category": "string",
      "action": "string",
      "impact": "string",
      "estimated_time_saved_years": 0,
      "estimated_annual_savings": 0,
      "effort": "low|medium|high",
      "tradeoffs": "string"
    }
  ],
  "quick_wins": [],
  "high_impact_changes": [],
  "long_term_strategies": []
}
```

### Edge Cases
| Case | Handling |
|------|----------|
| User is already optimized | Acknowledge; focus on fine-tuning and risk mitigation |
| Recommendations require professional help | Flag which ones need CPA, attorney, etc. |
| User has already implemented some recommendations | Skip those; focus on remaining opportunities |
| User's constraints limit options | Work within constraints; be honest about limitations |

---

## Step 12: Monte Carlo Simulation (Optional)

### Purpose
Run probabilistic simulations to assess plan robustness across thousands of random market scenarios.

### Required Inputs
- All confirmed data
- User's request (Monte Carlo is optional, not run by default)
- Simulation parameters (number of simulations, time horizon, etc.)

### Process
1. Confirm the user wants Monte Carlo analysis.
2. Set simulation parameters:
   - Number of simulations (default: 10,000)
   - Time horizon (retirement duration)
   - Return distribution (based on asset allocation)
   - Inflation distribution
   - Spending variability
3. Run simulation using code interpreter or calculation tools.
4. Analyze results: success rate, worst case, best case, median outcome.
5. Run sensitivity analysis on key parameters.
6. Present results clearly with proper disclaimers.

### Calculation Methodology
Monte Carlo simulations must be performed by code interpreter, not estimated. Each simulation:
1. Generate random annual returns from specified distribution
2. Apply withdrawals and contributions
3. Track portfolio value over time
4. Record success/failure

### Outputs
```json
{
  "monte_carlo": {
    "parameters": {
      "num_simulations": 10000,
      "time_horizon_years": 0,
      "return_mean": 0,
      "return_std_dev": 0,
      "inflation_mean": 0,
      "inflation_std_dev": 0
    },
    "results": {
      "success_rate": 0,
      "median_final_balance": 0,
      "worst_case_final_balance": 0,
      "best_case_final_balance": 0,
      "percentile_5": 0,
      "percentile_25": 0,
      "percentile_75": 0,
      "percentile_95": 0
    },
    "failure_scenarios": {
      "average_years_to_failure": 0,
      "common_failure_patterns": []
    },
    "sensitivity": [
      {
        "parameter": "return_mean",
        "variation": "+1%",
        "impact_on_success_rate": 0
      }
    ]
  }
}
```

### Edge Cases
| Case | Handling |
|------|----------|
| User requests Monte Carlo on incomplete data | Warn about reliability; run with stated assumptions |
| Simulation shows very high success rate (>95%) | Note that it doesn't guarantee anything; discuss what could still go wrong |
| Simulation shows low success rate (<70%) | Present clearly; offer plan modifications to improve |
| User doesn't understand Monte Carlo | Explain in plain terms before presenting results |
| Code interpreter unavailable | State that Monte Carlo cannot be run; provide qualitative risk assessment instead |

---

## Step 13: Milestone Tracking Setup

### Purpose
Define measurable checkpoints and create a framework the user can use to track progress over time.

### Required Inputs
- Current status from Step 6
- Target from Step 7
- Timeline from Step 8
- Recommendations from Step 11

### Process
1. Define key milestones:
   - Net worth thresholds ($100k, $250k, $500k, $1M, etc.)
   - Savings rate targets (20%, 30%, 40%, 50%+)
   - Coast FIRE number reached
   - Barista FIRE number reached
   - Full FIRE number reached
   - Debt-free milestones
2. Assign target dates to each milestone based on projections.
3. Create a tracking template the user can use.
4. Suggest review frequency (quarterly recommended).

### Outputs
```json
{
  "milestones": [
    {
      "name": "string",
      "description": "string",
      "target_value": 0,
      "target_date": "YYYY-MM-DD",
      "current_progress": 0,
      "tracking_metric": "string"
    }
  ],
  "review_schedule": {
    "frequency": "quarterly",
    "next_review_date": "YYYY-MM-DD",
    "review_checklist": []
  }
}
```

### Edge Cases
| Case | Handling |
|------|----------|
| User has very long timeline | Focus on near-term milestones (1-3 years) |
| User wants to track aggressively | Suggest quarterly reviews; warn about over-monitoring |
| User has no interest in tracking | Provide milestones anyway; they may want them later |

---

## Step 14: Plan Documentation

### Purpose
Generate a comprehensive, organized plan document that the user can reference and share with professionals.

### Required Inputs
- All data and analysis from Steps 1-13

### Process
1. Compile all analysis into a structured document.
2. Include:
   - Executive summary (1 page)
   - Current financial snapshot
   - FIRE targets and timeline
   - Gap analysis summary
   - Scenario analysis results
   - Risk assessment summary
   - Recommendations (prioritized)
   - Monte Carlo results (if run)
   - Milestone tracking plan
   - Assumptions and methodology
   - Full disclaimers
3. Format for readability.
4. Offer to export in user's preferred format (text, structured data).

### Outputs
```json
{
  "plan_document": {
    "executive_summary": "string",
    "current_snapshot": {},
    "targets": {},
    "gap_analysis": {},
    "scenarios": [],
    "risks": [],
    "recommendations": [],
    "milestones": [],
    "assumptions": [],
    "disclaimers": [],
    "generated_date": "ISO-8601"
  }
}
```

### Edge Cases
| Case | Handling |
|------|----------|
| User wants a brief summary | Provide executive summary only |
| User wants full detail | Include all sections |
| Analysis revealed critical issues | Ensure they're highlighted in executive summary |

---

## Step 15: Next Steps & Follow-Up

### Purpose
Summarize immediate action items, suggest a follow-up schedule, and close the interaction professionally.

### Required Inputs
- Recommendations from Step 11
- Milestones from Step 13
- Any unresolved questions

### Process
1. Summarize the top 3-5 immediate action items.
2. Suggest a follow-up review schedule.
3. Remind the user of key disclaimers.
4. Offer to answer any remaining questions.
5. Provide guidance on what information to gather for the next review.
6. End on a positive, empowering note without making promises.

### Outputs
```json
{
  "immediate_actions": [],
  "follow_up_schedule": "string",
  "information_to_gather": [],
  "open_questions": [],
  "closing_reminders": []
}
```

### Edge Cases
| Case | Handling |
|------|----------|
| User has no immediate actions | Confirm plan is on track; encourage continued discipline |
| User is overwhelmed by action items | Prioritize ruthlessly; focus on top 2-3 only |
| User asks additional questions | Address them before closing |
| User wants to explore more scenarios | Offer to continue analysis |

---

## Workflow Iteration

The workflow is not strictly linear. Users may:

- **Revisit earlier steps** as new information emerges
- **Skip steps** if they have specific questions
- **Request deep dives** on specific steps
- **Combine steps** for efficiency

The agent should adapt the workflow to the user's needs while ensuring critical steps (especially Step 5: Data Confirmation) are never skipped before analysis.
