"""Plot Unilever and Apple close-price performance during 2025."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from prices import load_prices

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "figures" / "unilever-vs-apple-2025.png"
START_DATE = pd.Timestamp("2025-01-01")
END_DATE = pd.Timestamp("2026-01-01")
TICKERS = {
    "ULVR.L": ("Unilever (ULVR.L)", "#1F36C7"),
    "AAPL": ("Apple (AAPL)", "#555555"),
}


def main() -> None:
    """Create a 2025 comparison chart rebased to the first shared trading day."""
    fig, ax = plt.subplots(figsize=(11, 6))

    for ticker, (label, color) in TICKERS.items():
        prices = load_prices(ticker)
        prices = prices.loc[(prices.index >= START_DATE) & (prices.index < END_DATE)]
        close = prices["Close"]
        performance = (close / close.iloc[0] - 1) * 100
        ax.plot(performance.index, performance, label=label, color=color, linewidth=1.8)

    first_day = max(
        load_prices(ticker).loc[lambda prices: prices.index >= START_DATE].index.min()
        for ticker in TICKERS
    )
    last_day = min(
        load_prices(ticker).loc[lambda prices: prices.index < END_DATE].index.max()
        for ticker in TICKERS
    )
    ax.set_title(
        f"Unilever vs Apple: Close price change "
        f"({first_day:%Y-%m-%d} to {last_day:%Y-%m-%d})"
    )
    ax.set_xlabel("Date")
    ax.set_ylabel("Change since first day (%)")
    ax.axhline(0, color="black", linewidth=0.8, alpha=0.5)
    ax.grid(True, alpha=0.25)
    ax.legend()
    fig.text(0.99, 0.01, "Source: Yahoo Finance", ha="right", va="bottom", fontsize=9)
    fig.tight_layout(rect=(0, 0.03, 1, 1))

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATH, dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()