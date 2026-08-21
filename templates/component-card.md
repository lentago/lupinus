<!-- TEMPLATE. Copy to estate/products/<name>.md when you adopt something.
     Delete these comments. Keep the frontmatter keys — they are what make the
     vault queryable later if you ever want that. -->

---
adopted-from: lentago/<product>
adopted: <YYYY-MM-DD>
tier: <Kit | Platform | Pattern>
receipt: journal/receipts/<product>-<YYYY-MM-DD>.md
owner: <who in your organization is responsible>
review: <YYYY-MM-DD — when to look at this again>
---

# <product> — <what it does for us, in your own words>

<!-- One or two sentences. Write it for a colleague who has never heard of it,
     or for yourself in eight months. Not marketing copy — what it actually
     does here. -->

## Depends on

<!-- THIS IS THE GRAPH. Every link here becomes an edge in the graph view, so
     write one link per real dependency and name the relationship in the text
     around it. Plain Markdown links only — never [[wikilinks]]. -->

- Runs in [<account>](../accounts/<account>.md)
- Deploys from [<account>](../accounts/<account>.md)
- Sends <what> to [<account>](../accounts/<account>.md)

## What it costs

<!-- Actual monthly number, and what drives it. Update when it changes; this
     is the number someone will ask you for at budget time. -->

## Where its runbook is

- Adoption: <link to the product's ADOPTION.md>
- Our receipt: <link to the journal entry from when we stood it up>

## What we changed

<!-- Every place you diverged from the stock product: values you swapped,
     features you turned off, things you added. Future-you will want this the
     first time an upgrade does something surprising. -->

## If this breaks

<!-- Who to tell, what to check first, and what depends on it being up.
     Two lines is fine. The point is that it is written down somewhere other
     than in one person's head. -->

## Exit

<!-- How we would leave: where the data is, what format it exports in, what
     would have to be rebuilt. Fill this in on the day you adopt, while it is
     still hypothetical and you are thinking clearly. -->
