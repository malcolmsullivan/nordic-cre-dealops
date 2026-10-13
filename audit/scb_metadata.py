import requests

BASE_URL = "https://api.scb.se/ov0104/v2beta/api/v2"

response = requests.get(f"{BASE_URL}/tables/TAB1165/metadata", timeout=10)

if response.status_code != 200:
    print("Request failed with status", response.status_code)
    raise SystemExit(1)

data = response.json()

print(data["label"])
print(data["id"])
print(data["size"])
print(list(data["dimension"].keys()))

types = data["dimension"]["Fastighetstyp"]["category"]
print(list(types.keys()))

for code, name in types["label"].items():
    print(code, "|", name)

contents = data["dimension"]["ContentsCode"]["category"]

for code, name in contents["label"].items():
    print(code, "|", name)