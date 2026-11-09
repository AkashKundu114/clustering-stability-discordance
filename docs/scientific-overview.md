# Scientific Overview: Stability-Accuracy Discordance

**Document:** `docs/scientific-overview.md` 
**Date:** 2026-11-07 
**Manuscript Title:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*  
**Running Header:** *Feature-Gated Bipartite Consensus Under Noise*  
**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)  
**Companion Repository:** [https://github.com/AkashKundu114/icc-clustering](https://github.com/AkashKundu114/icc-clustering) 

---

## 1. Executive Summary

Consensus clustering (cluster ensembling) is widely considered a gold standard for discovering reliable subgroups in biomedical data. In particular, resampling stability - the reproducibility of cluster partitions under random sample subsampling or bootstrapping - is frequently taken as evidence of biological cluster validity.

This research empirically tests this foundational assumption. Across six high-dimensional biomedical microarray cohorts ($D/N > 20$) and 12 comparative clustering algorithms across 13 benchmark datasets (6 high-D biomedical cohorts and 7 multi-domain benchmarks), we demonstrate that **subsample stability does not imply external classification accuracy**. Under high noise and feature-sample imbalance, base clusterers frequently latch onto mutually agreeing, data-driven noise partitions that display near-perfect subsample stability while showing zero or near-zero alignment with clinical diagnostic ground truth.

---

## 2. Core Concepts: Stability vs. Alignment

It is crucial to distinguish between three orthogonal concepts that are often conflated in unsupervised literature:

1. **Resampling Stability ($\text{Stab}$):** 
 Agreement between partitions produced on different random subsamples of the same dataset. Evaluated via the Adjusted Rand Index (ARI) on overlapping samples:
 $$\text{Stab}(C_1, C_2) = \text{ARI}(C_1|_{S_1 \cap S_2}, C_2|_{S_1 \cap S_2})$$
2. **External Label Alignment ($\text{Acc}$):** 
 Agreement between an unsupervised partition and an independent external biological or clinical reference label vector $y^*$:
 $$\text{Acc}(C) = \text{ARI}(C, y^*)$$
3. **The Discordance Gap ($\Delta$):** 
 The arithmetic difference between observed stability and external label recovery:
 $$\Delta = \text{Stab} - \text{Acc}$$
 When $\Delta \gg 0$ alongside high stability ($\text{Stab} \ge 0.50$), an algorithm is in a state of **stability-accuracy discordance**.

---

## 3. The Phenomenon of Distance Concentration

In high-dimensional regimes ($D \gg N$), pairwise Euclidean distances between observations concentrate around their mean:
$$\lim_{D \to \infty} \frac{d_{\max} - d_{\min}}{d_{\min}} = 0$$
When thousands of continuous uninformative distractor dimensions submerge a modest biological signal, independent base clustering estimators share the exact same realization of background noise. As a result:
- They repeatedly partition observations along spurious variance axes.
- Multiple random restarts repeatedly rediscover the same noise boundary, yielding high subsample stability.
- However, because these boundaries reflect noise rather than biology, external diagnostic accuracy remains near zero.

---

## 4. Null Calibration and Non-Degeneracy

To verify that observed stability is not a statistical artifact:
1. **Column-Permuted Null Controls:** Permuting values independently within each column destroys all inter-feature correlations while preserving marginal distributions. If an algorithm achieves stability on real data that significantly exceeds null stability ($\text{Stab}_{\text{real}} - \text{Stab}_{\text{null}} \ge 0.10$), the stability reflects true geometric structure in the empirical data manifold.
2. **Non-Degeneracy Screen (Rule i'):** Trivial partitions (e.g., placing all observations into a single giant cluster or isolating singletons) naturally produce artificial stability. A partition is non-degenerate if its smallest cluster contains $\ge 5\%$ of points in at least $90\%$ of subsamples.
