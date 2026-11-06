# Monitor new App Store and Google Play reviews with Slack alerts for 1–2★

Schedule this input daily: the first run saves a baseline, every next run returns only reviews that are new since the previous run (changeType new) or edited by their author (changeType changed), and posts the new 1–2★ reviews to Slack or a webhook. Works for the iOS and Android versions of the same app in one run.

- Actor: [App Store & Google Play Reviews](https://apify.com/cleanyield/app-store-google-play-reviews)
- Real run: 60 results in 1.2 s (refreshed 2026-11-05)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** This sample is a first run (baseline), so every review is new. Monitor runs fetch newest-first and stop as soon as they reach reviews already seen, so daily runs usually need one request per app and country/language.
