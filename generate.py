import requests
import json
from datetime import datetime

# Fetch Bitcoin price
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()

price = data["bpi"]["USD"]["rate"]

# Save raw data
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Generate markdown report
with open("report.md", "w") as f:
    f.write("# 📊 Automated Bitcoin Report\n\n")
    f.write(f"Last Updated: {datetime.utcnow()} UTC\n\n")
    f.write(f"### 💰 Current BTC Price (USD): ${price}\n\n")
    f.write("---\n")
    f.write("Generated automatically using GitHub Actions.\n")
