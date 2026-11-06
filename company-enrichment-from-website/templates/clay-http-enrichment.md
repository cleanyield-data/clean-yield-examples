# Clay: company enrichment column via HTTP API (sync mode)

Use the Actor as an **HTTP API** enrichment in a Clay table that has a `Domain` (or `Website`) column. One request per row returns the company profile in a few seconds.

## Setup

1. In your Clay table: **Add enrichment → HTTP API**.
2. Method: `POST`
3. Endpoint:
   ```
   https://api.apify.com/v2/acts/cleanyield~company-enrichment-from-website/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>&timeout=60
   ```
4. Headers: `Content-Type: application/json`
5. Body:
   ```json
   { "domains": ["/Domain"], "sections": ["contacts", "social", "technologies", "hiring", "posts"], "domainTimeoutSecs": 15 }
   ```
   (`/Domain` is Clay's column reference; insert it with the column picker.)
6. Rate limit: 5–10 requests per second is fine. Turn on **Only run if** `Domain` is not empty.

## Output columns to map

The response is an array with one object (or empty if the site could not be enriched — not charged):

| Clay column | JSON path |
|---|---|
| Company name | `[0].companyName` |
| Generic email | `[0].emails[0].email` |
| Email type | `[0].emails[0].type` |
| Phone (E.164) | `[0].phones[0].phone` |
| LinkedIn | `[0].socialProfiles.linkedin` |
| X | `[0].socialProfiles.x` |
| Tech stack | `[0].technologies` (map `name`) |
| Is hiring | `[0].hiring.isHiring` |
| Open roles | `[0].hiring.openRolesCount` |
| ATS | `[0].hiring.atsProvider` |
| Latest post | `[0].latestPosts[0].title` / `[0].latestPosts[0].url` |
| Country | `[0].country` |

## Tips

- Personal emails are off by default (GDPR-friendly). Add `"includePersonalEmails": true` only if you have a legal basis.
- Use the **Buying signals** columns (hiring, technologies, latest post) to personalize your first line.
