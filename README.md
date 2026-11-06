# Clean Yield examples

Ready-to-run examples for the **Clean Yield** Actors on the Apify Store, in Python, JavaScript, n8n and Make.

**Clean Yield** publishes data Actors built for reliability: official public sources and APIs where possible, one clean schema, a quality gate on a fixed test set before every release, and **pay-per-result pricing** (you only pay for valid results; failed lookups are free, no platform usage fees). They also work from AI agents through the Apify MCP server.

## Actors

| Actor | What it does | Examples |
|---|---|---|
| [Company Enrichment from Website](https://apify.com/cleanyield/company-enrichment-from-website) | Turn a list of domains into a company profile: emails, phones, social profiles, tech stack, hiring signals. | [`company-enrichment-from-website/`](company-enrichment-from-website/) |
| [FMCSA Carrier Data](https://apify.com/cleanyield/fmcsa-carrier-data) | US trucking companies and freight brokers from official FMCSA data: USDOT/MC lookup, daily new and revoked authority feed, radius search, insurance history, safety, contacts. | [`fmcsa-carrier-data/`](fmcsa-carrier-data/) |
| [App Store & Google Play Reviews](https://apify.com/cleanyield/app-store-google-play-reviews) | Reviews from the Apple App Store and Google Play in one clean schema, by country and language, with developer replies. | [`app-store-google-play-reviews/`](app-store-google-play-reviews/) |
| [ATS Jobs Scraper](https://apify.com/cleanyield/ats-jobs-scraper) | Live open jobs from Greenhouse, Lever, Ashby, Workday, Recruitee, Personio and Teamtailor job boards, with salary (also annual USD), remote type, seniority and closed-job tracking. | [`ats-jobs-scraper/`](ats-jobs-scraper/) |
| [Latin America Public Tenders](https://apify.com/cleanyield/latam-public-tenders) | Public procurement tenders from official open data: Colombia (SECOP), Brazil (PNCP), Chile (Mercado Público), Paraguay (DNCP) and Uruguay (ARCE, beta), with awards, documents, UNSPSC category and English titles. | [`latam-public-tenders/`](latam-public-tenders/) |

Each folder has real `examples/` (input + output sample from a real run), ready-to-use `templates/` (n8n, Make, Clay), and code in `python/`, `javascript/`, `n8n/` and `make/`.

## Get your Apify API token

1. Create a free Apify account: https://apify.com/ (the free plan includes monthly credit to try the Actors).
2. Open **Apify Console > Settings > API & Integrations**: https://console.apify.com/settings/integrations
3. Copy the **Personal API token**.
4. Use it as an environment variable, never commit it:

```bash
export APIFY_TOKEN=<YOUR_APIFY_TOKEN>
```

## Quick start

```bash
# Python
pip install apify-client
python ats-jobs-scraper/python/example.py

# JavaScript (Node.js 18+)
npm install apify-client
node ats-jobs-scraper/javascript/example.mjs
```

**n8n:** *Workflows > Import from file* > pick `<actor>/n8n/workflow.json`. Create a *Header Auth* credential with Name `Authorization` and Value `Bearer <YOUR_APIFY_TOKEN>`, select it in the HTTP Request node, run.

**Make:** follow `<actor>/make/README.md`.

**Any other tool (Zapier, Clay, curl...)**: one POST request runs the Actor and returns the results:

```bash
curl -X POST "https://api.apify.com/v2/acts/cleanyield~ats-jobs-scraper/run-sync-get-dataset-items" \
  -H "Authorization: Bearer <YOUR_APIFY_TOKEN>" -H "Content-Type: application/json" \
  -d '{"companies": ["anthropic"], "maxJobsPerCompany": 5}'
```

## Costs

Every Actor is pay-per-result: the price per 1,000 results is on its Store page. You can set a maximum cost per run in Apify; the Actors stop when it is reached.

## License

Examples are MIT licensed: copy them into your own projects.
