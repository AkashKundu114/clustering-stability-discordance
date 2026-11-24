# Changelog

All notable changes to the **CSD (Clustering Stability-Accuracy Discordance)** reproducibility package are documented here.

- **Manuscript Title:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*
- **Running Header:** *Feature-Gated Bipartite Consensus Under Noise*
- **Authors:** Kalyan Kumar Das, Akash Kundu, Anirban Mukhopadhyay
- **Journal:** Springer Nature - *Data Mining and Knowledge Discovery* (DMKD)
- **Status:** Under review
- **Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)
- **Benchmark Scope:** 13 benchmark datasets and 12 comparative clustering algorithms.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0-rc2] - 2026-11-24

### Added
- Top-level `csd` package alias (`src/csd/__init__.py`) re-exporting core clustering and conformal modules.
- Restored root documentation links (`DATA_AVAILABILITY.md`, `ENVIRONMENT.md`, `REPRODUCIBILITY.md`).
- Added Contributor Covenant Code of Conduct and Contributing guidelines.
- Standardized four-tier reproducibility audit framework under `audit/`.

### Fixed
- Fixed root `Dockerfile` path for locked requirements (`environment/requirements-lock.txt`).
- Fixed cross-platform console handle error in reproduction CLI tests.
- Synchronized author sequence with submitted manuscript title page across metadata.
- Updated `scripts/run.py` and `scripts/reproduce.py` with repository-root independent path resolution.
- Sanitized local development paths and removed residual coverage artifacts.

## [1.0.0-rc1] - 2026-11-07

### Added
- **Initial Public Reproducibility Release:** Dedicated companion repository for the research manuscript *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*, prepared for peer-reviewed journal.
- **Tier 1 Saved-Evidence Reconstruction:** Zero-network, self-contained verification tool (`reproduction/scripts/recompute_saved_stability.py`) recalculating all 62,640 pairwise subsample stability ARIs and 2,160 external ARIs in ~50 seconds.
- **Dataset Rights and Provenance Manifests:** Audited manifests for 4,323 public telemetry/summary records, 4,326 restricted partitions/clinical caches, and 8 source-fetch datasets (`data/manifests/`).
- **Unified Reproduction CLI:** Top-level runner (`scripts/reproduce.py`) for synthetic smoke execution and verification test suites.
- **Verification Test Suite:** 86 unit and integration tests verifying consensus engines, metrics, registry schemas, and CLI integrity.
- **Documentation Suite:** In-depth guides covering research questions, empirical findings, compute requirements, environment configurations, and tiered data governance.
