# Dataset Inventory, Provenance, and Domain Characteristics

**Document:** `docs/datasets-and-provenance.md` 
**Date:** 2026-11-07 
**Project:** Stability-Accuracy Discordance in High-Dimensional Consensus Clustering 

---

## 1. Complete Dataset Registry Summary

The empirical investigation encompasses 13 multi-domain benchmark datasets, divided into two distinct experimental frameworks:
1. **The Six-Cohort Stability Study:** Six biomedical microarray cohorts exhibiting extreme feature-to-sample ratios ($D/N > 20$), subjected to $80\%$ stratified subsampling, real vs. column-permuted null evaluations ($62{,}640$ pairwise comparisons across 72 cells), and post-hoc non-degeneracy audits.
2. **The 13-Dataset Multi-Domain Benchmark:** An exploratory historical baseline comparing 12 clustering algorithms across diverse tabular, acoustic, speech, hyperspectral, text, and computer vision domains ($3{,}000$ assembled score records from $1{,}430$ planned fits; fresh clean rerun partial at $892$ fits).

| Dataset Identifier | Domain / Modality | Samples ($N$) | Features ($D$) | Ratio ($D/N$) | Classes ($K$) | Primary Accession / Canonical Link | Original Publication |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Part I: High-$D$ Biomedical Cohorts** | | | | | | | |
| `cns` | Pediatric Brain Tumors | 60 | 7,129 | 118.82 | 2 | [OpenML 45086](https://www.openml.org/d/45086) | Pomeroy et al., *Nature* (2002) |
| `colon` | Colon Carcinoma | 62 | 2,000 | 32.26 | 2 | [OpenML 45087](https://www.openml.org/d/45087) | Alon et al., *PNAS* (1999) |
| `leukemia` | Acute Leukemia (ALL/AML)| 72 | 7,129 | 99.01 | 2 | [OpenML 1104](https://www.openml.org/d/1104) | Golub et al., *Science* (1999) |
| `ovarian` | Ovarian Mass Spectrometry| 253 | 15,154| 59.90 | 2 | [OpenML 45098](https://www.openml.org/d/45098) | Petricoin et al., *Lancet* (2002) |
| `prostate` | Prostate Microarray | 102 | 12,600| 123.53 | 2 | [OpenML 45099](https://www.openml.org/d/45099) | Singh et al., *Cancer Cell* (2002) |
| `srbct` | Childhood Solid Tumors | 83 | 2,308 | 27.81 | 4 | [OpenML 45101](https://www.openml.org/d/45101) | Khan et al., *Nature Med.* (2001) |
| **Part II: Multi-Domain Benchmarks** | | | | | | | |
| `sonar` | Acoustic Sonar Signals | 208 | 60 | 0.29 | 2 | [UCI 151](https://archive.ics.uci.edu/dataset/151) | Gorman & Sejnowski (1988) |
| `madelon` | Synthetic Non-Linear | 500* | 500 | 1.00 | 2 | [UCI 171](https://archive.ics.uci.edu/dataset/171) | Guyon et al., *NIPS* (2003) |
| `isolet` | Acoustic Spoken Letters | 7,797 | 617 | 0.08 | 26 | [UCI 54](https://archive.ics.uci.edu/dataset/54) | Fanty & Cole (1991) |
| `pbmc68k_red`| Single-Cell RNA-seq | 700 | 765 | 1.09 | 10 | [10x Genomics](https://www.10xgenomics.com) | Zheng et al., *Nat. Commun.* (2017) |
| `newsgroups20`| Document TF-IDF Text | 18,846| 10,000| 0.53 | 20 | [UCI 113](https://archive.ics.uci.edu/dataset/113) | Lang, *ICML* (1995) |
| `indian_pines`| Hyperspectral Imaging | 10,249| 200 | 0.02 | 16 | [UPV/EHU](http://www.ehu.eus/ccwintco)| Landgrebe et al., Purdue (1992) |
| `yale_b` | Cropped Face Manifolds | 2,414 | 1,024 | 0.42 | 38 | [Yale CVC](https://cvc.cs.yale.edu) | Georghiades et al., *TPAMI* (2001) |

*\*Madelon evaluated on deterministic 500-sample balanced subsample.*

---

## 2. Granular Dataset Descriptions & Biological Modalities

### 2.1 Central Nervous System Embryonal Tumors (`cns`)
- **Biological Origin:** Gene expression profiles of pediatric embryonal central nervous system tumors.
- **Reference Label Structure:** Binary division between survivors and non-survivors under adjuvant chemotherapy/radiotherapy.
- **Dimensionality Profile:** $N = 60, D = 7{,}129$ Affymetrix oligonucleotide features. $D/N = 118.82$.
- **Signal-to-Noise Profile:** Extreme distance concentration. Unsupervised clustering baseline methods repeatedly converge to high subsample stability ($\text{Stab} \ge 0.54$) while yielding near-zero correlation with clinical outcome ($\text{Acc} \le 0.02$).

### 2.2 Colon Carcinoma Gene Expression (`colon`)
- **Biological Origin:** Affymetrix hum60k oligonucleotide array measurements of 40 colon tumor specimens and 22 normal colon tissue biopsies.
- **Reference Label Structure:** Binary pathology annotation (tumor vs. normal mucosa).
- **Dimensionality Profile:** $N = 62, D = 2{,}000$ high-variance expressed genes selected from raw probe set. $D/N = 32.26$.
- **Discordance Findings:** Classical and spectral methods converge to stability $\sim 0.55$, but empirical accuracy against tumor/normal distinction hovers between $-0.02$ and $+0.07$.

### 2.3 Golub Acute Leukemia (`leukemia`)
- **Biological Origin:** Bone marrow RNA hybridization from acute lymphoblastic leukemia (ALL, $n=47$) and acute myeloid leukemia (AML, $n=25$) patients.
- **Reference Label Structure:** Binary diagnostic classification (ALL vs. AML).
- **Dimensionality Profile:** $N = 72, D = 7{,}129$ expression levels. $D/N = 99.01$.
- **Signal Profile:** Possesses clear multimodal biological signal along lineage markers (CD19, myeloperoxidase). GAC achieves elevated accuracy ($\text{Acc} = 0.600 \pm 0.367$) by isolating bimodal coordinates via BGSS.

### 2.4 Ovarian Cancer Proteomic Spectra (`ovarian`)
- **Biological Origin:** Surface-Enhanced Laser Desorption and Ionization Time-of-Flight (SELDI-TOF) mass spectrometry from serum samples (FDA-NCI Clinical Proteomics Program).
- **Reference Label Structure:** Binary classification between benign/healthy controls ($n=91$) and ovarian epithelial carcinoma ($n=162$).
- **Dimensionality Profile:** $N = 253, D = 15{,}154$ mass-to-charge ($m/z$) intensity channels. $D/N = 59.90$.
- **Discordance Findings:** Classical methods yield persistent stability ($\text{Stab} \sim 0.77$ for FCM) while accuracy against cancer status remains zero ($\text{Acc} = 0.002$).

### 2.5 Prostate Microarray (`prostate`)
- **Biological Origin:** Radical prostatectomy specimens hybridised on Affymetrix microarrays (Singh et al., 2002).
- **Reference Label Structure:** 52 prostate tumors and 50 non-tumor prostate tissue specimens.
- **Dimensionality Profile:** $N = 102, D = 12{,}600$ probe sets. $D/N = 123.53$.
- **Discordance Findings:** Demonstrates the most acute discordance in the benchmark. Ward hierarchical clustering achieves subsample stability of $0.996$ and Spectral clustering achieves $0.971$, but both have empirical accuracy near zero ($0.026$ and $-0.002$, respectively). PCA diagnostics show that base clusterers latch onto outlier clusters and total expression variance rather than tumor pathology.

### 2.6 Small Round Blue Cell Tumors (`srbct`)
- **Biological Origin:** cDNA microarray hybridizations of childhood round-cell tumors.
- **Reference Label Structure:** 4 distinct diagnostic categories: neuroblastoma (NB), rhabdomyosarcoma (RMS), non-Hodgkin lymphoma (Burkitt lymphoma, BL), and Ewing family of tumors (EWS).
- **Dimensionality Profile:** $N = 83, D = 2{,}308$ gene expression coordinates. $D/N = 27.81$.
- **Signal Profile:** Distinct 4-class multi-class separation, where GAC feature gating yields $\text{Acc} = 0.546 \pm 0.102$.

---

## 3. Data Acquisition & Validation Commands

All datasets are retrievable via scripted acquisition tools:

```bash
# Fetch open-access UCI and single-cell benchmarks (CC BY 4.0)
python scripts/fetch_data.py --tier open

# Load UPV/EHU Indian Pines hyperspectral scene
python -c "from icc.datasets.spectral import load_indian_pines; X, y = load_indian_pines(); print(X.shape)"

# Load Yale Face B face manifolds with SHA-256 validation
python -c "from icc.datasets.image import load_yale_b; X, y = load_yale_b(); print(X.shape)"
```
