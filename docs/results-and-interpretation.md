# Results, Statistical Adjudication, and Interpretation

**Document:** `docs/results-and-interpretation.md` 
**Date:** 2026-11-07 
**Project:** Stability-Accuracy Discordance in High-Dimensional Consensus Clustering 

---

## 1. Primary Empirical Findings: Six-Cohort Stability Study

The empirical foundation rests on 62,640 pairwise subsample stability evaluations ($31{,}320$ real $+ 31{,}320$ column-permuted null controls) and 2,160 external ARI measurements across 72 experimental cells:

### 1.1 Fresh Rerun Summary Metrics Across All 72 Cells
- **Grand Mean Subsample Stability:** `0.509812`
- **Grand Mean External ARI:** `0.052522`
- **Mean Discordance Gap ($\Delta$):** `+0.457289`
- **Median Discordance Gap:** `+0.442304`
- **Mean Column-Permuted Null Stability:** `0.006608`

### 1.2 Non-Degenerate Discordance Zone (Rule i')
- **Number of Cells Meeting Rule (i'):** 18 cells (out of 72).
- **Mean Subsample Stability:** `0.718875`
- **Mean External ARI:** `0.004231`
- **Mean Discordance Gap:** `+0.714644`
- **Median Discordance Gap:** `+0.700120`

### 1.3 Persistent Multi-Cohort Discordance (Rule iii)
- **Algorithms:** FCAG, FCM, FastMVC across Colon, CNS, Prostate/Ovarian (9 cells).
- **Mean Subsample Stability:** `0.683764`
- **Mean External ARI:** `-0.002853` (collapses to chance).
- **Mean Discordance Gap:** `+0.686617`

---

## 2. Forensic Reconciliation: Historical (`0.516586`) vs. Fresh (`0.509812`)

- **Historical Grand Mean Stability:** `0.51658606`
- **Fresh Grand Mean Stability:** `0.50981152`
- **Overall Difference ($\Delta$):** `-0.00677454`
- **Locus of Divergence:** Proved bit-for-bit to be **100% confined to DEC** ($221$ of $4{,}320$ partitions changed; $0$ partitions changed across the other 11 algorithms).
- **Driver:** Architectural implementation evolution from historical TensorFlow/Keras CPU mini-batch training with EarlyStopping to fresh PyTorch CUDA GPU full-batch optimization.
- **Typo Resolution:** The value `0.511394` in earlier markdown documentation was an isolated manual transcription error that never existed in any raw data or partition array.

---

## 3. Exploratory 13-Dataset Multi-Domain Benchmark

Evaluated across the 3,000 assembled historical score records (from 1,430 planned fits; 892 fresh clean fits completed before freezing):

- **Non-Parametric Friedman Omnibus Test:**
 $$\chi_F^2 = 11.556, \quad p = 0.3979 \approx 0.40, \quad \text{df} = 11$$
- **Omnibus Ranks Across All 13 Benchmarks:**
 1. K-Means ($R = 5.15$)
 2. Standard Consensus ($R = 5.23$)
 3. DEC ($R = 5.23$)
 4. GAC ($R = 5.62$)
 5. Ward ($R = 5.69$)
 6. Ungated AC ($R = 6.92$)
 7. FCM ($R = 7.08$)
 8. Spectral ($R = 7.08$)
 9. Core-Halo ($R = 7.15$)
 10. FastMVC ($R = 7.38$)
 11. CoHiRF ($R = 7.69$)
 12. FCAG ($R = 7.77$)
- **Nemenyi Critical Difference ($\alpha = 0.05$):** $\text{CD} = 4.622$. All 12 algorithms reside in a single shared equivalence clique. Complex consensus methods provide no statistically detectable advantage over elementary baselines.
