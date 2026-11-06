# Monitor new sales jobs at fintech competitors (daily alerts)

Monitor mode: watch Stripe, Ramp, Brex, Plaid and Coinbase for sales roles. The first run returns all current matches as changeType new (272 here); scheduled daily runs return only new or changed jobs (salary, location, title…), optionally closed ones, and send a Slack/webhook alert with a per-company hiring summary (HIRING_SIGNALS).

- Actor: [ATS Jobs Scraper](https://apify.com/cleanyield/ats-jobs-scraper)
- Real run: 272 results in 5.5 s (refreshed 2026-11-05)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** Turn on 'First run: save baseline only' if you only want jobs posted from now on (the first run then outputs and charges nothing). A small company-checked fee applies per watched company and run.
