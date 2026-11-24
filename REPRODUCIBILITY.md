# Reproducibility Framework & Verification Protocols

**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)
**Submitted Manuscript Reference:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*
**Authors:** Kalyan Kumar Das (Techno India University), Akash Kundu (Techno India University), Anirban Mukhopadhyay (University of Kalyani)
**Audited Baseline Commit:** `44838fa`

---

## 1. Multi-Tier Verification Framework

To enable independent researchers and journal reviewers to inspect, verify, and reproduce the empirical results without reliance on undocumented machine state, the repository defines four structured verification tiers:

| Tier | Focus & Scope | Expected Runtime | Hardware Requirement | Verification Command / Target |
|:---|:---|:---:|:---:|:---|
| **Tier 0** | Software environment, packaging, mathematical unit tests, CLI smoke tests | $< 90\text{ s}$ | 1 CPU, 1 GB RAM | `python -m pytest tests/unit tests/test_reproduce_cli.py` (82 unit tests pass) |
| **Tier 1** | Aggregate multi-domain benchmark re-aggregation, Friedman omnibus test, and average ranks | $< 30\text{ s}$ | 1 CPU, 512 MB RAM | `python reproduction/scripts/recompute_benchmark_scores.py` |
| **Tier 2** | Saved-partition stability verification (4,320 partitions, 62,640 ARIs, 2,160 external ARIs, 72 cells) | $< 60\text{ s}$ | 1 CPU, 512 MB RAM | `python reproduction/scripts/recompute_saved_stability.py` |
| **Tier 3** | Fresh end-to-end experimental reproduction from raw datasets | Hours to days | 8+ cores, 16+ GB RAM, GPU | Feasible on 6 microarrays; large-$N$ benchmarks bounded by 16 GB host RAM |

---

## 2. Tier Execution Walkthrough

### Tier 0: Algorithmic & Software Verification
Verifies package installation, CLI entry points, and algorithmic fidelity:
```powershell
# Install package in editable development mode
python -m pip install -e ".[dev]"

# Execute unit and CLI tests
python -m pytest tests/unit tests/test_reproduce_cli.py
```
*Expected Outcome:* 82 unit tests and 4 CLI tests pass with zero warnings in $\approx 85\text{ seconds}$.

### Tier 1: Aggregate Score Re-Aggregation & Friedman Test
Re-aggregates the 3,000 historical score rows across all 156 cells ($13 \text{ datasets} \times 12 \text{ methods}$):
```powershell
python reproduction/scripts/recompute_benchmark_scores.py \
    --scores data/historical_benchmarks/benchmark_matrix_passF.csv data/historical_benchmarks/exp3_cohirf_benchmark.csv \
    --output-dir results/tier1_benchmark
```
*Expected Outcome:* Outputs `benchmark_recalculation.json` and verifies Friedman test statistic $\chi_F^2 = 11.556, \text{df}=11, p = 0.3979 \approx 0.40$, K-Means Rank 1 ($5.15$), and GAC Rank 4 ($5.62$).

### Tier 2: Saved-Partition Subsample Stability Recalculation
Recomputes pairwise stability, external diagnostic accuracy, and degeneracy rules from the precomputed partition bundle:
```powershell
python reproduction/scripts/recompute_saved_stability.py \
    --data-root /path/to/evidence_bundle \
    --output-dir results/tier2_stability
```
*Expected Outcome:* Cryptographically verifies input hashes and outputs `recomputation_summary.json` and `recomputed_cells.csv` in $\approx 45\text{ seconds}$:
- Fresh Grand Mean Stability ($\bar{S}$): `0.509812` (`0.510`)
- Fresh Grand Mean External ARI ($\bar{A}$): `0.052522` (`0.053`)
- Fresh Mean Discordance Gap ($\bar{\Delta}$): `+0.457289` (`+0.457`, median `+0.442`)
- Permuted Null Stability ($\bar{S}_{\text{null}}$): `0.006608` (`0.007`)
- Rule (i') Non-Degenerate 18-cell Subset Gap: `+0.714644` (`+0.715`)
- Rule (iii) Multi-Cohort 9-cell Core Gap: `+0.686617` (`+0.687`)

### Tier 3: Fresh End-to-End Experimental Reproduction
- **Six High-Dimensional Microarray Cohorts ($n=6$):** 100% complete in modern clean execution across 4,320 model fits. 3,960 partitions are 100% byte-for-byte identical to historical archives; 221 DEC partitions exhibit known optimization protocol divergence.
- **Large-Sample Multi-Domain Benchmarks ($N > 2400$):** Exactly 892 of 1,430 planned unique fits completed in the modern clean environment; 538 fits were halted due to $O(N^2)$ host RAM exhaustion on dense consensus matrix operations on a 16 GB workstation.

---

## 3. Documentation Pointers

- Reviewer Quickstart: [`reproduction/reviewer_guide/quick_verification.md`](reproduction/reviewer_guide/quick_verification.md)
- Complete Reviewer Guide: [`docs/reviewer-reproduction.md`](docs/reviewer-reproduction.md)
- Experimental Protocols: [`EXPERIMENTAL_PROTOCOL.md`](EXPERIMENTAL_PROTOCOL.md)
- Dataset Rights: [`DATA_AVAILABILITY.md`](DATA_AVAILABILITY.md) and [`docs/data_rights.md`](docs/data_rights.md)
- Scientific Boundaries: [`docs/limitations.md`](docs/limitations.md)
