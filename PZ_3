import sqlite3
import datetime

DB_NAME = "security_events.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS EventSources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            location TEXT,
            type TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS EventTypes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type_name TEXT UNIQUE,
            severity TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS SecurityEvents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            source_id INTEGER,
            event_type_id INTEGER,
            message TEXT,
            ip_address TEXT,
            username TEXT,
            FOREIGN KEY (source_id) REFERENCES EventSources(id),
            FOREIGN KEY (event_type_id) REFERENCES EventTypes(id)
        )
    ''')

    conn.commit()
    conn.close()

def populate_data():
    conn = get_connection()
    cursor = conn.cursor()

    event_types = [
        ("Login Success", "Informational"),
        ("Login Failed", "Warning"),
        ("Port Scan Detected", "Warning"),
        ("Malware Alert", "Critical"),
        ("System Failure", "Critical")
    ]

    for etype in event_types:
        cursor.execute("INSERT OR IGNORE INTO EventTypes (type_name, severity) VALUES (?, ?)", etype)

    sources = [
        ("Firewall_A", "192.168.1.1", "Firewall"),
        ("Web_Server_Logs", "192.168.1.2", "Web Server"),
        ("IDS_Sensor_B", "192.168.1.3", "IDS"),
        ("New_Firewall", "192.168.1.99", "Firewall")
    ]

    for source in sources:
        cursor.execute("INSERT OR IGNORE INTO EventSources (name, location, type) VALUES (?, ?, ?)", source)

    now = datetime.datetime.now()
    events = []
    for i in range(12):
        timestamp = (now - datetime.timedelta(hours=i * 2)).isoformat()

        if i % 4 == 0:
            events.append((timestamp, 1, 2, "User failed login attempt", "192.168.1.100", "admin"))
        elif i % 4 == 1:
            events.append((timestamp, 2, 1, "User logged in successfully", "192.168.1.105", "user1"))
        elif i % 4 == 2:
            events.append((timestamp, 3, 3, "Port scan detected", "192.168.1.50", None))
        else:
            events.append((timestamp, 1, 4, "Malware detected", "192.168.1.110", "user2"))

    cursor.executemany('''
        INSERT INTO SecurityEvents (timestamp, source_id, event_type_id, message, ip_address, username)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', events)

    conn.commit()
    conn.close()

def register_event_source(name, location, type_):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO EventSources (name, location, type) VALUES (?, ?, ?)", (name, location, type_))
    conn.commit()
    conn.close()

def register_event_type(type_name, severity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO EventTypes (type_name, severity) VALUES (?, ?)", (type_name, severity))
    conn.commit()
    conn.close()

def log_security_event(source_name, event_type_name, message, ip_address=None, username=None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM EventSources WHERE name = ?", (source_name,))
    res = cursor.fetchone()
    if not res:
        print(f"Source '{source_name}' not found.")
        conn.close()
        return
    source_id = res[0]

    cursor.execute("SELECT id FROM EventTypes WHERE type_name = ?", (event_type_name,))
    res = cursor.fetchone()
    if not res:
        print(f"Event type '{event_type_name}' not found.")
        conn.close()
        return
    event_type_id = res[0]

    timestamp = datetime.datetime.now().isoformat()
    cursor.execute('''
        INSERT INTO SecurityEvents (timestamp, source_id, event_type_id, message, ip_address, username)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (timestamp, source_id, event_type_id, message, ip_address, username))

    conn.commit()
    conn.close()

def get_failed_logins_last_24h():
    conn = get_connection()
    cursor = conn.cursor()

    last_24h = (datetime.datetime.now() - datetime.timedelta(hours=24)).isoformat()

    cursor.execute('''
        SELECT se.timestamp, es.name, se.ip_address, se.username
        FROM SecurityEvents se
        JOIN EventSources es ON se.source_id = es.id
        JOIN EventTypes et ON se.event_type_id = et.id
        WHERE et.type_name = 'Login Failed' AND se.timestamp >= ?
    ''', (last_24h,))

    results = cursor.fetchall()
    conn.close()
    return results

def detect_brute_force():
    conn = get_connection()
    cursor = conn.cursor()

    last_hour = (datetime.datetime.now() - datetime.timedelta(hours=1)).isoformat()

    cursor.execute('''
        SELECT ip_address, COUNT(*) as attempts
        FROM SecurityEvents se
        JOIN EventTypes et ON se.event_type_id = et.id
        WHERE et.type_name = 'Login Failed' AND se.timestamp >= ?
        GROUP BY ip_address
        HAVING COUNT(*) > 5
    ''', (last_hour,))

    results = cursor.fetchall()
    conn.close()
    return results

def get_critical_events_last_week():
    conn = get_connection()
    cursor = conn.cursor()

    last_week = (datetime.datetime.now() - datetime.timedelta(days=7)).isoformat()

    cursor.execute('''
        SELECT es.name, COUNT(*) as count
        FROM SecurityEvents se
        JOIN EventSources es ON se.source_id = es.id
        JOIN EventTypes et ON se.event_type_id = et.id
        WHERE et.severity = 'Critical' AND se.timestamp >= ?
        GROUP BY es.name
    ''', (last_week,))

    results = cursor.fetchall()
    conn.close()
    return results

def search_events_by_keyword(keyword):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT se.timestamp, es.name, et.type_name, se.message
        FROM SecurityEvents se
        JOIN EventSources es ON se.source_id = es.id
        JOIN EventTypes et ON se.event_type_id = et.id
        WHERE se.message LIKE ?
    ''', (f'%{keyword}%',))

    results = cursor.fetchall()
    conn.close()
    return results

def main():
    init_database()
    populate_data()

    register_event_source("New_Firewall", "192.168.1.99", "Firewall")
    register_event_type("System Failure", "Critical")
    log_security_event("Firewall_A", "Login Failed", "Suspicious login detected", "192.168.1.45", "hacker")

    print("== Login Failed за останні 24 години ==")
    for row in get_failed_logins_last_24h():
        print(row)

    print("\n== IP з >5 Failed Login за останню годину (потенційна атака) ==")
    for row in detect_brute_force():
        print(row)

    print("\n== Критичні події за останній тиждень (по джерелах) ==")
    for row in get_critical_events_last_week():
        print(row)

    print("\n== Події з ключовим словом 'login' ==")
    for row in search_events_by_keyword("login"):
        print(row)

if __name__ == "__main__":
    main()
