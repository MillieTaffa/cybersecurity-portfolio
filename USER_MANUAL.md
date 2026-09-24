# SentinelScanner User Manual

This manual explains what SentinelScanner is, what it does, how it works, why it matters, and how to run it safely.

## What is SentinelScanner?

SentinelScanner is a beginner-friendly cybersecurity project designed to demonstrate how a security scanner works in a controlled environment. It focuses on a small but important set of tasks:

- analysing suspicious URLs
- looking for SQL injection patterns
- checking basic security settings
- storing findings in SQLite
- generating a readable report
- showing results in a dashboard
- confirming whether remediation worked

It is a learning project, not a full enterprise-grade security platform.

## What SentinelScanner does

SentinelScanner acts like a lightweight security assessment tool. It looks for selected weaknesses and turns them into structured findings.

Each finding explains:

- what was detected
- where it was detected
- why it matters
- how serious it is
- how confident the tool is
- what evidence supports the finding
- how to fix it
- whether the issue is still open or resolved

## Why it exists

Many scanners simply say something is wrong, but they do not explain why. SentinelScanner is built around a better idea:

Detect → Explain → Remediate → Verify

This means:

1. detect a problem
2. explain the risk clearly
3. suggest a fix
4. run the check again
5. confirm the issue is resolved

This workflow is important in real security work.

## How it works

The project is modular, which means each part has a clear responsibility.

### 1. Scanner core
The scanner orchestrates the process. It decides which detectors to run and collects all findings.

### 2. Detectors
Each detector checks one kind of issue.

Examples in this project:

- phishing URL detection
- SQL injection exposure detection
- configuration weakness checks

Each detector creates a finding object in the same format.

### 3. Finding model
Every finding is created in a standard structure so the rest of the system can use it consistently.

The finding includes fields such as:

- detector
- title
- severity
- confidence
- target
- component
- description
- evidence
- recommendation
- status

### 4. Risk engine
The risk engine classifies the issue by severity and confidence.

- severity describes impact
- confidence describes how certain the scanner is

These are not the same thing.

### 5. Database
The results are saved in SQLite so the project can keep a record of scans and findings.

### 6. Reporting
The report turns raw findings into readable output that a human can understand.

### 7. Dashboard
The dashboard makes the data easier to view, especially for demonstrations and portfolio use.

## Why this project is useful

This project shows important software engineering and security ideas:

- modular design
- clear detection logic
- explainable findings
- risk classification
- storage and retrieval of results
- remediation verification
- safe local testing

It is a strong example of a practical, beginner-friendly security tool.

## How to run the project

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

### 4. Run a sample detection

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

Then open the local URL shown in the browser.

## How to use the lab safely

The project includes a local lab under the [lab](lab) folder. It is intentionally vulnerable and should be used only on your own machine or in a controlled learning environment.

To run it:

```bash
python lab/vulnerable_app/app.py
```

Then open:

```text
http://localhost:8001
```

## Safety rules

Use SentinelScanner only for:

- your own machine
- local lab testing
- explicitly authorised systems
- educational projects

Do not use it to:

- scan public websites without permission
- attack third-party systems
- test internet services you do not own
- perform harmful or criminal activity

## Beginner summary

SentinelScanner is a simple demonstration of a security scanner that:

- checks a few selected issues
- creates structured results
- records them in a database
- explains the problem in plain language
- recommends a fix
- validates whether the problem is resolved

That makes it a practical project for learning cybersecurity, Python, automation, data handling, and secure development practices.

## Final note

This project is designed to teach the principles of security detection and verification in a safe, understandable way. It is intentionally small so you can follow the workflow clearly and learn the fundamentals without being overwhelmed.
