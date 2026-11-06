# Ready-made alert inputs by sector ("avisame de cada licitación nueva de mi rubro")

Copy one input, set **Monitor mode** + a Slack or webhook URL, and schedule the Actor daily (Schedules → Create schedule → every day 07:00). Each morning you get only the new tenders of your sector, plus deadline extensions and awards of tenders you already received.
The `sectors` packs match Spanish (Colombia, Chile) and Portuguese (Brazil) keywords in the tender title and the main UNSPSC category; add your own `keywords` for niche products and `excludeKeywords` to remove noise.

| Sector | Input |
|---|---|
| IT, software & computers | `{ "sectors": ["it-software"], "publishedWithinDays": 7, "monitorMode": true }` |
| Construction & public works over USD 100k | `{ "sectors": ["construction"], "minAmountUsd": 100000, "publishedWithinDays": 7, "monitorMode": true }` |
| Cleaning & facility services in São Paulo and Bogotá | `{ "sectors": ["cleaning"], "regions": ["SP", "Bogotá"], "publishedWithinDays": 7, "monitorMode": true }` |
| Security & surveillance (guards, CCTV) | `{ "sectors": ["security"], "publishedWithinDays": 7, "monitorMode": true }` |
| Medical supplies, drugs & lab (Brazil) | `{ "countries": ["BR"], "sectors": ["medical"], "publishedWithinDays": 7, "monitorMode": true }` |
| Food & school meals | `{ "sectors": ["food"], "publishedWithinDays": 7, "monitorMode": true }` |
| Vehicles, parts, tyres & fuel | `{ "sectors": ["vehicles"], "publishedWithinDays": 7, "monitorMode": true }` |
| Office supplies & furniture (small tenders) | `{ "sectors": ["office-supplies"], "maxAmountUsd": 50000, "publishedWithinDays": 7, "monitorMode": true }` |
| Consulting, audit & engineering studies | `{ "sectors": ["consulting"], "publishedWithinDays": 7, "monitorMode": true }` |
| Telecom & connectivity | `{ "sectors": ["telecom"], "publishedWithinDays": 7, "monitorMode": true }` |
| Electrical, lighting & solar | `{ "sectors": ["energy"], "publishedWithinDays": 7, "monitorMode": true }` |
| Events, travel & lodging | `{ "sectors": ["events-travel"], "publishedWithinDays": 7, "monitorMode": true }` |
| Training & education services | `{ "sectors": ["training-education"], "publishedWithinDays": 7, "monitorMode": true }` |
| Uniforms, workwear & PPE | `{ "sectors": ["uniforms-ppe"], "publishedWithinDays": 7, "monitorMode": true }` |
| Waste management & environment | `{ "sectors": ["waste-environment"], "publishedWithinDays": 7, "monitorMode": true }` |
| Your own product (e.g. ambulances) | `{ "keywords": ["ambulancia", "ambulância"], "publishedWithinDays": 7, "monitorMode": true }` |
| One buyer you follow (e.g. a ministry or a city) | `{ "buyers": ["899999063", "Prefeitura de Belo Horizonte"], "status": [], "publishedWithinDays": 7, "monitorMode": true }` |
| Who wins in my sector (competitive intelligence) | `{ "countries": ["CO"], "sectors": ["it-software"], "status": ["awarded"], "publishedWithinDays": 60, "awardeeData": "omitIndividuals" }` |

Add to any of them: `"notifySlackWebhookUrl": "https://hooks.slack.com/services/T000/B000/XXXX"` or `"notifyWebhookUrl": "https://hooks.zapier.com/hooks/catch/123/abc"`.
