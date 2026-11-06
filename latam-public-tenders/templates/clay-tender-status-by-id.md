# Clay: check status, deadline and winner of tenders by ID

Use the Actor as an HTTP enrichment column (sync mode, ~1–3 s per row) on a table of tenders you are following or bidding on.

1. Table with a column `Tender ID` — the id shown on each portal: `CO1.REQ.11304903` (SECOP II), `88124961000159-1-000131/2026` (PNCP "Id contratação PNCP"), `5751-39-LR26` (Mercado Público), or the `tenderId` from this Actor.
2. Add column → **HTTP API**:
   - Method: `POST`
   - URL: `https://api.apify.com/v2/acts/cleanyield~latam-public-tenders/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>`
   - Body (JSON): `{ "tenderIds": ["{{Tender ID}}"], "includeAwardees": true, "awardeeData": "omitIndividuals" }`
3. Map the first item of the response to columns:
   - `status` (open / closed / awarded / cancelled / unsuccessful / suspended), `statusOriginal`
   - `closingAtLocal` (deadline as shown on the portal), `closingAt` (UTC)
   - `amount.value`, `amount.currency`, `amount.valueUsd`
   - `awardees[0].name`, `awardees[0].taxId`, `awardedAmount.value` (who won and for how much)
   - `url` (official page)
4. Re-run the column weekly, or switch to monitor mode in Apify to be notified only when something changes.

Cost: USD 0.008 per tender found; ids that don't exist are not charged.
