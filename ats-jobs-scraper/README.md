# ATS Jobs Scraper

Live open jobs from Greenhouse, Lever, Ashby, Workday, Recruitee, Personio and Teamtailor job boards, with salary (also annual USD), remote type, seniority and closed-job tracking.

**Run it on Apify:** https://apify.com/cleanyield/ats-jobs-scraper

Pay per result: you only pay for valid results; failed lookups are free and there are no platform usage fees.

## Real examples (input + output)

| Example | Real run |
|---|---|
| [Greenhouse jobs API: all open jobs of a company with salary](examples/01-greenhouse-company-jobs/) | 50 results · 2.3 s |
| [Lever postings API: export every job of several companies](examples/02-lever-postings-export/) | 395 results · 3.1 s |
| [Ashby jobs with salary: engineering roles paying $200k+](examples/03-ashby-high-salary-engineering/) | 356 results · 6.4 s |
| [Remote jobs in the US at remote-first startups](examples/04-remote-us-startup-jobs/) | 241 results · 6.4 s |
| [Monitor new sales jobs at fintech competitors (daily alerts)](examples/05-monitor-new-jobs-competitors/) | 272 results · 5.5 s |
| [Find which ATS a company uses (Greenhouse, Lever or Ashby)](examples/06-detect-company-ats/) | 9 results · 3.7 s |
| [Internships at tech companies across Greenhouse, Lever and Ashby](examples/07-tech-internships/) | 59 results · 6.2 s |
| [Hiring signals for sales: which companies are hiring engineers right now (Pro mode)](examples/08-pro-hiring-signals-why-now/) | 4 results · 5.2 s |
| [Live job postings posted after a date (no expired jobs)](examples/09-new-jobs-posted-after-date/) | 173 results · 4.9 s |

## Ready-to-use templates

| Template | Type |
|---|---|
| [`clay-is-company-hiring.md`](templates/clay-is-company-hiring.md) | step-by-step guide |
| [`make-new-jobs-to-google-sheets.md`](templates/make-new-jobs-to-google-sheets.md) | step-by-step guide |
| [`n8n-hiring-signals-google-sheets.json`](templates/n8n-hiring-signals-google-sheets.json) | n8n workflow (import from file) |
| [`n8n-new-jobs-to-slack.json`](templates/n8n-new-jobs-to-slack.json) | n8n workflow (import from file) |

## Code

- `python/example.py` and `javascript/example.mjs`: run the Actor and print the results.
- `n8n/workflow.json` and `make/README.md`: no-code setup.

Use your own Apify API token as an environment variable (`APIFY_TOKEN`); never commit it.
