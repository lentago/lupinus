# Accounts

One note per account, platform, or vendor your products depend on. These are the
nodes everything else points at, so they carry the answers you need in a hurry.

**Never put a credential in these notes.** Not a password, not an API key, not a
recovery code. Record *where* the credential lives — your password manager, your
cloud secret store — and who can reach it. A vault in a git repository is
exactly the wrong place for secrets, and unlike a leaked file, a leaked git
history is forever.

## What a good account note has

```markdown
# AWS

Our production cloud account.

- **Account number:** <the identifier, which is not a secret>
- **Who has access:** alex (admin), sam (read-only)
- **Credentials live in:** 1Password → Infrastructure vault
- **Billing:** finance@ourorg.example, ~$140/month
- **Support plan:** Basic
- **If we lost access:** root recovery goes to the shared ops mailbox

## Used by

- [solidago](../products/solidago.md)
```

## Suggested notes to start with

Create these as they become real — an empty file for something you do not use is
just noise:

- `github-org.md` — where your repositories live and who administers them
- `dns.md` — your registrar and who can change records (this one is load-bearing
  more often than people expect)
- `aws.md` — if you adopt anything cloud
- `processor.md` — your payment processor, if you take donations
- `email.md` — where alerts and password resets actually arrive

## The "Used by" section

Adding a back-link from an account to the products that use it is optional —
Obsidian's backlink pane shows you the same thing automatically. Write it out
anyway if you want it visible in plain GitHub, or for the benefit of colleagues
who never open a vault.
