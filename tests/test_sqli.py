from src.detectors.sqli import detect_sql_injection_exposure


def test_sqli_payload_is_flagged():
    findings = detect_sql_injection_exposure("name=' OR '1'='1")
    assert len(findings) >= 1
    assert findings[0].detector == 'sqli'
    assert findings[0].severity == 'high'


def test_safe_payload_is_not_flagged():
    findings = detect_sql_injection_exposure("name=alex")
    assert findings == []
