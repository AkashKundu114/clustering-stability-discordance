"""Unit tests validating the dataset registry integrity and rights classifications."""

from pathlib import Path
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = ROOT / "data" / "dataset_registry.csv"


def test_registry_exists_and_loads():
    assert REGISTRY_PATH.is_file(), f"Registry file missing at {REGISTRY_PATH}"
    df = pd.read_csv(REGISTRY_PATH)
    assert len(df) == 13, f"Expected 13 datasets in registry, found {len(df)}"


def test_required_columns_present():
    df = pd.read_csv(REGISTRY_PATH)
    expected_cols = [
        "dataset_id",
        "dataset_name",
        "domain",
        "n_samples",
        "n_features",
        "n_classes",
        "d_over_n",
        "license",
        "redistribution_status",
    ]
    for col in expected_cols:
        assert col in df.columns, f"Missing required column: {col}"


def test_high_d_cohort_boundary():
    df = pd.read_csv(REGISTRY_PATH)
    high_d = df[df["d_over_n"] > 20.0]
    expected_high_d = {"cns", "colon", "leukemia", "ovarian", "prostate", "srbct"}
    assert set(high_d["dataset_id"]) == expected_high_d, f"Mismatch in high-D cohorts: {set(high_d['dataset_id'])}"


def test_yale_b_redistribution_restricted():
    df = pd.read_csv(REGISTRY_PATH)
    yale_row = df[df["dataset_id"] == "yale_b"].iloc[0]
    assert yale_row["redistribution_status"] == "RESTRICTED_REDISTRIBUTION"
    assert "prohibited" in yale_row["license"].lower()
    assert "do not bundle" in yale_row["rights_notes"].lower()


def test_open_access_benchmarks():
    df = pd.read_csv(REGISTRY_PATH)
    open_acc = df[df["redistribution_status"] == "OPEN_ACCESS"]
    expected_open = {"sonar", "madelon", "isolet", "zheng68k", "newsgroups20"}
    assert set(open_acc["dataset_id"]) == expected_open
