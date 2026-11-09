# Reviewer Reproduction Guide: Peer-Reviewed Journal

**Manuscript Title:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*  
**Running Header:** *Feature-Gated Bipartite Consensus Under Noise*  
**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)  
**Companion Repository:** [https://github.com/AkashKundu114/icc-clustering](https://github.com/AkashKundu114/icc-clustering) 
**Authors:** Kalyan Kumar Das, Akash Kundu, Anirban Mukhopadhyay 

---

## Dear Reviewer,

Thank you for reviewing our manuscript. We have engineered this repository so that you can independently audit and verify every numerical claim and statistical calculation in our paper with minimal effort, zero network exposure, and within **less than 60 seconds** on your everyday laptop.

---

## 1. Fast Track: 40-Second Verification of Core Claims

The central scientific contribution of our paper is the demonstration that **subsample stability does not imply clustering accuracy on high-dimensional biomedical cohorts ($D/N > 20$)**.

To independently verify the complete empirical foundation:
- $4{,}320$ partition arrays
- $4{,}320$ execution Parquet records
- $62{,}640$ pairwise subsample stability evaluations ($31{,}320$ real, $31{,}320$ null)
- $2{,}160$ external ARI measurements
- All discordance gaps, null controls, and decision rules (Rules i, i', and iii)

### Instructions
1. Ensure Python 3.10+ and standard packages are available:
 ```bash
 pip install numpy scipy pandas scikit-learn
 ```
2. Run the self-contained Tier 1 reproduction script:
 ```bash
 python reproduction/scripts/recompute_saved_stability.py \
 --data-root /path/to/reviewer_evidence_bundle \
 --output-dir results/reviewer_audit
 ```

### What You Will See
The script performs full cryptographic checksum checks on all inputs and recalculates all metrics from scratch. In ~38 seconds, it will output:
```json
{
 "counts": {
 "partition_files": 4320,
 "per_fit_records": 4320,
 "cells": 72,
 "real_pairwise_ari": 31320,
 "null_pairwise_ari": 31320,
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

Inspect `results/reviewer_audit/recomputed_cells.csv` to review the per-cell breakdown:
- **18 Cells Meeting Rule (i'):** Mean stability $0.718875$, Mean accuracy $0.004231$, Discordance gap $+0.714644$.
- **9 Cells for FCAG, FCM, FastMVC on CNS, Colon, Prostate/Ovarian:** Mean stability $0.683764$, Mean accuracy $-0.002853$, Discordance gap $+0.686617$.

---

## 2. Status of the 13-Dataset Multi-Domain Benchmark

In Section 6.2, we report an exploratory historical comparison across 13 datasets. As detailed in our paper and `DATA_AVAILABILITY.md`:
- The 3,000 assembled score records reflect historical benchmark archives.
- The non-parametric Friedman omnibus test yields $\chi_F^2 = 11.556, p = 0.3979 \approx 0.40$ ($\text{df}=11$), establishing that all 12 comparative algorithms belong to a single equivalence clique under Nemenyi critical difference testing ($\text{CD}=4.62$). Simple K-Means attains top rank ($5.15$).
- A modern fresh re-execution completed 892 of 1,430 planned unique fits before being halted to avoid host memory exhaustion on dense spectral/distance matrix operations.
- To verify the historical scores and Friedman calculation:
 ```bash
 python reproduction/scripts/recompute_benchmark_scores.py \
 --scores data/historical_benchmarks/benchmark_matrix_passF.csv data/historical_benchmarks/exp3_cohirf_benchmark.csv \
 --output-dir results/recomputed_benchmark
 ```

---

## 3. Data Governance & Reviewer Confidential Access

In strict adherence to standard research data guidelines and upstream institutional terms:
- Open-access benchmarks (Sonar, Madelon, Isolet, 20 Newsgroups, PBMC68k) carry permissive **CC BY 4.0** licenses.
- Extended Yale Face Database B terms prohibit third-party database redistribution; images are acquired dynamically from authorized servers.
- Clinical biomedical microarrays (Colon, Leukemia, CNS, Ovarian, Prostate, SRBCT) originate from landmark hospital biobanks and are retrieved via OpenML's API.
- All evaluation partition arrays ($4{,}320$ partitions) are provided confidentially via the journal editorial system under a Data Use Agreement.

We welcome any questions or requests for additional verification.
