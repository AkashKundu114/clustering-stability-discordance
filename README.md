# CSD: Clustering Stability-Accuracy Discordance in High-Dimensional Biomedical Data

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests: 86 Passing](https://img.shields.io/badge/tests-86%20passed-brightgreen.svg)](tests/)
[![Code style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Types: Mypy](https://img.shields.io/badge/types-mypy-blue.svg)](https://mypy-lang.org/)

> **CSD** stands for **Clustering Stability-Accuracy Discordance**.  
> **Full Manuscript Title:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*  
> **Running Header:** *Feature-Gated Bipartite Consensus Under Noise*  
> **Authors:** Kalyan Kumar Das (Techno India University), Akash Kundu (Techno India University), Anirban Mukhopadhyay (University of Kalyani)  
> **Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)  
> **Companion Repository:** [https://github.com/AkashKundu114/icc-clustering](https://github.com/AkashKundu114/icc-clustering)

---

## 1. Scientific Summary and Core Thesis

This repository (**CSD**) hosts the reproducible research code, saved-evidence reconstruction tools, dataset governance manifests, and documentation for the research manuscript *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise* (Running header: *Feature-Gated Bipartite Consensus Under Noise*). The investigation empirically evaluates **13 benchmark datasets** (spanning high-dimensional biomedical cohorts and multi-domain benchmarks) across **12 comparative clustering algorithms** to investigate whether resampling stability implies external reference-label accuracy in high-dimensional biomedical data ($D \gg N$).

### Core Finding
**Resampling stability and external reference-label alignment are fundamentally distinct mathematical quantities.** In high-dimensional regimes with extreme noise ($D/N > 20$), unsupervised clustering algorithms can repeatedly converge onto mutually agreeing, data-driven noise partitions. These partitions achieve high subsample stability while exhibiting zero or near-zero agreement with external diagnostic or biological ground-truth labels.

---

## 2. Research Questions and Empirical Evidence

Across six clinical cancer microarray cohorts ($N = 60\text{-}102$, $D = 2{,}000\text{-}12{,}600$, $D/N = 32\text{-}201$) evaluated over 12 clustering algorithms with 30 subsampling iterations per cell:

1. **Does subsample stability guarantee external label accuracy in high-dimensional data?**  
   *Finding:* No. Base clustering algorithms repeatedly achieve subsample stability $\ge 0.50$ (and up to $0.996$) while empirical Adjusted Rand Index (ARI) against clinical annotations collapses to chance (mean external ARI: $0.052522$). The mean stability-accuracy gap across all 72 cells is $+0.457289$ (median $+0.442304$).
2. **Do discordant partitions reflect data-driven structure or trivial permutation artifacts?**  
   *Finding:* Data-driven structure. Under column-permuted null controls where feature-feature covariance is broken, stability collapses to near zero ($-0.003$ to $+0.049$, grand mean $0.006608$). Thus, high stability reflects true geometric concentration in the sample space, but along technical or noise axes unrelated to diagnostic classes.
3. **Can modular algorithmic interventions bridge the stability-accuracy gap?**  
   *Finding:* Selectively. Using Gated Anchor Consensus (GAC) as an experimental ablation vehicle, we find that random feature gating and bipartite anchor graph compression alone do not improve accuracy. Unsupervised Bimodality-Gated Subspace Selection (BGSS) selectively recovers signal when informative coordinates possess multimodal marginals (for example, Leukemia and SRBCT), but fails when signal is diffuse or non-bimodal (for example, Prostate and CNS).

---

## 3. Repository Architecture

```text
csd/
├── .github/workflows/ci.yml       # Automated CI (lint, typing, tests, smoke verification)
├── configs/                       # Algorithm and dataset execution configurations
├── data/
│   ├── dataset_registry.csv       # 19-dataset governance registry
│   ├── registry.yaml              # Structural registry schemas
│   └── manifests/
│       ├── public_artifacts.csv   # 4,323 audited public telemetry/summary records
│       ├── restricted_artifacts.csv# 4,326 restricted files (partitions and clinical caches)
│       └── source_fetch_only.csv  # Direct upstream download sources (GEO, ArrayExpress)
├── docs/                          # Scientific and reproduction documentation
├── reproduction/
│   ├── scripts/
│   │   ├── recompute_saved_stability.py  # Tier 1 six-cohort stability recalculation
│   │   └── recompute_benchmark_scores.py # Tier 1 13-dataset benchmark recalculation
│   └── reviewer_guide/            # Step-by-step reviewer instructions
├── scripts/
│   ├── reproduce.py               # Top-level reproduction CLI runner
│   ├── evaluate.py                # Partition evaluation script
│   └── validate_registry_and_release_metadata.py
├── src/
│   ├── icc/                       # Core algorithms, consensus engine, and metrics
│   └── cicc/                      # Conformal inductive consensus modules
├── tests/                         # Unit, integration, and CLI test suite (86 tests)
├── CITATION.cff                   # Citation metadata
├── DATA_AVAILABILITY.md           # Tiered data governance statement
├── ENVIRONMENT.md                 # System requirements and dependency lockfiles
├── LICENSE                        # MIT License
├── README.md                      # This document
├── REPRODUCIBILITY.md             # Tier 1 reconstruction protocols
└── THIRD_PARTY_NOTICES.md         # Upstream data licensing and provenance notices
```

---

## 4. Quickstart: Verification and Reproduction

### 4.1 Environment Setup
```bash
# Clone the repository
git clone https://github.com/AkashKundu114/clustering-stability-discordance.git
cd clustering-stability-discordance

# Create and activate a clean Python 3.10+ virtual environment
python -m venv venv
# On Linux/macOS:
source venv/bin/activate
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# Install core and test dependencies
pip install -e ".[dev]"
```

### 4.2 Run Test Suite
```bash
python -m pytest tests/unit tests/test_reproduce_cli.py
```
*Expected result:* 86 passed in ~50s.

### 4.3 Run Synthetic Smoke Workflow
```bash
python scripts/reproduce.py --scope smoke
```

### 4.4 Tier 1 Saved-Evidence Reconstruction
For reviewers with access to the authorized partition bundle:
```bash
python reproduction/scripts/recompute_saved_stability.py \
    --data-root /path/to/evidence_bundle \
    --output-dir results/recomputed_tier1
```
*Output:* Recalculates all 62,640 pairwise subsample stability ARIs and 2,160 external ARIs in ~50 seconds without refitting base models.

---

## 5. Dataset Governance and Ethics

In compliance with standard research data policies, this repository implements a four-tiered data governance model:
* **Tier A (Committed):** Synthetic benchmark configurations, analysis code, evaluation manifests.
* **Tier B (Source-Fetch):** Public open-access datasets (UCI, CuratedMicroarrayData) fetched via deterministic scripts with SHA-256 verification.
* **Tier C (Restricted / Academic Non-Commercial):** Yale Face Database B and UPV/EHU Lung Cancer (non-redistributable); original download links and acquisition instructions provided.
* **Tier D (Confidential Reviewer Package):** Precomputed partition arrays (`.npy`) and clinical caches (`.npz`) available to reviewers under confidential academic peer-review terms.

See [`DATA_AVAILABILITY.md`](DATA_AVAILABILITY.md) and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) for complete details.

---

## 6. Citation

If you use this codebase or refer to the stability-accuracy discordance findings, please cite:

```bibtex
@article{das2026stability,
  title={Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise},
  author={Das, Kalyan Kumar and Kundu, Akash and Mukhopadhyay, Anirban},
  year={2026},
  journal={arXiv preprint},
  note={Under review}
}

@software{csd2026code,
  author={Das, Kalyan Kumar and Kundu, Akash and Mukhopadhyay, Anirban},
  title={CSD: Clustering Stability-Accuracy Discordance in High-Dimensional Biomedical Data},
  year={2026},
  url={https://github.com/AkashKundu114/clustering-stability-discordance},
  note={Companion repository: https://github.com/AkashKundu114/icc-clustering}
}
```

---

## 7. License

This repository is distributed under the [MIT License](LICENSE). Third-party datasets and benchmarks remain subject to their respective original licenses and terms.
