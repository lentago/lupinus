# ADR-0002: The guide repo is also the adopter's ops-vault template

**Status:** Accepted (2026-08-19)

## Context

Adoption is the first day. What an adopter needs on every day after is a place
to operate from: what they run, which accounts it depends on, what the data
pathways are, what broke last time, when the renewals land.

That place was already implied by the delivery doctrine — the adopter owns a
config/state repository separate from the unmodified upstream products. What it
lacked was a shape, and a reason to open it.

An Obsidian-compatible vault supplies both. A vault is a folder of Markdown, so
it costs nothing structurally; its graph view turns the links between notes into
a picture of the estate, where edges are the integrations and data pathways
between products and accounts.

The original design shipped this as a *separate* kit, on the reasoning that a
guide is an updatable product while a vault is divergent state, and template
copies have no git relationship to upstream — so merging them would hand every
adopter a slowly rotting snapshot of the guide.

## Decision

One repo. This repo is `template: true`; "Use this template" gives the adopter a
single private repo carrying both the guide and their vault scaffold.

The staleness objection dissolves on inspection of *which* pages get copied:

- The per-product runbooks — the content that must stay live — are **never**
  copied in either design. They live in the owning repos and are only linked.
- What lands in a copy is the picker, the tutorial, and the conventions: Day-1
  pages whose job is complete once adoption succeeds.
- The one deliberately living page, the tier registry, carries a banner pointing
  at the upstream version.

Two conventions keep the merge safe:

1. **Guide pages live under `guide/` and are read-only in copies.** That makes
   refreshing them a conflict-free `git checkout upstream/main -- guide/`.
2. **Annotate by backlink, never in the page.** The urge to write margin notes on
   a runbook you are following is served by Obsidian's own mechanism: a note in
   `journal/` linking to the guide page shows up in its backlink pane.

The federation rule from [ADR-0001](0001-federated-hub-and-spoke.md) gains one
rider: the hub may be *mirrored* into adopter copies where a conflict-free
refresh path exists. Per-product runbooks remain never-copied.

## Alternatives

- **A separate ops-vault kit repo.** The original proposal. Rejected as
  needless: it split one motion into two ("clone the guide, then also clone the
  vault"), and it cost the property that makes the graph worth having — with the
  guide in the vault, component notes link to local guide pages, so the estate
  map and the suite map render as one connected graph instead of dead external
  links that create no edges.
- **Wikilink syntax** (`[[note]]`), Obsidian's default. Rejected. GitHub does not
  render it in repository Markdown and the fleet's link checker cannot resolve
  it. Obsidian's `useMarkdownLinks` setting emits standard `[text](path.md)`
  links instead and builds the same graph — so the whole federation is
  vault-compatible at zero cost.
- **Retrospective — not considered at the time: a typed-edge plugin stack**
  (Dataview, Juggl) as the baseline rather than an option. Worse as a default —
  it makes the vault depend on community plugins to be readable at all, which
  contradicts the portability the kit is selling. It stays documented as an
  optional layer.

## Consequences

- One green button gets an adopter both artifacts, in a repo that can be private
  — which the vault needs, since it will hold estate-specific detail.
- The guide refresh is a ceremony some adopters will skip, leaving a stale
  picker in their copy. Accepted: the picker's job ended at adoption, and the
  page where staleness would actually mislead carries a banner.
- The vault is **Day 2, never Day 1**. Onboarding stays browser-only; nothing in
  the adoption path may require opening a vault.
- The kit is Obsidian-*compatible*, not Obsidian-*dependent*: the same folder
  works in any editor, and the kit documents its own exit.
