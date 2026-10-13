import requests

BASE_URL = "https://api.scb.se/ov0104/v2beta/api/v2"

terms = ["fastighetspriser", "byggnader", "lokaler", "BO0501"]

for term in terms:
    params = {
        "query": term,
        "pageSize": 50
    }

response = requests.get(f"{BASE_URL}/tables", params=params, timeout=10)

if response.status_code != 200:
    print("Request failed with status", response.status_code)
    raise SystemExit(1)

data = response.json()

print("matching tables:", data["page"]["totalElements"])

for table in data["tables"]:
    print(table["id"], "|", table["label"])