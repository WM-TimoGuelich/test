import requests
import time


url = "https://api.github.com/repos/WM-TimoGuelich/test/commits"

while True:
    response = requests.get(url=url, timeout=3)
    print(response.status_code)
    data: list[dict] = response.json()

    print(f"Anzahl der commits: {len(data)}")
    time.sleep(3)
