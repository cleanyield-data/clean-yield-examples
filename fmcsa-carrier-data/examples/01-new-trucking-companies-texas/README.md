# New trucking companies in Texas (last 30 days) with phone and email

Get interstate trucking companies whose USDOT number was registered in Texas in the last 30 days, newest first, with phone in E.164, email, fleet size and address. Insurance agents, factoring companies and freight brokers use it as a weekly new-carrier lead feed.

- Actor: [FMCSA Carrier Data](https://apify.com/cleanyield/fmcsa-carrier-data)
- Real run: 25 results in 4.5 s (refreshed 2026-11-05)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** FMCSA publishes new registrations with a 1–2 day delay. Brand-new carriers usually have no MC authority or insurance on file yet (authority is null, insurancePolicies is empty). Contact data is whatever the company filed on its MCS-150.
