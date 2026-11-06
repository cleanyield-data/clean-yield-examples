# Make: weekly email digest of new public tenders for your sector

For suppliers and consultancies that sell to the government in Colombia, Brazil and Chile: every Monday, one email with the tenders of your sector published in the last 7 days, only the ones you haven't received before, plus tenders you already got whose deadline was extended or that were awarded.

1. **Apify → Run an Actor** (connection with your Apify token).
   - Actor: `cleanyield/latam-public-tenders`
   - Run synchronously: **Yes**
   - Input (JSON):
     ```json
     {
       "countries": ["CO", "CL"],
       "sectors": ["construction"],
       "regions": ["Antioquia", "Valparaíso", "Metropolitana"],
       "status": ["open"],
       "publishedWithinDays": 8,
       "minAmountUsd": 50000,
       "maxResults": 300,
       "monitorMode": true,
       "monitorStateName": "make-construction-weekly"
     }
     ```
2. **Apify → Get Dataset Items** — Dataset ID: the `defaultDatasetId` from step 1, format JSON, limit 300.
3. **Tools → Text aggregator** over the items, one line per tender:
   `{{country}} · {{title}} · {{buyer.name}} · {{amount.currency}} {{amount.value}} (~USD {{amount.valueUsd}}) · closes {{closingAtLocal}} · {{url}}`
   Tip: add a filter before the aggregator with `changeType = changed` for a second section "Updates on tenders you already know" and show `changes[].note` (e.g. "deadline extended by 7 days", "awarded").
4. **Email / Gmail → Send an email** to your sales team with the aggregated text.
5. Schedule the scenario: **Every week, Monday 07:00**.

Each tender is charged once (USD 0.008); unchanged tenders in later weeks are free. Never paste your real token in shared blueprints: use `<YOUR_APIFY_TOKEN>`.
