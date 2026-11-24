# Project Inventory & Baseline Repository Audit

**Document:** `docs/project_inventory.md`
**Date:** November 2026
**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)
**Package Version:** `1.0.0-rc2`
**Base Commit:** `44838faec32b051d40b31b6e556ecac205008549`

---

## 1. Current Git Repository State

- **Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)
- **Manuscript Title:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*
- **Running Header:** *Feature-Gated Bipartite Consensus Under Noise*
- **Authors:** Kalyan Kumar Das (Techno India University), Akash Kundu (Techno India University), Anirban Mukhopadhyay (University of Kalyani)
- **Journal:** Springer Nature - *Data Mining and Knowledge Discovery* (DMKD)
- **Status:** Under review
- **Tracked Files:** 194 files
- **Python Compatibility:** Python `>=3.10` (Tested on Python 3.10 through Python 3.14.6 64-bit AMD64)
- **Active Test Suite:** 150 total tests collected; all 82 unit tests passing in $\approx 85\text{ seconds}$

---

## 2. Submitted Manuscript Reference

The authoritative reference for all submitted claims, formulas, tables, figures, and limitations is the exact 48-page submitted manuscript PDF:
- **File Name:** `Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise.pdf`
- **Page Count:** 48 pages (35-page main paper + 13-page electronic supplementary material)
- **File Size:** 7,528,380 bytes
- **SHA-256 Checksum:** `b32259bfd704a7a7e6dd45e5717a731f0d8100d819cfd792911645e7da571a3c`
- **Submission Date:** November 19, 2026

---

## 3. Directory & Component Layout

```text
csd/
├── .editorconfig                          # Cross-editor formatting specifications
├── .env.example                           # Template for environment variables
├── .gitattributes                         # Repository line ending configuration
├── .gitignore                             # Ignore rules for private data and build caches
├── .zenodo.json                           # Zenodo release and citation metadata
├── CHANGELOG.md                           # Version release notes and patch history
├── CITATION.cff                           # Academic citation metadata
├── COMPUTE_REQUIREMENTS.md                # Hardware, RAM, and runtime profiles per tier
├── DATA_AVAILABILITY.md                   # Tiered data rights and governance specification
├── Dockerfile                             # Containerized runtime specification
├── ENVIRONMENT.md                         # Dependency stack and environment lockfile notes
├── EXPERIMENTAL_PROTOCOL.md               # Random seeds, subsample schedules, and formulas
├── LICENSE                                # MIT License
├── Makefile                               # Automation shortcuts (lint, test, smoke, clean)
├── README.md                              # Authoritative public entry point and research summary
├── REPRODUCIBILITY.md                     # Tiered reproduction instructions
├── SECURITY.md                            # Security and vulnerability disclosure policy
├── SUPPORT.md                             # User and reviewer support channels
├── THIRD_PARTY_NOTICES.md                 # Attribution notices for datasets and dependencies
├── demo.py                                # Standalone demonstrator on synthetic data
├── pyproject.toml                         # Python packaging configuration and tool settings
├── requirements.txt                       # Core runtime dependencies
├── requirements-dev.txt                   # Developer and test dependencies
│
├── .github/                               # GitHub continuous integration and issue templates
│   ├── dependabot.yml                     # Automated dependency update configuration
│   ├── PULL_REQUEST_TEMPLATE.md           # Template for pull requests
│   ├── ISSUE_TEMPLATE/                    # Bug, feature, and reproducibility inquiry forms
│   └── workflows/ci.yml                   # Automated CI workflow
│
├── audit/                                 # Reproducibility audit records
│   └── submission_reproducibility/
│       └── documentation/                 # Documentation and configuration audit artifacts
│
├── configs/                               # YAML experiment definitions
│   ├── baselines.yaml                     # Hyperparameters for 12 clustering algorithms
│   ├── datasets.yaml                      # Dataset schemas, dimensions, and paths
│   ├── default.yaml                       # Default pipeline configuration
│   └── experiment_defaults.yaml           # Subsampling and seed schedules
│
├── data/                                  # Data governance, registries, and manifests
│   ├── dataset_registry.csv               # 13-dataset registry with licenses and access paths
│   ├── registry.yaml                      # Structural schema definitions for datasets
│   └── manifests/                         # Public, restricted, and source-fetch manifests
│
├── docs/                                  # Comprehensive documentation suite (30+ topics)
├── environment/                           # Conda and requirements lockfiles
├── reproduction/                          # Portable verification scripts (recompute_saved_stability.py)
├── results/                               # Results summaries and smoke test telemetry
├── scripts/                               # CLI utilities and runners (reproduce.py, evaluate.py)
├── src/                                   # Core research software (`icc`, `cicc`, `csd`)
└── tests/                                 # Unit, integration, and regression test suite
```

---

## 4. Primary Empirical Accounting Summary

| Dimension | Scope | Accounting Quantity | Verification Status |
|---|---|---|:---:|
| **Biomedical Cohorts** | CNS, Colon, Leukemia, Ovarian, Prostate, SRBCT | 6 datasets ($D/N = 28\text{--}124$) | `VERIFIED` |
| **Clustering Methods** | K-Means, Ward, Spectral, FCM, StdCons, CoreHalo, FCAG, FastMVC, CoHiRF, UngatedAC, GAC, DEC | 12 comparative algorithms | `VERIFIED` |
| **Primary Cells** | $6 \text{ cohorts} \times 12 \text{ methods}$ | 72 experimental cells | `VERIFIED` |
| **Partition Arrays** | $72 \text{ cells} \times 30 \text{ repeats} \times 2 \text{ modes}$ | 4,320 partition arrays (`.npy`) | `VERIFIED` |
| **Pairwise Comparisons**| $\binom{30}{2} = 435 \text{ pairs/cell} \times 72$ | 31,320 real + 31,320 null = 62,640 | `VERIFIED` |
| **External Diagnostic ARIs**| $72 \text{ cells} \times 30 \text{ subsamples}$ | 2,160 external evaluations | `VERIFIED` |
| **Multi-Domain Benchmark**| 13 datasets $\times 12$ algorithms | 3,000 historical score rows | `VERIFIED` |
| **Fresh Rerun Fits** | Planned unique model fits | 892 / 1,430 fits completed (538 halted: 16 GB RAM ceiling) | `VERIFIED` |

---

## 5. Test Suite & Verification Toolchain

- **Algorithmic & Mathematical Unit Tests:** `python -m pytest tests/unit` - **82 passed in ~85s**
- **CLI Reproduction Tests:** `python -m pytest tests/test_reproduce_cli.py` - **4 passed in ~5s**
- **Full Test Suite:** 150 tests across unit, integration, and regression suites.
- **Tier 1 Saved-Partition Recomputation:** `python reproduction/scripts/recompute_saved_stability.py` - Verified in ~50s.
- **Tier 1 Benchmark Recomputation:** `python reproduction/scripts/recompute_benchmark_scores.py` - Verified in ~10s.
