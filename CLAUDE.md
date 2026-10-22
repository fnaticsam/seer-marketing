# seer.coach — teaser site

Marketing/waitlist teaser for **SEER, the AI coach for gaming** (League of Legends first). The actual product lives in `~/Code/seer-coach` — read that repo for ground truth on features before writing marketing copy.

## Architecture

- `public/index.html` — **the entire site**. HTML, CSS, and JS inline. No build step, no framework, no package.json. Keep it that way.
- `public/logos/seer-mark.svg` — primary eye/star mark; `seer-mark-icon.svg` is the SVG favicon. `public/apple-touch-icon.png` provides the raster icon fallback.
- `public/seer-logo.png` — retired badge retained for history. Presentation PNG variants and the social share card are intentional exports; use inline SVG/CSS for new page illustrations.
- `scripts/gen-designsystem.py` — source for the eight design previews. Regenerate those pages with Python after template changes.
- `docs/seer-brand-powerpoint.md` — final Seer Protocol brand reference; `public/brand.md` is its published copy. Keep both copies identical.
- `vercel.json` — static deploy config (`framework: null`, `cleanUrls`).
- `review/` and `.playwright-mcp/` — gitignored screenshot scratch dirs.

## Waitlist backend (Supabase)

- Project `seer-marketing` (org: Sams personal, eu-west-2). Credentials are inline in `index.html` — the publishable key is safe to ship; do not remove or "fix" it.
- `public.waitlist` table: anon can INSERT only, never SELECT. Duplicates return 409 → treated as "already on the list".
- Live count comes from the `get_waitlist_count()` RPC (count only) and is only displayed once ≥25 signups — honest, not seeded. Keep that threshold.

## Conventions

- Brand: Seer Protocol — Studio Black `#121416`, Zinc `#F4F4F5`, and Seer Green `#28D397` as the primary accent. Gold, red, blue and purple communicate recommendation, warning, team and analysis roles. Follow the final brand reference rather than the archived design alternatives. The all-seeing eye is the mascot.
- Copy register: irreverent, gamer-native ("get gud", "hardstuck", "LP"). No corporate fluff.
- Honesty: pre-launch product — no fake testimonials, fake counts, or invented measurements. Stylized fictional game scenarios in demos are fine.
- Every animation must respect `prefers-reduced-motion` (there's a global kill switch at the bottom of the CSS).
- Fonts: Oswald (display), Inter (body), JetBrains Mono (labels), and Orbitron (wordmark) via Google Fonts.

## Workflows

- Run locally: `python3 -m http.server 4173 --directory public`, then open `http://localhost:4173`. This needs no downloaded preview package. Use localhost rather than opening the HTML as a file so browser APIs have a normal origin.
- Verify visually: Playwright screenshots; scroll-reveal `.rv` elements are opacity:0 until in view — add the `in` class via JS before full-page screenshots.
- Deploy: `vercel --prod` from repo root. Domain: seer.coach. No env vars.
- Signups: view the `waitlist` table in the Supabase dashboard (the public site can't read rows).
