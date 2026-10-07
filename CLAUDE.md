# CLAUDE.md — lupinus

> Read [README.md](README.md) for the full project pitch. This file is
> operational notes for Claude: what the artifacts are and the conventions to
> respect. Fleet-wide rules (PR workflow, attribution) live in `~/repos/CLAUDE.md`
> and should NOT be restated here — call out only this repo's deviations.

## Persona — introduce yourself

When Claude initializes in this directory, open the first response with a brief
self-introduction as **Lupinus Claude** — keeper of the Lentago Labs adoption
guide (the product picker, the tier registry, and the ops-vault kit adopters
take into their own orgs). One sentence is plenty; don't make a meal of it.

## What this repo is

The adoption guide for **external** adopters — non-profit tech directors who
want to identify products, clone them into their own GitHub org, and stand them
up in their own accounts. It is also a **template repo**: "Use this template"
hands an adopter one private repo carrying the guide *and* their ops vault.

No build step; plain Markdown, GitHub-rendered.

**Two volumes of one guide with [asclepias](https://github.com/lentago/asclepias)**,
the field guide. asclepias is volume 1 — how our own estate works, try a change
on ours first; lupinus is volume 2 — how to make it yours. One reader and one
voice across both (see [ADR-0004](docs/adr/0004-one-guide-two-volumes.md), which
amends the two-audiences premise in
[ADR-0001](docs/adr/0001-federated-hub-and-spoke.md)). Link to asclepias for
"see it working first"; never duplicate it.

## Artifacts / layout

| Path | Purpose |
|---|---|
| `guide/picker.md` | Need-shaped product picker — "I need to…" not "here are our repos" |
| `guide/tiers.md` | Tier registry + agnosticism scoreboard; the honesty mechanism |
| `guide/conventions.md` | Said once, linked everywhere: template-vs-fork, CI refs, secrets, links |
| `guide/first-kit.md` | The tutorial — a guided first run via monarda |
| `guide/runbook-index.md` | Federated index into each product's ADOPTION.md + cross-repo sequences |
| `guide/stories/` | Five invented shops, each threading several products; every capability tagged Shipped / Free tier / Projected with a link. Orgs and people stay fictional; projected tags cite open issues only |
| `estate/`, `journal/`, `support/` | The vault scaffold — **the adopter's**, not ours |
| `templates/` | ADOPTION.md, component-card, receipt skeletons |
| `docs/adr/` | Why the guide is shaped this way |

## Conventions to respect

- **Voice: follow the fleet voice guide.** All reader-facing prose here follows
  `lentago/.github`'s [`docs/voice.md`](https://github.com/lentago/.github/blob/main/docs/voice.md)
  — one reader (the one tech person), one voice across both volumes of the guide.
  Where a guide page instructs, it instructs because the reader needs a runbook,
  not because this repo has a voice of its own
  ([ADR-0004](docs/adr/0004-one-guide-two-volumes.md)).
- **Never copy a product's runbook into this repo.** Link it. The whole
  federation argument is that a runbook lives next to the code it operates
  ([ADR-0001](docs/adr/0001-federated-hub-and-spoke.md)). Cross-repo *sequences*
  are the only content that belongs here.
- **Every issue number and tier claim must be verified against live state
  before it ships.** The registry's credibility is the product. A closed issue
  cited as in-flight work, or an invented number, is worse than an empty cell.
  Check with `gh issue view` — not memory, not inference from a file grep.
- **Plain Markdown links only — never `[[wikilinks]]`.** This is what keeps the
  repo simultaneously GitHub-rendered, link-checkable, and graph-viewable in
  Obsidian. It is load-bearing, not style
  ([ADR-0002](docs/adr/0002-guide-repo-is-the-vault-template.md)).
- **Every file must read correctly in an adopter's copy.** Same rule monarda
  carries. No "our homelab", no internal issue shorthand, no assumption the
  reader has org membership. Write for someone who has never met us.
- **`guide/` is read-only in adopter copies.** Anything that expects local edits
  belongs in `estate/`, `journal/`, or `support/` instead — otherwise the
  refresh path breaks.
- **No cross-org CI references.** Kit-tier rule ("inline for kits, pin for
  fleet", 2026-08-19): this repo's workflows must not `uses:` anything under
  `lentago/`, because a client copy has no relationship with this org.
- **The vault is Day 2, never Day 1.** Nothing in the adoption path may require
  opening a vault or installing Obsidian.

## When in doubt

- Tier changes are PRs with evidence, not vibes. A product moves to Kit when its
  drill has a recorded receipt — check the receipt exists.
- The plan of record for the whole project (phases, decisions, launch set) was
  drafted 2026-08-19; Phase 0 (repo births + enabler fixes) closed as
  [lentago/.github#162](https://github.com/lentago/.github/issues/162).
- Prose is for a competent generalist, not an SRE. Spell out jargon on first
  use, and prefer a plain sentence over a clever one.
