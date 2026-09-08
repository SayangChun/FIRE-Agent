# FIRE Agent Documentation

## Installation

```bash
git clone https://github.com/your-username/fire-agent.git
cd fire-agent
```

### Verify
```bash
python -c "from tools.fire_calculator import calculate_fire_number; print(calculate_fire_number(40000, 0.04))"
```
Expected: `{'fire_number': 1000000.0, 'withdrawal_rate': 0.04, 'annual_retirement_expenses': 40000}`

## Quick Start

1. Choose platform: ChatGPT / Gemini / Claude / Generic (see `adapters/`)
2. Create Custom GPT, Gem, or Project
3. Paste system prompt from adapter file
4. Upload knowledge files (optional but recommended)
5. Enable code execution (Code Interpreter / Artifacts / native Python)
6. Gather financial data: age, income, expenses, assets, liabilities, savings
7. Start conversation: "Help me calculate my FIRE number"
8. Follow the 15-step workflow (agent guides you)

## Platform Guides

| Platform | Setup | Strengths |
|----------|-------|-----------|
| **ChatGPT** | Create GPT → paste prompt → enable Code Interpreter | Widely used, Custom GPTs |
| **Gemini** | Create Gem → paste prompt → upload files | No char limit, native Python |
| **Claude** | Create Project → set instructions → enable Artifacts | Nuanced reasoning, structured output |
| **Generic** | Paste into any system prompt field | Works anywhere, API-friendly |

## FAQ

**Q: Is this financial advice?**
A: No. FIRE Agent is an analytical tool. Consult licensed professionals for advice.

**Q: Do I need API keys?**
A: No for platform adapters (ChatGPT/Gemini/Claude). Yes for direct API deployment.

**Q: How accurate are calculations?**
A: As accurate as the formulas allow. Results depend on input assumptions. Monte Carlo models probability, not certainty.

**Q: Which platform should I use?**
A: All work well. ChatGPT for most users, Gemini for no-limit prompts, Claude for complex analysis, Generic for developers.

**Q: What is the 4% rule?**
A: Withdraw 4% annually in retirement. FIRE Number = Annual Expenses / 0.04. FIRE Agent also supports 3%, 3.5%, 5%.

**Q: How often should I update?**
A: Quarterly or after major events (job change, inheritance, marriage).

**Q: Is my data safe?**
A: Your data stays with your platform. Don't include sensitive identifiers (SSN, account numbers).

**Q: Can I share with friends?**
A: Yes — share your Custom GPT / Gem / Project link, or the `system_prompt.md` file.

**Q: Can I use for international users?**
A: Yes. Specify your country, currency, and local tax/healthcare factors. FIRE principles are universal.

**Q: Can I model part-time retirement income?**
A: Yes. Describe your part-time income plans and FIRE Agent adjusts the portfolio needed.

## Key Formulas

| Metric | Formula |
|--------|---------|
| FIRE Number | Annual Retirement Expenses / Withdrawal Rate |
| Progress | Investable Assets / FIRE Number × 100 |
| Savings Rate | (Income - Expenses) / Income × 100 |
| Years to FIRE | `-ln(1 - (FIRE × r) / (Savings × (1+r))) / ln(1+r)` |

## Requirements

- AI platform account (Plus/Pro/Advanced recommended)
- Python 3.8+ (only for running tools directly)
- No API keys required for platform adapters
