# Data Governance & Redistribution Rights Register

**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)
**Submitted Manuscript Reference:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*
**Audited Baseline Commit:** `44838fa`

To guarantee ethical compliance and adhere strictly to copyright, clinical biobank access terms, and third-party data licenses, this repository classifies all 13 evaluated benchmark datasets into three distinct governance categories.

---

## 1. Governance Categories

### Category A — Public Open Access (Permissive Redistribution)
These datasets are distributed under standard, permissive open-source licenses (primarily Creative Commons Attribution 4.0 International, CC BY 4.0). They may be freely accessed, processed, and redistributed with appropriate academic attribution:

1. **`sonar` (Connectionist Bench Sonar, Mines vs. Rocks):**
   - *Publisher:* Gorman & Sejnowski (1988) / UCI Machine Learning Repository
   - *License:* CC BY 4.0 (DOI: `10.24432/C5T88L`)
   - *Acquisition:* Direct UCI download or OpenML API (`openml.org/d/40`).
2. **`madelon` (NIPS 2003 Feature Selection Challenge):**
   - *Publisher:* Guyon et al. (2003) / UCI Machine Learning Repository
   - *License:* CC BY 4.0 (DOI: `10.24432/C5Z30F`)
   - *Acquisition:* Direct UCI download or OpenML API (`openml.org/d/1485`).
3. **`isolet` (Isolated Letter Speech Recognition):**
   - *Publisher:* Fanty & Cole (1991) / UCI Machine Learning Repository
   - *License:* CC BY 4.0 (DOI: `10.24432/C51G69`)
   - *Acquisition:* Direct UCI download or OpenML API (`openml.org/d/300`).
4. **`newsgroups20` (Twenty Newsgroups):**
   - *Publisher:* Lang (1995) / CMU / scikit-learn
   - *License:* CC BY 4.0 (DOI: `10.24432/C5C323`)
   - *Acquisition:* Automated scikit-learn fetcher (`sklearn.datasets.fetch_20newsgroups`).
5. **`zheng68k` (PBMC68k Single-Cell Transcriptomics):**
   - *Publisher:* Zheng et al. (2017) / 10x Genomics
   - *License:* CC BY 4.0 (10x Genomics Open Access)
   - *Acquisition:* Automated Scanpy reduced loader (`scanpy.datasets.pbmc68k_reduced`).

---

### Category B — Source-Fetch-Only (Clinical Microarrays & University Endpoints)
These datasets originate from clinical human tissue biopsies or university server archives. To preserve donor privacy, satisfy biobank data-use agreements, and comply with institutional terms, **raw expression matrices and patient-level sample identifiers are not redistributed in the public Git repository**. Instead, users and reviewers acquire the data dynamically from authorized upstream repositories:

6. **`cns` (Central Nervous System Embryonal Tumors):**
   - *Publisher:* Pomeroy et al. (Nature 2002) / Dana-Farber Cancer Institute
   - *Upstream Host:* OpenML Dataset ID `45086` (`openml.org/d/45086`)
   - *Dimensions:* $N=60, D=7{,}129, K=5$
7. **`colon` (Colon Cancer Gene Expression):**
   - *Publisher:* Alon et al. (PNAS 1999) / Princeton University
   - *Upstream Host:* OpenML Dataset ID `45087` (`openml.org/d/45087`)
   - *Dimensions:* $N=62, D=2{,}000, K=2$
8. **`leukemia` (Golub Acute Leukemia ALL vs. AML):**
   - *Publisher:* Golub et al. (Science 1999) / Whitehead Institute & Broad Institute
   - *Upstream Host:* OpenML Dataset ID `1104` (`openml.org/d/1104`)
   - *Dimensions:* $N=72, D=7{,}129, K=3$
9. **`ovarian` (Ovarian Cancer Mass Spectrometry SELDI):**
   - *Publisher:* Petricoin et al. (Lancet 2002) / FDA-NCI Clinical Proteomics Program
   - *Upstream Host:* OpenML Dataset ID `45098` (`openml.org/d/45098`)
   - *Dimensions:* $N=253, D=15{,}154, K=2$
10. **`prostate` (Prostate Adenocarcinoma Microarray):**
    - *Publisher:* Singh et al. (Cancer Cell 2002) / Brigham & Women's Hospital & Harvard Medical School
    - *Upstream Host:* OpenML Dataset ID `45099` (`openml.org/d/45099`)
    - *Dimensions:* $N=102, D=12{,}600, K=2$
11. **`srbct` (Small Round Blue Cell Tumors):**
    - *Publisher:* Khan et al. (Nature Medicine 2001) / NIH National Human Genome Research Institute (NHGRI)
    - *Upstream Host:* OpenML Dataset ID `45101` (`openml.org/d/45101`)
    - *Dimensions:* $N=83, D=2{,}308, K=4$
12. **`indian_pines` (Hyperspectral Remote Sensing Flight Line):**
    - *Publisher:* Purdue University / Universidad del País Vasco (UPV/EHU) Computational Intelligence Group
    - *Upstream Host:* UPV/EHU University Server (`http://www.ehu.eus/ccwintco/uploads/6/67/Indian_pines_corrected.mat`)
    - *License:* Academic Research Use Only with institutional attribution.

---

### Category C — Restricted Redistribution (Explicit Legal Proscription)
13. **`yale_b` (Extended Yale Face Database B):**
    - *Publisher:* Georghiades et al. (IEEE TPAMI 2001) / Yale Center for Computational Vision and Control (CVC)
    - *Upstream Host:* `https://cvc.cs.yale.edu/cvc/projects/yalefacesB/yalefacesB.html`
    - *Redistribution Clause:* Yale CVC terms explicitly state:
      > *"Without permission from Yale University, images cannot be incorporated into a larger database which is then publicly distributed."*
    - *Compliance Protocol:* Bundling raw Yale B face images into Git, GitHub, or Zenodo releases is legally prohibited. The repository strictly enforces dynamic acquisition via `src/icc/datasets/image.py` with hash verification (`tests/unit/test_yale_b_download_integrity.py`).

---

## 2. Dynamic Data Fetch Hook

All Category A and Category B datasets can be fetched and preprocessed using the automated tool:

```powershell
# Fetch specific dataset via official upstream API
python scripts/fetch_data.py --dataset leukemia

# Run unsupervised preprocessing
python scripts/prepare_data.py --dataset leukemia
```
