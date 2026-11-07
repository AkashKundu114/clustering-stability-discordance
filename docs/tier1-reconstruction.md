# Tier 1: Saved-Evidence Reconstruction Guide

**Document:** `docs/tier1-reconstruction.md`  
**Date:** 2026-11-07  
**Project:** Stability-Accuracy Discordance in High-Dimensional Consensus Clustering  
**Target Journal:** Springer Nature — *Data Mining and Knowledge Discovery* (DMKD)

---

## 1. What Tier 1 Reconstructs

Tier 1 is a self-contained, zero-network-exposure evaluation protocol designed specifically for journal editors and peer reviewers. It mathematically re-evaluates all empirical metrics directly from validated partition arrays and per-fit metadata logs:

- Validates all $4{,}320$ partition integer arrays (`.npy`).
- Validates all $4{,}320$ execution telemetry records (`.parquet`).
- Recalculates all $62{,}640$ pairwise subsample stability ARIs ($31{,}320$ real $+ 31{,}320$ null).
- Recalculates all $2{,}160$ external ARI measurements against diagnostic truth.
- Computes mean and median discordance gaps across all 72 experimental cells.
- Evaluates non-degeneracy conditions (Rule i', Rule ii, Rule iii).
- Verifies aggregate agreement with committed baseline summary tables down to double-precision floating-point limits ($< 1.11 \times 10^{-16}$).

---

## 2. System Requirements

- **Processor:** Any modern CPU (1 core is sufficient).
- **RAM:** $< 512\text{ MB}$.
- **GPU:** None required.
- **Runtime:** **~38–53 seconds** on standard laptop workstations.
- **Dependencies:** Standard Python stack:
  ```bash
  pip install numpy scipy pandas scikit-learn
  ```

---

## 3. Step-by-Step Execution

1. Obtain the authorized reviewer evidence bundle (`partitions/` and `runs/`).
2. Run the committed recomputation CLI:
   ```bash
   python reproduction/scripts/recompute_saved_stability.py \
       --data-root /path/to/evidence_bundle \
       --output-dir results/recomputed_tier1
   ```
3. Verify the generated output manifest and summary:
   ```json
   {
     "counts": {
       "partition_files": 4320,
       "per_fit_records": 4320,
       "cells": 72,
       "real_pairwise_ari": 31320,
       "null_pairwise_ari": 31320,
       "partition_duplicate_hash_groups": 140,
       "validation_errors": 0
     },
     "summary": {
       "mean_stability": 0.509812,
       "mean_external_ari": 0.052522,
       "mean_gap": 0.457289,
       "median_gap": 0.442304,
       "mean_null_stability": 0.006608
     }
   }
   ```
4. Output files created:
   - `results/recomputed_tier1/recomputation_summary.json` (Full per-cell breakdown and aggregate metrics).
   - `results/recomputed_tier1/recomputed_cells.csv` (CSV table of all 72 cells).
   - `results/recomputed_tier1/output_manifest.json` (SHA-256 hashes of generated artifacts).
