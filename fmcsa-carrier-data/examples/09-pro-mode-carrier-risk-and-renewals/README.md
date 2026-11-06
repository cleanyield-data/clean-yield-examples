# Carrier risk score, insurance renewal and why-now (Pro mode)

Paste your USDOT numbers and tick Pro mode: each carrier gets a 0-100 risk score with the reasons behind it (out-of-service orders, insurance below the required minimum, revocations, out-of-service rates above the national average...), the estimated renewal date of its liability policy and a dated reason to contact it now.

- Actor: [FMCSA Carrier Data](https://apify.com/cleanyield/fmcsa-carrier-data)
- Real run: 3 results in 4 s (refreshed 2026-11)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** The risk score uses only FMCSA public data and fixed, published points (see README); it is not a credit or insurance rating. Insurance renewal is estimated as the anniversary of the current BIPD policy's effective date. The AI summary (insight) appears when the AI service is available; otherwise it is empty and not charged.
