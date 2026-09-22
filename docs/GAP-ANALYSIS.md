# Gap analysis — lupinus

**Date:** 2026-09-22 · **Scope:** every tracked file in this repository, read
together. This is a documentation audit, not a code review: it looks for places
where the guide promises something the repository does not yet carry, where two
pages describe the same workflow differently, and where the next unit of writing
would pay off most.

Every claim below cites a path. Where a claim depended on state outside this
repo — a linked issue, a product's `ADOPTION.md` — it was checked against live
GitHub on the date above, and that is noted inline. This file lives under
`docs/` beside the [ADRs](adr/README.md); like them, an adopter who takes a
template copy is free to keep it as background or delete it.

## What already checks out

Recording these so the gaps below are read against a baseline, not as a verdict
on the whole repo:

- **The link checker is green.** `python3 ci/check_docs_links.py --root .`
  scans 22 markdown files and every relative link resolves.
- **The tier registry's issue citations are live.** All five structural issues
  cited in [`guide/tiers.md`](../guide/tiers.md) — `solidago#184`,
  `drosera#131`, `betula#74`, `osmunda#4`, `claytonia#47` — exist and are open
  as of this date. The registry's core credibility claim ("every structural row
  names a real, tracked issue") holds.

## A. Described but not present

### A1. The Kit tier is claimed without the receipt it requires

This is the most consequential gap, because the receipt gate is the mechanism
the whole registry is built on.

[`docs/adr/0003-drill-and-receipt.md`](adr/0003-drill-and-receipt.md) states the
rule plainly: *"A product must have a recorded receipt before it can be listed
as a Kit."* [`guide/tiers.md`](../guide/tiers.md) restates it in the tier table
— Kit means *"drill run with a recorded receipt"* — and
[`guide/first-kit.md`](../guide/first-kit.md) closes with *"a product cannot be
listed as a Kit until someone has produced one."*

Yet in the "Where each product stands" table of
[`guide/tiers.md`](../guide/tiers.md), four of the six products tiered **Kit**
carry no receipt:

| Product (row in tiers.md) | Tier | Receipt column says |
|---|---|---|
| monarda — campaign-site kit | Kit | *pending first run* |
| kalmia — Ansible workstation layer | Kit | *pending* |
| lock-in ledger | Kit | *pending* |
| drosera — status page | Kit | *pending* |

Only osmunda's Kit row claims a receipt ("exercised, timings recorded
upstream"), and that claim is unlinked — there is no path from this repo to the
timing it refers to.

The monarda case is verifiable and unambiguous: monarda's live `ADOPTION.md`
opens with `**Status of this runbook:** never run`. So the guide's flagship
"[your first kit](../guide/first-kit.md)" — the product the entire onboarding
funnel leads with — is tiered Kit while its own runbook declares itself
unexercised. By the repo's own rule these four rows are, at most, provisional
Kits; nothing in the guide marks them as such.

### A2. `estate/attachments/` is configured but absent

[`.obsidian/app.json`](../.obsidian/app.json) sets
`"attachmentFolderPath": "estate/attachments"`, but no such directory exists in
the tree. Obsidian will create it on first use, so this never errors — but the
vault ships promising a folder it does not contain, and there is no `.gitkeep`
holding the path. Minor, and listed only because it is a concrete
referenced-but-absent path.

## B. Two pages, one workflow, two shapes

### B1. Single-file `ADOPTION.md` (template) vs. three-file split (the exemplar)

The adoption runbook is described two incompatible ways, and neither page
acknowledges the other.

- [`templates/ADOPTION.md`](../templates/ADOPTION.md) puts the **Intake** table
  (§ Intake) and the **drill** table (§ The drill) *inline* in a single file.
  [`templates/README.md`](../templates/README.md) reinforces this, calling
  Intake and the drill "two sections [that] are load-bearing" of the one
  document.
- [`guide/first-kit.md`](../guide/first-kit.md) steps 2 and 3, however, send the
  adopter to two *separate* files in monarda —
  `INTAKE.md` and `DRY-RUN.md` — distinct from `ADOPTION.md` (step 1).

Checked live: monarda actually carries all three files, and its `ADOPTION.md`
does **not** embed the tables — its § Intake says "Complete `INTAKE.md`" and its
§ The drill says the drill "lives in `DRY-RUN.md`". So the reference
implementation the guide holds up delegates to separate files, while the
template a maintainer is told to copy inlines everything.
[`docs/adr/0003-drill-and-receipt.md`](adr/0003-drill-and-receipt.md) even
describes monarda in its Context as one that "pairs an intake questionnaire with
a timed dry-run" — i.e. separate artifacts — the very split the template
flattened away.

The result: a maintainer copying [`templates/ADOPTION.md`](../templates/ADOPTION.md)
literally produces a one-file runbook that looks nothing like the exemplar
[`guide/first-kit.md`](../guide/first-kit.md) tells adopters to read. Both
shapes are defensible; the gap is that the split is undocumented and
unmentioned in either place, so the divergence reads as an accident rather than
a choice.

### B2. Which products exist depends on which page you open

Four surfaces enumerate the product set, and they disagree:

- [`guide/picker.md`](../guide/picker.md) lists ~13 products across its "I need
  to…" table, including claytonia, epigaea, brasenia, betula, and
  shared-workflows + repo-template.
- [`guide/tiers.md`](../guide/tiers.md) scores all of them.
- [`support/README.md`](../support/README.md)'s "Where to ask, per product"
  table lists only seven: monarda, solidago, kalmia, drosera, betula, osmunda,
  and lupinus itself. **claytonia, epigaea, and brasenia are missing entirely.**
  An adopter who reads about one of those three Patterns in the picker and wants
  to report a problem finds no row telling them where.
- [`guide/runbook-index.md`](../guide/runbook-index.md) lists only the six
  Kit/Platform rows — but this one says so explicitly ("Rows without an
  `ADOPTION.md` yet point at the best existing document instead"), so it is a
  deliberate subset, not a drift.

The support-table omission is the concrete defect; the deeper issue is that
there is no single product list any of these four pages is checked against, so
they drift independently and a reader cannot tell an intentional omission from a
stale one.

### B3. kalmia is a Kit whose runbook link is a README section

Tied to A1 but distinct: [`guide/runbook-index.md`](../guide/runbook-index.md)
points "A configured ops workstation" at *"kalmia → README, Quick start"*, not
an `ADOPTION.md`. [`guide/tiers.md`](../guide/tiers.md) defines Kit as
*"`ADOPTION.md` complete"*. So kalmia is tiered Kit while the guide's own index
can only offer a README section for it. The runbook-index note about pointing at
"the best existing document" softens this, but the tier table's definition and
the index's link still contradict each other for this row.

## C. The three most valuable things to write next

### C1. Produce and wire in monarda's first receipt

**Rationale.** The receipt gate is the single mechanism that makes every tier
claim falsifiable ([`docs/adr/0003-drill-and-receipt.md`](adr/0003-drill-and-receipt.md)),
and right now it is unproven on the exact product the guide leads with:
monarda's `ADOPTION.md` says "never run" and
[`guide/tiers.md`](../guide/tiers.md) says "pending first run" (finding A1).
[`guide/first-kit.md`](../guide/first-kit.md) tells adopters that recording the
receipt is "the one people skip and the one that matters most" — a claim the
project has not yet honoured for itself. Running monarda's drill, filling its
`ADOPTION.md` Receipt, and turning the tiers.md "pending first run" cell into a
real number does three things at once: it validates the whole drill+receipt
apparatus, it converts monarda from a provisional Kit to a real one, and it
leaves behind a filled-in receipt that becomes the worked example every later
adopter copies from `templates/receipt.md`. Highest leverage of anything here,
because it retires the gap at the centre of the model.

### C2. A maintainer note reconciling the `ADOPTION.md` split

**Rationale.** Finding B1 leaves a maintainer with two contradictory exemplars
and no guidance: the template
([`templates/ADOPTION.md`](../templates/ADOPTION.md)) inlines Intake and the
drill, the reference product splits them into `INTAKE.md`/`DRY-RUN.md`, and
[`templates/README.md`](../templates/README.md) — the natural place for this —
is silent on the choice. A short section there (or a fourth ADR) stating when to
inline versus split, and updating the template to name the split as a supported
option, would remove the only genuinely confusing decision in the authoring
path. It is cheap to write and it directly protects the consistency the whole
federation argument depends on: an adopter who "learns to read one adoption doc
should be able to read all of them" ([ADR-0003](adr/0003-drill-and-receipt.md)),
which fails the moment two products chose different shapes for undocumented
reasons.

### C3. A single product registry the other pages derive from

**Rationale.** Finding B2 showed the product set enumerated four ways with a
real omission ([`support/README.md`](../support/README.md) is missing three
products the picker sells). The durable fix is one canonical list — a
`guide/products.md`, or a small data block — carrying each product's name, repo,
tier, and issues URL, with the picker, tiers, runbook-index, and support tables
either generated from it or checked against it. This matches how the repo
already thinks about drift: [`guide/tiers.md`](../guide/tiers.md) insists tier
changes move "by pull request, when the tracked work closes," and
[`ci/check_docs_links.py`](../ci/check_docs_links.py) already exists as the model
for a cheap, precise consistency check in CI. A registry closes the current
support-table gap and, more importantly, makes the *next* omission impossible to
ship silently — which, for a repo whose product is its own honesty, is worth
more than the one fix.
