# Tests Documentation

This directory contains all test files for the RSS Feed Reader project.

# Test Files

- test_parser.py: Contains unit tests for the RSS parser functionality

  - Tests RSS feed parsing

  - Tests Atom feed parsing

  - Uses pytest framework

  - Includes mock data for testing

# Running Tests

### Prerequisites

- Python 3.x

- pytest

- Any other required dependencies (see requirements.txt)

### Installation

```bash
pip install -r requirements-test.txt
```

### Running All Tests

```bash pytest

```

### Running Specific Tests

# Run tests in a specific file

pytest tests/test_parser.py

# Run tests with specific markers

pytest -m "parser"

# Run tests with coverage report

pytest --cov=src tests/

# Test Configuration

- Description of any configuration files

- Environment variables needed for testing

- Mock data setup
