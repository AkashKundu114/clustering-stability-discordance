# Contributing to CSD

Thank you for your interest in contributing to **CSD (Clustering Stability-Accuracy Discordance)**. This repository hosts the research code, reproduction tools, and documentation for evaluating clustering stability and external alignment under high-dimensional noise.

We welcome contributions ranging from bug fixes and documentation clarifications to new clustering baselines, additional benchmark datasets, and performance improvements.

---

## Code of Conduct

All contributors and participants are expected to adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). Please report any violations or concerns via the [Issue Tracker](https://github.com/AkashKundu114/clustering-stability-discordance/issues).

---

## Getting Started

### Prerequisites
* Python 3.10 through 3.14 (tested across Linux and Windows)
* Git

### Step-by-Step Environment Setup
1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/AkashKundu114/clustering-stability-discordance.git
   cd clustering-stability-discordance
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # On Linux/macOS
   python3 -m venv venv
   source venv/bin/activate

   # On Windows (PowerShell)
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies in editable mode:**
   ```bash
   pip install -e .
   pip install -r requirements-dev.txt
   ```

4. **Verify installation:**
   ```bash
   python -c "import csd; print(csd.__version__)"
   ```

---

## Development Workflow

1. **Create a topic branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Implement your changes:**
   * Write clean, readable, documented Python following PEP 8 conventions.
   * Add docstrings for public classes and functions.
   * Ensure backwards compatibility with supported Python versions (3.10-3.14).

3. **Run automated tests:**
   Before opening a pull request, run the test suite to ensure all unit tests and CLI verification checks pass:
   ```bash
   pytest tests/unit tests/test_reproduce_cli.py -o addopts=""
   ```

4. **Check code formatting and linting:**
   ```bash
   ruff check .
   ruff format --check .
   ```

5. **Commit your changes:**
   Write clear, concise commit messages following standard conventions:
   ```bash
   git commit -m "feat(algorithms): add new sparse clustering baseline"
   ```

---

## Submitting a Pull Request

1. Push your topic branch to your fork on GitHub.
2. Open a Pull Request against the `main` branch of `AkashKundu114/clustering-stability-discordance`.
3. Provide a clear description of:
   * The purpose of the changes.
   * Any issue numbers resolved (e.g., `Fixes #12`).
   * Test coverage added or verified.
4. Ensure continuous integration checks pass. Maintainers will review your pull request promptly.

---

## Reporting Issues

If you find a bug, inconsistency, or documentation typo:
* Open an issue on GitHub with a descriptive title and steps to reproduce.
* Include your operating system, Python version, and dependency versions.
* For potential security vulnerabilities, please refer to our [Security Policy](SECURITY.md).
