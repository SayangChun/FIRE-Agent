# FIRE Agent — Frequently Asked Questions

Answers to 20+ common questions about FIRE Agent.

---

## General Questions

### 1. What is FIRE Agent?

FIRE Agent is an AI-powered financial independence planning assistant. It helps you calculate your FIRE (Financial Independence, Retire Early) number, run scenario analyses, identify risks, and create actionable plans to achieve financial independence.

FIRE Agent is not a licensed financial advisor — it's an analytical tool that performs calculations and surfaces insights based on your inputs.

### 2. Do I need API keys to use FIRE Agent?

**No.** The platform adapters (ChatGPT, Gemini, Claude) don't require API keys. You only need API keys if you're deploying FIRE Agent through a custom API integration.

### 3. Is this financial advice?

**No.** FIRE Agent is an analytical tool, not a licensed financial advisor, tax professional, or attorney. It performs calculations, models scenarios, and provides educational information. Always consult qualified professionals for personalized financial, tax, or legal advice.

### 4. How accurate are the calculations?

FIRE Agent uses mathematical formulas and Monte Carlo simulations for calculations. Results are estimates based on your inputs and assumptions. Actual outcomes will vary based on market conditions, life changes, inflation, and other factors. The calculations are as accurate as the formulas allow, but they're not guarantees of future performance.

---

## Technical Questions

### 5. Can I use this with ChatGPT free?

**Yes, but with limitations.** ChatGPT free tier works for basic conversations. However, ChatGPT Plus is recommended for:
- Custom GPTs (where FIRE Agent is set up)
- Code Interpreter (for accurate Python-based calculations)
- Better performance with complex analyses

### 6. Which AI platform should I use?

All platforms work well. Choose based on your preference:

| Platform | Strengths | Best For |
|----------|-----------|----------|
| **ChatGPT** | Widely used, Code Interpreter, Custom GPTs | Most users |
| **Gemini** | No character limit, native Python, free tier | Detailed analysis |
| **Claude** | Nuanced reasoning, structured output | Complex scenarios |
| **Generic** | Works anywhere, API-friendly | Developers |

### 7. How does Monte Carlo simulation work?

Monte Carlo simulation runs thousands of random market scenarios (typically 1,000-10,000 iterations) using your financial inputs. Each iteration assumes different market returns based on historical patterns. The simulation shows:
- **Success probability:** Percentage of scenarios where you don't run out of money
- **Range of outcomes:** Best case, worst case, and median results
- **Time horizons:** Success rates at different retirement ages

### 8. What is the 4% rule?

The 4% rule is a guideline suggesting you can safely withdraw 4% of your portfolio annually in retirement without running out of money over a 30-year period. It's based on historical market data.

**Example:** If you need $40,000/year in retirement, your FIRE number = $40,000 / 0.04 = $1,000,000.

FIRE Agent also supports other withdrawal rates (3%, 3.5%, 5%) for more conservative or aggressive planning.

---

## Financial Questions

### 9. Can I use this for tax planning?

FIRE Agent provides **general tax education** (e.g., Roth conversion concepts, tax-loss harvesting benefits, capital gains vs. income tax). However, it does **not** provide specific tax advice. Consult a tax professional for personalized tax planning.

### 10. How do I update my financial data?

**Option 1: Start a new conversation**
Begin fresh with your updated numbers.

**Option 2: Update in existing conversation**
```
I need to update my financial profile:
- New annual income: $110,000 (was $100,000)
- New portfolio value: $250,000 (was $200,000)
Please recalculate everything.
```

**Option 3: Upload updated CSV**
Update `templates/financial_profile.csv` with new values and upload.

### 11. What files can I upload?

FIRE Agent can process:
- **CSV files:** Financial profile templates, budget spreadsheets
- **PDF files:** Bank statements, investment summaries
- **Text files:** Financial notes, goals
- **Images:** Screenshots of financial dashboards (if your platform supports image analysis)

### 12. What if my income changes?

FIRE Agent can model income changes:
- **Raise:** "I'm getting a 15% raise next month. How does that affect my FIRE timeline?"
- **Job loss:** "What if I lose my job for 6 months? How does that impact my plan?"
- **Side income:** "I'm starting a side business earning $20,000/year. Update my analysis."

### 13. Can I track multiple income sources?

**Yes.** Provide all income sources in your profile:
```
Income sources:
- Primary job: $80,000/year
- Freelance work: $15,000/year
- Rental income: $12,000/year
- Investment dividends: $3,000/year
Total: $110,000/year
```

### 14. How do I handle stock options?

Provide the details:
```
Stock options:
- Company: TechCorp
- Vested shares: 1,000
- Strike price: $50
- Current market price: $120
- Vesting schedule: 25% annually
```

FIRE Agent can model different scenarios (exercise now, hold, sell gradually).

---

## Strategy Questions

### 15. What about international users?

FIRE Agent works for any country. When setting up:
1. Specify your country in the financial profile
2. Use your local currency
3. Adjust for local factors:
   - Tax rates and brackets
   - Social security/pension systems
   - Healthcare costs
   - Cost of living differences

The 4% rule and other FIRE principles are universal, but specific numbers will vary by country.

### 16. Can I use this for business finances?

FIRE Agent focuses on **personal** financial independence. For business finances:
- Separation of personal and business assets
- Business valuation considerations
- Owner's draw vs. salary
- Exit strategy planning

Consult a business financial advisor for company-specific planning.

### 17. How does inflation affect my FIRE plan?

FIRE Agent accounts for inflation in several ways:
- **Real returns:** Investment returns minus inflation
- **Inflation-adjusted FIRE number:** Your target grows with inflation
- **Purchasing power:** Future expenses in today's dollars

**Example:** With 3% inflation, $40,000/year today = $53,700/year in 10 years.

### 18. Can I use this for Coast FIRE or Barista FIRE?

**Yes.** FIRE Agent supports all FIRE types:
- **Lean FIRE:** Minimalist retirement (~$40,000/year)
- **Regular FIRE:** Comfortable retirement (~$60,000/year)
- **Fat FIRE:** Luxury retirement (~$100,000+/year)
- **Coast FIRE:** Save enough now, let compound interest work
- **Barista FIRE:** Partial retirement with part-time work

Just specify your target lifestyle when providing data.

---

## Practical Questions

### 19. How often should I update my profile?

**Recommended schedule:**
- **Quarterly:** Review and update all numbers
- **After major events:** Job change, inheritance, major purchase, marriage, divorce
- **Annually:** Comprehensive review with scenario updates
- **As needed:** When market conditions change significantly

### 20. Is my data safe?

**Your data stays with you.** FIRE Agent doesn't store your financial information permanently. Conversations are subject to your AI platform's privacy policy.

**Best practices:**
- Don't include sensitive identifiers (Social Security numbers, account numbers)
- Use general descriptions for accounts ("401k" not account numbers)
- Review your platform's data retention policies
- Delete conversations containing sensitive financial data

### 21. Can I share this with friends?

**Yes!** You can share:
- **ChatGPT:** Share your Custom GPT link
- **Gemini:** Share your Gem link
- **Claude:** Share your Project link
- **Generic:** Share the `system_prompt.md` file

Friends can set up their own FIRE Agent instance using the shared link or files.

### 22. What if I want to work part-time in retirement?

FIRE Agent can model part-time income:
```
I want to retire at 50 but work part-time earning $20,000/year
until age 60. How does that affect my FIRE number?
```

This reduces the portfolio needed since you're not fully self-funding from day one.

---

## Advanced Questions

### 23. Can I run multiple scenarios at once?

**Yes.** Ask FIRE Agent to compare scenarios:
```
Run three scenarios for me:
1. Conservative: 4% returns, retire at 55
2. Base: 7% returns, retire at 50
3. Optimistic: 9% returns, retire at 45
Compare the results.
```

### 24. How do I handle a partner's finances?

Provide both profiles:
```
My situation:
- Age: 35, Income: $100,000, Expenses: $45,000, Portfolio: $200,000

Partner's situation:
- Age: 33, Income: $80,000, Portfolio: $150,000

Combined:
- Joint expenses: $70,000/year
- Joint retirement target: $55,000/year
```

### 25. Can I customize the calculations?

**Yes.** You can adjust:
- Withdrawal rate (3%, 3.5%, 4%, 5%)
- Expected returns (conservative to aggressive)
- Inflation assumptions
- Monte Carlo iterations
- Retirement age targets

Just specify your preferences in the conversation.

---

## Still Have Questions?

- Review the [User Guide](user_guide.md) for detailed usage instructions
- Check platform-specific guides for setup help
- Start a conversation with FIRE Agent — it can answer questions about its own capabilities

---

## Quick Reference

| Question | Answer |
|----------|--------|
| What is FIRE Agent? | AI-powered financial independence planner |
| Do I need API keys? | No (unless using API deployment) |
| Is this financial advice? | No — analytical tool only |
| Can I use ChatGPT free? | Yes, but Plus recommended |
| How accurate are calculations? | As accurate as the formulas allow |
| Can I share with friends? | Yes — share the GPT/Gem/project link |
| Is my data safe? | Yes — stays with your platform |
| How often to update? | Quarterly or after major events |