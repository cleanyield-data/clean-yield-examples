# Make: weekly new trucking companies → Google Sheets / CRM

Scenario for truck insurance agents and factoring companies: every Monday, the carriers registered in your states in the last 7 days, only the ones you haven't received before.

1. **Apify → Run an Actor** (module "Run an Actor", connection with your Apify token).
   - Actor: `cleanyield/fmcsa-carrier-data`
   - Run synchronously: **Yes**
   - Input (JSON):
     ```json
     {
       "states": ["FL", "GA"],
       "entityTypes": ["carrier"],
       "operationType": "interstate",
       "addedWithinDays": 7,
       "maxResults": 2000,
       "monitorMode": true,
       "monitorStateName": "make-new-carriers-fl-ga"
     }
     ```
2. **Apify → Get Dataset Items** — Dataset ID: `{{1.defaultDatasetId}}`, format JSON, limit 2000.
3. **Google Sheets → Add a Row** (or HubSpot / Pipedrive "Create a company"), mapping:
   - USDOT → `dotNumber` · Company → `companyName` · Legal name → `legalName`
   - Phone → `phone` (already E.164) · Email → `email`
   - City / State / ZIP → `physicalAddress.city` / `physicalAddress.state` / `physicalAddress.zip5`
   - Power units → `powerUnits` · Added → `addDate` · SAFER → `fmcsaUrl`
4. Schedule the scenario: **Every week, Monday 07:00**.

Tips: add a filter between 2 and 3 with `email` exists to keep only carriers with email; for CAN-SPAM, include your physical address and an opt-out in every email. Never paste your real token in shared blueprints: use `<YOUR_APIFY_TOKEN>`.
