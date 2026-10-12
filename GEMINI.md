# Gemini / Antigravity Agent Guidelines

These guidelines are active on every turn. Adhere to the following rules when developing, configuring, or debugging this repository:

1. **Storage & Publishing**:
   - For database or Upstash targets: Do NOT require or execute GitHub commits. Publishing happens directly over HTTP via the site's `/api/posts` endpoint.
   - For pure serverless/git-backed targets: Commit only `content/posts/` and `public/uploads/`. Never stage untracked configuration or docs.
2. **Image Routing**:
   - Next.js images must always use the URL path `/uploads/<filename>`.
   - Never use `/static/uploads/` for Next.js image URLs. Maintain the rewrite in `next.config.ts` from `/static/uploads/:path*` to `/uploads/:path*`.
   - Ensure hero image files are copied into `<target>/public/uploads/` during publishing.
3. **AI Image Engines**:
   - Order: Cloudflare Workers AI (`flux-1-schnell`) -> Gemini image REST (`gemini-3.1-flash-image-preview`) -> Codex (`gpt-image-2`) -> Tavily stock search.
   - Prompts must forbid text, letters, watermarks, and UI elements.
4. **Multi-Website Isolation**:
   - Each website has its own repository, secret token, and storage engine. Do not assume one global repo applies to all websites.
