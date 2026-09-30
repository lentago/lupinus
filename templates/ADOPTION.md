<!-- TEMPLATE. Copy to the root of a product repo as ADOPTION.md and fill in.
     Delete every instruction comment as you go. The shape is fixed — see
     lupinus/docs/adr/0003-drill-and-receipt.md for why each section exists. -->

# Adopting <product>

<!-- One paragraph, written straight to the adopter as "you". What they end up
     with, concretely. Name what it does NOT do — the fastest way to lose
     someone's afternoon is to let them discover the boundary at step 9. -->

**Status of this runbook:** <exercised on YYYY-MM-DD against <version/commit> |
never run — see [Receipt](#receipt)>

## What you get

<!-- Bullets or short prose. Then the ownership table — this is the trust
     statement, and it is not boilerplate. Adjust rows to what is true here. -->

| What | Who owns it |
|---|---|
| The repository | You |
| The accounts it runs in | You |
| The data | You |
| The domain | You |

<!-- If anything is NOT owned by the adopter, say so in this table. An honest
     row here is worth more than the whole document. -->

## What this is not

<!-- The boundary. Two or three lines. What people reasonably assume this does
     that it does not. -->

## Prerequisites

<!-- EVERYTHING, in one list. No scavenger hunts across other repos. Include
     versions where they matter. If another product must be adopted first, say
     so here and link its ADOPTION.md. -->

- **Accounts:**
- **Hardware:**
- **Tools:** <name and minimum version>
- **Access you must already have:**

**Cost:** <$X/month, itemized if it is not obvious — or "none">
**Time:** <realistic estimate; if a drill has been run, use the recorded number>

## Intake

<!-- Every value the adopter must supply. The third column is the point: it
     names the exact field, variable, or secret the answer becomes, so filling
     in configuration is mechanical rather than interpretive. -->

| Question | Your answer | Maps to |
|---|---|---|
| | | `<file>` → `<field>` |

## Swap list

<!-- Every opinionated value carried over from OUR estate. Be exhaustive —
     an adopter finding an un-listed hardcoded value is the failure mode this
     section exists to prevent.

     "Tracked" column: a mechanical swap is just "put your value here". If a
     value CANNOT be swapped yet because the code is not parameterized, name
     the issue that will fix it — or write "not planned", explicitly. Never
     leave a structural limitation implied by silence.
     See lupinus/guide/tiers.md § How this page stays honest. -->

| Ours | Where it lives | Put yours here | Tracked |
|---|---|---|---|
| | `<path>:<line>` | | mechanical |

## The drill

<!-- Numbered steps. Rules:
     - Copy-pasteable commands. Placeholders LOUD: <YOUR_ORG>, <YOUR_DOMAIN>.
     - One action per step.
     - Every step has a falsifiable "check it's green".
     - LOCAL FIRST: everything verifiable offline comes before anything that
       touches a deploy target, costs money, or is hard to undo. -->

| # | Step | Check it's green | ✅ |
|---|---|---|---|
| 1 | | | |
| 2 | | | |

**If a check does not go green,** stop at that step — the next one assumes it
worked. See [Troubleshooting](#troubleshooting).

## Verify it works

<!-- The end-to-end proof, from the outside. Not "the workflow was green" —
     the actual thing working: a page loads, a metric arrives, an alert fires. -->

## Receipt

<!-- Filled in by whoever runs the drill. A blank table means UNEXERCISED, and
     the status line at the top must say so. Don't delete this section to tidy
     it up — an empty receipt is information, and it's honest. -->

| Field | Value |
|---|---|
| Date | |
| Operator | |
| Version tested | |
| Deploy target | |
| Total elapsed | |
| Slowest step | |
| All checks green | |
| Notes | |

## Teardown

<!-- How to remove it completely, with verification. For anything that costs
     money this is not optional — an adopter who cannot confidently undo will
     not confidently start. Include how to confirm the billing actually stops. -->

## You are operationally ready when

<!-- The finish line as a checklist. Adjust to the product. -->

- [ ] Backups are configured and you have restored one
- [ ] Alerts reach a human who is awake
- [ ] Secrets are your own, not the example values
- [ ] You have run the teardown at least once, somewhere safe
- [ ] Someone other than the person who set it up can follow this document

## Troubleshooting

<!-- Real failures seen, with the symptom first — that is how people search. -->

**Symptom:**
**Cause:**
**Fix:**

## Getting help

Open an issue on this repository. Include: what step you were on, the exact
command, the full output, and your platform. If it is a documentation problem —
a step that was wrong, unclear, or missing a prerequisite — that is the most
valuable issue you can file.

---

**Runbook owner:** <@handle> · **Last verified:** <YYYY-MM-DD>
<!-- Both required. An unowned, undated runbook decays silently. -->
