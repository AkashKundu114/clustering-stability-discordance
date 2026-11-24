# Experimental Protocol Specification

**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)
**Submitted Manuscript Reference:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*
**Authors:** Kalyan Kumar Das, Akash Kundu, Anirban Mukhopadhyay
**Journal:** Springer Nature - *Data Mining and Knowledge Discovery* (DMKD)
**Status:** Under review
**Audited Baseline Commit:** `44838fa`

This document provides the formal mathematical and computational protocols governing all experiments reported in the submitted manuscript.

---

## 1. Primary Six-Cohort Experiment Protocol (EXP-01)

### 1.1 Evaluated Datasets ($n=6$)
The primary empirical benchmark evaluates six high-dimensional biomedical cancer cohorts characterized by extreme dimensional imbalance ($D/N > 20$):
- **CNS:** $N = 60, D = 7{,}129, K = 2$ ($D/N = 118.8$)
- **Colon:** $N = 62, D = 2{,}000, K = 2$ ($D/N = 32.3$)
- **Leukemia:** $N = 72, D = 7{,}129, K = 2$ ($D/N = 99.0$)
- **Ovarian:** $N = 253, D = 15{,}154, K = 2$ ($D/N = 59.9$)
- **Prostate:** $N = 102, D = 12{,}600, K = 2$ ($D/N = 123.5$)
- **SRBCT:** $N = 83, D = 2{,}308, K = 4$ ($D/N = 27.8$)

### 1.2 Evaluated Algorithms ($k=12$)
1. `K-Means`: Single-restart Lloyd's algorithm (`sklearn.cluster.KMeans`).
2. `Ward`: Hierarchical agglomerative clustering with Ward minimum variance criterion (`sklearn.cluster.AgglomerativeClustering`).
3. `Spectral`: Normalized spectral graph cut clustering (`sklearn.cluster.SpectralClustering`).
4. `FCM`: Fuzzy C-Means with fuzziness parameter $m = 2.0$.
5. `StdCons`: Standard dense co-association consensus clustering ($M = 25$ base partitions, average linkage).
6. `CoreHalo`: Density-based core-halo threshold consensus clustering.
7. `FCAG`: Fuzzy C-means bipartite anchor graph consensus ($L = 40$ anchors).
8. `FastMVC`: Fast Multi-View bipartite consensus clustering across random feature subspaces.
9. `CoHiRF`: Hierarchical consensus ensemble using random forest similarity graphs.
10. `UngatedAC` (ICC-v1): Bipartite anchor graph consensus without feature gating (ambient $D$).
11. `GAC` (ICC-v2): Bimodality-Gated Subspace Selection with bipartite anchor graph consensus ($M = 25, L = 40$).
12. `DEC`: Deep Embedded Clustering with autoencoder latent representation.

### 1.3 Subsampling and Seed Schedule
- **Subsample Ratio:** Stratified $80\%$ subsampling without replacement:
  $$N_{\text{sub}} = \lfloor 0.8 \times N \rfloor$$
- **Replications ($B$):** Exactly $B = 30$ independent subsample draws per experimental cell.
- **Pseudo-Random Seed Schedule:**
  - Subsample generation: seeds $\mathcal{S}_{\text{sub}} = \{5000, 5001, \dots, 5029\}$.
  - Model fitting seeds: explicitly passed to estimators to ensure deterministic base fits.
- **Modes of Evaluation:**
  - `real`: Observed expression matrix $X \in \mathbb{R}^{N \times D}$.
  - `null`: Column-permuted control matrix $\tilde{X}$, where each feature column $d \in \{1, \dots, D\}$ is independently shuffled across samples.

### 1.4 Metric Formulations
1. **Pairwise Subsample Stability ($S_{ij}$):**
   $$S_{ij} = \text{ARI}\left(P_i|_{I_i \cap I_j}, P_j|_{I_i \cap I_j}\right), \quad \bar{S} = \frac{1}{435} \sum_{1 \le i < j \le 30} S_{ij}$$
2. **External Diagnostic Accuracy ($\bar{A}$):**
   $$\bar{A} = \frac{1}{30} \sum_{i=1}^{30} \text{ARI}\left(P_i, Y|_{I_i}\right)$$
3. **Discordance Gap ($\bar{\Delta}$):**
   $$\bar{\Delta} = \bar{S} - \bar{A}$$
4. **Permuted-Null Baseline ($\bar{S}_{\text{null}}$):**
   Subsample stability evaluated across partitions generated on column-permuted inputs $\tilde{X}$.

### 1.5 Degeneracy Screening Rules
- **Rule (i) [Pre-specified Numeric]:** $\bar{S} \ge 0.50$ AND $\bar{A} \le 0.05$ (20 cells pass).
- **Rule (i') [Post-hoc Non-Degeneracy]:** Passes Rule (i) AND smallest cluster contains $\ge 5\%$ of subsample points in $\ge 27$ of 30 subsample repeats (18 cells pass).
- **Rule (ii) [Excess Stability]:** $\bar{S} - \bar{S}_{\text{null}} \ge 0.10$.
- **Rule (iii) [Multi-Cohort Persistence]:** Satisfies Rule (i') across $\ge 3$ distinct cohorts (FCAG, FCM, FastMVC: 9 cells).

---

## 2. GAC Algorithmic Protocol & Ablation Design (EXP-03)

### 2.1 Bimodality-Gated Subspace Selection (BGSS)
For each feature coordinate $d \in \{1, \dots, D\}$:
1. Compute sample skewness $g_{1,d}$ and sample excess kurtosis $g_{2,d}$.
2. Apply finite-sample bias correction to uniform kurtosis baseline:
   $$c_N = \frac{3(N - 1)^2}{(N - 2)(N - 3)}$$
3. Compute Sarle's bimodality coefficient:
   $$b_d = \frac{g_{1,d}^2 + 1}{g_{2,d} + c_N + 10^{-5}}$$
4. Select active candidate pool $\mathcal{F}_{\text{active}}$ as the top $\lfloor \alpha D \rfloor$ features ranked by $b_d$, where:
   $$\text{pool\_size} = \max\left(K, \left\lfloor \min\left(1.0, \max(0.15, \frac{100}{D})\right) \cdot D \right\rfloor\right)$$

### 2.2 Factorial Design ($2 \times 2$)
Evaluates the cross-product of feature space and consensus graph architecture:
- $\text{Ambient } (D) \times \text{Standard Consensus}$ ($V_0$)
- $\text{Ambient } (D) \times \text{Anchor Graph Consensus}$ ($V_3$)
- $\text{BGSS Gated } (\mathcal{F}_{\text{active}}) \times \text{Standard Consensus}$ ($V_2$)
- $\text{BGSS Gated } (\mathcal{F}_{\text{active}}) \times \text{Anchor Graph Consensus}$ ($V_5$)
- Random seeds: $\mathcal{S}_{\text{ablation}} = \{0, 1, \dots, 29\}$ ($n=6$ cohorts).

### 2.3 Random-Gating Control Protocol
- **Corrected Control:** Features are sampled uniformly at random directly from ambient space $D$ without BGSS ranking ($|\mathcal{F}_{\text{rand}}| = |\mathcal{F}_{\text{active}}|$).
- **Historical Cascaded Control:** Cascaded BGSS filtering inside the randomly drawn pool (yielding $0.155$); replaced by the unguided control ($0.047$).

---

## 3. Multi-Domain Benchmark Protocol (EXP-07)

### 3.1 Evaluated Benchmark Datasets ($N=13$)
- High-$D$ Biomedical Microarrays ($n=6$): CNS, Colon, Leukemia, Ovarian, Prostate, SRBCT.
- Acoustic / Speech: Sonar ($N=208, D=60, K=2$), ISOLET ($N=7{,}797, D=617, K=26$).
- Non-Linear Synthetic: Madelon ($N=500, D=500, K=2$).
- Single-Cell RNA-seq: PBMC68k Reduced ($N=700, D=765, K=10$).
- Sparse Document Text: 20 Newsgroups ($N=18{,}846, D=10{,}000, K=20$).
- Hyperspectral Imagery: Indian Pines ($N=10{,}249, D=200, K=16$).
- Face Imagery: Extended Yale B ($N=2{,}414, D=1{,}024, K=38$).

### 3.2 Seed Schedules
- High-Dimensional Cohorts: seeds $42\text{--}71$ ($30$ seeds).
- Other Benchmarks: seeds $42\text{--}51$ ($10$ seeds).
- Modular Ablations & Factorial: seeds $0\text{--}29$ ($30$ seeds).

### 3.3 Statistical Rank Methodology
- Non-parametric Friedman test:
  $$\chi_F^2 = \frac{12 N}{k(k+1)} \left[ \sum_{j=1}^k R_j^2 \right] - 3N(k+1)$$
  where $N=13$ blocks (datasets), $k=12$ treatments (algorithms).
- Nemenyi two-tailed critical difference:
  $$\text{CD} = q_{\alpha=0.05, k=12} \sqrt{\frac{k(k+1)}{6N}} = 3.328 \times \sqrt{2} = 4.622$$
