# Compare your app reviews against competitors (Uber vs Lyft vs Bolt)

Fetches recent reviews for your app and your competitors on both stores and builds deterministic, actionable alerts: a new version rated lower than the previous one, negative Google Play reviews left without a reply, and how your app ranks against each competitor on the same store. The first app of each store in the list is treated as yours.

- Actor: [App Store & Google Play Reviews](https://apify.com/cleanyield/app-store-google-play-reviews)
- Real run: 2000 results in 8.6 s (refreshed 2026-11-05)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** Week-over-week alerts need reviews covering 14 days: for very popular apps keep monitor mode running for two weeks (it accumulates history) or raise maxReviewsPerApp. App Store and Google Play ratings are never mixed in one ranking.
