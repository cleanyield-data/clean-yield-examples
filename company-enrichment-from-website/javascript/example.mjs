// Company Enrichment from Website - run it from Node.js with the official Apify client.
//
// Store page: https://apify.com/cleanyield/company-enrichment-from-website
//
//   npm install apify-client
//   export APIFY_TOKEN=<YOUR_APIFY_TOKEN>
//   node example.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN ?? '<YOUR_APIFY_TOKEN>' });

const input = {
    "domains": [
        "plausible.io",
        "katzsdelicatessen.com",
        "tiendanube.com"
    ],
    "includePersonalEmails": false,
    "maxPagesPerDomain": 10
};

// Starts the Actor and waits for it to finish.
const run = await client.actor('cleanyield/company-enrichment-from-website').call(input);
if (run.status !== 'SUCCEEDED') throw new Error(`Run did not succeed: ${run.status}`);

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`Got ${items.length} results`);
for (const item of items.slice(0, 3)) console.log(JSON.stringify(item, null, 2).slice(0, 800));
