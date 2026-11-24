# CSD Documentation, Configuration & Repository Hygiene Audit

**Document:** `audit/submission_reproducibility/documentation_audit.md`  
**Date:** November 2026  
**Canonical Repository:** [`AkashKundu114/clustering-stability-discordance`](https://github.com/AkashKundu114/clustering-stability-discordance)  
**Maintenance Branch:** `docs/hygiene-and-synchronization`  
**Audited Baseline Commit:** `44838fa`  

---

## 1. Executive Audit Summary

A comprehensive documentation, packaging, and ignore-rule audit was conducted across the entire repository to ensure that:
1. All documentation reflects the authoritative 48-page submitted manuscript PDF (*Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*, SHA-256: `b32259bfd704a7a7e6dd45e5717a731f0d8100d819cfd792911645e7da571a3c`).
2. No outdated badges, incorrect author orders, broken internal links, or obsolete CLI commands persist.
3. Packaging configuration (`pyproject.toml`, dependencies, build backend) builds cleanly without warnings.
4. Version-control ignore rules strictly exclude private audit loops, raw clinical arrays, and large submission zip archives while tracking official public audit assets.
5. All 92 repository documentation and configuration files are cataloged, verified, and mapped.

---

## 2. Repository Inventory Summary

The repository contains **92 documentation and configuration files**, classified across the following functional categories:

| Location / Category | File Count | Purpose | Verification Status |
|---|---|---|---|
| **Repository Root** | 12 | Primary project entry points (`README.md`, `REPRODUCIBILITY.md`, `ENVIRONMENT.md`, `EXPERIMENTAL_PROTOCOL.md`, metadata, licenses) | **VERIFIED** |
| **`docs/` Directory** | 11 | Detailed specifications (`submitted_manuscript.md`, `experiment_catalog.md`, `result_dictionary.md`, `data_rights.md`, `limitations.md`, etc.) | **VERIFIED** |
| **`experiments/`** | 1 | Experiment directory guidance (`experiments/README.md`) | **VERIFIED** |
| **`results/`** | 7 | Result directory and figure descriptions (`results/README.md`, `results/figures/README.md`, etc.) | **VERIFIED** |
| **`reproduction/`** | 3 | Historical arithmetic checks and reviewer guidance (`reproduction/README.md`, `quick_verification.md`, `numerical_comparison_report.md`) | **VERIFIED** |
| **`tests/`** | 2 | Test suite documentation and CLI verification tests (`tests/README.md`, `tests/test_reproduce_cli.py`) | **VERIFIED** |
| **`audit/submission_reproducibility/`** | 5 | Core public audit records (`README.md`, `audit_report.md`, `claim_evidence_matrix.csv`, `reproduction_status.csv`, `documentation_audit.md`) | **VERIFIED** |
| **Dotfiles & Tool Configs** | 51 | GitHub workflows, linting, editor, git configuration, and lockfiles | **VERIFIED** |
| **Total Tracked** | **92** | Full documentation and configuration surface | **100% AUDITED** |

*Note: The 33+ MB zip archives and internal submission drafts in `DMKD_Submission_Package/` are explicitly excluded from Git tracking via `.gitignore`.*

---

## 3. Outdated Documentation Identified & Corrected

During this hygiene pass, the following discrepancies were identified and surgically corrected:

1. **Test Badge & Count Mismatch:**
   - *Previous state:* `README.md` displayed an outdated `tests-86%20passed` badge from an earlier development iteration.
   - *Resolution:* Synchronized badge to reflect exact test outcomes: `82 unit passed (150 total collected)`.
2. **Author Sequence Discrepancy:**
   - *Previous state:* `CITATION.cff` and `.zenodo.json` listed Akash Kundu as the first author in both software and preferred citations.
   - *Resolution:* Synchronized author sequence to match the submitted manuscript title page: Kalyan Kumar Das (First Author), Akash Kundu (Second Author / Corresponding Contributor), Anirban Mukhopadhyay (Senior Author).
3. **Dataset Attribution Typo:**
   - *Previous state:* `README.md` erroneously associated UPV/EHU with "Lung Cancer".
   - *Resolution:* Corrected UPV/EHU attribution to the hyperspectral Indian Pines repository.
4. **Environment Name Harmonization:**
   - *Previous state:* `ENVIRONMENT.md` contained a stray reference to `conda activate icc-clustering`.
   - *Resolution:* Updated command to `conda activate csd` and added explicit hardware memory boundaries for 16 GB commodity machines.
5. **Reproduction Tier Harmonization:**
   - *Previous state:* `REPRODUCIBILITY.md` featured a three-tier layout with mixed tier numbering.
   - *Resolution:* Harmonized into the standardized 4-tier reproduction framework (Tier 0: Environment & Tests, Tier 1: Aggregate Friedman test, Tier 2: Saved-partition stability recalculation, Tier 3: Fresh rerun bounds).
6. **Subprocess Windows Handle Failure:**
   - *Previous state:* `tests/test_reproduce_cli.py` invoked `subprocess.run` without `stdin=subprocess.DEVNULL`, causing `OSError: [WinError 6] The handle is invalid` on Windows when executed from non-console background environments.
   - *Resolution:* Added `stdin=subprocess.DEVNULL` to both `subprocess.run` calls; all 4 CLI tests pass cleanly.

---

## 4. Packaging & Configuration Audit

- **Package Identity:** Synchronized to `csd` version `1.0.0-rc2` under `pyproject.toml`.
- **Build Backend:** `hatchling.build` configured with standard metadata.
- **Packaging Build Verification:** Successfully executed `python -m build --wheel --no-isolation`. The resulting artifact `csd-1.0.0rc2-py3-none-any.whl` built with zero warnings or missing entry points.
- **CI Workflows:** All 4 GitHub Actions workflows (`ci.yml`, `docs.yml`, `publish.yml`, `zenodo.yml`) were verified to target package `csd` and use correct pytest options (`-o addopts=""`).
- **Dependencies:** Strictly pinned in `requirements.txt` and `requirements-dev.txt`, with verified lockfile in `reproduction/environment/win-py314-requirements-lock.txt`.

---

## 5. Ignore Rules (`.gitignore`) & Tracking Audit

A forensic audit of `.gitignore` was conducted to ensure proper isolation of private materials and public audit records:

| Category | Ignore Rules in `.gitignore` | Audit Finding & Safety Verification |
|---|---|---|
| **Private Audit & Research** | `/audit/*`<br>`!/audit/submission_reproducibility/`<br>`/paper/`<br>`/manuscript/`<br>`/submission/` | Private author audit material remains excluded; the official submission reproducibility directory is explicitly permitted. |
| **Submission Bundles** | `DMKD_Submission_Package/`<br>`*.zip` | Prevents heavy 33+ MB submission packages and zip archives from bloating git history. |
| **Research Data & Caches** | `/data/raw/`<br>`/data/cache/`<br>`*.h5`<br>`*.h5ad`<br>`/results/stability/partitions/`<br>`/results/stability/runs/` | Human clinical microarrays, SELDI spectra, and patient-indexed partition arrays are strictly excluded from git tracking. |
| **Python Build & Tests** | `__pycache__/`<br>`*.py[cod]`<br>`.pytest_cache/`<br>`.ruff_cache/`<br>`.coverage`<br>`build/`<br>`dist/` | Standard build and test cache artifacts are cleanly excluded. |
| **Virtual Environments** | `.env`<br>`.env.*`<br>`!.env.example`<br>`.venv/`<br>`venv/`<br>`env/` | Local environment variables and virtualenvs are ignored; example template `.env.example` is tracked. |
| **IDE & System Metadata** | `.vscode/`<br>`.idea/`<br>`.DS_Store`<br>`Thumbs.db` | Operating system and IDE configuration artifacts are excluded. |

*Tracking Check:* Exactly 194 files tracked via `git ls-files` at baseline. Zero tracked `.pyc`, zero tracked virtualenvs, zero tracked patient microarrays.

---

## 6. Link Integrity Audit

An automated script evaluated **220 internal markdown file links and external HTTP URLs** across all documentation in the repository.

- **Total Links Checked:** 220
- **Valid Links:** 220
- **Broken Links:** 0
- **Audit Result:** **100% INTEGRITY PASSED**

Every cross-reference between `README.md`, `REPRODUCIBILITY.md`, `EXPERIMENTAL_PROTOCOL.md`, `docs/`, and `audit/` resolves to an existing file.

---

## 7. Documentation Change Log

| File Path | Change Type | Reason | Verification Status |
|---|---|---|---|
| `.gitignore` | MODIFIED | Allow `audit/submission_reproducibility/` while ignoring private audit and zip archives | **VERIFIED** |
| `CITATION.cff` | MODIFIED | Synchronize author order to Das, Kundu, Mukhopadhyay | **VERIFIED** |
| `.zenodo.json` | MODIFIED | Synchronize Zenodo creators order | **VERIFIED** |
| `README.md` | MODIFIED | Update test badge, add submitted PDF reference, fix UPV/EHU typo, link 4-tier model | **VERIFIED** |
| `REPRODUCIBILITY.md` | MODIFIED | Harmonize into 4 standardized reproduction tiers | **VERIFIED** |
| `ENVIRONMENT.md` | MODIFIED | Update activate command to `csd`; add 16 GB RAM boundary notes | **VERIFIED** |
| `docs/limitations.md` | MODIFIED | Substantially expand across 14 empirical, statistical, and operational boundaries | **VERIFIED** |
| `docs/project_inventory.md` | MODIFIED | Synchronize to canonical repository `clustering-stability-discordance` commit `44838fa` | **VERIFIED** |
| `tests/test_reproduce_cli.py` | MODIFIED | Add `stdin=subprocess.DEVNULL` to fix Windows invalid handle exception | **VERIFIED** |
| `EXPERIMENTAL_PROTOCOL.md` | CREATED | Core root specification of seeds, splits, BGSS formulas, and factorial design | **VERIFIED** |
| `docs/repository_structure.md` | CREATED | Architectural tree and directory responsibility guide | **VERIFIED** |
| `docs/experiment_catalog.md` | CREATED | Detailed mapping of EXP-01 through EXP-07 with methods and artifacts | **VERIFIED** |
| `docs/result_dictionary.md` | CREATED | Empirical metric dictionary with exact reported vs recomputed quantities | **VERIFIED** |
| `docs/reproducibility_architecture.md` | CREATED | Four-tier reproduction framework specification | **VERIFIED** |
| `docs/submitted_manuscript.md` | CREATED | Exact metadata, SHA-256 hash, and evidence mapping for 48-page submitted PDF | **VERIFIED** |
| `docs/data_rights.md` | CREATED | Data governance taxonomy (Category A, B, C) for all 13 datasets | **VERIFIED** |
| `docs/experimental_provenance.md` | CREATED | Provenance classifications (Authenticated, Corroborated, Historical) | **VERIFIED** |
| `audit/submission_reproducibility/claim_evidence_matrix.csv` | CREATED | Manuscript claim to code and artifact mapping | **VERIFIED** |
| `audit/submission_reproducibility/reproduction_status.csv` | CREATED | Experiment reproduction tier, status, and limitations registry | **VERIFIED** |
| `audit/submission_reproducibility/audit_report.md` | CREATED | Comprehensive consolidated audit findings and final assessment | **VERIFIED** |
| `audit/submission_reproducibility/documentation_audit.md` | CREATED | Consolidated documentation, packaging, ignore-rule, and link audit | **VERIFIED** |
| `audit/submission_reproducibility/README.md` | CREATED | Audit navigation, interpretation, and scope guide | **VERIFIED** |
