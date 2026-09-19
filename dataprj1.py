import os
from datetime import date, timedelta
import requests
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    def load_dotenv(*a,**k): pass

API_KEY = os.getenv("EODHD_API_KEY")
BASE_URL = "https://eodhd.com/api/eod"

def get_closing_prices(ticker, window):
    api_key = os.getenv("EODHD_API_KEY") or API_KEY
    if not api_key:
        print("Error: EODHD_API_KEY not found. Add it to your .env file.")
        return []
    if not ticker or not str(ticker).strip():
        print("Error: ticker cannot be empty.")
        return []
    if not isinstance(window, int) or window < 1:
        print("Error: window size must be a positive integer.")
        return []
    start = date.today() - timedelta(days=window * 2 + 10)
    params = {
        "api_token": api_key,
        "fmt": "json",
        "from": start.isoformat(),
        "to": date.today().isoformat(),
        "period": "d",
        "order": "a",
    }
    try:
        response = requests.get(f"{BASE_URL}/{ticker}", params=params, timeout=15)
        response.raise_for_status()
        rows = response.json()
    except requests.HTTPError as e:
        status = e.response.status_code if e.response is not None else "?"
        print(f"Error: API returned HTTP {status} for {ticker}.")
        return []
    except requests.RequestException as e:
        print(f"Error: request failed ({type(e).__name__}).")
        return []
    except ValueError:
        print("Error: API did not return valid JSON.")
        return []
    if not isinstance(rows, list) or not rows:
        print(f"Error: no price data returned for {ticker}.")
        return []
    rows.sort(key=lambda row: row.get("date", ""))
    closes = [row["close"] for row in rows if isinstance(row, dict) and row.get("close") is not None]
    if len(closes) < window:
        print(f"Warning: only {len(closes)} prices available, requested {window}.")
    return closes[-window:]
