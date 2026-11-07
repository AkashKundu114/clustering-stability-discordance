# Data Dictionary and Variable Definitions

**Document:** `docs/data-dictionary.md` 
**Date:** 2026-11-07 
**Project:** Stability-Accuracy Discordance in High-Dimensional Consensus Clustering 

---

## 1. Summary Tables & Recomputed Metrics

### Schema for `results/stability/subsample_stability_summary.csv` and `recomputed_cells.csv`:

| Column Name | Data Type | Description | Permitted Values / Range |
| :--- | :--- | :--- | :--- |
| `cohort` | `string` | Benchmark biomedical cohort identifier | `cns`, `colon`, `leukemia`, `ovarian`, `prostate`, `srbct` |
| `method` | `string` | Clustering algorithm evaluated | `K-Means`, `Ward`, `Spectral`, `FCM`, `StdCons`, `CoreHalo`, `DEC`, `FCAG`, `FastMVC`, `CoHiRF`, `UngatedAC`, `GAC` |
| `subsample_stability` | `float64` | Mean pairwise ARI across 435 subsample pairs on real data | $[-0.5, 1.0]$ |
| `subsample_accuracy` | `float64` | Mean external ARI against clinical diagnostic reference labels | $[-0.5, 1.0]$ |
| `discordance_gap` | `float64` | Difference between stability and accuracy ($\text{Stab} - \text{Acc}$) | $[-1.0, 2.0]$ |
| `null_stability` | `float64` | Mean pairwise ARI on column-permuted null data | $[-0.1, 0.5]$ |
| `rule_i_met` | `boolean` | True if $\text{Stab} \ge 0.50$ and $\text{Acc} \le 0.05$ | `True`, `False` |
| `rule_i_prime_met` | `boolean` | True if Rule (i) met AND non-degenerate (min cluster $\ge 5\%$ in $\ge 90\%$ runs) | `True`, `False` |
| `rule_ii_met` | `boolean` | True if $\text{Stab}_{\text{real}} - \text{Stab}_{\text{null}} < 0.10$ | `True`, `False` |

---

## 2. Per-Fit Parquet Execution Telemetry Logs

### Schema for `results/stability/runs/*.parquet`:

| Column Name | Data Type | Description | Privacy / Leakage Audit Status |
| :--- | :--- | :--- | :--- |
| `dataset` | `string` | Cohort identifier (e.g., `cns`, `colon`) | Non-sensitive categorical identifier |
| `model` | `string` | Algorithm name (e.g., `CoHiRF`, `GAC`) | Non-sensitive categorical identifier |
| `mode` | `string` | Experimental mode: `real` or `null` | Non-sensitive protocol flag |
| `subsample_id` | `int64` | Draw index within experimental cell ($0$ to $29$) | Integer counter |
| `sub_seed` | `int64` | Subsample random seed schedule value | Deterministic integer seed |
| `null_seed` | `int64` | Null permutation random seed value | Deterministic integer seed |
| `status` | `string` | Execution outcome: `success`, `failed` | Process status string |
| `runtime` | `float64` | Model execution elapsed wall-clock seconds | Non-sensitive numeric benchmark metric |
| `accuracy` | `float64` | Adjusted Rand Index against external reference (NaN on null) | Summary scalar evaluation metric |
| `n_samples` | `int64` | Number of observations in $80\%$ subsample draw | Integer sample count |

---

## 3. Mathematical Notation & Symbols

| Symbol | Mathematical Definition | Context in Manuscript |
| :--- | :--- | :--- |
| $N$ | Number of samples / observations | Dataset sample size |
| $D$ | Number of dimensions / features | Total feature dimension |
| $K$ | Number of clusters / ground-truth classes | Prespecified cluster count |
| $M$ | Number of base clusterers in ensemble | Default: $M=25$ |
| $L$ | Number of anchor landmarks in bipartite graph | Default: $L=40$ ($L \ll N$) |
| $\alpha$ | Proportion of features sampled in random subspace | Default: $\alpha = 0.15$ |
| $\text{ARI}$ | Adjusted Rand Index | Chance-corrected partition agreement |
| $\Delta$ | Discordance gap ($\text{Stab} - \text{Acc}$) | Degree of stability-accuracy discrepancy |
| $\chi_F^2$ | Non-parametric Friedman test statistic | Omnibus rank comparison across 13 datasets |
| $\text{CD}$ | Nemenyi Critical Difference | Significance threshold for post-hoc rank groups |
