# ADR-0003: Adoption runbooks are drills that end in a measured receipt

**Status:** Accepted (2026-08-19)

## Context

Two repos in the suite had independently arrived at the same shape for
procedural documentation, four weeks apart:

- `lentago/monarda` pairs an intake questionnaire with a timed dry-run whose
  every step has an observable success condition, ending in a receipt table —
  date, operator, total elapsed time, slowest step.
- `lentago/brasenia` pairs a phased operator test spec with a filled-in
  validation-notes document recording what actually happened on the night it was
  run.

Neither had a name, so neither could be asked for by name. Meanwhile the
suite's other setup documents varied from excellent (`solidago/docs/BOOTSTRAP.md`,
11 numbered steps with a time estimate) to absent.

The wider practice is settled on the anatomy: an outcome-shaped title,
preconditions, exact commands, verification after every step, rollback,
escalation, and an owner with a last-verified date. What the two in-house
examples add is the part most runbooks omit — **proof the procedure was
actually executed**, and what it cost in wall-clock time.

## Decision

Name the pattern **drill + receipt**, template it, and make it the standard
shape for every `ADOPTION.md` in the suite.

- **Drill**: numbered steps, copy-pasteable commands, adopter placeholders
  visually unmistakable, and a falsifiable *"check it's green"* beside every
  step. Ordered local-first — everything verifiable offline happens before
  anything touches a deploy target or costs money.
- **Receipt**: date, operator, elapsed time, slowest step, all-green yes/no. The
  recorded time is the receipt.
- **Status marker**: every drill states whether it has been run — *exercised*
  (with a receipt) or *unexercised*. An unexercised drill is not a defect, but
  claiming an unproven one works is.

A product must have a recorded receipt before it can be listed as a Kit in the
[tier registry](../../guide/tiers.md).

## Alternatives

- **Adopt an external runbook template wholesale.** Considered; partially
  adopted. The consensus anatomy is imported, but no surveyed template carries
  the receipt idea — the strongest thing the in-house examples had. Importing
  the anatomy and keeping the receipt was strictly better than either alone.
- **Leave each repo to its own format.** Rejected. The variation was already the
  problem: an adopter who learns to read one adoption doc should be able to read
  all of them.
- **Retrospective — not considered at the time: automate the drill as a script
  instead of documenting it.** Better *where it applies* — a step that never
  varies is automation waiting to happen, and the suite already has drill
  scripts of exactly this kind. It is not a replacement, though: the drill's
  value for a generalist adopter is partly that they see what each step does to
  their estate before it happens.

## Consequences

- Receipts make claims falsifiable. "Standing this up takes an afternoon" stops
  being a sales line and becomes a number someone recorded.
- Running the drills costs real time and, for cloud products, real money. That
  cost is the point, and it is the gate on the Kit tier.
- Receipts decay. A drill run against last quarter's product is evidence about
  last quarter, which is why the status marker carries a date and the template
  asks for the version tested against.
- Writing a drill surfaces adoption bugs early — the first pass over the AWS
  platform's runbook found that a fresh clone could not run `terraform plan` at
  all, which no amount of prose review had caught.
