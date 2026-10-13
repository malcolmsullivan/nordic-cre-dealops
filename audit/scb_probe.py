import requests

BASE_URL = "https://api.scb.se/ov0104/v2beta/api/v2"

response = requests.get(f"{BASE_URL}/config", timeout=10)

if response.status_code != 200:
    print("Request failed with status", response.status_code)
    raise SystemExit (1)

data = response.json()

print("max cells:", data["maxDataCells"])
print("calls per window:", data["maxCallsPerTimeWindow"])
print("time window:", data["timeWindow"])
print("license:", data["license"])