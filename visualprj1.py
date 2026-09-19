import os
import matplotlib
# FIX: Auto-detect headless - original had this commented out causing crash on servers
if not os.environ.get("DISPLAY") and os.name != "nt":
    matplotlib.use("Agg")
else:
    try:
        matplotlib.use("Agg")
    except Exception:
        pass

import matplotlib.pyplot as plt
import pandas as pd
from dataprj1 import get_closing_prices

def run_visuals(closing_prices, save_path="returns_analysis.png"):
    if not closing_prices or len(closing_prices) < 2:
        print("Error: not enough closing prices to plot.")
        return
    daily_returns = (
        pd.Series(closing_prices)
        .pct_change()
        .replace([float("inf"), float("-inf")], pd.NA)
        .dropna()
    )
    if daily_returns.empty:
        print("Error: no valid daily returns to plot.")
        return
    print("Daily Returns Calculated:")
    print(daily_returns.tail())
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))
    axes[0].plot(daily_returns.values, color="teal", linewidth=1.2, marker="o", markersize=3)
    axes[0].set_title("Daily Returns Time Series (Volatility Check)")
    axes[0].set_ylabel("Return Rate")
    axes[0].grid(True, linestyle="--", alpha=0.6)
    axes[1].hist(daily_returns.values, bins=15, color="coral", edgecolor="black", alpha=0.7)
    axes[1].set_title("Daily Returns Distribution (Frequency)")
    axes[1].set_ylabel("Frequency")
    axes[1].set_xlabel("Return Value")
    axes[1].grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    try:
        plt.savefig(save_path, dpi=150)
        print(f"Plot saved to {save_path}")
    except Exception as e:
        print(f"Warning: could not save plot: {e}")
    try:
        plt.show()
    except Exception:
        pass
    finally:
        plt.close(fig)

if __name__ == "__main__":
    ticker = input("Enter ticker: ").strip().upper()
    if not ticker:
        print("Error: ticker cannot be empty.")
        raise SystemExit(1)
    try:
        window = int(input("Enter window size: ").strip())
        if window < 2:
            print("Error: window must be at least 2.")
            raise SystemExit(1)
    except ValueError:
        print("Error: window size must be a whole number.")
        raise SystemExit(1)
    run_visuals(get_closing_prices(ticker, window))
