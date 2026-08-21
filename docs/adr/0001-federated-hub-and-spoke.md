# ADR-0001: The guide is a hub; runbooks live in the repos they operate

**Status:** Accepted (2026-08-19)

## Context

The Lentago suite is roughly a dozen repositories. An outside adopter — the
tech director of a non-profit, a competent generalist rather than an SRE —
needs to answer three questions: which of these fits my operation, how do I get
it into my own GitHub org, and how do I stand it up.

Nothing answered those questions. Every call to action on lentago.dev routed to
"book a consult"; the repos themselves were written for their operator. The
suite's delivery doctrine already said what the answer had to look like:
kits ship into client-owned estates, run on the client's own accounts, and
"forkable is the exit path" (`lentago/.github` ADR-0007). What was missing was
the operational surface for that promise.

The hard constraint on any solution: **an adopter forks one repo, not the
suite.** Whatever a product's adoption instructions are, they have to survive
being cloned alone, with no access to a central site or build system.

## Decision

Hub and spoke, in plain Markdown, with no build step.

- **Each product repo owns an `ADOPTION.md`** at its root — the runbook for
  standing that product up in someone else's estate. It travels with the code,
  renders on GitHub, and is complete on its own.
- **This repo is the hub**: it orients (which product fits me), sequences (what
  order to adopt in), and links out. It never copies a product's runbook.
- **No aggregation is load-bearing.** A rendered site may be added later as a
  presentation layer; nothing may ever depend on it.

This extends a convention the suite already ran — the field guide's runbook
index (`lentago/asclepias`) already pointed into owning repos rather than
restating them.

## Alternatives

- **An `adopt/` tree inside `lentago/asclepias`.** Rejected. asclepias onboards
  invited colleagues into *the maintainer's* live fleet; its voice convention is
  deliberately collegial and never instructive, and its day-one path assumes an
  org invite the adopter never receives. Two audiences, two front doors — the
  same reasoning that created asclepias rather than folding it into the org
  meta-repo.
- **A single aggregated docs site** (Antora, MkDocs with a multirepo plugin,
  Docusaurus, Backstage TechDocs). Rejected on maintenance grounds for a solo
  maintainer, and more decisively on the fork-one-repo constraint: aggregation
  puts the adoption instructions somewhere the forked repo cannot reach. Antora
  additionally requires AsciiDoc; the surveyed MkDocs multirepo plugin
  self-describes as no longer actively developed.
- **Retrospective — not considered at the time: per-repo rendered docs sites**
  (the repo-per-product model some public ops guides use, each publishing its
  own site under one domain). Lateral, and still available: it layers cleanly on
  top of this decision without moving any content, because the content already
  lives in the repo it documents.

## Consequences

- A product's adoption instructions are reviewed by the same gate as its code,
  in the same PR, by whoever knows it best.
- The hub can never drift into being the source of truth, because it holds no
  runbook content to drift.
- The cost is real but bounded: cross-product sequences (adopt A, then B on top)
  have no single owner, so they live here and must be maintained by hand.
- Adopters browsing on GitHub see unrendered Markdown. Accepted — it is legible,
  it needs no toolchain, and it is what a `git clone` gives them anyway.
