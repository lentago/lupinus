# Architecture decision records

Decisions about how this guide is shaped and why. Records here are written at
decision time unless a record says otherwise.

## Index

| ADR | Title | Status | Date |
|---|---|---|---|
| [0001](0001-federated-hub-and-spoke.md) | The guide is a hub; runbooks live in the repos they operate | Accepted | 2026-08-19 |
| [0002](0002-guide-repo-is-the-vault-template.md) | The guide repo is also the adopter's ops-vault template | Accepted | 2026-08-19 |
| [0003](0003-drill-and-receipt.md) | Adoption runbooks are drills that end in a measured receipt | Accepted | 2026-08-19 |
| [0004](0004-one-guide-two-volumes.md) | One guide, two volumes — asclepias and lupinus share one voice | Accepted | 2026-09-30 |

---

## How to add an ADR to this repo

Create `docs/adr/NNNN-<short-slug>.md` and add a row to the index above. Use this structure:

```markdown
# ADR-NNNN: <Title>

**Status:** Accepted (<date>)

## Context

Why was a decision needed? What constraints and forces were in play?

## Decision

What was decided, and how does it address the context?

## Alternatives

List the options that were actually weighed, then add one or two marked
*"retrospective — not considered at the time"* with an honest assessment
(worse / better / lateral) and a short reason.

## Consequences

What does this decision make easier or harder going forward? What are the
known trade-offs or scars?
```

**Recorded vs. retrospective alternatives:** Alternatives that were actually weighed at decision
time go in the list without special marking. Options added later for completeness must be
explicitly labelled *"retrospective — not considered at the time"* so future readers know they
were not part of the original deliberation. Honest assessment (worse / better / lateral) is
required — do not present retrospective options as neutral.

> **If you created a repo from this template:** these records document the
> guide itself. You are welcome to keep them as background, or delete them and
> start your own log — your estate's decisions are worth recording too.
