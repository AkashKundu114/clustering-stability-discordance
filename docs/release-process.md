# Release Engineering and Publication Gate Process

**Document:** `docs/release-process.md` 
**Date:** 2026-11-07 
**Candidate Version:** `v1.0.0-rc1` 
**Final Release Target:** `v1.0.0` 

---

## 1. Release Architecture & Naming Strategy

### 1.1 Repository Identity
- **Current Repository:** `AkashKundu114/icc-clustering`
- **Proposed Public Candidate Name:** `clustering-stability-discordance`
- **Proposed Public Title:** **Clustering Stability-Accuracy Discordance in High-Dimensional Biomedical Data**
- **Description:** "Reproducible research code, saved-evidence reconstruction tools, and documentation for an empirical study of resampling stability and external-label alignment in high-dimensional biomedical clustering."
- **Topics:** `clustering`, `consensus-clustering`, `clustering-stability`, `high-dimensional-data`, `biomedical-data`, `unsupervised-learning`, `statistical-learning`, `reproducible-research`, `data-mining`, `computational-biology`, `research-software`, `python`.

### 1.2 Renaming vs. Mirror Repository Strategy
Before renaming the existing repository on GitHub:
1. GitHub automatically redirects HTTP clone requests, release downloads, and web page visits from `AkashKundu114/icc-clustering` to `AkashKundu114/clustering-stability-discordance`.
2. Existing Git remotes will continue functioning seamlessly via automatic server-side 301 redirects.
3. However, all internal links in documentation, `CITATION.cff`, and README have been proactively updated to reference `clustering-stability-discordance`.
4. **Publication Gate:** The repository visibility must **NOT** be changed from Private to Public, and the repository must **NOT** be renamed, until all human co-authors provide formal written sign-off at the final publication gate.

---

## 2. Release Candidate `v1.0.0-rc1` Specification

### Scope of `v1.0.0-rc1`
- **Research Version:** Loop 6.6.1 Audited Baseline.
- **Reproducibility Tier:** Tier 1 (Saved-Evidence Reconstruction) fully verified and functional.
- **Unit & Verification Tests:** 86 tests passing (72 unit tests, 4 reproduction CLI tests, 5 registry tests, 5 manifest integrity tests).
- **Public Artifacts:** 4,323 files cleared in `data/manifests/public_artifacts.csv`. Zero patient microarray caches, raw face images, or partition arrays included.
- **Documentation Suite:** 27 authoritative markdown guides covering methodology, reproduction, data rights, and limitations.

---

## 3. Strict Pre-Release Verification Gates

Before tagging and publishing `v1.0.0`, all of the following checks must be completed:

```text
[PASS] Gate 1: Unit & Integration Tests pass with exit code 0.
[PASS] Gate 2: Clean-clone Tier 1 reconstruction reproduces grand metrics (< 10^-16 diff).
[PASS] Gate 3: Secret & Credential Scan shows zero leaked tokens or keys.
[PASS] Gate 4: Patient Identifier Scan shows zero unmasked clinical subjects.
[PASS] Gate 5: Manifest Verification confirms exactly 4,323 public and 4,326 restricted artifacts.
[PASS] Gate 6: Incomplete 13-dataset benchmark (892/1,430 fits) disclosed in all docs.
[PENDING] Gate 7: Co-Authors Kalyan Kumar Das, Akash Kundu, Prof. Anirban Mukhopadhyay approve public release.
[PENDING] Gate 8: Third-party inquiries dispatched to Yale CVC and UPV/EHU.
```

---

## 4. Archival Deposition Protocol (Zenodo Integration)

If an archival DOI is minted upon journal acceptance:
1. **Never deposit restricted datasets:** Confirm that the Zenodo integration archive excludes `results/stability/partitions/` and `data/cache/`.
2. **Verify DOI Resolution:** Do not record or cite a Zenodo DOI in the manuscript until it physically resolves to the published release deposit.
3. **Draft DOI Placeholders:** Any draft DOI references in `paper/review/main.tex` or documentation must be clearly flagged for co-author verification upon publication.
