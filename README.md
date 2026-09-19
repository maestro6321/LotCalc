# 🏦 LotCalc — MetaTrader 5 Risk & Lot Size Calculator

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Flet](https://img.shields.io/badge/Flet-1.0.0-red.svg)](https://flet.dev/)
[![MetaTrader5](https://img.shields.io/badge/MetaTrader5-5.0.0-green.svg)](https://www.metatrader5.com/)

> A modern, desktop cross-platform risk management tool built with **Flet** for **MetaTrader 5** traders. Calculate optimal lot sizes based on your account balance, risk percentage, and pip value — with live market data pulled directly from MT5.

---

## 🚀 Features

- **🎯 Smart Lot Calculation** — Auto-calculates lot size based on balance, risk %, and pipet size
- **📊 Live Market Data** — Fetches real-time leverage, tick size, contract size, and symbol price from MetaTrader 5
- **🔍 Symbol Search** — Searchable dropdown with live MT5 symbol list
- **🎛️ Visual Controls** — Intuitive sliders, text fields, and color-coded display values
- **⚡ One-Click Refresh** — Context menu or button to refresh all market data
- **🖥️ Native Windows App** — Built as a standalone `.exe` with PyInstaller via Flet

### Calculated Values

| Field | Description |
|-------|-------------|
| **Lot Size** | Calculated lot size (below minimum step shown if applicable) |
| **Price** | Current symbol ask price |
| **Margin** | Required margin for the calculated lot |
| **Balance** | Account balance (live from MT5) |
| **Leverage** | Account leverage |
| **Tick Size / Value** | Symbol tick specifications |
| **Contract Size** | Contract size per lot |
| **Digits** | Symbol price precision |
| **Volume Step** | Minimum volume increment step |

---

## 📋 Prerequisites

| Requirement | Minimum Version | Notes |
|------------|----------------|-------|
| Python | `3.11+` | [Download](https://www.python.org/downloads/) |
| MetaTrader 5 | `5.0+` | [Download](https://www.metatrader5.com/en/download) |
| Operating System | Windows 10/11 | MT5 is Windows-only |

---

## ⚙️ Installation

### 1. Install MetaTrader 5
Download and install [MetaTrader 5](https://www.metatrader5.com/en/download) and ensure it's running.

### 2. Clone & Setup
```bash
git clone https://github.com/maestro6321/LotCalc.git
cd LotCalc
```

### 3. Create Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🏃 Usage

### Run the App (Development)
```bash
python main.py
```
or
```bash
flet run
```

### Run with Virtual Environment
```bash
.venv\Scripts\activate
flet run
```

### How It Works
1. **Launch** the app — it connects to your running MetaTrader 5 terminal
2. **Select a symbol** from the searchable dropdown (default: `XAUUSD`)
3. **Set your Risk %** — percentage of your balance you're willing to risk
4. **Adjust Pipet Size** — use the slider (0–2000%) to set loss per lot
5. **Click "Calculate"** — see your optimal lot size, price, and margin
6. **Refresh** — right-click the app or use the context menu to update market data

---

## 🏗️ Building the App

### Prerequisites for Building
- Python `3.12` or `3.13`
- Git
- uv (optional — handled by CI)

### Build Windows App (Manual)
```bash
# Activate environment
.venv\Scripts\activate

# Build
flet build windows --yes
```

The built app will be in `build\windows\`.

### Build via GitHub Actions
Push a tagged release to trigger automated build:
```bash
git tag v1.0.0
git push origin v1.0.0
```

The CI will:
- ✅ Install dependencies
- ✅ Build the Windows `.exe`
- ✅ Upload as a release asset and build artifact

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| [Flet](https://flet.dev/) | GUI framework (Flutter-based, Python) |
| [MetaTrader5](https://pypi.org/project/MetaTrader5/) | MT5 terminal integration & market data |
| [Python](https://www.python.org/) | Core logic |
| [uv](https://github.com/astral-sh/uv) | Fast Python package manager (CI) |
| [setuptools](https://setuptools.dev/) | Python packaging backend |

---

## 📁 Project Structure

```
LotCalc/
├── main.py                     # App entry point
├── requirements.txt            # Python dependencies
├── pyproject.toml              # Project config (build)
├── .gitignore                  # Git ignore rules
├── .github/
│   └── workflows/
│       └── build.yml           # CI/CD build workflow
├── classes/
│   ├── __init__.py             # Package init (re-exports)
│   ├── setting.py              # App window & layout settings
│   ├── controls.py             # UI controls & layout
│   └── functions.py            # MT5 integration & calculations
└── build/                      # Build output (gitignored)
    └── windows/
        └── lotcalc.exe
```

---

## 📊 Versioning

We use [Semantic Versioning](https://semver.org/). Check releases for the latest version.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/maestro6321/LotCalc/issues)
- **Releases**: [GitHub Releases](https://github.com/maestro6321/LotCalc/releases)

---

> ⚠️ **Note**: This tool requires an active MetaTrader 5 terminal and account. It is not affiliated with MetaQuotes Software Corp.
