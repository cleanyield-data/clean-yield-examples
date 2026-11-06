# Clay: "Is this company hiring?" enrichment column

Use the Actor's **sync endpoint** as an HTTP API column. It answers in seconds for one company.

1. In your Clay table, add a column **HTTP API** (Enrich data → HTTP API).
2. Method `POST`, URL:
   ```
   https://api.apify.com/v2/acts/cleanyield~ats-jobs-scraper/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>
   ```
3. Body (map `/Company Domain` or `/Company Name` from your table):
   ```json
   {
     "companies": ["{{Company Name}}"],
     "maxJobsPerCompany": 100,
     "includeDescription": "none"
   }
   ```
   A careers page URL or a job board URL works too (e.g. `https://{{Company Domain}}/careers`): the Actor finds the Greenhouse/Lever/Ashby link inside.
4. The response is an array of jobs. Useful formulas on the result column:
   - **Open jobs**: `{{HTTP API}}.length`
   - **Hiring engineers?**: `{{HTTP API}}.filter(j => /engineer/i.test(j.title)).length > 0`
   - **ATS**: `{{HTTP API}}[0]?.ats`
   - **Top salary posted (USD/year)**: `Math.max(...{{HTTP API}}.map(j => j.salaryAnnualMax || 0))`
5. Companies not on Greenhouse, Lever or Ashby return an empty array and **cost nothing**.

Cost: you pay per job returned (USD 2 per 1,000 jobs on the Free plan). Use `maxJobsPerCompany` to cap it (e.g. 20 is enough for a yes/no signal).
