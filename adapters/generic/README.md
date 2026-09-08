# FIRE Agent — Generic Platform Adapter

Universal setup guide for deploying FIRE Agent on **any** AI platform that supports system prompts and file uploads.

---

## Supported Platforms

This guide works for any AI platform that allows:

- Custom system prompts / instructions
- File uploads or knowledge bases
- Multi-turn conversation

**Examples:** ChatGPT, Claude, Gemini, Llama-based platforms (Perplexity, Poe, etc.), open-source UIs (Open WebUI, text-generation-webui), API-based setups (OpenAI API, Anthropic API, etc.)

---

## Step 1: Copy the System Prompt

1. Open `system_prompt.md` in this folder
2. Copy the **entire contents**
3. Paste into your platform's:
   - System prompt field
   - Custom instructions field
   - API `system` message
   - Agent configuration

### Platform-Specific Locations

| Platform | Where to paste |
|----------|---------------|
| ChatGPT (API) | `system` message in the messages array |
| Claude (API) | `system` parameter in the API call |
| Gemini (API) | `systemInstruction` field |
| Open WebUI | Admin Panel → Settings → System Prompt |
| Poe | Create Bot → Bot Instructions |
| Perplexity | Focus → Custom instructions |
| Ollama (Modelfile) | `SYSTEM` directive |
| LM Studio | System prompt field in chat settings |

---

## Step 2: Upload Knowledge Files

If your platform supports file uploads or a knowledge base:

### Core Knowledge Files (Recommended)

| # | File | Purpose |
|---|------|---------|
| 1 | `fire_formulas.txt` | FIRE calculation formulas and constants |
| 2 | `risk_framework.txt` | 8 risk categories and mitigation strategies |
| 3 | `scenario_templates.txt` | Scenario parameter templates |
| 4 | `fire_types.txt` | FIRE type classification definitions |
| 5 | `monte_carlo_method.txt` | Monte Carlo simulation methodology |

> **No knowledge upload available?** The system prompt in `system_prompt.md` is self-contained. It includes all formulas, workflow steps, and rules inline. Knowledge files are supplementary reference material.

---

## Step 3: Enable Code Execution (If Available)

The FIRE Agent prompt expects Python code execution for calculations. If your platform supports it:

- **ChatGPT:** Enable Code Interpreter / Advanced Data Analysis
- **Claude:** Enable Artifacts
- **Gemini:** Code execution is native
- **API setups:** Provide a Python code interpreter tool or function calling
- **Open WebUI:** Enable Code Interpreter plugin if available

If code execution is **not** available:
- The agent will fall back to formula-based calculations
- Monte Carlo simulations will be approximated
- Results may be less precise but still useful

---

## Step 4: Start a Conversation

Begin with a greeting or direct question. Examples:

```
Hello! I'd like to plan for financial independence. Can you help me
calculate my FIRE number and create a roadmap?
```

```
I want to retire in 15 years. Here's my financial situation:
- Age: 40
- Annual income: $150,000
- Annual expenses: $70,000
- Invested assets: $500,000
- No debt
Can you run a complete FIRE analysis?
```

---

## Step 5: Verify the Agent Follows the Workflow

The agent should:
1. Ask clarifying questions about your FIRE goal
2. Collect your financial information
3. Validate the data
4. Create a Financial Profile
5. Calculate FIRE Number, Progress, Savings Rate
6. Estimate FI Date
7. Run Scenario Analysis
8. Run Monte Carlo (if code execution is available)
9. Identify FIRE Type
10. Identify Risks
11. Perform Trade-off Analysis
12. Generate a FIRE Plan
13. Generate a complete FIRE Report with Disclaimer

If the agent skips steps, remind it: **"Please follow the 15-step FIRE workflow from your instructions."**

---

## Step 6: Customize (Optional)

You can modify `system_prompt.md` for your specific needs:

- **Adjust defaults:** Change Monte Carlo iterations, default withdrawal rate, etc.
- **Add local context:** Include country-specific tax rules, social security assumptions
- **Modify language:** Translate the prompt to another language
- **Add integrations:** Connect to financial APIs (Plaid, Yahoo Finance, etc.)

---

## API Deployment Example

For developers deploying FIRE Agent via API:

```python
import openai  # or anthropic, google.generativeai, etc.

system_prompt = open("adapters/generic/system_prompt.md").read()

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
)
```

---

## File Structure

```
adapters/generic/
├── README.md              ← You are here
└── system_prompt.md       ← Complete standalone system prompt
```
