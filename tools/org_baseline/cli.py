"""CLI entry point.

Usage in CI:
    python -m org_baseline.cli \
      --consumer-root consumer \
      --org-root org \
      --manifest org/baseline-manifest.json \
      --output-mode check-run \
      --head-sha "$PR_HEAD_SHA" \
      --repo "$REPO"

Usage locally (no GitHub API):
    python -m org_baseline.cli \
      --consumer-root path/to/consumer \
      --org-root path/to/org \
      --manifest path/to/org/baseline-manifest.json \
      --output-mode markdown
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from .check import overall_passed, run_check
from .manifest import load_manifest
from .report import to_check_run_payload, to_json, to_markdown


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="org-baseline",
        description=__doc__.splitlines()[0] if __doc__ else None,
    )
    p.add_argument("--consumer-root", type=Path, required=True)
    p.add_argument("--org-root", type=Path, required=True)
    p.add_argument("--manifest", type=Path, required=True)
    p.add_argument(
        "--output-mode",
        choices=("json", "markdown", "check-run"),
        default="markdown",
        help="What to emit on stdout. check-run also POSTs to GitHub Check Runs API.",
    )
    p.add_argument(
        "--head-sha",
        help="PR head SHA (required for check-run mode).",
    )
    p.add_argument(
        "--repo",
        help='Consumer repo in "owner/repo" form (required for check-run mode).',
    )
    p.add_argument(
        "--step-summary",
        type=Path,
        default=None,
        help=(
            "If set, also append the markdown report to this path (typically $GITHUB_STEP_SUMMARY)."
        ),
    )
    return p


def _post_check_run(repo: str, payload: dict) -> None:
    """POST the Check Run via gh CLI (uses GITHUB_TOKEN from env)."""
    body = json.dumps(payload)
    subprocess.run(
        [
            "gh",
            "api",
            "-X",
            "POST",
            f"repos/{repo}/check-runs",
            "--input",
            "-",
        ],
        input=body,
        text=True,
        check=True,
    )


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)

    manifest = load_manifest(args.manifest)
    results = run_check(manifest, args.org_root, args.consumer_root)
    passed = overall_passed(results)

    md = to_markdown(results)
    if args.step_summary is not None:
        with args.step_summary.open("a", encoding="utf-8") as fh:
            fh.write(md + "\n")

    if args.output_mode == "json":
        print(to_json(results))
    elif args.output_mode == "markdown":
        print(md)
    elif args.output_mode == "check-run":
        if not args.head_sha or not args.repo:
            print("error: --head-sha and --repo required for check-run mode", file=sys.stderr)
            return 2
        payload = to_check_run_payload(results, head_sha=args.head_sha)
        _post_check_run(args.repo, payload)
        # Also print markdown to job log for grepability.
        print(md)

    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
