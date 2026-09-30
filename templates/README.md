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

- **Intake** — the third column names the exact field each answer becomes.
  Without it, an adopter has to guess how their answer relates to your
  configuration, which is where adoptions stall.
- **Swap list** — every value carried over from our estate. A structural
  limitation with no tracking issue is the thing this guide exists to stop
  happening quietly; write "not planned" rather than nothing.
