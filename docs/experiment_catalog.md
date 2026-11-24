# Experiment Catalog

**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)
**Submitted Manuscript Reference:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*
**Authors:** Kalyan Kumar Das, Akash Kundu, Anirban Mukhopadhyay

This catalog provides an authoritative mapping of every major experiment in the submitted manuscript to its identifier, purpose, protocol, datasets, evaluated methods, parameters, and evidence artifacts.

---

## EXP-01: Primary Six-Cohort Stability-Accuracy Benchmark

- **Manuscript Reference:** Section 3.2, Table 3, Table 4, Table 5, Figure 3.
- **Core Scientific Question:** Does subsample stability guarantee external reference-label accuracy in high-dimensional biomedical cohorts ($D \gg N$)?
- **Evaluated Cohorts ($n=6$):**
  1. `cns`: $N=60, D=7{,}129, K=5$ (Medulloblastoma, Mglio, Oligo, PNET, Normal; $D/N = 118.8$)
  2. `colon`: $N=62, D=2{,}000, K=2$ (Tumor, Normal; $D/N = 32.3$)
  3. `leukemia`: $N=72, D=7{,}129, K=3$ (ALL-B, ALL-T, AML; $D/N = 99.0$)
  4. `ovarian`: $N=253, D=15{,}154, K=2$ (Cancer, Normal; $D/N = 59.9$)
  5. `prostate`: $N=102, D=12{,}600, K=2$ (Tumor, Normal; $D/N = 123.5$)
  6. `srbct`: $N=83, D=2{,}308, K=4$ (EWS, BL, NB, RMS; $D/N = 27.8$)
- **Evaluated Algorithms ($k=12$):**
  `K-Means`, `Ward`, `Spectral`, `FCM`, `StdCons`, `CoreHalo`, `FCAG`, `FastMVC`, `CoHiRF`, `UngatedAC` (ICC-v1), `GAC` (ICC-v2), `DEC`.
- **Subsampling Protocol:**
  - 30 stratified 80% subsamples per cell ($N_{\text{sub}} = \lfloor 0.8 N \rfloor$).
  - Evaluated in two modes: `real` (observed data) and `null` (column-permuted noise control).
  - Seed schedule: seeds $5000\text{--}5029$.
- **Arithmetic Accounting:**
  - Total cells: $6 \times 12 = 72$.
  - Partition arrays: $72 \times 30 \times 2 = \mathbf{4{,}320 \text{ partition files}}$ (`.npy`).
  - Execution logs: $\mathbf{4{,}320 \text{ telemetry files}}$ (`.parquet`).
  - Pairwise stability comparisons: $\binom{30}{2} = 435$ pairs/cell $\times 72$ cells $= \mathbf{31{,}320 \text{ real}} + \mathbf{31{,}320 \text{ null}} = \mathbf{62{,}640 \text{ total evaluations}}$.
  - External ARI evaluations: $72 \times 30 = \mathbf{2{,}160 \text{ external ARI evaluations}}$.
- **Key Empirical Results:**
  - Fresh Grand Mean Stability ($\bar{S}$): **`0.509812`** (Manuscript: `0.510`)
  - Fresh Grand Mean External Accuracy ($\bar{A}$): **`0.052522`** (Manuscript: `0.053`)
  - Fresh Mean Discordance Gap ($\bar{\Delta}$): **`+0.457289`** (Manuscript: `+0.457`, median `+0.442`)
  - Column-Permuted Null Stability ($\bar{S}_{\text{null}}$): **`0.006608`** (Manuscript: `0.007`)
  - Historical Grand Mean Gap: **`+0.464274`** (Manuscript: `+0.464`, median `+0.448`)
  - Historical 60 Non-Degenerate Cells Gap: **`+0.485376`** (Manuscript: `+0.485`)
- **Degeneracy Rule (i') Subset (18 cells):**
  Descriptive mean stability: **`0.718875`** (`0.719`), external accuracy: **`0.004231`** (`0.004`), gap: **`+0.714644`** (`+0.715`).
- **Rule (iii) Core Subset (9 cells: FCAG, FCM, FastMVC on CNS, Colon, Prostate/Ovarian):**
  Mean stability: **`0.683764`** (`0.684`), accuracy: **`-0.002853`** (`-0.003`), gap: **`+0.686617`** (`+0.687`).
- **DEC Divergence Forensic:**
  221 partitions differ between historical CPU Keras and fresh GPU PyTorch executions due to training protocol changes (full-batch vs mini-batch, no early stopping). All 11 non-DEC methods (3,960 partitions) are 100% bitwise identical.

---

## EXP-02: Synthetic Distractor Noise Expansion

- **Manuscript Reference:** Section 3.1, Table 2, Figure 2a-c.
- **Core Scientific Question:** How do clustering accuracy, subsample stability, and distance metric geometries behave as uninformative ambient noise expands?
- **Experimental Design:**
  - Synthetic Gaussian mixtures ($N=300, K=3$) with 10 signal dimensions ($D_{\text{signal}}=10$).
  - Distractor noise coordinates expanding across $D_{\text{noise}} \in [0, 5000]$.
  - Five distinct noise distributions: isotropic Gaussian, uniform, Student-$t$, correlated Gaussian, and zero-inflated sparse noise.
- **Key Findings:**
  - Subsample stability tracks accuracy degradation, collapsing below $0.03$ for centroid and fuzzy partitioners (Ward drops from $1.000$ to $0.026$).
  - Discrepancy $\Delta = \text{Stability} - \text{ARI}$ remains $< 0.20$ across almost all regimes under isotropic noise.
  - Critical distinction: **Synthetic simulations document accuracy collapse; real biomedical cohorts document stability-accuracy discordance.**

---

## EXP-03: GAC Factorial Decomposition & Modular Knockouts

- **Manuscript Reference:** Section 4.1, Section 4.2, Table 18, Table 19, Figure 4.
- **Core Scientific Question:** Which architectural components in Gated Anchor Consensus (GAC) recover signal under heavy noise?
- **Factorial Design ($2 \times 2$ across 6 cohorts, seeds $0\text{--}29$):**
  - Ambient Standard Consensus ($V_0$): $0.037$
  - Ambient Anchor Graph Consensus ($V_3$): $0.046$
  - BGSS Gated Standard Consensus ($V_2$): $0.077$
  - BGSS Gated Anchor Graph Consensus ($V_5$): $\mathbf{0.217}$
  - Factorial Interaction ($V_5 - V_2$): $+0.139$ (95% bootstrap CI: $[+0.007, +0.321]$, Wilcoxon $p = 0.16, n=6$).
- **Random-Gating Baseline Correction:**
  - Historical uncorrected control had cascaded BGSS within the random draw (reported $0.155$).
  - Corrected unguided random control draws features directly from $D$ without BGSS ranking (reported **$0.047$**).
  - Net BGSS gain: $+0.169$ ($0.217$ vs $0.047$, 95% CI: $[+0.036, +0.310]$, Wilcoxon $W=0.0, p=0.031$ uncorrected, Holm-adjusted $p=0.093$, $n=6$).
- **Component Ablations (Table 19):**
  - Remove BGSS Gating ($V_5 \to V_3$): $\Delta = +0.171$
  - Remove Bipartite Graph ($V_5 \to V_2$): $\Delta = +0.139$
  - Remove Ensembling ($V_5 \to V_1$): $\Delta = +0.147$
  - Remove Anchor Certification ($V_5 \to V_4$): $\Delta = +0.019$ (CI: $[-0.040, +0.082]$, Wilcoxon $p=0.84$). **Null result confirmed.**

---

## EXP-04: Anchor Budget & Sample Determinacy Landmark Study

- **Manuscript Reference:** Section 4.2, Figure S4, Table S8.
- **Core Scientific Question:** How sensitive is the bipartite spectral approximation to landmark budget $L$ and determinacy-based landmark selection?
- **Parameters:** $L \in \{10, 20, 40, 80, 160\}$ across 6 biomedical cohorts.
- **Key Finding:** Approximation fidelity plateaus for $L \ge 40$. High-determinacy landmark filtering ($V_5$) yields no statistically significant advantage over uniform random landmark selection ($V_4$: $+0.019$, $p=0.84$).

---

## EXP-05: Extreme Scalability on Synthetic Mixtures ($N \le 10^6$)

- **Manuscript Reference:** Section 5.2, Table 7, Table 8, Figure 6 (Supplementary Section S1).
- **Core Scientific Question:** Does bipartite factorization eliminate $O(N^2)$ memory ceilings up to one million samples?
- **Configurations (Gaussian mixtures, $D=100, K=5$, seeds $\{0, 1, 2\}$):**
  - **Config A:** $M=25$ models, $L=40$ anchors.
  - **Config B:** $M=15$ models, $L=60$ anchors.
- **Key Findings:**
  - At $N = 10^4$: auxiliary consensus graph memory drops from $762.9\text{ MB}$ to $3.05\text{ MB}$ ($99.6\%$ reduction).
  - At $N = 10^6$: dense matrix requires $\approx 7.63\text{ TB}$ (impossible on single node); GAC executes in $182.64 \pm 51.01\text{ s}$ (Config A) and $141.22 \pm 34.87\text{ s}$ (Config B) with peak RAM under $4\text{ GB}$.
  - Empirical scaling exponents: $\beta \approx 0.755$ (Config A) and $\beta \approx 0.873$ (Config B).

---

## EXP-06: Out-of-Sample Inductive Generalization

- **Manuscript Reference:** Section 5.2, Table 6, Table S3, Figure 4a-b (Supplementary Section S2).
- **Core Scientific Question:** Can transductive consensus partitions be extended to unseen query points without re-estimating the graph?
- **Protocol:** 10 random train/test splits (80% fit, 20% query) using closed-form determinacy-weighted centroid projections.
- **Key Finding:** Projection scales in $O(K \cdot |\mathcal{F}_{\text{active}}|)$ time, matching nearest-centroid labels on $95.3\%$ of query instances.

---

## EXP-07: Exploratory Multi-Domain 13-Dataset Benchmark

- **Manuscript Reference:** Section 5.1, Table 6, Figure 7a-n (Supplementary Section S3).
- **Core Scientific Question:** How does GAC perform across non-microarray domains (text, audio, face images, single-cell)?
- **Evaluated Datasets ($N=13$):**
  6 biomedical microarrays + `sonar`, `madelon`, `isolet`, `zheng68k`, `newsgroups20`, `indian_pines`, `yale_b`.
- **Accounting Status:**
  - 3,000 assembled historical score records across 156 cells ($13 \times 12$).
  - 892 of 1,430 planned fresh fits completed; 538 fits halted due to 16 GB host memory limits on large-$N$ benchmarks ($N > 2400$).
- **Statistical Inferential Result:**
  - Friedman omnibus test across 13 datasets: $\chi_F^2 = \mathbf{11.556213}$, $\text{df} = 11$, $p = \mathbf{0.397908} \approx 0.40$ ($p \gg 0.05$).
  - **Failure to reject the null hypothesis of equal algorithm performance.**
  - Nemenyi critical difference $\text{CD} = 4.622 > \Delta_{\max} = 2.615$. **All 12 algorithms reside in a single statistical equivalence clique.**
  - K-Means achieves Rank 1 ($5.15$); GAC achieves Rank 4 ($5.62$). GAC dominates only in the high-D subgroup ($n=6$, Rank 2.17). Excluding Leukemia and SRBCT, GAC's remaining-dataset mean ARI is $0.076$.
