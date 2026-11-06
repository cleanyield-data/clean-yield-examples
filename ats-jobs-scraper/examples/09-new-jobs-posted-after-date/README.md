# Live job postings posted after a date (no expired jobs)

Jobs posted on or after an exact date at Greenhouse, Lever and Ashby companies, read live at run time: no closed jobs, no other company's rows.

- Actor: [ATS Jobs Scraper](https://apify.com/cleanyield/ats-jobs-scraper)
- Real run: 173 results in 4.9 s (refreshed 2026-11-06)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** Only Greenhouse, Lever and Ashby boards. The date is the publish date the ATS reports; a few boards reset it when a job is reposted, so a reposted job counts as new. Jobs without a publish date are left out.
