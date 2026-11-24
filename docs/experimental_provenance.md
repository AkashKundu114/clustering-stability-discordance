# Experimental Provenance & Verification Classification

**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)
**Submitted Manuscript Reference:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*
**Authors:** Kalyan Kumar Das, Akash Kundu, Anirban Mukhopadhyay
**Journal:** Springer Nature - *Data Mining and Knowledge Discovery* (DMKD)
**Status:** Under review
**Audited Baseline Commit:** `44838fa`

To maintain scientific integrity and prevent historical artifacts from being conflated with fresh executions, this document establishes the provenance classification for every research artifact and experiment in the project.

---

## 1. Provenance Classification Schema

| Provenance Level | Operational Definition | Evidentiary Standard |
|---|---|---|
| **`AUTHENTICATED`** | Freshly executed and verified in the current reproducibility environment with complete environment and telemetry capture. | Verifiable execution log, dynamic SHA-256 hash, zero dependency on unrecorded state. |
| **`CORROBORATED`** | Generated in a prior execution cycle, independently corroborated by multiple consistent sources, bitwise identical where expected. | Identical byte-for-byte hash across independent repositories or archives. |
| **`PARTIALLY_RECONSTRUCTED`** | Execution details or partitions recovered, but minor implementation or environmental differences prevent exact bit-for-bit reproduction. | Divergence fully isolated and forensic cause documented (e.g. DEC framework shift). |
| **`HISTORICAL_ONLY`** | Precomputed historical results preserved as reported; not re-executed in the modern environment. | Preserved historical records; explicitly marked as not freshly rerun. |
| **`UNVERIFIED / UNKNOWN`** | Output exists but underlying execution parameters or input hashes cannot be reliably established. | Not admitted as verified scientific evidence. |

---

## 2. Artifact Provenance Ledger

### 2.1 Primary Six-Cohort Experiment (EXP-01: 72 Cells)
- **Non-DEC Partition Arrays (3,960 files):** **`CORROBORATED`**
  Exactly 3,960 out of 3,960 partition arrays across K-Means, Ward, Spectral, FCM, StdCons, CoreHalo, FCAG, FastMVC, CoHiRF, UngatedAC, and GAC are **100% byte-for-byte identical** between historical archives and the fresh rerun (`4,099 / 4,320` total identical).
- **DEC Partition Arrays (221 files):** **`PARTIALLY_RECONSTRUCTED`**
  Exactly 221 partitions differ in SHA-256 hash. The divergence was forensically isolated to an implementation and optimization protocol shift: historical DEC ran on CPU using TensorFlow/Keras with mini-batching (`batch_size=256`), shuffling, and `EarlyStopping`, whereas fresh DEC ran on GPU using PyTorch 2.16 with full-batch evaluation and fixed epoch loops without early stopping.
- **Pairwise Stability & Diagnostic Calculations (62,640 ARIs):** **`AUTHENTICATED`**
  Independently recalculated from raw partitions via `recompute_saved_stability.py` in $< 60\text{ seconds}$. Recomputed values match manuscript reported values to machine precision.

---

### 2.2 GAC Factorial & Modular Knockout Ablations (EXP-03)
- **Corrected Random-Gating Baseline ($0.047$):** **`AUTHENTICATED`**
  The corrected unguided control draws features directly from $D$ without BGSS ranking. The historical uncorrected control ($0.155$) cascaded BGSS filtering inside the random draw and is documented as a versioned experimental correction.
- **BGSS Factorial Interaction ($+0.139$) & Gain ($+0.169$):** **`AUTHENTICATED`**
  Recomputed across all 6 cohorts over seeds $0\text{--}29$. Confidence intervals and Wilcoxon tests verified.
- **Sample Determinacy Landmark Null Result ($V_5 - V_4 = +0.019$):** **`AUTHENTICATED`**
  Verified that high-determinacy landmark filtering provides no significant advantage over uniform random selection ($p=0.84$).

---

### 2.3 Multi-Domain 13-Dataset Benchmark (EXP-07)
- **Assembled Historical Score Records (3,000 rows):** **`CORROBORATED`**
  Assembled from `benchmark_matrix_passF.csv` (2,860 rows) and `exp3_cohirf_benchmark.csv` (140 rows).
- **Benchmark Arithmetic & Friedman Ranks:** **`AUTHENTICATED`**
  Re-aggregated via `recompute_benchmark_scores.py`. Recomputed $\chi_F^2 = 11.556, p = 0.3979 \approx 0.40$, K-Means Rank 1 ($5.15$), and GAC Rank 4 ($5.62$).
- **Fresh Completed Model Fits (892 fits):** **`AUTHENTICATED`**
  Completed during modern re-execution across all 6 biomedical cohorts, Sonar, and Madelon.
- **Halted Benchmark Fits (538 fits):** **`HISTORICAL_ONLY`**
  Halted due to $O(N^2)$ memory ceilings on large-$N$ datasets ($N > 2400$) on 16 GB workstations. Preserved intact as historical records without modification.

---

### 2.4 Extreme Scalability (EXP-05: $N \le 10^6$)
- **Runtime and Memory Scaling Exponents ($\beta \approx 0.755, 0.873$):** **`AUTHENTICATED`**
  Freshly benchmarked across Gaussian mixture instances up to $N = 10^6$ samples over seeds $\{0, 1, 2\}$.
