import requests
import yfinance as yf

TOKEN = "DEIN_TOKEN"
CHAT_ID = "8233354282"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

tickers = ["AAPL", "TSLA", "NVDA", "AMZN", "META", "MSFT"]

for ticker in tickers:
    try:
        data = yf.download(ticker, period="2d", interval="1d", progress=False)
        
        if len(data) < 2:
            continue

        last = data.iloc[-1]
        prev = data.iloc[-2]

        change = ((last["Close"] - prev["Close"]) / prev["Close"]) * 100

        if change > 5:
            send(f"🚀 {ticker} +{change:.2f}% heute")

    except:
        pass
