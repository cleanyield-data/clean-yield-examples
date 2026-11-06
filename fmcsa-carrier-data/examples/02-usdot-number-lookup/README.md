# Bulk USDOT number lookup: company name, authority, insurance and fleet

Paste a list of USDOT numbers and get one clean record per carrier: legal and DBA name, USDOT status, out-of-service flag, MC numbers, operating authorities, insurance filings (insurer, policy, effective date), power units, drivers, cargo and SAFER link.

- Actor: [FMCSA Carrier Data](https://apify.com/cleanyield/fmcsa-carrier-data)
- Real run: 3 results in 3.7 s (refreshed 2026-11-05)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** Numbers that do not exist are reported in the log and not charged. Insurance comes from FMCSA filings (BMC-91X, BMC-34, BMC-84...), not from the insurer.
