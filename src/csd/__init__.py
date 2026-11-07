"""
CSD: Clustering-Stability-Discordance Research Software Suite.

Re-exports core functionality from Invariant Core Consensus (icc)
and Conformal Inductive Consensus Clustering (cicc).
"""

import sys
from pathlib import Path

# Ensure local package resolution
_pkg_root = Path(__file__).resolve().parent.parent
if str(_pkg_root) not in sys.path:
    sys.path.insert(0, str(_pkg_root))

import icc
import cicc

from icc import (
    GAC,
    InvariantCoreConsensus,
    InvariantCoreConsensusV2,
    run_clusterer,
    list_algorithms,
    list_datasets,
    load_dataset,
    evaluate_all,
)

__version__ = "1.0.0-rc2"

__all__ = [
    "__version__",
    "icc",
    "cicc",
    "GAC",
    "InvariantCoreConsensus",
    "InvariantCoreConsensusV2",
    "run_clusterer",
    "list_algorithms",
    "list_datasets",
    "load_dataset",
    "evaluate_all",
]
