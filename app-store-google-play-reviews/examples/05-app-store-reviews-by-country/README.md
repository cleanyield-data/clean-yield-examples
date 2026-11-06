# App Store reviews by country (US, UK, Germany, France)

Collects the newest App Store reviews of one iOS app from several country storefronts in one run, each tagged with its ISO country code. Useful for localization teams and for comparing sentiment across markets.

- Actor: [App Store & Google Play Reviews](https://apify.com/cleanyield/app-store-google-play-reviews)
- Real run: 40 results in 2.5 s (refreshed 2026-11-05)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** Each storefront has its own reviews and its own ~500 review cap. If the app is not available in a country, that country is skipped and reported in REVIEW_STATS.
