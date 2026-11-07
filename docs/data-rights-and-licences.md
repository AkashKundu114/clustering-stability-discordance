# Data Rights, Licensing, and Governance Framework

**Document:** `docs/data-rights-and-licences.md`  
**Date:** 2026-11-07  
**Project:** Stability-Accuracy Discordance in High-Dimensional Consensus Clustering  
**Target Journal:** Springer Nature — *Data Mining and Knowledge Discovery* (DMKD)

---

## 1. Governance Principles & Standards

In strict adherence to academic research ethics, copyright laws, and Springer Nature research data policies:

1. **Download Availability $\neq$ Redistribution Permission:**  
   The ability to download a dataset from an institutional website, personal repository, or competition server does not grant legal authority to redistribute the raw data in a GitHub repository or Zenodo archive.
2. **Upstream Copyright Ownership:**  
   Secondary aggregators (e.g., OpenML, Kaggle) cannot override the licensing terms or human-subject biobank restrictions established by the primary creators or hospital ethics committees.
3. **Protection of Clinical & Patient Data:**  
   Even de-identified clinical genomic microarrays must not be checked into public version control systems.
4. **Derived Artifact Safeguards:**  
   Partition files containing sample-level cluster assignment vectors indexed directly to hospital clinical observations are treated as confidential research materials.

---

## 2. Dataset-by-Dataset Rights Register

| Dataset | Canonical Upstream Endpoint | Upstream Host | Confirmed License / Terms | Classification Category | Public Redistribution Permitted? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Sonar** | UCI ID 151 / DOI: 10.24432/C5T88L | UCI ML Repository | **CC BY 4.0** | Category A — Public Open Access | **YES** (with attribution) |
| **Madelon** | UCI ID 171 / DOI: 10.24432/C5Z30F | UCI ML Repository | **CC BY 4.0** | Category A — Public Open Access | **YES** (with attribution) |
| **ISOLET** | UCI ID 54 / DOI: 10.24432/C51G69 | UCI ML Repository | **CC BY 4.0** | Category A — Public Open Access | **YES** (with attribution) |
| **20 Newsgroups** | UCI ID 113 / DOI: 10.24432/C5C323| UCI ML Repository | **CC BY 4.0** | Category A — Public Open Access | **YES** (with attribution) |
| **PBMC68k-red** | 10x Genomics Dataset Portal | 10x Genomics / Scanpy | **CC BY 4.0** | Category A — Public Open Access | **YES** (with attribution) |
| **Indian Pines** | UPV/EHU Hyperspectral Archive | Univ. Basque Country (UPV/EHU) | Academic Research Use | Category B — Source-Fetch-Only | **NO** (Direct fetch only) |
| **Yale Face B** | Yale CVC Face Database B | Yale University CVC / UCSD | Research Use Only; Redistribution Prohibited | Category C — Restricted Redistribution | **NO** (Database bundling strictly prohibited) |
| **CNS** | OpenML ID 45086 | OpenML / Broad Institute | Biobank Research Data | Category B — Source-Fetch-Only | **NO** (API fetch only; DUA for review) |
| **Colon** | OpenML ID 45087 | OpenML / Princeton Biobank | Biobank Research Data | Category B — Source-Fetch-Only | **NO** (API fetch only; DUA for review) |
| **Leukemia** | OpenML ID 1104 | OpenML / Whitehead Inst. | Biobank Research Data | Category B — Source-Fetch-Only | **NO** (API fetch only; DUA for review) |
| **Ovarian** | OpenML ID 45098 | OpenML / FDA-NCI Proteomics | Clinical Research Data | Category B — Source-Fetch-Only | **NO** (API fetch only; DUA for review) |
| **Prostate** | OpenML ID 45099 | OpenML / Brigham & Women's | Biobank Research Data | Category B — Source-Fetch-Only | **NO** (API fetch only; DUA for review) |
| **SRBCT** | OpenML ID 45101 | OpenML / NIH NHGRI | Pediatric Biopsy Data | Category B — Source-Fetch-Only | **NO** (API fetch only; DUA for review) |

---

## 3. Artifact Bifurcation: Public vs. Confidential Reviewer Packages

All $8{,}649$ empirical evaluation artifacts generated during this study are classified into two strictly separated distributions:

### 3.1 Public-Eligible Open-Access Distribution ($4{,}323$ files)
- **Manifest:** `data/manifests/public_artifacts.csv`
- **Included Content:**
  - $4{,}320$ execution telemetry files (`results/stability/runs/*.parquet`): Contain runtime, seed schedules, iteration counts, convergence status, sample count, and summary accuracy metrics. Zero patient features, raw spectra, or facial images.
  - $1$ subsample stability grand summary table (`results/stability/subsample_stability_summary.csv`).
  - $2$ historical multi-domain benchmark score tables (`benchmark_matrix_passF.csv`, `exp3_cohirf_benchmark.csv`).
- **Permitted Destinations:** Public GitHub candidate repository, open Zenodo data deposition upon paper acceptance.

### 3.2 Access-Controlled Confidential Reviewer Package ($4{,}326$ files)
- **Manifest:** `data/manifests/restricted_artifacts.csv`
- **Included Content:**
  - $4{,}320$ partition integer arrays (`results/stability/partitions/*.npy`): Contain 1D cluster assignment vectors indexed directly to individual patient biopsy observations.
  - $6$ preprocessed clinical feature caches (`data/cache/*.npz`): Contain microarray gene expression and mass spectrometry intensity matrices.
- **Handling Protocol:**
  - **NEVER** committed to public Git branches or public repository mirrors.
  - Deposited confidentially via DMKD Editorial Manager under **"Supplementary Material for Review Only"**.
  - Accessible to journal editors and appointed peer reviewers under a research Data Use Agreement (DUA).

---

## 4. Third-Party Formal Inquiries

To maintain full institutional transparency, formal clarification inquiries have been drafted for third-party entities:
1. **Yale Center for Computational Vision and Control (`cvc-support@cs.yale.edu`):** Requesting confirmation that dynamic script-based fetch conforms to Yale CVC non-redistribution terms.
2. **Computational Intelligence Group, UPV/EHU (`manuel.grana@ehu.eus`):** Inquiring regarding persistent academic citation requirements for the corrected Indian Pines flight line product.
