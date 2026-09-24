from src.findings import make_finding


def test_finding_has_required_fields():
    finding = make_finding(
        detector='phishing',
        title='Suspicious URL',
        severity='medium',
        confidence='high',
        target='https://example.com',
        component='URL',
        description='A suspicious URL was detected',
        evidence='Contains suspicious pattern',
        recommendation='Verify the destination',
    )

    assert finding.detector == 'phishing'
    assert finding.title == 'Suspicious URL'
    assert finding.severity == 'medium'
    assert finding.confidence == 'high'
    assert finding.target == 'https://example.com'
    assert finding.status == 'open'
