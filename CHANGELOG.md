# Changelog

All notable changes to the **CSD (Clustering Stability–Accuracy Discordance)** reproducibility package are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0-rc1] - 2026-11-07

### Added
- **Initial Public Reproducibility Release:** Dedicated companion repository for the research manuscript *An Empirical Analysis of Stability-Accuracy Discordance in High-Dimensional Consensus Clustering: Evidence from Biomedical Cohorts*, prepared for Springer Nature *Data Mining and Knowledge Discovery* (DMKD).
- **Tier 1 Saved-Evidence Reconstruction:** Zero-network, self-contained verification tool (`reproduction/scripts/recompute_saved_stability.py`) recalculating all 62,640 pairwise subsample stability ARIs and 2,160 external ARIs in ~50 seconds.
- **Dataset Rights and Provenance Manifests:** Audited manifests for 4,323 public telemetry/summary records, 4,326 restricted partitions/clinical caches, and 8 source-fetch datasets (`data/manifests/`).
- **Unified Reproduction CLI:** Top-level runner (`scripts/reproduce.py`) for synthetic smoke execution and verification test suites.
- **Verification Test Suite:** 86 unit and integration tests verifying consensus engines, metrics, registry schemas, and CLI integrity.
- **Documentation Suite:** In-depth guides covering research questions, empirical findings, compute requirements, environment configurations, and tiered data governance.
