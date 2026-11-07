# Tier 2: Fresh Experiment Status and Incomplete Benchmark Disclosure

**Document:** `docs/tier2-experiment-status.md` 
**Date:** 2026-11-07 
**Project:** Stability-Accuracy Discordance in High-Dimensional Consensus Clustering 

---

## 1. Operational Scope of Tier 2

Tier 2 represents a complete end-to-end re-execution of clustering models from raw preprocessed datasets, re-running all base clusterers, ensembling logic, and evaluation routines from scratch.

Unlike Tier 1 (which reconstructs metrics from saved partition arrays in under 60 seconds), Tier 2 requires significant compute resources, specialized hardware (NVIDIA GPU for deep DEC baselines), and extensive execution time.

---

## 2. Status of the Six-Cohort Stability Study (Completed)

- **Total Planned Fits:** $4{,}320$ fits ($72\text{ cells} \times 30\text{ subsamples} \times 2\text{ modes [real, null]}$).
- **Execution Status:** **100% Completed** in dedicated clean-clone re-execution on 2026-11-02.
- **Compute Time:** Approximately 10-14 hours of continuous compute on an AMD Ryzen 9 8940HX with an NVIDIA GeForce RTX 5060 Laptop GPU.
- **Reproducibility Findings:**
 - 11 of 12 algorithms ($3{,}960$ of $4{,}320$ partitions) are **100% bitwise identical** to original historical outputs.
 - The remaining 360 partitions (DEC) exhibited expected numerical divergence due to framework evolution (TensorFlow/Keras CPU mini-batch vs. PyTorch CUDA GPU full-batch).

---

## 3. Status of the 13-Dataset Multi-Domain Benchmark (Exploratory / Incomplete)

> [!IMPORTANT] 
> **Mandatory Disclosure for Referees and Authors:** 
> The 13-dataset multi-domain benchmark is presented strictly as an **exploratory historical comparison**, NOT as a completed fresh benchmark.

### The Numbers:
- **Planned Unique Model Fits in Historical Logs:** $1{,}430$ fits.
- **Assembled Historical Score Records:** $3{,}000$ rows (evaluated across canonical seeds: 30 seeds on $D/N > 20$ cohorts, 10 seeds on others).
- **Fresh Re-Execution Completed:** **892 fits**.
- **Fresh Re-Execution Incomplete / Missing:** **538 fits**.

### Why the Fresh Benchmark Was Frozen:
During full-scale re-execution on a 16 GB host workstation, computing dense distance kernels, all-pairs similarity graphs, and spectral projections on large-$N$ benchmarks ($N \ge 10{,}249$ on Indian Pines; $N \ge 18{,}846$ on 20 Newsgroups; $K=38$ on Yale B) caused host memory usage to exceed 14.8 GB (>93% physical allocation).

To prevent operating system thrashing, swap failure, and kernel panic:
- The fresh re-execution was frozen at **892 fits**.
- **Referees must NOT attempt to execute the 538 incomplete benchmark fits on systems with $\le 16\text{ GB}$ of RAM.**
- The historical benchmark records are preserved, authenticated via SHA-256 manifests, and disclosed with complete transparency.
- Friedman omnibus testing on the assembled historical baseline confirms that all 12 algorithms reside in a single equivalence clique ($\chi_F^2 = 11.56, p = 0.40, \text{CD}=4.62$), with simple K-Means achieving top position ($5.15$).
