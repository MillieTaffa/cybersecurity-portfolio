from src.risk import classify_severity, classify_confidence


def test_classify_severity():
    assert classify_severity(4) == 'critical'
    assert classify_severity(3) == 'high'
    assert classify_severity(2) == 'medium'
    assert classify_severity(1) == 'low'


def test_classify_confidence():
    assert classify_confidence(2) == 'high'
    assert classify_confidence(1) == 'medium'
    assert classify_confidence(0) == 'low'
