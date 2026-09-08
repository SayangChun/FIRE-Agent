# FIRE Agent Installation Guide

Welcome to FIRE Agent — your AI-powered financial independence planning assistant. This guide will help you download, set up, and verify the project.

---

## Downloading the Project

### Option 1: Git Clone (Recommended)

```bash
git clone https://github.com/your-username/fire-agent.git
cd fire-agent
```

### Option 2: Download ZIP

1. Go to the project repository
2. Click **"Code"** → **"Download ZIP"**
3. Extract the ZIP file to your desired location
4. Open the extracted folder

---

## Directory Structure

After downloading, you'll see the following structure:

```
fire-agent/
├── adapters/           # Platform-specific setup guides
│   ├── chatgpt/        # ChatGPT Custom GPT setup
│   ├── claude/         # Claude Projects setup
│   ├── gemini/         # Gemini Gems setup
│   └── generic/        # Universal platform adapter
├── core/               # Core FIRE Agent logic
│   ├── calculations/   # Mathematical formulas and models
│   ├── instructions/   # System prompts and workflow
│   ├── methodology/    # FIRE type definitions
│   ├── risk/           # Risk analysis frameworks
│   └── schemas/        # Data schemas (JSON)
├── templates/          # Financial profile templates
├── tools/              # Python calculation tools
├── tests/              # Test files
├── docs/               # Documentation (you are here)
└── fire-agent/         # Additional agent files
```

---

## What Each Folder Contains

### `adapters/`
Platform-specific setup instructions for deploying FIRE Agent on different AI services:
- **chatgpt/**: Step-by-step guide for ChatGPT Custom GPTs
- **claude/**: Guide for Claude Projects with custom instructions
- **gemini/**: Guide for Gemini Gems
- **generic/**: Universal adapter for any AI platform (APIs, open-source UIs, etc.)

Each adapter folder contains:
- `README.md` or setup guide
- `system_prompt.md` or `instructions.md` (platform-optimized prompts)
- `knowledge_files.md` (list of files to upload as knowledge base)

### `core/`
The heart of FIRE Agent — contains all logic, formulas, and workflows:
- **calculations/**: Mathematical models for FIRE numbers, savings rates, compound growth, Monte Carlo simulations, inflation adjustments, and withdrawal strategies
- **instructions/**: Complete system prompts, workflow documentation, behavioral guidelines, and safety disclaimers
- **methodology/**: Definitions and criteria for different FIRE types (Lean, Regular, Coast, Barista, Fat FIRE)
- **risk/**: Analysis frameworks for 8 risk categories (sequence-of-returns, longevity, inflation, concentration, etc.)
- **schemas/**: JSON schemas for financial profiles, reports, and scenarios

### `templates/`
Ready-to-use templates for collecting financial data:
- `financial_profile.csv`: Structured template for inputting your financial information

### `tools/`
Python scripts for running FIRE calculations independently:
- `fire_calculator.py`: FIRE number and progress calculations
- `monte_carlo.py`: Monte Carlo simulation engine
- `withdrawal_simulator.py`: Withdrawal strategy analysis
- `compound_calculator.py`: Compound growth projections
- `savings_calculator.py`: Savings rate calculations
- `savings_rate.py`: Savings rate optimization

### `tests/`
Test files to verify calculations are working correctly.

---

## Verifying File Completeness

After downloading, verify you have all essential files:

### Essential Files Checklist

```bash
# Check core system prompt
ls core/instructions/system.md

# Check calculation tools
ls tools/fire_calculator.py
ls tools/monte_carlo.py

# Check adapters
ls adapters/chatgpt/README.md
ls adapters/gemini/README.md
ls adapters/claude/README.md
ls adapters/generic/README.md

# Check templates
ls templates/financial_profile.csv
```

### Verify Core Calculations

Run a quick test to ensure Python tools are working:

```bash
cd fire-agent
python -c "from tools.fire_calculator import calculate_fire_number; print(calculate_fire_number(40000, 0.04))"
```

Expected output:
```python
{'fire_number': 1000000.0, 'withdrawal_rate': 0.04, 'annual_retirement_expenses': 40000}
```

### Verify Documentation

Ensure all documentation files exist:

```bash
ls docs/
# Should contain:
# - installation.md (this file)
# - user_guide.md
# - chatgpt.md
# - gemini.md
# - faq.md
```

---

## Next Steps

Once you've verified the files are complete, proceed to:

1. **[User Guide](user_guide.md)** — Complete guide to using FIRE Agent
2. **Platform-Specific Guides:**
   - [ChatGPT Setup](chatgpt.md)
   - [Gemini Setup](gemini.md)
   - [Claude Setup](../adapters/claude/README.md)
   - [Generic Platform Setup](../adapters/generic/README.md)

---

## Requirements

- **AI Platform Account**: ChatGPT Plus, Claude Pro, or Gemini Advanced recommended
- **Python 3.8+** (only if running calculation tools directly)
- **No API keys required** for basic usage through platform adapters

---

## Need Help?

- Check the [FAQ](faq.md) for common questions
- Review platform-specific guides for setup troubleshooting
- Ensure you're following the 15-step workflow described in the User Guide