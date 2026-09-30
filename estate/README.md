# Your estate

This is the half of the repository that's **yours**. The [guide](../guide/picker.md)
is ours and gets refreshed from upstream; everything under `estate/`,
[`journal/`](../journal/README.md), and [`support/`](../support/README.md) is
written by you and never overwritten.

It is a plain folder of Markdown, so it works in any editor. It is also laid out
as an **Obsidian vault** — open this repository as a vault and the notes here
become a map of what you run, where the links between notes are the real
integrations and data pathways between your systems.

## What goes where

| Folder | What it holds |
|---|---|
| [`products/`](products/README.md) | One note per thing you have adopted |
| [`accounts/`](accounts/README.md) | One note per account or platform your products depend on |
| `pathways.canvas` | A diagram of how data actually moves between them |

## Start here, on the day you adopt something

1. Copy [the component card template](../templates/component-card.md) to
   `products/<name>.md`.
2. Fill in the frontmatter and, most importantly, the **Depends on** section —
   one link per real dependency, pointing at the notes in `accounts/`.
3. Create any account note that does not exist yet, from
   [the accounts README](accounts/README.md).

That is it. Five minutes per product, best done while the adoption is fresh.

## Why the links matter

Each link is an edge. After you have adopted two or three things, the graph view
stops being decoration and starts answering questions you would otherwise have to
reconstruct from memory:

- *If this account went away tomorrow, what stops working?* Look at what points
  at it.
- *What have we got that touches donor data?* Follow the edges out of the
  processor note.
- *What did we add last quarter?* The new subgraph is visibly separate — and if
  adopting something new required rewiring everything else, that is worth
  noticing too.

The graph is built from ordinary Markdown links, so it costs you nothing beyond
writing the links you would want anyway. Keep them plain — `[name](path.md)`,
never `[[name]]` — for the reasons in
[conventions](../guide/conventions.md#write-links-the-plain-way).

## Labelled pathways

The graph shows *that* two things are connected. When you need to show *how* —
"ships logs to", "deploys into", "reads donations from" — use
`pathways.canvas`, which opens as a diagram with labelled arrows. It is
[JSON Canvas](https://jsoncanvas.org), an open format, so it is readable
without Obsidian too.

The one shipped here is a starter with example nodes. Replace them.

## If you do not use Obsidian

Nothing breaks. These are Markdown files with links; any editor reads them, and
GitHub renders them. You lose the graph view and the backlink pane, which are
conveniences rather than the substance. The substance is that the notes exist.

**The exit, stated plainly:** your data is Markdown in a git repository you own.
Obsidian is a free-to-use reader over it, not a place your content lives. If you
stop using it, you keep everything, and the folder still works.
