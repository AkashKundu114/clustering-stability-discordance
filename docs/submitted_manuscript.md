# Submitted Manuscript Reference & Evidence Mapping

**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)
**Document Type:** Formal Historical Submission Reference
**Submission Date:** November 19, 2026
**Target Journal:** Springer Nature – *Data Mining and Knowledge Discovery* (DMKD)

---

## 1. Manuscript Identification & Metadata

The authoritative reference for all scientific claims, experimental methodology, numerical results, tables, figures, and limitations is the exact 48-page consolidated manuscript PDF:

- **Full Title:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*
- **Running Header:** *Feature-Gated Bipartite Consensus Under Noise*
- **Author Order & Affiliations:**
  1. **Kalyan Kumar Das** (Department of Computer Science and Engineering, Techno India University, Kolkata, West Bengal, India; ORCID: `0009-0004-8333-8900`)
  2. **Akash Kundu** (Department of Computer Science and Engineering, Techno India University, Kolkata, West Bengal, India; ORCID: `0009-0003-8246-7316`)
  3. **Anirban Mukhopadhyay** (Department of Computer Science and Engineering, University of Kalyani, Kalyani, West Bengal, India; ORCID: `0000-0001-8128-3521`)
- **Submission Version Identifier:** `v2.0-final-submission` (`DMKD_Submission_Package`)
- **Reference PDF Filename:** `Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise.pdf`
- **Total Page Count:** **48 pages** (35-page main manuscript + 13-page Electronic Supplementary Material)
- **File Size:** 7,528,380 bytes
- **SHA-256 Checksum:** `b32259bfd704a7a7e6dd45e5717a731f0d8100d819cfd792911645e7da571a3c`

---

## 2. Structure of the Submitted 48-Page Manuscript

### Main Paper (Pages 1–35)
1. **Section 1: Introduction** — High-dimensional geometry ($D \gg N$), distance concentration, the core premise of subsample stability vs external accuracy.
2. **Section 2: Related Work** — Stability and consensus literature, feature selection in high dimensions, anchor graph methods, out-of-sample extension.
3. **Section 3: Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise**
   - *Section 3.1: Simulation Under Isotropic Distractor Noise* (Table 2, Figure 2a–c)
   - *Section 3.2: Evidence from Biomedical Cohorts* (Table 3, Table 4, Table 5, Figure 3)
4. **Section 4: Case Study: Gated Anchor Consensus (GAC)**
   - *Section 4.1: Bimodality-Gated Subspace Selection (BGSS)*
   - *Section 4.2: Bipartite Anchor Graph Consensus*
   - *Section 4.3: Stability-Weighted Active Subspace Centroid Assignment*
5. **Section 5: Experimental Setup & Multi-Domain Evaluation**
   - *Section 5.1: Multi-Domain Benchmark Parity & Negative Results* (Table 6)
   - *Section 5.2: Computational Scalability & Boundary Conditions* (Table 7, Table 8)
6. **Section 6: Ablation Study and Modular Decomposition**
   - *Section 6.1: Factorial Decomposition: Gating vs. Consensus Architecture* (Table 18)
   - *Section 6.2: High-Determinacy Anchor Selection Null Result* (Table 19)
7. **Section 7: Discussion, Recommendations, Limitations, and Future Work**
8. **Section 8: Conclusion**
9. **Declarations:** Mandatory Springer Nature statements (Funding, Conflicts of Interest, Ethics & Consent, Publication Consent, Data Availability, Code Availability, CRediT Author Contributions).

### Electronic Supplementary Material (Pages 36–48)
- **Section S1:** Computational Scalability and Extreme Memory Scaling ($N \le 10^6$ instances; Table S1, Table S2, Figure S2, Figure 6).
- **Section S2:** Out-of-Sample Inductive Generalization and Centroid Projections (Table S3, Figure S1, Figure 4a–b).
- **Section S3:** Multi-Domain 13-Dataset Benchmark Diagnostic Suite (13-panel gallery Figure 7a–n, Tables S4–S10).
- **Section S4:** Extended Modular Ablations and Noise Regimes (Tables S11–S12, Figure S5, Figure 10).

---

## 3. Manuscript-to-Repository Evidence Mapping

| Manuscript Item | Description | Authoritative Repository Artifact |
|---|---|---|
| **Table 1** | Summary of 6 biomedical cohorts ($N, D, D/N, K$) | `data/dataset_registry.csv` |
| **Table 2** | Synthetic distance geometries under isotropic noise | `src/icc/core.py`, `tests/unit/test_core.py` |
| **Table 3** | Primary 6-cohort stability–accuracy benchmark across 72 cells | `reproduction/scripts/recompute_saved_stability.py` |
| **Table 4** | Subsample degeneracy diagnostic audit (5% threshold) | `reproduction/scripts/recompute_saved_stability.py` |
| **Table 5** | Clustered bootstrap confidence intervals for primary gap | `docs/statistical-analysis.md`, `docs/result_dictionary.md` |
| **Table 6** | 13-dataset benchmark ARI and Friedman ranks | `reproduction/scripts/recompute_benchmark_scores.py` |
| **Table 7 (Supp S1)** | Runtime and peak RAM scaling across $N \in [500, 10{,}000]$ | `tests/regression/test_scaling_timing.py` |
| **Table 8 (Supp S1)** | Extreme scalability up to $N = 10^6$ samples (Config A & B) | `docs/result_dictionary.md`, `tests/regression/test_scaling_timing.py` |
| **Table 18** | $2 \times 2$ factorial decomposition (Ambient vs BGSS $\times$ Dense vs Bipartite) | `docs/result_dictionary.md`, `docs/experiment_catalog.md` |
| **Table 19** | Component knockout ablations ($V_5 \to V_0$) | `docs/result_dictionary.md`, `docs/experiment_catalog.md` |
| **Figure 1** | Conceptual overview diagram | `docs/scientific-overview.md` |
| **Figure 2a–c** | Synthetic simulation accuracy, stability, and noise sensitivity | `tests/unit/test_core.py` |
| **Figure 3** | Six-cohort empirical stability vs accuracy scatter plot | `reproduction/scripts/recompute_saved_stability.py` |
| **Figure 4** | GAC algorithmic workflow schematic | `src/icc/consensus/icc.py` |
| **Figure 6 (Supp S1)** | Empirical scalability curves up to $N = 10^6$ instances | `tests/regression/test_scaling_timing.py` |
| **Figure 7a–n (Supp S3)**| 13-panel empirical ARI boxplots | `reproduction/scripts/recompute_benchmark_scores.py` |

---

## 4. Post-Submission Improvements & Versioned Corrections

The submitted manuscript represents a frozen historical artifact. All updates made in this repository are versioned improvements and engineering hardening:

1. **Random-Gating Baseline Correction:**
   - *Historical Version:* Drew random feature subsets from inside the pre-filtered BGSS pool, reporting an inflated random baseline of $0.155$.
   - *Corrected Baseline:* Draws random feature subsets directly from ambient space $D$ without BGSS ranking, yielding the true unguided baseline of **$0.047$** (reported in Section 4.1).
2. **Title Harmonization:**
   - Harmonized all repository documentation, metadata (`pyproject.toml`, `CITATION.cff`, `.zenodo.json`), and CI configurations from earlier working title (*Stability Without Validity...*) to the submitted title (*Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*).
3. **DEC Implementation & Training Protocol Forensic:**
   - Fully audited the 221 differing DEC partitions between historical CPU Keras and fresh GPU PyTorch executions. Confirmed that all 11 non-DEC methods (3,960 partitions) are 100% bitwise identical.
4. **WDAC / AppLocker Robustness Fallbacks:**
   - Added pure-NumPy restricted unpicklers and fallbacks in `recompute_saved_stability.py` to allow verification in restricted enterprise execution environments without native C extension permissions.
