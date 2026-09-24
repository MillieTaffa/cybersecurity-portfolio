# SentinelScanner

A beginner-friendly cybersecurity assessment project built to demonstrate how a modular security scanner works in a safe, local environment.

## Overview

SentinelScanner helps you:

- analyse suspicious URLs
- detect SQL injection patterns in a controlled lab
- check basic security configuration problems
- store findings in SQLite
- generate a readable report
- display results in a simple dashboard
- verify whether a fix actually resolved the issue

This project is intentionally small and practical. It is designed to teach the core ideas behind security detection without becoming an oversized or unrealistic security platform.

## Why this project matters

A real scanner should do more than say, “This is bad.” It should explain:

- what was found
- where it was found
- why it is risky
- how serious it is
- how confident the scanner is
- what evidence supports the result
- how to fix it
- whether the issue is still present after remediation

This is the heart of SentinelScanner.

## Project goals

- detect suspicious URL patterns
- detect unsafe SQL handling in a controlled application
- check a few insecure configuration settings
- classify severity and confidence
- save findings in a database
- show results in a dashboard
- demonstrate remediation and re-testing

## Project structure

```text
cybersecurity-portfolio/
├── README.md
├── USER_MANUAL.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── src/
│   ├── __init__.py
│   ├── scanner.py
│   ├── findings.py
│   ├── risk.py
│   ├── reporting.py
│   ├── database.py
│   └── detectors/
│       ├── __init__.py
│       ├── phishing.py
│       ├── sqli.py
│       └── configuration.py
├── dashboard/
│   └── app.py
├── database/
│   ├── schema.sql
├── tests/
│   ├── test_phishing.py
│   ├── test_sqli.py
│   ├── test_configuration.py
│   ├── test_risk.py
│   └── test_findings.py
├── lab/
│   ├── README.md
│   └── vulnerable_app/
│       └── app.py
├── docs/
│   ├── ARCHITECTURE.md
│   ├── SECURITY.md
│   └── SCOPE.md
└── .pytest_cache/
```

## Quick start

### 1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the tests

```bash
pytest
```

### 4. Run a sample scan from Python

```bash
python - <<'PY'
from src.scanner import run_scan

findings = run_scan(
    target='example.com',
    url='http://10.0.0.5/login?next=https://example.com%2Flogin',
    config={'debug': True, 'https_only': False, 'authentication_required': False},
    payload="name=' OR '1'='1"
)

for item in findings:
    print(item.title, item.severity, item.confidence)
PY
```

### 5. Start the dashboard

```bash
streamlit run dashboard/app.py
```

Then open the local URL shown in the terminal.

## Safety and allowed use

This project is intended only for:

- your own machine
- a local lab
- intentionally vulnerable sample code
- explicitly authorised testing

It should not be used to scan random public websites or attack third-party systems without permission.

## Beginner-friendly workflow

Think of SentinelScanner like this:

1. A target is provided.
2. The scanner runs one or more detectors.
3. Each detector checks a specific type of issue.
4. Each detector creates a standard finding object.
5. Findings are stored in SQLite.
6. A report and dashboard make the results readable.
7. A fix is applied.
8. The scanner runs again to confirm the issue has been resolved.

## Main ideas in the code

### Finding model

Every detector returns a finding with the same structure:

- detector name
- title
- severity
- confidence
- target
- component
- description
- evidence
- recommendation
- status

This keeps the code modular and consistent.

### Risk engine

The risk engine decides how serious the issue is. Severity tells you impact, while confidence tells you how certain the detector is that the issue is real.

### Database layer

Findings are stored in SQLite so the scanner can keep a record of detections and re-test behaviour.

### Dashboard

The dashboard is only a visual layer. It does not decide whether something is a security issue; the detectors do.

## Example scenario

A typical workflow looks like this:

- a suspicious URL is analysed
- a phishing-style finding is created
- a SQL injection pattern is detected in a local app
- a weak configuration is flagged
- all findings are saved to SQLite
- the report is generated
- the dashboard shows the results

## Future ideas

This MVP stays focused on a simple and useful set of checks. Possible future upgrades include:

- XSS detection
- CSRF detection
- API security checks
- secret scanning
- container vulnerability checks
- cloud configuration validation
- more advanced dashboards and alerts

## Documentation

- [USER_MANUAL.md](USER_MANUAL.md) — explains what SentinelScanner is, what it does, how it works, and why it exists
- [lab/README.md](lab/README.md) — explains how to use the local lab safely

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
