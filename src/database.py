import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / 'database' / 'sentinelscanner.db'
SCHEMA_PATH = Path(__file__).resolve().parents[1] / 'database' / 'schema.sql'


def initialise_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute('PRAGMA foreign_keys = ON')
    schema_sql = SCHEMA_PATH.read_text(encoding='utf-8')
    conn.executescript(schema_sql)
    conn.commit()
    conn.close()


def connect_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def save_scan(target, status='open'):
    initialise_db()
    conn = connect_db()
    cursor = conn.execute(
        'INSERT INTO scans (target, started_at, completed_at, status) VALUES (?, datetime("now"), NULL, ?)',
        (target, status)
    )
    scan_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return scan_id


def save_finding(scan_id, finding):
    conn = connect_db()
    conn.execute(
        '''
        INSERT INTO findings (
            scan_id, detector, title, severity, confidence, target,
            component, description, evidence, recommendation, status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (
            scan_id,
            finding.detector,
            finding.title,
            finding.severity,
            finding.confidence,
            finding.target,
            finding.component,
            finding.description,
            finding.evidence,
            finding.recommendation,
            finding.status,
        ),
    )
    conn.commit()
    conn.close()


def get_findings_by_scan(scan_id):
    conn = connect_db()
    rows = conn.execute(
        'SELECT * FROM findings WHERE scan_id = ? ORDER BY id',
        (scan_id,)
    ).fetchall()
    conn.close()
    return rows


def get_latest_scan_id():
    conn = connect_db()
    row = conn.execute('SELECT MAX(id) AS id FROM scans').fetchone()
    conn.close()
    return row['id'] if row and row['id'] is not None else None
