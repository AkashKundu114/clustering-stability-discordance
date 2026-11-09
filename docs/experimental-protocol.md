# Experimental Protocol and Algorithmic Benchmark Specifications

**Document:** `docs/experimental-protocol.md` 
**Date:** 2026-11-07 
**Project:** Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise  
**Running Header:** Feature-Gated Bipartite Consensus Under Noise  
**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)  
**Companion Repository:** [https://github.com/AkashKundu114/icc-clustering](https://github.com/AkashKundu114/icc-clustering) 

---

## 1. Experimental Architectures

The research comprises two strictly separated computational experiments:

```text
┌────────────────────────────────────────────────────────────────────────┐
│ EXPERIMENT 1: Six-Cohort Biomedical Stability Analysis │
│ - 6 biomedical cohorts (CNS, Colon, Leukemia, Ovarian, Prostate, │
│ SRBCT) with D/N > 20. │
│ - 12 comparative algorithms. │
│ - 30 stratified 80% subsample runs per cell per condition. │
│ - Conditions: Real Data vs. Column-Permuted Null Controls. │
│ - Combinatorics: 72 cells x 435 pairs = 31,320 real comparisons + │
│ 31,320 null comparisons = 62,640 pairwise ARI evaluations. │
│ - External accuracy: 72 cells x 30 runs = 2,160 external ARIs. │
└────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────┐
│ EXPERIMENT 2: Exploratory 13-Dataset Multi-Domain Benchmark │
│ - 13 datasets spanning tabular, acoustic, speech, text, hyperspectral,│
│ single-cell, and image domains. │
│ - 12 comparative algorithms. │
│ - Seed schedules: 30 seeds on high-D cohorts, 10 seeds on others. │
│ - 3,000 assembled historical score records from 1,430 planned fits. │
│ - Modern rerun completed 892 fits before being halted on dense │
│ distance matrices (16 GB memory ceiling). │
│ - Non-parametric Friedman omnibus test: chi_F^2 = 11.56, p = 0.40. │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Decision Rules Governing Discordance

Three formal decision rules govern the classification of experimental cells:

1. **Rule (i) - Unconstrained Discordance:** 
 $$\text{Stab}_{\text{real}} \ge 0.50 \quad \text{and} \quad \text{Acc} \le 0.05$$
2. **Rule (i') - Non-Degenerate Discordance (Post-Hoc Refinement):** 
 Satisfies Rule (i) and additionally satisfies:
 $$\min_{k} \frac{|C_k|}{N} \ge 0.05 \quad \text{in} \ge 90\% \text{ of subsamples}$$
 This excludes trivial artifactual stability caused by singleton clusters or complete collapse to a single giant cluster.
3. **Rule (ii) - Indeterminate Null Regime:** 
 $$\text{Stab}_{\text{real}} - \text{Stab}_{\text{null}} < 0.10$$
 Stability on real data fails to exceed chance under feature permutation; stability provides no structural guidance.
4. **Rule (iii) - Persistent Multi-Cohort Discordance:** 
 An algorithm satisfies Rule (i') across at least three distinct high-$D$ cohorts.

---

## 3. Comparative Algorithmic Implementations

The twelve benchmarked algorithms represent classical, ensembling, deep, and graph-based clustering paradigms:

1. **K-Means:** Classical single-restart Lloyd's algorithm with K-Means++ initialization.
2. **Ward Hierarchical:** Agglomerative hierarchical clustering minimizing within-cluster variance.
3. **Spectral Clustering:** Normalized spectral embedding via normalized graph Laplacian with radial basis function (RBF) affinity kernel.
4. **Fuzzy C-Means (FCM):** Soft probabilistic clustering with fuzziness exponent $m=2.0$.
5. **Standard Consensus (StdCons / Monti):** Classical consensus clustering building full $N \times N$ consensus matrix from K-Means base clusterers ($M=25$).
6. **Core-Halo Consensus:** Distance-to-core partitioned consensus clustering separating high-confidence cores from boundary halos.
7. **DEC (Deep Embedding Clustering):** Deep neural autoencoder with Student's $t$-distribution soft assignment and KL divergence refinement.
8. **FCAG:** Fast Consensus Clustering with Anchor Graphs using uniform random anchor selection.
9. **FastMVC:** Fast multi-view consensus clustering adapted for multi-feature subspaces.
10. **CoHiRF:** Hierarchical consensus clustering combining random forests with unanimity voting ($M=25, \text{ratio}=0.15, \text{thresh}=0.80$).
11. **Ungated AC (ICC-v1):** Anchor-based consensus clustering without feature gating.
12. **GAC (Gated Anchor Consensus / ICC-v2):** Proposed experimental attribution vehicle coupling BGSS feature screening, random subspaces, and bipartite anchor graphs.
