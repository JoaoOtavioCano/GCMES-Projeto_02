import yfinance as yf

asset = yf.Ticker("BRLUSD=X")


print(float(asset.fast_info["lastPrice"]) * 4.92)
