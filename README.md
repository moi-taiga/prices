# prices

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ImperialCollegeLondon/prices?quickstart=1)

Daily stock prices for three companies, from Yahoo Finance, and a small Python package to load them.

| Ticker | Company |
|---|---|
| `AAPL` | Apple |
| `NVDA` | NVIDIA |
| `ULVR.L` | Unilever |

## Quickstart

Open a Codespace with the button above, which has everything set up already. Or, with Python 3.10 or later and Git:

```bash
git clone https://github.com/ImperialCollegeLondon/prices.git
cd prices
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m pytest
```

```python
from prices import load_prices

aapl = load_prices("AAPL")
```

## Data

The files in `data/raw/` are daily prices from 2 January 2024 to 31 December 2025, one file per ticker, downloaded on 14 October 2026 with [yfinance](https://github.com/ranaroussi/yfinance):

```python
yf.download(ticker, start="2024-01-01", end="2026-01-01",
            auto_adjust=False, multi_level_index=False)
```

Each file has these columns:

| Column | Meaning |
|---|---|
| `Date` | Trading day |
| `Open`, `High`, `Low`, `Close` | Prices for the day, adjusted for stock splits |
| `Adj Close` | Closing price adjusted for splits and dividends |
| `Volume` | Number of shares traded |

Yahoo Finance data is for personal and educational use. See Yahoo's terms before using it for anything else.

## Plot

Generate a comparison chart of each stock's adjusted-price change since its first
2024 trading day. Each ticker is plotted on its own trading dates, without filling
in dates when its market was closed:

```bash
python scripts/plot_prices.py
```

The chart is saved to `figures/stock-price-performance-since-2024.png`.
