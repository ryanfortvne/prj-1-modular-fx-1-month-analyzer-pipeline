import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import calculationsprj1
from dataprj1 import get_closing_prices
from visualprj1 import run_visuals

def main():
    print("=== Financial Data Analysis & Visualization Suite ===")
    try:
        ticker = input("Enter ticker (e.g., AAPL.US or EURUSD.FOREX): ").strip().upper()
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.")
        return
    if not ticker:
        print("Error: ticker cannot be empty.")
        return
    try:
        raw_window = input("Enter the number of recent closing prices to fetch: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.")
        return
    try:
        window_fetched = int(raw_window)
    except ValueError:
        print("Error: please enter a whole number.")
        return
    if window_fetched < 2:
        print("Error: window must be at least 2 to run the analysis.")
        return
    print(f"\nFetching data for {ticker} (last {window_fetched} closes)...")
    closing_prices = get_closing_prices(ticker, window_fetched)
    if not closing_prices:
        print("Error: Could not retrieve closing prices. Check your ticker or API key.")
        return
    if len(closing_prices) < 2:
        print(f"Error: only {len(closing_prices)} price(s) retrieved, need at least 2.")
        return
    if len(closing_prices) < window_fetched:
        print(f"Note: requested {window_fetched}, but only {len(closing_prices)} available.")
    print(f"Successfully retrieved {len(closing_prices)} price points.\n")
    print("=" * 40)
    print("STATISTICAL CALCULATIONS")
    print("=" * 40)
    calculationsprj1.ticker_analysis(closing_prices)
    print("\nGenerating visual analysis plots...")
    run_visuals(closing_prices)

if __name__ == "__main__":
    main()
