---
name: data-report
description: Summarise a raw price file - dates, gaps, missing values and the largest daily changes.
argument-hint: <ticker, for example ULVR.L>
disable-model-invocation: true  # only runs when you type /data-report
---

# Data report

Report on the raw price file for the ticker you were given. Don't change any files.

1. Load it with `prices.load_prices`.
2. Report, as a short table:
   - the first and last date, and the number of rows
   - the lowest and highest `Close`
   - missing values in each column
   - trading days in the other tickers' files that are missing from this one
   - the three largest daily percentage changes in `Close`, up or down, with their dates
3. End with one line on anything to watch for before using the data.