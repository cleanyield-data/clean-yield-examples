# Check a tender's status, deadline and winner by ID

Look up specific tenders by the ID shown on each portal (SECOP II process id, PNCP control number, Mercado Público code) and get their current status, deadline, amount and, if awarded, the winner. Useful for tracking the tenders you bid on, in Clay or a spreadsheet.

- Actor: [Latin America Public Tenders](https://apify.com/cleanyield/latam-public-tenders)
- Real run: 3 results in 26.2 s (refreshed 2026-11)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** IDs that don't exist are reported in the log and not charged. Brazil awardees need a couple of extra requests per awarded tender.
