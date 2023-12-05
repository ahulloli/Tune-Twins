import psycopg2
import creds
from ai_vocals import createAIVocals

def getAllSongs():
    # Connect to database
    conn = psycopg2.connect(
        host="hoarse-ray-6455.g8z.cockroachlabs.cloud", 
        port=26257,
        database="defaultdb", 
        user=f"{creds.cockroach_username}",
        password=f"{creds.cockroach_password}",
        sslmode="require" 
    )
    cur = conn.cursor()

    cur.execute("SELECT name FROM songs")
    all_songs = cur.fetchall()

    cur.close()
    conn.close()

    return all_songs

def getSong(song_name, artist_name):
    # Connect to database
    conn = psycopg2.connect(
        host="hoarse-ray-6455.g8z.cockroachlabs.cloud", 
        port=26257,
        database="defaultdb", 
        user=f"{creds.cockroach_username}",
        password=f"{creds.cockroach_password}",
        sslmode="require" 
    )
    cur = conn.cursor()

    cur.execute(
        f"SELECT link FROM songs WHERE song_name = '{song_name}'"
    )
    link = cur.fetchone()

    cur.execute(
        f"SELECT model FROM artists WHERE artist_name = '{artist_name}'"
    )
    model_name = cur.fetchone()

    cur.close()
    conn.close()

    if link == None:
        return "Error: Song not found"
    
    createAIVocals(link, song_name, model_name)


