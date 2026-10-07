# Pennywell Street Pantry

**Scope:** all-volunteer. Forty volunteers, zero staff, one church basement, two distributions a week. **The one tech person:** Marta, a retired controls engineer, about six hours a week, "until somebody younger shows up."

## What they pay for today

| Tool | What it was for | What it costs them (illustrative) | Who knows how it works |
|---|---|---|---|
| Salesforce Nonprofit Cloud, ten free licenses | "Donor management," recommended by a board member's nephew | The licenses were free. The consultant who set it up was not, and the renewal of the add-ons he picked is due in March. | Nobody since the nephew moved to Denver. |
| A website builder subscription | The pantry's site and donate button | Monthly. The donate button sends people to a page the nephew built. | Marta, sort of. |
| A mailing-list tool, paid tier | The monthly newsletter | They crossed the free tier's contact cap two years ago and never looked back. | The volunteer who writes the newsletter. |

## The night it broke

A Tuesday in October. The fall food drive opens Saturday. The donate page returns an error nobody can read, and the only person who could log in to fix it is in Denver and not answering. Marta has the website builder's password, but the donate widget lives in Salesforce, and she does not have that one. She emails the nephew. She emails the consultant. She gets the pantry's treasurer to find the invoice so she can at least call somebody.

The drive opens Saturday with a hand-written "donate at the door" sign.

## The path out

1. **One page for the drive, in the pantry's own GitHub account.** *Shipped:* [monarda](https://github.com/lentago/monarda), the campaign-site kit. Marta fills in the [intake questionnaire](https://github.com/lentago/monarda/blob/main/INTAKE.md), edits one config file, and GitHub Pages serves it for nothing. The donate button points at the processor's own hosted page, so no card data ever touches the site ([ADR-0002](https://github.com/lentago/monarda/blob/main/docs/adr/0002-processor-hosted-payments-only.md)). *Heads up:* the [timed dry-run](https://github.com/lentago/monarda/blob/main/DRY-RUN.md) has not been run yet ([monarda#5](https://github.com/lentago/monarda/issues/5)), so we don't have a receipt for how long a first run takes. We'd run it with Marta and record hers.
2. **The donor list lives where the money lands.** *Free tier:* the processor (Givebutter, Zeffy, and others) already keeps every donor and every gift, and exports it. That is the "CRM" the pantry was actually using Salesforce for.
3. **A copy they own, forever.** *Projected:* the [Liberation Pipeline](https://github.com/lentago/.github/issues/123) exports the processor's donor data and the mailing list on a schedule into storage the pantry owns, in open formats, with a restore drill so the copy is proven rather than hoped. This is the piece that makes "leaving Salesforce" safe: nothing is lost on the way out.
4. **The deadlines stop living in one person's head.** *Projected:* the [Good-Standing Kit](https://github.com/lentago/.github/issues/122) turns the 990-N, the state charities filing, and the annual report into GitHub Issues that open themselves before the due date, with the filed copy committed as the receipt.
5. **A place to write down how the pantry's tech works.** *Shipped:* the [lupinus ops vault](https://github.com/lentago/lupinus), a plain-folder notebook that opens in Obsidian or any text editor, in the pantry's own private repo. When somebody younger shows up, the first thing they read is Marta's notes.
6. **Someone to call, if she needs to.** *Shipped:* [support, pro bono](https://github.com/lentago/lupinus/blob/main/support/README.md). Best effort, no on-call, free for a food pantry.

## What got kicked to the curb

| Before | After |
|---|---|
| Salesforce add-ons renewal in March | Cancelled. The processor's export plus a copy they own. |
| Website builder subscription | GitHub Pages, $0. |
| Mailing-list paid tier | Still paid, for now. Honest answer: the free tiers cap contacts, and the pantry is over the cap. *Projected:* the Liberation Pipeline at least guarantees the list is theirs to move. |
| The nephew | A runbook. |

## The fire-us test

Marta's repo is in the pantry's GitHub account. The processor account is the treasurer's. The domain is registered to the pantry, not to a volunteer. If Lentago vanished tomorrow, the site would still build on Saturday.

---

*One of [five shops, one tech person each](README.md). Read the tags before you read the story.*

> 🌱 **Lentago Labs** is a pro-bono operations practice for organizations that
> run on volunteers, donations, and one overworked tech person. Everything here
> is free to take, and we practice what we publish: our own estate runs this
> way, in the open. Start at the [org profile](https://github.com/lentago).
