from src.findings import make_finding


def detect_sql_injection_exposure(payload, target='local-lab'):
    suspicious_patterns = [
        "' or '1'='1",
        "or 1=1",
        "union select",
        "--",
        "; drop",
        "sleep(",
        "select * from",
    ]

    lowered = (payload or '').lower()
    matches = [pattern for pattern in suspicious_patterns if pattern in lowered]

    if not matches:
        return []

    return [
        make_finding(
            detector='sqli',
            title='Unsafe SQL query handling detected',
            severity='high',
            confidence='high',
            target=target,
            component='database-query',
            description='The application accepts a payload with SQL injection indicators and may be vulnerable to unsafe query construction.',
            evidence=f"Detected suspicious SQL patterns: {', '.join(matches)}",
            recommendation='Use parameterised queries or prepared statements to separate SQL logic from user input.',
            status='open',
        )
    ]
