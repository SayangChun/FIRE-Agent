# FIRE Agent — Gemini Gems Setup Guide

Step-by-step instructions to deploy FIRE Agent as a Gemini Gem.

---

## Prerequisites

- Google account with Gemini access (gemini.google.com)
- Gemini Advanced subscription recommended for best results
- The files in the `adapters/gemini/` folder

---

## Step 1: Create a New Gem

1. Go to [gemini.google.com](https://gemini.google.com)
2. Click **"Gems"** in the left sidebar (or navigate to gemini.google.com/gems)
3. Click **"+"** or **"Create new Gem"**
4. You'll see the Gem editor with fields for Name, Instructions, and Knowledge

---

## Step 2: Configure Basic Settings

| Field | Value |
|-------|-------|
| **Name** | `FIRE Agent` |
| **Instructions** | *(See `instructions.md` — paste the full contents)* |
| **Knowledge** | *(Upload files — see Step 4)* |

---

## Step 3: Add Instructions

1. Open `instructions.md` in the `adapters/gemini/` folder
2. Copy the **entire contents**
3. Paste into the **Instructions** field in the Gem editor

### Gemini-Specific Formatting Notes

- Gemini Gems support markdown in instructions — keep markdown formatting
- Gemini does NOT have a hard character limit on instructions like ChatGPT
- Gemini handles long system prompts well — no need to trim
- Use `###` headings for structure
- Code blocks and JSON blocks render correctly
- Gemini can execute Python code natively — no special capability toggle needed

> **Tip:** Gemini is particularly good at handling multi-step workflows. The 15-step workflow in the instructions works well without modification.

---

## Step 4: Upload Knowledge Files

In the Gem editor, under **Knowledge**:

1. Click **"Upload files"** or drag-and-drop
2. Upload the knowledge files listed in `knowledge_files.md`
3. Supported formats: `.txt`, `.pdf`, `.csv`, `.docx`, `.md`

### Knowledge File Checklist

| # | File | Purpose |
|---|------|---------|
| 1 | `fire_formulas.txt` | Core FIRE math formulas |
| 2 | `risk_framework.txt` | 8 risk categories and mitigations |
| 3 | `scenario_templates.txt` | Conservative/Base/Optimistic parameters |
| 4 | `fire_types.txt` | FIRE type definitions |
| 5 | `monte_carlo_method.txt` | Simulation methodology |

> **Gemini Knowledge Limit:** Gemini Gems can reference uploaded files, but the exact file count limit may vary. Start with the 5 core files above.

---

## Step 5: Test the Gem

1. Click **"Save"** to save the Gem
2. Open a new Gemini chat
3. Select your FIRE Agent Gem from the Gems list
4. Test with these scenarios:

### Test Case 1: Basic FIRE Number
```
I'm 35, earn $120,000/year after tax, spend $50,000/year,
and have $300,000 invested. Calculate my FIRE number and progress.
```

**Expected Result:** FIRE Agent should calculate:
- FIRE number = $50,000 / 0.04 = $1,250,000
- Progress = $300,000 / $1,250,000 = 24%
- Years to FIRE based on savings rate and returns

### Test Case 2: Full Analysis
```
Run a complete FIRE analysis for me. I want to retire at 45.
My current portfolio is $500,000, I save $40,000/year,
and expect to spend $60,000/year in retirement.
```

**Expected Result:** Complete 15-step workflow with all calculations, scenarios, risks, and recommendations.

### Test Case 3: Risk Analysis
```
What are the biggest risks to my FIRE plan?
I'm 90% in US stocks with no bonds or real estate.
```

**Expected Result:** Identification of concentration risk, lack of diversification, and sequence-of-returns risk.

### Test Case 4: Monte Carlo Simulation
```
Run a Monte Carlo simulation with 10,000 iterations.
My portfolio is $400,000, I save $25,000/year, and need $35,000/year in retirement.
```

**Expected Result:** Success probability across different time horizons.

---

## Step 6: Share the Gem

1. In the Gems list, click the **share icon** next to your Gem
2. Choose sharing option:
   - **Private** — only you
   - **Link sharing** — anyone with the link
3. Copy the link to share

---

## Usage Tips

### 1. Be Specific with Numbers
Provide exact figures for accurate calculations:
```
Age: 32
Annual income: $95,000
Annual expenses: $45,000
Current portfolio: $180,000
Monthly contribution: $2,500
```

### 2. Use the Financial Profile Template
Download `templates/financial_profile.csv`, fill in your data, and upload it to Gemini.

### 3. Ask for Specific Analyses
- "Calculate my FIRE number at 3.5% withdrawal rate"
- "Run a Monte Carlo simulation with 5,000 iterations"
- "Compare Lean FIRE vs. Fat FIRE for my situation"

### 4. Request Detailed Reports
```
Please generate a comprehensive FIRE report including:
- Current status
- FIRE number calculation
- Scenario analysis (Conservative, Base, Optimistic)
- Risk assessment
- Actionable recommendations
```

### 5. Follow Up with Questions
After receiving your analysis, ask:
- "What's the biggest risk to my plan?"
- "How can I reduce my FIRE number?"
- "What if I want to retire 5 years earlier?"
- "Show me the Monte Carlo simulation details"

---

## Troubleshooting

### "Gem doesn't follow the workflow"
- Ensure the full `instructions.md` content is pasted
- Gemini may need a reminder: "Please follow the 15-step FIRE workflow"
- Check that the instructions field isn't truncated

### "Calculations are wrong"
- Gemini has native Python execution — it should use code for all calculations
- If it's approximating, ask: "Please use Python code to calculate this precisely"
- Verify your input data is correct

### "Gem doesn't reference knowledge files"
- Gemini reads knowledge files when relevant; you can prompt: "Refer to the uploaded risk framework for this analysis"
- You can also paste relevant content directly into the conversation

### "Gem gives investment advice"
- Remind it: "You must not recommend specific buy/sell tickers. Analyze asset classes, not individual securities."

### "Gem doesn't include disclaimers"
- Emphasize: "Always include appropriate disclaimers in your analysis"
- The instructions should include disclaimer requirements

### "Gem is too verbose"
- Ask for more concise responses: "Please provide a summary version"
- Or specify: "Give me the key numbers and recommendations only"

---

## Gemini Advantages

Gemini has several strengths that work well with FIRE Agent:

1. **No character limit on instructions** — Use the full system prompt without trimming
2. **Native Python execution** — Accurate calculations without special setup
3. **Multi-step workflow handling** — Excellent at following the 15-step process
4. **Knowledge file integration** — Good at referencing uploaded documents
5. **Real-time web access** — Can look up current market data if needed

---

## File Structure

```
adapters/gemini/
├── README.md              ← Detailed setup guide
├── instructions.md        ← Paste into Instructions field
└── knowledge_files.md     ← List of files to upload
```

---

## Next Steps

- **[User Guide](user_guide.md)** — Complete guide to using FIRE Agent
- **[FAQ](faq.md)** — Answers to common questions
- **[Installation Guide](installation.md)** — Project setup and verification
- **[ChatGPT Guide](chatgpt.md)** — If you also want to set up on ChatGPT