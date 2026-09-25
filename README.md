# 🏦 LotCalc — MetaTrader 5 Risk & Lot Size Calculator

> A lightweight Windows desktop application for calculating position size based on account balance, risk percentage, and stop-loss percentage, using live market data from MetaTrader 5.

LotCalc connects directly to a running MetaTrader 5 terminal and calculates an appropriate trading volume based on the selected symbol's live trading specifications.

---

## 🚀 Features

- 🎯 **Risk-Based Lot Calculation** — Calculate lot size from account balance and desired risk percentage.
- 📉 **Percentage-Based Stop Loss** — Define stop loss as a percentage of the current market price instead of relying on broker-specific pip or point conventions.
- 📊 **Live MT5 Market Data** — Reads symbol price and trading specifications directly from MetaTrader 5.
- 🔍 **Symbol Search** — Select symbols from the available MT5 symbol list.
- ⚙️ **Broker-Aware Calculation** — Uses the symbol's tick size and tick value for position sizing.
- 📐 **Volume Step Handling** — Lot size is normalized according to the broker's supported volume step.
- 💰 **Live Account Balance** — Uses the current MT5 account balance.
- 🖥️ **Windows Desktop Application** — Packaged as a standalone Windows application.
- 🎨 **Custom Application Icon** — Includes the LotCalc application icon in the packaged Windows executable.
- 🔄 **Live Data Refresh** — Refresh market and account information directly from MT5.

---

## 📐 Risk Calculation

LotCalc is designed around percentage-based risk management.

### Risk Amount

The amount of money allocated to the trade is calculated from the account balance and selected risk percentage:

```text
Risk Amount = Account Balance × Risk %
```

For example:

```text
Balance = $6,246.89
Risk    = 1%

Risk Amount = $6,246.89 × 0.01
            = $62.4689
```

### Stop Loss Distance

The stop-loss distance is calculated as a percentage of the current symbol price:

```text
Stop Distance = Current Price × Stop Loss %
```

The resulting price distance is then converted into the symbol's tick structure using the live MT5 tick size and tick value.

The final lot size is normalized according to the broker's supported volume step.

> **Important:** Actual trading results can vary because of spread, execution price, commissions, swaps, slippage, and broker-specific symbol specifications.

---

## 🧪 Example

A practical XAUUSD test:

| Parameter | Value |
|---|---:|
| Account Balance | $6,246.89 |
| Risk | 1% |
| Stop Loss | 0.12% |
| Calculated Lot | 0.12 |

The resulting position was tested on XAUUSD with a `0.12` lot position.

The trade generated approximately `$59.28` profit, equivalent to approximately `0.95%` of the account balance.

This example demonstrates the intended relationship between account risk, stop-loss percentage, and calculated position size.

---

## 📊 MT5 Data

LotCalc obtains the required trading information directly from MetaTrader 5.

The application can use:

- Account balance
- Symbol price
- Tick size
- Tick value
- Contract size
- Digits
- Volume step
- Symbol information

This allows the calculation to adapt to the trading specifications provided by the connected broker.

---

## 📋 Requirements

| Requirement | Version / Condition |
|---|---|
| Windows | Windows 10 / 11 (64-bit) |
| MetaTrader 5 | Installed and running |
| MT5 Account | Logged in to a trading account |
| Python | 3.10+ for development |
| Flet | 1.0.0+ |

MetaTrader 5 must be running when using the application because LotCalc obtains account and symbol information from the MT5 terminal.

---

## 📥 Installation

### Option 1 — Download the Windows Release

Download the latest Windows release from the GitHub Releases page.

1. Download the `LotCalc-vX.X.X-windows.zip` archive.
2. Extract the archive.
3. Start `LotCalc.exe`.
4. Make sure MetaTrader 5 is running and logged in.

No Python installation is required when using the packaged Windows release.

---

### Option 2 — Run from Source

Clone the repository:

```bash
git clone https://github.com/maestro6321/LotCalc.git
cd LotCalc
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install the project:

```bash
pip install .
```

Run the application:

```bash
flet run
```

---

## 🏗️ Project Structure

```text
LotCalc/
├── .github/
│   └── workflows/
│       └── build.yml
│
├── src/
│   ├── main.py
│   ├── assets/
│   │   ├── icon.png
│   │   └── version.txt
│   │
│   └── classes/
│       ├── __init__.py
│       ├── controls.py
│       ├── functions.py
│       └── setting.py
│
├── .gitignore
├── README.md
└── pyproject.toml
```

---

## ⚙️ Configuration

Project configuration and Python dependencies are maintained in:

```text
pyproject.toml
```

The application source is located under:

```text
src/
```

Flet is configured to use `src` as the application path.



---

## 🖥️ Building the Windows Application

The application can be built locally with:

```bash
flet build windows --yes
```

The generated Windows application is placed under:

```text
build/windows/
```

### GitHub Actions

The repository includes an automated Windows build workflow.

A published GitHub release triggers the build process:

```text
GitHub Release
      ↓
Checkout tagged commit
      ↓
Install Python dependencies
      ↓
Build with Flet
      ↓
Generate application icons
      ↓
Build Windows application
      ↓
Create ZIP archive
      ↓
Upload release asset
```

The resulting release package follows this naming convention:

```text
LotCalc-vX.X.X-windows.zip
```


---

## 🔒 Risk Management Note

LotCalc is a position-sizing calculator. It does not provide trading signals or guarantee trading results.

The calculated lot size depends on the information supplied by MetaTrader 5 and the trading conditions of the connected broker.

Always verify the calculated volume, stop-loss level, contract specifications, and potential loss before placing a trade.

---

## 🤝 Contributing

Contributions and improvements are welcome.

1. Fork the repository.
2. Create a feature branch:

```bash
git checkout -b feature/my-feature
```

3. Commit your changes:

```bash
git commit -m "Add my feature"
```

4. Push the branch:

```bash
git push origin feature/my-feature
```

5. Open a Pull Request.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## ⚠️ Disclaimer

LotCalc is provided as a calculation and position-sizing utility.

It is not financial advice and does not guarantee trading performance or profitability.

LotCalc is not affiliated with MetaQuotes Software Corp.