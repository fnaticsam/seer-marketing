# seer.coach — teaser site

A single-file teaser for **SEER, the AI coach for League of Legends**, with a notify-me waitlist. Dark, mysterious, gamery: an all-seeing eye that tracks the cursor, a scramble headline, an auto-playing product demo, and email capture at six touchpoints.

## Files
- `public/index.html` — the entire site (HTML, CSS, JS inline). No build step.
- `public/logos/seer-mark.svg` — THE logo (traced new eye+star mark, `currentColor`); `seer-mark-icon.svg` is the favicon tile.
- `public/apple-touch-icon.png` — 180×180 raster of the mark icon (also the PNG favicon fallback).
- `public/seer-logo.png` — retired old teal badge (unused, kept for history).
- `public/og.png` — 1200×630 share card (Discord/X/Reddit embeds). Regenerate via a scratch page (new mark + headline) screenshotted at 1200×630.
- `vercel.json` — static deploy config.

## Page structure (top to bottom)
Nav (Demo/Why/Product/How + CTA) → Hero (headline, waitlist form #1, "Watch Seer cook") → coach-line marquee ribbon → **Seer in action** demo (auto-playing Profile / Draft / Live / Post-game tabs mirroring the real app flow at sam-seer.vercel.app, with word-by-word streaming coach messages and data-point chips; pauses on hover, seeks on tab click, cancels off-screen) → trust strip → Problem cards → Product cards (with "see it in the demo" jump links) → How it works (animated SVG mini-scenes) → mid-page form #2 → The Receipts (Gemini/Overwolf/Fnatic + founder note + roadmap pills) → FAQ (`details/summary`) → final CTA (the eye opens on arrival; form #3) → footer.

## Waitlist backend (Supabase)
- Project: `seer-marketing` (org: Sams personal, region: eu-west-2)
- Table: `public.waitlist` (email, source, referrer, user_agent, created_at). `source` is `hero` / `mid` / `cta` via `data-source`.
- Emails are stored on submit. Duplicates are blocked (case-insensitive) and treated as "already on the list" (409).
- Security: anon can INSERT only, never read. A live count is exposed through `get_waitlist_count()` (count only) and is displayed only once 25+ people have joined (honest, not seeded).

Credentials are wired into `index.html` (project URL + publishable key). The publishable key is safe to ship in a public site.

### Seeing your signups
Open the Supabase dashboard for `seer-marketing` and view the `waitlist` table, or query it with the service role. The public site cannot read rows.

## Run locally
```
npx serve public -l 4173
```
Note: scroll-reveal `.rv` elements are invisible until in view — when taking full-page screenshots, add the `in` class first. The demo only autoplays once its shell is ≥35% visible.

## Deploy
Static site, deploy as-is:
```
vercel --prod
```
Then point `seer.coach` at the deployment. No environment variables or framework settings needed.

## Tweaks
- Hero copy: search `every game you ever inted` in `index.html`.
- Demo scenario/messages: the `SCRIPTS` array in the demo engine (timestamps in ms, `fx` keys map to the `FX` object).
- Ribbon coach lines: the two duplicate `<span>` blocks in `.ribbon-track`.
- Rotating hint words: the `words` array.
- All animation respects `prefers-reduced-motion` (CSS kill-switch + a JS `REDUCED` flag; the demo renders as a static storyboard).
