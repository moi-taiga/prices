---
name: charts
description: House style for charts of the price data. Use whenever making a chart or figure.
user-invocable: false  # the agent loads it; it isn't a / command
---

# Charts

1. Plot the percentage change in `Close` from the first date in the chart.
2. One line per ticker, in these colours: AAPL `#555555`, NVDA `#76B900`, ULVR.L `#1F36C7`.
3. A title saying what is shown and the date range. Label the y axis "Change since first day (%)".
4. A note in the bottom corner: "Source: Yahoo Finance".
5. Save to `figures/` as a PNG at 150 dpi. Don't call `plt.show()`.