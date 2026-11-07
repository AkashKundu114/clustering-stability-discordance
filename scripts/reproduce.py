"""Run the supported synthetic smoke workflow or the automated test suite."""

import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run supported software checks; this does not reproduce the historical paper analyses."
    )
    parser.add_argument(
        "--scope",
        default="smoke",
        choices=["smoke", "verify"],
        help="smoke runs a synthetic example; verify runs the test suite",
    )
    args = parser.parse_args()

    if args.scope == "smoke":
        print("[*] Running synthetic smoke example (not a research-result reproduction).", flush=True)
        cmd = [
            sys.executable,
            str(ROOT / "scripts" / "run.py"),
            "--config",
            str(ROOT / "configs" / "examples" / "synthetic.yaml"),
        ]
    else:
        print("[*] Running verification test suite.", flush=True)
        cmd = [sys.executable, "-m", "pytest", str(ROOT / "tests")]
    return subprocess.run(cmd, cwd=str(ROOT), check=False).returncode


if __name__ == "__main__":
    sys.exit(main())
