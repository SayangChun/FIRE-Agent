# FIRE Agent — ChatGPT Custom GPT Setup Guide

Step-by-step instructions to deploy FIRE Agent as a Custom GPT in ChatGPT.

---

## Prerequisites

- ChatGPT Plus subscription (required for Custom GPTs)
- Access to [chat.openai.com/gpts](https://chat.openai.com/gpts)
- The files in the `adapters/chatgpt/` folder

---

## Step 1: Create a New Custom GPT

1. Go to [chat.openai.com/gpts](https://chat.openai.com/gpts)
2. Click **"Create a GPT"**
3. You'll see the GPT Editor with two tabs: **Create** and **Configure**

---

## Step 2: Configure Basic Settings

In the **Configure** tab:

| Field | Value |
|-------|-------|
| **Name** | `FIRE Agent` |
| **Description** | Personal FIRE (Financial Independence, Retire Early) financial planning assistant. Analyzes finances, calculates FIRE numbers, runs scenario analysis, and generates actionable plans. |
| **Instructions** | *(See Step 3 below)* |
| **Conversation Starters** | Add these prompts (optional but recommended): |
| | `Help me calculate my FIRE number` |
| | `Analyze my financial independence progress` |
| | `Run a Monte Carlo simulation on my portfolio` |
| | `What FIRE type fits my situation?` |

---

## Step 3: Upload Instructions

1. Open `system_prompt.md` in the `adapters/chatgpt/` folder
2. Copy the **entire contents**
3. Paste into the **Instructions** field in the GPT Editor

> **ChatGPT Instructions field limit:** ~8,000 characters for the base instructions. If the prompt exceeds this, prioritize the Identity, Core Principles, Workflow, and Data Handling sections. The full prompt is provided in `system_prompt.md` — trim the Output Format section if needed.

### ChatGPT-Specific Formatting Notes

- ChatGPT Custom GPTs support markdown in instructions — keep the markdown formatting
- Avoid using `<xml>` tags or non-standard formatting
- The `###` heading hierarchy works well for structure
- Code blocks (```) render properly in instructions
- Do NOT include `/` commands or API references — Custom GPTs cannot call external APIs by default

---

## Step 4: Upload Knowledge Files

1. In the GPT Editor, scroll to the **Knowledge** section
2. Click **"Upload files"**
3. Upload the knowledge files listed in `knowledge_files.md`

> **Important:** Each Custom GPT can have up to **20 files** uploaded as knowledge. Keep files under 10 MB each.

### Knowledge File Checklist

| # | File | Purpose |
|---|------|---------|
| 1 | FIRE calculation formulas | Core math for FIRE number, savings rate, progress |
| 2 | Risk analysis framework | 8 risk categories and mitigation strategies |
| 3 | Scenario analysis templates | Conservative/Base/Optimistic parameter sets |
| 4 | FIRE type definitions | Lean, Regular, Coast, Barista, Fat FIRE criteria |
| 5 | Monte Carlo methodology | Simulation approach, seed handling, output interpretation |

---

## Step 5: Set Capabilities

In the **Configure** tab, under **Capabilities**:

| Capability | Recommended |
|------------|-------------|
| **Web Browsing** | Off (optional — FIRE calculations are self-contained) |
| **DALL·E Image Generation** | Off |
| **Code Interpreter** | **On** — enables Python-based FIRE calculations |

> **Code Interpreter is highly recommended.** It allows the GPT to run actual Python code for precise FIRE calculations, Monte Carlo simulations, and scenario modeling rather than relying on approximation.

---

## Step 6: Test the GPT

1. Click **"Preview"** (right side of the editor)
2. Test with these scenarios:

### Test Case 1: Basic FIRE Number
```
I'm 30 years old, earn $100,000/year after tax, spend $60,000/year,
and have $200,000 invested. Calculate my FIRE number and progress.
```

**Expected Result:** FIRE Agent should calculate:
- FIRE number = $60,000 / 0.04 = $1,500,000
- Progress = $200,000 / $1,500,000 = 13.3%
- Years to FIRE based on savings rate and returns

### Test Case 2: Scenario Analysis
```
Run Conservative, Base, and Optimistic scenarios for my early retirement.
Assume 4% average market return, 7% growth, and 9% optimistic growth.
```

**Expected Result:** Three scenario comparison with different timelines and success probabilities.

### Test Case 3: Monte Carlo
```
Run a Monte Carlo simulation with 10,000 iterations.
My portfolio is $500,000, I save $30,000/year, and need $40,000/year in retirement.
```

**Expected Result:** Success probability across different time horizons (e.g., 85% success at 15 years).

### Test Case 4: Risk Analysis
```
Identify FIRE risks in my plan. I'm heavily concentrated in tech stocks
and have no emergency fund.
```

**Expected Result:** Identification of concentration risk, sequence-of-returns risk, and lack of emergency fund.

---

## Step 7: Publish

1. Click **"Update"** (or "Publish" for first time)
2. Choose visibility:
   - **Only me** — private, just for your use
   - **Anyone with the link** — shareable
   - **Public** — listed in the GPT store
3. Click **"Confirm"**

---

## Conversation Starters

Add these to make it easy for users to start:

| Starter | Purpose |
|---------|---------|
| `Help me calculate my FIRE number` | Quick FIRE number calculation |
| `Analyze my financial independence progress` | Full progress analysis |
| `Run a Monte Carlo simulation on my portfolio` | Risk assessment |
| `What FIRE type fits my situation?` | FIRE type identification |
| `Run scenario analysis for my early retirement` | What-if modeling |
| `Identify risks in my FIRE plan` | Risk assessment |

---

## Troubleshooting

### "The GPT doesn't follow the 15-step workflow"
- Ensure the full `system_prompt.md` content is pasted in Instructions
- If truncated, prioritize Steps 1-8 and the Disclaimer section
- Remind the GPT: "Please follow the 15-step FIRE workflow from your instructions"

### "Calculations are inaccurate"
- Make sure Code Interpreter is enabled
- The GPT should use Python code for all numerical computations, not mental math
- Prompt: "Please use Python code to calculate this precisely"

### "GPT ignores the disclaimer"
- The disclaimer is at the end of the system prompt; if instructions are truncated, paste the disclaimer separately
- Emphasize: "Always include this disclaimer in complete FIRE reports"

### "File uploads aren't being read"
- Custom GPT knowledge files are passive references — the GPT reads them when relevant
- If the GPT doesn't reference them, rephrase: "Refer to the uploaded knowledge file for [topic]"
- You can also copy-paste relevant content directly into the conversation

### "GPT recommends specific stocks"
- The instructions prohibit this — re-emphasize: "Do not recommend specific securities. Analyze asset classes only."

### "GPT gives investment advice"
- Remind it: "You must not recommend specific buy/sell tickers. Analyze asset classes, not individual securities."

### "Instructions field is too long"
- ChatGPT has an ~8,000 character limit for instructions
- Priority order: Identity → Core Principles → Workflow → Data Handling → Output Format
- Keep the 15-step workflow summary, but you can trim detailed explanations

---

## File Structure

```
adapters/chatgpt/
├── README.md              ← Detailed setup guide
├── system_prompt.md       ← Paste into Instructions field
└── knowledge_files.md     ← List of files to upload as Knowledge
```

---

## Tips for Best Results

1. **Enable Code Interpreter** — This is critical for accurate calculations
2. **Use conversation starters** — Makes it easy for users to begin
3. **Test thoroughly** — Use the test cases above before publishing
4. **Start with basic questions** — Let the GPT collect data before running complex analyses
5. **Save important conversations** — You can reference previous analyses
6. **Update knowledge files** — If you add new FIRE methodologies, re-upload them

---

## Next Steps

- **[User Guide](user_guide.md)** — Complete guide to using FIRE Agent
- **[FAQ](faq.md)** — Answers to common questions
- **[Installation Guide](installation.md)** — Project setup and verification