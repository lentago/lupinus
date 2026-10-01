# Ridgeback Valley Family Shelter

**Scope:** twelve staff across three buildings, forty beds, a county contract with reporting requirements. **The one tech person:** Dev, "IT Director," which means Dev is also the help desk, the Wi-Fi, the donated laptops, and the person the county auditor emails.

## What they pay for today

| Tool | What it was for | What it costs them (illustrative) | Who knows how it works |
|---|---|---|---|
| ServiceNow ITSM, five agent seats | Help desk and "change management," inherited from a managed-service provider that left in 2025 | A contract the previous executive director signed for three years. Four of the five seats have never logged in. | The MSP. The MSP is gone. |
| Salesforce Nonprofit Cloud plus a consultant retainer | Donor and case records | The retainer is the biggest line on the tech budget. Every report the county wants is a billable change request. | The consultant. |
| An antivirus and backup bundle, per device | Compliance checkbox for the county contract | Per laptop, per year, including the eleven laptops that no longer boot. | Nobody has checked the restore works. |

## The night it broke

A snowstorm closes the county, and the shelter's intake coordinator can't reach the shared drive from the overflow building. Dev opens a ServiceNow ticket out of habit and then realizes Dev is the only agent assigned to the queue. The ticket is a note to self. By the time the Wi-Fi is back, the coordinator has done intake on paper, and that paper has to be typed into Salesforce by Thursday for the county report, which is a change request the consultant bills at an hourly rate because the county changed the form.

## The path out

1. **A help desk that is a private GitHub repo with issue forms.** *Free tier:* GitHub Issues. Staff file a request through a form with the three questions Dev actually needs; labels replace queues; a project board replaces the dashboard nobody opened. *Shipped:* [repo-template](https://github.com/lentago/repo-template) and the fleet's own [lab-run issue form](https://github.com/lentago/asclepias/tree/main/.github/ISSUE_TEMPLATE) are the starting point, and [.github#196](https://github.com/lentago/.github/issues/196) is the private-repo help-desk starter that packages them. This is the one that retires the ServiceNow contract at renewal: a help desk for one agent is a list.
2. **Change management is a pull request.** *Shipped:* the entire fleet runs this way, and the [asclepias glossary](https://github.com/lentago/asclepias/blob/main/manual/glossary.md) translates CAB, CMDB, and PIR into what a one-person shop actually does. Every change to a config, a doc, or a workstation image is a reviewed, recorded PR. The county auditor gets a URL instead of a binder.
3. **The knowledge base is the ops vault.** *Shipped:* [lupinus](https://github.com/lentago/lupinus) in the shelter's private repo. *Projected:* the [Institutional Memory kit](https://github.com/lentago/.github/issues/126) adds a private, grounded Ask that answers staff questions only from the shelter's own runbooks, with hard daily caps, so the Wi-Fi question gets answered at 9 pm without waking Dev.
4. **The front desk that routes to a human.** *Shipped, partially:* [mitchella](https://github.com/lentago/mitchella), a Slack front desk that checks live status before it answers and files nothing without a person's confirmation. Honest status: [it has never made a live API call](https://github.com/lentago/mitchella/blob/main/ROADMAP.md) and can't yet hold a thread. *Projected:* mitchella M1 and M2 close that gap.
5. **Eleven dead laptops become a standard image.** *Shipped:* [kalmia](https://github.com/lentago/kalmia) provisions a fresh Linux box into a configured workstation in one command, with five profiles proven from clean installs. *Projected:* [kalmia#107](https://github.com/lentago/kalmia/issues/107), the donated-hardware refresh profile, "wipe, provision, managed profile, timeboxed to an afternoon per device." That is the afternoon that replaces the per-device bundle.
6. **Alerts that reach a person.** *Shipped:* [drosera](https://github.com/lentago/drosera), dashboards and 41 alert rules on Grafana's free tier, applied from files when a PR merges. Site-down and TLS-expiry probes cover the three buildings' links. *Heads up:* today there is one email contact point and no on-call rotation. For a one-person shop that is the truth of the matter anyway.
7. **Logs kept longer than the firewall keeps them.** *Shipped:* [betula](https://github.com/lentago/betula) ships a Firewalla's full logs to Loki on the free tier, within five minutes of a merged config change, with rollback.
8. **The insurance questionnaire answers itself.** *Projected:* the [Insurance-Receipts Pack](https://github.com/lentago/.github/issues/125): MFA, documented backups with an offline copy, log capture, and an incident habit, assembled so every "yes" on the cyber-insurance form links to the receipt.
9. **The county report comes from one fact base.** *Projected:* the [funder-report fact pipeline](https://github.com/lentago/.github/issues/130). Program numbers committed once, cited in the county report, the board deck, and the annual report. The hourly change request becomes a PR Dev reviews.

## What got kicked to the curb

| Before | After |
|---|---|
| ServiceNow, five seats, three years | Not renewed. Issue forms, labels, a project board, $0. |
| Salesforce consultant retainer | *Projected.* Case records stay in a system of record the county accepts; the retainer shrinks to the reporting work, and the fact pipeline eats that. We don't replace the case system, and we say so. |
| Per-device antivirus and backup bundle | A standard image, a backup with a tested restore, and receipts. *Shipped* for the image; *projected* for the pack. |
| The MSP's binder | A repo the auditor can read. |

## The fire-us test

Dev's org owns the GitHub organization, the Grafana account, and the vault. The runbook for leaving us is a page in the vault. The dashboards are files, and the files are Dev's.

---

*One of [five shops, one tech person each](README.md). Read the tags before you read the story.*

> 🌱 **Lentago Labs** is a pro-bono operations practice for organizations that
> run on volunteers, donations, and one overworked tech person. Everything here
> is free to take, and we practice what we publish: our own estate runs this
> way, in the open. Start at the [org profile](https://github.com/lentago), and
> read this repo on [DeepWiki](https://deepwiki.com/lentago/lupinus).
