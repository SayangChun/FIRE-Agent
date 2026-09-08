# FIRE Agent

> **A Portable AI FIRE Digital Employee — Your Personal Financial Independence Advisor**

FIRE Agent is a complete, portable AI agent package for Financial Independence, Retire Early (FIRE) planning. It runs on **your own AI platform** — no API keys, no servers, no subscriptions required.

---

## What Is FIRE Agent?

FIRE Agent is **not** a website or SaaS product. It is a **portable agent kit** that you install into your own AI environment (ChatGPT, Gemini, Claude, or any compatible AI).

```
FIRE Agent Core          Your AI Runtime
┌──────────────┐         ┌──────────────┐
│ Instructions │         │ ChatGPT      │
│ Methodology  │   +     │ Gemini       │
│ Calculations │         │ Claude       │
│ Risk Rules   │         │ Other AI     │
│ Schemas      │         └──────┬───────┘
│ Examples     │                │
└──────────────┘                ▼
                         Your Financial Data
                         (Excel, CSV, PDF, etc.)
                               │
                               ▼
                      FIRE Analysis Report
```

## Quick Start

### Step 1: Download

```bash
git clone https://github.com/your-username/fire-agent.git
```

Or download the ZIP file from the releases page.

### Step 2: Choose Your Platform

| Platform | Guide |
|----------|-------|
| ChatGPT | [ChatGPT Setup](adapters/chatgpt/README.md) |
| Gemini | [Gemini Setup](adapters/gemini/README.md) |
| Claude | [Claude Setup](adapters/claude/README.md) |
| Other AI | [Generic Setup](adapters/generic/README.md) |

### Step 3: Upload & Configure

Follow the platform-specific guide to:
1. Create your AI agent/assistant
2. Upload the system prompt
3. Upload knowledge files
4. Upload your financial data

### Step 4: Start Your FIRE Analysis

Tell the agent:
> "Help me figure out when I can retire"

Or upload your financial files:
> "Here's my portfolio: assets.xlsx"

---

## What FIRE Agent Does

### Core Capabilities

- **FIRE Number Calculation** — How much you need to retire
- **FIRE Progress Tracking** — How close you are
- **Savings Rate Analysis** — Impact on your timeline
- **FIRE Age Estimation** — When you can retire
- **Scenario Analysis** — Conservative / Base / Optimistic
- **Monte Carlo Simulation** — 10,000-run success probability
- **FIRE Type Classification** — Lean / Regular / Coast / Barista / Fat
- **Risk Analysis** — Sequence risk, inflation, longevity, concentration
- **Trade-off Analysis** — Compare strategies quantitatively
- **Reverse Planning** — "I want to retire at 45 — what do I need?"
- **Coast FIRE Check** — Am I already coasting?
- **Barista FIRE Analysis** — Semi-retirement planning

### Supported File Types

- Excel (.xlsx)
- CSV (.csv)
- PDF
- Images / Screenshots
- Plain text

### FIRE Types Supported

| Type | Description |
|------|-------------|
| Lean FIRE | Minimalist retirement on low annual expenses |
| Regular FIRE | Standard lifestyle retirement |
| Fat FIRE | Comfortable/luxury retirement |
| Coast FIRE | Coast to retirement with no more aggressive saving |
| Barista FIRE | Semi-retirement with part-time work |

---

## Project Structure

```
fire-agent/
├── core/
│   ├── instructions/        # Agent system prompts & behavior rules
│   │   ├── system.md        # Main system prompt
│   │   ├── behavior.md      # Behavioral guidelines
│   │   ├── safety.md        # Safety & compliance rules
│   │   └── workflow.md      # 15-step workflow
│   │
│   ├── methodology/         # FIRE knowledge base
│   │   ├── fire.md          # FIRE overview
│   │   ├── lean-fire.md
│   │   ├── regular-fire.md
│   │   ├── coast-fire.md
│   │   ├── barista-fire.md
│   │   └── fat-fire.md
│   │
│   ├── calculations/        # Calculation rules & formulas
│   │   ├── fire_number.md
│   │   ├── savings_rate.md
│   │   ├── compound_growth.md
│   │   ├── withdrawal.md
│   │   ├── inflation.md
│   │   └── monte_carlo.md
│   │
│   ├── risk/                # Risk framework
│   │   ├── sequence_risk.md
│   │   ├── inflation_risk.md
│   │   ├── longevity_risk.md
│   │   └── concentration_risk.md
│   │
│   ├── schemas/             # Data schemas
│   │   ├── financial_profile.json
│   │   ├── fire_result.json
│   │   ├── scenario.json
│   │   └── report.json
│   │
│   └── examples/            # Example cases
│       ├── case_1_student.md
│       ├── case_2_office_worker.md
│       ├── case_3_programmer.md
│       ├── case_4_btc_holder.md
│       └── case_5_near_fire.md
│
├── adapters/                # Platform-specific adapters
│   ├── chatgpt/
│   ├── gemini/
│   ├── claude/
│   └── generic/
│
├── tools/                   # Python calculation tools
│   ├── fire_calculator.py
│   ├── savings_calculator.py
│   ├── compound_calculator.py
│   ├── withdrawal_simulator.py
│   ├── monte_carlo.py
│   └── fire_score.py
│
├── templates/               # User templates
│   ├── financial_profile.csv
│   └── fire_report.md
│
├── docs/                    # Documentation
│   ├── installation.md
│   ├── user_guide.md
│   ├── chatgpt.md
│   ├── gemini.md
│   └── faq.md
│
├── tests/                   # Unit tests
│   ├── test_fire_calculator.py
│   ├── test_savings_calculator.py
│   ├── test_compound_calculator.py
│   ├── test_withdrawal_simulator.py
│   ├── test_monte_carlo.py
│   └── test_fire_score.py
│
└── README.md
```

---

## Key Design Principles

### 1. No API Keys Required

FIRE Agent runs on **your own AI platform**. You use your existing ChatGPT, Gemini, Claude, or other AI subscription. No additional API keys needed.

### 2. Agent Core ≠ AI Runtime

The FIRE Agent Core (instructions, methodology, calculations, rules) is completely separate from the AI runtime. This means:

- You can switch AI platforms without losing your agent
- Your financial data stays with you
- No vendor lock-in

### 3. Calculations Are Deterministic

FIRE Agent uses **code-based calculations**, not LLM estimates. All critical financial math is performed by:

- Python tools (when code execution is available)
- Explicit formulas (when code execution is not available)

The LLM handles natural language interaction, data extraction, and result presentation — not financial math.

### 4. Your Data Stays Yours

FIRE Agent does not store your financial data on any external server. Your data lives:
- In your AI conversation
- In your local files
- Nowhere else

---

## How Calculations Work

### FIRE Number

```
FIRE Number = Annual Retirement Expenses / Withdrawal Rate

Example:
  Annual expenses: ¥120,000
  Withdrawal rate: 4%
  FIRE Number: ¥3,000,000
```

### Savings Rate

```
Savings Rate = (Annual Income - Annual Expenses) / Annual Income

Example:
  Annual income: ¥240,000
  Annual expenses: ¥96,000
  Savings rate: 60%
```

### FIRE Age Estimate

Uses iterative compound growth simulation:
```
For each year:
  assets = assets × (1 + monthly_return)^12 + contributions
  If assets >= FIRE Number: reached!
```

### Monte Carlo Simulation

Runs 10,000 simulations with:
- Log-normal return distribution
- Inflation-adjusted withdrawals
- Random annual returns

Reports success probability and asset distribution percentiles.

---

## Usage Examples

### Basic FIRE Check

```
You: "I'm 30 years old, make ¥20,000/month, spend ¥8,000/month,
      and have ¥500,000 in investments. When can I retire?"

FIRE Agent: [Performs full analysis and provides timeline]
```

### Upload Financial Data

```
You: [Upload assets.xlsx]
You: "Analyze my FIRE readiness"

FIRE Agent: [Extracts data, confirms with you, then analyzes]
```

### Scenario Analysis

```
You: "What if the market only returns 5% per year?"

FIRE Agent: [Runs conservative scenario and compares results]
```

### Trade-off Analysis

```
You: "I want to retire 5 years earlier. What are my options?"

FIRE Agent: [Compares: increase income, reduce expenses, etc.]
```

---

## Running Tests

```bash
# Install pytest
pip install pytest

# Run all tests
pytest tests/ -v

# Run specific test
pytest tests/test_fire_calculator.py -v
```

---

## Documentation

| Document | Description |
|----------|-------------|
| [Installation Guide](docs/installation.md) | How to download and set up |
| [User Guide](docs/user_guide.md) | Complete usage guide |
| [ChatGPT Guide](docs/chatgpt.md) | ChatGPT-specific setup |
| [Gemini Guide](docs/gemini.md) | Gemini-specific setup |
| [FAQ](docs/faq.md) | Frequently asked questions |

---

## FIRE Agent Is Not

- ❌ Investment advice
- ❌ Tax advice
- ❌ Legal advice
- ❌ Medical advice
- ❌ A guarantee of financial outcomes
- ❌ A replacement for professional financial planning

## FIRE Agent Is

- ✅ A personal financial analysis tool
- ✅ A FIRE planning framework
- ✅ A scenario simulation engine
- ✅ A risk assessment tool
- ✅ A financial education resource

---

## Disclaimer

FIRE Agent is a personal financial planning and scenario analysis tool. It does not constitute investment, tax, legal, or medical advice.

All return rates, inflation rates, withdrawal rates, and simulation results are hypothetical assumptions. Monte Carlo results do not represent actual future success probabilities.

Users should make judgments based on their own circumstances and consult qualified professionals for financial, tax, and legal decisions.

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## Support

- Documentation: [docs/](docs/)
- FAQ: [docs/faq.md](docs/faq.md)
- Issues: GitHub Issues

---

**FIRE Agent — Your Portable AI FIRE Financial Advisor**
