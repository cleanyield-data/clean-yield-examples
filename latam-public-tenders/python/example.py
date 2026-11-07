"""Latin America Public Tenders - run it from Python with the official Apify client.

Store page: https://apify.com/cleanyield/latam-public-tenders

    pip install apify-client
    export APIFY_TOKEN=<YOUR_APIFY_TOKEN>
    python example.py
"""
import json
import os

from apify_client import ApifyClient

TOKEN = os.environ.get("APIFY_TOKEN", "<YOUR_APIFY_TOKEN>")

run_input = {
    "countries": [
        "CO",
        "BR",
        "CL"
    ],
    "sectors": [
        "it-software"
    ],
    "status": [
        "open"
    ],
    "publishedWithinDays": 5,
    "maxResults": 15
}


def main() -> None:
    client = ApifyClient(TOKEN)
    # Starts the Actor and waits for it to finish.
    run = client.actor("cleanyield/latam-public-tenders").call(run_input=run_input)
    # apify-client 1.x returns a dict, 2.x+ a Run object: read both.
    status = getattr(run, "status", None) or (run.get("status") if isinstance(run, dict) else None)
    if run is None or str(status).split(".")[-1].upper() != "SUCCEEDED":
        raise SystemExit(f"Run did not succeed: {status}")
    dataset_id = getattr(run, "default_dataset_id", None) or run["defaultDatasetId"]

    items = list(client.dataset(dataset_id).iterate_items())
    print(f"Got {len(items)} results")
    for item in items[:3]:
        print(json.dumps(item, ensure_ascii=False, indent=2)[:800])


if __name__ == "__main__":
    main()
