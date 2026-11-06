# Monitor new carriers and authority/insurance changes (scheduled)

Schedule this input daily or weekly: each run outputs only carriers that are new since the previous run or whose authority, insurance, fleet, phone/email, address, name or safety rating changed, with a field-by-field changes list and an optional Slack/webhook alert.

- Actor: [FMCSA Carrier Data](https://apify.com/cleanyield/fmcsa-carrier-data)
- Real run: 31 results in 5.8 s (refreshed 2026-11-05)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** The first run is the baseline: every carrier counts as new (changeType new). Changes are detected between runs, so the sample below (a first run) has no "changed" items yet. The state keeps up to 50,000 carriers per monitor.
