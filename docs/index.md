# CSD Documentation: Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise

**Manuscript Title:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*  
**Running Header:** *Feature-Gated Bipartite Consensus Under Noise*  
**Authors:** Kalyan Kumar Das, Akash Kundu, Anirban Mukhopadhyay  
**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)  
**Companion Repository:** [https://github.com/AkashKundu114/icc-clustering](https://github.com/AkashKundu114/icc-clustering)  

This documentation suite describes the reproducible research software, data loaders, governance protocols, and empirical findings for the investigation of clustering stability-accuracy discordance across **13 benchmark datasets** and **12 comparative clustering algorithms**.

---

## Start Here

- [Scientific Overview](scientific-overview.md): executive summary, distance concentration, and null calibration.
- [Reviewer Reproduction Guide](reviewer-reproduction.md): 40-second fast-track verification of core numerical claims.
- [Research Questions](research-questions.md): empirical findings for RQ1, RQ2, and RQ3.
- [Research Overview](research-overview.md): question, scope, and interpretation.
- [Methodology](methodology.md): the distinct stability and external-ARI designs.
- [Experimental Protocol](experimental-protocol.md): formal decision rules, combinatorics, and comparative algorithms.
- [Datasets and Provenance](datasets-and-provenance.md): domain characteristics, sample sizes, and accessions.
- [Dataset Access and Terms](datasets.md): upstream terms, licensing status, and cautions.
- [Data Rights and Governance](data-rights-and-licences.md): four-tier data governance framework.
- [Results and Interpretation](results-and-interpretation.md): primary empirical findings, reconciliation, and Friedman analysis.
- [Results Release Status](results.md): result-package availability and evidence limits.
- [Statistical Analysis](statistical-analysis.md): estimands, dependence, and sensitivity.
- [Limitations](limitations.md): evidence boundaries and implementation caveats.
- [Reproducibility](reproducibility.md): current tested status across three evidence tiers.
- [Compute Requirements](compute-requirements.md): hardware profiles and the 16 GB memory boundary.
- [Saved-Output Verification Tools](../reproduction/README.md): portable recalculation commands and evidence inputs.
- [Software Architecture](software-architecture.md): code layout and module hierarchy.
- [Setup and Environments](setup.md): installation and tested Python environments.
- [Citation](citation.md): software citation, paper bibliography, and DOI status.
- [Release Process](release-process.md): verification gates and release engineering.
- [Glossary](glossary.md): terminology used throughout the documentation.
- [FAQ](faq.md): common practical questions.

The code API is under `src/`; package metadata and dependencies are in `pyproject.toml`; dataset registry configuration is in `configs/datasets.yaml`; command-line helpers are under `scripts/`; tests are under `tests/`.
