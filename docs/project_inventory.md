# Project Inventory & Baseline Repository Audit

**Document:** `docs/project_inventory.md` 
**Date:** 2026-11-07 
**Branch:** `release-finalisation` 
**Base Commit:** `aa9f716d887ac94ca51792d37b310187c8da3231` 
**Primary Goal:** Comprehensive co-author-review preparation, public reproducibility repository engineering, dataset rights governance, and submission package construction.

---

## 1. Current Git Repository State

- **Repository Origin:** `https://github.com/AkashKundu114/icc-clustering.git`
- **Active Branch:** `release-finalisation` (branched from `main` at `aa9f716`)
- **Main HEAD Commit:** `aa9f716d887ac94ca51792d37b310187c8da3231` ("Document provenance and harden Yale B downloads")
- **Tags Present:** `v1.0.0`, `v2.0.0`, `v2.1.0`, `v2.2.0`, `v2.2.1`, `v2.2.2`
- **Visibility:** Private (transitioning toward public candidate `clustering-stability-discordance`)
- **Untracked Historical Documentation Files at Start of Finalisation:**
 - `COMPUTE_REQUIREMENTS.md` (2,440 bytes)
 - `DATA_AVAILABILITY.md` (5,265 bytes)
 - `REPRODUCIBILITY.md` (3,369 bytes)
 - `data/dataset_registry.csv` (5,449 bytes)
 - `docs/reviewer_reproduction.md` (4,359 bytes)

---

## 2. Directory & Component Layout

```text
csd/
├── .github/ # Issue templates and GitHub workflows
├── audit/ # Comprehensive forensic audit reports (loops 1 to 6.6.1)
│ ├── loop6_6/ # Loop 6.6 baseline reports, patches, and artifact manifests
│ ├── loop6_6_1/ # Loop 6.6.1 clean-clone acceptance & metric reconciliation reports
│ └── finalisation/ # Phase 10 integration and acceptance reports (this execution)
├── configs/ # Model, algorithm, and benchmark YAML configurations
├── data/ # Dataset manifests, registry, and local cache pointers
│ ├── dataset_registry.csv
│ └── manifests/ # Public, restricted, and source-fetch-only file manifests
├── docs/ # Authoritative documentation suite (27+ topics)
├── environment/ # Reproducible environment specifications (conda, docker, lockfiles)
├── paper/ # Manuscript sources, figures, tables, and co-author review drafts
│ ├── manuscript/ # Baseline manuscript (immutable backup preserved)
│ ├── review/ # Co-author review working copy and revision records
│ ├── figures/ # High-resolution vector and raster publication figures
│ └── tables/ # Generated LaTeX table inputs
├── reproduction/ # Zero-dependency and independent arithmetic reproduction scripts
│ └── scripts/
│ ├── recompute_saved_stability.py
│ └── recompute_benchmark_scores.py
├── results/ # Aggregated evaluation metrics, telemetry, and figures
├── scripts/ # Dataset fetchers, CLI runners, and utility scripts
├── src/ # Core package source (`icc` and `cicc`)
├── submission/ # Dedicated journal submission package
│ └── journal/ # LaTeX source, title page, declarations, reviewer guides
└── tests/ # Unit, integration, regression, and CLI test suites
```

---

## 3. Manuscript Baseline State

- **Primary Source:** `paper/manuscript/main.tex` (Length: 125,503 bytes)
- **Immutable Backup Hash (SHA-256):** `c12c945878a0f616cad4f1243f05e18ce4040b9e9219d4cef49049a27c461742` (Stored at `audit/finalisation/backup/main.tex.orig`)
- **Bibliography:** `paper/manuscript/references.bib` (SHA-256: `773e7cf911e4b073da02f1afc9da0dabec29967541ebca4c471349f67b12fb7c`)
- **Document Class:** `sn-jnl.cls` (Journal LaTeX template)
- **Title:** *An Empirical Analysis of Stability-Accuracy Discordance in High-Dimensional Consensus Clustering: Evidence from Biomedical Cohorts*
- **Authors:** Kalyan Kumar Das, Akash Kundu, Anirban Mukhopadhyay

---

## 4. Primary Data & Evidence Locations

1. **Author Evidence Archive:**
 - Location: `results/stability/`
 - Partitions: 4,320 `.npy` array files ($72\text{ cells} \times 30\text{ subsamples} \times 2\text{ modes}$)
 - Run Telemetry: 4,320 `.parquet` execution metadata files
 - Summaries: `subsample_stability_summary.csv` (Mean stability: `0.516586`), `real_data_stability_summary.csv`
2. **Benchmark Historical Results:**
 - Location: `results/benchmark/benchmark_matrix_passF.csv` and `exp3_cohirf_benchmark.csv`
 - Total rows: 3,000 assembled historical score records from 1,430 planned fits
 - Completed fresh fits: 892 / 1,430 (538 incomplete, frozen due to 16 GB host memory limit)
3. **Clinical Microarray Caches:**
 - Location: `data/cache/*.npz` (6 files: CNS, Colon, Leukemia, Ovarian, Prostate, SRBCT)

---

## 5. Test Suite & Verification Toolchain

- **Unit Tests:** `python -m pytest tests/unit` - **72 passed in 88.70s**
- **CLI Reproduction Tests:** `python -m pytest tests/test_reproduce_cli.py` - **4 passed in 4.80s**
- **Tier 1 Saved-Partition Recomputation:** `python reproduction/scripts/recompute_saved_stability.py` - **Verified in ~50s**:
 - Partition count: 4,320
 - Per-fit records: 4,320
 - Cells: 72
 - Real pairwise comparisons: 31,320
 - Null pairwise comparisons: 31,320
 - Total pairwise evaluations: 62,640
 - External ARI observations: 2,160
 - Recomputed metrics match historical records to $< 1.11 \times 10^{-16}$.
- **Benchmark Recomputation:** `python reproduction/scripts/recompute_benchmark_scores.py` - **Verified in ~2s**:
 - Rows: 3,000
 - Friedman statistic: $\chi_F^2 = 11.556, p = 0.3979$ ($p \approx 0.40$), $\text{df}=11$.

---

## 6. Files That Must NEVER Enter the Public Repository

The following files contain patient-linked clinical indices, sensitive face imagery, or university-restricted raw data and are strictly classified as `CONFIDENTIAL_REVIEWER_PACKAGE` or `RESTRICTED`:

1. **Partition Arrays ($4{,}320$ files):** `results/stability/partitions/*.npy` (contain 1D index cluster assignments mapped to clinical patient tumor samples).
2. **Clinical Microarray Caches ($6$ files):** `data/cache/*.npz` (CNS, Colon, Leukemia, Ovarian, Prostate, SRBCT patient gene expression spectra).
3. **Raw Extended Yale Face Database B Images:** `CroppedYaleB.zip` or unpacked `.pgm` arrays (redistribution prohibited under Yale CVC terms of use).
4. **Indian Pines Raw Hyperspectral Scene:** `Indian_pines_corrected.mat` (direct fetch only from UPV/EHU repository).
5. **Private Credentials, API Keys, or Personal Correspondence:** Zero credentials detected; all such paths are excluded via `.gitignore`.

---

## 7. Known Blockers and External Clearances

1. **Native LaTeX Toolchain:**
 - Status on local workstation: Native `pdflatex` / `latexmk` not installed on Windows PATH; Docker daemon not running.
 - Per Section 12.2 of project guidelines: Status honestly documented as `NOT_COMPILED`. Comprehensive tested compilation commands, Dockerfile, and pre-compiled historical PDF references (`audit/loop6_3/manuscript_pdf_20261102/main.pdf`) provided.
2. **Third-Party Redistribution Clearances:**
 - Extended Yale Face Database B: Formal written clearance request drafted to Yale CVC (`cvc-support@cs.yale.edu`); redistribution currently prohibited.
 - Indian Pines: Formal inquiry drafted to UPV/EHU (`manuel.grana@ehu.eus`); direct university fetch supported.
3. **Human Publication Gates:**
 - Author details, affiliations, ORCIDs, and formal approval must be signed off by human co-authors before journal submission or public repository release.
