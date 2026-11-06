# Greenhouse jobs API: all open jobs of a company with salary

Get the open jobs of any company that uses Greenhouse (here: Anthropic, newest 50) straight from the official public job board API, with structured salary (min/max/currency/period), split location (city, region, ISO country), workplace type and the full description as clean text. This run returned 50 jobs.

- Actor: [ATS Jobs Scraper](https://apify.com/cleanyield/ats-jobs-scraper)
- Real run: 50 results in 2.3 s (refreshed 2026-11-05)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** Greenhouse boards do not publish an employment type field: employmentType is filled only when the company adds it as a custom field or the title says it (intern, contract…). descriptionText is truncated in this sample.
