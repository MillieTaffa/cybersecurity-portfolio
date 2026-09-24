# SentinelScanner

SentinelScanner is a beginner-friendly cybersecurity assessment project. It focuses on a small and safe security workflow:

- analyse a suspicious URL
- look for SQL injection patterns in a controlled lab
- check a few security settings
- store the findings in SQLite
- show them in a simple dashboard
- explain what was found and how to fix it

This project is intentionally small, clear, and safe. It is designed to help you learn how a modular security scanner works without jumping into huge enterprise systems.

## Why this project exists

A good security scanner should do more than say "something is wrong". It should explain:

- what was detected
- where it was detected
- why it matters
- how serious it is
- what evidence supports the finding
- how to fix it
- whether the problem still exists after remediation

That is the heart of SentinelScanner.

## Project goals

- detect suspicious URLs
- detect unsafe SQL pattern usage in a controlled environment
- check configuration weaknesses
- assign severity and confidence levels
- store findings in a database
- generate a readable report
- show results in a simple dashboard
- demonstrate remediation and re-test

## Project structure

```text
cybersecurity-portfolio/
├── README.md
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
│   └── sentinelscanner.db
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

### 3. Run tests

```bash
pytest
```

### 4. Run the scanner from Python

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

## Safety and scope

This project is only meant for:

- your own machine
- a local lab
- deliberately vulnerable sample code
- explicitly authorised testing

This project does not scan random public websites or attack external systems.

## Beginner explanation

Think of SentinelScanner like this:

1. A target is given to the scanner.
2. The scanner chooses detectors.
3. Each detector looks for one class of issue.
4. Every detector creates a standard finding object.
5. The findings are stored in SQLite.
6. A report and dashboard make the results readable.
7. A fix is applied.
8. The scanner runs again to check whether the issue is resolved.

## Main ideas in the code

### Finding model

Each detector returns a finding with the same structure:

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

This makes the project modular.

### Risk engine

The risk engine decides how serious something is. Severity is about impact, while confidence is about how sure the detector is.

### Database

Findings are saved to SQLite so the project can show history and re-test behaviour.

### Dashboard

The dashboard is only a front-end layer. It does not decide whether something is a security issue; the detectors do.

## Example scenario

- A suspicious URL is analysed
- a phishing-style finding is created
- a SQL injection pattern is detected in a local app
- a weak security configuration is flagged
- all findings are stored
- the report is generated
- the dashboard displays the results

## Future ideas

This MVP intentionally stays focused. Possible future work includes:

- XSS checks
- CSRF checks
- API security rules
- secret scanning
- container vulnerability checks
- cloud configuration review
- more advanced dashboards and alerts

## License

This project is intended for educational and portfolio use.
