# Reproducibility Statement and Verification Protocols

**Manuscript Title:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*  
**Running Header:** *Feature-Gated Bipartite Consensus Under Noise*  
**Authors:** Kalyan Kumar Das (Techno India University), Akash Kundu (Techno India University), Anirban Mukhopadhyay (University of Kalyani)  
**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)  
**Companion Repository:** [https://github.com/AkashKundu114/icc-clustering](https://github.com/AkashKundu114/icc-clustering)  

---

## 1. Multi-Tier Verification Framework

Reproducibility is organized into three distinct verification tiers across the **13 benchmark datasets** and **12 comparative clustering algorithms**:

| Tier | Scope & Focus | Hardware & Time Requirements | Command / Status |
| :--- | :--- | :--- | :--- |
| **Tier 1: Reviewer Metric Recomputation** | Recomputes all 62,640 pairwise subsample stability ARIs and 2,160 external ARIs directly from validated partition arrays. | 1 CPU core, < 512 MB RAM, **~38-50 seconds**. | `python reproduction/scripts/recompute_saved_stability.py --data-root <evidence-dir> --output-dir results/tier1` |
| **Tier 2: Unit, Integration & Smoke Suite** | Verifies consensus algorithms, registry schemas, and CLI integrity across Python 3.10-3.14. | 1-2 CPU cores, ~1 GB RAM, **~1-2 minutes**. | `python -m pytest tests/` and `python scripts/reproduce.py --scope smoke` |
| **Tier 3A: Fresh Six-Cohort Re-Run** | Full end-to-end model fitting from preprocessed cohort caches (4,320 fits). | 8+ cores, 16 GB RAM, NVIDIA CUDA GPU, **~10-14 hours**. | Completed locally on 2026-11-02. Bit-for-bit identical across 11 of 12 algorithms. |
| **Tier 3B: 13-Dataset Full Benchmark** | Exploratory historical comparison across 13 multi-domain datasets (1,430 planned fits). | 16+ cores, 32+ GB RAM, **~36-48 hours**. | Frozen at 892 fits due to 16 GB memory ceiling on large-$N$ benchmarks ($N \ge 10,000$). Verified via Friedman omnibus test ($\chi_F^2 = 11.56, p = 0.40$). |

---

## 2. Reviewer Verification Guide

For detailed step-by-step instructions on executing the Tier 1 zero-network verification script, see:
- [`reproduction/README.md`](reproduction/README.md)
- [`docs/reviewer-reproduction.md`](docs/reviewer-reproduction.md)
- [`reproduction/reviewer_guide/quick_verification.md`](reproduction/reviewer_guide/quick_verification.md)

---

## 3. Evidence and Governance Transparency

The software package installs cleanly in Python 3.10-3.14 environments, and all unit tests pass with zero warnings. Saved-output arithmetic, fresh local execution, and authenticated historical provenance are maintained as separate evidence levels to preserve full scientific integrity.
