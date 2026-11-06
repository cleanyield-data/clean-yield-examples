# Pregão eletrônico for medical supplies in São Paulo (PNCP)

Open reverse auctions (pregão eletrônico) for drugs, hospital supplies and medical equipment published on Brazil's PNCP in the last 3 days by buyers in the state of São Paulo. Includes the buyer CNPJ, estimated value in BRL and USD, deadline in Brasília time and UTC, and the e-procurement system where bids are submitted.

- Actor: [Latin America Public Tenders](https://apify.com/cleanyield/latam-public-tenders)
- Real run: 10 results in 2.6 s (refreshed 2026-11)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** PNCP does not classify tenders with UNSPSC: the medical sector matches Portuguese keywords in the title. The PNCP API is slow at times; requests are retried automatically.
