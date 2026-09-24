from src.findings import make_finding


def detect_configuration_issues(config, target='local-lab'):
    findings = []

    if config.get('debug') is True:
        findings.append(
            make_finding(
                detector='configuration',
                title='Debug mode enabled',
                severity='medium',
                confidence='high',
                target=target,
                component='application-settings',
                description='Debug mode is enabled, which can expose sensitive information and make troubleshooting easier for attackers.',
                evidence='Configuration key "debug" is set to True.',
                recommendation='Disable debug mode in production and keep verbose error output restricted to secure environments.',
                status='open',
            )
        )

    if config.get('https_only') is False:
        findings.append(
            make_finding(
                detector='configuration',
                title='HTTPS enforcement disabled',
                severity='high',
                confidence='high',
                target=target,
                component='transport-security',
                description='The application is configured to allow non-HTTPS traffic.',
                evidence='Configuration key "https_only" is set to False.',
                recommendation='Enforce HTTPS and redirect insecure requests to encrypted endpoints.',
                status='open',
            )
        )

    if config.get('authentication_required') is False:
        findings.append(
            make_finding(
                detector='configuration',
                title='Authentication is not required',
                severity='high',
                confidence='high',
                target=target,
                component='access-control',
                description='The application appears to allow access without authentication.',
                evidence='Configuration key "authentication_required" is set to False.',
                recommendation='Require authentication for sensitive endpoints and enforce access control policies.',
                status='open',
            )
        )

    return findings
