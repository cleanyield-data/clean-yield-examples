# Website contact scraper: paste your startUrls input as is

Paste a startUrls input as is: get emails, phones and social links per site with familiar field names, one row per company and one fixed price.

- Actor: [Company Enrichment from Website](https://apify.com/cleanyield/company-enrichment-from-website)
- Real run: 3 results in 2.7 s (refreshed 2026-11-06)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** Reads at most 10 pages per site in the HTML the server sends (no browser). Sites that block bots are reported as blocked and not charged. Personal emails are omitted unless includePersonalEmails is on.
