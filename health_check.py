import argparse
import requests

def check_service_health(url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            print(f"[OK] {url} is reachable.")
        else:
            print(f"[ERROR] {url} returned {r.status_code}")
    except Exception as e:
        print(f"[DOWN] {url} unreachable: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    args = parser.parse_args()
    check_service_health(args.url)
