# Monitor target accounts for buying signals

Schedule a weekly run over your target account list. The first run returns every company (changeType 'new'); later runs return only companies that changed, with a list of changes such as started_hiring, open_roles_changed, technology_added, new_post or contact_added, and can send a Slack or webhook alert. You pay only for companies that changed.

- Actor: [Company Enrichment from Website](https://apify.com/cleanyield/company-enrichment-from-website)
- Real run: 3 results in 2.3 s (refreshed 2026-11-06)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** Changes are detected between runs that use the same monitorStateName. A contact is only reported as removed if the page where it was seen was read successfully, to avoid false alarms. Hosting and framework changes are ignored.
