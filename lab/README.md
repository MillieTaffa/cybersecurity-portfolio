# Local Security Lab

This lab is intentionally small and safe.

## Purpose

The purpose of this lab is to demonstrate that SentinelScanner can:

- detect a security issue
- explain the issue with details
- recommend a fix
- re-run the scan after remediation
- verify that the issue is resolved

## Controlled app

The vulnerable application is a tiny Python script that accepts a username value and runs an unsafe SQL-like query pattern.

It exists only for teaching and local demonstration.

## Running the lab

```bash
python lab/vulnerable_app/app.py
```

Then visit:

```text
http://localhost:8001
```

## What is in scope

- local demonstration
- authorised testing only
- controlled SQL injection learning example

## What is out of scope

- scanning public websites
- attacking third-party systems
- exploiting live services
- credential attacks

## Remediation example

The unsafe pattern is:

```python
query = "SELECT * FROM users WHERE username = '" + username + "'"
```

A safer approach is to use a parameterised query:

```python
query = "SELECT * FROM users WHERE username = ?"
```

The scanner can run again after this change to confirm the issue is resolved.
