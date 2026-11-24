# CSD Submission Reproducibility & Scientific Evidence Audit

> **Note:** Under review.

**Canonical Repository:** [`AkashKundu114/clustering-stability-discordance`](https://github.com/AkashKundu114/clustering-stability-discordance)
**Authoritative Reference:** Exact 48-page submitted manuscript PDF (*Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise* by Kalyan Kumar Das, Akash Kundu, and Anirban Mukhopadhyay; SHA-256: `b32259bfd704a7a7e6dd45e5717a731f0d8100d819cfd792911645e7da571a3c`).

---

## 1. Purpose & Scope

This directory contains the compact, permanent audit record of the submission reproducibility and scientific evidence verification for the CSD project. It is designed to enable independent reviewers and researchers to inspect, understand, and verify the evidence supporting every claim made in the submitted manuscript.

To avoid redundant duplication, this directory references existing project assets, tests, results, and documentation rather than duplicating them.

---

## 2. Directory Navigation

The audit record is structured into five core files and one log directory:

```text
audit/
└── submission_reproducibility/
    ├── README.md                  # This navigation and interpretation guide
    ├── audit_report.md            # Comprehensive audit findings, discrepancies, resolutions, and assessment
    ├── claim_evidence_matrix.csv  # Manuscript claim -> location -> experiment -> code -> artifact -> status
    ├── reproduction_status.csv    # Experiment -> reproduction tier -> status -> environment -> limitations
    ├── documentation_audit.md     # Consolidated documentation, packaging, ignore-rules, and link audit
    └── logs/                      # Essential machine-generated verification logs
        ├── pytest_unit_verification.log # 86 unit and CLI tests passed (52.38s)
        └── smoke_execution.log          # 15 synthetic benchmark configurations executed (~8s)
```

---

## 3. How to Interpret the Audit Records

### 3.1 Verification Status Definitions
- `VERIFIED_BITWISE`: The recomputed value matches the manuscript value exactly to all reported decimal places (e.g., Grand Mean Stability $\bar{S}=0.510$, Mean ARI $\bar{A}=0.053$, Discordance Gap $\bar{\Delta}=+0.457$, Permuted Null $S_{\text{null}}=0.007$).
- `VERIFIED_CONVERGENT`: The empirical phenomenon or statistical test direction is confirmed by fresh execution, with minor stochastic variation within expected confidence bounds (e.g., synthetic noise collapse, factorial interaction $p=0.16$).
- `CORROBORATED_BOUNDED`: The archived output matrix confirms the reported summary statistic, but complete fresh rerun is bounded by documented hardware memory constraints (e.g., 13-dataset benchmark Friedman test $\chi_F^2=11.556, p=0.40$).
- `DOCUMENTED_LIMITATION`: A structural, statistical, or operational boundary that restricts the generalizability or re-execution scope (e.g., 16 GB RAM ceiling, $n=6$ sample size, DEC autoencoder optimization shifts).

### 3.2 Four-Tier Reproduction Framework
Reviewers can verify claims across four tiers detailed in [`docs/reproducibility_architecture.md`](../../docs/reproducibility_architecture.md):
- **Tier 0 (Environment & Tests):** Run `pytest tests/unit tests/test_reproduce_cli.py -o addopts=""` (~50 seconds).
- **Tier 1 (Instant Aggregate Re-computation):** Run `python reproduction/scripts/recompute_benchmark_scores.py` (~5 seconds).
- **Tier 2 (Saved-Partition Stability Recalculation):** Run `python reproduction/scripts/recompute_saved_stability.py` (~2 minutes).
- **Tier 3 (Fresh Rerun Bounds):** Run `python scripts/reproduce.py --scope smoke` (~8 seconds).

---

## 4. Key Cross-References

- **Core Scientific Protocol:** [`EXPERIMENTAL_PROTOCOL.md`](../../EXPERIMENTAL_PROTOCOL.md)
- **Submitted Manuscript Metadata:** [`docs/submitted_manuscript.md`](../../docs/submitted_manuscript.md)
- **Experiment Catalog (EXP-01 to EXP-07):** [`docs/experiment_catalog.md`](../../docs/experiment_catalog.md)
- **Empirical Metric Dictionary:** [`docs/result_dictionary.md`](../../docs/result_dictionary.md)
- **Data Governance & License Rights:** [`docs/data_rights.md`](../../docs/data_rights.md)
- **Experimental Artifact Provenance:** [`docs/experimental_provenance.md`](../../docs/experimental_provenance.md)
- **Scientific & Operational Limitations:** [`docs/limitations.md`](../../docs/limitations.md)
