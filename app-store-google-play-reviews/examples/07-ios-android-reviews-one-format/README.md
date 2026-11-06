# All iOS & Android reviews of one app in a single JSON format

Every review you ask for from the App Store and Google Play in one run and one schema, each row tagged with app, store and country. No 10-review cap.

- Actor: [App Store & Google Play Reviews](https://apify.com/cleanyield/app-store-google-play-reviews)
- Real run: 400 results in 3.5 s (refreshed 2026-11-06)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** Apple's public feed lists up to about 500 recent reviews per country; Google Play has no country filter (it groups by language), so country is null there. Ratings without text are not listed by either store.
