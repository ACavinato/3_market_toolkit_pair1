"""
demo.py — a short runnable script that demonstrates the pipeline.

>>> Partner B owns this file. <<<

When done, this script should:
  1. Load all prices from  data/raw/
  2. For each ticker, compute daily returns, cumulative returns,
     Sharpe ratio, and max drawdown.
  3. Print a one-line summary per ticker.
  4. Save a plot of cumulative returns to  outputs/cumulative_returns.png .

Run it from the repo root:

    python -m src.demo

Note on file choice: we use a plain .py script instead of a Jupyter notebook
because notebooks are painful to diff and review in PRs. Same result, easier
for your partner to read.
"""

from pathlib import Path

import matplotlib.pyplot as plt   # remember to add matplotlib to requirements.txt

from src.ingest import load_all_prices
from src.metrics import (
    daily_returns,
    cumulative_returns,
    sharpe_ratio,
    max_drawdown,
)


def main():
    # TODO 1: load all prices from  'data/raw'
    #         >>> prices = load_all_prices('data/raw')

    # TODO 2: create an outputs/ folder if it doesn't exist
    #         >>> outputs_dir = Path('outputs')
    #         >>> outputs_dir.mkdir(exist_ok=True)

    # TODO 3: for each ticker, compute the metrics and print a summary.
    #         Skeleton to fill in:
    #
    #         fig, ax = plt.subplots(figsize=(10, 5))
    #
    #         for ticker in sorted(prices['ticker'].unique()):
    #             # filter the DataFrame to this ticker's rows only
    #             sub = prices[prices['ticker'] == ticker].copy()
    #
    #             # set the date as the index so plots have real dates on x-axis
    #             sub = sub.set_index('date')
    #
    #             # compute the metrics — call your metrics.py functions
    #             r    = daily_returns(sub['close'])
    #             cum  = cumulative_returns(r)
    #             sr   = sharpe_ratio(r)
    #             mdd  = max_drawdown(cum)
    #
    #             # print one summary line — use an f-string
    #             print(f"{ticker.upper():5s}  Sharpe: {sr:6.2f}  "
    #                   f"MaxDD: {mdd:7.1%}  FinalCum: {cum.iloc[-1]:7.1%}")
    #
    #             # add a line to the plot
    #             ax.plot(cum.index, cum.values, label=ticker.upper())

    # TODO 4: finish the plot: title, xlabel, ylabel, legend, grid
    #         Then save it and close the figure.
    #
    #         ax.set_title('Cumulative returns')
    #         ax.set_xlabel('Date')
    #         ax.set_ylabel('Cumulative return')
    #         ax.legend()
    #         ax.grid(alpha=0.3)
    #         out_path = outputs_dir / 'cumulative_returns.png'
    #         fig.savefig(out_path, dpi=150, bbox_inches='tight')
    #         plt.close(fig)
    #         print(f"Saved plot to {out_path}")

    raise NotImplementedError("demo.py — assemble the pieces above")


if __name__ == '__main__':
    main()
