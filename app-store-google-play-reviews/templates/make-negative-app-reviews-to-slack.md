# Make: new negative App Store & Google Play reviews → Slack (or email)

Every morning, get the new 1–2★ reviews of your iOS and Android app in a Slack channel. Monitor mode remembers what was already sent, so you never get the same review twice.

## Modules

1. **Apify → Run an Actor** (connection with your Apify token)
   - Actor: `cleanyield/app-store-google-play-reviews`
   - Run synchronously: **Yes**
   - Input JSON:
     ```json
     {
       "apps": ["https://apps.apple.com/us/app/YOUR-APP/id000000000", "com.yourcompany.yourapp"],
       "countries": ["us"],
       "languages": ["en"],
       "maxReviewsPerApp": 200,
       "maxRating": 2,
       "monitorMode": true,
       "monitorStateName": "my-app-negative-reviews-make"
     }
     ```
2. **Apify → Get Dataset Items**: Dataset ID = `defaultDatasetId` from module 1. Limit 200.
3. **Slack → Create a Message** (or **Gmail → Send an email**), one per item:
   - Text: `{{rating}}★ {{appName}} ({{store}} {{country}}{{language}}) v{{appVersion}}`
     `{{title}} {{text}}`
     `{{url}}`
4. Scenario schedule: **Every day** at 08:00.

## Notes

- `maxRating: 2` returns only 1–2★ reviews; remove it to get all new reviews.
- Cost: USD 0.005 per app per run + USD 0.10 per 1,000 new reviews (e.g. 2 apps checked daily with 15 new negative reviews a day ≈ USD 0.35 per month).
- Prefer zero setup? Put a Slack incoming webhook in `notifySlackWebhookUrl` and skip modules 2–3: the Actor posts the alert itself.
- Never paste your real token in shared scenarios: use `<YOUR_APIFY_TOKEN>` in blueprints.
