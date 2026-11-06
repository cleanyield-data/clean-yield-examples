// Latin America Public Tenders - run it from Node.js with the official Apify client.
//
// Store page: https://apify.com/cleanyield/latam-public-tenders
//
//   npm install apify-client
//   export APIFY_TOKEN=<YOUR_APIFY_TOKEN>
//   node example.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN ?? '<YOUR_APIFY_TOKEN>' });

const input = {
    "countries": [
        "CO",
        "BR",
        "CL"
    ],
    "sectors": [
        "it-software"
    ],
    "status": [
        "open"
    ],
    "publishedWithinDays": 5,
    "maxResults": 15
};

// Starts the Actor and waits for it to finish.
const run = await client.actor('cleanyield/latam-public-tenders').call(input);
if (run.status !== 'SUCCEEDED') throw new Error(`Run did not succeed: ${run.status}`);

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`Got ${items.length} results`);
for (const item of items.slice(0, 3)) console.log(JSON.stringify(item, null, 2).slice(0, 800));
