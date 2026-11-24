# Computational Environment & Installation Guide

**Canonical Repository:** [https://github.com/AkashKundu114/clustering-stability-discordance](https://github.com/AkashKundu114/clustering-stability-discordance)
**Submitted Manuscript Reference:** *Stability, Accuracy, and Feature-Gated Bipartite Consensus Under Noise*
**Authors:** Kalyan Kumar Das, Akash Kundu, Anirban Mukhopadhyay
**Journal:** Springer Nature - *Data Mining and Knowledge Discovery* (DMKD)
**Status:** Under review
**Audited Baseline Commit:** `44838fa`

This guide documents the software stack, operating system specifications, hardware boundaries, and installation instructions for running the CSD reproducibility suite.

---

## 1. Minimal Installation (Reviewer Verification Mode)

To independently verify all reported metrics and run the unit test suite, standard scientific Python packages are required:

```bash
# Clone the canonical repository
git clone https://github.com/AkashKundu114/clustering-stability-discordance.git
cd clustering-stability-discordance

# Create a clean virtual environment (Python 3.10+)
python -m venv .venv

# Activate environment:
# On Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# On Linux/macOS:
source .venv/bin/activate

# Install core and test dependencies in editable mode
pip install -e ".[dev]"
```

---

## 2. Conda Installation

For Anaconda or Miniconda environments:

```bash
conda env create -f environment/environment.yml
conda activate csd
pip install -e ".[dev]"
```

---

## 3. Docker Container Setup

A container specification is provided under `environment/Dockerfile`:

```bash
# Build the container image
docker build -t csd-verification -f environment/Dockerfile .

# Run the automated verification tests inside the container
docker run --rm csd-verification
```

---

## 4. Hardware Environment & Boundary Notes

- **Audited Host Machine:** Intel Core i7 / AMD Ryzen workstation with 16 GB RAM and NVIDIA CUDA GPU.
- **Python Runtimes Audited:** Python 3.10 through Python 3.14.6 64-bit AMD64.
- **Hardware Boundary for Dense Consensus:**
  - $N \le 2{,}600$ (Microarrays, Sonar, Madelon): Executes comfortably in $< 2\text{ GB}$ of RAM.
  - $N > 2{,}600$ (ISOLET $N=7{,}797$, Indian Pines $N=10{,}249$, 20 Newsgroups $N=18{,}846$, PBMC68k $N=68{,}579$): Standard dense consensus ($N \times N$) requires tens of gigabytes of RAM. Reruns on standard 16 GB workstations trigger memory exhaustion and OS paging. Exactly 892 of 1,430 unique fits completed in the modern clean environment; 538 fits were halted to protect host stability.

---

## 5. Verification Check

Run the test suite:

```bash
python -m pytest tests/unit tests/test_reproduce_cli.py
```

*Expected Result:* **82 unit tests and 4 CLI tests pass with exit code 0.**
