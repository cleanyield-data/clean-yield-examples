# Chile Mercado Público tenders without an API ticket

New public tenders from Chile's Mercado Público with no API ticket: buyer RUT, region, bid deadline in Chile time and amount in CLP and USD.

- Actor: [Latin America Public Tenders](https://apify.com/cleanyield/latam-public-tenders)
- Real run: 3 results in 8.3 s (refreshed 2026-11-06)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** Reads Mercado Público's public OCDS open data, which can lag the portal by a few hours. Tenders without a published estimated amount have amount null.
