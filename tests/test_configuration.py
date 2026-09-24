from src.detectors.configuration import detect_configuration_issues


def test_insecure_configuration_is_flagged():
    findings = detect_configuration_issues({
        'debug': True,
        'https_only': False,
        'authentication_required': False,
    })
    assert len(findings) >= 3


def test_secure_configuration_is_not_flagged():
    findings = detect_configuration_issues({
        'debug': False,
        'https_only': True,
        'authentication_required': True,
    })
    assert findings == []
