# Colombia SECOP II open tenders with bid deadlines

Open competitive SECOP II tenders in Colombia for construction and consulting, each with its bid deadline, buyer NIT and amount in COP and USD.

- Actor: [Latin America Public Tenders](https://apify.com/cleanyield/latam-public-tenders)
- Real run: 3 results in 2.3 s (refreshed 2026-11-06)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** SECOP II open data publishes the bid deadline as a date (closingDate); the exact hour is not in the source, so closingAt is null for Colombia. Direct contracts and special-regime processes are left out by default because nobody can bid on them.
