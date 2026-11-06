# Detect a website's tech stack: Shopify, HubSpot, WordPress

Check which ecommerce platform, CMS, analytics, marketing automation, chat and payment tools a list of company websites uses. Detection is based on specific signatures (asset paths, script hosts, headers, cookies), not on the word appearing in the text, so a blog post about WordPress does not count as 'uses WordPress'.

- Actor: [Company Enrichment from Website](https://apify.com/cleanyield/company-enrichment-from-website)
- Real run: 3 results in 1.7 s (refreshed 2026-11-06)
- `input.json`: paste it in the Actor input (JSON tab) or send it to the API.
- `output-sample.json`: the first 5 results of that run.

**Limitations:** Tools that load only after user interaction or through a tag manager without traces in the HTML are not seen. Hosting/CDN and frameworks are included but do not count as a buying signal on their own.
