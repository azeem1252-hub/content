# Content Pipeline Agent 🚀
### Autonomous Multi-Agent Content Publishing & Mission Control Studio

An enterprise-grade autonomous content publishing platform powered by **LangGraph**, **Groq / Mistral LLMs**, **Gemini / Codex Image Generation**, **Slack Human-in-the-Loop Review Gates**, and a **FastAPI Mission Control Studio**.

---

## 📁 Project Architecture & Directory Layout

```
Content Pipeline agent/
├── data/                            # Local persistent SQLite databases (.gitignored)
│   ├── pipeline.db                  # Core database (posts, websites, schedules, runs)
│   └── pipeline_checkpoints.db      # Durable LangGraph thread checkpointer
│
├── docs/                            # Documentation & Architecture Plans
│   └── architecture_plan.md         # Full system architecture and design specifications
│
├── pipeline/                        # LangGraph Publishing Engine & Autonomous Agents
│   ├── adapters/                    # External integrations (Codex, Gemini, Slack, Next.js)
│   │   ├── codex_image.py           # Codex / ChatGPT / Pollinations image generation
│   │   ├── gemini_image.py          # Gemini flash image generation
│   │   ├── slack_bot.py             # Slack Block Kit review cards & interactive modals
│   │   └── website_client.py        # Webhook / REST publishing adapter
│   ├── nodes/                       # LangGraph state-graph nodes
│   │   ├── outline_node.py          # Trend research & SEO outline generation
│   │   ├── draft_node.py            # Long-form article drafting
│   │   ├── audit_node.py            # Automated SEO auditing & scoring
│   │   ├── image_node.py            # Hero visual prompt synthesis & generation
│   │   ├── review_node.py           # Slack human review gate interrupt
│   │   ├── publish_node.py          # Live publishing to CMS / website
│   │   └── repurpose_node.py        # Social distribution (LinkedIn, X threads)
│   ├── graph.py                     # StateGraph assembly & compilation
│   ├── llm_client.py                # Multi-provider LLM router (Groq / Mistral)
│   ├── pipeline_manager.py          # Async execution queue & checkpointer manager
│   ├── scheduler.py                 # Automated APScheduler background runner
│   ├── state.py                     # ContentState type definitions
│   ├── topic_researcher.py          # Autonomous trend & topic discovery
│   └── utils.py                     # Text cleaning, slug generation, read-time calculation
│
├── storage/                         # Core Persistence & Database Layer
│   ├── __init__.py                  # Clean exports of all DB operations
│   └── db.py                        # SQLite schema, connections, and CRUD operations
│
├── web/                             # Mission Control Studio Frontend & APIs
│   ├── static/                      # Static assets
│   │   ├── css/                     # dashboard.css (Obsidian Dark & Crisp Snow Light)
│   │   ├── js/                      # dashboard.js (live streams, telemetry, controls)
│   │   └── uploads/                 # Generated hero images & media
│   ├── templates/                   # Jinja2 HTML templates
│   │   ├── dashboard.html           # Mission Control Studio Dashboard
│   │   └── preview.html             # Draft preview & live editorial review gate
│   ├── __init__.py
│   └── app.py                       # FastAPI application & REST APIs
│
├── scripts/                         # Command Line Tools & Diagnostics
│   ├── run_studio.py                # Starts Mission Control Web Studio on port 8000
│   ├── run_pipeline.py              # CLI runner for LangGraph pipeline
│   ├── run_slack_listener.py        # Slack Socket Mode interactive listener
│   ├── smoke_test.py                # Offline pipeline integration test
│   ├── verify_app.py                # Full application endpoint & asset verification
│   └── verify_checkpointer.py       # Checkpointer thread persistence test
│
├── tests/                           # Complete pytest automated test suite
│   ├── conftest.py                  # Pytest fixtures & isolated in-memory DB
│   └── test_*.py                    # Unit and integration tests
│
├── main.py                          # Unified CLI entrypoint
├── config.py                        # Centralized configuration & environment loader
├── pytest.ini                       # Test runner configuration
└── requirements.txt                 # Dependencies
```

---

## ⚡ Quick Start

### 0. Clone & Install Dependencies
```bash
git clone <repository-url>
cd "Content Pipeline agent"
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
*(Dependencies include FastAPI, LangGraph, APScheduler, Tavily, Google GenAI / Gemini, Pillow, Trafilatura, and Pytest).*

### 1. Launch Mission Control Studio
Start the FastAPI server hosting the Mission Control Studio:
```bash
python main.py studio
```
* **Mission Control Studio**: `http://localhost:8000` (or `http://localhost:8000/dashboard`)
* **OpenAPI Documentation**: `http://localhost:8000/docs`

---

### 2. Run Autonomous Pipeline via CLI
Generate, audit, and stage an article:
```bash
python main.py pipeline --topic "Multi-Agent AI Workflows in 2026" --keywords "Agents, LangGraph, AI"
```
*(Add `--auto-approve` to bypass the Slack editorial gate for automated testing)*

---

### 3. Start Slack Socket Mode Listener
Listen for editorial approvals, rejection, and revision feedback from Slack:
```bash
python main.py slack
```

---

### 4. Run Diagnostic & Smoke Tests
Verify that all LangGraph nodes, checkpointer states, and database operations are healthy:
```bash
python main.py verify
```

To run the complete automated test suite:
```bash
pytest
```

---

## 🛠️ Environment Configuration
Configure your keys in `.env` (copy from `.env.example`):
```ini
GROQ_API_KEY=gsk_...
MISTRAL_API_KEY=...
PREFERRED_PROVIDER=groq
GEMINI_API_KEY=AIza...
TAVILY_API_KEY=tvly-...
SLACK_BOT_TOKEN=xoxb-...
SLACK_APP_TOKEN=xapp-...
SLACK_CHANNEL_ID=C0...
DATABASE_URL=data/pipeline.db
PUBLIC_BASE_URL=http://127.0.0.1:8000
```
