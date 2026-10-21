"""Plot the stocks' adjusted-price performance since the start of 2024."""

from pathlib import Path

import matplotlib.pyplot as plt

from prices import TICKERS, load_prices

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "figures" / "stock-price-performance-since-2024.png"


def main() -> None:
    """Create a comparison chart rebased to each stock's first available price."""
    fig, ax = plt.subplots(figsize=(11, 6))

    for ticker in TICKERS:
        prices = load_prices(ticker)
        adjusted_close = prices["Adj Close"]
        performance = (adjusted_close / adjusted_close.iloc[0] - 1) * 100
        ax.plot(performance.index, performance, label=ticker, linewidth=1.8)

    ax.set_title("Stock price performance since 2024")
    ax.set_xlabel("Date")
    ax.set_ylabel("Change in adjusted close from first 2024 trading day (%)")
    ax.axhline(0, color="black", linewidth=0.8, alpha=0.5)
    ax.grid(True, alpha=0.25)
    ax.legend(title="Ticker")
    fig.tight_layout()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATH, dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
