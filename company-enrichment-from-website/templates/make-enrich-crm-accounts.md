# Make: enrich new CRM accounts with company data from their website

Every time a new account (company) is created in your CRM or a new row lands in a Google Sheet, enrich it with emails, phones, social profiles, tech stack and hiring signals, and write the result back.

## Modules

1. **Trigger**: Google Sheets → *Watch New Rows* (or HubSpot CRM → *Watch Companies*, Pipedrive → *Watch Organizations*). The row must have a `domain` (or website URL) column.
2. **Apify → Run an Actor**
   - Actor: `cleanyield/company-enrichment-from-website`
   - Run synchronously: **Yes** (typically 2–6 s per company; set timeout 120 s)
   - Input JSON:
     ```json
     { "domains": ["{{1.domain}}"], "sections": ["contacts", "social", "technologies", "hiring"], "domainTimeoutSecs": 15 }
     ```
3. **Apify → Get Dataset Items**
   - Dataset ID: `{{2.defaultDatasetId}}`, Limit: 1
   - If the dataset is empty, the site was down, parked, blocked or had no data: it was **not charged** (see `FAILED_DOMAINS` in the run's key-value store). Add a filter "items count > 0" before the next step.
4. **Google Sheets → Update a Row** (or CRM → *Update Company*), mapping:
   - `companyName` → Company name
   - `emails[1].email` → Email (generic/role inbox)
   - `phones[1].phone` → Phone (E.164)
   - `socialProfiles.linkedin` → LinkedIn
   - `technologies[]` (map `name`, join with ", ") → Tech stack
   - `hiring.isHiring`, `hiring.openRolesCount`, `hiring.atsProvider` → Hiring
   - `country` → Country (ISO-2)

## Connection

Apify app connection with your API token (`<YOUR_APIFY_TOKEN>`, from Apify Console → Settings → Integrations). Never paste the token into module fields that get logged.

## Cost

Fixed price per company returned; failed or empty sites are free. One new account = at most one charged result.
