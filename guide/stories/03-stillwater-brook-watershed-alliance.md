# Stillwater Brook Watershed Alliance

**Scope:** a land trust and hatchery with four staff, two hundred members, a visitor center, and sensors in a river. **The one tech person:** Priya, program coordinator, who became the tech person when she was the only one who could get the stream gauge to upload.

## What they pay for today

| Tool | What it was for | What it costs them (illustrative) | Who knows how it works |
|---|---|---|---|
| A facilities work-order SaaS, sold as "ServiceNow-lite" | Maintenance requests for the hatchery and visitor center | Per user, per month, for four users. The walk-in cooler alarm is a phone call to whoever is closest. | The vendor's onboarding video. |
| A sensor vendor's cloud dashboard | Stream temperature and flow | Per sensor, per month, with export locked behind the next tier up. | Priya, barely. |
| A Salesforce-based membership add-on | Members and renewals | Annual, plus a consultant to change the renewal email. | The consultant. |

## The night it broke

A July heat wave. The hatchery's walk-in cooler compressor fails at 11 pm. The alarm is a buzzer on the cooler. The nearest staff member is forty minutes away and asleep. By morning the fish are a loss, and the grant that paid for them requires an incident report by the end of the week, which Priya writes from memory because the cooler's temperature log is on a vendor dashboard that keeps seven days and charges for export.

## The path out

1. **Sensors and alarms for a physical space, as code.** *Shipped:* [epigaea](https://github.com/lentago/epigaea), a Home Assistant estate with 146 devices, a water-leak automation, battery-health tracking, and CI that deploys a merged change within five minutes and rolls back with a phone alert if it fails. *Projected:* the [cold-chain and facilities kit](https://github.com/lentago/.github/issues/129): a sensor bill of materials, the Home Assistant config module, dashboards, and an escalation runbook, piloted on our own hardware first with a month of catches published. The cooler gets a probe, the probe gets a threshold, the threshold calls Priya's phone and then the backup's.
2. **The temperature log is theirs.** *Shipped:* [drosera](https://github.com/lentago/drosera) dashboards on the Grafana free tier, applied from files. The cooler trace, the stream gauge, and the visitor-center door count on one pane, with retention the alliance controls. *Shipped:* [betula](https://github.com/lentago/betula)'s pattern for keeping full logs longer than the device does. Honest status: betula's one shipped client is a firewall. A sensor client is the [core/client split](https://github.com/lentago/betula/issues/74) the roadmap already names.
3. **A sensor trip opens a work order.** *Free tier:* GitHub Issues. *Projected:* [.github#195](https://github.com/lentago/.github/issues/195), the automation that turns an epigaea alert into an issue with the temperature trace attached. The fleet's preferred runtime for exactly this is "Actions cron plus Issues plus email" ([ADR-0007](https://github.com/lentago/.github/blob/main/docs/adr/0007-client-owned-delivery-no-multi-tenant-saas.md)). That replaces the work-order SaaS for a four-person team.
4. **The visitor center screen shows what matters right now.** *Shipped, phase 1:* [brasenia](https://github.com/lentago/brasenia), a wall display that streams a composed brief to a Roku dev channel. *Projected:* phase 3, panes driven by real activity, and the [Chromecast-native path](https://github.com/lentago/brasenia/issues/12) that retires the Roku chain. Stream temperature on the lobby wall is the pitch.
5. **"Are we open" from one source of truth.** *Shipped:* [drosera's status page](https://github.com/lentago/drosera/tree/main/status-page), a GitHub Pages page rebuilt every thirty minutes. *Projected:* [drosera#197](https://github.com/lentago/drosera/issues/197), one source that drives the storm-closure banner, the status page, the lobby pane, and the business listings.
6. **Public data, published with provenance.** *Shipped:* [uvularia](https://github.com/lentago/uvularia), the records vault. The alliance's minutes, meeting notices, permits, and trail announcements live as plain files in its own GitHub, each with its source attached, and a public ["Is it posted?" board](https://lentago.github.io/uvularia-demo-site/board/) shows whether what had to be posted went up on time. That board is already this alliance's: uvularia's demonstration client is Stillwater. *Projected:* the grounded Ask box that answers only from those records, in the alliance's own AWS account with hard daily caps. The code is merged, but a live answer hasn't been recorded yet ([.github#200](https://github.com/lentago/.github/issues/200)). The stream data becomes a public page members can ask questions of.
7. **Members and renewals.** *Free tier:* the processor's membership feature, plus the mailing list. *Projected:* the [Liberation Pipeline](https://github.com/lentago/.github/issues/123) keeps the export current. We don't build the membership database, and the consultant's renewal-email change becomes a template the alliance edits.

## What got kicked to the curb

| Before | After |
|---|---|
| Facilities work-order SaaS | Sensor trips open GitHub Issues. *Projected.* |
| Sensor vendor dashboard with paid export | Home Assistant on their own box, Grafana free tier, data they keep. *Shipped* pattern, *projected* kit. |
| Salesforce membership add-on and consultant | The processor plus an owned export. *Free tier* plus *projected*. |
| The buzzer on the cooler | A phone call at 11:02 pm, to two people. |

## The fire-us test

The Home Assistant box is in the visitor center. The Grafana account is the alliance's. The sensor bill of materials is a list in their repo. Everything that calls Priya's phone is configured in a file she can read.

---

*One of [five shops, one tech person each](README.md). Read the tags before you read the story.*

> 🌱 **Lentago Labs** is a pro-bono operations practice for organizations that
> run on volunteers, donations, and one overworked tech person. Everything here
> is free to take, and we practice what we publish: our own estate runs this
> way, in the open. Start at the [org profile](https://github.com/lentago).
