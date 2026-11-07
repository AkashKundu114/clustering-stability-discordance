"""
CSD: Clustering-Stability-Discordance Research Software Suite.

Re-exports core functionality from Invariant Core Consensus (icc)
and Conformal Inductive Consensus Clustering (cicc).
"""

from __future__ import annotations

import cicc
import icc
from icc import (
    GAC,
    InvariantCoreConsensus,
    InvariantCoreConsensusV2,
    evaluate_all,
    list_algorithms,
    list_datasets,
    load_dataset,
    run_clusterer,
)

__version__ = "1.0.0-rc2"

__all__ = [
    "GAC",
    "InvariantCoreConsensus",
    "InvariantCoreConsensusV2",
    "__version__",
    "cicc",
    "evaluate_all",
    "icc",
    "list_algorithms",
    "list_datasets",
    "load_dataset",
    "run_clusterer",
]
