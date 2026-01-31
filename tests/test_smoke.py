import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], cwd: Path) -> None:
    result = subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True)
    assert result.returncode == 0


def test_demo_runs(tmp_path: Path) -> None:
    repo = Path(__file__).resolve().parents[1]
    run(
        [
            sys.executable,
            str(repo / "01-anonymisation-gdpr" / "anonymize.py"),
            "--input",
            str(repo / "01-anonymisation-gdpr" / "clients.sample.csv"),
            "--output",
            str(tmp_path / "clients.anonymized.csv"),
        ],
        cwd=repo / "01-anonymisation-gdpr",
    )
    run(
        [
            sys.executable,
            str(repo / "03-detecteur-phishing" / "phishing_score.py"),
            "--text",
            "Urgent: verification de mot de passe avant virement",
        ],
        cwd=repo / "03-detecteur-phishing",
    )
    baseline = tmp_path / "baseline.json"
    run(
        [
            sys.executable,
            str(repo / "04-file-integrity-monitor" / "fim.py"),
            "--folder",
            str(repo / "04-file-integrity-monitor"),
            "--baseline",
            str(baseline),
        ],
        cwd=repo / "04-file-integrity-monitor",
    )
