from flask import Flask
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('data.db')
    conn.execute('CREATE TABLE IF NOT EXISTS visits (count INTEGER)')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO visits (count) VALUES (1)')
    conn.commit()

    count = cursor.execute('SELECT COUNT(*) FROM visits').fetchone()[0]
    conn.close()

    return f"Visits: {count}"

@app.route('/status')
def status():
    return {"status": "running"}

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)