# seer.coach — teaser site

A single-file "coming soon" teaser for Seer with a notify-me waitlist. Dark, mysterious, gamery: an all-seeing eye that tracks the cursor, a scramble headline, rotating gameplay hints, and a one-field email capture.

## Files
- `index.html` — the entire site (HTML, CSS, JS inline). No build step.
- `public/seer-logo.png` — favicon.

## Waitlist backend (Supabase)
- Project: `seer-marketing` (org: Sams personal, region: eu-west-2)
- Table: `public.waitlist` (email, source, referrer, user_agent, created_at)
- Emails are stored on submit. Duplicate emails are blocked (case-insensitive) and treated as "already on the list".
- Security: anon can INSERT only. Anon CANNOT read the list back, so emails are never exposed on the public site. A live count is exposed through a `get_waitlist_count()` RPC (count only, no rows).

Credentials are already wired into `index.html` (project URL + publishable key). The publishable key is safe to ship in a public site.

### Seeing your signups
Open the Supabase dashboard for `seer-marketing` and view the `waitlist` table, or query it with the service role. The public site cannot read rows.

## Run locally
Open `index.html` in a browser, or serve the folder:
```
npx serve .
```

## Deploy
Static site, deploy the folder as-is.
```
vercel --prod
```
Then point `seer.coach` at the deployment. No environment variables or framework settings needed.

## Tweaks
- Headline / copy: search `It sees the game` and `The Seer has you` in `index.html`.
- Hint words: the `words` array near the bottom of the script.
- The live count line only appears once 25+ people have joined (honest, not seeded).
