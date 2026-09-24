# How to Run SentinelScanner

This guide explains how to run the project step by step from the beginning.

## 1. Open the project folder

In your terminal, go to the project folder:

```bash
cd /home/khethiops/Desktop/sentinelscanner/cybersecurity-portfolio
```

## 2. Create a virtual environment

A virtual environment keeps the project dependencies separate from the rest of your computer.

```bash
python3 -m venv .venv
```

## 3. Activate the virtual environment

On Linux and Mac:

```bash
source .venv/bin/activate
```

If you are using PowerShell on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 4. Install the required packages

```bash
pip install -r requirements.txt
```

This installs:

- Streamlit
- Plotly
- Pytest
- Flask

## 5. Run the tests

This checks whether the project works correctly.

```bash
pytest -q
```

If everything is working, you should see all tests pass.

## 6. Start the vulnerable lab

The lab is a small local application used for demonstration and testing.

```bash
python lab/vulnerable_app/app.py
```

Then open this in your browser:

```text
http://localhost:8001
```

This starts the intentionally vulnerable demo app.

## 7. Run the scanner manually

In another terminal window, while the lab is running, run:

```bash
cd /home/khethiops/Desktop/sentinelscanner/cybersecurity-portfolio
source .venv/bin/activate
python - <<'PY'
from src.scanner import run_scan

findings = run_scan(
    target='local-lab',
    url='http://10.0.0.5/login?next=https://example.com%2Flogin',
    config={'debug': True, 'https_only': False, 'authentication_required': False},
    payload="name=' OR '1'='1"
)

for item in findings:
    print(item.title, item.severity, item.confidence)
PY
```

This runs the scanner and prints the findings.

## 8. Start the dashboard

In a separate terminal, run:

```bash
cd /home/khethiops/Desktop/sentinelscanner/cybersecurity-portfolio
source .venv/bin/activate
streamlit run dashboard/app.py
```

Then open the URL shown in the terminal, usually:

```text
http://localhost:8501
```

This opens the SentinelScanner dashboard.

## 9. What you are seeing

You should be able to see:

- summary information
- scan results
- findings table
- some basic severity information
- the overall dashboard view

## 10. How to stop the app

To stop a running Python app in the terminal, press:

```bash
Ctrl + C
```

## 11. Common troubleshooting

### Problem: pytest cannot find the project modules

Make sure you are in the project root and using the virtual environment:

```bash
cd /home/khethiops/Desktop/sentinelscanner/cybersecurity-portfolio
source .venv/bin/activate
pytest -q
```

### Problem: Streamlit does not start

Make sure the dependencies were installed:

```bash
pip install -r requirements.txt
```

### Problem: the lab does not open in the browser

Check that the app is still running in the terminal and that the port is correct:

```text
http://localhost:8001
```

## 12. Simple summary

To run the full project, do this:

```bash
cd /home/khethiops/Desktop/sentinelscanner/cybersecurity-portfolio
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python lab/vulnerable_app/app.py
streamlit run dashboard/app.py
```

This is the standard way to run SentinelScanner step by step.
