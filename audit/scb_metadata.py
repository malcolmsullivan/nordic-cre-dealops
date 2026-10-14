import requests

BASE_URL = "https://api.scb.se/ov0104/v2beta/api/v2"

TABLE_ID = "TAB402"

response = requests.get(f"{BASE_URL}/tables/{TABLE_ID}/metadata", timeout=10)

if response.status_code != 200:
    print("Request failed with status", response.status_code)
    raise SystemExit(1)

data = response.json()

print(data["label"])

for dim in data["id"]:
    labels = data["dimension"][dim]["category"]["label"]
    print("===", dim, "|", len(labels), "categories")
    if len(labels) <= 120:
        for code, name in labels.items():
            print(code, "|", name)
    else:
        for code, name in list(labels.items())[:5]:
            print(" e.g.", code, "|", name)