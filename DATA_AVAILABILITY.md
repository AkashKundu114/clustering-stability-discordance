# Data Availability Statement

**Manuscript Title:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*  
**Running Header:** *Feature-Gated Bipartite Consensus Under Noise*  
**Authors:** Kalyan Kumar Das (Techno India University), Akash Kundu (Techno India University), Anirban Mukhopadhyay (University of Kalyani)  
**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)  
**Companion Repository:** [https://github.com/AkashKundu114/icc-clustering](https://github.com/AkashKundu114/icc-clustering)  

---

## 1. Overview and Scope

This research empirically examines stability-accuracy discordance across **13 benchmark datasets** evaluated over **12 comparative clustering algorithms**. In adherence to research ethics, biobank data governance, and institutional licensing requirements, data assets and empirical evaluation artifacts are structured under a four-tiered availability model.

The full details of dataset provenance, citations, and access rights are documented in [docs/datasets.md](docs/datasets.md), [docs/data-rights-and-licences.md](docs/data-rights-and-licences.md), and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

---

## 2. Four-Tiered Data Governance Framework

| Governance Tier | Classification Scope | Datasets / Artifacts Included | Public Availability & Access Procedure |
| :--- | :--- | :--- | :--- |
| **Tier A (Committed Code & Manifests)** | Open-source software, configs, test suites, and integrity manifests. | Benchmark configs (`configs/`), synthetic smoke data, artifact checksums (`data/manifests/`). | Immediately available under MIT license in the repository. |
| **Tier B (Deterministic Source-Fetch)** | Public open-access benchmark datasets. | **Sonar** (UCI 151), **Madelon** (UCI 171), **ISOLET** (UCI 54), **20 Newsgroups** (UCI 113), **PBMC68k-red** (10x Genomics), **Indian Pines** (UPV/EHU). | Freely accessible from canonical upstream repositories via deterministic acquisition scripts with SHA-256 integrity checks. |
| **Tier C (Restricted Redistribution)** | Academic research-only benchmarks with non-redistribution clauses. | **Extended Yale Face Database B** (Yale University CVC / UCSD). | Raw images cannot be redistributed in public archives per Yale CVC terms. The automated fetcher retrieves files directly from authorized institutional endpoints. |
| **Tier D (Confidential Reviewer Package)** | High-$D$ clinical biomedical cohorts & patient-level partition arrays. | **CNS** (OpenML 45086), **Colon** (OpenML 45087), **Leukemia** (OpenML 1104), **Ovarian** (OpenML 45098), **Prostate** (OpenML 45099), **SRBCT** (OpenML 45101), plus 4,320 partition arrays (`.npy`) and clinical caches (`.npz`). | De-identified clinical genomic matrices and derived patient-indexed partitions are safeguarded under a confidential peer-review Data Use Agreement (DUA). Reviewers can verify all arithmetic in ~50 seconds via Tier 1 tools (`reproduction/scripts/recompute_saved_stability.py`). |

---

## 3. Benchmark Datasets and Comparative Algorithms

The study evaluates across:
- **13 Benchmark Datasets:**
  1. CNS Embryonal Tumors ($N=60, D=7,129, K=2$)
  2. Colon Carcinoma ($N=62, D=2,000, K=2$)
  3. Golub Acute Leukemia ($N=72, D=7,129, K=2$)
  4. Ovarian Cancer Proteomics ($N=253, D=15,154, K=2$)
  5. Prostate Microarray ($N=102, D=12,600, K=2$)
  6. Small Round Blue Cell Tumors [SRBCT] ($N=83, D=2,308, K=4$)
  7. Sonar Connectionist Bench ($N=208, D=60, K=2$)
  8. Madelon Synthetic Manifold ($N=500, D=500, K=2$)
  9. ISOLET Spoken Letter Recognition ($N=7,797, D=617, K=26$)
  10. 20 Newsgroups Document Text ($N=18,846, D=10,000, K=20$)
  11. PBMC68k Reduced Single-Cell RNA-seq ($N=700, D=765, K=10$)
  12. Indian Pines Hyperspectral Scene ($N=10,249, D=200, K=16$)
  13. Extended Yale Face Database B ($N=2,414, D=1,024, K=38$)

- **12 Comparative Algorithms:**
  1. K-Means
  2. Ward Hierarchical Clustering
  3. Spectral Clustering
  4. Fuzzy C-Means (FCM)
  5. Standard Consensus Clustering (StdCons / Monti)
  6. Core-Halo Consensus
  7. Deep Embedding Clustering (DEC)
  8. Fast Consensus with Anchor Graphs (FCAG)
  9. Fast Multi-View Consensus (FastMVC)
  10. CoHiRF (Hierarchical Random Forest Consensus)
  11. Ungated Anchor Consensus (Ungated AC / ICC-v1)
  12. Gated Anchor Consensus (GAC / ICC-v2)

---

## 4. Citation and Rights Policy

Raw benchmark data and patient cohorts remain the property of their respective creators and biobanks. Software components are licensed under the MIT license. For citation guidelines and software releases, refer to [`docs/citation.md`](docs/citation.md) and [`CITATION.cff`](CITATION.cff).
