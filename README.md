# FIRE Agent

> Portable AI FIRE Digital Employee — Your Personal Financial Independence Advisor

Runs on **your own AI platform** (ChatGPT, Gemini, Claude). No API keys. No servers. No subscriptions.

## How It Works

```
FIRE Agent Core  +  Your AI Platform  +  Your Financial Data  =  FIRE Analysis
```

## Quick Start

1. Choose platform: `adapters/chatgpt.md` | `adapters/gemini.md` | `adapters/claude.md` | `adapters/generic.md`
2. Create AI agent → upload `core/instructions.md`
3. Upload knowledge: `core/methodology.md` + `core/calculations.md` + `core/risk.md`
4. Upload `templates/financial_profile.xlsx` (fill in your data)
5. Chat: "帮我分析我的 FIRE 进度"

## Core Capabilities

| Feature | Description |
|---------|-------------|
| FIRE Number | Annual expenses / withdrawal rate |
| FIRE Progress | Current assets / FIRE number |
| Savings Rate | Impact on timeline |
| FIRE Age | Compound growth simulation |
| Scenarios | Conservative / Base / Optimistic |
| Monte Carlo | 10,000-run success probability |
| FIRE Types | Lean / Regular / Coast / Barista / Fat |
| Risk Analysis | Sequence, inflation, longevity, concentration |
| Trade-offs | Compare strategies quantitatively |
| Reverse Plan | "Retire at 45 — what do I need?" |

## Project Structure

```
fire-agent/
├── core/               # Agent core
│   ├── instructions.md # System prompt + behavior + safety + workflow
│   ├── methodology.md  # FIRE knowledge (lean/coast/barista/fat)
│   ├── calculations.md # Formulas (fire number, compound, MC, etc.)
│   ├── risk.md         # Risk framework
│   ├── schemas.json    # Data schemas
│   └── examples.md     # 5 example cases
├── adapters/           # Platform setup guides
│   ├── chatgpt.md
│   ├── gemini.md
│   ├── claude.md
│   └── generic.md
├── tools/              # Python calculators
├── templates/          # Financial profile (CSV/XLSX) + report
├── tests/              # 86 unit tests
├── docs.md             # Installation + user guide + FAQ
└── README.md
```

## Key Principles

- **No API keys** — runs on your existing AI subscription
- **Deterministic math** — calculations via code, not LLM estimates
- **Data stays yours** — no external storage
- **Agent Core ≠ AI Runtime** — portable across platforms

## Calculations

```
FIRE Number = Annual Retirement Expenses / Withdrawal Rate
Savings Rate = (Income - Expenses) / Income
FIRE Age    = Simulate compound growth until assets >= FIRE Number
Monte Carlo = 10,000 random return paths → success probability
```

## Tests

```bash
pip install pytest
pytest tests/ -v          # 86 tests
```

## Disclaimer

FIRE Agent is a personal financial planning and scenario analysis tool. It does not constitute investment, tax, legal, or medical advice. All projections are hypothetical. Consult qualified professionals for financial decisions.

---

**FIRE Agent — Your Portable AI FIRE Financial Advisor**
