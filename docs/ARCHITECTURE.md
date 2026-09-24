# Architecture

This project uses a simple and beginner-friendly architecture.

## Main flow

1. The scanner receives a target and some test values.
2. It chooses detectors.
3. Each detector checks one category of issue.
4. Each detector creates a standard finding.
5. Findings are stored in SQLite.
6. A report is generated.
7. The dashboard shows results.
8. A remediation step is applied.
9. The scanner runs again to confirm the issue is resolved.

## Modules

### `src/scanner.py`
This is the orchestrator. It decides which detectors run.

### `src/findings.py`
This defines the common structure of a finding.

### `src/risk.py`
This classifies severity and confidence.

### `src/database.py`
This stores and retrieves results.

### `src/reporting.py`
This turns findings into a readable summary.

### `src/detectors/`
This contains detector-specific logic.

### `dashboard/app.py`
This is the UI layer for displaying results.

## Diagram

```text
Target
  |
  v
Scanner
  |
  +--> Phishing Detector
  +--> SQLi Detector
  +--> Configuration Detector
  |
  v
Findings
  |
  v
Risk Engine
  |
  v
SQLite Database
  |
  v
Report + Dashboard
```

## Why this design is useful

- each detector is separate
- future detectors can be added easily
- the same finding model is reused
- the dashboard does not need to know how the issue was detected
- the scanner is easier to test and explain
