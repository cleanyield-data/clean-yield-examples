# Scrape negative App Store reviews (1–2 stars) for any app

Pulls only the 1–2★ reviews of an iOS app from one App Store country, newest first. Useful for support and product teams who want to read what is going wrong without scrolling through 5-star reviews. Each review comes with title, text, date, app version and a working link to the app reviews page.

- Actor: [App Store & Google Play Reviews](https://apify.com/cleanyield/app-store-google-play-reviews)
- Real run: 30 results in 2.2 s (refreshed 2026-11-05)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** App Store only exposes the ~500 most recent reviews per country, so a star filter searches within those. Apple does not provide developer replies or the review language.
