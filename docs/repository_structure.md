# Repository Structure & Component Architecture

**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)
**Package Name:** `csd` (Version `1.0.0-rc2`)
**Submitted Manuscript Reference:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*
**Audited Baseline Commit:** `44838fa`

---

## 1. Directory Tree

The directory layout of `csd` separates version-controlled research code, configurations, data manifests, reproducibility tooling, test suites, and internal verification documentation:

```text
csd/
├── .editorconfig                          # Cross-editor formatting specifications
├── .env.example                           # Template for optional environment variables
├── .gitattributes                         # Line-ending and repository attributes
├── .gitignore                             # Ignore rules for private data, zips, and build caches
├── .zenodo.json                           # Zenodo release and citation metadata
├── CHANGELOG.md                           # Version release notes and patch history
├── CITATION.cff                           # Authoritative academic citation metadata
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
│   ├── dependabot.yml                     # Dependency update configuration
│   ├── PULL_REQUEST_TEMPLATE.md           # Template for pull requests
│   ├── ISSUE_TEMPLATE/                    # Bug, feature, and reproducibility inquiry forms
│   └── workflows/
│       └── ci.yml                         # Automated CI pipeline (lint, typing, tests, smoke)
│
├── audit/                                 # Reproducibility audit records
│   └── submission_reproducibility/
│       └── documentation/                 # Documentation and configuration audit artifacts
│           ├── documentation_inventory.csv# Complete inventory of all repository doc files
│           ├── documentation_change_log.csv# Traceable change log of updates
│           ├── link_audit.csv             # Automated internal link verification report
│           ├── configuration_audit.md     # Package, CI, and metadata synchronization audit
│           ├── ignore_rules_audit.md      # Comprehensive ignore-rule and tracking audit
│           ├── final_consistency_report.md# Cross-repository numerical consistency verification
│           └── final_reviewer_simulation.md# Clean-clone reviewer simulation log
│
├── configs/                               # YAML experiment definitions
│   ├── baselines.yaml                     # Hyperparameters for 12 clustering algorithms
│   ├── datasets.yaml                      # Dataset schemas, dimensions, and paths
│   ├── default.yaml                       # Default pipeline configuration
│   ├── experiment_defaults.yaml           # Subsampling and seed schedules
│   ├── README.md                          # Configuration guide
│   └── examples/                          # Example configurations for genomics and synthetic runs
│
├── data/                                  # Data governance, registries, and manifests
│   ├── dataset_registry.csv               # 13-dataset registry with licenses and access paths
│   ├── registry.yaml                      # Structural schema definitions for datasets
│   ├── README.md                          # Data access instructions
│   └── manifests/
│       ├── public_artifacts.csv           # 4,323 verified public telemetry/summary records
│       ├── restricted_artifacts.csv       # Restricted partitions and clinical caches
│       └── source_fetch_only.csv          # Direct download pointers for external repositories
│
├── docs/                                  # Comprehensive documentation suite
│   ├── README.md                          # Documentation index
│   ├── api.md                             # Python API reference for csd and icc modules
│   ├── citation.md                        # BibTeX and citation guides
│   ├── compute-requirements.md            # Hardware boundaries and RAM requirements
│   ├── data-dictionary.md                 # Column schemas for data manifests and summaries
│   ├── data-rights-and-licences.md        # Comprehensive dataset rights register
│   ├── data_rights.md                     # Category A, B, and C redistribution classifications
│   ├── datasets.md                        # Dataset profiles, sources, and dimensions
│   ├── datasets-and-provenance.md         # Data lineage and clinical biobank sources
│   ├── environment-setup.md               # Python virtual environment instructions
│   ├── experiment_catalog.md              # Catalog of EXP-01 through EXP-07
│   ├── experimental-protocol.md           # Formal experimental protocols
│   ├── experimental_provenance.md         # Historical vs fresh execution records
│   ├── limitations.md                     # Scientific and operational boundaries
│   ├── methodology.md                     # Methodological premise of discordance
│   ├── project_inventory.md               # Component inventory and baseline metrics
│   ├── provenance.md                      # Provenance levels and audit history
│   ├── release-process.md                 # Release engineering protocol
│   ├── reproducibility.md                 # 4-tier reproduction framework
│   ├── reproducibility_architecture.md    # Multi-tier verification architecture
│   ├── research-overview.md               # Research motivations and questions
│   ├── research-questions.md              # The three core research hypotheses
│   ├── result_dictionary.md               # Dictionary of metrics, rules, and statistics
│   ├── results-and-interpretation.md      # Scientific interpretation of benchmark tables
│   ├── reviewer-reproduction.md           # Step-by-step reviewer verification guide
│   ├── reviewer_reproduction.md           # Cross-link compatibility copy
│   ├── scientific-overview.md             # Theoretical overview of distance concentration
│   ├── setup.md                           # Installation and environment troubleshooting
│   ├── software-architecture.md           # Software architecture and algorithm components
│   ├── statistical-analysis.md            # Statistical tests, bootstrap, and rank procedures
│   ├── submitted_manuscript.md            # Reference documentation for 48-page submitted PDF
│   ├── theory.md                          # Mathematical theorems (Theorem 1, Proposition 1)
│   ├── tier1-reconstruction.md            # Saved-output recomputation instructions
│   ├── tier2-experiment-status.md         # Memory boundaries and Tier 2 feasibility
│   └── troubleshooting.md                 # Common errors, platform quirks, and workarounds
│
├── environment/                           # Reproducibility environment specifications
│   ├── Dockerfile                         # Container build instructions
│   ├── environment.yml                    # Conda environment definition
│   ├── requirements-lock.txt              # Frozen dependency lockfile
│   └── versions.json                      # Reference package versions
│
├── reproduction/                          # Portable verification scripts
│   ├── README.md                          # Instructions for running saved-evidence verification
│   ├── claim-to-evidence-matrix.csv       # Claim-to-evidence cross-reference table
│   ├── numerical_comparison_report.md     # Comparison between historical and fresh metrics
│   ├── environment/
│   │   └── win-py314-requirements-lock.txt# Windows Python 3.14 lockfile
│   ├── reviewer_guide/
│   │   └── quick_verification.md          # 50-second quick verification walkthrough
│   └── scripts/
│       ├── recompute_saved_stability.py   # Pure-NumPy six-cohort stability recalculation
│       └── recompute_benchmark_scores.py  # 13-dataset Friedman rank and score re-aggregation
│
├── results/                               # Execution summaries and test telemetry
│   ├── README.md                          # Results directory guide
│   └── experiments/                       # Telemetry JSON records from smoke tests
│
├── scripts/                               # CLI utilities and runners
│   ├── README.md                          # Scripts documentation
│   ├── evaluate.py                        # Standalone partition evaluation tool
│   ├── fetch_data.py                      # Dynamic dataset downloader
│   ├── prepare_data.py                    # Unsupervised preprocessing pipeline
│   ├── reproduce.py                       # Top-level reproduction CLI runner
│   ├── run.py                             # Experiment orchestration script
│   └── validate_registry_and_release_metadata.py # Metadata validator
│
├── src/                                   # Core research software
│   ├── cicc/                              # Conformal inductive consensus clustering
│   ├── csd/                               # Canonical package namespace
│   └── icc/                               # Primary consensus algorithms and evaluation tools
│
└── tests/                                 # Test suite (150 total tests collected)
    ├── README.md                          # Test suite execution guide
    ├── test_reproduce_cli.py              # CLI smoke and argument validation tests
    ├── integration/                       # Dataset discovery, loaders, and pipeline tests
    ├── regression/                        # Numerical fidelity and compatibility tests
    └── unit/                              # Algorithmic and mathematical unit tests (82 tests)
```

---

## 2. Component Responsibilities

1. **`src/icc/`:** Contains core implementations of Gated Anchor Consensus (`InvariantCoreConsensusV2`), Bimodality-Gated Subspace Selection (`BGSS`), classical baselines (`kmeans`, `spectral`, `ward`, `fcm`, `stdcons`), and the partition evaluation metrics.
2. **`reproduction/scripts/`:** Zero-dependency, pure-NumPy verification tools designed to run in $< 60$ seconds on saved partition bundles, verifying all 62,640 pairwise stability ARIs and computing Friedman rank tests.
3. **`data/manifests/`:** Explicit integrity manifests recording file paths, byte sizes, and SHA-256 hashes of all public and restricted research artifacts.
4. **`docs/`:** Authoritative documentation covering the submitted manuscript, experimental protocols, dataset rights, limitations, and mathematical formulations.
5. **`audit/`:** Permanent version-controlled audit records verifying documentation inventory, link integrity, ignore rules, and reviewer simulation logs.
