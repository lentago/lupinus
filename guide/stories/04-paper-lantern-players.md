# Paper Lantern Players

**Scope:** a community theatre, four productions a year, one part-time managing director, a board, and a hundred-odd volunteers who build sets and sell tickets. **The one tech person:** Theo, board treasurer, a bookkeeper by day, who keeps the website alive because the domain renewal email comes to him.

## What they pay for today

| Tool | What it was for | What it costs them (illustrative) | Who knows how it works |
|---|---|---|---|
| Salesforce, sold as "patron management" | Subscribers, donors, and season tickets | A nonprofit discount on a license nobody has opened since the person who bought it left the board. | Nobody. |
| A ticketing platform | Ticket sales | A per-ticket fee, which is fine. | Theo, and the box-office volunteer. |
| A domain registered to a former volunteer's personal account | The theatre's name on the internet | The renewal is cheap. The volunteer is in another state and may or may not see the email. | The former volunteer. |
| A scheduling app, paid tier | Volunteer shifts for set builds and front of house | Per month, for a feature the free tier almost had. | The stage manager. |

## The night it broke

Opening night of the spring show. The website is down because the domain lapsed: the renewal email went to the former volunteer's spam folder. Tickets are still selling through the ticketing platform, but the theatre's own URL shows a parked page with ads. Theo finds out from a patron at the door. He cannot renew the domain because it is not his, and the registrar will not talk to him.

## The path out

1. **Ownership insurance for the theatre's presence.** *Projected:* the [Digital Custody audit](https://github.com/lentago/.github/issues/124): domain, DNS, site, and settings custody as code, plus an access register in git where every credential has a named steward and offboarding is a pull request. This is the whole story in one kit, and it is sized "effort S" on the roadmap. *Shipped already:* the fleet's own [renewal calendar](https://github.com/lentago/.github/tree/main/fleet-reports/lock-in) checks daily and opens an issue before a domain or certificate lapses. The theatre gets the same workflow in its own repo.
2. **A campaign page per season, owned outright.** *Shipped:* [monarda](https://github.com/lentago/monarda). Four productions a year means four campaign pages, each a copy of one config file, each on GitHub Pages for nothing, each pointing at the ticketing platform the theatre already likes.
3. **Patrons live where the tickets are sold.** *Free tier:* the ticketing platform already knows every patron and every seat, and exports. Salesforce was a second copy nobody updated. *Projected:* the [Liberation Pipeline](https://github.com/lentago/.github/issues/123) keeps that export in the theatre's own storage, so the patron list survives a change of platform.
4. **Volunteer shifts.** *Projected, and deliberately only a spike:* [.github#132](https://github.com/lentago/.github/issues/132), "evaluate, don't build," a two-evening look at free-tier scheduling tools against a volunteer-org needs profile, ending in a memo that says integrate, build, or decline. We don't build a scheduling app on a hunch.
5. **Filing deadlines as issues.** *Projected:* the [Good-Standing Kit](https://github.com/lentago/.github/issues/122). The 990, the state charities filing, the annual report, and the event permits open themselves as issues with the filed copy committed as the receipt. Theo is a bookkeeper; this is the part he will love.
6. **The snow-day banner.** *Projected:* [drosera#197](https://github.com/lentago/drosera/issues/197), one "are we open" source of truth. Show cancelled for weather is a one-line change that updates the site, the status page, and the listing.

## What got kicked to the curb

| Before | After |
|---|---|
| Salesforce patron license | Cancelled. The ticketing platform's export, owned. |
| Domain on a former volunteer's account | Transferred to the theatre, with a steward named in the access register. *Projected* kit, *shipped* renewal-check workflow. |
| Scheduling app paid tier | Decided by a memo, not a renewal notice. |
| The renewal email in someone's spam | An issue that opens itself thirty days early. |

## The fire-us test

Theo's name is on the registrar account, the theatre's name is on the GitHub organization, and the access register says who holds what. Nothing about the theatre's presence routes through a Lentago account, because that was the problem to begin with.

---

*One of [five shops, one tech person each](README.md). Read the tags before you read the story.*

> 🌱 **Lentago Labs** is a pro-bono operations practice for organizations that
> run on volunteers, donations, and one overworked tech person. Everything here
> is free to take, and we practice what we publish: our own estate runs this
> way, in the open. Start at the [org profile](https://github.com/lentago), and
> read this repo on [DeepWiki](https://deepwiki.com/lentago/lupinus).
