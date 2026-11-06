# Enrich Latin American companies from their website

Full company profiles for LATAM websites: phones normalized to E.164 with the right country code (+54, +55, +52), Spanish and Portuguese contact pages (contacto, contato, fale conosco, trabaja con nosotros, trabalhe conosco), WhatsApp links, and LATAM platforms like Tiendanube, VTEX and RD Station.

- Actor: [Company Enrichment from Website](https://apify.com/cleanyield/company-enrichment-from-website)
- Real run: 3 results in 4.2 s (refreshed 2026-11-06)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** Country is inferred from the address in structured data, the country TLD, international phone numbers or the page language region; .com sites without those signals get country null.
