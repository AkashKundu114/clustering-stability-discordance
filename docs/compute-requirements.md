# Compute Requirements and Resource Profiles

**Document:** `docs/compute-requirements.md`  
**Date:** 2026-11-07  
**Project:** Stability-Accuracy Discordance in High-Dimensional Consensus Clustering  
**Target Journal:** Springer Nature — *Data Mining and Knowledge Discovery* (DMKD)

---

## 1. Resource Matrix Across Verification Tiers

| Activity | CPU Requirement | RAM Requirement | GPU Needed? | Wall-Clock Time | Recommended Environment |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tier 1: Reviewer Metric Recomputation** | 1 Core | < 512 MB | No | **~38–53 seconds** | Standard Laptop / Desktop |
| **Tier 2: Unit Tests & Governance Tests** | 1–2 Cores | 1 GB | No | **~1–2 minutes** | Standard Laptop / CI Runner |
| **Tier 3A: Fresh Six-Cohort Re-Run** | 8+ Cores (Ryzen 9 / Intel i7/i9) | 16 GB | Recommended (CUDA GPU for DEC) | **10–14 hours** | Workstation with NVIDIA GPU |
| **Tier 3B: 13-Dataset Full Benchmark** | 16+ Cores | 32+ GB | Mandatory | **~36–48 hours** | HPC Compute Node (Halted in repo) |

---

## 2. Workstation Hardware Boundaries

### The 16 GB Physical Memory Ceiling
Extensive profiling on an AMD Ryzen 9 8940HX workstation with 16 GB of DDR5 RAM revealed:
- Benchmark datasets with $N \ge 10{,}000$ (e.g., Indian Pines with $N=10{,}249$, 20 Newsgroups with $N=18{,}846$) generate $N \times N$ dense distance matrices exceeding $2.8\text{ GB}$ per matrix.
- When running baseline algorithms that lack sparse or anchor graph approximations (e.g., standard Spectral Clustering, full-matrix Monti consensus), peak host memory exceeds $14.8\text{ GB}$ (>93% allocation).
- To preserve workstation stability, the fresh 13-dataset benchmark was frozen at **892 / 1,430 fits**.

---

## 3. Supported Operating Systems & Tested Software

- **Operating Systems:** Windows 10/11 (64-bit), Ubuntu Linux (20.04 LTS, 22.04 LTS, 24.04 LTS), macOS (12.0+).
- **Python Runtimes:** Python 3.10, 3.11, 3.12, 3.13, 3.14.
- **Core Dependencies:**
  - `numpy >= 1.23.0`
  - `scipy >= 1.10.0`
  - `pandas >= 2.0.0`
  - `scikit-learn >= 1.3.0`
  - `pyyaml >= 6.0`
  - `pytest >= 7.0.0`
- **Optional Deep Learning Stack (for DEC):**
  - `torch >= 2.0.0` with CUDA runtime.
