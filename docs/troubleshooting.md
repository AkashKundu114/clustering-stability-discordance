# Troubleshooting and Common Questions

**Document:** `docs/troubleshooting.md` 
**Date:** 2026-11-07 
**Project:** Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise  
**Running Header:** Feature-Gated Bipartite Consensus Under Noise  
**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)  
**Companion Repository:** [https://github.com/AkashKundu114/icc-clustering](https://github.com/AkashKundu114/icc-clustering) 

---

## 1. Common Issues and Resolutions

### Issue 1: "FileNotFoundError: Evidence bundle not found"
- **Symptom:** Running `python reproduction/scripts/recompute_saved_stability.py` raises `FileNotFoundError`.
- **Cause:** The script requires the `--data-root` argument pointing to the authorized evidence bundle directory containing `results/stability/partitions/` and `results/stability/runs/`.
- **Resolution:** Specify the full local path to the evidence directory:
 ```bash
 python reproduction/scripts/recompute_saved_stability.py \
 --data-root /path/to/authorized/evidence_bundle \
 --output-dir results/recomputed_tier1
 ```

---

### Issue 2: "MemoryError or OS Freezing during 13-Dataset Benchmark (12 Comparative Algorithms)"
- **Symptom:** Host RAM climbs toward 100% and operating system becomes unresponsive when running large-dataset benchmarks.
- **Cause:** Large-$N$ benchmarks ($N \ge 10{,}000$) create dense $N \times N$ distance and similarity matrices requiring >14 GB of RAM.
- **Resolution:** Do not attempt full end-to-end reruns on systems with $\le 16\text{ GB}$ of RAM. Use the Tier 1 verification tool (`recompute_benchmark_scores.py`) to verify the arithmetic and Friedman statistics from the validated historical tables.

---

### Issue 3: "LaTeX Compilation: Class file sn-jnl.cls not found"
- **Symptom:** `pdflatex` reports missing document class.
- **Cause:** Compilation must be executed from within the manuscript directory (`paper/manuscript` or `paper/review`) where `sn-jnl.cls` resides.
- **Resolution:**
 ```bash
 cd paper/review
 pdflatex main.tex
 bibtex main
 pdflatex main.tex
 pdflatex main.tex
 ```

---

### Issue 4: "Yale Face B Download Blocked"
- **Symptom:** Network error downloading Yale Face B archive.
- **Cause:** Institutional servers may experience transient connectivity issues or rate limiting.
- **Resolution:** Verify your network connection and retry. In strict compliance with Yale University CVC terms of use, raw Yale B face images cannot be bundled into public repositories.
