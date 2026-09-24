from src.detectors.phishing import detect_phishing_url


def test_normal_url_is_not_flagged():
    results = detect_phishing_url('https://example.com/login')
    assert results == []


def test_suspicious_url_is_flagged():
    results = detect_phishing_url('http://10.0.0.5/login?next=https://example.com%2Flogin')
    assert len(results) >= 1
    assert results[0].title == 'Suspicious URL characteristics detected'
