# Find which ATS a company uses (Greenhouse, Lever or Ashby)

Give company names or careers pages and the Actor tells you which ATS each one uses and its board URL: Figma (found from its careers page link), Scale AI (name tried on the three ATS), Match Group (Lever). Companies not on these ATS are reported for free in the COMPANIES record with a clear message.

- Actor: [ATS Jobs Scraper](https://apify.com/cleanyield/ats-jobs-scraper)
- Real run: 9 results in 3.7 s (refreshed 2026-11-05)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** Only Greenhouse, Lever and Ashby are detected. Companies on Workday, Workable, SmartRecruiters or a custom ATS come back as notFound (free).
