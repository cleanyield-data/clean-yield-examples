# Make: new jobs at your watchlist → Google Sheets (daily)

Scenario with 3 modules. Time to set up: ~5 minutes. No real tokens in this file.

1. **Apify → Run an Actor** (wait for the run to finish: *Yes*)
   - Connection: your Apify account (API token from Apify Console → Settings → Integrations).
   - Actor: `cleanyield/ats-jobs-scraper`
   - Input JSON:
     ```json
     {
       "companies": ["stripe", "ramp", "https://jobs.lever.co/spotify", "openai", "https://www.figma.com/careers/"],
       "keywords": ["product manager", "engineer"],
       "locations": ["United States", "remote"],
       "monitorMode": true,
       "monitorStateName": "make-watchlist",
       "skipExistingOnFirstRun": true,
       "includeDescription": "none"
     }
     ```
2. **Apify → Get Dataset Items**
   - Dataset ID: `{{1.defaultDatasetId}}` · Limit: 1000.
3. **Google Sheets → Add a Row** (one row per item; Make iterates automatically)
   - Columns: `changeType`, `company`, `title`, `location`, `workplaceType`, `salaryText`, `salaryAnnualMin`, `salaryAnnualMax`, `postedAt`, `url`, `jobId`.
   - Optional filter between 2 and 3: `changeType` = `new`.

Schedule the scenario **every day**. Monitor mode returns only new or changed jobs, so the sheet only grows with fresh postings, and you pay only for those (plus USD 0.001 per watched company per run).

Tip: instead of polling, you can also set `notifyWebhookUrl` to a Make **Custom webhook** and receive a JSON summary only when something changed.
