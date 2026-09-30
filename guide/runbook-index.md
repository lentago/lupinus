# Runbook index

Every product's adoption runbook — the step-by-step for standing it up — lives in
that product's own repository, as an `ADOPTION.md` at its root. This page only
points at them.

That's deliberate. A runbook that sits next to the code it operates gets reviewed
when that code changes, ships with the repository when you clone it, and can't
drift into describing a version that no longer exists. A copy here would do none
of those things. It also means you can adopt one product without ever reading
this page.

## Adoption runbooks

| I want to stand up | Runbook | Tier |
|---|---|---|
| A campaign or fundraising site | [monarda → ADOPTION.md](https://github.com/lentago/monarda/blob/main/ADOPTION.md) | Kit |
| An AWS environment I own | [solidago → ADOPTION.md](https://github.com/lentago/solidago/blob/main/ADOPTION.md) | Platform |
| A configured ops workstation | [kalmia → README, Quick start](https://github.com/lentago/kalmia#quick-start) | Kit |
| A temporary Kubernetes cluster | [osmunda → runbooks/](https://github.com/lentago/osmunda/tree/main/runbooks) | Kit |
| A public status page | [drosera → status-page/](https://github.com/lentago/drosera/tree/main/status-page) | Kit |
| A vendor lock-in review | [the lock-in kit](https://github.com/lentago/.github/tree/main/fleet-reports/lock-in) | Kit |

Rows without an `ADOPTION.md` yet point at the best existing document instead,
and say so. As those runbooks are written, the links move and the tier column
catches up — see [tiers](tiers.md) for what's in flight.

## Sequences that span products

Some things are worth doing in an order. These live here rather than in any one
repository, because no single repository owns them.

**A public presence you own, end to end.**
[monarda](https://github.com/lentago/monarda) first, on free hosting. If you
later outgrow it — you need several sites, private networking, or a database —
adopt [solidago](https://github.com/lentago/solidago) and move the site onto it.
Doing it in this order means you are already comfortable with the deploy shape
before you are paying for infrastructure.

**Seeing what you run.** Adopt any product first, then
[drosera](https://github.com/lentago/drosera)'s status page for the outside view.
The full observability stack is a [Pattern](tiers.md) today — read it for the
approach rather than adopting it whole.

**Before you commit to any vendor**, including us: run the
[lock-in review](https://github.com/lentago/.github/tree/main/fleet-reports/lock-in).
It takes an afternoon and is the single most useful thing on this page. We run it
on our own estate and publish the result.

## Operating runbooks, once you are running

This index covers *adoption* — the day you stand something up. For the days
after, the runbooks that matter are the ones you write: what broke, what you
did, what you would do differently.

That is what [your ops vault](../estate/README.md) is for, and specifically
[`journal/`](../journal/README.md). Nobody else can write those for you; they are
about your estate.

## A note for maintainers

If you own a product repository here: the runbook belongs to you, in your repo,
to the [drill and receipt](../docs/adr/0003-drill-and-receipt.md) shape. Use
[the template](../templates/ADOPTION.md). Write it *here* only if it genuinely
spans repositories — like the sequences above.
