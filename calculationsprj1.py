from dataprj1 import get_closing_prices

def ticker_analysis(closing_prices):
    if not closing_prices or len(closing_prices) < 2:
        print("Not enough data to analyze (need at least 2).")
        return
    last_price = closing_prices[-1]
    previous_price = closing_prices[-2]
    print("\n--- Calculations ---")
    print(f"Last Closing Price: {last_price}")
    print(f"Previous Closing Price: {previous_price}")
    if previous_price == 0:
        print("Percentage Change: n/a (previous price was 0)")
    else:
        percentage_change = ((last_price - previous_price) / previous_price) * 100
        print(f"Percentage Change: {percentage_change:.2f}%")
    returns = [
        (closing_prices[i] - closing_prices[i - 1]) / closing_prices[i - 1]
        for i in range(1, len(closing_prices))
        if closing_prices[i - 1] != 0
    ]
    if not returns:
        print("Not enough valid returns to compute statistics.")
        return
    mean_return = sum(returns) / len(returns)
    variance = sum((r - mean_return) ** 2 for r in returns) / len(returns)
    volatility = variance ** 0.5
    print(f"Average Return: {mean_return * 100:.2f}%")
    print(f"Volatility: {volatility * 100:.2f}%")

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
    ticker_analysis(get_closing_prices(ticker, window))
