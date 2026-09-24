# Local Security Lab User Manual

This document explains how to use the local lab in SentinelScanner, what it does, why it is included, and how to run it safely.

## What this file is for

This lab is a safe, intentionally vulnerable example application created for learning and demonstration. It exists so you can see how SentinelScanner:

- detects a security weakness
- explains the finding clearly
- recommends a fix
- re-runs the scan after the fix
- confirms the issue is resolved

It is not meant for attacking public systems or using on real production environments.

## What the lab does

The lab contains a tiny web application that accepts a username and builds a query in an unsafe way. This is a simplified example of poor SQL handling.

The unsafe pattern looks like this:

```python
query = "SELECT * FROM users WHERE username = '" + username + "'"
```

This is dangerous because user input is inserted directly into the query string. If an attacker sends crafted input, the logic can be altered.

## Why this lab exists

The purpose of the lab is to teach the full security cycle:

1. identify a weakness
2. explain it
3. fix it
4. scan again
5. verify the fix worked

This mirrors how a real security assessment should work in a controlled environment.

## What is in scope

This lab is only for:

- local demonstration
- authorised testing
- educational use
- controlled security learning

## What is out of scope

This lab does not include or support:

- scanning public websites
- attacking third-party services
- exploiting live infrastructure
- credential attacks
- malicious or harmful behaviour

## How to run it

Open a terminal in the project root and run:

```bash
python lab/vulnerable_app/app.py
```

Then open this address in your browser:

```text
http://localhost:8001
```

You should see a simple page with a username field.

## How to use it

1. Start the app.
2. Enter a username in the form.
3. Submit the form.
4. Observe the generated unsafe query string in the page output.
5. Run SentinelScanner to detect the issue.
6. Review the finding details.
7. Apply the remediation fix.
8. Run the scanner again.
9. Verify that the finding no longer appears.

## How the security issue is detected

SentinelScanner checks for patterns that suggest unsafe SQL behaviour. For example, payloads such as:

```text
' OR '1'='1
```

or other SQL injection indicators are treated as suspicious input.

## How to fix it

A safer implementation uses parameterised queries or prepared statements.

Example of a secure pattern:

```python
query = "SELECT * FROM users WHERE username = ?"
```

This separates the SQL logic from user input and prevents direct string injection into the query itself.

## Why the fix works

When user input is passed separately from the SQL command, the database treats the value as data instead of executable SQL logic. This greatly reduces the risk of injection.

## Recommended workflow

The safest way to use the lab is:

```bash
python lab/vulnerable_app/app.py
```

Then, in another terminal, run:

```bash
. .venv/bin/activate
pytest
```

Or run the scanner manually in Python to test the detection logic.

## Beginner summary

This lab is a teaching tool. It shows a bad pattern and then demonstrates how a proper security scanner can detect it, explain it, and validate the fix.

The main lesson is:

> Security tools are not only about finding problems — they are also about explaining the problem and confirming that the fix works.

## Final note

Use this lab only in a local, controlled, and authorised environment. It is meant for learning and demonstration, not for testing real systems.
