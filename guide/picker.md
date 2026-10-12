# Which of these fits my operation?

Start from what you need, not from what we built. Each row below names the
product that covers a need, what it'll cost you per month, and how much of it you
can stand up from the repository alone today. That last column is the
[tier](tiers.md) — read it as a warning label, because it's the honest measure of
how much work is still on you.

**Nothing here is hosted by us.** Everything you adopt runs in accounts you own,
on infrastructure you control. See [conventions](conventions.md) for the
mechanics, and the [no-hosting pledge](https://github.com/lentago/.github/blob/main/docs/adr/0007-client-owned-delivery-no-multi-tenant-saas.md)
for why it works that way.

## I need to…

Rows are grouped by the promise they keep, in the order the rest of the guide
uses. Each row keeps the need in your words.

## Your site and giving page

| …do this | Adopt | Runs on | Cost/month | Tier |
|---|---|---|---|---|
| **Put up a campaign or fundraising site** my organization owns outright | [monarda](https://github.com/lentago/monarda) | Your GitHub Pages (or your S3/CloudFront) | **$0** on Pages | Kit |

## Your records and your proof

| …do this | Adopt | Runs on | Cost/month | Tier |
|---|---|---|---|---|
| **Publish our public records and show, live, what was posted on time** — minutes, notices, bylaws, policies, with the posting rules next to them and a public "Is it posted?" board | [uvularia](https://github.com/lentago/uvularia) ([records template](https://github.com/lentago/uvularia-records-template); one repository is the whole first rung, a [branded site](https://github.com/lentago/uvularia-site-template) is optional) | Your GitHub + your GitHub Pages | **$0** | Kit ([receipt](https://github.com/lentago/uvularia/blob/main/receipts/2026-10-12-agent-run-rung1.md), [live demo board](https://lentago.github.io/uvularia-demo-records/)) |

## Your machines and logins

| …do this | Adopt | Runs on | Cost/month | Tier |
|---|---|---|---|---|
| **Set up a working laptop or VM** for whoever does your ops — same tools every time | [kalmia](https://github.com/lentago/kalmia) (the Ansible layer only) | Any Linux machine you already have | **$0** | Kit |

## Your alarms and status

| …do this | Adopt | Runs on | Cost/month | Tier |
|---|---|---|---|---|
| **Publish a status page** your staff and community can check | [drosera](https://github.com/lentago/drosera) (`status-page/`) | Your GitHub Pages | **$0** | Kit |
| **See your servers and services** — dashboards, alerts, log search — without buying a monitoring product | [drosera](https://github.com/lentago/drosera) (full stack) | Your Grafana Cloud free tier | **$0** on the free tier | Pattern |
| **Capture and keep logs** from a firewall or cloud service for longer than the vendor keeps them | [betula](https://github.com/lentago/betula) | Your log destination + the source device | Varies by destination | Pattern |

## Your help desk and runbooks

No row here yet. The front desk, mitchella, is a Pattern for now, not a kit
you can stand up whole; its row in the [tier registry](tiers.md#where-each-product-stands)
says what is still missing.

## Your data and your exit

| …do this | Adopt | Runs on | Cost/month | Tier |
|---|---|---|---|---|
| **Audit what you would lose** if a vendor disappeared, and prove your exits work | [the lock-in ledger](https://github.com/lentago/.github/tree/main/fleet-reports/lock-in) | Nothing — it is a review you run | **$0** | Kit |

For keeping logs from a firewall or cloud service, see the log-capture row under
[your alarms and status](#your-alarms-and-status).

## When you need them

These three are not every shop's week. Skip them until you do.

### Your building

| …do this | Adopt | Runs on | Cost/month | Tier |
|---|---|---|---|---|
| **Monitor a physical space** — temperatures, doors, power — and act on what you see | [epigaea](https://github.com/lentago/epigaea) | A machine on-site + sensors | Hardware only | Pattern |
| **Put a shared display** on a wall that shows what matters right now | [brasenia](https://github.com/lentago/brasenia) | A media host + a TV | Hardware only | Pattern |

### Cloud you own

| …do this | Adopt | Runs on | Cost/month | Tier |
|---|---|---|---|---|
| **Run a real AWS environment** you own: private networking, containers, a managed database, backups, alarms, budgets | [solidago](https://github.com/lentago/solidago) | Your AWS account + a domain you register | **~$130** ([teardown](https://github.com/lentago/solidago/blob/main/docs/RUNBOOK.md) drops it to ~$40) | Platform |
| **Spin up a temporary Kubernetes cluster** for a specific job and destroy it the same day | [osmunda](https://github.com/lentago/osmunda) (`runbooks/`) | Your AWS account | **~$0.15/hour, while it exists** | Kit |

### AI with receipts

| …do this | Adopt | Runs on | Cost/month | Tier |
|---|---|---|---|---|
| **Have background agents do routine repo work** and open pull requests for review | [claytonia](https://github.com/lentago/claytonia) | Your own hardware + an AI provider account | Provider usage | Pattern |

## The guide itself

This one is the guide's scaffolding, not a promise: it keeps your own
repositories consistent.

| …do this | Adopt | Runs on | Cost/month | Tier |
|---|---|---|---|---|
| **Standardize your own repositories** — one CI definition, consistent settings | [shared-workflows](https://github.com/lentago/shared-workflows) + [repo-template](https://github.com/lentago/repo-template) | GitHub | **$0** | Platform |

## Reading the tier column

- **Kit** — clone it today and stand it up from the repo alone. Someone has run
  the drill and recorded how long it took.
- **Platform** — adoptable with about a day's work and your own accounts. You
  will swap a short, mechanical list of our values for yours.
- **Pattern** — read it, lift the parts you need, but do not try to stand it up
  whole. These are real systems built for one estate; what transfers is the
  approach, and each one says plainly what is worth taking.

A Pattern is not a lesser product — it's an honest label. Several are the most
interesting systems in the suite. They're simply not packaged for a stranger
yet, and [tiers](tiers.md) tracks what would have to change.

## If you're not sure where to start

Start with [your first kit](first-kit.md). It's the campaign-site kit, it costs
nothing, it needs no accounts beyond GitHub and a payment processor, and it ends
with a live site. The point is less the site than the shape: you'll have run a
drill, recorded a receipt, and seen how everything else here expects to be
adopted.

## What we are not

No product here collects donations directly, stores donor records, or processes
payment cards — the campaign kit points at a payment processor's own hosted
widget and never touches card data. None of them is a CRM, a case-management
system, or an accounting package. If that's what you need, buy one; then use the
[lock-in ledger](https://github.com/lentago/.github/tree/main/fleet-reports/lock-in)
to check you can leave it later. Nor is any of it phones, printers, or Wi-Fi,
which is where a good part of your week goes.
