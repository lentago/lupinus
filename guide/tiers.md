# Tiers and the agnosticism scoreboard

> **Reading this in your own copy of the guide?** This is the one page that
> keeps changing. The live version is at
> [lentago/lupinus](https://github.com/lentago/lupinus/blob/main/guide/tiers.md);
> check it before concluding a product is still where this copy says it is.

Two things live on this page: how adoptable each product is today, and exactly
what stands between it and being more adoptable. The second half is the point.
Most of this suite was built for one estate, and saying so plainly — with the
work items that would change it — is more useful than pretending otherwise.

## The tiers

| Tier | What it means | What a product must clear to earn it |
|---|---|---|
| **Kit** | Clone it today; stand it up from the repo alone | `ADOPTION.md` complete · drill run with a recorded receipt · no dependency on our accounts or org |
| **Platform** | Adoptable with about a day's work and your own accounts | `ADOPTION.md` complete · swap list short and mechanical · receipt recorded |
| **Pattern** | Read it, lift pieces, do not stand it up whole | Honest "what to lift" note · swap list explaining why, each row tracked or explicitly not planned |

## Where each product stands

| Product | Tier | Receipt | What would move it up |
|---|---|---|---|
| [monarda](https://github.com/lentago/monarda) — campaign-site kit | **Kit** | *pending first run* | — |
| [kalmia](https://github.com/lentago/kalmia) — Ansible workstation layer | **Kit** | *pending* | — (the Proxmox layer below is a separate unit) |
| [osmunda](https://github.com/lentago/osmunda) — ephemeral cluster drills | **Kit** | exercised, timings recorded upstream | Move drill credentials off an operator IAM user to a role |
| [lock-in ledger](https://github.com/lentago/.github/tree/main/fleet-reports/lock-in) | **Kit** | *pending* | — |
| [drosera](https://github.com/lentago/drosera) — status page | **Kit** | *pending* | Worked example wired to a Pages target |
| [solidago](https://github.com/lentago/solidago) — AWS platform | **Platform** | *pending* | Scripted identity-provider bootstrap; the standing plan noise in [solidago#184](https://github.com/lentago/solidago/issues/184) |
| [shared-workflows](https://github.com/lentago/shared-workflows) + [repo-template](https://github.com/lentago/repo-template) | **Platform** | *pending* | An adopter guide for fork-and-repin vs. vendoring |
| [drosera](https://github.com/lentago/drosera) — full observability stack | **Pattern** | — | An "adopt into your own stack" document; a collector config with our addresses removed; the multi-client work in [drosera#131](https://github.com/lentago/drosera/issues/131) |
| [betula](https://github.com/lentago/betula) — log capture | **Pattern** | — | The core/client split in [betula#74](https://github.com/lentago/betula/issues/74), which makes our firewall one client among several rather than the product |
| [epigaea](https://github.com/lentago/epigaea) — physical-world telemetry | **Pattern** | — | Separating the reusable deploy mechanism from the one building it describes |
| [osmunda](https://github.com/lentago/osmunda) — Kubernetes platform | **Pattern** | — | The cluster-install gap in [osmunda#4](https://github.com/lentago/osmunda/issues/4) |
| [claytonia](https://github.com/lentago/claytonia) — agent fleet | **Pattern** | — | A zero-to-first-job install path; the platform seam in [claytonia#47](https://github.com/lentago/claytonia/issues/47) |
| [kalmia](https://github.com/lentago/kalmia) — Proxmox guest layer | **Pattern** | — | It has no variables at all today — it is a record of one cluster, not a tool for building one |
| [brasenia](https://github.com/lentago/brasenia) — shared viewport | **Pattern** | — | The product is a later phase and is not built; today it is a design document with one working client |

## How this page stays honest

Three rules, borrowed from how the suite handles renames — where "we will just
keep the old name" is not an acceptable resolution:

1. **Every opinionated value an adopter must change is a row in that product's
   swap list**, in its own `ADOPTION.md`, where you hit it.
2. **Every swap-list row is either mechanical or tracked.** Mechanical means
   "put your value here" — an account number, a domain, an email address.
   Structural means it cannot be swapped yet, and the row names the issue that
   will fix it. A row may also say *not planned* — but explicitly, never by
   silence.
3. **Tier changes happen by pull request**, when the tracked work closes. The
   registry moves because something actually changed, not because someone felt
   better about it.

## Why so many Patterns

Because it is true today. The suite was built as one operator's working estate
and published as it went; the parts that were designed from the start to land in
someone else's accounts — the campaign kit, the workstation layer, the drills —
are the parts that are Kits. Making the rest portable is ordinary work, and it is
tracked above.

If you want a product moved up and it is stuck behind a tracked issue, say so on
that issue. Knowing someone is waiting is the most useful thing you can tell us.
