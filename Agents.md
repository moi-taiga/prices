# AGENTS.md

Daily stock prices from Yahoo Finance, and a small package in `src/prices/` to load them.

## Data

- Files in `data/raw/` are as downloaded. Never edit, rename or overwrite them.
- `ULVR.L` is quoted in pence, the US stocks in dollars. Unless asked otherwise, a plot of multiple stocks should be useful for comparison: put them on one chart, each as a percentage change from the same start date.
- New York and London have different holidays, so the files don't have the same dates. Never make up prices for missing days: plot each stock on its own dates.

## Where things go

- Save charts to `figures/`, and the code that makes them to `scripts/`, so anyone can re-run it.

## Checks

- Run `python -m pytest` after any change.