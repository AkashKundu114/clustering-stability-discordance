# Reproducibility Architecture & Verification Tiers

**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)
**Submitted Manuscript Reference:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*
**Audited Baseline Commit:** `44838fa`

To ensure that independent researchers can inspect, verify, and reproduce the empirical findings without reliance on undocumented machine state, the repository defines four structured reproduction tiers.

---

## 1. Tier Overview Matrix

| Tier | Name | Target Scope | Required Artifacts | Expected Runtime | Target Audience |
|---|---|---|---|---|---|
| **Tier 0** | Software Environment & Unit Tests | Package installation, imports, unit tests, CLI smoke tests | Repository source only | $< 90\text{ seconds}$ | Any researcher |
| **Tier 1** | Aggregate Score Verification | Recompute Table 6, average ranks, Friedman omnibus test, and Nemenyi CD | Publicly documented score tables | $< 30\text{ seconds}$ | Reviewers & meta-analysts |
| **Tier 2** | Saved-Partition Verification | Recompute all 62,640 pairwise stability values, external ARIs, degeneracy rules | Precomputed partition bundle | $< 60\text{ seconds}$ | Audit reviewers |
| **Tier 3** | Fresh End-to-End Rerun | Re-execute base clustering algorithms, subsampling, and null controls | Raw datasets + hardware cluster | Hours to days (RAM bounded) | System replicators |

---

## 2. Detailed Tier Specifications

### Tier 0 - Software Environment & Algorithmic Fidelity
- **What it verifies:** Package installation, CLI entry points, mathematical correctness of bimodality scoring, bipartite Laplacian construction, spectral embedding, and algorithm wrappers.
- **Execution:**
  ```powershell
  python -m pip install -e ".[dev]"
  python -m pytest tests/unit tests/test_reproduce_cli.py
  ```
- **Expected Outcome:** 82 unit tests pass in $\approx 85\text{ seconds}$. 0 test failures.

### Tier 1 - Aggregate Benchmark Score Verification
- **What it verifies:** Recomputes the multi-domain benchmark arithmetic, per-method mean ARIs, cross-dataset ranks, Friedman test statistic ($\chi_F^2 = 11.556, p = 0.3979 \approx 0.40$), and Nemenyi critical difference ($\text{CD} = 4.622$) across all 156 cells ($13 \times 12$).
- **Tool:** `reproduction/scripts/recompute_benchmark_scores.py`
- **Execution:**
  ```powershell
  python reproduction/scripts/recompute_benchmark_scores.py \
      --scores /path/to/benchmark_matrix_passF.csv /path/to/exp3_cohirf_benchmark.csv \
      --output-dir results/recomputed_benchmark
  ```
- **What it does not verify:** Does not authenticate the execution timestamps or environments of the original historical fits; verifies numerical arithmetic and rank tests.

### Tier 2 - Saved-Partition Stability Verification
- **What it verifies:** Loads all 4,320 saved partition arrays (`.npy`), recomputes all 31,320 real pairwise stability ARIs, all 31,320 column-permuted null ARIs, all 2,160 external diagnostic ARIs, and checks the 5% cluster degeneracy criterion across all 72 cells.
- **Tool:** `reproduction/scripts/recompute_saved_stability.py`
- **Execution:**
  ```powershell
  python reproduction/scripts/recompute_saved_stability.py \
      --data-root /path/to/evidence_bundle \
      --output-dir results/recomputed_stability
  ```
- **Expected Outcome:** Reproduces fresh grand mean stability ($0.510$), accuracy ($0.053$), gap ($+0.457$), null stability ($0.007$), Rule (i') 18-cell subset ($+0.715$), and Rule (iii) 9-cell core ($+0.687$).

### Tier 3 - Fresh Experimental Reproduction & Hardware Boundaries
- **What it verifies:** Full re-execution of clustering pipelines on raw or preprocessed datasets, generating fresh partitions, computing pairwise stability, and re-fitting all models.
- **Feasibility & Hardware Bounds:**
  - *High-Dimensional Microarrays ($n=6$):* 100% feasible on standard workstations (completed on 2026-11-02 in $\approx 4\text{ hours}$).
  - *Large-Sample Benchmarks ($N > 2400$):* Standard dense consensus and spectral decomposition require dense $N \times N$ matrices ($18{,}846 \times 18{,}846$ on 20 Newsgroups requires $2.84\text{ GB}$ per matrix; $68{,}579 \times 68{,}579$ on PBMC68k requires $37.6\text{ GB}$). Reruns on standard 16 GB workstations trigger memory paging and OS freezes. Exactly 892 of 1,430 unique fits were completed in the fresh environment; 538 fits were halted due to memory limits.
