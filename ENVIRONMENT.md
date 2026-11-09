# Environment Setup and Installation Guide

**Document:** `docs/environment-setup.md` 
**Date:** 2026-11-07 
**Project:** Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise  
**Running Header:** Feature-Gated Bipartite Consensus Under Noise  
**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)  
**Companion Repository:** [https://github.com/AkashKundu114/icc-clustering](https://github.com/AkashKundu114/icc-clustering)  
**Benchmark Scope:** 13 benchmark datasets and 12 comparative algorithms 

---

## 1. Minimal Installation (Reviewer Verification Mode)

To independently verify all reported metrics and run the unit test suite, only minimal numerical dependencies are needed:

```bash
# Clone the repository
git clone https://github.com/AkashKundu114/clustering-stability-discordance.git
cd clustering-stability-discordance

# Create a clean virtual environment
python -m venv .venv

# Activate environment:
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# Install locked dependencies
pip install -r environment/requirements-lock.txt

# Install package in editable mode
pip install -e .
```

---

## 2. Conda Installation

If using Anaconda or Miniconda:

```bash
conda env create -f environment/environment.yml
conda activate icc-clustering
pip install -e .
```

---

## 3. Docker Container Setup

A Dockerfile is provided under `environment/Dockerfile`:

```bash
# Build the container image
docker build -t icc-discordance -f environment/Dockerfile .

# Run the automated verification tests inside the container
docker run --rm icc-discordance
```

---

## 4. Verification Check

Run the reproduction test suite:

```bash
python -m pytest tests/test_reproduce_cli.py tests/unit/test_dataset_registry.py tests/unit/test_manifest_integrity.py -v
```

Expected result: **All tests pass with exit code 0.**
