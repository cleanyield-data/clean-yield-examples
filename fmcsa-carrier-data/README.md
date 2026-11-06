# FMCSA Carrier Data

US trucking companies and freight brokers from official FMCSA data: USDOT/MC lookup, daily new and revoked authority feed, radius search, insurance history, safety, contacts.

**Run it on Apify:** https://apify.com/cleanyield/fmcsa-carrier-data

Pay per result: you only pay for valid results; failed lookups are free and there are no platform usage fees.

## Real examples (input + output)

| Example | Real run |
|---|---|
| [New trucking companies in Texas (last 30 days) with phone and email](examples/01-new-trucking-companies-texas/) | 25 results · 4.5 s |
| [Bulk USDOT number lookup: company name, authority, insurance and fleet](examples/02-usdot-number-lookup/) | 3 results · 3.7 s |
| [MC number to USDOT lookup (carrier and broker authority)](examples/03-mc-number-lookup/) | 3 results · 5.1 s |
| [Freight brokers with active authority in Illinois](examples/04-freight-brokers-illinois/) | 20 results · 4.6 s |
| [Refrigerated (reefer) carriers with 5–50 trucks in Georgia](examples/05-reefer-carriers-small-fleets-georgia/) | 20 results · 4.9 s |
| [Owner-operators (1 truck) with active MC authority in Arizona](examples/06-owner-operators-arizona/) | 20 results · 4.3 s |
| [Hazmat carriers in Louisiana](examples/07-hazmat-carriers-louisiana/) | 15 results · 4.1 s |
| [Monitor new carriers and authority/insurance changes (scheduled)](examples/08-monitor-new-carriers-and-changes/) | 31 results · 5.8 s |
| [Carrier risk score, insurance renewal and why-now (Pro mode)](examples/09-pro-mode-carrier-risk-and-renewals/) | 3 results · 4 s |
| [Truck insurance leads: carriers with insurer and fleet size](examples/10-truck-insurance-leads-insurer-fleet/) | 3 results · 6.3 s |

## Ready-to-use templates

| Template | Type |
|---|---|
| [`clay-usdot-enrichment.md`](templates/clay-usdot-enrichment.md) | step-by-step guide |
| [`make-weekly-new-carrier-leads.md`](templates/make-weekly-new-carrier-leads.md) | step-by-step guide |
| [`n8n-carrier-watchlist-changes-to-slack.json`](templates/n8n-carrier-watchlist-changes-to-slack.json) | n8n workflow (import from file) |
| [`n8n-new-carriers-to-google-sheets.json`](templates/n8n-new-carriers-to-google-sheets.json) | n8n workflow (import from file) |

## Code

- `python/example.py` and `javascript/example.mjs`: run the Actor and print the results.
- `n8n/workflow.json` and `make/README.md`: no-code setup.

Use your own Apify API token as an environment variable (`APIFY_TOKEN`); never commit it.
