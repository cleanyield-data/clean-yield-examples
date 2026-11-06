# Lever postings API: export every job of several companies

Export all published Lever postings of Spotify and Palantir in one run, normalized to the same schema as Greenhouse and Ashby: team, department, commitment (normalized to full_time, contract, internship…), workplace type (remote/hybrid/onsite), every location and the apply link. Without descriptions the output is light and fast: 394 jobs.

- Actor: [ATS Jobs Scraper](https://apify.com/cleanyield/ats-jobs-scraper)
- Real run: 395 results in 3.1 s (refreshed 2026-11-05)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** Lever rarely publishes structured salaries; when the description states a range (common for US and Canada roles) it is extracted with salarySource: description. Requests to Lever are spaced 1 second apart as its robots.txt asks.
