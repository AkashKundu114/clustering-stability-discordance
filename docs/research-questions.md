# Research Questions and Empirical Findings

**Document:** `docs/research-questions.md` 
**Date:** 2026-11-07 
**Project:** Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise  
**Running Header:** Feature-Gated Bipartite Consensus Under Noise  
**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)  
**Companion Repository:** [https://github.com/AkashKundu114/icc-clustering](https://github.com/AkashKundu114/icc-clustering) 

---

## 1. Research Question 1 (RQ1): The Stability-Accuracy Relationship

> **Does subsample stability guarantee external reference-label accuracy in high-dimensional biomedical cohorts?**

### Empirical Evidence
- Evaluated across 72 experimental cells (6 high-$D$ biomedical cohorts $\times$ 12 comparative algorithms, framed within the 13 benchmark datasets).
- Total pairwise comparisons: $62{,}640$ evaluations ($31{,}320$ real $+ 31{,}320$ column-permuted null controls).
- External ARI evaluations: $2{,}160$ measurements against clinical reference labels.
- Across all 72 cells, authoritative fresh re-execution yields:
 - Grand Mean Subsample Stability: $0.509812$
 - Grand Mean External Accuracy (ARI): $0.052522$
 - Mean Discordance Gap ($\Delta$): $+0.457289$
 - Median Discordance Gap: $+0.442304$
- **Conclusion for RQ1:** **NO.** Resampling stability does not guarantee external accuracy. In fact, a positive discordance gap is pervasive across algorithms in high-dimensional biomedical regimes.

---

## 2. Research Question 2 (RQ2): Geometric Structure vs. Permutation Artifacts

> **Do non-degenerate discordant clusterings reflect data-driven structure or trivial noise artifacts?**

### Empirical Evidence
- Evaluated against column-permuted null data where all feature correlations are broken.
- Across the six cohorts, column-permuted null stability averages only $0.006608$ (near zero).
- In contrast, real data stability across the 18 non-degenerate discordant cells (Rule i') reaches $0.718875$, while external accuracy is $0.004231$ (gap $+0.714644$).
- On Prostate ($D=12{,}600$), Ward achieves $\text{Stab}=0.996$ and Spectral achieves $\text{Stab}=0.971$ (null stability $\le 0.049$).
- Principal component analysis reveals that these clusterings strongly track top principal components ($r = 0.77\text{--}0.86$ with PC1) and total per-sample expression variance, rather than diagnostic tumor status.
- **Conclusion for RQ2:** High stability reflects genuine, repeatable geometric concentration in the empirical data space, but this concentration tracks dominant technical variance rather than biological pathology.

---

## 3. Research Question 3 (RQ3): Algorithmic Remediation via GAC

> **Can modular unsupervised interventions - feature gating, subspace ensembling, and bipartite compression - mitigate stability-accuracy discordance?**

### Empirical Evidence
- Evaluated using Gated Anchor Consensus (GAC) as an experimental ablation vehicle.
- **Random Feature Gating:** Does not improve accuracy ($0.046$ dense, $0.047$ bipartite vs. $0.037$ ambient consensus).
- **Bipartite Anchor Compression:** Reduces auxiliary graph memory by $99.6\%$ at $N=10^4$ ($O(NL)$ vs. $O(N^2)$), but does not alter clustering accuracy in isolation.
- **Bimodality-Gated Subspace Selection (BGSS):** Selectively elevates accuracy on signal-rich cohorts where informative markers show bimodal separation (Leukemia $\text{ARI} = 0.600 \pm 0.367$, SRBCT $\text{ARI} = 0.546 \pm 0.102$).
- **Boundary Failures:** On diffuse or non-bimodal cohorts (Prostate, CNS), BGSS fails to isolate signal, yielding discordance gaps of $+0.847$ and $+0.542$.
- **Conclusion for RQ3:** Univariate bimodality filtering helps only when signal coordinates possess multimodal marginals; it cannot overcome complex multivariate or diffuse manifold noise.
