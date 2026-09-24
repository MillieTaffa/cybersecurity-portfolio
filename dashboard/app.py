import streamlit as st

from src.database import initialise_db, connect_db
from src.reporting import format_report


st.set_page_config(page_title='SentinelScanner Dashboard', layout='wide')

initialise_db()

st.title('SentinelScanner Dashboard')
st.caption('Security assessment results from the local lab and controlled detections.')

conn = connect_db()
scans = conn.execute('SELECT * FROM scans ORDER BY id DESC').fetchall()
conn.close()

if not scans:
    st.info('No scans have been stored yet. Run the scanner to create findings.')
    st.stop()

latest_scan = scans[0]

col1, col2, col3 = st.columns(3)
col1.metric('Target', latest_scan['target'])
col2.metric('Status', latest_scan['status'])
col3.metric('Scan ID', latest_scan['id'])

st.subheader('Latest scan summary')

conn = connect_db()
findings = conn.execute(
    'SELECT * FROM findings WHERE scan_id = ? ORDER BY id',
    (latest_scan['id'],)
).fetchall()
conn.close()

if findings:
    st.write(format_report([
        type('FindingStub', (), {
            'title': row['title'],
            'detector': row['detector'],
            'severity': row['severity'],
            'confidence': row['confidence'],
            'target': row['target'],
            'evidence': row['evidence'],
            'recommendation': row['recommendation'],
        })() for row in findings
    ], latest_scan['target']))

    st.dataframe([
        {
            'Detector': row['detector'],
            'Title': row['title'],
            'Severity': row['severity'],
            'Confidence': row['confidence'],
            'Status': row['status'],
        }
        for row in findings
    ])
else:
    st.warning('This scan has no findings yet.')

st.subheader('Previous scan history')
for scan in scans:
    st.write(f"Scan {scan['id']}: {scan['target']} | status: {scan['status']}")
