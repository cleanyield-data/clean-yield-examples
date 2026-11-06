# MC number to USDOT lookup (carrier and broker authority)

Convert MC (or FF/MX) docket numbers into full carrier records: USDOT number, legal name, authority type and status per docket, BIPD insurance on file vs. required.

- Actor: [FMCSA Carrier Data](https://apify.com/cleanyield/fmcsa-carrier-data)
- Real run: 3 results in 5.1 s (refreshed 2026-11-05)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** MC numbers issued by FMCSA's new Motus system can have 7–8 digits; both old and new formats are supported.
