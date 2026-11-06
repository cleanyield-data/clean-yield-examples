# Company Enrichment from Website

Turn a list of domains into a company profile: emails, phones, social profiles, tech stack, hiring signals.

**Run it on Apify:** https://apify.com/cleanyield/company-enrichment-from-website

Pay per result: you only pay for valid results; failed lookups are free and there are no platform usage fees.

## Real examples (input + output)

| Example | Real run |
|---|---|
| [Find company emails and phone numbers from a website](examples/01-company-emails-phones/) | 3 results · 2.4 s |
| [Detect a website's tech stack: Shopify, HubSpot, WordPress](examples/02-tech-stack-lookup/) | 3 results · 1.7 s |
| [Check if a company is hiring: careers page, ATS and open roles](examples/03-is-company-hiring/) | 3 results · 2.1 s |
| [Get the latest blog posts of competitor websites](examples/04-competitor-blog-posts/) | 3 results · 1.3 s |
| [Enrich Latin American companies from their website](examples/05-latam-company-enrichment/) | 3 results · 4.2 s |
| [Monitor target accounts for buying signals](examples/06-monitor-accounts-buying-signals/) | 3 results · 2.3 s |
| [Score companies by buying intent: who to contact first and why](examples/07-company-buying-intent-score/) | 2 results · 3.5 s |
| [Website contact scraper: paste your startUrls input as is](examples/08-website-contact-scraper-startUrls/) | 3 results · 2.7 s |
| [Company phone numbers from websites, normalized to E.164](examples/09-company-phone-numbers-e164/) | 3 results · 3.4 s |

## Ready-to-use templates

| Template | Type |
|---|---|
| [`clay-http-enrichment.md`](templates/clay-http-enrichment.md) | step-by-step guide |
| [`make-enrich-crm-accounts.md`](templates/make-enrich-crm-accounts.md) | step-by-step guide |
| [`n8n-enrich-google-sheet-leads.json`](templates/n8n-enrich-google-sheet-leads.json) | n8n workflow (import from file) |
| [`n8n-weekly-buying-signals-slack.json`](templates/n8n-weekly-buying-signals-slack.json) | n8n workflow (import from file) |

## Code

- `python/example.py` and `javascript/example.mjs`: run the Actor and print the results.
- `n8n/workflow.json` and `make/README.md`: no-code setup.

Use your own Apify API token as an environment variable (`APIFY_TOKEN`); never commit it.
