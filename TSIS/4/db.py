import psycopg2
from config import db_params

def get_db_connection():
    return psycopg2.connect(**db_params)

def get_personal_best(username):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT MAX(score) FROM game_sessions s
        JOIN players p ON s.player_id = p.id
        WHERE p.username = %s
    """, (username,))
    res = cur.fetchone()[0]
    cur.close()
    conn.close()
    return res if res else 0

def save_game_result(username, score, level):
    conn = get_db_connection()
    cur = conn.cursor()
    # Insert player if not exists
    cur.execute("INSERT INTO players (username) VALUES (%s) ON CONFLICT (username) DO NOTHING", (username,))
    cur.execute("SELECT id FROM players WHERE username = %s", (username,))
    player_id = cur.fetchone()[0]
    # Save session
    cur.execute("INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s, %s, %s)", 
                (player_id, score, level))
    conn.commit()
    cur.close()
    conn.close()

def get_leaderboard():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT p.username, s.score, s.level_reached, s.played_at 
        FROM game_sessions s 
        JOIN players p ON s.player_id = p.id 
        ORDER BY s.score DESC LIMIT 10
    """)
    res = cur.fetchall()
    cur.close()
    conn.close()
    return res
