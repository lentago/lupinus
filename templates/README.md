# Templates

Fill-in-the-blank starting points. Copy them; don't edit them in place.

| Template | Copy it to | Who uses it |
|---|---|---|
| [ADOPTION.md](ADOPTION.md) | the root of a product repository | Maintainers publishing a product |
| [component-card.md](component-card.md) | `estate/products/<name>.md` in your vault | Adopters, when they adopt something |
| [receipt.md](receipt.md) | `journal/receipts/<product>-<date>.md` | Anyone who runs a drill |

## Why the ADOPTION template is so opinionated

Because the sections that get dropped are always the same ones, and they're the
ones you need most when you're the one adopting: the exhaustive prerequisites,
the check beside every step, the teardown, and the receipt. The shape is argued
in [ADR-0003](../docs/adr/0003-drill-and-receipt.md).

Two sections are load-bearing and easy to under-fill:

- **Intake** — wherever it lives, the third column names the exact field each answer becomes.
  Without it, an adopter has to guess how their answer relates to your
  configuration, which is where adoptions stall.
- **Swap list** — every value carried over from our estate. A structural
  limitation with no tracking issue is the thing this guide exists to stop
  happening quietly; write "not planned" rather than nothing.

## One file or three: keep the intake and the drill inline, or split them out

The template puts the Intake table and the drill table inside `ADOPTION.md`.
That's the default, and most products should keep it: one file to read, one
file to keep current. [solidago's runbook](https://github.com/lentago/solidago/blob/main/ADOPTION.md)
is built that way.

Move either one into a file of its own when it has a life of its own:

- **The intake is answered before anyone starts.** It's a questionnaire filled
  in ahead of time, often by the person the product is for rather than the one
  setting it up, and it's long enough to need sections. Put it in `INTAKE.md`.
- **The drill has its own clock.** It records a time at every checkpoint and
  has a receipt table of its own, or there's more than one drill, each timed
  separately. Put it in `DRY-RUN.md`.

[monarda's runbook](https://github.com/lentago/monarda/blob/main/ADOPTION.md)
splits both. It's the one [your first kit](../guide/first-kit.md) walks you
through, so it's the shape most adopters see first.

> **Heads up.** A split moves the *content* of `## Intake` or `## The drill`,
> never the heading. Keep every section of `ADOPTION.md`, in the template's
> order, and under a moved section leave one short paragraph that says where
> the content went and what "done" looks like. That's what keeps
> [ADR-0003](../docs/adr/0003-drill-and-receipt.md)'s promise: someone who has
> learned to read one runbook can find their way around all of them.

The template's comments carry monarda's two paragraphs, ready to adapt. Copy
them and swap in your own config file and finish line. The `## Receipt` section stays in
`ADOPTION.md` either way, as the summary (date, elapsed time, slowest step,
all-green); the time at each checkpoint stays with the drill.
