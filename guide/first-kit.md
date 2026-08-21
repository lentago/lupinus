# Your first kit

A guided first run, start to finish, ending with something real on the internet.

We use the campaign-site kit for this. Not because a campaign site is
necessarily what you need — you may not need one at all — but because it is the
shortest honest path through the whole shape: pick, intake, drill, receipt,
own. Everything else here expects to be adopted the same way, so doing it once
on the cheapest product makes the expensive ones familiar.

**What it costs:** nothing. **What you need:** a GitHub account, about an hour,
and a payment processor account if you want the donate button to actually work
(you can finish without one).

## What you are about to do

1. Answer a one-page questionnaire about the campaign.
2. Copy a template into your own GitHub organization.
3. Put your answers into one configuration file.
4. Watch it build and deploy to a live address.
5. Write down how long it took.

Step 5 is the one people skip and the one that matters most. See
[why below](#about-that-last-step).

## Before you start

- **A GitHub organization you control.** A personal account works. If your
  organization has its own GitHub, use that — the point is that this lands in an
  account you own.
- **About an hour.** It is usually much less, but do not start this fifteen
  minutes before a meeting; the slow steps are outside your control (DNS, a
  build queue) and rushing them is how mistakes happen.
- **Optional: a payment processor account.** The kit points at a processor's own
  hosted donate page or widget. It never touches card data — see the kit's own
  notes on why that boundary exists.

## Run it

Everything from here is in the kit itself, because the kit is where it belongs
— it travels with the code and stays correct as the code changes:

1. **Read [monarda's adoption runbook](https://github.com/lentago/monarda/blob/main/ADOPTION.md).**
   Start at the prerequisites and work down. It is written for you, not for us.
2. **Fill in [the intake questionnaire](https://github.com/lentago/monarda/blob/main/INTAKE.md).**
   Every question names the configuration field its answer becomes, so this is
   not busywork — it is the configuration, in plain English, before you touch a
   file.
3. **Work [the dry run](https://github.com/lentago/monarda/blob/main/DRY-RUN.md)**
   step by step. Each step tells you what "it worked" looks like. If a check
   does not go green, stop there rather than pressing on — the next step assumes
   the last one worked.

Come back here when you have a live URL.

## About that last step

The dry run ends with a receipt: the date, who ran it, how long it took
end to end, and which step was slowest. Fill it in honestly, including the
number you are not proud of.

This is the habit worth taking from this exercise, more than the site itself:

- **It makes claims checkable.** "This takes an afternoon" is a sales line until
  someone writes down that it took two hours and forty minutes, most of it
  waiting for DNS.
- **It tells you where the pain is.** The slowest step is the one to pre-stage
  next time, or to automate, or to warn the next person about.
- **It ages visibly.** A receipt from six months ago against a product that has
  changed since is a prompt to re-run, not a guarantee.

Every runbook in this suite ends this way, and a product cannot be listed as a
[Kit](tiers.md) until someone has produced one.

## What you have when you are done

A live site, in a repository your organization owns, deployed by a workflow you
can read, on infrastructure you control. Nothing in it points back at us except
some links you are free to delete. If you stop working with us tomorrow, nothing
about it changes.

That is the whole promise, demonstrated on something small enough to verify.

## Where to go next

- **[The picker](picker.md)** — now that you know the shape, find the product
  that addresses an actual need of yours.
- **[Your ops vault](../estate/README.md)** — the other half of this repository:
  where you record what you now run, what it depends on, and what happens to it
  over time. Adding your first component note takes about five minutes and is
  most usefully done while this run is fresh.
- **[Conventions](conventions.md)** — the rules that hold for every product,
  including how to keep this guide up to date.
