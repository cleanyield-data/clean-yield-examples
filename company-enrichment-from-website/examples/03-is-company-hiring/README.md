# Check if a company is hiring: careers page, ATS and open roles

For each company website, find the careers page, detect the applicant tracking system from its links (Greenhouse, Lever, Ashby, Workable, Workday, Recruitee and more) and, for Greenhouse, Lever and Ashby, count open roles through their public job board API. A clear evidence sentence explains every isHiring value.

- Actor: [Company Enrichment from Website](https://apify.com/cleanyield/company-enrichment-from-website)
- Real run: 3 results in 2.1 s (refreshed 2026-11-06)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** Open roles are counted only when the ATS has a public read-only API (Greenhouse, Lever, Ashby) or the page publishes JobPosting data; otherwise openRolesCount is null. Careers pages that load jobs only with JavaScript are marked as hiring unless they say there are no openings.
