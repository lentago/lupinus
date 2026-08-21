# Journal

What happened, when, and what you learned. Two kinds of entry:

| Folder | For |
|---|---|
| [`receipts/`](receipts/README.md) | Records of adoption drills you ran |
| [`incidents/`](incidents/README.md) | Records of things that broke |

Both are append-only in spirit: you add entries, you do not tidy old ones. An
entry that turned out to be wrong gets a correction appended, not a rewrite —
the wrong version is part of what happened.

## Why write any of this down

Because the alternative is that it lives in one person's memory until they are
on holiday.

Two specific payoffs, both of which arrive later than you would like:

- **Receipts make estimates real.** The second time you stand something up, the
  first receipt tells you how long to book and which step to start early.
- **Incidents compound.** The value is not the individual write-up; it is
  noticing on the fourth one that three of them were the same expired
  credential, and finally fixing the thing underneath.

## Link outward

Entries here should link to the component note they concern, so the connection
shows up in both directions:

```markdown
Ran the drill for [monarda](../estate/products/monarda.md).
```

The component note then shows this entry in its backlinks without you having to
maintain a list.

## This is also where you annotate the guide

The guide under [`guide/`](../guide/picker.md) is refreshed from upstream, so
editing it locally means losing your edits. If you want to note that a step was
confusing, or that something did not apply to you, write it here and link the
page:

```markdown
Working through [the conventions page](../guide/conventions.md), the ruleset
step needed an extra approval from our IT — worth an hour's lead time.
```

Your note then appears in that page's backlinks every time you open it, and it
survives every refresh.
