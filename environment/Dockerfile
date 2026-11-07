# Reproducible container environment for ICC clustering research verification
# Target: Springer Nature DMKD Reviewer Verification Environment

FROM python:3.11-slim

LABEL maintainer="Akash Kundu <akashkundu1152@gmail.com>"
LABEL description="Reproducible container for Tier 1 saved-evidence verification of stability-accuracy discordance."

WORKDIR /workspace

# Install system utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install minimal numerical and verification dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
    numpy>=1.23.0 \
    scipy>=1.10.0 \
    pandas>=2.0.0 \
    scikit-learn>=1.3.0 \
    pyyaml>=6.0 \
    pytest>=7.0.0 \
    tabulate>=0.9.0

# Copy repository source
COPY . /workspace

# Set default execution command: run the reproduction CLI test suite
CMD ["python", "-m", "pytest", "tests/test_reproduce_cli.py", "-v"]
