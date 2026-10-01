# Understory Fiscal Collective

**Scope:** a fiscal sponsor. One legal entity, fifteen sponsored projects, each with its own volunteers, its own funders, and its own idea of how a website works. **The one tech person:** Jun, operations manager, who is the tech person for all fifteen, whether or not the projects know it.

*Heads up:* this is the most projected story of the five. It is also the one that pulls hardest on the pieces we most want to build, which is why it is here.

## What they pay for today

| Tool | What it was for | What it costs them (illustrative) | Who knows how it works |
|---|---|---|---|
| Salesforce Nonprofit Cloud, enterprise tier, with a partner agency | One CRM for fifteen projects' donors, with "per-project visibility" that took a year of consulting to configure | The largest line in the collective's overhead. Every funder-report format is a billable change. | The agency. |
| ServiceNow, scoped down to a help desk | Requests from fifteen projects' volunteers | Jun is the only agent. The queue is a list Jun could have kept in a text file. | Jun, reluctantly. |
| Fifteen website builders, fifteen domains, fifteen renewal dates | Each project's site | Fifteen subscriptions, several on departed volunteers' cards. | Fifteen different people. |
| An AI-policy consultant | Funders have started asking "do you use AI, and how?" | A one-time engagement that produced a document nobody can act on. | The consultant. |

## The night it broke

Grant season. Three projects' funder reports are due the same week, each wants numbers in a different shape, and each number lives in a Salesforce report the agency built. One project's volunteer coordinator left and took the only login to that project's site with her. Jun's help-desk queue has nineteen tickets from volunteers asking for things Jun has answered before, in email, which nobody can find. A funder asks for the collective's AI usage policy, and Jun forwards the consultant's PDF, which says nothing about what the collective actually does.

## The path out

1. **Every project gets the same starter kit.** *Shipped:* [repo-template](https://github.com/lentago/repo-template) and [shared-workflows](https://github.com/lentago/shared-workflows) mean a new project's repo starts with the checks, labels, and templates already in place, which is the same mechanism that keeps the fleet's own twenty repos aligned. *Projected:* [Ops-in-a-Box](https://github.com/lentago/.github/issues/133), the miniature estate starter: fork, bootstrap, first PR, break it, read your own dashboard, write your first post-mortem. This is the onboarding for each project's volunteer, and it becomes the guide's Lab 05.
2. **Fifteen sites become fifteen copies of one config.** *Shipped:* [monarda](https://github.com/lentago/monarda), on GitHub Pages, in the collective's one GitHub organization with a repo per project. Fifteen subscriptions become zero. *Projected:* the [Digital Custody audit](https://github.com/lentago/.github/issues/124) consolidates the fifteen domains under the collective with a named steward each.
3. **The help desk is issue forms, and the chores get done by agents.** *Free tier:* GitHub Issues across fifteen repos, one project board (*projected* as a starter: [.github#196](https://github.com/lentago/.github/issues/196)). *Shipped:* [claytonia](https://github.com/lentago/claytonia), a fleet of agents that pick up routine repo chores from a shared queue and open pull requests that a human must merge, with per-job cost and duration on a dashboard. The nineteen "you've answered this before" tickets become jobs Jun dispatches and reviews instead of work Jun does by hand. *Honest status:* claytonia's [never-merge rule](https://github.com/lentago/claytonia/issues/117) is practice, not yet an enforced required check.
4. **One front desk for fifteen projects.** *Shipped, partially:* [mitchella](https://github.com/lentago/mitchella), answering from the collective's own runbooks and routing the rest to Jun. *Heads up on the bright line:* [ADR-0007](https://github.com/lentago/.github/blob/main/docs/adr/0007-client-owned-delivery-no-multi-tenant-saas.md) forbids multi-tenant services we operate. A fiscal sponsor is one legal entity and its projects are its own programs, so a desk the collective runs is inside the line. Lentago is a fireable maintainer of it, never the operator.
5. **The funder reports come from one fact base.** *Projected:* the [funder-report fact pipeline](https://github.com/lentago/.github/issues/130). Each project commits its program numbers once; the annual report, each funder's format, and the board deck cite the same facts. Agents draft the narrative, humans merge. The agency's billable change requests end here.
6. **The AI policy is the running practice.** *Projected:* [AI-with-receipts](https://github.com/lentago/.github/issues/127). The collective adopts the reviewed-merge model for documents first, derives a one-page policy from what it actually does, and answers the funder's question with links to merged PRs. *Shipped:* the fleet demonstrates this live; every agent PR in the open repos is a receipt.
7. **The donor data gets out of Salesforce intact.** *Projected:* the [Liberation Pipeline](https://github.com/lentago/.github/issues/123), fifteen sources, fifteen owned exports, restore drills on the game-day cadence. Adding a project never touches another project's collector. The collective leaves Salesforce when the restore drill passes, not before.
8. **Shared tools on hardware the collective owns.** *Shipped:* [osmunda](https://github.com/lentago/osmunda), a small standing Kubernetes cluster reconciled from git, plus a temporary cloud cluster with a hard cost gate ([21 minutes meter-on to meter-off, about five cents](https://github.com/lentago/osmunda/blob/main/runbooks/eks-up.md)). *Honest status:* the n8n workflow engine that would glue the collectors together is a [pre-cutover draft](https://github.com/lentago/osmunda/tree/main/apps/n8n) on osmunda and still runs on a lone container at home.
9. **Privacy posture, because several states now reach nonprofits.** *Projected:* the [privacy posture kit](https://github.com/lentago/.github/issues/131), a data map, minimization, and retention as code. Engineering and posture; counsel does law.

## What got kicked to the curb

| Before | After |
|---|---|
| Salesforce enterprise tier and the agency | *Projected.* Exits when the Liberation Pipeline's restore drill passes and the fact pipeline produces the first funder report. Not a day before. |
| ServiceNow help desk, one agent | Issue forms, a board, and agents doing the repeat work. *Free tier* plus *shipped*. |
| Fifteen website subscriptions on fifteen cards | Fifteen repos, one org, $0. *Shipped.* |
| The AI-policy PDF | A policy derived from merged PRs. *Projected.* |

## The fire-us test

The collective owns the GitHub organization, the cluster hardware, the Grafana account, and every domain. The agent fleet runs in the collective's own containers with the collective's own provider key. Firing us is a runbook, and the runbook is in their vault.

---

*One of [five shops, one tech person each](README.md). Read the tags before you read the story.*

> 🌱 **Lentago Labs** is a pro-bono operations practice for organizations that
> run on volunteers, donations, and one overworked tech person. Everything here
> is free to take, and we practice what we publish: our own estate runs this
> way, in the open. Start at the [org profile](https://github.com/lentago), and
> read this repo on [DeepWiki](https://deepwiki.com/lentago/lupinus).
