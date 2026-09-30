# ADR-0004: One guide, two volumes — asclepias and lupinus share one voice

**Status:** Accepted (2026-09-30)

## Context

[ADR-0001](0001-federated-hub-and-spoke.md) rejected folding this guide into
`lentago/asclepias`, and its stated reason was that the two repositories served
two different readers. asclepias onboarded people invited into *the maintainer's
live fleet* in a deliberately collegial, never-instructive voice (its ADR-0004);
lupinus instructed *external adopters* standing products up in their own
accounts. "Two audiences, two front doors" was the premise.

That premise no longer holds. On 2026-09-30 Lentago Labs was repositioned as a
pro-bono operations practice for organizations that run on volunteers,
donations, and one overworked tech person (`lentago/.github`
[ADR-0008](https://github.com/lentago/.github/blob/main/docs/adr/0008-pro-bono-practice-one-reader.md)).
All reader-facing documentation across the fleet is now written for one reader
in one voice, and the canon for that voice is
[`docs/voice.md`](https://github.com/lentago/.github/blob/main/docs/voice.md).
There is no longer an invited-reader audience distinct from an adopter audience;
both collapse into the one tech person the fleet now writes for.

## Decision

asclepias and lupinus are two volumes of a single guide, not two guides for two
audiences.

- **asclepias is volume 1** — how our own estate works, and an invitation to try
  a change on ours first, where nothing critical rides on it.
- **lupinus is volume 2** — how to make it yours: find the products worth your
  time, take them into your own organization, and run them from your own vault.
- **Both follow the fleet voice guide.** The instructive-versus-collegial split
  recorded in ADR-0001 and in this repo's former voice convention is retired.
  Where a page here instructs, it instructs because the reader needs a runbook —
  not because lupinus has a different voice from asclepias.

The hub-and-spoke architecture that ADR-0001 actually decided is untouched: each
product still owns its `ADOPTION.md`, this repo is still the hub that orients and
links and never copies, and an adopter still forks one repo rather than the
suite. This record amends only the *premise* in that ADR's Alternatives section —
the claim that asclepias and lupinus serve different audiences in different
voices — not the decision that premise was used to justify.

## Alternatives

- **Merge the two repositories now that the audience is one.** Rejected, for the
  same fork-one-repo reason ADR-0001 gave: asclepias documents the live fleet an
  invited reader tries changes against, while lupinus is a template an adopter
  clones into their own org. One voice does not make them one artifact. Two
  volumes, one voice, two repositories.
- **Keep two voices, one per repository.** Rejected. A second register here is
  exactly what ADR-0008 retired fleet-wide; maintaining it would drift from the
  canon and reintroduce the split the repositioning exists to remove.
- **Retrospective — not considered at the time: write lupinus for the one tech
  person from the outset.** Better, had the repositioning predated the repo. The
  content here was already the closest in the fleet to that reader, so what was
  missing was warmth and openers rather than structure — which is why this is an
  amendment rather than a rewrite.

## Consequences

- This repo's voice convention now points at the fleet voice guide instead of
  stating its own; see [CLAUDE.md](../../CLAUDE.md). Contributors follow one
  canon, not a per-repo rule they have to reconcile with it.
- Cross-links to asclepias frame it as volume 1 — "see it working on ours first"
  — rather than as a different-audience sibling.
- The neutral, factual voice of records — ADRs, incident reports, fleet reports —
  is unaffected here and in asclepias. This record is itself written in it.
