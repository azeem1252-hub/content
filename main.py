"""
Content Pipeline Agent — Unified Command Line Interface (CLI)
Entrypoint for launching the Web Studio, triggering pipeline runs, starting Slack listener, or running diagnostic tests.

Usage:
    python main.py studio                      # Launch Web Studio on http://localhost:8000
    python main.py pipeline --topic "..."      # Run autonomous content publishing pipeline
    python main.py slack                       # Start Slack Socket Mode interactive listener
    python main.py verify                      # Run offline pipeline smoke test
"""

import sys
import argparse
import uvicorn
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def cmd_studio(args):
    """Launch the Mission Control Studio & Dispatch Blog server."""
    from scripts.run_studio import main as studio_main
    studio_main()


def cmd_pipeline(args):
    """Trigger the LangGraph publishing pipeline."""
    from scripts.run_pipeline import run as pipeline_run
    kws = [k.strip() for k in args.keywords.split(",") if k.strip()]
    pipeline_run(
        topic=args.topic,
        keywords=kws,
        target_audience=args.audience,
        auto_approve=args.auto_approve
    )


def cmd_slack(args):
    """Start the Slack Socket Mode interactive listener."""
    from scripts.run_slack_listener import start_slack_listener
    start_slack_listener()


def cmd_verify(args):
    """Run offline pipeline smoke test and checkpointer verification."""
    from scripts.smoke_test import run as run_smoke_test
    print("=" * 60)
    print("  RUNNING OFFLINE PIPELINE SMOKE TEST")
    print("=" * 60)
    run_smoke_test()


def cmd_opportunities(args):
    """Generate and view the v5 Opportunity Feed ('What should I publish?')."""
    from pipeline.adapters.opportunity_feed import generate_opportunity_feed
    print(f"\n--- Generating Opportunity Feed for website '{args.site}' (limit={args.limit}) ---")
    items = generate_opportunity_feed(website_id=args.site, limit=args.limit)
    print(f"Generated {len(items)} prioritized opportunities:\n")
    for i, it in enumerate(items, 1):
        comp_badge = " [COMP/PRICE - HUMAN REQUIRED]" if it.get("human_approval_required") else ""
        print(f"{i}. [{it.get('relative_rank')}/100 Rank] {it.get('title')}{comp_badge}")
        print(f"   Action: {it.get('action')} | Template: {it.get('template_type')} | Effort: {it.get('effort_level')}")
        print(f"   Est. Clicks: {it.get('expected_clicks_min')} - {it.get('expected_clicks_max')} (Conf: {it.get('confidence_level')})")
        print(f"   Why: {it.get('plain_reason')}\n")


def cmd_decay(args):
    """Diagnose content decay and prioritize update portfolio (A8b)."""
    from pipeline.adapters.content_decay import prioritize_update_portfolio
    print(f"\n--- Running Content Decay & Update Agent for website '{args.site}' ---")
    plans = prioritize_update_portfolio(website_id=args.site, reviewer_hours_budget=args.hours)
    print(f"Found {len(plans)} candidate articles needing updates within {args.hours}h budget:\n")
    for i, p in enumerate(plans, 1):
        print(f"{i}. {p.get('title')} ({p.get('url')})")
        print(f"   Diagnosis: {p.get('diagnosis')} (Conf: {p.get('diagnosis_confidence')})")
        print(f"   Priority Score: {p.get('priority_score')} | Recoverable Clicks: {p.get('recoverable_clicks')}")
        print(f"   Work Items: {p.get('work_items_count')} changes (~{p.get('estimated_minutes')} reviewer minutes)")
        print(f"   Analysis: {p.get('diagnosis_explanation')}\n")


def cmd_eval(args):
    """Calculate Difference-in-Differences causal lift (A12)."""
    from pipeline.adapters.eval_experiments import calculate_difference_in_differences
    t_pre = [float(x.strip()) for x in args.treat_pre.split(",") if x.strip()]
    t_post = [float(x.strip()) for x in args.treat_post.split(",") if x.strip()]
    c_pre = [float(x.strip()) for x in args.ctrl_pre.split(",") if x.strip()]
    c_post = [float(x.strip()) for x in args.ctrl_post.split(",") if x.strip()]

    print("\n--- Running Difference-in-Differences (DiD) Causal Evaluation ---")
    res = calculate_difference_in_differences(t_pre, t_post, c_pre, c_post, metric_name=args.metric)
    print(f"Verdict: {res.get('verdict')}")
    print(f"DiD Causal Effect: {res.get('did_causal_effect')} {args.metric} per page")
    print(f"Treatment Delta: {res.get('treatment_delta')} | Control Delta: {res.get('control_delta')}")
    print(f"95% Confidence Interval: {res.get('confidence_interval_95')}")
    print(f"Analysis: {res.get('explanation')}\n")


def main():
    import storage.db as db
    db.init_db()

    parser = argparse.ArgumentParser(

        description="Content Pipeline Agent — Autonomous Publishing & Mission Control CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py studio
  python main.py pipeline --topic "Autonomous AI Workflows in 2026"
  python main.py opportunities --site default
  python main.py decay --site default --hours 8
  python main.py eval --treat-pre 10,12,11 --treat-post 25,27,26 --ctrl-pre 10,11,10 --ctrl-post 11,12,11
  python main.py verify
"""
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # studio / web
    sub_studio = subparsers.add_parser("studio", aliases=["web"], help="Start Web Studio & Mission Control Dashboard")
    sub_studio.set_defaults(func=cmd_studio)

    # pipeline
    sub_pipeline = subparsers.add_parser("pipeline", help="Run the LangGraph content publishing pipeline")
    sub_pipeline.add_argument("--topic", type=str, default="Autonomous Multi-Agent Pipelines in 2026", help="Article topic")
    sub_pipeline.add_argument("--keywords", type=str, default="LangGraph, Groq, Autonomous Agents, AI", help="Comma-separated keywords")
    sub_pipeline.add_argument("--audience", type=str, default="Technical Leaders & Developers", help="Target audience")
    sub_pipeline.add_argument("--auto-approve", action="store_true", help="Auto-approve without pausing at Slack review gate")
    sub_pipeline.set_defaults(func=cmd_pipeline)

    # opportunities
    sub_opp = subparsers.add_parser("opportunities", aliases=["feed"], help="Generate Opportunity Feed (Pillar A1b)")
    sub_opp.add_argument("--site", type=str, default="default", help="Website ID")
    sub_opp.add_argument("--limit", type=int, default=10, help="Max opportunities to generate")
    sub_opp.set_defaults(func=cmd_opportunities)

    # decay
    sub_decay = subparsers.add_parser("decay", help="Run Content Decay & Update Agent (Pillar A8b)")
    sub_decay.add_argument("--site", type=str, default="default", help="Website ID")
    sub_decay.add_argument("--hours", type=float, default=10.0, help="Human reviewer capacity in hours")
    sub_decay.set_defaults(func=cmd_decay)

    # eval
    sub_eval = subparsers.add_parser("eval", help="Run Difference-in-Differences causal evaluation (Pillar A12)")
    sub_eval.add_argument("--treat-pre", type=str, required=True, help="Comma-separated treatment pre-period numbers")
    sub_eval.add_argument("--treat-post", type=str, required=True, help="Comma-separated treatment post-period numbers")
    sub_eval.add_argument("--ctrl-pre", type=str, required=True, help="Comma-separated control pre-period numbers")
    sub_eval.add_argument("--ctrl-post", type=str, required=True, help="Comma-separated control post-period numbers")
    sub_eval.add_argument("--metric", type=str, default="clicks", help="Metric name (e.g. clicks)")
    sub_eval.set_defaults(func=cmd_eval)

    # slack
    sub_slack = subparsers.add_parser("slack", help="Start Slack Socket Mode interactive listener")
    sub_slack.set_defaults(func=cmd_slack)

    # verify
    sub_verify = subparsers.add_parser("verify", aliases=["test"], help="Run offline smoke test and checkpointer verification")
    sub_verify.set_defaults(func=cmd_verify)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    args.func(args)



if __name__ == "__main__":
    main()
