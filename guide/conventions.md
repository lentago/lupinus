# Conventions

The handful of things that are true for every product here. Each product's
`ADOPTION.md` links back to this page rather than repeating it.

## Use the template button, not fork

For anything you will customize — which is nearly everything — take a **template
copy**, not a fork:

- A template copy starts with clean history and no upstream link, and **it can be
  made private**. A fork of a public repository cannot.
- You will put real configuration in these repos: your domain, your account
  numbers, your alert addresses. That belongs somewhere you control the
  visibility of.

Fork only when you intend to send a change back to us.

Repos marked *Template* on GitHub carry a **Use this template** button. For the
others, the honest move is: clone, delete `.git`, and push to a new repository of
your own — or read the [tier](tiers.md) entry, because a product that is not a
template usually is not ready to be adopted whole.

## Keep our code unmodified; own your configuration separately

The pattern that keeps you able to take our improvements later:

- **Upstream product repos stay as they are.** Do not edit them into your
  version. Consume them — as a template copy you re-sync, or by reference.
- **You own one configuration repository.** Your variable files, your inventory,
  your overlays, your secrets references. That is where your estate's specifics
  live, and it is yours entirely.

Your copy of this guide *is* that repository — see
[your ops vault](../estate/README.md).

## Configuration by example file

Every product follows the same secrets convention, and no repository here has
ever contained a live credential:

- A committed `*.example` file shows every value you must supply, with a comment
  saying what it is and where to get it.
- The real file — the one with your values — is git-ignored. Copy the example,
  fill it in, and never commit it.

If you find a product where the example file is missing or out of date, that is a
bug worth reporting; it is the single most common way an adoption stalls.

## Our CI references, and what to do about them

Most repos in the suite run their continuous integration by calling shared
workflow definitions from our organization, like this:

```yaml
uses: lentago/shared-workflows/.github/workflows/docs-check.yml@v1.2.2
```

In your copy that is a cross-organization dependency: it points at a repository
you have no relationship with, and some of those workflows expect credentials
(an AI provider key, for instance) that your organization will not have. Worse,
if such a check is *required* on your default branch, a failure to run leaves
pull requests unable to merge.

Three options, in order of how much you care:

1. **Delete the workflows you cannot use.** The AI review and responder
   workflows need an API key. If you do not have one, they are noise.
2. **Vendor the one you want.** Copy the workflow's actual logic into your repo
   so it has no external reference. If a required check's *name* matters to your
   branch rules, keep the workflow and job names identical or your rules stop
   matching.
3. **Repoint at your own fork** of the shared workflows, pinned to a tag you
   control.

**Kits do this for you.** Anything at the Kit tier ships with no
cross-organization workflow references at all — that is part of what earns the
tier.

## Settings do not travel with files

A template copy brings files. It does not bring branch protection, required
checks, labels, or merge settings — those are repository settings, and your new
repo starts on GitHub's defaults.

The minimum worth setting on a repository that deploys anything:

```bash
# Require pull requests to your default branch, and squash-merge them.
gh api -X PUT repos/<YOUR_ORG>/<YOUR_REPO> \
  -F allow_squash_merge=true -F allow_merge_commit=false \
  -F allow_rebase_merge=false -F delete_branch_on_merge=true
```

Then, in **Settings → Rules → Rulesets**, add a ruleset targeting your default
branch that requires a pull request before merging. If you add required status
checks, add them **only after** you have seen that check report on a real pull
request — requiring a check that never runs will block every merge, and undoing
it is a manual trip through the settings UI.

## Write links the plain way

Throughout this guide and every runbook, links are ordinary Markdown:

```markdown
[the tier registry](tiers.md)
```

Not `[[tiers]]`. This is deliberate: the plain form renders on GitHub, passes the
link checker, works in any editor — **and** still builds the graph in
[your vault](../estate/README.md). Wiki-style links do none of the first three.

If you use Obsidian, its setting is **Options → Files & Links → New link format →
Relative path**, with **Use `[[Wikilinks]]` turned off**. Your copy ships that
way already.

## Refreshing this guide

Guide pages live under `guide/` and are **read-only in your copy** — that is what
makes updating them a single conflict-free command:

```bash
git remote add upstream https://github.com/lentago/lupinus.git   # once
git fetch upstream
git checkout upstream/main -- guide/
```

Because you never edit those files, that checkout cannot conflict. Do it when
you want; quarterly is plenty.

**To make a note on a runbook, do not edit the runbook.** Write your note in
`journal/` and link to the page from there — it will appear in that page's
backlinks whenever you open it, which is more useful than a margin note anyway,
and it survives every refresh.
