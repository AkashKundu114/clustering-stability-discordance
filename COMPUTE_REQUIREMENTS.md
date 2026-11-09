# Compute Requirements and Resource Profiles

**Manuscript Title:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*  
**Running Header:** *Feature-Gated Bipartite Consensus Under Noise*  
**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)  
**Companion Repository:** [https://github.com/AkashKundu114/icc-clustering](https://github.com/AkashKundu114/icc-clustering)  

This document details hardware specifications, memory budgets, software dependencies, and expected runtimes for evaluating the **CSD** (`clustering-stability-discordance`) codebase across the **13 benchmark datasets** and **12 comparative clustering algorithms**.

---

## 1. Quick Requirements Overview

| Activity | CPU Requirements | RAM Requirement | GPU Needed? | Wall-Clock Time | Recommended Environment |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tier 1: Reviewer Metric Recomputation** | 1 Core | 512 MB | No | **~38 seconds** | Standard Laptop / Desktop |
| **Tier 2: Unit Tests & Smoke Suite** | 1-2 Cores | 1 GB | No | **~1-2 minutes** | Standard Laptop / CI Runner |
| **Tier 3A: Fresh Six-Cohort Re-Run** | 8+ Cores (Ryzen 9 / Intel i7/i9) | 16 GB | Recommended (CUDA GPU for DEC) | **10-14 hours** | Workstation with NVIDIA GPU |
| **Tier 3B: 13-Dataset Full Benchmark** | 16+ Cores | 32+ GB | Mandatory | **~36-48 hours** | HPC Compute Node (Halted in repo) |

---

## 2. Memory Footprint and Host Workstation Boundaries

### The 16 GB Ceiling
During exhaustive full-scale benchmarking on a 16 GB host machine (AMD Ryzen 9 8940HX, 16 physical cores, 16 GB DDR5 RAM, NVIDIA GeForce RTX 5060 Laptop GPU), computing dense similarity kernels and spectral projections on large-$N$ benchmarks ($N \ge 10{,}249$ on Indian Pines; $N \ge 18{,}846$ on 20 Newsgroups; $K=38$ on Yale B) caused host memory usage to exceed 14.8 GB (>93%).

To prevent operating system thrashing and memory exhaustion:
- The fresh re-execution of the 13-dataset benchmark was halted at **892 / 1,430 fits** (538 fits missing).
- We strongly advise referees **NOT** to attempt a full from-scratch re-clustering of large-$N$ benchmarks on systems with $\le 16\text{ GB}$ of RAM.
- Referees should utilize **Tier 1**, which recomputes all 62,640 pairwise subsample stability ARIs and external accuracy metrics directly from validated partition arrays in under 45 seconds using $< 500\text{ MB}$ of RAM.

---

## 3. Software Environment & Dependencies

- **Supported Operating Systems:** Linux (Ubuntu 20.04+, Debian 11+), macOS (12.0+), Windows 10/11 (64-bit).
- **Python Version:** Python $\ge 3.10$ (validated on Python 3.10, 3.11, 3.12, 3.13, 3.14).
- **Core Numerical Stack:**
 - `numpy >= 1.23.0`
 - `scipy >= 1.10.0`
 - `pandas >= 2.0.0`
 - `scikit-learn >= 1.3.0`
 - `pyyaml >= 6.0`
- **Optional Deep Learning Stack (for DEC):**
 - `torch >= 2.0.0` with CUDA runtime (recommended) or PyTorch CPU.
