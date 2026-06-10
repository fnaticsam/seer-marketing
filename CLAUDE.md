# seer.coach — teaser site

Marketing/waitlist teaser for **SEER, the AI coach for gaming** (League of Legends first). The actual product lives in `~/Code/seer-coach` — read that repo for ground truth on features before writing marketing copy.

## Architecture

- `public/index.html` — **the entire site**. HTML, CSS, and JS inline. No build step, no framework, no package.json. Keep it that way.
- `public/seer-logo.png` — favicon/logo. Only binary asset; new illustrations must be inline SVG/CSS.
- `vercel.json` — static deploy config (`framework: null`, `cleanUrls`).
- `review/` and `.playwright-mcp/` — gitignored screenshot scratch dirs.

## Waitlist backend (Supabase)

- Project `seer-marketing` (org: Sams personal, eu-west-2). Credentials are inline in `index.html` — the publishable key is safe to ship; do not remove or "fix" it.
- `public.waitlist` table: anon can INSERT only, never SELECT. Duplicates return 409 → treated as "already on the list".
- Live count comes from the `get_waitlist_count()` RPC (count only) and is only displayed once ≥25 signups — honest, not seeded. Keep that threshold.

## Conventions

- Brand: dark, mysterious, gamery. Gradient `--purple #a85cff → --pink #ff5ea8 → --orange #ff6a1a` on bg `#0a0810`. The all-seeing eye is the mascot.
- Copy register: irreverent, gamer-native ("get gud", "hardstuck", "LP"). No corporate fluff.
- Honesty: pre-launch product — no fake testimonials, fake counts, or invented measurements. Stylized fictional game scenarios in demos are fine.
- Every animation must respect `prefers-reduced-motion` (there's a global kill switch at the bottom of the CSS).
- Fonts: Space Grotesk (display), Inter (body), JetBrains Mono (labels) via Google Fonts.

## Workflows

- Run locally: `npx serve public -l 4173` (or open `public/index.html` directly).
- Verify visually: Playwright screenshots; scroll-reveal `.rv` elements are opacity:0 until in view — add the `in` class via JS before full-page screenshots.
- Deploy: `vercel --prod` from repo root. Domain: seer.coach. No env vars.
- Signups: view the `waitlist` table in the Supabase dashboard (the public site can't read rows).
