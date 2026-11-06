# Plantillas para n8n, Make y Clay (canal principal fuera de la Store)

3–5 plantillas por Actor, listas para publicar en la biblioteca de n8n, las galerías de Make y comunidades de Clay.
Ejemplos de casos: "reseñas negativas nuevas → Slack", "enriquecer leads de una planilla", "cambios de precio → Google Sheets".

- `n8n-<slug>.json`: workflow exportado de n8n (importable con "Import from file"). Usar el nodo oficial
  de Apify o HTTP Request contra
  `https://api.apify.com/v2/acts/cleanyield~<actor>/run-sync-get-dataset-items?token=<YOUR_APIFY_TOKEN>`.
- `make-<slug>.md`: escenario de Make paso a paso (app de Apify "Run an Actor" + "Get Dataset Items" + destino), con el input en JSON.
- `clay-<slug>.md`: cómo usarlo como enriquecimiento HTTP en Clay (modo síncrono, columnas de entrada y de salida).

Nunca tokens reales: siempre `<YOUR_APIFY_TOKEN>`.
