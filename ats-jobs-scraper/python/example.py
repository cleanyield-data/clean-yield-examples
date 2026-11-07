"""ATS Jobs Scraper - run it from Python with the official Apify client.

Store page: https://apify.com/cleanyield/ats-jobs-scraper

    pip install apify-client
    export APIFY_TOKEN=<YOUR_APIFY_TOKEN>
    python example.py
"""
import json
import os

from apify_client import ApifyClient

TOKEN = os.environ.get("APIFY_TOKEN", "<YOUR_APIFY_TOKEN>")

run_input = {
    "companies": [
        "anthropic",
        "https://jobs.lever.co/spotify",
        "jobs.ashbyhq.com/ramp"
    ],
    "maxJobsPerCompany": 20,
    "includeDescription": "text"
}


def main() -> None:
    client = ApifyClient(TOKEN)
    # Starts the Actor and waits for it to finish.
    run = client.actor("cleanyield/ats-jobs-scraper").call(run_input=run_input)
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
