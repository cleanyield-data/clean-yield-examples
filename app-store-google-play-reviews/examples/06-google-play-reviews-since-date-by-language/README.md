# Google Play reviews since a date, in Spanish and Portuguese

Returns only Google Play reviews written in the last few days, in two languages, newest first. Because results are sorted newest first, the Actor stops paging as soon as it passes the date: fast and cheap for weekly reports after a release.

- Actor: [App Store & Google Play Reviews](https://apify.com/cleanyield/app-store-google-play-reviews)
- Real run: 80 results in 1 s (refreshed 2026-11-05)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** The date is the review date shown by Google, which is updated when a user edits the review. Relative periods (3 days, 2 weeks) are computed from the run start time.
