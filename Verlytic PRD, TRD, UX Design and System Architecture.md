# Verlytic: PRD, TRD, UX Design and System Architecture

*Version 1.0 · 9 Oct 2026 · Research gathered 4 Oct 2026 · Companion file: AGENT\_BUILD\_SPEC.md (stage-level build contracts for the coding agent)*

**Document map:** Part 1 PRD (what and why) · Part 2 TRD (how, technically) · Part 3 UI/UX design · Part 4 System architecture and design.

**Conventions:** Priorities use MoSCoW (M = must, S = should, C = could, W = won't now). Requirement IDs (FR-x.y, NFR-x, TR-x, UX-x) are stable and traceable across parts. Items marked (verify) rest on secondary sources and must be confirmed against primary documentation before customer-facing use. 'Verlytic' is the product name; complete formal trademark and domain clearance before launch.

---

# PART 1: PRODUCT REQUIREMENTS DOCUMENT (PRD)

## 1.1 Summary

Verlytic is a content operations platform for teams that already publish a lot. It connects to Google Search Console, Google Analytics and the CMS, finds which existing pages are decaying and why, ranks what to update or publish next with visible evidence, prepares changes with every claim sourced and checked, requires named human approval, publishes to the CMS, and measures results against matched untouched pages. It optimises each page for three surfaces: classic search results (SEO), extracted answers such as featured snippets and People Also Ask (AEO), and citations inside AI answer engines (GEO).

**Positioning:** Verified, human-approved, measurable content. Hands-off mechanics, human-approved content.

**Strategy:** the update loop ships first. It works on content a human already published, carries the least scaled-content risk, and reuses every building block needed later for new-article generation.

## 1.2 Problem statement

| # | Problem | Evidence base |
| --- | --- | --- |
| P1 | Existing content loses traffic quietly; teams add new posts instead of fixing old ones, and cannot tell which pages to fix first | Decay-workflow literature; matched-control analysis of about 103,000 refreshed pages found refreshed pages beat similar untouched pages by about 19 percentage points on average, with wide variance |
| P2 | Keyword tools return lists, not decisions | Product gap noted in competitor reviews |
| P3 | AI writers publish unchecked statistics, old prices and invented sources | Google's 1 Oct 2026 AI-content guidance, as reported, calls manual fact-checking before publishing critical (verify) |
| P4 | Nobody knows whether answer boxes or AI engines cite them; the data is noisy | Studies show AI citations are volatile and engines disagree on sources |
| P5 | Autopilot tools risk scaled-content penalties | Google's spam policy targets mass-produced low-value pages; an August 2026 update was reported to target them |
| P6 | Evidence of what worked is anecdotal | Most published case studies are self-selected successes |

## 1.3 Vision and principles

**Vision:** the system an editor trusts to tell them the next twelve useful things to do to their content, with proof, and to show afterwards whether it worked.

**Product principles**

1. **Evidence over opinion.** Every recommendation shows the data behind it. No evidence, no listing.
2. **Humans decide.** Automation prepares; a named person approves.
3. **Diagnose before prescribing.** Not every traffic drop needs a rewrite; 'leave it alone' is a valid answer.
4. **Measure honestly.** Ranges, intervals and matched controls; never promised rankings or citations.
5. **Three surfaces, one foundation.** SEO underpins AEO and GEO.
6. **Reversible by default.** Every change can be rolled back.

## 1.4 Target users and personas

| Persona | Role | Goals | Pain | Key needs |
| --- | --- | --- | --- | --- |
| **Maya**, Content and SEO lead | In-house at a B2B SaaS company with 80 to 400 articles | Protect and grow organic traffic with a small team | Cannot see which pages are decaying; distrusts AI drafts | Prioritised update list, explained reasons, safe workflow, proof of results |
| **Omar**, Agency owner | Runs SEO and content for 5 to 30 clients | Deliver measurable results at lower cost; report to clients | Reporting is manual; quality control is hard | Multi-site workspace, client-ready reports, approval trail, white-label later |
| **Lena**, Subject-matter reviewer | Expert or editor who approves content | Publish only accurate content in little time | Reviewing AI text is slow and risky | Claim-by-claim evidence, forced checklist, clear diff, named attribution |
| **Admin** | Owner of the account | Control access, budgets, compliance | Unclear costs and permissions | Roles, budgets, audit log, disclosure settings |

Primary buyer for the first release: Maya and Omar. Solo bloggers are out of scope for now (price-sensitive, low retention).

## 1.5 Jobs to be done

1. When traffic dips, help me see which pages are really decaying, why, and what to do first.
2. When I plan content, tell me what to publish next and prove why.
3. When a draft or update is ready, show me exactly which claims are supported, so I can approve with confidence.
4. When content is live, tell me whether it worked, honestly.
5. When AI answers matter, show me where I am cited, with a sense of how reliable that number is.

## 1.6 Goals and non-goals

**Goals (first 12 months)**

- G1. Deliver an update loop that diagnoses decay with stated confidence and prepares evidence-backed change sets.
- G2. Provide an Opportunity Feed where every item shows stored evidence.
- G3. Achieve a measurable approval workflow: every published change carries a named attestation.
- G4. Provide AI-visibility measurement with intervals across four engines plus a data-provider tier.
- G5. Prove value per client with matched-control comparisons.

**Non-goals**

- Guaranteeing rankings, AI citations or traffic.
- Fully unattended publishing as a default or as a marketing promise.
- A full SEO suite (backlink index, enterprise crawlers); data is bought from providers.
- Social media scheduling, email marketing, or a general-purpose CMS.
- Scraping consumer chat interfaces, fake accounts, or automated community posting.
- Solo-blogger autopilot pricing tiers.

## 1.7 Success metrics

Targets below are hypotheses to validate in the beta; set final numbers after the first baseline.

| Tier | Metric | Definition | Initial hypothesis |
| --- | --- | --- | --- |
| North star | **Verified wins per active site per quarter** | Published, approved updates or articles whose matched-control comparison at 90 days is positive beyond the noise floor | Track baseline in beta; aim for a majority of updated pages positive |
| Activation | Time to first insight | Minutes from connecting Search Console to seeing a ranked decay and opportunity list | Under 30 minutes of wall-clock for a 100-page site |
| Quality | Unsupported-claim rate at publish | Share of published claims without a supporting source, measured by audit samples | Trend toward near zero; report measured value |
| Quality | Verifier precision and recall | On the labelled golden claim set | Set target after first measurement |
| Efficiency | Reviewer time per update | Median minutes from review open to approve | Falls over time |
| Efficiency | Reviewer edit distance | Share of generated text changed by reviewers | Falls over time |
| Trust | Reviewer disagreement rate | Second reviewer disagrees with the first on the audit sample | Low and falling |
| Outcome | Refresh win rate | Updated pages beating matched controls at 28 and 90 days | Reported with intervals |
| Retention | Weekly active reviewers | Reviewers acting on tasks | Stable or growing |
| Cost | Cost per approved update | External API and model cost per published update | Tracked in the cost ledger |

## 1.8 Release plan

| Release | Milestones (see Part 2) | Theme | Exit criteria |
| --- | --- | --- | --- |
| **R1: Diagnose and Update** | M0 to M5 | Connect, inventory, decay diagnosis, audit, verification, review, evidence-backed updates | 10 real updates published with zero unreviewed changes; diagnosis precision measured on 30 labelled pages |
| **R2: Studio and Publish** | M6 to M8 | Article Studio, CMS publish, new-article pipeline | 20 posts published with no unnoticed rendering defects |
| **R3: AI Visibility** | M9 to M10 | Citation panel, snippet tracking, experiments, off-site plans | Citation rates with intervals per engine; at least 5 documented experiments |
| **R4: Enterprise** | M11 to M12 | Compliance settings, RBAC, Postgres, queue, observability | Staging deploy from CI; tenant-isolation tests pass |
| **Beta** | M13 | 3 to 5 design partners, 60 to 90 days | Published matched-control results |

## 1.9 Functional requirements

### E1. Onboarding and integrations

| ID | Requirement | Pri | Acceptance criteria |
| --- | --- | --- | --- |
| FR-1.1 | Connect Search Console with read-only OAuth and let the user choose a property | M | Property list shown; token stored encrypted; revoked token marks integration needs-reauth |
| FR-1.2 | Connect GA4 with read-only OAuth | M | Property selectable; test query succeeds |
| FR-1.3 | Connect a CMS (WordPress first) with a test read call | M | Connection test shows site name; write permission requested only at publish time |
| FR-1.4 | Collect brand kit, authors, bot policy, publish mode, disclosure settings | M | Saved per site; versioned |
| FR-1.5 | Backfill Search Console history and guide BigQuery export setup | S | Maximum available history stored in own tables |
| FR-1.6 | Explain missing permissions in plain language | M | Error names the missing scope and how to grant it |

### E2. Site understanding and inventory

| ID | Requirement | Pri | Acceptance criteria |
| --- | --- | --- | --- |
| FR-2.1 | Draft a business profile from the site; require user confirmation | M | No scoring runs before confirmation |
| FR-2.2 | Crawl respecting robots.txt and rate limits; store per-page technical and content data | M | Orphans, redirects, noindex, JS-only pages identified on a fixture site |
| FR-2.3 | Convert blog-like pages to a structured article model, keeping raw HTML | M | Round-trip renders without content loss on fixtures |
| FR-2.4 | Discover and classify competitors (business versus search competitors); user confirms | S | Classification evidence shown |
| FR-2.5 | Show a content-gap view from competitor rankings and unanswered questions | S | Each gap links to its source data |

### E3. Decay detection and diagnosis

| ID | Requirement | Pri | Acceptance criteria |
| --- | --- | --- | --- |
| FR-3.1 | Detect decay using 28-day versus prior 28-day windows, validated with year-over-year 90-day windows | M | Seasonal fixture is not flagged |
| FR-3.2 | Apply minimum baseline and sustained-decline filters; rank by absolute clicks lost | M | Config-driven thresholds |
| FR-3.3 | Classify each decaying page: ranking decay, CTR decay, demand decay, query drift, seasonality, technical, sitewide, cannibalisation, AI-citation loss | M | Each signature has a test; diagnosis includes confidence and evidence |
| FR-3.4 | Maintain data-quality breakpoints (for example the September 2025 impressions break); mark impressions and position comparisons across a break as not comparable | M | Break-coincident drops are not alerted without clicks confirmation |
| FR-3.5 | Allow 'leave alone' as a recommendation | M | Demand-decay fixture produces leave-alone |

### E4. Page audit

| ID | Requirement | Pri | Acceptance criteria |
| --- | --- | --- | --- |
| FR-4.1 | Check dates (visible, structured data, sitemap) | M | Mismatches reported |
| FR-4.2 | Re-verify time-sensitive claims and flag outdated statistics with proposed sourced replacements | M | Uses the 'outdated' verdict |
| FR-4.3 | Check links (status, soft 404, redirect chains) and propose replacements | M | Weekly monitor |
| FR-4.4 | Detect outdated screenshots by recapture and visual comparison | S | Threshold in config |
| FR-4.5 | Find unanswered questions, weak titles, missing schema, cannibalisation, thin content (by information gain), missing sources | M | Each finding has evidence, severity, effort |
| FR-4.6 | Detect product and price changes from official sources; require human confirmation of any price change | S | Observations stored with an as-of date |
| FR-4.7 | Compare against current competitor pages | S | New entities and subtopics listed |

### E5. Opportunity Feed ('What should I publish?')

| ID | Requirement | Pri | Acceptance criteria |
| --- | --- | --- | --- |
| FR-5.1 | Rank new, update and consolidate opportunities from templates (best-of, cost, versus, worth-it, alternatives, how-to, what-is) | M | Templates configurable per site |
| FR-5.2 | Show a 0 to 100 rank within the site (not a prediction) and an impact range with confidence | M | Components visible |
| FR-5.3 | Render 'Why this opportunity?' from stored evidence only; hide items with no evidence | M | Property test: every displayed line maps to an evidence row |
| FR-5.4 | Accept, snooze, reject with reason; learn from reasons | S | Reasons stored |
| FR-5.5 | Choose the best update set within a reviewer-hours budget | M | Budget input respected |
| FR-5.6 | Warn and require verification for comparison and pricing topics | M | Human approver required |

### E6. Update Agent

| ID | Requirement | Pri | Acceptance criteria |
| --- | --- | --- | --- |
| FR-6.1 | Generate an Update Report: last updated, diagnosis, problems, opportunities, AI visibility, recommendation, change count, effort, impact range | M | Every figure derives from stored findings |
| FR-6.2 | On 'Update Article', produce a change set of discrete, individually reviewable changes | M | Each change has before, after, sources, reason |
| FR-6.3 | Protect passages that map to ranking queries and keep the URL, anchors and title unless justified | M | Unjustified deletion blocked |
| FR-6.4 | Verify every added or changed claim | M | No unverified change reaches review |
| FR-6.5 | Apply date rules: change visible date and dateModified only for significant updates, keeping page, structured data and sitemap consistent | M | Date-only refresh blocked |
| FR-6.6 | Publish as a revision with rollback | M | Rollback restores prior version |
| FR-6.7 | Support consolidate and redirect flows with human approval; prune only with explicit approval | S | 301 map generated |

### E7. New-article pipeline

| ID | Requirement | Pri | Acceptance criteria |
| --- | --- | --- | --- |
| FR-7.1 | Build a SERP-based brief with gaps, entities, questions, target answer surfaces and fan-out coverage | M | Brief schema valid; competitor text not reproduced |
| FR-7.2 | Require an evidence pack with original input before drafting | M | Drafting blocked without it unless waived for no-new-claim refreshes |
| FR-7.3 | Draft section by section in the site's style, using only evidence-pack facts | M | Unsupported-fact lint passes |
| FR-7.4 | Cap critique loops and escalate to a human when exceeded | M | Loop count enforced |

### E8. Verification

| ID | Requirement | Pri | Acceptance criteria |
| --- | --- | --- | --- |
| FR-8.1 | Extract atomic, self-contained claims, including from titles, metadata, captions and alt text | M | Golden set coverage |
| FR-8.2 | Retrieve evidence independently of the draft; at least two sources where possible | M | Source tiers respected |
| FR-8.3 | Check numbers, dates, names and units deterministically before any model verdict | M | Mismatch caught in code |
| FR-8.4 | Return supported, contradicted, unsubstantiated or outdated with a cited span; reject verdicts without a span | M | Validation test |
| FR-8.5 | Enforce policy: remove or rewrite unsupported stats; escalate contradictions; require named experts for regulated claims | M | Policy tests |
| FR-8.6 | Produce an immutable verification report | M | Append-only |
| FR-8.7 | Re-verify after any later text change | M | Gate fails if a changed span lacks a fresh verdict |

### E9. SEO, AEO and GEO optimisation

| ID | Requirement | Pri | Acceptance criteria |
| --- | --- | --- | --- |
| FR-9.1 | Check titles, metas, headings, byline, dates, sources and readability with configurable lint | M | Lint results listed |
| FR-9.2 | Build answer blocks that match the SERP's current snippet format, only where the page already ranks near the top 10 | S | Eligibility gate visible |
| FR-9.3 | Offer visible FAQs from People Also Ask and panel prompts; markup optional | S | Markup off by default |
| FR-9.4 | Audit AI-crawler access by bot and rule, weekly, and alert on regressions | M | Per-bot verdict with matched rule |
| FR-9.5 | Show a transparent citation-readiness checklist, never a predictor | S | Labelled as a checklist |
| FR-9.6 | Propose internal links in and out with descriptive anchors | M | Human accept or reject |
| FR-9.7 | Generate structured data from typed builders and validate against visible content | M | Invalid schema blocks publish |

### E10. Article Studio

| ID | Requirement | Pri | Acceptance criteria |
| --- | --- | --- | --- |
| FR-10.1 | Maintain one article model rendered to HTML, Markdown and CMS formats | M | Same verified text across renderers |
| FR-10.2 | Choose components by blueprint and justify each visual | M | Justification stored |
| FR-10.3 | Render tables as real HTML tables with captions and sources | M | No table images |
| FR-10.4 | Render diagrams from validated Mermaid, D2 or Graphviz to accessible SVG | S | axe checks pass |
| FR-10.5 | Draw charts only from sourced data and attach an accessible data table | M | Unsourced data rejected |
| FR-10.6 | Capture real screenshots with redaction for software steps | S | PII redaction test |
| FR-10.7 | Generate optional AI images with provenance, disclosure and no unverified in-image text | C | Original retained; IPTC set |
| FR-10.8 | Produce deterministic social cards | S | 1200x630 |
| FR-10.9 | Run render gates: accessibility, performance, links, layout at three viewports | M | Any failure blocks |

### E11. Review and approval

| ID | Requirement | Pri | Acceptance criteria |
| --- | --- | --- | --- |
| FR-11.1 | Provide a review screen with preview, diff, claim and evidence panel, metadata panel, schema preview, visual QA | M | All present |
| FR-11.2 | Force confirmation of every high-risk claim and every statistic, price and date before Approve enables | M | Button disabled otherwise |
| FR-11.3 | Require named qualified experts for regulated topics | M | Role check |
| FR-11.4 | Support sampled second-reviewer audits and track disagreement | S | Sample rate in config |
| FR-11.5 | Store immutable attestations with document hash and checklist state | M | Append-only |
| FR-11.6 | Optional public 'reviewed by' byline and disclosure label | S | Per-site setting |

### E12. Publishing

| ID | Requirement | Pri | Acceptance criteria |
| --- | --- | --- | --- |
| FR-12.1 | Mode 1 (default): automated publishing after approval | M | No publish without attestation |
| FR-12.2 | Mode 2: low-risk refresh autopilot, opt-in | C | Conditions enforced |
| FR-12.3 | Mode 3: unattended new articles, off by default and not marketed | W | Not built in R1 to R3 |
| FR-12.4 | Stage as draft, upload media, set metadata, preview, publish, then verify the live page against the intended document | M | Mismatch triggers rollback or task |
| FR-12.5 | Velocity caps, per-site pause, and automatic pause on anomalies | M | Triggers configurable |
| FR-12.6 | WordPress adapter first; Webflow, Shopify, Ghost and Git-based later | M/S | Adapter contract tests |

### E13. Measurement and AI visibility

| ID | Requirement | Pri | Acceptance criteria |
| --- | --- | --- | --- |
| FR-13.1 | Sync Search Console and GA4 nightly into own history tables | M | Gaps alerted |
| FR-13.2 | Import the Search Console Generative AI report (API if available, else CSV) | S | Stored separately (verify) |
| FR-13.3 | Track rankings, snippet owner, People Also Ask and AI Overview sources weekly | S | History retained |
| FR-13.4 | Run an AI-citation panel across four engines using intent clusters, paraphrases and reruns | S | Rates reported with intervals only |
| FR-13.5 | Add data-provider tier and calibrate against the own panel | S | Agreement reported |
| FR-13.6 | Track AI referrals in GA4 and AI crawler hits in logs | C | Config-driven lists |
| FR-13.7 | Weekly technical audit including Core Web Vitals | S | Prioritised fix list |
| FR-13.8 | Per-article scorecard | M | All listed fields |

### E14. Experiments and learning

| ID | Requirement | Pri | Acceptance criteria |
| --- | --- | --- | --- |
| FR-14.1 | Tag every update with change types and hold out matched controls where possible | M | Matching documented |
| FR-14.2 | Compare at 7, 28 and 90 days using difference-in-differences with intervals; say 'inconclusive' when samples are small | M | Minimum pairs enforced |
| FR-14.3 | Propose reverts when results fall beyond the noise floor | S | Human decision |
| FR-14.4 | Re-fit recoverability and click-through models from outcomes; learnings are proposals a human approves | S | Approval step |
| FR-14.5 | Earned-presence plans for off-site sources; humans publish | C | No automated posting |

### E15. Administration, billing and security

| ID | Requirement | Pri | Acceptance criteria |
| --- | --- | --- | --- |
| FR-15.1 | Roles: Admin, Editor, Reviewer, Viewer, scoped per site | M | Authorisation tests |
| FR-15.2 | Budgets per tenant and per run with hard stop and alert | M | Cost ledger |
| FR-15.3 | Audit log of state changes | M | Append-only |
| FR-15.4 | Data export and deletion per tenant | S | Documented SLA |
| FR-15.5 | Disclosure and compliance settings per site | S | Applied at render |
| FR-15.6 | Billing and plans | S | After beta |

## 1.10 Product-level non-functional requirements

| ID | Requirement |
| --- | --- |
| NFR-1 Trust | No fabricated data, quotes, sources, screenshots or testimonials anywhere in the product or its marketing |
| NFR-2 Accuracy | Verifier accuracy is measured on a labelled set and reported; no accuracy claim is made without a measurement |
| NFR-3 Performance | Inventory of a 500-page site in under 2 hours; review screen interactive in under 3 seconds on a typical laptop (targets to validate) |
| NFR-4 Availability | Review and publish paths target 99.5% monthly in the enterprise release (validate) |
| NFR-5 Accessibility | Product UI and generated articles meet WCAG 2.2 AA targets |
| NFR-6 Privacy | Customer data is isolated per tenant, encrypted at rest and in transit, exportable and deletable |
| NFR-7 Compliance | Disclosure settings and attestations support EU AI Act transparency obligations; counsel reviews terms (verify) |
| NFR-8 Reversibility | Every publish and update is reversible |
| NFR-9 Cost transparency | Users see usage and cost per run |

## 1.11 Packaging and pricing hypotheses

Validate with design partners; do not publish prices before testing.

| Path | Hypothesis | Notes |
| --- | --- | --- |
| Managed service first | Monthly retainer for update and review work with Verlytic as the core tool | Funds development; teaches what to productise; agency retainers are the right reference class |
| Self-serve tiers | By number of sites, pages under management and reviewed updates per month | Compare with current competitor prices before setting (verify) |
| Agency plan | Multi-client workspace and client reports; white-label later | After stable multi-tenancy |

## 1.12 Go-to-market and beta

- Offer a free content health audit: connect Search Console, receive a ranked decay report.
- Recruit 3 to 5 design partners with at least 50 articles and Search Console history; run 60 to 90 days with matched controls.
- Publish a methodology page and measured before-and-after results with intervals.
- Messaging pillars: diagnose, don't guess; verified, not vibes; proven, not promised.

## 1.13 Assumptions, dependencies, constraints

- Customers can grant Search Console and GA4 read access and have at least 50 articles with history.
- Google, data-provider and model-provider APIs remain available; quotas and prices change (verify at build).
- A qualified human reviewer exists on the customer side.
- Constraint: no guarantees about rankings or citations; counsel reviews terms, comparative-claim topics and the EU AI Act position.

## 1.14 Product risks

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| Scaled-content penalties | Medium | High | Evidence pack, velocity caps, human attestation, refresh-first strategy |
| False decay diagnoses | Medium | Medium | Year-over-year validation, breakpoints, leave-alone outcome |
| Verifier mistakes create false confidence | Medium | High | Different stronger model, deterministic checks, forced human confirmation, measured accuracy |
| Noisy AI-citation data misleads users | High | Medium | Intervals, clusters, calibration, plain-language caveats |
| Reviewers rubber-stamp | Medium | High | Forced confirmations, second-reviewer audits, disagreement metric |
| Platform data changes | High | Medium | Breakpoint table, adapter contract tests |
| Over-promising in sales | Medium | High | Claims policy |

## 1.15 Claims policy (marketing and in-product copy)

Never claim: zero hallucinations, guaranteed rankings or citations, fully hands-off content, unlabelled illustrative numbers, fake logos or testimonials, headline lift percentages from other companies' case studies. Always label demo numbers 'Illustrative'.

## 1.16 Open questions

1. Update loop first or new-article generation first? (Recommendation: update loop first.)
2. Which CMS first? (Recommendation: WordPress.)
3. Which niche for design partners?
4. Which vendors or categories need price monitoring, and with what permission or official source?
5. Markets and languages in scope (affects EU disclosure and locale handling)?
6. Is Verlytic a provider under the EU AI Act when sold as a product? (counsel)

---

# PART 2: TECHNICAL REQUIREMENTS DOCUMENT (TRD)

## 2.1 Purpose and scope

This part defines how Verlytic is built: stack, modules, integrations, data, APIs, algorithms, non-functional targets, security, testing and delivery. It implements the PRD (Part 1) and is implemented by the stage contracts in AGENT\_BUILD\_SPEC.md (stages S1 to S24, gates G1 to G8, milestones M0 to M13). Where this part states a numeric target it is a hypothesis to validate unless a source is given.

## 2.2 Technical principles

| ID | Principle | Consequence |
| --- | --- | --- |
| TP-1 | Never fabricate data, sources, quotes, prices or metrics | Every generated factual statement links to a stored evidence row; fixtures are labelled synthetic |
| TP-2 | Nothing hardcoded | Thresholds, weights, prompts, model names, bot lists, source tiers and templates live in versioned config or the database |
| TP-3 | Deterministic code decides; models assist | Diagnoses, policy outcomes and gates are rules over data; models extract, draft, phrase and critique within schemas |
| TP-4 | Typed contracts | Stages exchange Pydantic models, validated at every boundary |
| TP-5 | Idempotent and reversible | Every job carries an idempotency key; every publish and update has a rollback path |
| TP-6 | Append-only evidence | Approvals, verification reports, panel records, price observations and audit entries are never edited |
| TP-7 | Untrusted text stays data | Web and uploaded text is wrapped, stripped of instructions, and never reaches nodes holding credentials |
| TP-8 | Measure with uncertainty | Rates and effects carry intervals; causal claims need matched controls |
| TP-9 | Reuse before rewrite | Existing repository code is adapted to the stage contracts, not duplicated |

## 2.3 Technology stack

| Layer | Choice (default) | Notes |
| --- | --- | --- |
| Language and runtime | Python 3.12 | Workers, API, stages |
| API | FastAPI, Pydantic v2 | OpenAPI generated; versioned /v1 |
| Orchestration | LangGraph with persistent checkpointer | AsyncPostgresSaver in production; interrupt() for human review |
| Database | SQLAlchemy 2, Alembic; SQLite for local, Postgres for production; pgvector | Repository layer enforces tenant filter |
| Queue and cache | Redis with ARQ or Celery | Rate limiters, API cache, job queue |
| Object storage | S3-compatible with CDN | Media, snapshots, originals, exports |
| Crawling and extraction | httpx, tenacity, selectolax, trafilatura | Robots-aware, per-host rate limits |
| Rendering and QA | Playwright (Chromium), axe-core, Lighthouse CI | Sandboxed workers |
| Diagrams and charts | mermaid-cli, D2, Graphviz; Vega-Lite or Plotly | Pinned versions in the image |
| Images | Pillow or pyvips, svgo | AVIF and WebP variants |
| NLP | spaCy or LLM entity extraction; embeddings via provider or sentence-transformers | Embedding model and dimension in config |
| Statistics | numpy, scipy, scikit-learn, statsmodels | Bootstrap, Wilson intervals, matching, DiD |
| Model access | One router interface (LiteLLM or the existing llm\_client) | Roles, fallbacks, budgets, ledger |
| Web app | React or Next.js, TypeScript, Tailwind | Accessible component library |
| Auth | OIDC provider (Auth0, Clerk or Keycloak) | Roles scoped per site |
| Observability | OpenTelemetry, structured logs, Sentry, Langfuse or LangSmith | Run-level traces |
| Quality | pytest, pytest-recording, ruff, mypy | CI gates |

## 2.4 Traceability: PRD to modules to milestones

| PRD epic | Primary modules | Stages | Milestone |
| --- | --- | --- | --- |
| E1 Onboarding | integrations, onboarding service | S1 | M1 |
| E2 Inventory | crawler, document-model converter, business-profile extractor | S2, S3, S4, S5 | M1 |
| E3 Decay | metrics store, breakpoints, decay engine | S8 | M2 |
| E4 Audit | audit engine, link and price monitors | S9 | M2 |
| E5 Feed | opportunity engine, CTR model, clustering | S6, S7, S10 | M4 |
| E6 Update Agent | change-set writer, diff service, publisher | S13, S22, S24 | M5 |
| E7 New article | brief builder, evidence service, writer | S11, S12, S13 | M8 |
| E8 Verification | claim, evidence, verdict, policy engine | S14 | M3 |
| E9 SEO/AEO/GEO | lint, answer-block builder, robots auditor, schema builders, link engine | S15 to S18 | M6 |
| E10 Studio | document model, renderers, visual engine, QA gates | S19, S20 | M6 |
| E11 Review | review service and UI, attestation store | S21 | M3 |
| E12 Publish | CMS adapters, post-publish verifier | S22 | M7 |
| E13 Measure | sync jobs, panel, SERP tracker, technical audit | S23 | M9 |
| E14 Experiments | matching, DiD, outcome store | S24 | M10 |
| E15 Admin | RBAC, budgets, audit log | cross-cutting | M11, M12 |

## 2.5 Module designs

### 2.5.1 Integrations layer

Every external call goes through an integration client that applies timeouts, retry with exponential backoff, per-provider rate limiting, optional caching, structured logging and a cost-ledger write. Clients expose typed methods and a recorded-fixture test double. No business logic lives in clients.

### 2.5.2 Metrics store and breakpoints

- page\_metrics\_daily is partitioned by month and keyed by (site\_id, page\_id, date). Query-level data goes to a separate table with a retention policy. Own history is the source of truth because Search Console retains about 16 months.
- metric\_breakpoints holds (date, affected\_metrics, scope, note, source). Comparison helpers refuse to compare impressions or position across a breakpoint and return a not-comparable flag that the UI renders as an annotation.

### 2.5.3 Crawler and inventory

Seeds from sitemaps, Search Console pages and internal links. Per-host politeness, robots checks, content-type sniffing, JS-render fallback with Playwright when allowed. Output is pages, page\_versions (raw HTML reference plus document JSON plus hash), links, images and query mappings. HTML-to-document conversion uses deterministic rules first and an LLM classifier only for ambiguous blocks; the converter must round-trip fixtures without content loss.

### 2.5.4 Decay engine

Pure functions over metrics: windows, filters, signature rules, confidence scoring. Output is a diagnosis with evidence rows. A model may write an explanation but never chooses the diagnosis. Ambiguous cases produce needs\_serp\_check and trigger a live SERP fetch.

### 2.5.5 Audit engine

A registry of checks, each a function (page, context) returning findings with severity, effort points and auto-fix flag. Checks are independently schedulable and cacheable. Price monitoring prefers official APIs or pricing pages, parses deterministically, and stores observations with an as-of date.

### 2.5.6 Opportunity engine

Candidate generators per source, enrichment, SERP-overlap clustering on the shortlist, scoring, impact range from CTR-model uncertainty, and an evidence builder that writes plan\_evidence rows. The UI explanation is a template over those rows; the model may only rephrase.

### 2.5.7 Research and evidence service

Search provider abstraction (Tavily, Exa, Brave), source-tier classifier, excerpt extractor limited to the configured word count, and a passage hash for later comparison. Full page text is not stored.

### 2.5.8 Writer

Section-by-section generation with structured output, style-profile injection, and a capped critique loop. Update runs call the change-set writer, which receives protected-passage constraints. All text ends up in the document model, which records diffs.

### 2.5.9 Verification engine

Sub-graph: extract claims (selection, disambiguation, decomposition, decontextualisation); retrieve evidence independently; deterministic number, date, unit and name matching; model verdict with required span; policy engine; report writer. Verdicts without spans fail validation. A diff-aware re-verifier runs whenever text changes.

### 2.5.10 Studio

- Document model: typed blocks with claims, sources and figure metadata.
- Renderers: semantic HTML, Markdown or MDX, WordPress blocks, and CMS field mappers.
- Visual engine: planner proposes visuals with a justification; pipelines for tables, diagrams, charts, screenshots, social cards and optional AI images; deterministic checks plus vision-model critique.
- Gates: accessibility (axe), performance (Lighthouse), links, schema, layout at three viewports.

### 2.5.11 Link and schema services

Internal links by embedding match with descriptive anchors; external links bound to evidence URLs; typed JSON-LD builders validated against visible content and re-validated on the live URL.

### 2.5.12 Review service

Builds the review bundle (preview, diff, claim and evidence panel, metadata, schema, visual QA), enforces forced confirmations server-side, records attestations (reviewer, role, time, document hash, checklist state), supports sampled second-reviewer audits and computes disagreement rates.

### 2.5.13 Publisher and CMS adapters

Adapter interface: connect\_test, upload\_media, create\_draft, update, schedule, publish, unpublish, fetch\_live, map\_metadata. Idempotency by dedupe key. Post-publish verifier diffs live DOM against the intended document and validates JSON-LD, canonical and indexability.

### 2.5.14 Panel and SERP tracking

One adapter per engine normalises to PanelRecord. Scheduler fans out paraphrase by engine by rerun. Statistics module computes Wilson and cluster-bootstrap intervals, noise floors and change flags. SERP tracker stores snippet owner, People Also Ask presence and AI Overview sources per tracked keyword.

### 2.5.15 Experiments

Matching on baseline clicks, page type, age and position band; difference-in-differences on log(clicks+1) with bootstrap intervals; minimum pair counts; outcome store; recoverability re-fit with shrinkage toward the config prior.

### 2.5.16 Model router

Roles (writer, critic, verifier, vision QA, embeddings, image), fallbacks, timeouts, budgets and cost-ledger writes. The verifier role must differ from the writer role; the router rejects configurations where they are the same.

### 2.5.17 Config service

Layered config (defaults, tenant, site) with versioning; runs record the config version they used; schema-validated on save.

## 2.6 Integration specifications

| System | Use | Key facts and constraints |
| --- | --- | --- |
| Google Search Console API | Search analytics, sitemaps, URL inspection | Read-only scope (webmasters.readonly); up to 25,000 rows per request with startRow pagination; daily row cap per site per search type; about 2 to 3 days lag; about 16 months retention; rare queries anonymised; URL Inspection about 2,000 per day per property and 600 per minute; BigQuery bulk export available |
| Search Console Generative AI report | AI Overview and AI Mode impressions | Announced June 2026, all sites from 31 August 2026; impressions only, reportedly no queries or clicks, features combined; whether the API exposes it is a spike (verify) |
| GA4 Data API | Sessions, key events, channels | Read-only scope (analytics.readonly); custom channel group for AI referrers |
| DataForSEO | Keywords, SERP, competitors, difficulty, intent, AI data | Labs endpoints: keyword\_suggestions, related\_keywords, keyword\_ideas, keywords\_for\_site, ranked\_keywords, competitors\_domain, domain\_intersection, bulk\_keyword\_difficulty, search\_intent; SERP google/organic/live/advanced; AI Optimization: LLM Responses, LLM Scraper, LLM Mentions, AI Keyword Data; Labs is live-mode with a documented per-minute call limit; prices and coverage to confirm in sandbox |
| Tavily or similar | Evidence search | Provider abstraction; rate limit and cost tracked |
| OpenAI Responses API | Panel and models | web\_search tool; url\_citation annotations on output text |
| Perplexity Sonar API | Panel | Citations and search results arrays |
| Gemini API | Panel and models | Grounding with Google Search; groundingChunks carry redirect URIs that must be resolved to publisher URLs |
| Anthropic Messages API | Panel and models | Web search tool; search-result blocks and text citations |
| WordPress REST | Publishing | /wp/v2/media and /wp/v2/posts; draft and future statuses; SEO-plugin fields via plugin REST support or a companion plugin |
| Webflow Data API v2, Shopify Admin API, Ghost Admin API | Publishing | Later adapters; verify current versions |
| Git (headless) | Publishing | Pull request with Markdown or MDX plus images |
| PageSpeed Insights and CrUX APIs | Performance | Field data first; lab data diagnostic; thresholds LCP 2.5 s, INP 200 ms, CLS 0.1 at p75 (verify unchanged) |
| IndexNow | Notification | Benefits Bing and participating engines, not Google |

All of the above are verified at build time against primary documentation; recorded fixtures guard against drift.

## 2.7 Data design

The logical model (tables by group) is in AGENT\_BUILD\_SPEC section 7. Technical rules:

- IDs are ULIDs; all times are UTC with timezone; money is integer micro-units plus currency.
- Every table has tenant\_id; site-scoped tables have site\_id. Repositories inject the filter; there is no raw query path without it.
- Large text, HTML and images live in object storage; tables hold references and hashes.
- Embeddings live in pgvector columns; model name and dimension are recorded per row to allow re-embedding.
- Append-only tables: approvals, verification\_reports, audit\_log, price\_observations, panel\_runs, panel\_records, cost\_ledger.
- Retention: raw HTML snapshots and screenshots by policy; query-level metrics trimmed by policy; deletion and export per tenant.
- Indexing: composite indexes on (tenant\_id, site\_id, date) for metrics; GIN or trigram only where search is needed; vector indexes (HNSW or IVFFlat) for similarity.

## 2.8 API design

- REST, versioned under /v1, OpenAPI generated from Pydantic schemas.
- Auth by OIDC bearer tokens; authorisation by role and site scope on every route; audit\_log entry on every state change.
- Pagination with cursors; filtering and sorting parameters whitelisted.
- Errors as RFC 7807 problem documents with a stable error code and a human-readable fix.
- Idempotency-Key header on POST routes that start runs or publish.
- Long operations return a run id; clients poll or subscribe to webhooks (run.needs\_human, run.approved, publication.created, finding.created, decay.detected). Webhooks are signed and retried with backoff.
- Rate limits per tenant with standard headers.
- Route inventory: AGENT\_BUILD\_SPEC section 9.

## 2.9 Algorithm specifications (summary)

| Algorithm | Specification |
| --- | --- |
| CTR model | CTR(position, has\_aio, has\_snippet) fitted from site GSC joined to dated SERP snapshots, with a hierarchical public prior until the configured minimum sample; never a single hardcoded AIO figure |
| Empirical reach | Median and 75th percentile keyword difficulty of keywords where the site ranks 1 to 10; recomputed monthly |
| Opportunity | expected\_clicks times business\_fit times feasibility times recency; display score is the percentile rank within the site's candidates |
| Clustering | SERP-overlap: keywords sharing at least N top-10 URLs join one cluster; N in config |
| Decay detection | 28 versus prior 28 days, validated by 90-day year-over-year; minimum baseline clicks; sustained weeks; ranked by absolute clicks lost; breakpoint-aware |
| Priority | (recoverable clicks times value per click plus citation-gap value plus risk reduction) divided by effort; best set within a reviewer-hours budget |
| Panel statistics | Wilson interval for single proportions; cluster bootstrap over paraphrases then runs for cluster rates; noise floor from rerun variance; change flagged only when intervals separate for two consecutive cycles |
| Update effect | Nearest-neighbour matching; difference-in-differences on log(clicks+1) with bootstrap intervals at 7, 28 and 90 days; minimum pairs enforced |

## 2.10 Non-functional technical requirements

| ID | Requirement | Target (validate) |
| --- | --- | --- |
| TR-1 Performance | Review bundle load | Under 3 s p95 for a 3,000-word article with 40 claims |
| TR-2 Performance | Inventory crawl | 500 pages in under 2 hours at polite rates |
| TR-3 Throughput | Concurrent runs per worker pool | Scales horizontally; no shared in-process state |
| TR-4 Reliability | Job success with retries | At least 99% of retryable failures recover without human action |
| TR-5 Availability | Review and publish paths | 99.5% monthly in the enterprise release |
| TR-6 Durability | Approvals and verification reports | Replicated storage; point-in-time recovery; tested restore |
| TR-7 Security | Secrets and tokens | Encrypted at rest with rotation; never logged |
| TR-8 Privacy | Tenant isolation | Verified by automated isolation tests in CI |
| TR-9 Observability | Traceability | Every stage execution traceable by run\_id with cost and duration |
| TR-10 Cost control | Budgets | Hard stop per tenant and per run; alert at configured thresholds |
| TR-11 Maintainability | Test coverage | Unit and contract tests for every module; golden sets in CI subset |
| TR-12 Accessibility | Generated articles and product UI | WCAG 2.2 AA targets; axe gate on every article |
| TR-13 Portability | Cloud independence | Containerised; S3-compatible storage; no proprietary orchestration lock-in |

## 2.11 Security design summary

- Prompt injection: delimiters, stripped scripts and hidden text, instruction-ignoring system rules, schema-validated outputs, no credentials or publish tools on research and verification nodes.
- SSRF: URL allow-check blocking private, loopback, link-local and metadata addresses and non-HTTP schemes; redirects re-checked.
- Secrets: per-tenant OAuth and CMS tokens encrypted (KMS or Fernet), rotated; never in prompts, state or logs.
- Output sanitisation before CMS publish.
- Copyright: URLs and short excerpts only; similarity checks on drafts.
- Privacy: consent-based OAuth, retention policy, export and delete, DPA template.
- Supply chain: pinned dependencies and lockfile, Dependabot, pip-audit, secret and image scanning.
- Full threat model: Part 4.

## 2.12 Testing strategy

| Layer | Scope | Rule |
| --- | --- | --- |
| Unit | Scoring, decay rules, policy engine, linters, formulas | No network |
| Contract | Each external adapter against recorded fixtures | Recordings refreshed on a schedule; failures flag API drift |
| Golden | About 200 labelled claims; 30 diagnosed pages; 50 briefs; 30 prompts per engine with hand-checked citation parsing; 20 articles for visual acceptance | Small subset in CI, full set nightly |
| Property | Invariants: every figure has alt and caption; every statistic has a source; every displayed feed line maps to an evidence row | Run on generated fixtures |
| End to end | Fake CMS and mocked providers: onboard, feed, update, review, publish, measure | In CI |
| Security | SSRF blocklist, tenant isolation, injection fixtures | In CI |

Acceptance metrics are measured first and targets set afterwards by ADR; no accuracy number is claimed before it is measured.

## 2.13 CI/CD and environments

Pipeline: ruff, mypy, unit, contract and property tests, eval smoke subset, image build, dependency and secret and image scans, push. Prompt or model changes must run the eval subset and block on regression. Environments: local (SQLite and in-process scheduler behind the same interfaces), staging, production, each with separate keys. Migrations run as a release step; health and readiness endpoints; feature flags for risky capabilities (publish modes 2 and 3, price monitoring, AI images).

## 2.14 Capacity and cost model

Cost per approved update = model tokens (drafting, critique, verification, vision QA) + search and evidence calls + keyword and SERP data calls + rendering and storage + reviewer time (tracked separately). Every term is measured in the cost ledger; do not publish unit costs until measured in the sandbox and beta. Levers: shortlist before SERP calls, cache by endpoint class, bulk endpoints, cheaper models for classification that pass the eval gate, strict budgets per tenant and per run.

## 2.15 Technical risks and spikes

| Risk or unknown | Mitigation or spike |
| --- | --- |
| GSC API may not expose the Generative AI report | Spike in M0; fall back to scheduled CSV import |
| Which engine APIs expose their sub-queries | Spike; skip fan-out mining for engines that do not |
| DataForSEO real costs and limits | Sandbox, then a small paid test |
| API panel versus consumer behaviour | Calibrate on 30 prompts against the scraper tier; report both |
| Possible 2026 Search Console impression correction | Confirm date and scope; add to breakpoints |
| Current AI-crawler user-agent names | Config-driven lists verified in vendor docs |
| EU AI Act provider status | Counsel |
| LLM verifier over-confidence | Deterministic checks first, span requirement, forced human confirmation, measured accuracy |

## 2.16 Initial architecture decision records

| ADR | Decision | Reason |
| --- | --- | --- |
| 0001 | LangGraph with a persistent checkpointer | Durable runs and human interrupts |
| 0002 | Rules decide diagnoses and gates; models assist | Auditability and testability |
| 0003 | One article document model, many renderers | Consistent verification and CMS portability |
| 0004 | Append-only evidence tables | Defensible audit trail |
| 0005 | Update loop before new-article generation | Lowest risk, fastest value |
| 0006 | Panel unit is an intent cluster with intervals | AI citations are volatile |
| 0007 | Repository layer and scheduler interface from day one | Painless move to Postgres and a queue |
| 0008 | Config-driven models, prompts and thresholds | Platform and vendor churn |

---

# PART 3: UI/UX DESIGN DOCUMENT

## 3.1 UX goals and principles

| ID | Principle | What it means on screen |
| --- | --- | --- |
| UX-1 | **Evidence is always one click away** | Every recommendation, score and verdict opens the data behind it |
| UX-2 | **Review is the product** | The review screen gets the most design effort; it must make careful approval faster than careless approval |
| UX-3 | **Honest uncertainty** | Ranges, intervals, as-of dates, confidence labels and not-comparable states are visible, never hidden in tooltips |
| UX-4 | **Decide, don't browse** | Screens lead with a ranked, explained list of next actions, not raw tables |
| UX-5 | **Calm and editorial** | A quiet, data-literate tone; colour carries meaning (verified, decaying, contradicted), not decoration |
| UX-6 | **Nothing surprising** | Nothing publishes, deletes or changes dates without an explicit, named human step |
| UX-7 | **Accessible by default** | WCAG 2.2 AA targets; status never conveyed by colour alone |

## 3.2 Contexts of use

- **Desktop first** for analysis and review (large screens, side-by-side diff and evidence).
- **Mobile** for notifications, read-only status, and lightweight approvals. Forced confirmations are preserved on mobile; high-risk review is encouraged on desktop.
- Reviewers (Lena) are occasional users: the review screen must be self-explanatory without training.

## 3.3 Information architecture

```
Site switcher (top left)  |  Search  |  Notifications  |  Account

Left navigation
  Today              what changed, what to do first, what awaits review
  Opportunities      the ranked feed (new, update, consolidate)
  Pages              inventory, page detail, update report
  Updates & runs     queue of runs, change sets, status
  Review             inbox of items awaiting a named reviewer
  Visibility         Rankings | Answer boxes | AI answers | AI referrals | Crawler access
  Experiments        what we changed and whether it worked
  Calendar           scheduled publishes and update triggers
  Settings           Integrations, Brand and authors, Bot policy, Publish mode,
                     Disclosure, Budgets, Team, Billing
```

Primary navigation has seven daily items; settings and billing are secondary. Multi-site accounts (agencies) switch site from the header; an All sites view lists decay and review counts per site.

## 3.4 Core user flows

### F1. Onboard and reach first insight

1. Sign in, create workspace, name the site.
2. Connect Search Console (read-only), choose a property; connect Analytics.
3. Connect the CMS (read-only test). Skip allowed; publishing later requires write access.
4. Review the drafted business profile: confirm or edit offerings, audiences, regulated topics, never-say list.
5. Add brand kit, authors, bot policy; defaults are safe (search bots allowed, training bots disallowed).
6. Progress screen shows the crawl and sync with plain-language steps and time estimates.
7. Land on Today with the first ranked decay list and opportunities. Target: first insight within 30 minutes for a 100-page site (hypothesis).

### F2. Understand a decaying page and start an update

1. From Today or Pages, open a page flagged by diagnosis.
2. Read the Update Report: diagnosis with confidence, problems, opportunities, AI visibility with range, recommendation, effort, impact range.
3. Inspect evidence behind any line (drawer).
4. Choose Update article, or Leave alone, or Snooze with reason.
5. A run starts; status appears in Updates and runs.

### F3. Review and approve an update

1. Notification: a change set is ready for review.
2. Open the review screen: preview, per-change diff, claims and evidence.
3. Accept or reject each change; edit text inline (edits re-trigger verification of the changed span).
4. Tick every flagged claim; the Approve button enables only when complete.
5. Confirm disclosure choice; Approve and schedule or publish now.
6. A post-publish check result appears; rollback is one action.

### F4. Publish something new

1. In Opportunities, open an item; read Why this opportunity; choose Create.
2. Provide original input (data, quote, example, screenshots) when asked; the run pauses until supplied.
3. Review brief; review draft through F3.

### F5. Check AI visibility

1. Open Visibility, then AI answers.
2. See cluster table: citation rate with range per engine, branded versus unbranded.
3. Open Where am I not cited; see who is cited; choose Create brief.

### F6. Roll back

Open the publication, choose Roll back, confirm; the previous revision is restored and the event is logged.

## 3.5 Screen specifications

### 3.5.1 Today

```
+--------------------------------------------------------------+
| Good morning, Maya.            Site: example.com   Last sync 2h|
+--------------------------------------------------------------+
| Fix these first (12 fit your 6 reviewer hours this month)      |
|  1 Best CRM software for small businesses                      |
|    Ranking decay (medium confidence)   18 changes   [Review]   |
|  2 Invoice template guide      CTR decay    6 changes  [Open]  |
|  ...                                          [See all]        |
+--------------------------------------------------------------+
| Waiting for review (3)       | Alerts (1)                      |
|  Update: Payroll setup, 9    |  Price changed on 2 pages       |
|  changes, from Omar          |  [Confirm prices]               |
+--------------------------------------------------------------+
| What changed this week: clicks, impressions, AI impressions    |
| (annotated where data is not comparable)                       |
+--------------------------------------------------------------+
```

Components: priority list with budget input, review inbox, alert cards, weekly change summary with annotations. Empty state: Connect Search Console to see which pages to fix first.

### 3.5.2 Opportunities (the feed)

- Row anatomy: title, action chip (New, Update, Consolidate), rank within site (0 to 100) with a tooltip that shows components, impact range with confidence label, effort, surface flags (SEO, AEO, GEO).
- Why this opportunity drawer: checklist lines each linked to an evidence row (source, value, as-of date). Lines appear only if evidence exists.
- Actions: Create or Update, Snooze, Reject with reason (required, chosen from a short list plus free text).
- Filters: type, topic cluster, effort, surface. Sorting by rank (default) or impact.
- Comparison and pricing items carry a notice: Needs verified product and price facts and a named approver.
- Note under the list: Ranks compare opportunities within this site. They are not predictions.

### 3.5.3 Pages (inventory)

Table columns: page, type, health badge, diagnosis chip, clicks trend sparkline, position, last updated, findings count, AI visibility. Row click opens Page detail. Bulk actions: add to update set, snooze. Saved views: Decaying, Needs sources, Outdated prices, Orphans.

### 3.5.4 Page detail and Update Report

- Header: URL, title, last updated, status, owner.
- Report card: diagnosis with confidence and evidence link; problems (counts open to lists); opportunities; AI visibility with range; recommendation; effort; impact range; primary button Update article.
- Performance chart: clicks and (where comparable) impressions and position, with vertical annotations for data-quality breakpoints and published updates; year-over-year toggle.
- Tabs: Findings, Questions not answered, Links, Schema, Competitors, History (versions and outcomes).

### 3.5.5 Review screen (most important screen)

```
+---------------------------+----------------------------------+
| LEFT: Change list         | CENTRE: Preview / Diff           |
|  [x] 1 Replace stat       |  Toggle: Preview | Diff | Metadata|
|  [ ] 2 Update price (!)   |  Viewport: Mobile Tablet Desktop |
|  [ ] 3 New section        |                                  |
|  Filters: needs me (4)    |  (rendered page; changed spans   |
|                           |   highlighted)                   |
+---------------------------+----------------------------------+
| RIGHT: Claim and evidence panel                              |
|  Claim: Plans from $24 per seat   [High risk]                |
|  Verdict: Supported   Sources: vendor pricing page, 3 Oct    |
|  Passage: 'From $24 per seat per month'   [Open source]      |
|  [ ] I checked this claim                                    |
+--------------------------------------------------------------+
| Checklist: 4 of 9 confirmed  | Disclosure: [label on/off]    |
| [Reject with reason]   [Approve and schedule] (disabled)     |
+--------------------------------------------------------------+
```

Behaviours:

- **Forced confirmation:** every high-risk claim, statistic, price and date has a checkbox; Approve stays disabled until all are ticked. Server-side enforcement mirrors the UI.
- **Per-change accept or reject** for update runs; rejected changes are removed from the revision.
- **Inline editing:** changing text marks the span as needs re-verification; the panel shows a fresh verdict before the checklist item can be ticked.
- **Verdict chips:** Supported, Outdated, Unsubstantiated, Contradicted, each with an icon and text label. Contradicted claims block approval until revised.
- **Visual QA panel:** accessibility, performance, link and layout results with pass or fail and a link to each issue.
- **Metadata tab:** title, meta description, alt text, captions and schema preview, each with its own verification status.
- **Attestation dialog:** names the reviewer and role, states that the reviewer has checked the flagged claims, records the document version hash; the reviewer cannot proceed without confirming.
- **Regulated topics:** if the run needs a qualified expert, the Approve control shows who must approve and why.
- **Second-reviewer audit:** when sampled, a banner explains that a colleague will re-check this item.
- **Reject with reason:** required reason list; returns the run to revision with the reasons attached.
- **Keyboard flow:** next or previous change, accept, reject and tick shortcuts; focus never lost on re-verification.

### 3.5.6 Visibility

- **Rankings:** tracked keywords with position trend, snippet owner and People Also Ask presence.
- **Answer boxes:** table of answer targets (question, surface, format, owner, our position, status) with won and lost events.
- **AI answers:** per intent cluster and engine: mention rate and citation rate with range bars (whiskers), branded and unbranded separated, sample counts shown, a change shown only when ranges separate across two cycles. Where am I not cited view lists clusters by business value with the sources that are cited, and a Create brief action. A calibration note explains that API runs may differ from what people see in consumer apps.
- **AI referrals:** sessions, engagement and conversions from AI sources.
- **Crawler access:** per-bot verdict with matched rule, weekly status and regression alerts.
- **Search Console AI impressions:** page-level impressions in AI Overviews and AI Mode with a note on what the report does and does not include.

### 3.5.7 Experiments

List of experiments: hypothesis, change types, treated and matched pages, window, result with interval, status. Plain language summary: Updated pages gained more clicks than similar untouched pages, with a range, or Inconclusive: not enough pairs yet.

### 3.5.8 Calendar

Scheduled publishes, update triggers (Google update windows, price checks, link checks), and review deadlines.

### 3.5.9 Settings

- **Publish mode:** Mode 1 selected by default. Modes 2 and 3 appear as opt-in with plain explanations of the risks and conditions; Mode 3 shows a warning and requires an additional confirmation and a recorded owner.
- **Bot policy:** per-bot toggles with purpose labels (training, AI search, user fetch) and the current robots rule.
- **Disclosure:** label text, placement, preview.
- **Budgets:** monthly and per-run limits with live usage.
- **Integrations:** status, last sync, re-authenticate.
- **Brand and authors:** kit, voice samples, author bios.
- **Team:** roles scoped per site.

## 3.6 Design system

### 3.6.1 Semantic colour tokens

| Token | Light | Dark | Meaning |
| --- | --- | --- | --- |
| surface | #F2F5F0 | #0C1210 | Page background |
| card | #FFFFFF | #131C18 | Panels |
| ink | #101C18 | #EDEFEA | Text |
| muted | #51605A | #9FB0A8 | Secondary text |
| line | #D3DBD3 | #24322D | Dividers |
| verified | #1F8A5B | #1F8A5B | Supported, approved, healthy |
| decay | #E8A33D | #E8A33D | Decaying, outdated, needs attention |
| contradicted | #D6453D | #D6453D | Contradicted, failed, blocking |
| link | #2F5BEA | #7D9BFF | Links and focus |

Every status uses icon plus text plus colour. Contrast meets WCAG AA for text and non-text elements; verify combinations with a contrast checker before release.

### 3.6.2 Typography

Headlines: a serif (Newsreader or similar) at display sizes only; interface and body: a clean sans (Geist or similar); numbers, IDs and data: a monospace face. Type scale on a 1.2 ratio from 14 px to 40 px for the app; line length under 80 characters for prose; tabular figures in tables.

### 3.6.3 Layout and spacing

4 px base unit; 12-column grid on desktop, 8 on tablet, 4 on mobile; content max width 1280 px for dashboards and 720 px for reading panes; radius 8 px for controls and 12 px for panels; elevation reserved for overlays.

### 3.6.4 Key components

| Component | Purpose and rules |
| --- | --- |
| Evidence chip | Source name, as-of date, opens drawer; always present beside a claim |
| Verdict chip | Supported, Outdated, Unsubstantiated, Contradicted; icon plus text |
| Diagnosis badge | Type with a confidence label (low, medium, high) |
| Impact range bar | Low to high range with confidence label, never a single number |
| Interval bar | Point estimate with range whiskers for citation rates; sample count beside it |
| Rank chip | 0 to 100 rank within site with a components tooltip |
| Diff block | Before and after, accept and reject controls, source links, keyboard operable |
| Claim row | Text, risk, verdict, sources, confirmation checkbox |
| Forced checklist | Progress count; disables the primary action until complete |
| Annotated chart | Breakpoint and publish annotations, year-over-year toggle |
| Notice | Info, warning and blocking variants with a fix link |
| Data table | Sortable, filterable, sticky header, keyboard navigation, saved views |
| Skeleton, empty, error | Standard patterns (see 3.9) |

## 3.7 Content and microcopy

Principles: plain verbs, sentence case, active voice, name things as users do, say what happens, keep the same name for an action throughout a flow.

| Situation | Copy |
| --- | --- |
| Primary actions | Update article. Review changes. Approve and schedule. Roll back |
| Rejected change | Reject with reason |
| Blocked approval | 4 claims still need your check |
| Uncertain rate | Cited in 3 of 5 runs (range 15% to 85%) |
| No data | Not enough data yet. We need 4 weeks of runs |
| Not comparable | Impressions are not comparable across this date. Google changed how it counts them |
| Leave alone | Demand fell, but your ranking held. No update recommended |
| Error | We could not read this property. Grant the Search Console read-only permission, then try again |
| Empty feed | Connect Search Console to see which pages to fix first |

Never use: guaranteed, zero errors, hallucination-free, will rank, proven to increase. Always label example numbers Illustrative.

## 3.8 Showing uncertainty and honesty

- Show ranges, sample counts and as-of dates next to every estimate.
- Mark breakpoints and not-comparable periods on charts.
- State what a number is not (for example: ranks compare opportunities within this site; they are not predictions).
- When the evidence is thin, say Inconclusive.
- Provide an Explain this link on every score.

## 3.9 States

| State | Pattern |
| --- | --- |
| Loading | Skeletons that match final layout; progress text for long jobs with step names |
| Empty | One sentence on what to do next and one primary action |
| Partial data | Banner with what is missing and why (for example, sync still running) |
| Needs re-authentication | Persistent banner on affected screens plus a Settings link; dependent jobs paused and labelled |
| Run needs human | Card in Review and Today stating the reason and the one action needed |
| Error | What happened, what to do, a retry control; no apology language |
| Conflict | If a page changed in the CMS since review began, show a three-way compare and block publish until resolved |

## 3.10 Motion

Motion answers actions or shows change: row expansion, diff accept confirmation, chart line draw on first view, status transitions. No decorative loops. All motion respects reduced-motion preferences, with static final states. Animate transform and opacity only.

## 3.11 Accessibility

- WCAG 2.2 AA targets for product UI and generated articles.
- Full keyboard operation, visible focus (3 px outline), logical focus order, skip links, no keyboard traps in modals.
- Tables with header scope; diffs exposed to screen readers as inserted and deleted text with labels.
- Status never by colour alone; minimum target size 24 px; text resizable to 200 percent without loss.
- Charts have text alternatives and a data table toggle.
- Forms with labels, inline errors, and error summaries.
- Test with axe in CI plus manual screen-reader passes on the review screen.

## 3.12 Responsive behaviour

| Breakpoint | Layout |
| --- | --- |
| 1280 and up | Three-pane review; two-column Today |
| 768 to 1279 | Review collapses to two panes with a bottom sheet for evidence |
| Under 768 | Single column; review as stacked steps (changes, claims, checklist); charts scroll horizontally inside their container; sticky action bar with the forced checklist count |

## 3.13 Notifications

| Event | Channels | Notes |
| --- | --- | --- |
| Review requested | In-app, email, optional Slack | Includes the number of high-risk claims |
| Run needs human | In-app, email | States the single action needed |
| Decay detected above threshold | In-app, weekly email digest | Batched to avoid noise |
| Price or product change | In-app, email | Requires confirmation |
| Publish succeeded or failed | In-app | Link to live page and check result |
| Automatic pause triggered | In-app, email | Explains the trigger |
| Integration needs re-authentication | In-app, email | Persistent until resolved |

Slack is optional and informational; approvals with attestations happen in the web app.

## 3.14 Roles and what each sees

| Role | Sees and can do |
| --- | --- |
| Admin | Everything, including budgets, publish mode, billing, team |
| Editor | Opportunities, pages, create and update runs, edit drafts, request review |
| Reviewer | Review inbox, claim panel, approve or reject, audit samples |
| Viewer | Read-only dashboards and reports |

Regulated-topic items route only to reviewers marked as qualified.

## 3.15 Relationship to the marketing site

The landing page uses the same colour semantics and tone. Every example on the page is labelled Illustrative and no copy promises rankings, citations or hands-off content.

## 3.16 UX research and instrumentation

- Moderated tests with 5 users per persona on F1 to F3 before each release; task success and time on task recorded.
- Review-screen tests: can a reviewer find the evidence for any claim in under 15 seconds; do reviewers understand why Approve is disabled.
- Instrument events: onboarding step completion, time to first insight, feed actions and rejection reasons, review time, edits per review, forced-checklist abandonment, rollback usage.
- Review of rejection reasons and reviewer disagreement monthly.

## 3.17 UX acceptance criteria

| ID | Criterion |
| --- | --- |
| UX-A1 | Every feed explanation line opens an evidence row |
| UX-A2 | Approve is impossible with unchecked flagged claims, in the UI and on the server |
| UX-A3 | No estimate appears without a range or sample count where one exists |
| UX-A4 | Charts annotate breakpoints and mark non-comparable periods |
| UX-A5 | The review screen passes axe with zero serious violations and a keyboard-only walkthrough |
| UX-A6 | Status is conveyed by icon and text as well as colour everywhere |
| UX-A7 | First-time reviewers complete F3 without help in usability tests |
| UX-A8 | Mode 3 cannot be enabled without an extra confirmation and a recorded owner |

---

# PART 4: SYSTEM ARCHITECTURE AND DESIGN DOCUMENT

## 4.1 Purpose and architectural drivers

This part describes the structure of Verlytic, why it is shaped this way, and how it behaves under failure. Diagrams are text-based so they can be pasted into agent prompts and diffed in version control.

**Quality attributes, in priority order**

| # | Attribute | Why it ranks here | Architectural response |
| --- | --- | --- | --- |
| 1 | Trust and auditability | The product sells verified, human-approved content | Append-only evidence, attestations, lineage from claim to publication |
| 2 | Correctness | Wrong diagnoses and unverified claims destroy trust | Deterministic rules decide; schema-validated model output; golden-set evals |
| 3 | Reversibility and safety | Publishing mistakes are costly | Draft-first, idempotent publish, rollback, auto-pause, kill switch |
| 4 | Security and tenancy | Customer analytics and CMS credentials are sensitive | Tenant filter in repositories, encrypted secrets, isolated render pool |
| 5 | Cost control | Search data, SERP calls and model calls add up | Ledger, budgets, caching, shortlisting, model tiering |
| 6 | Evolvability | Platforms, APIs and models change fast | Adapters, config-driven models and thresholds, contract tests |
| 7 | Scalability | Many sites and pages per tenant | Stateless workers, queue-based scaling, partitioned metrics |
| 8 | Observability | Debugging multi-step agent runs | Run-level traces, cost and duration per stage |

## 4.2 System context

```
   Maya / Omar (Editors)      Lena (Reviewer)        Admin
            |                        |                  |
            +------------+-----------+------------------+
                         |  HTTPS (web app, REST API)
                         v
              +------------------------+
              |       VERLYTIC         |
              +-----------+------------+
   reads data  |          |           | writes content
     +---------+    +-----+------+    +----------+
     v              v            v               v
 Google Search   Google       DataForSEO     Customer CMS
 Console API     Analytics 4  (keywords,     (WordPress first;
 (read-only)     (read-only)  SERP, AI data) Webflow, Shopify, Ghost, Git)
                      |
        +-------------+--------------+
        v             v              v
   Evidence search  Model providers  PageSpeed / CrUX,
   (Tavily etc.)    (writer, verifier, IndexNow, image
                     vision, embeddings, providers
                     AI engines for panel)
```

Trust boundaries: customer browser, Verlytic platform, customer CMS and Google accounts (via OAuth), third-party APIs, and the open web (untrusted content).

## 4.3 Container view

```
+----------------+      +-------------------+      +----------------------+
|  Web app       | ---> |  API service      | ---> |  Postgres + pgvector |
|  (React/Next)  | REST |  (FastAPI)        |      |  app data, metrics,  |
+----------------+      |  authN/Z, audit   |      |  checkpoints, ledger |
                        +---------+---------+      +----------+-----------+
                                  | enqueue                   ^
                                  v                           |
                        +-------------------+                 |
                        |  Redis            |                 |
                        |  queue, cache,    |                 |
                        |  rate limiters    |                 |
                        +----+---------+----+                 |
                             |         |                      |
              +--------------+--+   +--+-----------------+    |
              | Run workers      |   | Crawl/monitor      |   |
              | LangGraph stages |   | workers            |---+
              | writer, verifier |   | crawl, links,      |
              | studio, publish  |   | prices, screenshots|
              +----+--------+----+   +--------------------+
                   |        |
      +------------+        +-------------+
      v                                   v
+------------------+            +----------------------+
| Render pool      |            | Object storage + CDN |
| Playwright, axe, |----------->| media, originals,    |
| Lighthouse,      |            | snapshots, exports   |
| diagram engines  |            +----------------------+
| (sandboxed)      |
+------------------+

Cross-cutting: Scheduler (cron to queue) | Model router + cost ledger |
Config service | Observability (OpenTelemetry, logs, Sentry, LLM traces)
```

Before the enterprise milestone, the same code runs on SQLite with an in-process scheduler behind identical repository and scheduler interfaces; the move to Postgres, Redis and separate workers changes configuration, not code.

## 4.4 Component and flow views

### 4.4.1 Run graph (LangGraph) by run type

```
Supervisor (plan-and-execute; writes the stage plan into state)
   |
   +-- update_article:
   |     load page -> brief (diff mode) -> evidence -> change-set writer
   |     -> VERIFY -> SEO/AEO/GEO + links + schema + visuals (change set only)
   |     -> render + gates -> [INTERRUPT: human review] -> publish revision
   |     -> post-publish checks -> measure/experiment
   |
   +-- new_article:
   |     brief -> evidence pack (gate G1) -> draft -> critique (<=2)
   |     -> VERIFY -> optimise -> links -> schema -> visuals -> render + gates
   |     -> [INTERRUPT: human review] -> publish -> checks -> measure
   |
   +-- onboard / opportunity_refresh: inventory -> competitors -> gaps
   |     -> questions -> AI opportunities -> decay + audit -> feed
   |
   +-- consolidate / citation_gap_fix / technical_fix / measure

Any node may raise NeedsHuman -> run pauses with a reason and a UI task.
```

### 4.4.2 Verification sub-graph

```
draft or change set
   |
   v
 claim extraction (selection > disambiguation > decomposition > decontextualisation)
   |
   v
 independent evidence retrieval (query by claim; tiers; excerpts; hashes)
   |
   v
 deterministic checks (numbers, dates, names, units)  -- mismatch -> verdict
   |
   v
 model verdict (different, stronger model) with required span
   |
   v
 policy engine (code): rewrite/remove | revise (<=2) | escalate | expert-required
   |
   v
 verification report (append-only) -> review bundle
```

### 4.4.3 Studio pipeline

```
 document model (typed blocks)
   |-- visual planner (justification per figure)
   |      |-- tables (HTML)  |-- diagrams (source > validate > SVG)
   |      |-- charts (sourced data > SVG/PNG)  |-- screenshots (Playwright)
   |      |-- social card (template)  |-- optional AI image (provenance kept)
   |-- links engine (internal by embeddings; external bound to evidence URL)
   |-- schema builders (typed JSON-LD, validated against visible content)
   |
   v
 renderers: semantic HTML | Markdown/MDX | WordPress blocks | CMS fields
   |
   v
 gates: axe (WCAG 2.2 AA) | Lighthouse | links | schema | 3-viewport layout QA
```

### 4.4.4 Measurement pipeline

```
 nightly:  GSC + GA4 sync -> own history tables -> breakpoint-aware comparisons
 weekly:   SERP tracking (rank, snippet owner, PAA, AIO sources)
           technical audit (crawl, CWV via PageSpeed/CrUX, bot policy)
           AI panel: paraphrase x engine x reruns -> PanelRecord -> intervals
 continuous: log classification of AI crawler hits
 derived:  decay detection -> diagnosis -> findings -> feed
           experiments: matching + difference-in-differences -> outcomes
           learning: recoverability and CTR model re-fit (proposals for human approval)
```

## 4.5 Key sequences

### 4.5.1 Update an article

```
User        API        Worker (run)     Verifier   Render pool   Reviewer     CMS
 |  Update    |            |               |           |            |           |
 |----------->| create run |               |           |            |           |
 |            |----------->| load page + metrics + findings         |           |
 |            |            |-- change set -->|          |            |           |
 |            |            |<-- verdicts ----|          |            |           |
 |            |            |-- render + gates ---------->|           |           |
 |            |            |<-- QA results ---------------|          |           |
 |            |            | INTERRUPT (checkpoint saved)             |           |
 |            |<-- notify review requested ----------------------------|           |
 |            |                                    forced checklist, accept/reject |
 |            |<-- approve + attestation (hash) ---------------------- |           |
 |            | resume --->| stage draft/revision ---------------------------------->|
 |            |            |<-- preview + ids -------------------------------------- |
 |            |            | publish; live-page diff; JSON-LD check; IndexNow         |
 |            |            | register tracking; schedule 7/28/90-day reviews          |
 |<-- result + rollback link                                                     |
```

### 4.5.2 Nightly sync and decay detection

```
Scheduler -> sync job (GSC, GA4) -> upsert metrics (idempotent by site, page, date)
          -> breakpoint-aware window compare -> decay rules -> diagnosis rows
          -> audit checks due -> findings -> priority recompute -> feed update
          -> notifications (batched)
```

### 4.5.3 Panel run

```
Scheduler -> select due clusters -> for each paraphrase x engine x rerun:
   adapter call (official API) -> normalise (resolve Gemini redirects) -> PanelRecord (append-only)
 -> aggregate (Wilson, cluster bootstrap) -> compare to noise floor
 -> flag change only if intervals separate in two consecutive cycles
 -> visibility dashboard + citation-gap tasks
```

### 4.5.4 Onboarding

```
OAuth (GSC, GA4) -> property choice -> CMS read test -> crawl + inventory
 -> business profile draft -> USER CONFIRMS -> competitors (user confirms)
 -> gaps, questions, AI opportunities -> decay + audit -> first feed
```

## 4.6 Data architecture

**Stores and responsibilities**

| Store | Holds | Notes |
| --- | --- | --- |
| Postgres | Entities, versions, metrics, checkpoints, ledger, evidence rows, approvals | Partitioned metrics; row-level security or enforced repository filters |
| pgvector | Embeddings of pages, passages, keywords, brand | Model and dimension recorded per row |
| Redis | Queue, API cache, rate limiters, short-lived locks | Not a system of record |
| Object storage | Raw HTML snapshots, original images, rendered media, screenshots, exports | Signed URLs; lifecycle rules |

**Lineage (the audit chain):** page version, then claim, then evidence, then verdict, then verification report, then reviewer attestation (with document hash), then publication, then outcome. Every link is a foreign key or hash, so any published sentence can be traced to its evidence and its approver.

**Immutability:** approvals, verification reports, audit log, price observations, panel records and cost ledger are append-only (enforced with database rules or triggers plus repository interfaces that expose no update method).

**Versioning:** article versions, prompts, style profiles and configs are versioned; a run stores the versions it used so any output can be reproduced or explained.

**Multi-tenancy:** shared database, shared schema, tenant\_id on every row, enforced in the repository layer and, in the enterprise release, by Postgres row-level security. Tenant-isolation tests run in CI. Object storage uses per-tenant prefixes; encryption keys are per tenant or per environment with rotation.

**Lifecycle:** hot data (recent metrics, active runs) in Postgres; raw snapshots and old query-level metrics move to cheaper storage by policy; deletion and export per tenant are first-class jobs.

## 4.7 Orchestration and consistency design

- **Checkpointing:** LangGraph state persisted after each node; runs resume after worker crashes.
- **Interrupts:** the graph pauses at human review (and any NeedsHuman) and resumes on an authenticated approval event.
- **Idempotency:** each node computes an idempotency key from run, stage and input versions; re-execution returns the stored output. External writes (CMS media, posts) use dedupe keys.
- **Retries:** exponential backoff with jitter for retryable errors; permanent errors fail fast with a clear reason; dead-letter queue for exhausted jobs with an operator view.
- **Publish as a saga:** stage, upload media, set metadata, publish, verify live. Each step has a compensating action (delete draft, restore previous revision). Failure after publish triggers rollback or a task.
- **Outbox pattern:** events (webhooks, notifications) are written to an outbox in the same transaction as the state change, then delivered at least once with signatures.
- **Concurrency:** optimistic locking on article versions; before publish, the adapter compares the CMS revision with the revision the review was based on and blocks on conflict (three-way compare in the UI).
- **Loop caps:** critique and verify-and-revise loops are capped by config; exceeding a cap raises NeedsHuman.

## 4.8 Deployment architecture

```
            Users --> CDN/WAF --> Load balancer
                                      |
                  +-------------------+-------------------+
                  v                                       v
          API service (N replicas)             Web app (static/SSR)
                  |
     +------------+-------------+------------------+
     v                          v                  v
 Run workers (autoscale     Crawl/monitor      Render pool (isolated
 by queue depth)            workers            network, egress allow-list)
     |                          |                  |
     +-----------+--------------+------------------+
                 v
     Managed Postgres (primary + replica, PITR)   Managed Redis   Object storage + CDN
```

- **Environments:** local, staging, production, with separate keys, databases and storage. Migrations run as a release step; health and readiness endpoints on every service.
- **Scaling:** API and workers are stateless and scale horizontally; autoscale workers on queue depth; separate queues and priorities so rendering and crawling never delay publishing; read replica for dashboards; metrics partitioned by month.
- **Network:** render pool has no route to internal networks and only allow-listed egress; workers reach providers through an egress proxy that logs destinations; secrets via a secret manager.
- **Disaster recovery (targets to validate):** point-in-time recovery for Postgres; tested restore monthly; object storage versioning; recovery objectives set by ADR once measured.
- **Not now:** Kubernetes, multi-region, service mesh. Revisit when load or customer requirements demand them.

## 4.9 Security architecture and threat model

| Threat | Asset at risk | Controls |
| --- | --- | --- |
| Prompt injection via crawled or retrieved pages | Run integrity, publish actions | Untrusted-data wrapping, stripped scripts and hidden text, schema-validated outputs, no credentials or publish tools in research and verification nodes |
| SSRF through fetch features | Internal network, metadata endpoints | URL allow-check blocking private, loopback, link-local and metadata addresses and non-HTTP schemes; redirect re-checks; egress proxy |
| OAuth or CMS token theft | Customer Google and CMS accounts | Encryption at rest with rotation; least-privilege read-only scopes; tokens never in logs, prompts or state; short-lived access where supported |
| Cross-tenant data leakage | All customer data | Enforced tenant filter, row-level security, isolation tests, per-tenant storage prefixes |
| Malicious or oversized uploads | Workers, storage | Type and size limits, malware scanning, isolated parsing, sandboxed rendering |
| XSS through generated HTML | Customer sites and the app | Output sanitisation, strict CSP in the app, escaping in renderers, no script blocks in articles |
| Reviewer fraud or rubber-stamping | Content integrity | Forced confirmations enforced server-side, second-reviewer sampling, disagreement metric, immutable attestations, role checks |
| Insider misuse | Customer data | Role-based access, audit log, break-glass procedure with logging |
| Supply chain compromise | Platform | Lockfile with exact versions, new releases delayed by policy, Dependabot, pip-audit, image and secret scanning |
| API-key abuse or runaway cost | Budget | Per-tenant budgets, per-run ceilings, rate limits, anomaly alerts |
| Rendering sandbox escape | Internal network | Container isolation, no host mounts, seccomp profile, network isolation |
| Webhook spoofing | Customer integrations | Signed payloads, replay protection |

Authentication by OIDC; authorisation by role and site scope on every route; audit log for every state change; data encrypted in transit and at rest.

## 4.10 Reliability and failure modes

| Failure | Behaviour |
| --- | --- |
| Search Console or GA4 API unavailable or quota hit | Retry with backoff; mark sync delayed; dashboards show last-good time; no decisions made from stale data without a visible banner |
| DataForSEO or search provider outage | Serve cached results within TTL; queue the rest; degrade the feed to existing data with a notice |
| Model provider outage or rate limit | Failover to the configured fallback for the same role; the verifier never falls back to the writer model; if no valid verifier exists, the run pauses (NeedsHuman) |
| Verification unavailable | Publishing is blocked; verification is never skipped |
| Render or visual step fails | Skip optional visuals with a visible note; required gates (accessibility, links, schema) still block |
| CMS API failure or conflict | Retry idempotently; on conflict show three-way compare; on repeated failure keep the draft and notify |
| Worker crash | Run resumes from the last checkpoint |
| Postgres unavailable | API returns a clear error; workers pause; queue retains jobs; no writes accepted without durable storage |
| Queue backlog | Autoscale; priority lanes keep review and publish paths responsive |
| Poisoned or malformed input | Quarantine and dead-letter with an operator view |
| Data-quality break (provider definition change) | Breakpoint added; comparisons across it flagged not comparable |

Principle: degrade by doing less, never by doing it unverified.

## 4.11 Observability

- **Traces:** OpenTelemetry spans per stage with run\_id, tenant\_id, site\_id, duration, cost and model version.
- **Logs:** structured JSON, no secrets, no full retrieved pages.
- **Metrics:** queue depth and age, job success and retry rates, stuck-run count, verifier failure rate, approval time, reviewer edit distance, cost per run, API error and latency by provider, cache hit rate.
- **LLM traces:** Langfuse or LangSmith for prompts, outputs, token use and eval scores.
- **Dashboards:** operations (queues, failures, cost), quality (verifier metrics, golden-set trends), product (time to first insight, review time).
- **Alerts:** stuck runs, verifier failure spike, GSC sync gaps, bot-policy regression, budget breach, automatic-pause triggers, error-budget burn.
- **SLOs (to validate):** review and publish paths 99.5% monthly; review bundle load under 3 s p95; sync freshness within 24 hours.

## 4.12 Cost architecture

- Every external call writes a ledger row (provider, endpoint, tokens or units, micro-cost, run).
- Budgets per tenant and per run with a hard stop and alerts at thresholds.
- Caching tiers by endpoint class: keyword and difficulty data (days to weeks), SERP snapshots (hours to days by location and device), page fetches (hours); panel answers are never cached because they are the measurement.
- Shortlisting before expensive SERP calls; bulk endpoints; model tiering (cheaper models for classification only when they pass the eval gate; stronger models for verification and critique).
- Usage and cost shown to users per run.

## 4.13 Evolution path

| Stage | Topology | Trigger to move on |
| --- | --- | --- |
| 1. Single node | SQLite, in-process scheduler, one process | Features validated with design partners |
| 2. Production basics | Postgres, Redis queue, API plus workers, object storage | Multiple tenants or concurrent runs |
| 3. Scaled workers | Separate crawler and render pools, autoscaling, read replica | Queue latency or render contention |
| 4. Enterprise | RLS, SSO, regional options, stricter DR | Enterprise customers and compliance asks |

Extension points: new AI-engine adapters, new CMS adapters, new languages and locales (locale per site in keyword, panel and hreflang logic), new audit checks (registered in the audit registry), new visual types (registered in the visual engine).

## 4.14 Key trade-offs and alternatives considered

| Decision | Chosen | Alternatives | Why |
| --- | --- | --- | --- |
| Orchestration | LangGraph with persistent checkpointer | Plain queue plus custom state machine; Temporal | Native interrupts and agent patterns; revisit Temporal if workflow durability needs grow |
| Decisions | Rules decide, models assist | Agentic end-to-end decisions | Auditability, testability, lower risk |
| Agents | One writer with capped critique | Many peer agents | Less drift and cost; add agents only if evals show gains |
| Content model | Typed document model with renderers | Raw HTML or Markdown pipeline | Verification once, consistent rendering, CMS portability |
| Metrics history | Own store plus BigQuery export | Rely on Search Console retention | 16-month limit and anonymisation |
| AI-citation data | Own panel plus data-provider tier | Provider only or panel only | Cross-check and calibration |
| Tenancy | Shared schema with tenant\_id and RLS | Schema or database per tenant | Simpler operations at this scale; revisit for large enterprise customers |
| Publishing default | Human-approved, automated mechanics | Fully unattended | Platform guidance, regulation and brand risk |
| Datastore | Postgres plus pgvector | Separate vector database | Fewer moving parts; revisit at scale |

## 4.15 Architecture fitness functions (automated checks)

1. No module outside the repository layer accesses the database.
2. No stage imports a model client directly; all model calls go through the router and write the ledger.
3. A static check fails the build on numeric thresholds or model names in stage code (they must come from config).
4. Every table query path injects tenant\_id; isolation tests attempt cross-tenant reads and must fail.
5. Append-only tables expose no update or delete method.
6. Verification cannot be skipped: the publish node refuses a document whose changed spans lack a fresh verdict and a valid attestation.
7. Research and verification nodes cannot import publisher or credential modules.
8. Every external adapter has a recorded-fixture contract test.
9. Every figure block has alt text and caption; every statistic has a source (property tests).
10. The verifier and writer roles resolve to different models (router configuration check).

## 4.16 Traceability and next steps

- PRD requirements map to modules in 2.4 and to stages in AGENT\_BUILD\_SPEC; UX acceptance criteria map to review and visibility screens; this part's fitness functions enforce the constraints that protect them.
- Next steps: run the milestone M0 audit and spikes, record the results as ADRs, set measured targets for verifier accuracy and diagnosis precision, and begin M1.

*End of document.*
