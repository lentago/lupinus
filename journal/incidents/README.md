# Incidents

One entry per thing that broke. Name them `<YYYY-MM-DD>-<short-slug>.md`.

This is not a formal process and there is no template to satisfy. Five headings
is plenty:

```markdown
# 2026-09-14 — donate button went to a 404

**What broke:** The donate link 404'd for about three hours on a Saturday.

**How we found out:** A board member clicked it. Not from monitoring.

**What we did:** Our processor changed the hosted-page URL format. Updated
the config field, redeployed, verified.

**What did NOT break:** Donations already in flight were unaffected — the
processor holds those, not us. Worth knowing.

**The lesson:** Nothing was watching the donate path. Added an uptime check
that follows the outbound link, not just the homepage.

Affects [monarda](../../estate/products/monarda.md).
```

## Two things worth keeping in every entry

**How you found out.** If the answer is repeatedly "a person told us", that is a
monitoring finding hiding inside an incident write-up.

**What did *not* break.** Easy to skip and genuinely useful — it records which
of your assumptions held, which is what lets you trust that part next time.

## Blame

Write these so anyone can read them without a person looking bad. The useful
subject of an incident report is the system that allowed the mistake, not the
person who made it — and reports written the other way stop getting written at
all, quickly.
