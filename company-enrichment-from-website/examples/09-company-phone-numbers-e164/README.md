# Company phone numbers from websites, normalized to E.164

Get each company's own phone numbers from its website, in E.164 with country and source, deduplicated and with IDs, years and test numbers filtered out.

- Actor: [Company Enrichment from Website](https://apify.com/cleanyield/company-enrichment-from-website)
- Real run: 3 results in 3.4 s (refreshed 2026-11-06)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** Only phones the company publishes on its own website (tel links, contact and legal pages, footer, structured data). Numbers shown only after JavaScript runs or inside images are not read.
