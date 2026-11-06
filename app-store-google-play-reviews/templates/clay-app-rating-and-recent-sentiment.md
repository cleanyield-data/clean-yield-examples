# Clay: enrich a list of companies' apps with recent review sentiment

Use case: you sell to mobile-first companies (or run an ASO agency). For each row with an App Store id or Google Play package, pull the most recent reviews and compute the recent average rating and share of 1–2★ reviews — a strong "pain" signal for outreach.

## Setup (HTTP API enrichment, sync mode)

1. Column `app` with an App Store URL/id or a Google Play URL/package (e.g. `com.duolingo`).
2. Add enrichment → **HTTP API**:
   - Method: `POST`
   - URL: `https://api.apify.com/v2/acts/cleanyield~app-store-google-play-reviews/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>`
   - Body:
     ```json
     { "apps": ["/app"], "countries": ["us"], "languages": ["en"], "maxReviewsPerApp": 50 }
     ```
     (replace `/app` with the Clay column reference).
   - Typical response time: 2–5 s for 50 reviews.
3. The response is an array of reviews. Add formula columns:
   - **Recent average**: `AVERAGE(response.map(r => r.rating))`
   - **Negative share**: `response.filter(r => r.isNegative).length / response.length`
   - **Latest complaint**: `response.find(r => r.isNegative)?.text`
   - **App name**: `response[0]?.appName`

## Cost

50 reviews per row = USD 0.005 per row (USD 0.10 per 1,000 reviews). 1,000 rows ≈ USD 5.
