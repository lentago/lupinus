# Five shops, one tech person each

*Every organization and person below is invented. Every product claim is tagged.*

**What this is.** Five made-up organizations, each small enough that one person does the computers, each paying for something built for a company a thousand times their size. For each one: what they pay for today, the night it broke, and the path out, product by product.

**Why bother.** Salesforce and ServiceNow don't lose these customers to a competitor. They lose them to a volunteer who finally asks, "what are we actually using this for?" These stories are that question, asked five times, with receipts.

**How to read the tags.** Every capability in every story carries one of three tags, and the tag is the honest part:

| Tag | Meaning |
|---|---|
| **Shipped** | It exists in the fleet today, and the link goes to the repo, file, or receipt that proves it. |
| **Free tier** | Not ours. Something the org already has or can get for nothing (GitHub Issues, a Grafana free account, a payment processor's hosted page). We show how to use it; we don't build it. |
| **Projected** | Not built yet. The link goes to the open issue it would become. Reading a projected tag as a promise is a mistake. Reading it as a roadmap is the point. |

**What we won't pretend.** Nothing in the suite is a donor database, a case-management system, or a ticketing product, and [lupinus says so plainly](https://github.com/lentago/lupinus/blob/main/guide/picker.md). The shops below kick Salesforce and ServiceNow to the curb anyway, because what they were buying was never the database. It was a campaign page, a calendar of deadlines, a place to write things down, and somebody to call. Those we can do, and most of it is already free.

## The five shops

Smallest first.

1. [Pennywell Street Pantry](01-pennywell-street-pantry.md): all-volunteer, zero staff, one retired engineer who does the computers.
2. [Ridgeback Valley Family Shelter](02-ridgeback-valley-family-shelter.md): twelve staff, one tech director, a ServiceNow contract inherited from a departed MSP.
3. [Stillwater Brook Watershed Alliance](03-stillwater-brook-watershed-alliance.md): four staff, a hatchery cooler, sensors in a river, a visitor-center screen.
4. [Paper Lantern Players](04-paper-lantern-players.md): a community theatre whose domain lapsed on a former volunteer's account.
5. [Understory Fiscal Collective](05-understory-fiscal-collective.md): a fiscal sponsor with fifteen projects and one tech person for all of them.

---


## Coverage: which story needs which piece

Shipped is **S**, free tier is **F**, projected is **P**. Blank means the story doesn't use it.

| Piece | Pantry | Shelter | Watershed | Theatre | Collective |
|---|---|---|---|---|---|
| monarda campaign site | S | | | S | S |
| lupinus ops vault | S | S | | | S |
| GitHub Issues as help desk | | F | F | | F |
| PR as change record / asclepias glossary | | S | | | S |
| drosera dashboards and alerts | | S | S | | |
| drosera status page / are-we-open #197 | | | S + P | P | |
| betula log capture | | S | S (client P) | | |
| kalmia workstations / donated-hardware #107 | | S + P | | | |
| epigaea / cold-chain kit #129 | | | S + P | | |
| brasenia wall display | | | S + P | | |
| claytonia agent fleet | | | | | S |
| mitchella front desk | | S (partial) | | | S (partial) |
| osmunda cluster / n8n | | | | | S (n8n draft) |
| repo-template + shared-workflows | | S | | | S |
| Liberation Pipeline #123 | P | | P | P | P |
| Good-Standing Kit #122 | P | | | P | |
| Digital Custody audit #124 | | | | P | P |
| Insurance-Receipts Pack #125 | | P | | | |
| Institutional Memory #126 | | P | | | |
| AI-with-receipts #127 | | | | | P |
| Ask-the-Records #128 | | | P | | |
| Funder-report pipeline #130 | | P | | | P |
| Privacy posture #131 | | | | | P |
| Volunteer scheduling spike #132 | | | | P | |
| Ops-in-a-Box #133 | | | | | P |
| Sensor trip opens an issue #195 | | | P | | |
| Help-desk starter #196 | | P | | | P |

## What the stories say about build order

If the goal is to develop hard, the stories vote. Counted by how many of the five shops need it to finish their exit:

| Projected piece | Stories | Why it ranks |
|---|---|---|
| Liberation Pipeline #123 | 4 | It is the exit itself. No shop leaves Salesforce safely without an owned, drilled export. Effort M on the roadmap. |
| Good-Standing Kit #122 | 2 | The deadline calendar is the part of a CRM a tiny shop actually used. Already first in the offerings queue. |
| Digital Custody audit #124 | 2 | Effort S, impact high, and the theatre story is entirely this kit. The renewal-check workflow it builds on already runs. |
| monarda dry-run receipt, monarda#5 | 3 | Not a new feature. Three stories lean on monarda and it has never been timed. Cheapest credibility in the fleet. |
| mitchella M1 | 2 | One live API call turns "partial" into "shipped" in two stories. |
| Funder-report pipeline #130 | 2 | The billable-change-request killer. Depends on the fact-base pattern that already runs on pondviewlane. |
| Cold-chain kit #129 | 1 | One story, but the most vivid one, and a month of catches on our own hardware is the receipt that sells it. |

Two pieces these stories needed that had no issue until they were written, filed 2026-10-01:

- **A sensor trip opens an issue**, [.github#195](https://github.com/lentago/.github/issues/195). The watershed story's work-order replacement: a small epigaea automation plus the Actions-cron-and-Issues runtime ADR-0007 already prefers.
- **A help-desk starter for a private repo**, [.github#196](https://github.com/lentago/.github/issues/196). Issue forms, labels, and a board, packaged the way repo-template packages a public repo. Both the shelter and the collective reach for it.

> 🌱 **Lentago Labs** is a pro-bono operations practice for organizations that
> run on volunteers, donations, and one overworked tech person. Everything here
> is free to take, and we practice what we publish: our own estate runs this
> way, in the open. Start at the [org profile](https://github.com/lentago), and
> read this repo on [DeepWiki](https://deepwiki.com/lentago/lupinus).
