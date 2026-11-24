# Repository Configuration & Metadata Synchronization Audit

**Document:** `audit/submission_reproducibility/documentation/configuration_audit.md`
**Date:** November 2026
**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)
**Audited Baseline Commit:** `44838fa`

---

## 1. Overview & Verification Matrix

Every repository-level packaging, dependency, CI, and citation configuration file was audited for mutual consistency, syntax validity, and operational execution:

| Configuration File | Format / Purpose | Target Specification | Audit Status | Key Synchronizations Applied |
|---|---|---|:---:|---|
| `pyproject.toml` | PEP 518/621 Packaging | `name = "csd"`, `v1.0.0-rc2`, Python `>=3.10` | **VERIFIED** | Author order aligned (`Kalyan Kumar Das`, `Akash Kundu`, `Anirban Mukhopadhyay`). CLI entrypoints (`csd`, `icc`, `reproduce`) verified. |
| `CITATION.cff` | Citation Metadata (CFF 1.2.0) | Software & preferred paper citation | **VERIFIED** | Author order synchronized: Kalyan Kumar Das, Akash Kundu, Anirban Mukhopadhyay. Title harmonized. |
| `.zenodo.json` | Zenodo Archive Metadata | Metadata deposit for releases | **VERIFIED** | Creators order synchronized with `CITATION.cff` and `pyproject.toml`. |
| `requirements.txt` | Core Runtime Dependencies | `numpy`, `scipy`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn` | **VERIFIED** | Validated against `pyproject.toml` dependencies. |
| `requirements-dev.txt` | Developer Dependencies | `pytest`, `pytest-cov`, `black`, `ruff`, `mypy` | **VERIFIED** | All test tools load cleanly. |
| `environment/environment.yml`| Conda Environment | Python 3.10+, conda dependencies | **VERIFIED** | Environment name `csd`, dependencies aligned. |
| `environment/requirements-lock.txt` | Dependency Lockfile | Pinned dependency versions | **VERIFIED** | Minimal reviewer lockfile. |
| `.github/workflows/ci.yml` | GitHub Actions CI Pipeline | Automated lint, typecheck, tests | **VERIFIED** | CI matrix verifies Python 3.10, 3.11, 3.12, 3.13, 3.14. No private data or tokens exposed. |
| `.editorconfig` | Cross-Editor Formatting | UTF-8, LF line endings, 4 spaces indent | **VERIFIED** | Standard clean formatting. |
| `.gitattributes` | Git Normalization | Text eol normalization | **VERIFIED** | Prevents Windows/Linux CRLF collisions. |

---

## 2. CLI Entry Points Audit

The entry points configured in `pyproject.toml` were audited:
- `csd = "icc.__main__:main"`: Primary CLI entry point.
- `icc = "icc.__main__:main"`: Backward-compatibility alias.
- `reproduce = "scripts.reproduce:main"`: Top-level reproduction runner.

Both CLI entry points were tested using `--help` and argument validation (`tests/test_reproduce_cli.py`), passing with exit code 0.
