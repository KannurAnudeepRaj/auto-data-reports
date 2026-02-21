import requests
import json
from datetime import datetime

url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    price = data["data"]["amount"]

    # Save raw data
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    # Generate report
    with open("report.md", "w") as f:
        f.write("# 📊 Automated Bitcoin Report\n\n")
        f.write(f"Last Updated: {datetime.utcnow()} UTC\n\n")
        f.write(f"### 💰 Current BTC Price (USD): ${price}\n\n")
        f.write("---\n")
        f.write("Generated automatically using GitHub Actions.\n")

except Exception as e:
    print("Error:", e)
    exit(0)
