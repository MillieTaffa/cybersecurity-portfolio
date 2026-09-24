from dataclasses import dataclass, asdict


@dataclass
class Finding:
    detector: str
    title: str
    severity: str
    confidence: str
    target: str
    component: str
    description: str
    evidence: str
    recommendation: str
    status: str = "open"

    def to_dict(self):
        return asdict(self)


def make_finding(
    detector,
    title,
    severity,
    confidence,
    target,
    component,
    description,
    evidence,
    recommendation,
    status="open",
):
    return Finding(
        detector=detector,
        title=title,
        severity=severity,
        confidence=confidence,
        target=target,
        component=component,
        description=description,
        evidence=evidence,
        recommendation=recommendation,
        status=status,
    )
