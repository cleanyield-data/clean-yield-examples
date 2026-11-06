# App Store & Google Play Reviews

Reviews from the Apple App Store and Google Play in one clean schema, by country and language, with developer replies.

**Run it on Apify:** https://apify.com/cleanyield/app-store-google-play-reviews

Pay per result: you only pay for valid results; failed lookups are free and there are no platform usage fees.

## Real examples (input + output)

| Example | Real run |
|---|---|
| [Scrape negative App Store reviews (1–2 stars) for any app](examples/01-negative-app-store-reviews/) | 30 results · 2.2 s |
| [Google Play reviews with developer replies](examples/02-google-play-reviews-with-developer-replies/) | 50 results · 0.9 s |
| [Compare your app reviews against competitors (Uber vs Lyft vs Bolt)](examples/03-compare-app-reviews-vs-competitors/) | 2000 results · 8.6 s |
| [Monitor new App Store and Google Play reviews with Slack alerts for 1–2★](examples/04-monitor-new-app-reviews-slack-alerts/) | 60 results · 1.2 s |
| [App Store reviews by country (US, UK, Germany, France)](examples/05-app-store-reviews-by-country/) | 40 results · 2.5 s |
| [Google Play reviews since a date, in Spanish and Portuguese](examples/06-google-play-reviews-since-date-by-language/) | 80 results · 1 s |
| [All iOS & Android reviews of one app in a single JSON format](examples/07-ios-android-reviews-one-format/) | 400 results · 3.5 s |

## Ready-to-use templates

| Template | Type |
|---|---|
| [`clay-app-rating-and-recent-sentiment.md`](templates/clay-app-rating-and-recent-sentiment.md) | step-by-step guide |
| [`make-negative-app-reviews-to-slack.md`](templates/make-negative-app-reviews-to-slack.md) | step-by-step guide |
| [`n8n-negative-app-reviews-to-slack.json`](templates/n8n-negative-app-reviews-to-slack.json) | n8n workflow (import from file) |
| [`n8n-weekly-app-reviews-to-google-sheets.json`](templates/n8n-weekly-app-reviews-to-google-sheets.json) | n8n workflow (import from file) |

## Code

- `python/example.py` and `javascript/example.mjs`: run the Actor and print the results.
- `n8n/workflow.json` and `make/README.md`: no-code setup.

Use your own Apify API token as an environment variable (`APIFY_TOKEN`); never commit it.
