import requests

API_KEY = "mRcKYoumTDYTNei4Xou8L_eIApMPERaS"

def get_latest_price(ticker):
    url = f"https://api.polygon.io/v2/last/trade/{ticker}?apiKey={API_KEY}"
    try:
        r = requests.get(url)
        data = r.json()
        return round(data['results']['p'], 2)
    except:
        return "Unavailable"