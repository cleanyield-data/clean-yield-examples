# Google Play reviews with developer replies

Gets the newest Google Play reviews of an Android app with the developer reply text and date, helpful votes (thumbs up) and the app version. Good for auditing how a support team answers reviews or for benchmarking a competitor's response rate.

- Actor: [App Store & Google Play Reviews](https://apify.com/cleanyield/app-store-google-play-reviews)
- Real run: 50 results in 0.9 s (refreshed 2026-11-05)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** Google Play groups reviews by language, so country is null; pick the languages you need. Reply dates come from Google and may be older than an edited review date.
