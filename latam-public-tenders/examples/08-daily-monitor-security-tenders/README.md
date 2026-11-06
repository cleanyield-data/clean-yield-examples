# Daily alerts: new security and surveillance tenders (monitor mode)

Monitor mode for security services (guards, CCTV, surveillance) in Colombia and Brazil: the first run is the baseline (every tender is new); scheduled daily, each run returns only new tenders plus tenders already sent whose deadline was extended, that were awarded, cancelled or changed amount, with a Slack or webhook alert. changeType and changes tell what happened.

- Actor: [Latin America Public Tenders](https://apify.com/cleanyield/latam-public-tenders)
- Real run: 10 results in 69.9 s (refreshed 2026-11)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** This sample is a first run, so every item is changeType: new. Changes appear in later runs. The state lives in a named key-value store (monitorStateName).
