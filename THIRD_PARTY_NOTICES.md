# Third-Party Notices and Dataset Terms of Use

This repository incorporates, references, or interfaces with open-source software libraries, benchmark dataset repositories, and scientific archives. This document details the upstream copyrights, licenses, and terms of use governing these third-party components.

---

## 1. Third-Party Benchmark Datasets

### 1.1 Creative Commons Attribution 4.0 International (CC BY 4.0)

The following datasets are distributed under the terms of the Creative Commons Attribution 4.0 International license:

- **Sonar (Connectionist Bench):**
 - **Host:** UC Irvine Machine Learning Repository (UCI ID: 151)
 - **DOI:** [10.24432/C5T88L](https://doi.org/10.24432/C5T88L)
 - **Creators:** R. Paul Gorman and Terrence J. Sejnowski (1988)
 - **License:** CC BY 4.0

- **Madelon:**
 - **Host:** UC Irvine Machine Learning Repository (UCI ID: 171)
 - **DOI:** [10.24432/C5Z30F](https://doi.org/10.24432/C5Z30F)
 - **Creators:** Isabelle Guyon, Steve Gunn, Asa Ben-Hur, Gideon Dror (2003)
 - **License:** CC BY 4.0

- **ISOLET (Isolated Letter Speech Recognition):**
 - **Host:** UC Irvine Machine Learning Repository (UCI ID: 54)
 - **DOI:** [10.24432/C51G69](https://doi.org/10.24432/C51G69)
 - **Creators:** Mark Fanty and Ronald Cole (1991)
 - **License:** CC BY 4.0

- **Twenty Newsgroups:**
 - **Host:** UC Irvine Machine Learning Repository (UCI ID: 113)
 - **DOI:** [10.24432/C5C323](https://doi.org/10.24432/C5C323)
 - **Creator:** Ken Lang (1995)
 - **License:** CC BY 4.0

- **PBMC68k (Demonstration Single-Cell RNA-Seq):**
 - **Host:** 10x Genomics Dataset Portal
 - **Reference:** Zheng et al., *Nature Communications* (2017)
 - **License:** Creative Commons Attribution 4.0 International (10x Genomics Open Access Demonstration Data)

---

### 1.2 Upstream University Endpoints & Controlled Redistribution

- **Indian Pines Hyperspectral Scene:**
 - **Origin:** Airborne Visible / Infrared Imaging Spectrometer (AVIRIS), Purdue University Campus
 - **Host Repository:** Computational Intelligence Group, University of the Basque Country (UPV/EHU)
 - **Endpoint URL:** `http://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes`
 - **Terms:** Freely available for non-commercial academic research. Redistribution within public package bundles is omitted in favor of direct endpoint retrieval via `icc.datasets.spectral.load_indian_pines`.

- **Extended Yale Face Database B:**
 - **Origin:** Yale Center for Computational Vision and Control (CVC) / University of California, San Diego (UCSD)
 - **Reference:** A.S. Georghiades, P.N. Belhumeur, and D.J. Kriegman, IEEE TPAMI (2001)
 - **Restricted Redistribution Notice:**
 > *"Without permission from Yale University, images from within the database cannot be incorporated into a larger database which is then publicly distributed."*
 - **Compliance Action:** Yale Face B image files are **NEVER distributed in this repository**. The automated loader (`icc.datasets.image.load_yale_b`) fetches the archive directly from the authorized distribution server with cryptographic checksum and array-structure validation.

---

### 1.3 Clinical Biomedical Cohorts (OpenML API / Hospital Biobanks)

The six high-dimensional biomedical cohorts analyzed in this work are de-identified secondary research data hosted on the OpenML platform:

1. **CNS Embryonal Tumors:** OpenML ID 45086 (Pomeroy et al., *Nature* 2002)
2. **Colon Adenocarcinoma:** OpenML ID 45087 (Alon et al., *PNAS* 1999)
3. **Golub Acute Leukemia:** OpenML ID 1104 (Golub et al., *Science* 1999)
4. **Ovarian Cancer Mass Spectrometry:** OpenML ID 45098 (Petricoin et al., *Lancet* 2002)
5. **Prostate Microarray:** OpenML ID 45099 (Singh et al., *Cancer Cell* 2002)
6. **Small Round Blue Cell Tumors (SRBCT):** OpenML ID 45101 (Khan et al., *Nature Medicine* 2001)

**Compliance Notice:** 
All clinical cohorts consist of de-identified historical research data exempt from human subject consent requirements under institutional review board secondary analysis provisions. Raw patient expression arrays are accessed directly via the OpenML API without author redistribution. Evaluation partition arrays are safeguarded under a confidential peer-review Data Use Agreement (DUA).

---

## 2. Open-Source Python Software Libraries

This project links against and utilizes several open-source libraries under permissive licenses:

- **NumPy** (`BSD-3-Clause`): Copyright (c) 2005-2026, NumPy Developers.
- **SciPy** (`BSD-3-Clause`): Copyright (c) 2001-2026, SciPy Developers.
- **pandas** (`BSD-3-Clause`): Copyright (c) 2008-2026, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team.
- **scikit-learn** (`BSD-3-Clause`): Copyright (c) 2007-2026, scikit-learn developers.
- **PyTorch** (`Modified BSD`): Copyright (c) 2016-present, Meta Platforms, Inc. and affiliates.
- **PyYAML** (`MIT License`): Copyright (c) 2017-2026, Ingy döt Net, Kirill Simonov.
