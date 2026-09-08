# FIRE Agent — Claude Projects Setup Guide

Step-by-step instructions to deploy FIRE Agent as a Claude Project with custom instructions.

---

## Prerequisites

- Claude account (claude.ai)
- Claude Pro subscription recommended for Projects feature
- The files in this `claude/` folder

---

## Step 1: Create a New Project

1. Go to [claude.ai](https://claude.ai)
2. Click **"Projects"** in the left sidebar
3. Click **"+ Create Project"**
4. Enter project name: `FIRE Agent`

---

## Step 2: Add Custom Instructions

1. In your project, click **"Set custom instructions"** (or the settings icon)
2. Open `instructions.md` in this folder
3. Copy the **entire contents**
4. Paste into the custom instructions field
5. Click **Save**

### Claude-Specific Formatting Notes

- Claude Projects support markdown in custom instructions — keep markdown formatting
- Claude has no hard character limit on custom instructions for Projects
- Claude handles long system prompts well — paste the full prompt
- Claude excels at structured analysis — the 15-step workflow works well
- Use `###` headings for clear structure
- Claude can execute code via Artifacts — enable this for calculations

> **Tip:** Claude's strength is nuanced reasoning and structured output. The trade-off analysis and risk identification steps work particularly well in Claude.

---

## Step 3: Upload Documents

In your project, under **Project Knowledge**:

1. Click **"+ Add content"**
2. Upload the knowledge files listed in `knowledge_files.md` (from the gemini adapter — same files apply)
3. Supported formats: `.txt`, `.pdf`, `.csv`, `.docx`, `.md`

### Knowledge File Checklist

| # | File | Purpose |
|---|------|---------|
| 1 | `fire_formulas.txt` | Core FIRE math formulas |
| 2 | `risk_framework.txt` | 8 risk categories and mitigations |
| 3 | `scenario_templates.txt` | Conservative/Base/Optimistic parameters |
| 4 | `fire_types.txt` | FIRE type definitions |
| 5 | `monte_carlo_method.txt` | Simulation methodology |

---

## Step 4: Enable Code Execution

For FIRE calculations to be accurate:

1. In your project settings, ensure **Artifacts** are enabled
2. Claude can write and execute Python code via Artifacts
3. When the user provides financial data, Claude should use code for:
   - FIRE number calculations
   - Monte Carlo simulations
   - Scenario analysis comparisons
   - Compound growth projections

---

## Step 5: Start a Conversation

1. Open your FIRE Agent project
2. Start a new conversation
3. The custom instructions and project knowledge are automatically applied

---

## Step 6: Test with These Scenarios

### Test Case 1: Basic FIRE Number
```
I'm 32, earn $90,000/year after tax, spend $45,000/year,
and have $150,000 in index funds. Calculate my FIRE number and how far along I am.
```

### Test Case 2: Full FIRE Report
```
Generate a complete FIRE report for me. I want to retire at 50.
Current assets: $400,000 (all in 401k), $50,000 (emergency fund).
Income: $130,000/year. Expenses: $55,000/year.
I expect to spend $50,000/year in retirement.
```

### Test Case 3: Risk Assessment
```
Analyze the risks in my FIRE plan. I have:
- 80% in US large-cap tech stocks
- 10% in bonds
- 10% in Bitcoin
- No real estate, no international diversification
- No disability insurance
```

### Test Case 4: Trade-off Analysis
```
I want to retire 5 years earlier (from 50 to 45). What trade-offs
should I consider? Quantify the impact of each option.
```

---

## Step 7: Share the Project (Optional)

1. In your project, click **"Share"**
2. Choose sharing option:
   - **Only me** — private
   - **Anyone with the link** — shareable
3. Copy the shared link

---

## Troubleshooting

### "Claude doesn't follow the 15-step workflow"
- Ensure the full `instructions.md` is pasted in custom instructions
- Remind Claude: "Please follow the 15-step FIRE workflow from your instructions"

### "Calculations are approximate"
- Claude should use Artifacts (code execution) for all math
- Prompt: "Please write and run Python code to calculate this precisely"

### "Claude recommends specific stocks"
- The instructions prohibit this — re-emphasize: "Do not recommend specific securities"

### "Project knowledge files aren't being used"
- Claude reads project knowledge when relevant
- Prompt: "Refer to the uploaded risk framework file for this analysis"

---

## File Structure

```
adapters/claude/
└── README.md              ← You are here

Also reference:
adapters/gemini/knowledge_files.md  ← Same knowledge files apply
```
