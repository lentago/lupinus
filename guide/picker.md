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

| …do this | Adopt | Runs on | Cost/month | Tier |
|---|---|---|---|---|
| **Put up a campaign or fundraising site** my organization owns outright | [monarda](https://github.com/lentago/monarda) | Your GitHub Pages (or your S3/CloudFront) | **$0** on Pages | Kit |
| **Set up a working laptop or VM** for whoever does your ops — same tools every time | [kalmia](https://github.com/lentago/kalmia) (the Ansible layer only) | Any Linux machine you already have | **$0** | Kit |
| **Publish a status page** your staff and community can check | [drosera](https://github.com/lentago/drosera) (`status-page/`) | Your GitHub Pages | **$0** | Kit |
| **Audit what you would lose** if a vendor disappeared, and prove your exits work | [the lock-in ledger](https://github.com/lentago/.github/tree/main/fleet-reports/lock-in) | Nothing — it is a review you run | **$0** | Kit |
| **Run a real AWS environment** you own: private networking, containers, a managed database, backups, alarms, budgets | [solidago](https://github.com/lentago/solidago) | Your AWS account + a domain you register | **~$130** ([teardown](https://github.com/lentago/solidago/blob/main/docs/RUNBOOK.md) drops it to ~$40) | Platform |
| **Spin up a temporary Kubernetes cluster** for a specific job and destroy it the same day | [osmunda](https://github.com/lentago/osmunda) (`runbooks/`) | Your AWS account | **~$0.15/hour, while it exists** | Kit |
| **See your servers and services** — dashboards, alerts, log search — without buying a monitoring product | [drosera](https://github.com/lentago/drosera) (full stack) | Your Grafana Cloud free tier | **$0** on the free tier | Pattern |
| **Capture and keep logs** from a firewall or cloud service for longer than the vendor keeps them | [betula](https://github.com/lentago/betula) | Your log destination + the source device | Varies by destination | Pattern |
| **Monitor a physical space** — temperatures, doors, power — and act on what you see | [epigaea](https://github.com/lentago/epigaea) | A machine on-site + sensors | Hardware only | Pattern |
| **Put a shared display** on a wall that shows what matters right now | [brasenia](https://github.com/lentago/brasenia) | A media host + a TV | Hardware only | Pattern |
| **Have background agents do routine repo work** and open pull requests for review | [claytonia](https://github.com/lentago/claytonia) | Your own hardware + an AI provider account | Provider usage | Pattern |
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
to check you can leave it later.
