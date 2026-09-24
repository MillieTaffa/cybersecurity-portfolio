def format_report(findings, target="Local Security Lab"):
    report_lines = [
        "SentinelScanner Security Assessment Report",
        "=" * 42,
        f"Target: {target}",
        f"Findings: {len(findings)}",
        "",
    ]

    if not findings:
        report_lines.append("No findings detected.")
        return "\n".join(report_lines)

    for index, finding in enumerate(findings, start=1):
        report_lines.append(f"{index}. {finding.title}")
        report_lines.append(f"   Detector: {finding.detector}")
        report_lines.append(f"   Severity: {finding.severity}")
        report_lines.append(f"   Confidence: {finding.confidence}")
        report_lines.append(f"   Target: {finding.target}")
        report_lines.append(f"   Evidence: {finding.evidence}")
        report_lines.append(f"   Recommendation: {finding.recommendation}")
        report_lines.append("")

    return "\n".join(report_lines)
