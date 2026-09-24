CREATE TABLE IF NOT EXISTS scans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    target TEXT NOT NULL,
    started_at TEXT NOT NULL,
    completed_at TEXT,
    status TEXT NOT NULL DEFAULT 'open'
);

CREATE TABLE IF NOT EXISTS findings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scan_id INTEGER NOT NULL,
    detector TEXT NOT NULL,
    title TEXT NOT NULL,
    severity TEXT NOT NULL,
    confidence TEXT NOT NULL,
    target TEXT NOT NULL,
    component TEXT NOT NULL,
    description TEXT NOT NULL,
    evidence TEXT NOT NULL,
    recommendation TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'open',
    FOREIGN KEY (scan_id) REFERENCES scans(id)
);
