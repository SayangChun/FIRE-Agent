# FIRE Agent User Guide

Complete guide to using FIRE Agent for your financial independence planning.

---

## Quick Start (5 Steps)

### Step 1: Choose Your Platform
Select where you want to use FIRE Agent:
- **ChatGPT** → [ChatGPT Setup Guide](chatgpt.md)
- **Gemini** → [Gemini Setup Guide](gemini.md)
- **Claude** → [Claude Setup](../adapters/claude/README.md)
- **Other Platform** → [Generic Setup](../adapters/generic/README.md)

### Step 2: Set Up the Agent
Follow your platform's setup guide to:
1. Create a Custom GPT, Gem, or Project
2. Paste the system prompt/instructions
3. Upload knowledge files (optional but recommended)
4. Enable code execution if available

### Step 3: Prepare Your Financial Data
Gather this information before your first conversation:
- Age and target retirement age
- Annual income (after tax)
- Annual expenses
- Current invested assets (stocks, bonds, ETFs, retirement accounts)
- Monthly savings/investment amount
- Any debts (mortgage, loans, credit cards)

### Step 4: Start a Conversation
Begin with a simple prompt:
```
Hello! I'd like to plan for financial independence. Can you help me
calculate my FIRE number and create a roadmap?
```

### Step 5: Follow the Workflow
FIRE Agent will guide you through a 15-step process:
1. Gather your financial information
2. Calculate your FIRE number
3. Analyze your current progress
4. Run scenario analyses
5. Identify risks
6. Create an actionable plan

---

## Platform-Specific Setup

### ChatGPT
See [ChatGPT Setup Guide](chatgpt.md) for detailed instructions on:
- Creating a Custom GPT
- Uploading knowledge files
- Enabling Code Interpreter
- Conversation starters

### Gemini
See [Gemini Setup Guide](gemini.md) for:
- Creating a Gem
- Configuring instructions
- Uploading knowledge files
- Usage tips

### Claude
See [Claude Setup](../adapters/claude/README.md) for:
- Creating a Project
- Setting custom instructions
- Uploading documents
- Enabling Artifacts

### Other Platforms
See [Generic Setup](../adapters/generic/README.md) for:
- Universal system prompt
- API deployment examples
- Open-source UI setup

---

## Using the Financial Profile Template

FIRE Agent provides a structured template for collecting your financial data.

### Template Location
```
templates/financial_profile.csv
```

### How to Use It

1. **Open the template** in any spreadsheet application (Excel, Google Sheets, Numbers)
2. **Fill in your values** in the `value` column
3. **Save as CSV** and upload to your AI platform, OR
4. **Copy the data** and paste it into your conversation

### Template Sections

| Section | Fields | Description |
|---------|--------|-------------|
| **Personal** | Age, target FIRE age, country, currency | Basic demographic information |
| **Income** | Monthly/annual income, growth rate | All post-tax income sources |
| **Expenses** | Monthly/annual expenses, retirement expenses | Current and projected spending |
| **Assets** | Cash, stocks, ETFs, bonds, crypto, real estate | All investable assets |
| **Liabilities** | Mortgage, consumer debt, other debts | Outstanding obligations |
| **Investment** | Monthly contribution, expected return, inflation, withdrawal rate | Investment assumptions |

### Example Profile

```csv
section,field,value,unit,notes
personal,age,30,years,Current age
personal,target_fire_age,45,years,Desired retirement age
income,annual,240000,CNY,Annual post-tax income
expenses,annual,96000,CNY,Annual living expenses
assets,stocks,100000,CNY,Individual stocks
assets,etf,80000,CNY,Index funds / ETFs
investment,monthly_contribution,10000,CNY,Monthly amount invested
```

---

## Uploading Financial Data

### Method 1: Direct Conversation
Simply type your financial information:
```
I'm 30 years old, earn $100,000/year after tax, spend $60,000/year,
and have $200,000 in index funds. I want to retire at 45.
```

### Method 2: Structured Format
Provide data in a clear structure:
```
Age: 35
Target FIRE age: 50
Annual income: $120,000
Annual expenses: $50,000
Current assets:
- 401k: $300,000
- Roth IRA: $50,000
- Taxable brokerage: $100,000
- Cash: $30,000
Monthly contribution: $3,000
```

### Method 3: Upload CSV Template
1. Download `templates/financial_profile.csv`
2. Fill in your values
3. Upload to your AI platform
4. Ask FIRE Agent to analyze the data

### Method 4: Upload Financial Documents
You can also upload:
- Bank statements (PDF)
- Investment account summaries
- Budget spreadsheets

---

## Interpreting Results

FIRE Agent provides several key metrics:

### FIRE Number
The portfolio size needed for financial independence.

**Example:** `$1,000,000` at 4% withdrawal rate = `$40,000` annual spending

### FIRE Progress
How far along you are toward your goal.

**Example:** `35%` means you have 35% of your target portfolio

### Savings Rate
Percentage of income you save/invest.

**Example:** `40%` savings rate means you save $40,000 on $100,000 income

### Years to FIRE
Estimated time until you reach financial independence.

**Example:** `12 years` from now

### Scenario Analysis
Comparison of different outcomes:

| Scenario | Return Rate | Years to FIRE | Probability |
|----------|-------------|---------------|-------------|
| Conservative | 4% | 18 years | 95% |
| Base | 7% | 12 years | 80% |
| Optimistic | 9% | 8 years | 60% |

### Risk Assessment
Identification of potential threats to your plan:
- Sequence-of-returns risk
- Inflation risk
- Healthcare cost risk
- Concentration risk
- Longevity risk

---

## Running Scenarios

Ask FIRE Agent to model different situations:

### Market Downturn
```
What happens if there's a 30% market crash in year 5?
How does that affect my FIRE timeline?
```

### Income Change
```
I might get a 20% raise next year. How does that impact my FIRE date?
What if I lose my job for 6 months?
```

### Expense Changes
```
We're planning to have kids. How does adding $15,000/year in childcare
expenses affect my FIRE plan?
```

### Early Social Security
```
Should I take Social Security at 62 or delay to 70?
Model both scenarios.
```

### Part-Time Work
```
I want to work part-time in early retirement earning $20,000/year.
How does that change my FIRE number?
```

---

## Common Questions

### "How accurate are the calculations?"
FIRE Agent uses mathematical formulas and Monte Carlo simulations. Results are estimates based on your inputs and assumptions. Actual outcomes will vary based on market conditions, life changes, and other factors.

### "Can I use this with ChatGPT free?"
Yes, but ChatGPT Plus is recommended for Custom GPTs and Code Interpreter. Free tier works with basic conversations.

### "Do I need API keys?"
No. The platform adapters (ChatGPT, Gemini, Claude) don't require API keys. Only API deployments need keys.

### "Is this financial advice?"
No. FIRE Agent is an analytical tool, not a licensed financial advisor. Always consult professionals for personalized advice.

### "How often should I update my profile?"
Update quarterly or whenever major financial changes occur (job change, inheritance, major purchase, etc.).

---

## Tips for Best Results

### 1. Be Specific with Numbers
**Good:** "I earn $85,000/year after tax, spend $42,000/year, and have $150,000 in index funds."

**Bad:** "I make decent money and save some of it."

### 2. Include All Assets
Don't forget:
- Retirement accounts (401k, IRA, Roth IRA)
- Taxable brokerage accounts
- Cash savings
- Real estate equity (if considering as investment)
- Other investments (bonds, crypto, etc.)

### 3. Be Honest About Expenses
Track your actual spending, not what you think you spend. Include:
- Fixed costs (rent/mortgage, insurance, utilities)
- Variable costs (groceries, gas, entertainment)
- Discretionary spending (travel, hobbies, dining out)

### 4. Ask Follow-Up Questions
After receiving your initial analysis:
- "What's the biggest risk to my plan?"
- "How can I reduce my FIRE number?"
- "What if I want to retire 5 years earlier?"
- "Show me the Monte Carlo simulation results"

### 5. Use the 15-Step Workflow
Let FIRE Agent guide you through the complete process. Don't skip steps — each builds on the previous one.

### 6. Enable Code Execution
For accurate calculations, ensure your platform has code execution enabled:
- **ChatGPT:** Code Interpreter
- **Claude:** Artifacts
- **Gemini:** Native Python execution

### 7. Save Your Results
Ask FIRE Agent to generate a complete report you can save:
```
Please generate a comprehensive FIRE report I can save for future reference.
Include all calculations, scenarios, risks, and recommendations.
```

### 8. Review Regularly
Schedule quarterly reviews to:
- Update your financial data
- Recalculate your FIRE number
- Adjust for life changes
- Track progress toward milestones

---

## Next Steps

- **[FAQ](faq.md)** — Answers to 20+ common questions
- **[ChatGPT Guide](chatgpt.md)** — Detailed ChatGPT setup
- **[Gemini Guide](gemini.md)** — Detailed Gemini setup
- **[Installation Guide](installation.md)** — Project setup and verification

---

## Need Help?

If you encounter issues:
1. Check the [FAQ](faq.md) for common solutions
2. Review your platform-specific setup guide
3. Ensure you're following the 15-step workflow
4. Verify your financial data is complete and accurate