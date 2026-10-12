# Five shops, one tech person each

*Every organization and person below is invented. Every product claim is tagged.*

**What this is.** Five made-up organizations, each small enough that one person does the computers, each paying for something built for a company a thousand times their size. For each one: what they pay for today, the night it broke, and the path out in three rungs: this weekend, this quarter, this year. Every step is headed by what it does for the shop, one of the promises on [the map](#the-map), not by the name of a product.

**Why bother.** Salesforce and ServiceNow don't lose these customers to a competitor. They lose them to a volunteer who finally asks, "what are we actually using this for?" These stories are that question, asked five times, with receipts.

**How to read the tags.** Every capability in every story carries one of three tags, and the tag is the honest part:

| Tag | Meaning |
|---|---|
| **Shipped** | It exists in the fleet today, and the link goes to the repo, file, or receipt that proves it. |
| **Free tier** | Not ours. Something the org already has or can get for nothing (GitHub Issues, a Grafana free account, a payment processor's hosted page). We show how to use it; we don't build it. |
| **Projected** | Not built yet. The link goes to the open issue it would become. Reading a projected tag as a commitment is a mistake. Reading it as a roadmap is the point. |

**What we won't pretend.** Nothing in the suite is a donor database, a case-management system, or a ticketing product, and [lupinus says so plainly](https://github.com/lentago/lupinus/blob/main/guide/picker.md). The shops below kick Salesforce and ServiceNow to the curb anyway, because what they were buying was never the database. It was a campaign page, a calendar of deadlines, a place to write things down, and somebody to call. Those we can do, and most of it is already free.

## The five shops

Smallest first.

1. [Pennywell Street Pantry](01-pennywell-street-pantry.md): all-volunteer, zero staff, one retired engineer who does the computers.
2. [Ridgeback Valley Family Shelter](02-ridgeback-valley-family-shelter.md): twelve staff, one tech director, a ServiceNow contract inherited from a departed MSP.
3. [Stillwater Brook Watershed Alliance](03-stillwater-brook-watershed-alliance.md): four staff, a hatchery cooler, sensors in a river, a visitor-center screen.
4. [Paper Lantern Players](04-paper-lantern-players.md): a community theatre whose domain lapsed on a former volunteer's account.
5. [Understory Fiscal Collective](05-understory-fiscal-collective.md): a fiscal sponsor with fifteen projects and one tech person for all of them.

---


## The map

Every story uses the same map. The fleet's offer is six promises every shop needs, plus three for when you need them (recorded in [ADR-0012](https://github.com/lentago/.github/blob/main/docs/adr/0012-six-promises-codenames-are-parts.md), an architecture decision record: the fleet's written-down reasons for a choice), in these words:

- **Your site and giving page** — a campaign page you own outright, with a
  donate button that goes straight to your payment processor.
- **Your records and your proof** — minutes, policies, and filings in one vault,
  the posting rules beside them, and a public board that shows what went up on
  time. When the board, the auditor, the funder, or the insurer asks, you send
  a link.
- **Your machines and logins** — every laptop set up the same way, every login
  with a named owner, and leaving is a pull request, a proposed change someone
  else reviews before it lands.
- **Your alarms and status** — know when something breaks before the executive
  director does, and a file that says who gets the call.
- **Your help desk and runbooks** — requests land in a list, answers come from
  runbooks you wrote once, and the front desk answers at 9 pm.
- **Your data and your exit** — every export you'd need to leave a vendor, on a
  schedule, into a repo you own, with a restore you've drilled.

When you need them: **your building** (sensors, and a lobby screen that says
whether you're open), **cloud you own** (a real AWS environment in your account,
as code), **AI with receipts** (agents that open pull requests and never merge).

![The map. Six promises every shop needs: your site and giving page, your records and your proof, your machines and logins, your alarms and status, your help desk and runbooks, your data and your exit. Three for when you need them: your building, cloud you own, AI with receipts. Below them, what is free and not ours. The guide runs down the side as the spine, and the pledge sits under everything.](map.svg)

The guide is the spine, not a product: [asclepias](https://github.com/lentago/asclepias) is volume 1 (see it working on our estate first) and [lupinus](https://github.com/lentago/lupinus) is volume 2 (make it yours). Under all of it sits the pledge ([ADR-0007](https://github.com/lentago/.github/blob/main/docs/adr/0007-client-owned-delivery-no-multi-tenant-saas.md)):

> **The pledge** — We will never host your systems for you. You'll own every
> piece, we'll show your people how to run it, and firing us is a runbook.

## The parts

Each product, the *part*, sits under exactly one promise. Its name is a codename (a plant's Latin name, the way every product here is named); its role says what it does in plain words. The tier, meaning how much of it you can stand up from the repository alone, lives only in the [tier registry](../tiers.md).

This table is the canonical product list. The [picker](../picker.md), the [tier registry](../tiers.md) and the [runbook index](../runbook-index.md) are checked against it on every pull request by [`ci/check_product_list.py`](../../ci/check_product_list.py): a product those pages name must be on this list, and every part under a promise must have a row in the tier registry. A new product starts here.

<!-- parts:start -->
| Promise | Part | Role | Where it lives |
|---|---|---|---|
| Your site and giving page | monarda | campaign page | [lentago/monarda](https://github.com/lentago/monarda) |
| Your records and your proof | uvularia | records and deadlines | [lentago/uvularia](https://github.com/lentago/uvularia) |
| Your machines and logins | kalmia | machine setup | [lentago/kalmia](https://github.com/lentago/kalmia) |
| Your alarms and status | drosera | alerts and status | [lentago/drosera](https://github.com/lentago/drosera) |
| Your alarms and status | betula | capture and keep (its exports also serve your data and your exit) | [lentago/betula](https://github.com/lentago/betula) |
| Your help desk and runbooks | mitchella | front desk | [lentago/mitchella](https://github.com/lentago/mitchella) |
| Your data and your exit | lock-in ledger | what you'd lose | [lentago/.github, fleet-reports/lock-in](https://github.com/lentago/.github/tree/main/fleet-reports/lock-in) |
| Your building | epigaea | building sensors | [lentago/epigaea](https://github.com/lentago/epigaea) |
| Your building | brasenia | lobby screen | [lentago/brasenia](https://github.com/lentago/brasenia) |
| Cloud you own | solidago | cloud you own (AWS) | [lentago/solidago](https://github.com/lentago/solidago) |
| Cloud you own | osmunda | cloud you own (Kubernetes) | [lentago/osmunda](https://github.com/lentago/osmunda) |
| AI with receipts | claytonia | AI with receipts | [lentago/claytonia](https://github.com/lentago/claytonia) |
| The guide (spine) | asclepias | volume 1: see it working on ours | [lentago/asclepias](https://github.com/lentago/asclepias) |
| The guide (spine) | lupinus | volume 2: make it yours, and the ops vault you keep under your help desk and runbooks | [lentago/lupinus](https://github.com/lentago/lupinus) |
| The guide (spine) | repo-template | how a new repository starts | [lentago/repo-template](https://github.com/lentago/repo-template) |
| The guide (spine) | shared-workflows | the checks every repository runs | [lentago/shared-workflows](https://github.com/lentago/shared-workflows) |
<!-- parts:end -->

The spine rows aren't tiered products, so the tier registry may skip them. The [support page](../../support/README.md) lists every part too, so you know where to report a problem with it, but that page is yours to edit in your copy, so the check leaves it alone.

## Coverage: which story needs which promise

Shipped is **S**, free tier is **F**, projected is **P**. The parts each shop uses sit in the cell. **Spine** marks the one promise each story is built around. Blank means the story doesn't use it.

| Promise | Pantry | Shelter | Watershed | Theatre | Collective |
|---|---|---|---|---|---|
| **Your site and giving page** | **Spine.** monarda S · processor's hosted page F | | | monarda S | monarda S |
| **Your records and your proof** | uvularia S · Good-Standing [.github#122](https://github.com/lentago/.github/issues/122) P | Insurance-Receipts [.github#125](https://github.com/lentago/.github/issues/125) P · funder report [.github#130](https://github.com/lentago/.github/issues/130) P | uvularia S · Ask box [.github#200](https://github.com/lentago/.github/issues/200) P | Good-Standing [.github#122](https://github.com/lentago/.github/issues/122) P | funder report [.github#130](https://github.com/lentago/.github/issues/130) P |
| **Your machines and logins** | | kalmia S · donated hardware [kalmia#107](https://github.com/lentago/kalmia/issues/107) P | | | |
| **Your alarms and status** | | drosera S · betula S | drosera S, dashboards and status page · are-we-open [drosera#197](https://github.com/lentago/drosera/issues/197) P · betula S, sensor client [betula#74](https://github.com/lentago/betula/issues/74) P | are-we-open [drosera#197](https://github.com/lentago/drosera/issues/197) P | |
| **Your help desk and runbooks** | ops vault S | **Spine.** GitHub Issues F · repo-template S · help-desk starter [.github#196](https://github.com/lentago/.github/issues/196) P · ops vault S · Institutional Memory [.github#126](https://github.com/lentago/.github/issues/126) P · mitchella S (partial) | | | GitHub Issues F · help-desk starter [.github#196](https://github.com/lentago/.github/issues/196) P · ops vault S · mitchella S (partial) |
| **Your data and your exit** | processor's export F · Liberation Pipeline [.github#123](https://github.com/lentago/.github/issues/123) P | | processor's export F · Liberation Pipeline [.github#123](https://github.com/lentago/.github/issues/123) P | **Spine.** lock-in renewal check S · Digital Custody [.github#124](https://github.com/lentago/.github/issues/124) P · ticketing export F · Liberation Pipeline [.github#123](https://github.com/lentago/.github/issues/123) P | Digital Custody [.github#124](https://github.com/lentago/.github/issues/124) P · Liberation Pipeline [.github#123](https://github.com/lentago/.github/issues/123) P · privacy posture [.github#131](https://github.com/lentago/.github/issues/131) P |
| *When you need it:* **your building** | | | **Spine.** epigaea S · cold-chain kit [.github#129](https://github.com/lentago/.github/issues/129) P · GitHub Issues F · sensor trip opens an issue [.github#195](https://github.com/lentago/.github/issues/195) P · brasenia S · Cast-native path [brasenia#12](https://github.com/lentago/brasenia/issues/12) P | | |
| *When you need it:* **cloud you own** | | | | | osmunda S (n8n draft) |
| *When you need it:* **AI with receipts** | | | | | **Spine.** claytonia S · reviewed-merge page [.github#127](https://github.com/lentago/.github/issues/127) P |

Two lines sit outside the nine rows. The guide itself: the shelter leans on the [asclepias glossary](https://github.com/lentago/asclepias/blob/main/manual/glossary.md) (S) for change management as a pull request, and the collective starts every project from repo-template and shared-workflows (S) and, later, [Ops-in-a-Box](https://github.com/lentago/.github/issues/133) (P). And one thing on no promise, on purpose: the theatre's volunteer scheduling is a [spike, .github#132](https://github.com/lentago/.github/issues/132) (P), a short look that ends in a decision memo, not a build.

## What the stories say about build order

If the goal is to develop hard, the stories vote. Counted by how many of the five shops need it to finish their exit:

| Projected piece | Stories | Why it ranks |
|---|---|---|
| Liberation Pipeline #123 | 4 | It is the exit itself. No shop leaves Salesforce safely without an owned, drilled export. Effort M on the roadmap. |
| Good-Standing Kit #122 | 2 | The deadline calendar is the part of a CRM a tiny shop actually used. The calendar itself already ships in uvularia; checking filings against the public registries is what remains. |
| Digital Custody audit #124 | 2 | Effort S, impact high, and the theatre story is entirely this kit. The renewal-check workflow it builds on already runs. |
| monarda dry-run receipt, monarda#5 | 3 | Done 2026-10-12: timed at 3 min 01 s ([receipt](https://github.com/lentago/monarda/blob/main/receipts/2026-10-12-agent-run.md)), two defects found and filed as issues. Three stories lean on it. |
| mitchella M1 | 2 | One live API call turns "partial" into "shipped" in two stories. |
| Funder-report pipeline #130 | 2 | The billable-change-request killer. It reads the uvularia records vault, which ships today, as the vault's first consumer ([uvularia#92](https://github.com/lentago/uvularia/issues/92)). |
| Cold-chain kit #129 | 1 | One story, but the most vivid one, and a month of catches on our own hardware is the receipt that sells it. |

Two pieces these stories needed that had no issue until they were written, filed 2026-10-01:

- **A sensor trip opens an issue**, [.github#195](https://github.com/lentago/.github/issues/195). The watershed story's work-order replacement: a small epigaea automation plus the Actions-cron-and-Issues runtime ADR-0007 already prefers.
- **A help-desk starter for a private repo**, [.github#196](https://github.com/lentago/.github/issues/196). Issue forms, labels, and a board, packaged the way repo-template packages a public repo. Both the shelter and the collective reach for it.

> 🌱 **Lentago Labs** is a pro-bono operations practice for organizations that
> run on volunteers, donations, and one overworked tech person. Everything here
> is free to take, and we practice what we publish: our own estate runs this
> way, in the open. Start at the [org profile](https://github.com/lentago).
