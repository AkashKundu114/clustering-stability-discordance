# Git Ignore Rules & Tracking Audit

**Document:** `audit/submission_reproducibility/documentation/ignore_rules_audit.md`
**Date:** November 2026
**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)
**Audited Baseline Commit:** `44838fa`

---

## 1. Executive Ignore Assessment

A forensic audit of `.gitignore` was executed to ensure that:
1. All private author audit loops, development drafts, and raw patient arrays remain strictly excluded.
2. The official public audit documentation (`audit/submission_reproducibility/`) is trackable.
3. Large submission archive zips (`*.zip`) and submission package trees (`DMKD_Submission_Package/`) are excluded from public git trees.
4. No sensitive tokens, `.env` files, or binary face databases can be accidentally committed.
5. All 194 currently tracked files in the canonical repository are legitimate research, documentation, or code assets.

---

## 2. Rule Categorization & Evaluation Matrix

| Category | Ignore Rules in `.gitignore` | Audit Finding & Safety Verification |
|---|---|---|
| **Private Audit & Research** | `/audit/*`<br>`!/audit/submission_reproducibility/`<br>`/paper/`<br>`/manuscript/`<br>`/submission/` | Private author audit material remains excluded; the official submission reproducibility documentation is explicitly permitted. |
| **Submission Bundles** | `DMKD_Submission_Package/`<br>`*.zip` | Prevents heavy 33+ MB submission packages and zip archives from bloating git history. |
| **Research Data & Caches** | `/data/raw/`<br>`/data/cache/`<br>`*.h5`<br>`*.h5ad`<br>`/results/stability/partitions/`<br>`/results/stability/runs/` | Human clinical microarrays, SELDI spectra, and patient-indexed partition arrays are strictly excluded from git tracking. |
| **Python Build & Tests** | `__pycache__/`<br>`*.py[cod]`<br>`.pytest_cache/`<br>`.ruff_cache/`<br>`.coverage`<br>`build/`<br>`dist/` | Standard build and test cache artifacts are cleanly excluded. |
| **Virtual Environments** | `.env`<br>`.env.*`<br>`!.env.example`<br>`.venv/`<br>`venv/`<br>`env/` | Local environment variables and virtualenvs are ignored; example template `.env.example` is tracked. |
| **IDE & System Metadata** | `.vscode/`<br>`.idea/`<br>`.DS_Store`<br>`Thumbs.db` | Operating system and IDE configuration artifacts are excluded. |

---

## 3. Git Tracking Verification

- **Tracked Files Inventory:** Exactly **194 files** tracked via `git ls-files`. Zero tracked `.pyc`, zero tracked virtualenv files, zero tracked clinical expression caches.
- **Untracked File Inspection:** Only `Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise.pdf` (7.5 MB reference PDF) is present as an untracked local reference.
- **Verification Command:** `git check-ignore -v data/cache/cns.npz` returns `.gitignore:14:/data/cache/` (Correctly Ignored).
- **Audit Verdict:** **PASSED.**
