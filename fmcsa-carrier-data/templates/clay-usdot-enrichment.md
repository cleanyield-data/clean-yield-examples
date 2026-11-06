# Clay: enrich a list of carriers by USDOT (or MC) number

Use the Actor as an HTTP enrichment column (sync mode, ~3–6 s per row).

1. Table with a column `USDOT` (or `MC`).
2. Add column → **HTTP API**:
   - Method: `POST`
   - URL: `https://api.apify.com/v2/acts/cleanyield~fmcsa-carrier-data/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>`
   - Body (JSON): `{ "dotNumbers": ["{{USDOT}}"], "includeInsurance": true }`
     (for MC numbers: `{ "mcNumbers": ["{{MC}}"] }`)
3. Map the first item of the response to columns:
   - `legalName`, `dbaName`, `usdotStatus`, `outOfService`, `authorityStatus`, `mcNumbers[0]`
   - `powerUnits`, `drivers`, `phone`, `email`, `physicalAddress.state`
   - `authority.bipdOnFileUsd`, `insurancePolicies[0].insurer`, `insurancePolicies[0].effectiveDate`
4. Optional: chain **Company Enrichment from Website** (`cleanyield/company-enrichment-from-website`) on the email domain for website, social profiles and technologies.

Cost: USD 0.005 per carrier found; numbers that don't exist are not charged.
