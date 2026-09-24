from src.findings import make_finding
from src.detectors.phishing import detect_phishing_url
from src.detectors.configuration import detect_configuration_issues
from src.detectors.sqli import detect_sql_injection_exposure
from src.database import initialise_db, save_scan, save_finding


def run_scan(target='local-lab', url=None, config=None, payload=None):
    initialise_db()
    findings = []

    if url:
        findings.extend(detect_phishing_url(url))

    if payload is not None:
        findings.extend(detect_sql_injection_exposure(payload, target=target))

    if config is not None:
        findings.extend(detect_configuration_issues(config, target=target))

    scan_id = save_scan(target, 'open')
    for item in findings:
        save_finding(scan_id, item)

    return findings


def scan_and_report(target='local-lab', url=None, config=None, payload=None):
    findings = run_scan(target=target, url=url, config=config, payload=payload)
    return findings
