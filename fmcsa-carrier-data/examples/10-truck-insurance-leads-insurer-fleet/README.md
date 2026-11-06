# Truck insurance leads: carriers with insurer and fleet size

Active for-hire carriers in Florida with 5-50 trucks: current insurer, policy, coverage and effective date, fleet counted like SAFER, ISO dates.

- Actor: [FMCSA Carrier Data](https://apify.com/cleanyield/fmcsa-carrier-data)
- Real run: 3 results in 6.3 s (refreshed 2026-11-06)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** Insurance comes from the filings in FMCSA open data (BIPD, cargo, bond); in this run 12 of 25 carriers had a filing on record, the rest show an empty list. The renewal date is an estimate available in Pro mode.
