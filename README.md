Modular FX 1-Month Analyzer Pipeline
A clean, modular Python pipeline for fetching, analyzing, and visualizing FX / Stock closing prices using the EODHD API.

It fetches the last N closing prices, calculates daily returns, percentage change, average return & volatility, and plots volatility clustering + return distribution.

Features
Modular design: data fetching (dataprj1.py), calculations (calculationsprj1.py), visualization (visualprj1.py) orchestrated by main.py
Safe error handling: missing API key, zero-price guards, invalid tickers, headless plotting (Agg backend)
Works on Windows / OneDrive / VS Code with spaces in path
Project Structure
prj 1 Modular FX 1-Month Analyzer Pipeline/
├── main.py                # Entry point - runs full pipeline
├── dataprj1.py            # Fetches closing prices from EODHD
├── calculationsprj1.py    # % change, average return, volatility
├── visualprj1.py          # Time series + histogram plots
├── requirements.txt       # Dependencies
├── .env                   # Your API key (create this, don't commit)
└── returns_analysis.png   # Generated plot
Installation
1. Clone / Open the folder
In VS Code: File -> Open Folder and select the pipeline folder.

IMPORTANT: All 4 .py files must be lowercase and in the SAME folder:

calculationsprj1.py (not Calculationsprj1.py)
dataprj1.py
main.py
visualprj1.py
requirements.txt (not Requirements.txt)
If you see a ModuleNotFoundError: No module named 'calculationsprj1', it's a case issue. Fix it:

powershell
Remove-Item -Recurse -Force __pycache__
Move-Item "Calculationsprj1.py" "temp.py" -Force; Move-Item "temp.py" "calculationsprj1.py" -Force
Move-Item "Requirements.txt" "temp.txt" -Force; Move-Item "temp.txt" "requirements.txt" -Force
2. Create a virtual environment (recommended)
powershell
# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1

# Mac / Linux
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
This is the step that fixes No module named 'dotenv':

powershell
pip install -r requirements.txt
What gets installed:

requests>=2.31.0 - EODHD API calls
pandas>=2.0.0 - pct_change & returns
matplotlib>=3.7.0 - plots
python-dotenv>=1.0.0 - loads .env file
If you get ERROR: Could not open requirements file, you are not in the project folder. Do cd "C:\path\to\prj 1 Modular FX 1-Month Analyzer Pipeline" first, then run pip install.

You can also install without the file:

powershell
pip install requests pandas matplotlib python-dotenv
Setup API Key
Get a free key from https://eodhd.com/
Create a file named .env in the SAME folder as main.py
Add this line:
EODHD_API_KEY=your_key_here
The code loads it with load_dotenv(). Never commit .env to git.

Add a .gitignore:

.env
__pycache__/
*.png
venv/
Usage
Always run from INSIDE the project folder:

powershell
cd "C:\Users\ryana\OneDrive\Desktop\QUANT\QD\prj 1 Modular FX 1-Month Analyzer Pipeline"
python main.py
Then:

Enter ticker (e.g., AAPL.US or EURUSD.FOREX): EURUSD.FOREX
Enter the number of recent closing prices to fetch: 30
Output:

Last / Previous close
Percentage Change
Average Return
Volatility
Plot saved as returns_analysis.png + shown on screen
Run modules individually
powershell
python dataprj1.py
python calculationsprj1.py
python visualprj1.py
Troubleshooting
ModuleNotFoundError: No module named 'calculationsprj1'

You are running from the wrong folder OR files have capital letters. cd into the folder and make all .py filenames lowercase. Delete __pycache__.
ERROR: Could not open requirements file: 'requirements.txt'

PowerShell is not in the project folder. cd to the folder that contains requirements.txt.
No module named 'dotenv'

You skipped pip install. Run pip install -r requirements.txt. Note: pip name is python-dotenv, import name is dotenv.
TclError: no display or plot not showing

Fixed in this version - it now uses Agg backend and saves to returns_analysis.png.
OneDrive / Spaces in path

Always quote paths: cd "C:\...\prj 1 Modular FX 1-Month Analyzer Pipeline"
Better: rename folder to fx_analyzer to avoid spaces.
Example
Ticker examples: AAPL.US, MSFT.US, EURUSD.FOREX, GBPUSD.FOREX, BTC-USD.CC

License
MIT - For educational / quant research use.
