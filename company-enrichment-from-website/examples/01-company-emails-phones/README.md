# Find company emails and phone numbers from a website

Paste a list of company websites and get one row per company with its generic and role emails (info@, press@, reservations@) and phone numbers in E.164, plus social profiles. Personal emails are omitted by default. Cloudflare-protected emails are decoded and vanity numbers like 1-800-4HOTDOG are converted.

- Actor: [Company Enrichment from Website](https://apify.com/cleanyield/company-enrichment-from-website)
- Real run: 3 results in 2.4 s (refreshed 2026-11-06)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** Only what the company publishes on its own website (home, contact/impressum, about). Emails hidden behind contact forms or loaded only with JavaScript are not found. Personal emails are omitted unless you turn on includePersonalEmails.
