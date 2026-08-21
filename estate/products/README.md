# Products

One note per thing you have adopted, named for the thing:
`monarda.md`, `solidago.md`, and so on. Start each from
[the component card template](../../templates/component-card.md).

A note here should answer, without anyone having to ask you:

- What is this and why do we have it?
- What does it depend on? (the links — these draw the graph)
- What does it cost?
- What did we change from stock?
- Who do we tell when it breaks?
- How would we leave?

That last one is worth filling in on the day you adopt, while leaving is still
hypothetical. It is much harder to write honestly once you depend on something.

## An example note

```markdown
---
adopted-from: lentago/monarda
adopted: 2026-09-02
tier: Kit
receipt: journal/receipts/monarda-2026-09-02.md
owner: alex
review: 2027-03-01
---

# monarda — our spring appeal site

Static campaign site for the spring appeal. Donations go straight to our
processor's hosted page; the site never sees card data.

## Depends on

- Deploys from [github-org](../accounts/github-org.md)
- Takes donations through [our processor](../accounts/processor.md)
```

Two adopted products with their dependency links written down is already enough
for the graph to earn its place.
