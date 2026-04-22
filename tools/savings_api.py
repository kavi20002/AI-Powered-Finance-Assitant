import requests

def fetch_currency():
    try:
        r = requests.get("https://api.frankfurter.app/latest")
        return r.json()
    except:
        return {"error": "API failed"}

def suggest_savings(leftover):
    return {
        "target": round(leftover * 0.2, 2)
    }