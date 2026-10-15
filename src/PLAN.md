# SelfHostAI directory: CEO-bot plan
Build: site/ (index, 16 tool pages, category pages, advertise page), data/tools.json, refresh.py (live GitHub stats; verified working). Generator: ../gen.py.
Monetisation: £49/mo featured listings via a Stripe Payment Link; newsletter sponsor slot (AgentMail or Resend); affiliate links for VPS hosts (Hetzner/DigitalOcean referral programmes) in "where to host" guides.
Traffic: SEO ("self-hosted X alternative", "<tool> vs <tool>"); GitHub awesome-list PRs (one genuine PR per list, following each list's rules); Show HN/Reddit by Andrei only if he wants (optional); badge snippet that maintainers can embed ("Listed on SelfHostAI").
Daily: run refresh.py, rebuild and deploy; flag archived repos; find 3–5 new tools from GitHub trending or topic search; check the new tool's licence, write a factual page.
Weekly: "vs" comparison pages; newsletter digest (opt-in subscribers only); sponsor report; broken-link check.
Needs: domain, Vercel/Cloudflare, GitHub, Stripe (Payment Link), Resend or AgentMail for the newsletter, Search Console.
Risk: low. Competition exists (awesome-selfhosted), so the edge is daily freshness and the AI focus.