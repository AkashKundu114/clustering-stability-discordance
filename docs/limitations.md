# Scientific, Algorithmic & Operational Limitations

**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)
**Submitted Manuscript Reference:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*
**Authors:** Kalyan Kumar Das, Akash Kundu, Anirban Mukhopadhyay
**Journal:** Springer Nature - *Data Mining and Knowledge Discovery* (DMKD)
**Status:** Under review
**Audited Baseline Commit:** `44838fa`

To maintain scientific rigor and prevent overgeneralization, this document compiles the empirical, theoretical, statistical, and operational boundaries of the research.

---

## 1. Scope and Generalization Boundaries

1. **Small Clinical Cohort Sample Size ($n=6$):**
   The primary empirical analysis evaluates six clinical cancer microarray cohorts ($D/N$ from 28 to 124). While severe stability-accuracy discordance is demonstrated across all six cohorts, six datasets do not constitute a random sample of all biomedical domains. Broad population-level claims regarding all high-dimensional data are not supported.
2. **Operational Reference Labels vs. Biological Ground Truth:**
   External reference labels (e.g. binary tumor status, histological subtypes) are operational clinical diagnostic categories. An Adjusted Rand Index of $\bar{A} \approx 0.00$ indicates that clusters do not align with primary clinical classifications; it does not prove the absence of unannotated biological or batch heterogeneity. External ARI serves as a diagnostic benchmark, not an absolute gold standard.
3. **Resampling Stability vs. Initialization Sensitivity:**
   The primary benchmark evaluates variance under sample subsampling (stratified 80% draws). Full-cohort seed stability ($\text{Seed}^*$) was benchmarked as a secondary metric. For deterministic methods (Ward, single-restart Lloyd's), seed stability is identically $1.000$, whereas subsample stability remains vulnerable to data perturbation.

---

## 2. Statistical & Inferential Limitations

4. **Statistical Dependence of Pairwise ARIs:**
   Within each of the 72 experimental cells, $\binom{30}{2} = 435$ pairwise stability comparisons are generated from the same 30 subsample partitions. Any two pairs sharing a common partition (e.g. $S_{1,2}$ and $S_{1,3}$) covary. Inferential statistical tests must never pool all 31,320 comparisons or treat 435 pairs as independent degrees of freedom. The valid units of inference are cell-level means ($N=72$) and cohort-level blocks ($N=6$).
5. **Small-Cluster Bootstrap Instability:**
   When performing cohort-clustered bootstrap resampling with only $N=6$ clusters, the probability of drawing a resample that omits a specific cohort is $(1 - 1/6)^6 \approx 33.5\%$. In one-third of all bootstrap resamples, extreme cohorts (e.g. Prostate $\bar{\Delta} = +0.690$ or Leukemia $\bar{\Delta} = +0.240$) are absent, producing wide bootstrap distributions. The manuscript correctly emphasizes descriptive cell metrics and leave-one-cohort-out bounds ($[+0.407, +0.485]$).
6. **Multiplicity in Post-Hoc Subsets (Rule i'):**
   Rule (i') was introduced post-hoc after observing degenerate single-point cluster collapse in CoreHalo on Prostate. While 18 cells pass Rule (i'), post-hoc criteria must not be conflated with pre-specified hypotheses. Results are reported both with and without Rule (i').
7. **Uncorrected vs. Corrected Significance for BGSS:**
   The Wilcoxon signed-rank test comparing BGSS against matched random gating yields $W = 0.0, p = 0.031$ uncorrected ($n=6$). When adjusted for the three gating comparisons using the Holm-Bonferroni correction, the adjusted p-value is $p = 0.093$, which exceeds the nominal $\alpha = 0.05$ threshold. The gain should be interpreted as suggestive, not definitive universal proof.

---

## 3. Algorithmic & GAC Boundaries

8. **Omnibus Parity & K-Means Superiority (Table 6):**
   Across the 13-dataset multi-domain benchmark, the non-parametric Friedman omnibus test yields $\chi_F^2 = 11.556, \text{df}=11, p = 0.3979 \approx 0.40$. The omnibus test **fails to reject the null hypothesis of equal algorithm performance**. All 12 comparative algorithms reside in a **single statistical equivalence clique** ($\Delta_{\max} = 2.615 < \text{CD} = 4.622$). K-Means attains the top overall rank ($5.15$); GAC ranks #4 ($5.62$). GAC dominates only in the high-dimensional clinical subgroup ($n=6$, Rank 2.17).
9. **GAC Performance Concentration in Leukemia and SRBCT:**
   GAC’s signal recovery on high-dimensional microarrays is driven primarily by Leukemia ($0.600$) and SRBCT ($0.546$), where informative genes possess pronounced marginal coordinate bimodality (enriching 27 of 50 diagnostic Golub markers, $p = 1.38 \times 10^{-10}$). On diffuse, non-bimodal manifolds (Prostate $0.012$, CNS $-0.002$), BGSS yields negligible gains ($+0.004$ to $+0.012$). Excluding Leukemia and SRBCT, GAC's mean ARI across the remaining 11 benchmark datasets is **$0.076$**.
10. **High-Determinacy Anchor Selection Null Result:**
    Landmark filtering based on sample determinacy ($V_5$) yields a negligible gain of $\Delta = +0.019$ ($p=0.84$) over uniform random landmark selection ($V_4$). Determinacy screening provides no measurable advantage over uniform random landmark drawing.
11. **High-Cardinality and Sparse Representation Failures:**
    When datasets possess high class cardinality ($K \ge 10$) or sparse count representations (e.g. 20 Newsgroups with $K=20$, PBMC68k with $K=10$), coordinate blending dilutes marginal contrast, causing GAC to collapse ($0.000$ on 20 Newsgroups vs. $0.555$ for Standard Consensus).

---

## 4. Hardware, Execution & Data Boundaries

12. **Workstation RAM Boundaries ($O(N^2)$ Ceilings on Large-$N$ Data):**
    Dense consensus and full spectral decompositions require $O(N^2)$ matrix memory and $O(N^3)$ factorization time. On large-sample benchmarks (20 Newsgroups $N=18{,}846$, ISOLET $N=7{,}797$, PBMC68k $N=68{,}579$), dense kernel construction ($18,846 \times 18,846 \times 8 \text{ bytes} \approx 2.84\text{ GB}$) causes memory exhaustion on standard 16 GB workstations. In the modern clean re-execution, **892 of 1,430 planned fits were completed; 538 fits were halted to prevent system crashes**.
13. **Deep Embedded Clustering (DEC) Implementation Shift:**
    Exactly 221 of 4,320 partition files differ between historical and fresh runs, confined exclusively to DEC. Historical DEC ran on CPU using TensorFlow/Keras with mini-batching, shuffling, and early stopping; fresh DEC ran on GPU using PyTorch 2.16 with full-batch evaluation and fixed epochs. The discrepancy is an implementation and training protocol shift whose individual components have not been fully isolated.
14. **Data Redistribution and Privacy Proscriptions:**
    Human clinical tissue microarrays (CNS, Colon, Leukemia, Ovarian, Prostate, SRBCT) cannot be redistributed directly in public Git repositories to preserve donor privacy. Extended Yale Face Database B terms explicitly prohibit incorporation into larger publicly distributed archives without Yale University permission.
