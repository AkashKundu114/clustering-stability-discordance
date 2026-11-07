"""Unit tests for public/private artifact manifest integrity and security boundaries."""

from pathlib import Path
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[2]
PUBLIC_MANIFEST = ROOT / "data" / "manifests" / "public_artifacts.csv"
RESTRICTED_MANIFEST = ROOT / "data" / "manifests" / "restricted_artifacts.csv"
SOURCE_FETCH_MANIFEST = ROOT / "data" / "manifests" / "source_fetch_only.csv"


def test_manifest_files_exist():
    assert PUBLIC_MANIFEST.is_file(), "public_artifacts.csv missing"
    assert RESTRICTED_MANIFEST.is_file(), "restricted_artifacts.csv missing"
    assert SOURCE_FETCH_MANIFEST.is_file(), "source_fetch_only.csv missing"


def test_artifact_counts_match_specification():
    pub_df = pd.read_csv(PUBLIC_MANIFEST)
    res_df = pd.read_csv(RESTRICTED_MANIFEST)
    assert len(pub_df) == 4323, f"Expected 4323 public artifacts, got {len(pub_df)}"
    assert len(res_df) == 4326, f"Expected 4326 restricted artifacts, got {len(res_df)}"
    assert len(pub_df) + len(res_df) == 8649, "Total artifact count must equal 8649"


def test_no_restricted_data_in_public_manifest():
    pub_df = pd.read_csv(PUBLIC_MANIFEST)
    # Partitions (.npy) and patient cache (.npz) must NEVER be in public manifest
    for path in pub_df["relative_path"]:
        assert not path.endswith(".npy"), f"Forbidden partition array in public manifest: {path}"
        assert not path.endswith(".npz"), f"Forbidden patient cache in public manifest: {path}"
        assert not "cache/" in path, f"Cache path leaked to public manifest: {path}"


def test_no_absolute_or_escaping_paths():
    for manifest_path in [PUBLIC_MANIFEST, RESTRICTED_MANIFEST]:
        df = pd.read_csv(manifest_path)
        for path in df["relative_path"]:
            assert not path.startswith(("/", "\\", "C:", "D:")), f"Absolute path detected: {path}"
            assert ".." not in path, f"Directory traversal detected: {path}"


def test_public_manifest_only_contains_telemetry_and_summaries():
    pub_df = pd.read_csv(PUBLIC_MANIFEST)
    for path in pub_df["relative_path"]:
        assert path.endswith(".parquet") or path.endswith(".csv"), f"Unexpected file type in public manifest: {path}"
