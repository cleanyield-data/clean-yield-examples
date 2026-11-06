# Latin America Public Tenders

Public procurement tenders from official open data: Colombia (SECOP), Brazil (PNCP), Chile (Mercado Público), Paraguay (DNCP) and Uruguay (ARCE, beta), with awards, documents, UNSPSC category and English titles.

**Run it on Apify:** https://apify.com/cleanyield/latam-public-tenders

Pay per result: you only pay for valid results; failed lookups are free and there are no platform usage fees.

## Real examples (input + output)

| Example | Real run |
|---|---|
| [IT and software government tenders in Colombia, Brazil and Chile (open, this week)](examples/01-it-software-tenders-latin-america/) | 15 results · 31.6 s |
| [Public works and construction tenders in Chile over USD 100,000](examples/02-construction-tenders-chile/) | 10 results · 193.7 s |
| [Pregão eletrônico for medical supplies in São Paulo (PNCP)](examples/03-pregao-eletronico-medical-sao-paulo/) | 10 results · 2.6 s |
| [SECOP II tenders for cleaning and security services in Colombia](examples/04-secop-ii-cleaning-security-colombia/) | 10 results · 1.6 s |
| [Who wins IT government tenders in Colombia (awardees and amounts)](examples/05-who-wins-it-tenders-colombia/) | 10 results · 2.8 s |
| [Check a tender's status, deadline and winner by ID](examples/06-tender-status-by-id/) | 3 results · 26.2 s |
| [Brazilian public tenders closing this week (over USD 50,000)](examples/07-brazil-tenders-closing-this-week/) | 10 results · 81.5 s |
| [Daily alerts: new security and surveillance tenders (monitor mode)](examples/08-daily-monitor-security-tenders/) | 10 results · 69.9 s |
| [Colombia SECOP II open tenders with bid deadlines](examples/09-colombia-secop-ii-open-tenders-deadline/) | 3 results · 2.3 s |
| [Chile Mercado Público tenders without an API ticket](examples/10-chile-mercado-publico-no-ticket/) | 3 results · 8.3 s |

## Ready-to-use templates

| Template | Type |
|---|---|
| [`alert-inputs-by-sector.md`](templates/alert-inputs-by-sector.md) | step-by-step guide |
| [`clay-tender-status-by-id.md`](templates/clay-tender-status-by-id.md) | step-by-step guide |
| [`make-weekly-tender-digest-email.md`](templates/make-weekly-tender-digest-email.md) | step-by-step guide |
| [`n8n-daily-sector-tenders-to-slack.json`](templates/n8n-daily-sector-tenders-to-slack.json) | n8n workflow (import from file) |
| [`n8n-new-tenders-to-google-sheets.json`](templates/n8n-new-tenders-to-google-sheets.json) | n8n workflow (import from file) |

## Code

- `python/example.py` and `javascript/example.mjs`: run the Actor and print the results.
- `n8n/workflow.json` and `make/README.md`: no-code setup.

Use your own Apify API token as an environment variable (`APIFY_TOKEN`); never commit it.
