from urllib.parse import urlparse

from src.findings import make_finding


def detect_phishing_url(url):
    findings = []
    parsed = urlparse(url)
    hostname = parsed.netloc.lower()
    path = parsed.path.lower()

    suspicious_indicators = []

    if not parsed.scheme or not parsed.netloc:
        suspicious_indicators.append(1)

    if hostname.count('.') > 4:
        suspicious_indicators.append(1)

    if hostname.startswith('10.') or hostname.startswith('127.') or hostname.startswith('192.168.'):
        suspicious_indicators.append(1)

    if '%2f' in url.lower() or '%2e' in url.lower() or '%40' in url.lower():
        suspicious_indicators.append(1)

    if len(path) > 50:
        suspicious_indicators.append(1)

    if suspicious_indicators:
        findings.append(
            make_finding(
                detector='phishing',
                title='Suspicious URL characteristics detected',
                severity='medium',
                confidence='high',
                target=url,
                component='URL',
                description='The URL includes patterns often associated with misleading or malicious destinations.',
                evidence=f"Suspicious indicators found: {len(suspicious_indicators)}. Parsed host: {hostname}",
                recommendation='Verify the destination domain manually and avoid entering credentials until the site is confirmed trustworthy.',
                status='open',
            )
        )

    return findings
