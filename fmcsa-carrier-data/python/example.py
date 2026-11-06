"""FMCSA Carrier Data - run it from Python with the official Apify client.

Store page: https://apify.com/cleanyield/fmcsa-carrier-data

    pip install apify-client
    export APIFY_TOKEN=<YOUR_APIFY_TOKEN>
    python example.py
"""
import json
import os

from apify_client import ApifyClient

TOKEN = os.environ.get("APIFY_TOKEN", "<YOUR_APIFY_TOKEN>")

run_input = {
    "states": [
        "TX"
    ],
    "entityTypes": [
        "carrier"
    ],
    "operationType": "interstate",
    "addedWithinDays": 30,
    "maxResults": 25
}


def main() -> None:
    client = ApifyClient(TOKEN)
    # Starts the Actor and waits for it to finish.
    run = client.actor("cleanyield/fmcsa-carrier-data").call(run_input=run_input)
    if run is None or run.get("status") != "SUCCEEDED":
        raise SystemExit(f"Run did not succeed: {run and run.get('status')}")

    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    print(f"Got {len(items)} results")
    for item in items[:3]:
        print(json.dumps(item, ensure_ascii=False, indent=2)[:800])


if __name__ == "__main__":
    main()
