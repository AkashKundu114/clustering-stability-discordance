# CSD: Clustering Stability-Accuracy Discordance in High-Dimensional Biomedical Data

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests: 82 Unit Tests Passing](https://img.shields.io/badge/tests-82%20passed-brightgreen.svg)](tests/)
[![Code style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Types: Mypy](https://img.shields.io/badge/types-mypy-blue.svg)](https://mypy-lang.org/)

> **CSD** stands for **Clustering Stability-Accuracy Discordance**.
> **Full Manuscript Title:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*
> **Running Header:** *Feature-Gated Bipartite Consensus Under Noise*
> **Authors:** Kalyan Kumar Das (Techno India University), Akash Kundu (Techno India University), Anirban Mukhopadhyay (University of Kalyani)
> **Target Journal:** Springer Nature – *Data Mining and Knowledge Discovery* (DMKD)
> **Authoritative Submission Reference:** Exact 48-page submitted PDF (`Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise.pdf`, SHA-256: `b32259bfd704a7a7e6dd45e5717a731f0d8100d819cfd792911645e7da571a3c`)
> **Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)
> **Companion Repository:** [https://github.com/AkashKundu114/icc-clustering](https://github.com/AkashKundu114/icc-clustering)

---

## 1. Scientific Overview & Core Thesis

This repository (**CSD**) hosts the reproducible research software, saved-evidence verification tools, dataset governance manifests, and documentation for the research manuscript *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*. The investigation evaluates **13 benchmark datasets** (spanning high-dimensional clinical cancer cohorts and multi-domain benchmarks) across **12 comparative clustering algorithms** to investigate whether resampling stability implies external reference-label accuracy under extreme noise ($D \gg N$).

### Core Finding
**Resampling stability and external reference-label accuracy are fundamentally distinct mathematical quantities.** In high-dimensional regimes dominated by distractor noise ($D/N > 20$), unsupervised clustering algorithms repeatedly converge onto mutually agreeing, data-driven noise partitions. These partitions achieve high subsample stability while exhibiting zero or near-zero agreement with external diagnostic ground-truth labels.

---

## 2. Research Questions & Empirical Findings

Across six clinical cancer microarray cohorts ($N = 60\text{--}253$, $D = 2{,}000\text{--}15{,}154$, $D/N = 28\text{--}124$) evaluated over 12 clustering algorithms with 30 subsampling iterations per cell ($62{,}640$ stability comparisons, $2{,}160$ external ARI measurements):

1. **Does subsample stability guarantee external label accuracy in high-dimensional data?**
   *Finding:* No. Unsupervised clustering algorithms repeatedly achieve subsample stability $\ge 0.50$ (up to $0.996$ for Ward on Prostate) while empirical Adjusted Rand Index (ARI) against clinical annotations collapses to chance (grand mean external ARI: $0.053$). The unconditional mean stability-accuracy discordance gap across all 72 cells is **$+0.457$** (median **$+0.442$**; historical mean gap $+0.464$).
2. **Do discordant partitions reflect data-driven structure or permutation artifacts?**
   *Finding:* Data-driven structure. Under column-permuted null controls where coordinate covariance is broken, stability collapses to near zero (grand mean $0.007$, actual $0.006608$). Thus, high empirical stability reflects genuine geometric concentration along data-driven coordinates, but along technical or noise axes unrelated to diagnostic classes.
3. **Can modular algorithmic interventions bridge the stability-accuracy gap?**
   *Finding:* Selectively. Using Gated Anchor Consensus (GAC) as an experimental ablation vehicle ($2 \times 2$ factorial), unguided random feature gating ($0.047$) and bipartite anchor graph compression alone ($0.046$) do not improve accuracy over ambient consensus ($0.037$). Unsupervised Bimodality-Gated Subspace Selection (BGSS) selectively recovers signal when informative coordinates possess marginal bimodality (elevating bipartite consensus to $0.217$, net gain $+0.169$ over matched random gating, $p = 0.031$, $n=6$), but yields negligible shifts on diffuse non-bimodal manifolds (Prostate $0.012$, CNS $-0.002$).
4. **Does GAC dominate omnibus benchmarks?**
   *Finding:* No. Across the 13-dataset multi-domain benchmark, the non-parametric Friedman omnibus test yields $\chi_F^2 = 11.556, p = 0.3979 \approx 0.40$ ($\text{df}=11$), failing to reject the null hypothesis of equal performance. All 12 algorithms reside in a **single statistical equivalence clique** ($\text{CD}=4.622 > \Delta_{\max}=2.615$). Simple K-Means ranks #1 omnibus ($5.15$), while GAC ranks #4 ($5.62$). GAC dominates only within the high-dimensional clinical subgroup ($n=6$, Rank 2.17).

---

## 3. Repository Architecture

```text
csd/
├── .github/workflows/ci.yml       # Automated CI (lint, typing, tests, smoke verification)
├── audit/
│   └── submission_reproducibility/# Independent reproducibility audit and link records
├── configs/                       # Algorithm and dataset execution configurations
├── data/
│   ├── dataset_registry.csv       # 13-dataset governance registry with licenses and routes
│   ├── registry.yaml              # Structural registry schemas
│   └── manifests/
│       ├── public_artifacts.csv   # 4,323 verified public telemetry/summary records
│       ├── restricted_artifacts.csv# Restricted partitions and clinical caches
│       └── source_fetch_only.csv  # Direct upstream download sources
├── docs/                          # Comprehensive documentation suite (30+ topics)
│   ├── submitted_manuscript.md    # Mapping for 48-page submitted PDF
│   ├── experiment_catalog.md      # Detailed catalog of EXP-01 through EXP-07
│   ├── result_dictionary.md       # Exact metric definitions and values
│   ├── reproducibility_architecture.md # 4-tier reproduction framework
│   ├── data_rights.md             # Category A, B, and C redistribution classifications
│   ├── experimental_provenance.md # Provenance levels (Authenticated vs Corroborated)
│   └── limitations.md             # Scientific, hardware, and operational boundaries
├── environment/                   # Container and environment lockfiles
├── reproduction/
│   ├── scripts/
│   │   ├── recompute_saved_stability.py  # Tier 2 six-cohort stability recalculation (<60s)
│   │   └── recompute_benchmark_scores.py # Tier 1 13-dataset Friedman rank test (<30s)
│   └── reviewer_guide/            # Step-by-step reviewer instructions
├── scripts/                       # CLI runners (reproduce.py, fetch_data.py, evaluate.py)
├── src/
│   ├── csd/                       # Canonical package namespace
│   ├── icc/                       # Core algorithms, consensus engine, and metrics
│   └── cicc/                      # Conformal inductive consensus modules
├── tests/                         # Test suite (150 collected; 82 unit tests passing)
├── CITATION.cff                   # Citation metadata
├── DATA_AVAILABILITY.md           # Tiered data governance statement
├── ENVIRONMENT.md                 # System requirements and dependency lockfiles
├── EXPERIMENTAL_PROTOCOL.md       # Random seeds, subsample splits, and formulas
├── LICENSE                        # MIT License
├── README.md                      # This document
├── REPRODUCIBILITY.md             # 4-tier reproduction framework
└── THIRD_PARTY_NOTICES.md         # Upstream data licensing and provenance notices
```

---

## 4. Quickstart: Verification & Reproduction

### 4.1 Environment Setup
```powershell
# Clone the canonical repository
git clone https://github.com/AkashKundu114/clustering-stability-discordance.git
cd clustering-stability-discordance

# Create and activate a clean Python 3.10+ virtual environment
python -m venv .venv
# On Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# On Linux/macOS:
source .venv/bin/activate

# Install core and test dependencies
pip install -e ".[dev]"
```

### 4.2 Run Test Suite (Tier 0)
```powershell
python -m pytest tests/unit tests/test_reproduce_cli.py
```
*Expected Result:* **82 unit tests and 4 CLI tests pass in ~85s.**

### 4.3 Tier 1: Aggregate Score Re-Aggregation & Friedman Test
```powershell
python reproduction/scripts/recompute_benchmark_scores.py \
    --scores data/historical_benchmarks/benchmark_matrix_passF.csv data/historical_benchmarks/exp3_cohirf_benchmark.csv \
    --output-dir results/tier1_recomputed
```
*Expected Result:* Re-aggregates 3,000 score rows and verifies $\chi_F^2 = 11.556, p = 0.3979 \approx 0.40$, K-Means Rank 1 ($5.15$), and GAC Rank 4 ($5.62$) in $< 30\text{ seconds}$.

### 4.4 Tier 2: Saved-Partition Subsample Stability Recalculation
```powershell
python reproduction/scripts/recompute_saved_stability.py \
    --data-root /path/to/evidence_bundle \
    --output-dir results/tier2_recomputed
```
*Expected Result:* Recalculates all 62,640 pairwise subsample stability ARIs and 2,160 external ARIs in $< 60\text{ seconds}$ without refitting base models, reproducing grand mean stability ($0.510$), accuracy ($0.053$), gap ($+0.457$), null ($0.007$), Rule (i') 18-cell subset ($+0.715$), and Rule (iii) core ($+0.687$).

---

## 5. Dataset Governance & Rights

To comply with ethical regulations, biobank data-use agreements, and third-party licenses:
- **Category A (Public Open Access — CC BY 4.0):** Sonar, Madelon, ISOLET, 20 Newsgroups, PBMC68k reduced. Fully distributable with attribution.
- **Category B (Source-Fetch-Only — Clinical Microarrays & University Servers):** Human cancer tissue biopsies (CNS, Colon, Leukemia, Ovarian, Prostate, SRBCT) and Indian Pines hyperspectral scene. Patient-indexed raw matrices are not bundled in public git; retrieved dynamically via OpenML API or institutional server.
- **Category C (Restricted Redistribution — Explicit Legal Proscription):** Extended Yale Face Database B (Yale CVC terms prohibit public redistribution in third-party archives). Acquired dynamically via `icc.datasets.image.load_yale_b`.

See [`DATA_AVAILABILITY.md`](DATA_AVAILABILITY.md) and [`docs/data_rights.md`](docs/data_rights.md).

---

## 6. Citation

If you use this codebase or refer to the stability-accuracy discordance findings, please cite:

```bibtex
@article{das2026stability,
  title={Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise},
  author={Das, Kalyan Kumar and Kundu, Akash and Mukhopadhyay, Anirban},
  year={2026},
  journal={Springer Nature Data Mining and Knowledge Discovery (Under Review)},
  note={Submission package v2.0-final-submission}
}

@software{csd2026code,
  author={Das, Kalyan Kumar and Kundu, Akash and Mukhopadhyay, Anirban},
  title={CSD: Clustering Stability-Accuracy Discordance in High-Dimensional Biomedical Data},
  year={2026},
  version={1.0.0-rc2},
  url={https://github.com/AkashKundu114/clustering-stability-discordance},
  note={Companion repository: https://github.com/AkashKundu114/icc-clustering}
}
```

---

## 7. License

This software is distributed under the [MIT License](LICENSE). Third-party datasets remain subject to their respective original licenses and institutional terms.
