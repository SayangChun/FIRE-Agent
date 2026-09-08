# FIRE Agent — Gemini Gems Setup Guide

Step-by-step instructions to deploy FIRE Agent as a Gemini Gem.

---

## Prerequisites

- Google account with Gemini access (gemini.google.com)
- Gemini Advanced subscription recommended for best results
- The files in this `gemini/` folder

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

1. Open `instructions.md` in this folder
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

### Test Case 2: Full Analysis
```
Run a complete FIRE analysis for me. I want to retire at 45.
My current portfolio is $500,000, I save $40,000/year,
and expect to spend $60,000/year in retirement.
```

### Test Case 3: Risk Analysis
```
What are the biggest risks to my FIRE plan?
I'm 90% in US stocks with no bonds or real estate.
```

---

## Step 6: Share the Gem

1. In the Gems list, click the **share icon** next to your Gem
2. Choose sharing option:
   - **Private** — only you
   - **Link sharing** — anyone with the link
3. Copy the link to share

---

## Troubleshooting

### "Gem doesn't follow the workflow"
- Ensure the full `instructions.md` content is pasted
- Gemini may need a reminder: "Please follow the 15-step FIRE workflow"

### "Calculations are wrong"
- Gemini has native Python execution — it should use code for all calculations
- If it's approximating, ask: "Please use Python code to calculate this precisely"

### "Gem doesn't reference knowledge files"
- Gemini reads knowledge files when relevant; you can prompt: "Refer to the uploaded risk framework for this analysis"

### "Gem gives investment advice"
- Remind it: "You must not recommend specific buy/sell tickers. Analyze asset classes, not individual securities."

---

## File Structure

```
adapters/gemini/
├── README.md              ← You are here
├── instructions.md        ← Paste into Instructions field
└── knowledge_files.md     ← List of files to upload
```
