import requests

r = requests.get("http://127.0.0.1:5000//marsExploration?s=SOSSOTOOT").json()
print(r["corrupted"])