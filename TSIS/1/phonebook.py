import psycopg2
import json
import csv
from connect import get_connection

def export_to_json(filename):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name as group_name,
               json_agg(json_build_object('phone', p.phone, 'type', p.type)) as phones
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        GROUP BY c.id, g.name
    """)
    data = cur.fetchall()
    
    results = []
    for row in data:
        results.append({
            "name": row[0], "email": row[1], 
            "birthday": str(row[2]) if row[2] else None,
            "group": row[3], "phones": row[4]
        })
    
    with open(filename, 'w') as f:
        json.dump(results, f, indent=4)
    cur.close()
    conn.close()

def import_from_json(filename):
    conn = get_connection()
    cur = conn.cursor()
    with open(filename, 'r') as f:
        contacts = json.load(f)
        
    for c in contacts:
        cur.execute("SELECT id FROM contacts WHERE name = %s", (c['name'],))
        exists = cur.fetchone()
        
        if exists:
            choice = input(f"Contact {c['name']} exists. Skip or Overwrite? (s/o): ").lower()
            if choice == 's': continue
            cur.execute("DELETE FROM contacts WHERE name = %s", (c['name'],))

        # Insert group and get ID
        cur.execute("INSERT INTO groups (name) VALUES (%s) ON CONFLICT (name) DO UPDATE SET name=EXCLUDED.name RETURNING id", (c['group'],))
        g_id = cur.fetchone()[0]
        
        # Insert contact
        cur.execute("INSERT INTO contacts (name, email, birthday, group_id) VALUES (%s, %s, %s, %s) RETURNING id", 
                    (c['name'], c['email'], c['birthday'], g_id))
        c_id = cur.fetchone()[0]
        
        # Insert phones
        for p in c['phones']:
            cur.execute("INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)", (c_id, p['phone'], p['type']))
            
    conn.commit()
    cur.close()
    conn.close()

def paginated_view(filter_group=None, sort_by="name"):
    conn = get_connection()
    cur = conn.cursor()
    limit = 5
    offset = 0
    
    while True:
        query = f"""
            SELECT c.name, c.email, g.name 
            FROM contacts c 
            LEFT JOIN groups g ON c.group_id = g.id
            WHERE (%s IS NULL OR g.name = %s)
            ORDER BY {sort_by}
            LIMIT %s OFFSET %s
        """
        cur.execute(query, (filter_group, filter_group, limit, offset))
        rows = cur.fetchall()
        
        print(f"\n--- Page {(offset//limit)+1} ---")
        for r in rows: print(f"{r[0]} | {r[1]} | {r[2]}")
        
        cmd = input("\n[n]ext, [p]rev, [q]uit: ").lower()
        if cmd == 'n': offset += limit
        elif cmd == 'p': offset = max(0, offset - limit)
        elif cmd == 'q': break

if __name__ == "__main__":
    # Example usage:
    # export_to_json('contacts.json')
    # import_from_json('contacts.json')
    paginated_view(sort_by="birthday")
